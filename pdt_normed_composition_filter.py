"""Cycle 030: normed distinction composition and Jacobi dimension filter.

The classification {0,1,3,7} is a known theorem for Euclidean vector cross
products. This module does not re-prove that classification computationally;
it provides exact constructions and falsification witnesses for the two
nontrivial dimensions 3 and 7.
"""
from __future__ import annotations
import numpy as np

FANO_TRIPLES = ((0,1,2),(0,3,4),(0,6,5),(1,3,5),(1,4,6),(2,3,6),(2,5,4))

def cross3(a, b):
    a = np.asarray(a, dtype=float); b = np.asarray(b, dtype=float)
    if a.shape != (3,) or b.shape != (3,):
        raise ValueError("cross3 expects length-3 vectors")
    return np.cross(a, b)

def cross7(a, b):
    a = np.asarray(a, dtype=float); b = np.asarray(b, dtype=float)
    if a.shape != (7,) or b.shape != (7,):
        raise ValueError("cross7 expects length-7 vectors")
    out = np.zeros(7, dtype=float)
    for i,j,k in FANO_TRIPLES:
        for x,y,z in ((i,j,k),(j,k,i),(k,i,j)):
            out[z] += a[x]*b[y] - a[y]*b[x]
    return out

def jacobiator(a,b,c,cross):
    return cross(a,cross(b,c)) + cross(b,cross(c,a)) + cross(c,cross(a,b))

def norm_identity_residual(a,b,cross):
    a=np.asarray(a,float); b=np.asarray(b,float)
    lhs=float(np.dot(cross(a,b),cross(a,b)))
    rhs=float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2)
    return lhs-rhs

def orthogonality_residual(a,b,cross):
    x=cross(a,b)
    return max(abs(float(np.dot(x,a))), abs(float(np.dot(x,b))))

def explicit_7d_jacobi_witness():
    e=np.eye(7)
    a,b,c=e[0],e[1],e[3]
    j=jacobiator(a,b,c,cross7)
    return a,b,c,j

def classification_row(n: int):
    # Known Brown-Gray/Hurwitz classification, not a computational discovery.
    normed_nontrivial = n in (3,7)
    jacobi_compatible = n == 3
    return {
        "n": int(n),
        "nontrivial_normed_cross_product": normed_nontrivial,
        "jacobi_compatible_known_model": jacobi_compatible,
        "passes_NDC_plus_JSC": normed_nontrivial and jacobi_compatible,
        "status": "CONDITIONAL" if n == 3 else ("FALSIFIED_BY_CLASSIFICATION" if not normed_nontrivial else "FALSIFIED_BY_JACOBI"),
    }

def randomized_audit(dim: int, trials: int=1000, seed: int=30030):
    if dim not in (3,7):
        raise ValueError("explicit models are implemented only for n=3 and n=7")
    rng=np.random.default_rng(seed+dim)
    cross=cross3 if dim==3 else cross7
    max_norm=max_orth=max_jac=0.0
    for _ in range(trials):
        a,b,c=(rng.normal(size=dim) for __ in range(3))
        max_norm=max(max_norm,abs(norm_identity_residual(a,b,cross)))
        max_orth=max(max_orth,orthogonality_residual(a,b,cross))
        max_jac=max(max_jac,float(np.linalg.norm(jacobiator(a,b,c,cross))))
    return {
        "n":dim, "trials":trials,
        "max_norm_identity_residual":max_norm,
        "max_orthogonality_residual":max_orth,
        "max_jacobiator_norm":max_jac,
    }

if __name__ == "__main__":
    for n in range(1,13):
        print(classification_row(n))
    print(randomized_audit(3, 500))
    print(randomized_audit(7, 500))
    print("7D witness jacobiator:", explicit_7d_jacobi_witness()[-1])
