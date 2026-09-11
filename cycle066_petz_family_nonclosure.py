"""Cycle 066: full Petz/Nussbaum-Szkola scalar-family nonclosure.

A 4x4 complex-Hadamard phase family keeps the complete Nussbaum-Szkola
classical pair (hence every Petz f-divergence / Petz-Renyi moment) fixed while
quantum trace distance changes. This is a PDT-II composition search boundary,
not a novelty claim for Petz or Nussbaum-Szkola theory.
"""
import json
import numpy as np

R4=np.array([0.55,0.25,0.15,0.05],float)
S4=np.array([0.50,0.25,0.15,0.10],float)


def hadamard(theta):
    z=np.exp(1j*theta)
    return 0.5*np.array([[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]],complex)


def trace_distance(rho,sigma):
    return float(0.5*np.abs(np.linalg.eigvalsh(rho-sigma)).sum())


def ns_pair(r,s,U):
    m=np.abs(U)**2
    return r[:,None]*m, s[None,:]*m


def petz_moment(alpha,r,s,U):
    m=np.abs(U)**2
    return float(np.sum((r[:,None]**alpha)*(s[None,:]**(1-alpha))*m))


def base_witness(theta):
    U=hadamard(theta)
    rho=U@np.diag(R4)@U.conj().T
    sigma=np.diag(S4)
    p,q=ns_pair(R4,S4,U)
    return rho,sigma,p,q


def endpoint_witness():
    rho0,sigma,p0,q0=base_witness(0.0)
    rhop,_,pp,qp=base_witness(np.pi)
    return {
        "dimension":4,
        "trace_distance_theta_0":trace_distance(rho0,sigma),
        "trace_distance_theta_pi":trace_distance(rhop,sigma),
        "separation":abs(trace_distance(rhop,sigma)-trace_distance(rho0,sigma)),
        "max_ns_difference":max(float(np.max(np.abs(p0-pp))),float(np.max(np.abs(q0-qp)))),
    }


def embedded_family(n,theta):
    if n<4:
        raise ValueError("Hadamard witness requires n>=4")
    if n==4:
        r,s=R4.copy(),S4.copy()
    else:
        block=0.8
        tail=(1-block)/(n-4)
        r=np.concatenate([block*R4,np.full(n-4,tail)])
        s=np.concatenate([block*S4,np.full(n-4,tail)])
    U=np.eye(n,dtype=complex)
    U[:4,:4]=hadamard(theta)
    rho=U@np.diag(r)@U.conj().T
    sigma=np.diag(s)
    return r,s,U,rho,sigma


def stress():
    dims=list(range(1,13))+[16,24,32,48,64,96,128]
    records=[]
    for n in dims:
        if n<4:
            records.append({"n":n,"witness_available":False,"classification":"DEGENERATE_FOR_THIS_FAMILY"})
            continue
        refp=refq=None
        max_drift=0.0
        vals=[]
        for theta in np.linspace(0,np.pi,65):
            r,s,U,rho,sigma=embedded_family(n,theta)
            p,q=ns_pair(r,s,U)
            if refp is None:
                refp,refq=p,q
            max_drift=max(max_drift,float(np.max(np.abs(p-refp))),float(np.max(np.abs(q-refq))))
            vals.append(trace_distance(rho,sigma))
        records.append({"n":n,"witness_available":True,"trace_distance_min":min(vals),"trace_distance_max":max(vals),"trace_distance_spread":max(vals)-min(vals),"max_ns_drift":max_drift})
    return {"endpoint":endpoint_witness(),"records":records}


if __name__=="__main__":
    print(json.dumps(stress(),indent=2))
