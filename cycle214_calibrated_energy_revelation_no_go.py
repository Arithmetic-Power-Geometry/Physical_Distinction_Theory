"""Exact checks for Cycle 214 calibrated-energy revelation no-go.

No stochastic simulation is used: all checks are finite and exact.
"""


def dynamics(n):
    if n < 3:
        return tuple(range(n))
    # Protected pair 0,1 has distinct dynamics; extensions are harmless.
    f = list(range(n))
    f[0], f[1], f[2] = 0, 1, 0
    return tuple(f)


def observation_signatures(n, budget):
    """Signatures of accessible binary observations at integer energy budget.

    All observations obey the exact symmetry 0<->1. As budget rises, indicators
    of unprotected states 2,3,... become accessible one by one.
    """
    if n < 3:
        return [tuple([0] * n)]
    sigs = [tuple([0] * n)]
    max_state = min(n - 1, 1 + max(0, int(budget)))
    for j in range(2, max_state + 1):
        sigs.append(tuple(1 if x == j else 0 for x in range(n)))
    return sigs


def equivalent(x, y, sigs):
    return all(a[x] == a[y] for a in sigs)


def run():
    rows = []
    for n in range(1, 13):
        f = dynamics(n)
        if n < 3:
            rows.append((n, "EDGE/DEGENERATE", True, True))
            continue

        budgets = list(range(0, max(3, n + 1)))
        protected_all = True
        strict_growth_seen = False
        previous_count = None
        for E in budgets:
            sigs = observation_signatures(n, E)
            protected_all &= equivalent(0, 1, sigs)
            if previous_count is not None and len(sigs) > previous_count:
                strict_growth_seen = True
            previous_count = len(sigs)

        dynamically_distinct = f[0] != f[1]
        # n=3 can already grow once; n>=4 has multiple possible refinements.
        assert protected_all
        assert dynamically_distinct
        assert strict_growth_seen
        rows.append((n, "EXACT", protected_all, dynamically_distinct))

    return rows


if __name__ == "__main__":
    result = run()
    for row in result:
        print(row)
    print("Cycle 214 exact checks passed for n=1..12 (n<3 edge/degenerate).")
