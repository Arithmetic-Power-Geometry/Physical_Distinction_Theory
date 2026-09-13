"""Cycle 128: composite-carrier dimension lower bound.

This audit does NOT claim tensor products as PDT novelty. It tests the exact
linear-algebra consequence used as a guardrail:

If a bilinear product map mu: V_A x V_B -> W has linearly independent product
images mu(e_i,f_j), then dim(W) >= dim(V_A)*dim(V_B). Consequently an
n-dimensional same-carrier composite W=V is impossible for n>1 under this
product-distinguishability hypothesis.
"""

from __future__ import annotations

import json
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def lower_bound(dim_a: int, dim_b: int) -> int:
    if dim_a < 1 or dim_b < 1:
        raise ValueError("dimensions must be positive")
    return dim_a * dim_b


def same_carrier_possible(n: int) -> bool:
    """Whether n can contain n^2 independent product directions."""
    return lower_bound(n, n) <= n


def kernel_lower_bound(n: int, target_dim: int | None = None) -> int:
    """Rank-nullity lower bound for any linearized bilinear product map.

    A bilinear mu factors uniquely through a linear map V tensor V -> W.
    If dim(W)=target_dim, nullity is at least n^2-target_dim.
    """
    if target_dim is None:
        target_dim = n
    if n < 1 or target_dim < 0:
        raise ValueError("invalid dimensions")
    return max(0, n * n - target_dim)


def audit() -> dict:
    rows = []
    for n in DIMS:
        rows.append(
            {
                "n": n,
                "independent_product_directions_required": n * n,
                "same_carrier_dimension": n,
                "minimum_kernel_if_forced_into_same_carrier": kernel_lower_bound(n),
                "same_carrier_compatible_with_independence": same_carrier_possible(n),
            }
        )

    failures = [r for r in rows if r["n"] > 1 and r["same_carrier_compatible_with_independence"]]
    return {
        "cycle": 128,
        "classification": {
            "dimension_bound": "PROVED",
            "same_carrier_for_n_gt_1_under_product_independence": "FALSIFIED",
            "tensor_product_universal_property": "IMPORTED/KNOWN",
            "pdt_native_composite_law": "OPEN",
        },
        "hypotheses": [
            "finite-dimensional real vector spaces V_A, V_B, W",
            "bilinear product map mu: V_A x V_B -> W",
            "the product images mu(e_i,f_j) are linearly independent (product-distinguishability / no product-direction collapse)",
        ],
        "theorem": "dim(W) >= dim(V_A)*dim(V_B)",
        "equal_dimension_corollary": "for dim(V_A)=dim(V_B)=n>1, W cannot also have dimension n",
        "smallest_decisive_case": {"n": 2, "required": 4, "same_carrier": 2, "minimum_kernel": 2},
        "rows": rows,
        "guard_failures": failures,
    }


def main() -> None:
    result = audit()
    out = Path("results/cycle128_composite_carrier_dimension_no_go.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
