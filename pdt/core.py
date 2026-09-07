"""Core numerical utilities for Physical Distinction Theory (PDT).

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""
from __future__ import annotations
import numpy as np
from numpy.linalg import eigvalsh, svd

LOG2 = np.log(2.0)

def _as_density(rho):
    rho = np.asarray(rho, dtype=complex)
    rho = (rho + rho.conj().T) / 2
    tr = np.trace(rho)
    if abs(tr) == 0:
        raise ValueError("density matrix has zero trace")
    rho = rho / tr
    vals = eigvalsh(rho)
    if vals.min() < -1e-10:
        raise ValueError("matrix is not positive semidefinite")
    return rho

def von_neumann_entropy(rho, base=2):
    vals = np.clip(eigvalsh(_as_density(rho)).real, 0, 1)
    vals = vals[vals > 1e-15]
    logs = np.log(vals) / np.log(base)
    return float(-np.sum(vals * logs))

def trace_distance(rho, sigma):
    d = _as_density(rho) - _as_density(sigma)
    return float(0.5 * np.sum(svd(d, compute_uv=False)))

def fidelity(rho, sigma):
    rho = _as_density(rho); sigma = _as_density(sigma)
    vals, vecs = np.linalg.eigh(rho)
    sr = (vecs * np.sqrt(np.clip(vals, 0, None))) @ vecs.conj().T
    x = sr @ sigma @ sr
    ex = eigvalsh((x + x.conj().T)/2)
    return float(np.clip(np.sum(np.sqrt(np.clip(ex,0,None)))**2, 0, 1))

def helstrom_error_binary(rho, sigma, prior=0.5):
    if abs(prior - 0.5) > 1e-12:
        a = prior*_as_density(rho) - (1-prior)*_as_density(sigma)
        return float(0.5*(1 - np.sum(svd(a, compute_uv=False))))
    return float(0.5*(1 - trace_distance(rho, sigma)))

def depolarize(rho, p):
    rho = _as_density(rho)
    d = rho.shape[0]
    return (1-p)*rho + p*np.eye(d)/d

def amplitude_damping(rho, gamma):
    rho = _as_density(rho)
    if rho.shape != (2,2):
        raise ValueError("amplitude damping implementation is qubit-only")
    g = float(gamma)
    k0 = np.array([[1,0],[0,np.sqrt(1-g)]],complex)
    k1 = np.array([[0,np.sqrt(g)],[0,0]],complex)
    return k0@rho@k0.conj().T + k1@rho@k1.conj().T

def pure_state(theta, phi=0.0):
    v = np.array([np.cos(theta/2), np.exp(1j*phi)*np.sin(theta/2)],complex)
    return np.outer(v,v.conj())

def random_density(d, rng):
    a = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    rho = a@a.conj().T
    return rho/np.trace(rho)

def equatorial_codebook(n):
    return [pure_state(np.pi/2, 2*np.pi*k/n) for k in range(n)]

def resource_bounded_code_capacity(states, epsilon=0.1, budget=None):
    """Exact maximum log2 codebook size under a pairwise Helstrom-error criterion."""
    states = list(states)
    if budget is not None:
        if callable(budget):
            states = [s for i,s in enumerate(states) if budget(i,s)]
        else:
            states = [s for s,m in zip(states,budget) if m]
    n = len(states)
    if n == 0:
        return 0.0, []
    compat = np.eye(n, dtype=bool)
    for i in range(n):
        for j in range(i+1,n):
            ok = helstrom_error_binary(states[i],states[j]) <= epsilon + 1e-12
            compat[i,j]=compat[j,i]=ok
    best=[]
    def expand(clique, candidates):
        nonlocal best
        if len(clique)+len(candidates) <= len(best):
            return
        while candidates:
            v=candidates.pop()
            new_c=[u for u in candidates if compat[v,u] and all(compat[u,w] for w in clique)]
            nc=clique+[v]
            if len(nc)>len(best): best=nc
            expand(nc,new_c)
            if len(clique)+len(candidates)<=len(best): return
    expand([], list(range(n)))
    return float(np.log2(max(1,len(best)))), best

def chsh_value(a0,a1,b0,b1):
    """CHSH value for planar Bloch-vector observables on a singlet state."""
    def unit(x):
        x=np.asarray(x,float); return x/np.linalg.norm(x)
    a0,a1,b0,b1=map(unit,(a0,a1,b0,b1))
    return float(abs(-a0@b0 - a0@b1 - a1@b0 + a1@b1))

def random_chsh_search(samples=100000, seed=7):
    rng=np.random.default_rng(seed)
    best=0.0; arg=None
    for _ in range(samples):
        ang=rng.uniform(0,2*np.pi,4)
        vec=[np.array([np.cos(t),np.sin(t)]) for t in ang]
        s=chsh_value(*vec)
        if s>best: best=s; arg=ang
    return best,arg

def causal_diamond_capacity_deficit(curvature_projection, L, alpha=1/24):
    """Toy leading-order curvature/capacity consistency model."""
    return alpha*curvature_projection*(L**2)
