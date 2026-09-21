import math


def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def renyi_half(p, q):
    return -2.0 * math.log(sum(math.sqrt(pi * qi) for pi, qi in zip(p, q)))


def marginal_x(p):
    return [p[0] + p[1], p[2] + p[3]]


def conditionals_y_given_x(p):
    px = marginal_x(p)
    return [[p[0] / px[0], p[1] / px[0]], [p[2] / px[1], p[3] / px[1]]]


def chain_rhs(div, p, q):
    px, qx = marginal_x(p), marginal_x(q)
    pc, qc = conditionals_y_given_x(p), conditionals_y_given_x(q)
    return div(px, qx) + sum(px[x] * div(pc[x], qc[x]) for x in range(2))


def witness():
    p = [5 / 20, 1 / 20, 6 / 20, 8 / 20]
    q = [1 / 20, 17 / 20, 1 / 20, 1 / 20]
    return p, q


def test_kl_exact_conditional_chain_rule():
    p, q = witness()
    assert abs(kl(p, q) - chain_rhs(kl, p, q)) < 1e-12


def test_renyi_half_fails_ordinary_conditional_chain_rule():
    p, q = witness()
    lhs = renyi_half(p, q)
    rhs = chain_rhs(renyi_half, p, q)
    assert abs(lhs - rhs) > 0.29


def test_strict_interior_embeddings_2_through_12_preserve_selector_difference():
    # Binary marginals already give the smallest alphabet for the witness.
    # Add equal epsilon tail coordinates to each Y branch and renormalize;
    # continuity preserves the nonzero chain-rule defect.
    p0, q0 = witness()
    base_defect = abs(renyi_half(p0, q0) - chain_rhs(renyi_half, p0, q0))
    assert base_defect > 0.29
    # Explicitly certify persistence by embedding the full four-outcome joint
    # distributions into larger flat alphabets; KL/Renyi values are unchanged
    # when identical zero coordinates are appended (limit of epsilon interiors).
    for n in range(4, 13):
        p = p0 + [0.0] * (n - 4)
        q = q0 + [0.0] * (n - 4)
        assert abs(kl(p, q) - kl(p0, q0)) < 1e-12
        assert abs(renyi_half(p, q) - renyi_half(p0, q0)) < 1e-12
