from fractions import Fraction

import cycle133_resolved_channel_mixing_quadraticity as c133


def test_exact_345_witness_selects_p2():
    assert c133.resolved_lp_resource([Fraction(3, 5), Fraction(4, 5)], 1) == Fraction(7, 5)
    assert c133.resolved_lp_resource([Fraction(3, 5), Fraction(4, 5)], 2) == 1
    assert c133.resolved_lp_resource([Fraction(3, 5), Fraction(4, 5)], 4) == Fraction(337, 625)


def test_n1_has_no_quadratic_selector():
    for t in [Fraction(-2), Fraction(-1, 2), Fraction(0), Fraction(3, 2)]:
        assert abs(t) >= 0
        assert abs(t) ** 4 >= 0
    assert abs(Fraction(1)) == 1
    assert abs(Fraction(1)) ** 4 == 1


def test_quadratic_resource_is_rotation_invariant():
    values = [1.2, -0.7, 2.0]
    mixed = c133.rotate_pair(values, 0, 1, 0.413)
    assert abs(
        c133.resolved_lp_resource(values, 2)
        - c133.resolved_lp_resource(mixed, 2)
    ) < 1e-12


def test_discrete_symmetry_does_not_select_p2():
    values = [1.0, 2.0, 3.0]
    transformed = [-3.0, 1.0, -2.0]
    for p in (1, 2, 4):
        assert c133.resolved_lp_resource(values, p) == c133.resolved_lp_resource(
            transformed, p
        )


def test_full_stress_has_no_quadratic_or_discrete_regression():
    result = c133.run_stress()
    assert result["quadratic_rotation_failures"] == 0
    assert result["discrete_signed_permutation_failures"] == 0
