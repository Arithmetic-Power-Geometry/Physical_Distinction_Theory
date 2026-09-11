import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "cycle074", ROOT / "cycle074_quadratic_revelation_conservation.py"
)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def test_quadratic_revelation_audit_has_no_failures():
    result = MOD.run_audit(seed=74011)
    assert result["failures"] == 0
    assert result["cases"] == 1480
    assert result["max_abs_telescoping_error"] < 1e-10


def test_lp_two_is_unique_on_two_coordinate_witness():
    result = MOD.run_audit(seed=74011)
    gaps = result["lp_witness"]
    assert abs(gaps["2.0"]["gap"]) < 1e-15
    for key, row in gaps.items():
        if key != "2.0":
            assert abs(row["gap"]) > 1e-6
