"""Cycle 246: exact finite checks for the transitivity + local-tomography selector no-go.

This is deliberately a structural regression test, not a simulation of nature.
Two established finite-dimensional theories are compared:
  C_n: classical n-level simplex, K=n, reversible group S_n;
  Q_n: complex n-level quantum theory, K=n^2, reversible unitary group U(n).
Both are locally tomographic under their standard tensor products and their
reversible groups act transitively on pure states.  Therefore these principles
do not select a unique state-space/composition theory and do not select n=3.
"""


def classical_K(n: int) -> int:
    assert n >= 1
    return n


def quantum_K(n: int) -> int:
    assert n >= 1
    return n * n


def check_local_tomography_scaling(K, a: int, b: int) -> bool:
    # Standard locally tomographic composites obey K_AB=K_A K_B.
    return K(a * b) == K(a) * K(b)


def run_exact_window(lo: int = 1, hi: int = 12) -> None:
    for n in range(lo, hi + 1):
        assert classical_K(n) >= 1
        assert quantum_K(n) >= 1
        # Pure-state transitivity is analytic/group-theoretic, not inferred here:
        # S_n maps any simplex vertex to any other; U(n) maps any unit vector/ray
        # to any other.  These flags prevent pretending a numerical proof.
        classical_transitivity_analytic = True
        quantum_transitivity_analytic = True
        assert classical_transitivity_analytic and quantum_transitivity_analytic

    for a in range(lo, hi + 1):
        for b in range(lo, hi + 1):
            assert check_local_tomography_scaling(classical_K, a, b)
            assert check_local_tomography_scaling(quantum_K, a, b)

    # The candidate principles admit n=2,3,4,... in both families.
    admissible_classical = list(range(lo, hi + 1))
    admissible_quantum = list(range(lo, hi + 1))
    assert 3 in admissible_classical and 3 in admissible_quantum
    assert any(n != 3 for n in admissible_classical)
    assert any(n != 3 for n in admissible_quantum)

    # The two theories are already inequivalent for n>=2 by parameter count.
    for n in range(max(2, lo), hi + 1):
        assert classical_K(n) != quantum_K(n)


if __name__ == "__main__":
    run_exact_window()
    print("PASS: n=1..12; classical and complex-quantum survivor families remain distinct.")
