from fractions import Fraction
from math import comb

STRESS_DIMS = tuple(range(1, 13)) + (16, 24, 32, 48, 64, 96, 128)


def carrier_dimensions(n: int) -> dict[str, int]:
    if n < 1:
        raise ValueError("n must be positive")
    return {
        "full_exterior_or_clifford": 2 ** n,
        "even_clifford": 2 ** (n - 1),
        "scalar_vector_bivector": 1 + n + comb(n, 2),
        "vector_bivector": n + comb(n, 2),
    }


def relative_overheads(n: int) -> dict[str, Fraction]:
    return {name: Fraction(dim, n) for name, dim in carrier_dimensions(n).items()}


def exact_stress_table(dimensions=STRESS_DIMS) -> list[dict]:
    rows = []
    for n in dimensions:
        dims = carrier_dimensions(n)
        costs = relative_overheads(n)
        rows.append({
            "n": n,
            **dims,
            **{f"{k}_overhead": str(v) for k, v in costs.items()},
        })
    return rows


def minimizers(max_n: int = 128) -> dict[str, dict]:
    if max_n < 1:
        raise ValueError("max_n must be positive")
    names = tuple(relative_overheads(1))
    out = {}
    for name in names:
        values = [(relative_overheads(n)[name], n) for n in range(1, max_n + 1)]
        minimum = min(v for v, _ in values)
        out[name] = {
            "minimum": str(minimum),
            "n": [n for value, n in values if value == minimum],
        }
    return out


def theorem_checks(max_n: int = 128) -> dict[str, bool]:
    # Exact finite checks accompanying analytic proofs:
    # 2^n/n has f(n+1)/f(n)=2n/(n+1): equality only n=1, increasing for n>1.
    # (1+n+C(n,2))/n=(n+1)/2+1/n: f(1)=f(2)=2 and
    # f(n+1)-f(n)=1/2-1/(n(n+1))>0 for n>=2.
    # (n+C(n,2))/n=(n+1)/2 is strictly increasing.
    full = [relative_overheads(n)["full_exterior_or_clifford"] for n in range(1, max_n + 1)]
    even = [relative_overheads(n)["even_clifford"] for n in range(1, max_n + 1)]
    svb = [relative_overheads(n)["scalar_vector_bivector"] for n in range(1, max_n + 1)]
    vb = [relative_overheads(n)["vector_bivector"] for n in range(1, max_n + 1)]
    return {
        "full_min_n1_n2": full[0] == full[1] == min(full) and all(full[i] < full[i + 1] for i in range(1, len(full) - 1)),
        "even_min_n1_n2": even[0] == even[1] == min(even) and all(even[i] < even[i + 1] for i in range(1, len(even) - 1)),
        "svb_min_n1_n2": svb[0] == svb[1] == min(svb) and all(svb[i] < svb[i + 1] for i in range(1, len(svb) - 1)),
        "vb_min_n1": vb[0] == min(vb) and all(vb[i] < vb[i + 1] for i in range(len(vb) - 1)),
    }


if __name__ == "__main__":
    import json
    print(json.dumps({
        "stress_table": exact_stress_table(),
        "minimizers_n1_to_n128": minimizers(128),
        "theorem_checks": theorem_checks(128),
    }, indent=2))
