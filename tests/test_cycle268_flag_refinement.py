"""Exact regression for Cycle 268 flag-refinement selector no-go.

We use diagonal probability vectors so Shannon entropy equals von Neumann
entropy exactly at the structural level.  The test verifies the block/direct-
sum chain rule numerically for n=1..12, including degenerate distributions.
The analytic proof is recorded in CYCLE268_FLAG_REFINEMENT_SELECTOR_NO_GO.md.
"""
import math


def H(p):
    return -sum(x * math.log(x) for x in p if x > 0.0)


def flagged_distribution(weights, conditionals):
    return [w * x for w, q in zip(weights, conditionals) for x in q]


def test_flag_entropy_chain_rule_n1_to_n12():
    weights = [0.25, 0.75]
    for n in range(1, 13):
        # Include a pure/degenerate branch and a full-support branch.
        q0 = [1.0] + [0.0] * (n - 1)
        q1 = [1.0 / n] * n
        joint = flagged_distribution(weights, [q0, q1])
        lhs = H(joint)
        rhs = H(weights) + sum(w * H(q) for w, q in zip(weights, [q0, q1]))
        assert math.isclose(lhs, rhs, rel_tol=0.0, abs_tol=1e-12)


def test_all_dimensions_survive_candidate():
    survivors = []
    for n in range(1, 13):
        weights = [0.5, 0.5]
        q = [1.0 / n] * n
        lhs = H(flagged_distribution(weights, [q, q]))
        rhs = H(weights) + H(q)
        if math.isclose(lhs, rhs, rel_tol=0.0, abs_tol=1e-12):
            survivors.append(n)
    assert survivors == list(range(1, 13))
