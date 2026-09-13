from __future__ import annotations

import json
import random
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def gp_blades(a: int, b: int) -> tuple[int, int]:
    """Euclidean Clifford product of ordered basis blades encoded as bitmasks.

    Returns (sign, mask), with e_i^2=+1.
    """
    sign = 1
    x = a
    while x:
        lsb = x & -x
        if (b & (lsb - 1)).bit_count() % 2:
            sign = -sign
        x ^= lsb
    return sign, a ^ b


def scale_product(sa: int, a: int, sb: int, b: int) -> tuple[int, int]:
    s, m = gp_blades(a, b)
    return sa * sb * s, m


def signed_permutation_image(mask: int, perm: list[int], signs: list[int]) -> tuple[int, int]:
    """Image of a blade under an orthogonal signed permutation of generators."""
    out_sign, out_mask = 1, 0
    for i in range(len(perm)):
        if mask >> i & 1:
            out_sign, out_mask = scale_product(out_sign, out_mask, signs[i], 1 << perm[i])
    return out_sign, out_mask


def signed_permutation_automorphism_check(a: int, b: int, perm: list[int], signs: list[int]) -> bool:
    sab, mab = gp_blades(a, b)
    sl, ml = signed_permutation_image(mab, perm, signs)
    lhs = (sab * sl, ml)
    sa, ma = signed_permutation_image(a, perm, signs)
    sb, mb = signed_permutation_image(b, perm, signs)
    rhs = scale_product(sa, ma, sb, mb)
    return lhs == rhs


def exact_generator_audit(n: int) -> dict:
    relation_failures = 0
    associativity_failures = 0
    closure_outside_vector = 0
    for i in range(n):
        ei = 1 << i
        s, m = gp_blades(ei, ei)
        relation_failures += int((s, m) != (1, 0))
        if m == 0:
            closure_outside_vector += 1
        for j in range(n):
            ej = 1 << j
            sij, mij = gp_blades(ei, ej)
            sji, mji = gp_blades(ej, ei)
            if i == j:
                relation_failures += int(not (mij == 0 and mji == 0 and sij == 1 and sji == 1))
            else:
                relation_failures += int(not (mij == mji and sij == -sji))
                if mij.bit_count() != 1:
                    closure_outside_vector += 1
            for k in range(n):
                ek = 1 << k
                s1, m1 = gp_blades(ei, ej)
                left = scale_product(s1, m1, 1, ek)
                s2, m2 = gp_blades(ej, ek)
                right = scale_product(1, ei, s2, m2)
                associativity_failures += int(left != right)
    return {
        "n": n,
        "clifford_dimension": 2 ** n,
        "generator_relation_failures": relation_failures,
        "generator_triple_associativity_failures": associativity_failures,
        "generator_products_outside_vector_sector": closure_outside_vector,
    }


def randomized_audit(trials: int = 8000, seed: int = 114_114) -> dict:
    rng = random.Random(seed)
    assoc_failures = 0
    equivariance_failures = 0
    tested_by_dimension = {n: 0 for n in DIMS}
    for _ in range(trials):
        n = rng.choice(DIMS)
        tested_by_dimension[n] += 1

        def blade():
            k = rng.randint(0, min(n, 10))
            idx = rng.sample(range(n), k)
            m = 0
            for i in idx:
                m |= 1 << i
            return m

        a, b, c = blade(), blade(), blade()
        s1, m1 = gp_blades(a, b)
        left = scale_product(s1, m1, 1, c)
        s2, m2 = gp_blades(b, c)
        right = scale_product(1, a, s2, m2)
        assoc_failures += int(left != right)

        perm = list(range(n))
        rng.shuffle(perm)
        signs = [rng.choice((-1, 1)) for _ in range(n)]
        equivariance_failures += int(not signed_permutation_automorphism_check(a, b, perm, signs))
    return {
        "trials": trials,
        "seed": seed,
        "dimensions": DIMS,
        "tested_by_dimension": tested_by_dimension,
        "associativity_failures": assoc_failures,
        "signed_orthogonal_equivariance_failures": equivariance_failures,
    }


def generate() -> dict:
    exact = [exact_generator_audit(n) for n in range(1, 13)]
    rnd = randomized_audit()
    return {
        "cycle": 114,
        "target": "PDT-II targets (1)/(2): test whether recursive finite-dimensional isotropic closure forces primitive composition VxV->V or n=3.",
        "breakthrough_candidate": False,
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED", "OPEN"],
        "candidate_principle": {
            "hypotheses": [
                "A real Euclidean primitive sector V generates a finite-dimensional algebra A.",
                "Composition is bilinear and recursively closed in A.",
                "Composition is associative.",
                "Orthogonal relabellings of V extend to algebra automorphisms.",
                "The construction exists uniformly under dimension change/refinement."
            ],
            "claim_tested": "These properties force A=V (same-sector closure), or otherwise select n=3.",
            "status": "FALSIFIED"
        },
        "smallest_decisive_counterexamples": {
            "n1_same_sector_failure": "In Cl_1, e1*e1=1, so even one generator leaves the vector sector although the full algebra is finite-dimensional and associative.",
            "n2_distinct_generator_failure": "In Cl_2, e1*e2 is a bivector, not a vector; yet Cl_2 is a finite-dimensional associative recursively closed algebra."
        },
        "surviving_theorem": {
            "status": "PROVED / IMPORTED-KNOWN",
            "statement": "For every finite n, the real Euclidean Clifford algebra Cl_n is an associative algebra generated by V=R^n with relation uv+vu=2<u,v> and vector-space dimension 2^n. Orthogonal transformations of V preserve the relation and extend to algebra automorphisms.",
            "pdt_novelty": "None claimed for Clifford algebra facts. PDT consequence is a no-go: recursive finite-dimensional isotropic closure alone cannot derive V-valued closure or n=3."
        },
        "exact_generator_audit_n1_to_n12": exact,
        "randomized_sparse_audit": rnd,
        "dimension_stress": {
            "tested": DIMS,
            "analytic_extension": "The Clifford construction exists for every finite n; randomized sparse basis-blade tests additionally cover the listed higher n without allocating 2^n-dimensional arrays."
        },
        "pdt_consequence": "Any non-circular n=3 derivation must justify why physically admissible primitive composition is required to close inside V itself, rather than in a larger graded/multivector carrier. Recursive composability, associativity, finite dimensionality and rotational naturality do not provide that justification.",
        "next_obligation": "Derive or falsify a PDT-native same-operational-type/idempotent closure principle strong enough to prohibit scalar/bivector/higher-grade sectors without assuming the desired VxV->V codomain.",
        "prior_art_boundary": "Clifford algebra associativity, 2^n dimension, defining anticommutation relation, and orthogonal naturality are established mathematics; they are used only as a countermodel/prior-art guard.",
        "same_input_prediction_status": "OPEN: this no-go does not generate P_PDT != P_QM.",
        "gravity_capacity_status": "OPEN / NOT ATTACKED: no gravity law is imported from the countermodel."
    }


if __name__ == "__main__":
    result = generate()
    p = Path("results/cycle114_clifford_recursive_closure_no_go.json")
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
