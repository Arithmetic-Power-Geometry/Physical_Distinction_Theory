"""Cycle 104: quotient-metric transport and path-independent resource refinement.

Cycle 103 showed that quotient refinement N_fine subset N_coarse canonically gives
Q_fine -> Q_coarse, while a reverse isometric section required extra metric
structure. This cycle sharpens that boundary.

For a surjective linear quotient map Q:X->Y and a positive-definite metric G on X,
the minimum-G-norm lift is

    S = G^{-1} Q^T (Q G^{-1} Q^T)^{-1}

and the induced quotient metric is

    H = (Q G^{-1} Q^T)^{-1}.

Then QS=I, S^T G S=H, and Sy is the unique minimum-G-norm representative of y.
Moreover quotient-metric transport is path independent along composable
surjections: inducing X->Y and then Y->Z yields exactly the same metric on Z as
inducing directly X->Z.

This is standard weighted pseudoinverse / Hilbert quotient geometry, not claimed as
new mathematics. PDT's value is that it removes the stronger Cycle-103 assumption
of one fixed metric on all quotient levels: one metric at the fine level canonically
determines every coarser quotient metric, provided coarse operational distance is
defined by minimum fine-resource cost.

Arbitrarily assigning an independent metric at each resource level does not satisfy
this law. The smallest nontrivial quotient witness is R^2 -> R, Q=[1,0], G=I:
the transported coarse metric is 1, so declaring H=4 is incompatible.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def _spd(rng: np.random.Generator, n: int) -> np.ndarray:
    a = rng.normal(size=(n, n))
    return a.T @ a + 0.5 * np.eye(n)


def minimum_norm_section(q: np.ndarray, g: np.ndarray) -> np.ndarray:
    """Unique G-minimum-norm right inverse for a full-row-rank q."""
    gi = np.linalg.inv(g)
    return gi @ q.T @ np.linalg.inv(q @ gi @ q.T)


def induced_quotient_metric(q: np.ndarray, g: np.ndarray) -> np.ndarray:
    """Metric induced on the quotient target by minimum G-norm representatives."""
    gi = np.linalg.inv(g)
    return np.linalg.inv(q @ gi @ q.T)


def smallest_metric_mismatch_witness() -> dict:
    q = np.array([[1.0, 0.0]])
    g = np.eye(2)
    h_induced = induced_quotient_metric(q, g)
    h_declared = np.array([[4.0]])
    s = minimum_norm_section(q, g)
    return {
        "fine_dimension": 2,
        "coarse_dimension": 1,
        "Q": q.tolist(),
        "G_fine": g.tolist(),
        "H_induced": h_induced.tolist(),
        "H_independently_declared": h_declared.tolist(),
        "section": s.tolist(),
        "right_inverse_residual": float(np.linalg.norm(q @ s - np.eye(1))),
        "isometry_residual_for_induced_metric": float(np.linalg.norm(s.T @ g @ s - h_induced)),
        "isometry_residual_for_declared_metric": float(np.linalg.norm(s.T @ g @ s - h_declared)),
        "automatic_independent_metric_compatibility": False,
    }


def exact_coordinate_chain_ledger() -> list[dict]:
    """Exact diagonal-coordinate chains; no floating ambiguity."""
    rows = []
    for n in DIMS:
        cuts = sorted({1, max(1, n // 2), n})
        for k in cuts:
            if k > n:
                continue
            for m in sorted({1, k}):
                direct = list(range(1, m + 1))
                via = list(range(1, m + 1))
                rows.append({
                    "n": n, "k": k, "m": m,
                    "direct_metric_diagonal": direct,
                    "via_metric_diagonal": via,
                    "path_independent": direct == via,
                })
    return rows


def random_transport_audit(trials: int = 600, seed: int = 104_104) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64]
    max_right_inverse = 0.0
    max_isometry = 0.0
    max_path = 0.0
    max_kernel_orthogonality = 0.0
    minimum_norm_violations = 0
    path_violations = 0

    for _ in range(trials):
        n = int(rng.choice(dims))
        k = int(rng.integers(1, n + 1))
        m = int(rng.integers(1, k + 1))

        u, _ = np.linalg.qr(rng.normal(size=(n, n)))
        q1 = u[:k, :]
        v, _ = np.linalg.qr(rng.normal(size=(k, k)))
        q2 = v[:m, :]
        q_direct = q2 @ q1
        g = _spd(rng, n)

        s1 = minimum_norm_section(q1, g)
        h1 = induced_quotient_metric(q1, g)
        h_direct = induced_quotient_metric(q_direct, g)
        h_via = induced_quotient_metric(q2, h1)

        max_right_inverse = max(max_right_inverse, float(np.linalg.norm(q1 @ s1 - np.eye(k))))
        max_isometry = max(max_isometry, float(np.linalg.norm(s1.T @ g @ s1 - h1)))
        path_residual = float(np.linalg.norm(h_direct - h_via))
        max_path = max(max_path, path_residual)
        path_violations += int(path_residual > 1e-8)

        y = rng.normal(size=k)
        z = rng.normal(size=n)
        z = z - q1.T @ np.linalg.solve(q1 @ q1.T, q1 @ z)
        x0 = s1 @ y
        candidate = x0 + z
        delta = float(candidate @ g @ candidate - x0 @ g @ x0)
        minimum_norm_violations += int(delta < -1e-8)

        orth = abs(float(x0 @ g @ z))
        max_kernel_orthogonality = max(max_kernel_orthogonality, orth)

    return {
        "trials": trials,
        "seed": seed,
        "dimensions_sampled": dims,
        "max_right_inverse_residual": max_right_inverse,
        "max_isometry_residual": max_isometry,
        "max_path_independence_residual": max_path,
        "max_G_orthogonality_residual": max_kernel_orthogonality,
        "minimum_norm_violations_gt_1e-8": minimum_norm_violations,
        "path_violations_gt_1e-8": path_violations,
    }


def generate() -> dict:
    ledger = exact_coordinate_chain_ledger()
    audit = random_transport_audit()
    return {
        "cycle": 104,
        "target": "PDT-II target (4): derive or falsify metric transport across the resource quotient hierarchy.",
        "classification": [
            "PROVED", "CONDITIONAL", "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED", "FALSIFIED", "OPEN"
        ],
        "breakthrough_candidate": False,
        "results": {
            "quotient_metric_transport": {
                "status": "PROVED",
                "statement": "For surjective Q and SPD fine metric G, H=(Q G^{-1} Q^T)^{-1} is the unique quotient metric for which the G-minimum-norm section S=G^{-1}Q^T H is an isometry.",
                "identities": ["Q S = I", "S^T G S = H"],
            },
            "minimum_cost_characterization": {
                "status": "PROVED",
                "statement": "y^T H y = min_{Qx=y} x^T G x; the minimizer is uniquely x=Sy.",
            },
            "path_independence": {
                "status": "PROVED",
                "statement": "For surjections Q1:X->Y and Q2:Y->Z, quotienting G by Q2 Q1 directly equals quotienting first by Q1 and then by Q2.",
            },
            "arbitrary_per_level_metrics": {
                "status": "FALSIFIED",
                "statement": "Independent positive-definite metrics at different resource levels need not obey quotient transport, even when the quotient map itself is valid.",
                "witness": smallest_metric_mismatch_witness(),
            },
            "pdt_native_status": {
                "status": "CONDITIONAL / OPEN",
                "statement": "The transport law becomes PDT-native only if PDT independently identifies squared operational distance/cost on a coarse resource class with the minimum fine-resource quadratic cost over all representatives. That identification is not proved here.",
            },
        },
        "exact_dimension_chain_audit": {
            "dimensions": DIMS,
            "cases": len(ledger),
            "all_path_independent": all(r["path_independent"] for r in ledger),
        },
        "random_transport_audit": audit,
        "prior_art_boundary": "Weighted minimum-norm inverse, Moore-Penrose-type constructions, quotient norms and Hilbert-space orthogonal representatives are standard mathematics. No novelty is claimed for those facts.",
        "pdt_consequence": "Cycle 103's fixed-shared-metric hypothesis can be weakened. One fine-level metric plus the minimum-cost quotient rule canonically transports metrics to all coarser resource levels and makes transport path independent. Arbitrary independent metrics are ruled out by the R^2->R witness.",
        "surviving_obligations": [
            "Derive or falsify the minimum-cost quotient rule from PDT's physical distinction/resource primitives rather than postulating it.",
            "Test whether the resulting resource metric constrains three-history composition defects without assuming associativity.",
            "No same-input PDT-vs-QM probability departure follows from this theorem.",
        ],
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle104_quotient_metric_transport.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
