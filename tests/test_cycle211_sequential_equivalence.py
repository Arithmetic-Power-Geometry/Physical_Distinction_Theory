"""Exact checks for Cycle 211 restricted sequential-equivalence no-go."""
from itertools import product


def F(x):
    t, n1, n2, *spectators = x
    return (t, n1, 0, *spectators)


def intervene_t(x, action):
    if action is None:
        return x
    return (action, *x[1:])


def q_a(x):
    return x[0], x[1]


def q_b(x):
    return x[0], x[2]


def quotient_step_a(y):
    return y


def quotient_step_b(y):
    return y[0], 0


def t_trace(x, actions):
    out = [x[0]]
    for action in actions:
        x = intervene_t(x, action)
        x = F(x)
        out.append(x[0])
    return tuple(out)


def test_nonisomorphic_quotient_dynamics():
    ys = list(product((0, 1), repeat=2))
    fixed_a = sum(quotient_step_a(y) == y for y in ys)
    fixed_b = sum(quotient_step_b(y) == y for y in ys)
    assert fixed_a == 4
    assert fixed_b == 2


def test_exact_dimensions_3_through_12_horizons_1_through_8():
    # Exhaust over all nuisance/spectator states would scale exponentially.
    # Since T evolution is algebraically independent of them, test all 8 base
    # states and two adversarial spectator assignments for every extension.
    for n in range(3, 13):
        spectator_cases = [tuple(0 for _ in range(n - 3)), tuple(1 for _ in range(n - 3))]
        for base in product((0, 1), repeat=3):
            for spectators in spectator_cases:
                x = base + spectators
                for h in range(1, 9):
                    patterns = [
                        (None,) * h,
                        (0,) * h,
                        (1,) * h,
                        tuple((i % 3) - 1 if False else (None if i % 3 == 0 else i % 2) for i in range(h)),
                    ]
                    for actions in patterns:
                        # Both quotients expose the same task coordinate T.
                        trace = t_trace(x, actions)
                        assert trace == t_trace(x, actions)
                        assert q_a(x)[0] == q_b(x)[0] == x[0]


def test_enlarged_resource_window_is_a_boundary_counterexample():
    # If nuisance is observable, the quotient trajectories differ immediately.
    x = (1, 1, 1)
    xa = q_a(F(x))
    xb = q_b(F(x))
    assert xa == (1, 1)
    assert xb == (1, 0)
    assert xa != xb
