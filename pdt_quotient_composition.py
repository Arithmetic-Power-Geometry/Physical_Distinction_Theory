"""Cycle 035: resource-quotient composition audit.

Linear-algebra core: if local null spaces are N<=V and M<=W, then the
product-accessible quotient is canonically
(V/N) tensor (W/M) ~= (V tensor W)/(N tensor W + V tensor M).
This does NOT determine a physical composite unless composite accessible
effects are independently fixed.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class QuotientCompositionAudit:
    dim_v: int
    dim_w: int
    null_v: int
    null_w: int

    @property
    def local_q_v(self) -> int:
        return self.dim_v - self.null_v

    @property
    def local_q_w(self) -> int:
        return self.dim_w - self.null_w

    @property
    def product_accessible_dim(self) -> int:
        return self.local_q_v * self.local_q_w

    @property
    def tensor_dim(self) -> int:
        return self.dim_v * self.dim_w

    @property
    def product_null_dim(self) -> int:
        # dim(N tensor W + V tensor M) = nN*dW + dV*nM - nN*nM
        return self.null_v*self.dim_w + self.dim_v*self.null_w - self.null_v*self.null_w

    def validate(self) -> bool:
        if not (0 <= self.null_v <= self.dim_v and 0 <= self.null_w <= self.dim_w):
            return False
        return self.tensor_dim - self.product_null_dim == self.product_accessible_dim


def admissible_composite_quotient_dimensions(dim_v: int, dim_w: int, null_v: int, null_w: int):
    """Dimensions consistent with the same local quotients once global effects may be added.

    Product effects guarantee at least qV*qW accessible directions. Independent
    global effects can reveal any number of the remaining tensor directions, up
    to dim(V tensor W). This is a linear operational model, not a claim that all
    such choices form a full physical GPT.
    """
    a = QuotientCompositionAudit(dim_v, dim_w, null_v, null_w)
    if not a.validate():
        raise ValueError("invalid dimensions")
    return list(range(a.product_accessible_dim, a.tensor_dim + 1))


def sweep(max_dim: int = 12):
    rows = []
    for dv in range(1, max_dim + 1):
        for dw in range(1, max_dim + 1):
            # Edge cases: no local null direction and one maximally nontrivial null count.
            for nv in sorted(set((0, max(0, dv-1)))):
                for nw in sorted(set((0, max(0, dw-1)))):
                    a = QuotientCompositionAudit(dv, dw, nv, nw)
                    rows.append({
                        "dim_v": dv, "dim_w": dw, "null_v": nv, "null_w": nw,
                        "q_v": a.local_q_v, "q_w": a.local_q_w,
                        "product_q": a.product_accessible_dim,
                        "tensor_dim": a.tensor_dim,
                        "product_null": a.product_null_dim,
                        "identity_ok": a.validate(),
                        "global_freedom": a.tensor_dim-a.product_accessible_dim,
                    })
    return rows
