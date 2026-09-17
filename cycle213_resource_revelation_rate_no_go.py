"""Exact checks for Cycle 213 resource-to-revelation rate no-go.

No third-party dependencies.  Run with: python cycle213_resource_revelation_rate_no_go.py
"""
from itertools import combinations


def partition_from_observations(n, observations):
    sig = {}
    for x in range(n):
        key = tuple(obs(x) for obs in observations)
        sig.setdefault(key, []).append(x)
    return tuple(sorted(tuple(v) for v in sig.values()))


def distinction_count(partition):
    n = sum(map(len, partition))
    total = n * (n - 1) // 2
    hidden = sum(len(b) * (len(b) - 1) // 2 for b in partition)
    return total - hidden


def witness_observations(n, levels=8):
    # q permanently merges 0 and 1; states >=2 remain labelled.
    def q(x):
        return 0 if x < 2 else x - 1

    families = []
    for r in range(1, levels + 1):
        # Strictly different observations, all deterministic functions of q.
        # The first observation already exposes q; later ones are redundant.
        obs = [q]
        for k in range(2, r + 1):
            obs.append(lambda x, k=k: (k * q(x) + k * k) % (n + k + 1))
        families.append(obs)
    return families


def run_exact_checks():
    rows = []
    for n in range(1, 13):
        if n < 3:
            rows.append((n, "DEGENERATE", None, None))
            continue
        fams = witness_observations(n)
        parts = [partition_from_observations(n, f) for f in fams]
        ds = [distinction_count(p) for p in parts]
        assert all(p == parts[0] for p in parts), (n, parts)
        assert all(d == ds[0] for d in ds), (n, ds)
        # Families grow in number of declared observations while D is flat.
        assert [len(f) for f in fams] == list(range(1, len(fams) + 1))
        # Hidden pair remains hidden.
        assert any(0 in b and 1 in b for b in parts[-1])
        rows.append((n, "PASS", ds[0], ds[-1] - ds[0]))
    return rows


if __name__ == "__main__":
    rows = run_exact_checks()
    print("n,status,D,delta_D_across_strict_family_growth")
    for row in rows:
        print(",".join(map(str, row)))
