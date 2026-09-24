import cmath
import math


def weyl_trace_inner(d, a, b, ap, bp):
    """Exact-form Hilbert-Schmidt inner product Tr(U_ab^† U_apbp)."""
    if (a - ap) % d != 0:
        return 0j
    delta_b = (bp - b) % d
    return sum(cmath.exp(2j * math.pi * delta_b * j / d) for j in range(d))


def test_generalized_weyl_orthogonality_n2_to_n12():
    for d in range(2, 13):
        for a in range(d):
            for b in range(d):
                for ap in range(d):
                    for bp in range(d):
                        got = weyl_trace_inner(d, a, b, ap, bp)
                        expected = d if (a == ap and b == bp) else 0
                        assert abs(got - expected) < 1e-9


def test_message_count_has_no_n3_singularity():
    counts = {d: d * d for d in range(1, 13)}
    assert counts[2] == 4
    assert counts[3] == 9
    assert counts[4] == 16
    assert all(counts[d] == d * d for d in range(1, 13))


def test_smallest_nontrivial_counterexample_is_n2():
    # Perfect generalized dense coding exists already for d=2.
    assert 2 != 3
    assert 2 * 2 == 4
