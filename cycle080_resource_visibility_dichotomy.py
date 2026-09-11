"""Cycle 080: resource visibility dichotomy.

Analytic theorem boundary.
Let S_R be the real span of effects accessible in resource window R. If two
states rho,sigma satisfy Tr[(rho-sigma)E]=0 for every E in S_R, then their
probabilities agree on every accessible effect. Equivalently rho-sigma lies in
the Hilbert-Schmidt annihilator S_R^perp. If S_R is informationally complete
(span = Herm_d), the annihilator is {0}, hence sigma=rho.

Therefore resource restriction alone cannot yield a same-input experimentally
visible PDT/QM deviation: hidden changes in S_R^perp are invisible inside R;
when R is informationally complete there are no nonzero hidden changes.

The numerical audit uses diagonal-resource windows and off-diagonal hidden
perturbations across d=1..12 and higher dimensions. The theorem is algebraic;
the audit is regression evidence only.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 80080


def run_audit() -> Dict[str, object]:
    rng = np.random.default_rng(SEED)
    records: List[Dict[str, object]] = []
    max_visible_gap = 0.0
    max_hidden_gap = 0.0
    nondegenerate = 0

    for d in DIMS:
        if d == 1:
            records.append({
                "d": 1,
                "classification": "DEGENERATE",
                "restricted_visible_error": 0.0,
                "inaccessible_witness_gap": 0.0,
            })
            continue

        vals = rng.random(d) + 0.5
        vals /= vals.sum()
        rho = np.diag(vals.astype(complex))

        # H is traceless, Hermitian and orthogonal to every diagonal effect.
        h = np.zeros((d, d), dtype=complex)
        h[0, 1] = h[1, 0] = 1.0 / np.sqrt(2.0)
        opnorm = float(np.linalg.norm(h, 2))
        eps = 0.25 * float(vals.min()) / opnorm
        sigma = rho + eps * h

        # Diagonal rank-one effects span the chosen accessible resource space.
        visible = 0.0
        for j in range(d):
            e = np.zeros((d, d), dtype=complex)
            e[j, j] = 1.0
            visible = max(visible, abs(float(np.real(np.trace((sigma - rho) @ e)))))

        # A valid effect outside the diagonal resource window detects the shift.
        witness = (np.eye(d) + h / opnorm) / 2.0
        hidden_gap = float(np.real(np.trace((sigma - rho) @ witness)))
        mineig = float(np.linalg.eigvalsh(sigma).min())

        if mineig < -1e-12:
            raise AssertionError("constructed sigma lost positivity")
        if visible > 1e-12:
            raise AssertionError("annihilator perturbation became resource-visible")
        if hidden_gap <= 0.0:
            raise AssertionError("outside-resource witness failed to separate states")

        nondegenerate += 1
        max_visible_gap = max(max_visible_gap, visible)
        max_hidden_gap = max(max_hidden_gap, hidden_gap)
        records.append({
            "d": d,
            "min_eigenvalue_sigma": mineig,
            "epsilon": eps,
            "restricted_visible_error": visible,
            "inaccessible_witness_gap": hidden_gap,
        })

    return {
        "cycle": 80,
        "classification": [
            "PROVED",
            "FALSIFIED(resource-restriction-only same-window deviation)",
            "NUMERICALLY SUPPORTED",
            "IMPORTED/KNOWN BOUNDARY",
        ],
        "breakthrough_candidate": False,
        "dimensions": DIMS,
        "nondegenerate_cases": nondegenerate,
        "max_accessible_probability_gap": max_visible_gap,
        "max_inaccessible_witness_gap": max_hidden_gap,
        "theorem_note": (
            "Accessible equality is exactly annihilator membership: "
            "Tr[(sigma-rho)E]=0 for all E in S_R iff sigma-rho in S_R^perp. "
            "If S_R spans all Hermitian operators, S_R^perp={0}."
        ),
        "records": records,
    }


def main() -> None:
    result = run_audit()
    out = Path("results") / "cycle080_resource_visibility_dichotomy.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
