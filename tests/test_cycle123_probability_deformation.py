from fractions import Fraction
from src.pdt.cycle123_probability_deformation import power_deform, exact_alpha2_witness, randomized_affinity_audit


def test_exact_alpha2_witness():
    w = exact_alpha2_witness()
    assert w["qmix"] == Fraction(1,4)
    assert w["lhs"] == Fraction(1,10)
    assert w["rhs"] == Fraction(1,4)
    assert w["residual"] == Fraction(-3,20)


def test_identity_is_affine():
    a = randomized_affinity_audit(1.0, trials=500)
    assert a["violations"] == 0


def test_power_deformation_breaks_affinity():
    for alpha in (0.5, 2.0, 3.0):
        a = randomized_affinity_audit(alpha, trials=500)
        assert a["violations"] > 0


def test_certainty_endpoints():
    for alpha in (0.5,1.0,2.0,3.0):
        assert power_deform(0.0,alpha) == 0.0
        assert power_deform(1.0,alpha) == 1.0
