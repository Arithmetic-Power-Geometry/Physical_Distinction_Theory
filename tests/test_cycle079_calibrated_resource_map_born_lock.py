import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "cycle079_calibrated_resource_map_born_lock.py"
spec = importlib.util.spec_from_file_location("cycle079", MODULE_PATH)
cycle079 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(cycle079)


def test_cycle079_regression_errors_small():
    r = cycle079.run_audit()
    assert r["max_effect_additivity_error"] < 1e-12
    assert r["max_preparation_mixing_error"] < 1e-12
    assert r["max_identity_calibration_error"] < 1e-12


def test_cycle079_nonidentity_candidates_fail_calibration_above_d1():
    r = cycle079.run_audit()
    # 16 nondegenerate dimensions x 5 repetitions = 80 failures expected
    assert r["calibration_failures"]["identity"] == 0
    assert r["calibration_failures"]["depolarizing"] == 80
    assert r["calibration_failures"]["transpose"] == 80
    assert r["calibration_failures"]["unitary"] == 80


def test_cycle079_d1_is_degenerate():
    r = cycle079.run_audit()
    d1 = next(x for x in r["per_dimension"] if x["d"] == 1)
    assert all(v == 0 for v in d1["calibration_failures"].values())
