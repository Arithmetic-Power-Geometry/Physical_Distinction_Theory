import math

import numpy as np

from pdt_tsirelson_composite_nonuniqueness import (
    audit_dimension,
    canonical_chsh_witness,
    chsh_value,
    in_c_cap,
    in_c_op,
    nuclear_norm,
    op_norm,
    product_correlator,
    random_orthogonal,
)


def test_distinct_bodies_start_at_n3():
    assert in_c_op(np.eye(2))
    assert in_c_cap(np.eye(2))
    for n in range(3, 13):
        I = np.eye(n)
        assert in_c_op(I)
        assert not in_c_cap(I)
        assert abs(nuclear_norm(I) - n) < 1e-12


def test_same_tsirelson_chsh_witness_n2_to_n12():
    target = 2.0 * math.sqrt(2.0)
    for n in range(2, 13):
        W = canonical_chsh_witness(n)
        assert in_c_op(W)
        assert in_c_cap(W)
        assert abs(op_norm(W) - 1.0) < 1e-12
        assert abs(nuclear_norm(W) - 2.0) < 1e-12
        assert abs(chsh_value(W) - target) < 1e-12


def test_all_product_correlators_are_in_both_bodies():
    rng = np.random.default_rng(4242)
    for n in range(2, 13):
        for _ in range(100):
            a = rng.normal(size=n)
            b = rng.normal(size=n)
            a /= max(1.0, np.linalg.norm(a))
            b /= max(1.0, np.linalg.norm(b))
            P = product_correlator(a, b)
            assert in_c_op(P)
            assert in_c_cap(P)


def test_local_orthogonal_invariance():
    rng = np.random.default_rng(4343)
    for n in range(2, 13):
        W = canonical_chsh_witness(n)
        op0 = op_norm(W)
        nuc0 = nuclear_norm(W)
        for _ in range(20):
            U = random_orthogonal(n, rng)
            V = random_orthogonal(n, rng)
            R = U @ W @ V.T
            assert abs(op_norm(R) - op0) < 1e-10
            assert abs(nuclear_norm(R) - nuc0) < 1e-10
            assert in_c_cap(R)


def test_audit_has_no_product_failures():
    for n in range(2, 13):
        row = audit_dimension(n, random_trials=20, seed=99)
        assert row["product_failures"] == 0
        assert row["witness_in_c_cap"]
        assert abs(row["chsh_value"] - row["chsh_target"]) < 1e-12
        if n >= 3:
            assert row["bodies_distinct"]
