"""Regression checks for PDT-II cycle 365 local-tomography no-go."""


def k_complex(n: int) -> int:
    return n * n


def k_real(n: int) -> int:
    return n * (n + 1) // 2


def test_complex_local_tomography_equal_dimensions_n1_n12():
    for n in range(1, 13):
        assert k_complex(n * n) == k_complex(n) ** 2


def test_complex_local_tomography_rectangular_n1_n12():
    for n in range(1, 13):
        for m in range(1, 13):
            assert k_complex(n * m) == k_complex(n) * k_complex(m)


def test_n2_is_nontrivial_counterexample_to_n3_selection():
    n = 2
    assert n != 3
    assert k_complex(n * n) == k_complex(n) ** 2


def test_n4_defeats_uniqueness_above_three():
    n = 4
    assert n != 3
    assert k_complex(n * n) == k_complex(n) ** 2


def test_real_qm_smallest_nontrivial_equal_dimension_failure():
    assert k_real(1) == 1
    assert k_real(1 * 1) == k_real(1) ** 2
    assert k_real(2 * 2) == 10
    assert k_real(2) ** 2 == 9
    assert k_real(2 * 2) != k_real(2) ** 2


def test_real_qm_defect_positive_n2_n12():
    for n in range(2, 13):
        assert k_real(n * n) - k_real(n) ** 2 > 0
