import numpy as np
from src.pdt.cycle143_equal_split_no_go import variance_term, resource, equal_split, audit


def test_exact_witness():
    x = np.array([1.0, 2.0])
    assert variance_term(x) == 4.5
    assert resource(x, 0.0) == 5.0
    assert resource(x, 1.0) == 9.5


def test_all_equal_splits_conserved():
    for k in range(1, 13):
        for r in [0.0, 0.1, 1.0, 7.25]:
            for eps in [0.0, 0.01, 0.1, 1.0]:
                assert np.isclose(resource(equal_split(r, k), eps), r*r)


def test_variance_nonnegative():
    rng = np.random.default_rng(143)
    for n in range(2, 13):
        for _ in range(100):
            assert variance_term(rng.normal(size=n)) >= -1e-10


def test_audit_has_no_equal_split_failures():
    result = audit()
    assert result["equal_split_failures"] == 0
    assert result["unequal_random_differences"] > 0
