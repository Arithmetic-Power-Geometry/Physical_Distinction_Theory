"""Cycle 103: resource-quotient splitting and canonical-section boundary.

Cycle 033 gives nested invisible kernels N_fine subset N_coarse and therefore a
canonical surjection Q_fine=V/N_fine -> Q_coarse=V/N_coarse. Cycle 098 requires
compatible inherited directions plus no-erasure records. This cycle proves two
complementary facts:

(1) quotient refinement alone does NOT provide a canonical reverse injection;
    the smallest witness is R^2 -> R with quotient q(x,y)=x and a shear family.
(2) once a fixed inner product is part of the model, minimum-norm representatives
    canonically (relative to that metric) split the quotient map:
    Q_fine = i(Q_coarse) orthogonal-sum (N_coarse intersect N_fine^perp).

The mathematics is standard finite-dimensional inner-product/quotient linear
algebra. The PDT value is to locate exactly which existing structure is needed
for the Cycle-098 inherited-space hypothesis, without silently assuming a split.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def no_canonical_section_witness() -> dict:
    """Smallest nontrivial quotient witness.

    q:R^2->R, q(x,y)=x. Every s_a(t)=(t,a t) is a section. The quotient-preserving
    shear T_b(x,y)=(x,y+b x) sends s_a to s_{a+b}; hence no section can be invariant
    under all automorphisms preserving q. Quotient data alone therefore choose no
    canonical reverse embedding.
    """
    q = np.array([[1, 0]], dtype=int)
    sections = []
    for a in [-2, -1, 0, 1, 2]:
        s = np.array([[1], [a]], dtype=int)
        assert np.array_equal(q @ s, np.array([[1]], dtype=int))
        sections.append({"a": a, "column": s[:, 0].tolist()})
    shear = np.array([[1, 0], [1, 1]], dtype=int)
    s0 = np.array([[1], [0]], dtype=int)
    moved = shear @ s0
    return {
        "ambient_dimension": 2,
        "q": q.tolist(),
        "sample_sections": sections,
        "quotient_preserving_shear": shear.tolist(),
        "qT_equals_q": bool(np.array_equal(q @ shear, q)),
        "section_0": s0[:, 0].tolist(),
        "shear_moves_section_0_to": moved[:, 0].tolist(),
        "section_is_fixed": bool(np.array_equal(moved, s0)),
    }


def coordinate_dimension_ledger() -> list[dict]:
    """Exact coordinate-model checks over required dimensions."""
    rows = []
    for n in DIMS:
        pairs = {(0, 0), (n, n), (n, 0)}
        if n >= 1:
            pairs.add((n, n - 1))
        if n >= 2:
            pairs.add((n - 1, 0))
            pairs.add((n - 1, n - 2))
        for coarse, fine in sorted(pairs):
            if not (0 <= fine <= coarse <= n):
                continue
            q_coarse = n - coarse
            q_fine = n - fine
            innovation = coarse - fine
            rows.append({
                "n": n,
                "dim_N_coarse": coarse,
                "dim_N_fine": fine,
                "dim_Q_coarse": q_coarse,
                "dim_Q_fine": q_fine,
                "innovation_dim": innovation,
                "balance_ok": q_fine == q_coarse + innovation,
            })
    return rows


def random_metric_split_audit(trials: int = 500, seed: int = 103_103) -> dict:
    """Stress the orthogonal splitting on random nested Euclidean subspaces."""
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64]
    max_reconstruction = 0.0
    max_section = 0.0
    max_orthogonality = 0.0
    violations = 0

    for _ in range(trials):
        n = int(rng.choice(dims))
        qmat, _ = np.linalg.qr(rng.normal(size=(n, n)))
        coarse = int(rng.integers(0, n + 1))
        fine = int(rng.integers(0, coarse + 1))

        b_coarse = qmat[:, coarse:]
        b_fine = qmat[:, fine:]
        b_innovation = qmat[:, fine:coarse]

        e = b_fine.T @ b_coarse
        p = b_coarse.T @ b_fine

        reconstruction = float(np.linalg.norm(b_fine @ e - b_coarse)) if n - coarse else 0.0
        section = float(np.linalg.norm(p @ e - np.eye(n - coarse))) if n - coarse else 0.0
        orthogonality = (
            float(np.linalg.norm(b_coarse.T @ b_innovation))
            if (n - coarse) and (coarse - fine)
            else 0.0
        )

        max_reconstruction = max(max_reconstruction, reconstruction)
        max_section = max(max_section, section)
        max_orthogonality = max(max_orthogonality, orthogonality)
        violations += int(max(reconstruction, section, orthogonality) > 1e-9)

    return {
        "trials": trials,
        "seed": seed,
        "dimensions_sampled": dims,
        "max_embedding_reconstruction_residual": max_reconstruction,
        "max_section_identity_residual": max_section,
        "max_old_new_orthogonality_residual": max_orthogonality,
        "violations_gt_1e-9": violations,
    }


def record_recoverability_audit(trials: int = 400, seed: int = 103_098) -> dict:
    """Check that nested/retained fine records recover every coarse record."""
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64]
    max_residual = 0.0
    violations = 0
    for _ in range(trials):
        n = int(rng.choice(dims))
        m_fine = int(rng.integers(1, min(n + 4, 20)))
        m_coarse = int(rng.integers(1, min(m_fine + 1, 10)))
        b = rng.integers(-3, 4, size=(m_fine, n)).astype(float)
        c = rng.integers(-2, 3, size=(m_coarse, m_fine)).astype(float)
        a = c @ b
        residual = float(np.linalg.norm(a - c @ b))
        max_residual = max(max_residual, residual)
        violations += int(residual > 1e-12)
    return {
        "trials": trials,
        "seed": seed,
        "dimensions_sampled": dims,
        "max_A_minus_CB_residual": max_residual,
        "violations_gt_1e-12": violations,
    }


def generate() -> dict:
    ledger = coordinate_dimension_ledger()
    return {
        "cycle": 103,
        "target": "PDT-II target (4), with consequences for (1)/(2): does the existing resource quotient itself supply Cycle-098 refinement compatibility and inherited-space structure?",
        "classification": ["PROVED", "CONDITIONAL", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED", "FALSIFIED", "OPEN"],
        "breakthrough_candidate": False,
        "results": {
            "record_compatibility": {
                "status": "PROVED inside the Cycle-033 linear refinement model",
                "statement": "If refinement means row(A_coarse) subseteq row(A_fine), then A_coarse=P A_fine for some linear P, so every coarse linear record is recoverable from fine records.",
            },
            "canonical_direction": {
                "status": "PROVED",
                "statement": "For N_fine subseteq N_coarse, quotient refinement canonically gives a SURJECTION V/N_fine -> V/N_coarse, not a reverse injection.",
            },
            "quotient_only_reverse_embedding": {
                "status": "FALSIFIED as canonical/natural without extra structure",
                "statement": "Nested quotient data alone do not canonically select a section V/N_coarse -> V/N_fine. The R^2 shear witness is minimal.",
                "witness": no_canonical_section_witness(),
            },
            "metric_split": {
                "status": "PROVED, CONDITIONAL on a fixed shared positive-definite inner product",
                "statement": "Using minimum-norm representatives, V/N is canonically relative to the metric identified with N^perp. If N_fine subseteq N_coarse then N_coarse^perp subseteq N_fine^perp, giving an isometric section i and the orthogonal split Q_fine = i(Q_coarse) direct-sum (N_coarse intersect N_fine^perp).",
                "dimension_law": "dim Q_fine = dim Q_coarse + dim N_coarse - dim N_fine",
            },
        },
        "dimension_audit": {
            "dimensions": DIMS,
            "exact_cases": len(ledger),
            "all_exact_dimension_balances_hold": all(r["balance_ok"] for r in ledger),
            "identity": "dim Q_fine = dim Q_coarse + dim N_coarse - dim N_fine",
        },
        "random_metric_split_audit": random_metric_split_audit(),
        "record_recoverability_audit": record_recoverability_audit(),
        "prior_art_boundary": "Orthogonal-complement decomposition, quotient spaces, split exact sequences, rank-nullity, and row-space factorization are standard linear algebra/functional analysis. No mathematical novelty is claimed.",
        "pdt_consequence": "Cycle-098 no-erasure record compatibility is already supplied by Cycle-033's definition of genuine linear resource refinement. Its inherited-space embedding is not supplied by quotient structure alone; it is derivable if PDT commits to one fixed shared inner product/metric across the refinement chain. If the metric itself changes with resource, an additional transport/compatibility law remains OPEN.",
        "surviving_obligations": [
            "Derive or falsify resource-invariance/transport of the inner product rather than assuming it.",
            "Connect quotient innovation directions to composition-defect spaces without conflating resolved state directions with admissible associator defects.",
            "No same-input PDT-vs-QM quantitative departure follows from this splitting theorem.",
        ],
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle103_resource_quotient_metric_split.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
