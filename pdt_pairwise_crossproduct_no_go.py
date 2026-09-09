"""Cycle 036: pairwise cross-product dimension-selection no-go.

This module audits a precise limitation of the current NDC dimension route.
The 3D and standard octonionic 7D cross products both satisfy the same
pairwise package: bilinearity, alternation, orthogonality, the norm identity,
and the repeated-input double-cross identity

    x × (x × y) = <x,y>x - ||x||^2 y.

Therefore this package cannot select n=3. A genuinely three-dimensional
filter must use additional structure that sees three independent inputs
(e.g. Jacobi/sequential consistency), stronger symmetry, or another PDT-native
principle. The underlying cross-product mathematics is established prior art.
"""
from __future__ import annotations
import numpy as np

FANO_TRIPLES = ((0,1,2),(0,3,4),(0,6,5),(1,3,5),(1,4,6),(2,3,6),(2,5,4))


def cross3(a, b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    if a.shape != (3,) or b.shape != (3,):
        raise ValueError("cross3 expects length-3 vectors")
    return np.cross(a,b)


def cross7(a, b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    if a.shape != (7,) or b.shape != (7,):
        raise ValueError("cross7 expects length-7 vectors")
    out=np.zeros(7,float)
    for i,j,k in FANO_TRIPLES:
        for x,y,z in ((i,j,k),(j,k,i),(k,i,j)):
            out[z] += a[x]*b[y] - a[y]*b[x]
    return out


def pairwise_residuals(a,b,cross):
    a=np.asarray(a,float); b=np.asarray(b,float)
    x=cross(a,b)
    alt=np.linalg.norm(cross(a,a))
    orth=max(abs(float(np.dot(a,x))),abs(float(np.dot(b,x))))
    norm=abs(float(np.dot(x,x) - (np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2)))
    double=np.linalg.norm(cross(a,cross(a,b)) - (np.dot(a,b)*a-np.dot(a,a)*b))
    return {"alternation":float(alt),"orthogonality":float(orth),"norm_identity":float(norm),"double_cross":float(double)}


def exact_basis_audit(dim:int):
    if dim not in (3,7):
        raise ValueError("explicit pairwise models implemented only for n=3,7")
    cross=cross3 if dim==3 else cross7
    e=np.eye(dim)
    maxima={"alternation":0.0,"orthogonality":0.0,"norm_identity":0.0,"double_cross":0.0}
    for i in range(dim):
        for j in range(dim):
            r=pairwise_residuals(e[i],e[j],cross)
            for k,v in r.items(): maxima[k]=max(maxima[k],v)
    return {"n":dim,**maxima,"passes_pairwise_package":all(v==0.0 for v in maxima.values())}


def randomized_audit(dim:int,trials:int=2000,seed:int=36036):
    if dim not in (3,7):
        raise ValueError("explicit pairwise models implemented only for n=3,7")
    cross=cross3 if dim==3 else cross7
    rng=np.random.default_rng(seed+dim)
    maxima={"alternation":0.0,"orthogonality":0.0,"norm_identity":0.0,"double_cross":0.0}
    for _ in range(trials):
        a=rng.normal(size=dim); b=rng.normal(size=dim)
        r=pairwise_residuals(a,b,cross)
        for k,v in r.items(): maxima[k]=max(maxima[k],v)
    return {"n":dim,"trials":trials,**maxima}


def dimension_status(n:int):
    # Brown-Gray/Hurwitz classification is imported/known mathematics.
    exists_nontrivial_normed_cross_product=n in (3,7)
    passes_pairwise=exists_nontrivial_normed_cross_product
    return {
        "n":int(n),
        "nontrivial_normed_cross_product":exists_nontrivial_normed_cross_product,
        "passes_pairwise_NDC_double_cross":passes_pairwise,
        "selects_n3":False if n in (3,7) else None,
        "status":"SURVIVES_PAIRWISE_FILTER" if passes_pairwise else "EXCLUDED_BY_KNOWN_CLASSIFICATION",
    }


if __name__ == "__main__":
    for n in range(1,13): print(dimension_status(n))
    print(exact_basis_audit(3)); print(exact_basis_audit(7))
    print(randomized_audit(3,500)); print(randomized_audit(7,500))
