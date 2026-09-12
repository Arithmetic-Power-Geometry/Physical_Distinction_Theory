"""Cycle 090: orientation-reversal no-go for the Cycle-089 n=3 selector.

Exact statement: if V=R^3 with the standard O(3) action and B: V x V -> V
is alternating, bilinear, and O(3)-equivariant, then B=0.

This is an exact symbolic/algebraic regression aid, not a novelty claim.
"""
from itertools import permutations


def levi_civita(i: int, j: int, k: int) -> int:
    if len({i, j, k}) < 3:
        return 0
    p = (i, j, k)
    inv = sum(p[a] > p[b] for a in range(3) for b in range(a + 1, 3))
    return -1 if inv % 2 else 1


def reflected_component(i: int, j: int, k: int, signs=(-1, 1, 1)) -> int:
    """Component multiplier under R=diag(-1,1,1) on all three slots."""
    return signs[i] * signs[j] * signs[k] * levi_civita(i, j, k)


def audit():
    nonzero = []
    contradictions = []
    for i, j, k in permutations(range(3), 3):
        t = levi_civita(i, j, k)
        rt = reflected_component(i, j, k)
        nonzero.append((i, j, k, t, rt))
        # Every nonzero 3-form component contains indices 0,1,2 exactly once,
        # so reflection reverses its sign.
        if rt == -t:
            contradictions.append((i, j, k))
    assert len(nonzero) == 6
    assert len(contradictions) == 6
    return {
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN"],
        "dimension": 3,
        "reflection": [-1, 1, 1],
        "determinant": -1,
        "nonzero_alternating_components": len(nonzero),
        "sign_reversed_components": len(contradictions),
        "conclusion": "No nonzero O(3)-equivariant alternating bilinear map VxV->V exists.",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
