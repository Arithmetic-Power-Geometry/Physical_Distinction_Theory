"""Cycle 101: finite triad-coherence certificate for alternative bilinear PDT composition.

After Cycle 100, two-generator coherence is known to be insufficient.  In an
alternative algebra the associator is alternating; since a bilinear product has
a trilinear associator, vanishing on all unordered primitive basis triads is
sufficient to force global associativity.  This is a certification theorem, not
a PDT-native derivation of the premise.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def conjugate(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    if x.ndim != 1 or x.size < 1 or x.size & (x.size - 1):
        raise ValueError("length must be a positive power of two")
    if x.size == 1:
        return x.copy()
    h = x.size // 2
    return np.concatenate((conjugate(x[:h]), -x[h:]))


def cd_mul(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    x = np.asarray(x)
    y = np.asarray(y)
    if x.ndim != 1 or y.ndim != 1 or x.shape != y.shape:
        raise ValueError("equal one-dimensional shapes required")
    if x.size < 1 or x.size & (x.size - 1):
        raise ValueError("length must be a positive power of two")
    if x.size == 1:
        return x * y
    h = x.size // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    first = cd_mul(a, c) - cd_mul(conjugate(d), b)
    second = cd_mul(d, a) + cd_mul(b, conjugate(c))
    return np.concatenate((first, second))


def associator(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
    return cd_mul(cd_mul(x, y), z) - cd_mul(x, cd_mul(y, z))


def octonion_unordered_triad_audit() -> dict:
    e = np.eye(8, dtype=int)
    rows = []
    for i, j, k in itertools.combinations(range(1, 8), 3):
        a = associator(e[i], e[j], e[k])
        sq = int(np.dot(a, a))
        rows.append({"triad": [i, j, k], "associator": a.tolist(),
                     "squared_norm": sq, "nonzero": sq != 0})
    nonzero = [r for r in rows if r["nonzero"]]
    zero = [r for r in rows if not r["nonzero"]]
    return {
        "unordered_imaginary_basis_triads": len(rows),
        "nonzero_associator_triads": len(nonzero),
        "zero_associator_triads": len(zero),
        "fraction_nonzero": len(nonzero) / len(rows),
        "all_nonzero_squared_norms": sorted(set(r["squared_norm"] for r in nonzero)),
        "associative_fano_line_triads": [r["triad"] for r in zero],
        "first_decisive_witness": nonzero[0],
    }


def permutation_alternation_audit() -> dict:
    e = np.eye(8, dtype=int)
    violations = 0
    checks = 0
    for triad in itertools.combinations(range(1, 8), 3):
        base = associator(e[triad[0]], e[triad[1]], e[triad[2]])
        for perm in itertools.permutations(range(3)):
            inv = sum(perm[a] > perm[b] for a in range(3) for b in range(a + 1, 3))
            sign = -1 if inv % 2 else 1
            got = associator(e[triad[perm[0]]], e[triad[perm[1]]], e[triad[perm[2]]])
            violations += int(not np.array_equal(got, sign * base))
            checks += 1
    return {"permutation_checks": checks, "violations": violations,
            "all_exact": violations == 0}


def repeated_argument_audit() -> dict:
    e = np.eye(8, dtype=int)
    violations = 0
    checks = 0
    for i in range(1, 8):
        for j in range(1, 8):
            for triple in ((e[i], e[i], e[j]), (e[j], e[i], e[i])):
                violations += int(np.any(associator(*triple)))
                checks += 1
    return {"checks": checks, "violations": violations,
            "all_exact": violations == 0}


def dimension_certificate_ledger() -> list[dict]:
    return [{"distinction_vector_dimension_n": n,
             "unordered_primitive_triad_checks": math.comb(n, 3) if n >= 3 else 0}
            for n in DIMS]


def random_trilinear_reconstruction_audit(trials: int = 2000,
                                            seed: int = 101_007) -> dict:
    rng = np.random.default_rng(seed)
    e = np.eye(8)
    basis_assoc = {triad: associator(e[triad[0]], e[triad[1]], e[triad[2]])
                   for triad in itertools.combinations(range(1, 8), 3)}
    max_residual = 0.0
    violations = 0
    for _ in range(trials):
        x, y, z = rng.normal(size=(3, 8))
        direct = associator(x, y, z)
        recon = np.zeros(8)
        for (i, j, k), a in basis_assoc.items():
            coeff = np.linalg.det(np.array([[x[i], x[j], x[k]],
                                            [y[i], y[j], y[k]],
                                            [z[i], z[j], z[k]]]))
            recon += coeff * a
        residual = float(np.linalg.norm(direct - recon))
        max_residual = max(max_residual, residual)
        violations += int(residual > 1e-9)
    return {"seed": seed, "random_triples": trials,
            "max_reconstruction_residual": max_residual,
            "violations_gt_1e-9": violations}


def generate() -> dict:
    return {
        "cycle": 101,
        "target": "PDT-II targets (1)/(2): finite three-history certificate after the two-generator no-go",
        "classification": ["PROVED", "CONDITIONAL", "IMPORTED/KNOWN",
                           "NUMERICALLY_SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
        "theorem": {
            "statement": "Let A be a finite-dimensional unital algebra with bilinear product and an alternative associator. If {e_i} spans its non-scalar primitive sector, then global associativity is equivalent to vanishing of [e_i,e_j,e_k] for every unordered triple i<j<k.",
            "proof_core": "Bilinearity makes the associator trilinear. Alternativity makes it alternating, so repeated-index coefficients vanish and permutation-related coefficients differ only by sign. Hence the unordered basis-triad values determine the associator everywhere.",
            "qualification": "This is a certification theorem. It does not derive from PDT why every primitive triad must be path-independent, and imposing all triad vanishings is equivalent to associativity under the stated hypotheses."
        },
        "octonion_boundary": octonion_unordered_triad_audit(),
        "exact_alternation": permutation_alternation_audit(),
        "exact_alternative_identities": repeated_argument_audit(),
        "randomized_reconstruction": random_trilinear_reconstruction_audit(),
        "dimension_certificate_ledger": dimension_certificate_ledger(),
        "prior_art_boundary": "The equivalence between alternativity and an alternating associator, and the alternative/nonassociative character of the octonions, are classical. The finite basis certificate is multilinear algebra, not a historical novelty claim.",
        "surviving_pdt_obligation": "Derive or falsify a PDT-native physical principle requiring primitive three-history path independence. Without such a derivation, the n=3 selection remains conditional; two-history coherence cannot supply it."
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle101_triad_coherence_certificate.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
