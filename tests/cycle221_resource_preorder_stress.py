"""Cycle 221 exact sanity tests for resource-monotone completeness.

Finite resource model: subsets S of [n], with free conversion S -> T iff T <= S
under inclusion. Cardinality is monotone but fails completeness from n=2 onward.
No external packages required.
"""
from itertools import combinations


def subsets(n):
    xs = range(n)
    return [frozenset(c) for r in range(n + 1) for c in combinations(xs, r)]


def converts(s, t):
    return t.issubset(s)


def cardinality_monotone(n):
    rs = subsets(n)
    return all(len(s) >= len(t) for s in rs for t in rs if converts(s, t))


def equal_value_incomparable_witness(n):
    rs = subsets(n)
    for i, s in enumerate(rs):
        for t in rs[i + 1:]:
            if len(s) == len(t) and not converts(s, t) and not converts(t, s):
                return s, t
    return None


def run():
    rows = []
    for n in range(1, 13):
        witness = equal_value_incomparable_witness(n)
        row = {
            "n": n,
            "cardinality_monotone": cardinality_monotone(n),
            "cardinality_complete": witness is None,
            "witness": None if witness is None else [sorted(witness[0]), sorted(witness[1])],
        }
        rows.append(row)

    assert all(r["cardinality_monotone"] for r in rows)
    assert rows[0]["cardinality_complete"]
    assert all(not r["cardinality_complete"] for r in rows[1:])
    assert rows[1]["witness"] == [[0], [1]]
    return rows


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
