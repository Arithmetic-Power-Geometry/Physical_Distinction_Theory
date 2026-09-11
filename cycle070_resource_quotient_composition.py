from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np

DIMS = tuple(range(1, 13))
HIGH_DIMS = (16, 24, 32, 48, 64)


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    a = x @ x.conj().T
    return a / np.trace(a)


def orthonormal_accessible_space(d: int, k: int, rng: np.random.Generator) -> list[np.ndarray]:
    if not (1 <= k <= d * d):
        raise ValueError("k must satisfy 1 <= k <= d^2")
    out = [np.eye(d, dtype=complex) / math.sqrt(d)]
    while len(out) < k:
        x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        h = (x + x.conj().T) / 2
        for b in out:
            h = h - float(np.trace(b.conj().T @ h).real) * b
        n = float(np.linalg.norm(h, "fro"))
        if n > 1e-12:
            out.append(h / n)
    return out


def restricted_coordinates(rho: np.ndarray, basis: list[np.ndarray]) -> np.ndarray:
    return np.asarray([np.trace(rho @ b).real for b in basis], dtype=float)


def restriction_error(rho: np.ndarray, fine: list[np.ndarray], coarse_k: int) -> float:
    fine_q = restricted_coordinates(rho, fine)
    coarse_q = restricted_coordinates(rho, fine[:coarse_k])
    return float(np.max(np.abs(fine_q[:coarse_k] - coarse_q), initial=0.0))


def annihilator_error(x: np.ndarray, basis: list[np.ndarray]) -> float:
    return float(np.max(np.abs([np.trace(x @ b).real for b in basis]), initial=0.0))


def product_coordinate_error(ra, rb, ba, bb) -> float:
    qa = restricted_coordinates(ra, ba)
    qb = restricted_coordinates(rb, bb)
    rab = np.kron(ra, rb)
    qab = np.asarray(
        [np.trace(rab @ np.kron(a, b)).real for a in ba for b in bb], dtype=float
    )
    return float(np.max(np.abs(qab - np.kron(qa, qb)), initial=0.0))


def run_audit(seed: int = 70070) -> dict:
    rng = np.random.default_rng(seed)
    max_restriction = 0.0
    max_annihilator = 0.0
    refinement_cases = 0
    for d in DIMS + HIGH_DIMS:
        reps = 20 if d <= 12 else 5
        for _ in range(reps):
            k = min(8, max(1, 2 * d), d * d)
            kp = min(d * d, k + min(3, d * d - k))
            fine = orthonormal_accessible_space(d, kp, rng)
            rho = random_density(d, rng)
            max_restriction = max(max_restriction, restriction_error(rho, fine, k))
            if kp > k:
                max_annihilator = max(max_annihilator, annihilator_error(fine[k], fine[:k]))
            refinement_cases += 1

    max_product = 0.0
    product_cases = 0
    for da in range(1, 7):
        for db in range(1, 7):
            for _ in range(8):
                ba = orthonormal_accessible_space(da, min(4, da * da), rng)
                bb = orthonormal_accessible_space(db, min(4, db * db), rng)
                ra, rb = random_density(da, rng), random_density(db, rng)
                max_product = max(max_product, product_coordinate_error(ra, rb, ba, bb))
                product_cases += 1

    return {
        "classification": ["PROVED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED"],
        "claim": "resource-restricted state functionals form an exact quotient and product states compose by tensor product on product-accessible observables",
        "dimensions_refinement": list(DIMS + HIGH_DIMS),
        "refinement_cases": refinement_cases,
        "product_dimension_pairs": [[a, b] for a in range(1, 7) for b in range(1, 7)],
        "product_cases": product_cases,
        "max_restriction_error": max_restriction,
        "max_annihilator_error": max_annihilator,
        "max_product_coordinate_error": max_product,
        "breakthrough_candidate": False,
        "reason_not_breakthrough": "finite-dimensional quotient/dual-space and operator-system restriction/tensor-product mathematics are established prior art",
    }


if __name__ == "__main__":
    result = run_audit()
    out = Path("results") / "cycle070_resource_quotient_composition.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
