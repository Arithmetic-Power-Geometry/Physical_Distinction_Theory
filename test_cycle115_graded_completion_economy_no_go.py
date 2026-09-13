from fractions import Fraction
import cycle115_graded_completion_economy_no_go as c115


def test_small_dimensions_exact():
    assert c115.carrier_dimensions(1) == {
        "full_exterior_or_clifford": 2,
        "even_clifford": 1,
        "scalar_vector_bivector": 2,
        "vector_bivector": 1,
    }
    assert c115.carrier_dimensions(2)["full_exterior_or_clifford"] == 4
    assert c115.carrier_dimensions(3)["scalar_vector_bivector"] == 7


def test_full_completion_minimizers():
    out = c115.minimizers(128)
    assert out["full_exterior_or_clifford"] == {"minimum": "2", "n": [1, 2]}
    assert out["even_clifford"] == {"minimum": "1", "n": [1, 2]}


def test_truncated_completion_minimizers():
    out = c115.minimizers(128)
    assert out["scalar_vector_bivector"] == {"minimum": "2", "n": [1, 2]}
    assert out["vector_bivector"] == {"minimum": "1", "n": [1]}


def test_n3_is_not_a_minimizer():
    costs = c115.relative_overheads(3)
    assert costs["full_exterior_or_clifford"] == Fraction(8, 3)
    assert costs["scalar_vector_bivector"] == Fraction(7, 3)
    assert costs["vector_bivector"] == Fraction(2, 1)
    assert costs["full_exterior_or_clifford"] > c115.relative_overheads(2)["full_exterior_or_clifford"]


def test_exact_theorem_checks_and_stress_dimensions():
    assert all(c115.theorem_checks(128).values())
    rows = c115.exact_stress_table()
    assert [row["n"] for row in rows] == list(c115.STRESS_DIMS)
    assert set(range(1, 13)).issubset({row["n"] for row in rows})


def test_invalid_dimensions_rejected():
    import pytest
    with pytest.raises(ValueError):
        c115.carrier_dimensions(0)
    with pytest.raises(ValueError):
        c115.minimizers(0)
