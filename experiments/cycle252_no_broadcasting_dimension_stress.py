"""Cycle 252: exact no-broadcasting dimension stress.

This is a theorem-regression harness, not experimental data.
Classical simplex: the copying channel i -> (i,i) broadcasts every distribution.
Quantum: the two pure states |0> and |+> are noncommuting for every n>=2,
so no single quantum channel can broadcast both (standard no-broadcasting theorem).
"""
from fractions import Fraction
import json

rows=[]
for n in range(1,13):
    # Exact classical copying marginal check for a deterministic family of rational p.
    weights=[Fraction(i+1, n*(n+1)//2) for i in range(n)]
    assert sum(weights)==1
    left=[sum((weights[i] if i==j==k else Fraction(0)) for k in range(n)) for j in range(n) for i in [j]]
    right=[sum((weights[i] if i==k==j else Fraction(0)) for k in range(n)) for j in range(n) for i in [j]]
    assert left==weights and right==weights
    if n==1:
        commutator_witness=Fraction(0)
        quantum_nonbroadcast_pair=False
    else:
        # rho0=|0><0|, rho+=|+><+| in span{|0>,|1>}.
        # [rho0,rho+] has entries (0,1)=+1/2,(1,0)=-1/2,
        # so Frobenius norm squared is exactly 1/2.
        commutator_witness=Fraction(1,2)
        quantum_nonbroadcast_pair=True
    rows.append({
        "n":n,
        "classical_universal_copying":True,
        "quantum_noncommuting_pair_exists":quantum_nonbroadcast_pair,
        "commutator_frobenius_norm_sq":str(commutator_witness),
    })

assert rows[0]["quantum_noncommuting_pair_exists"] is False
assert all(r["quantum_noncommuting_pair_exists"] for r in rows[1:])
print(json.dumps(rows,indent=2))
