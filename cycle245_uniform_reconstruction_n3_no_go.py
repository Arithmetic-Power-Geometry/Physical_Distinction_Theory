"""Cycle 245: exact regression for dimension-uniform reconstruction blindness.

This is not a physics simulation.  It verifies the finite-window consequence of the
proved logical point: once a reconstruction law K(N)=N**r is imposed uniformly in
N, its defining residuals vanish for every admissible N, so they cannot select N=3.
"""


def residuals(n: int, r: int) -> tuple[int, int, int]:
    assert n >= 1 and r >= 1
    k = lambda x: x ** r
    unit = k(1) - 1
    monotonicity_slack = k(n + 1) - k(n)  # must be > 0
    # Use a nontrivial composite partner n+1.
    multiplicativity = k(n * (n + 1)) - k(n) * k(n + 1)
    return unit, monotonicity_slack, multiplicativity


def test_uniform_power_laws_n1_to_n12() -> None:
    for r in range(1, 9):
        for n in range(1, 13):
            unit, slack, mult = residuals(n, r)
            assert unit == 0
            assert slack > 0
            assert mult == 0


def test_quantum_scaling_does_not_single_out_three() -> None:
    # r=2 is the familiar complex-quantum parameter scaling K=N^2.
    survivors = []
    for n in range(1, 13):
        unit, slack, mult = residuals(n, 2)
        if unit == 0 and slack > 0 and mult == 0:
            survivors.append(n)
    assert survivors == list(range(1, 13))
    assert survivors != [3]


if __name__ == "__main__":
    test_uniform_power_laws_n1_to_n12()
    test_quantum_scaling_does_not_single_out_three()
    print("cycle245 exact checks passed for n=1..12, r=1..8")
