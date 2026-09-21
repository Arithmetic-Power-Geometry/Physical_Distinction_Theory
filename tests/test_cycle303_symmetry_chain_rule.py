import math


def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))


def jeffreys(p, q):
    return kl(p, q) + kl(q, p)


def joint(px, cond):
    return [px[x] * cond[x][y] for x in range(len(px)) for y in range(len(cond[x]))]


def test_cycle303_exact_defect_formula():
    px = [3/4, 1/4]
    qx = [1/4, 3/4]
    pc = [[3/4, 1/4], [1/2, 1/2]]
    qc = [[1/2, 1/2], [1/2, 1/2]]
    pxy, qxy = joint(px, pc), joint(qx, qc)

    lhs = jeffreys(pxy, qxy)
    proposed = jeffreys(px, qx) + sum(
        px[x] * jeffreys(pc[x], qc[x]) for x in range(2)
    )
    defect = lhs - proposed
    exact_target = -0.25 * math.log(4/3)

    assert abs(defect - exact_target) < 1e-12
    assert abs(defect) > 1e-6


def test_correct_two_weight_chain_rule():
    px = [3/4, 1/4]
    qx = [1/4, 3/4]
    pc = [[3/4, 1/4], [1/2, 1/2]]
    qc = [[1/2, 1/2], [1/2, 1/2]]
    pxy, qxy = joint(px, pc), joint(qx, qc)

    rhs = jeffreys(px, qx)
    rhs += sum(px[x] * kl(pc[x], qc[x]) for x in range(2))
    rhs += sum(qx[x] * kl(qc[x], pc[x]) for x in range(2))
    assert abs(jeffreys(pxy, qxy) - rhs) < 1e-12
