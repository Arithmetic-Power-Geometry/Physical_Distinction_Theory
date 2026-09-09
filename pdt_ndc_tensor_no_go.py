"""Cycle 031: tensor-closure no-go for universal Normed Distinction Composition (NDC).

The mathematical input is the classical classification of nontrivial real Euclidean
binary vector cross products: dimensions 3 and 7 only.  This module does not claim
that classification as PDT novelty.
"""

NONTRIVIAL_NDC_DIMS = frozenset({3, 7})
TRIVIAL_OR_NDC_DIMS = frozenset({1, 3, 7})


def tensor_dimension(n: int, m: int) -> int:
    if n < 1 or m < 1:
        raise ValueError("dimensions must be positive integers")
    return int(n) * int(m)


def admits_nontrivial_ndc(n: int) -> bool:
    return int(n) in NONTRIVIAL_NDC_DIMS


def admits_ndc_allowing_trivial(n: int) -> bool:
    return int(n) in TRIVIAL_OR_NDC_DIMS


def tensor_pair_row(n: int, m: int) -> dict:
    nm = tensor_dimension(n, m)
    return {
        "n": int(n),
        "m": int(m),
        "tensor_dimension": nm,
        "n_nontrivial_ndc": admits_nontrivial_ndc(n),
        "m_nontrivial_ndc": admits_nontrivial_ndc(m),
        "tensor_nontrivial_ndc": admits_nontrivial_ndc(nm),
        "universal_ndc_closed": (
            admits_nontrivial_ndc(n)
            and admits_nontrivial_ndc(m)
            and admits_nontrivial_ndc(nm)
        ),
    }


def self_tensor_row(n: int) -> dict:
    row = tensor_pair_row(n, n)
    row["local_ndc_class"] = (
        "NONTRIVIAL" if admits_nontrivial_ndc(n)
        else "TRIVIAL" if n == 1
        else "FORBIDDEN_BY_CLASSIFICATION"
    )
    row["self_tensor_ndc_class"] = (
        "NONTRIVIAL" if admits_nontrivial_ndc(n * n)
        else "TRIVIAL" if n * n == 1
        else "FORBIDDEN_BY_CLASSIFICATION"
    )
    return row


def nontrivial_tensor_closure_witnesses():
    """Exact witnesses showing failure of universal NDC under standard tensoring."""
    return [tensor_pair_row(3, 3), tensor_pair_row(3, 7), tensor_pair_row(7, 7)]


def theorem_holds() -> bool:
    """Return True iff every nontrivial NDC local pair leaves the NDC dimension set."""
    return all(not r["tensor_nontrivial_ndc"] for r in nontrivial_tensor_closure_witnesses())
