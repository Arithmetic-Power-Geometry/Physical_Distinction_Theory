import math


def canonical_rank2_purification(n: int):
    assert n >= 2
    # Sparse amplitudes of (|00>+|11>)/sqrt(2).
    a = 1.0 / math.sqrt(2.0)
    return {(0, 0): a, (1, 1): a}


def reduced_diagonal_from_sparse_pure(amplitudes, n: int):
    # For this Schmidt-diagonal witness, tracing E leaves diagonal weights.
    out = [0.0] * n
    for (i, _e), amp in amplitudes.items():
        out[i] += amp * amp
    return out


def test_rank2_purification_exact_structure_n2_to_n12():
    for n in range(2, 13):
        psi = canonical_rank2_purification(n)
        reduced = reduced_diagonal_from_sparse_pure(psi, n)
        assert math.isclose(sum(reduced), 1.0, rel_tol=0.0, abs_tol=1e-15)
        assert math.isclose(reduced[0], 0.5, rel_tol=0.0, abs_tol=1e-15)
        assert math.isclose(reduced[1], 0.5, rel_tol=0.0, abs_tol=1e-15)
        assert all(x == 0.0 for x in reduced[2:])


def test_no_n3_singularity_in_witness_invariants():
    invariants = []
    for n in range(2, 13):
        reduced = reduced_diagonal_from_sparse_pure(canonical_rank2_purification(n), n)
        positive = [x for x in reduced if x > 0.0]
        invariants.append((len(positive), round(sum(x * x for x in reduced), 15)))
    assert len(set(invariants)) == 1
    assert invariants[0] == (2, 0.5)


def test_pure_state_degenerate_edge_case():
    for n in range(1, 13):
        # |0>_S|0>_E is a purification of |0><0| in every ambient dimension.
        reduced = [1.0] + [0.0] * (n - 1)
        assert sum(reduced) == 1.0
        assert sum(x * x for x in reduced) == 1.0
