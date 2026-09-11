import importlib.util
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "cycle075", ROOT / "cycle075_quadratic_product_composition.py"
)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def test_product_composition_audit_has_no_failures():
    result = MOD.run_audit(seed=75011)
    assert result["failures"] == 0
    assert result["cases"] == 1480
    assert result["max_abs_product_error"] < 1e-12


def test_exact_two_qubit_negative_residual_witness():
    assert MOD.exact_negative_residual(2) == Fraction(-56, 625)


def test_residual_is_sign_indefinite_from_dimension_two_up():
    for n in list(range(2, 13)) + [16, 24, 32, 48, 64, 96, 128]:
        assert MOD.exact_negative_residual(n) < 0
        assert MOD.exact_positive_residual(n) > 0


def test_dimension_one_is_degenerate():
    assert MOD.exact_negative_residual(1) == 0
    assert MOD.exact_positive_residual(1) == 0
