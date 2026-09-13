from __future__ import annotations
import itertools, json
from pathlib import Path
import numpy as np

DIMS = list(range(1,13)) + [16,24,32,48,64,96,128]


def mul(C,x,y):
    return np.einsum('ijk,j,k->i', C, x, y)

def assoc(C,x,y,z):
    return mul(C,mul(C,x,y),z)-mul(C,x,mul(C,y,z))

def comm(C,x,y):
    return mul(C,x,y)-mul(C,y,x)

def jacobi_left(C,x,y,z):
    return comm(C,x,comm(C,y,z))+comm(C,y,comm(C,z,x))+comm(C,z,comm(C,x,y))

def alt_assoc(C,x,y,z):
    return (assoc(C,x,y,z)+assoc(C,y,z,x)+assoc(C,z,x,y)
            -assoc(C,x,z,y)-assoc(C,z,y,x)-assoc(C,y,x,z))

def lie_admissible_witness(n):
    C=np.zeros((n,n,n),dtype=int)
    if n>=2:
        C[1,0,1]=1  # e1*e2=e2, 0-based
    return C

FANO=((1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5))
def oct_tensor():
    C=np.zeros((8,8,8),dtype=int)
    C[0,0,0]=1
    for i in range(1,8):
        C[i,0,i]=1; C[i,i,0]=1; C[0,i,i]=-1
    for a,b,c in FANO:
        cyc=((a,b,c),(b,c,a),(c,a,b))
        for i,j,k in cyc:
            C[k,i,j]=1; C[k,j,i]=-1
    return C

def basis(n,i):
    x=np.zeros(n,dtype=int); x[i]=1; return x

def exact_general_identity_audit():
    rng=np.random.default_rng(110)
    checks=0; failures=0; max_abs=0
    for n in range(1,7):
        for _ in range(120):
            C=rng.integers(-2,3,size=(n,n,n))
            x=rng.integers(-2,3,size=n); y=rng.integers(-2,3,size=n); z=rng.integers(-2,3,size=n)
            r=jacobi_left(C,x,y,z)+alt_assoc(C,x,y,z)
            checks += 1
            m=int(np.max(np.abs(r))) if r.size else 0
            max_abs=max(max_abs,m); failures += int(m!=0)
    return {'checks':checks,'failures':failures,'max_abs_residual':max_abs}

def dimension_countermodel_audit():
    rows=[]
    for n in DIMS:
        if n==1:
            rows.append({'n':n,'nonassociative_witness':False,'jacobi_exact':True,'basis_triples_checked':1})
            continue
        C=lie_admissible_witness(n)
        a=assoc(C,basis(n,0),basis(n,0),basis(n,1))
        nonassoc=bool(np.any(a))
        if n<=12:
            bad=0
            for i,j,k in itertools.product(range(n),repeat=3):
                if np.any(jacobi_left(C,basis(n,i),basis(n,j),basis(n,k))): bad+=1
            checked=n**3
        else:
            # exact structural certificate: bracket is [e1,e2]=e2 and all others zero,
            # the 2D affine Lie algebra plus an abelian central summand.
            bad=0; checked='analytic: aff(1) direct-sum abelian'
        rows.append({'n':n,'nonassociative_witness':nonassoc,'assoc_witness':'A(e1,e1,e2)=-e2','jacobi_bad_basis_triples':bad,'basis_triples_checked':checked})
    return rows

def octonion_audit():
    C=oct_tensor(); e=lambda i:basis(8,i)
    A=assoc(C,e(1),e(2),e(4))
    J=jacobi_left(C,e(1),e(2),e(4))
    # half-commutator cross product Jacobiator is 1/4 of commutator Jacobiator
    nonzero_A=0; relation_fail=0
    for i,j,k in itertools.product(range(1,8),repeat=3):
        a=assoc(C,e(i),e(j),e(k)); jv=jacobi_left(C,e(i),e(j),e(k))
        nonzero_A += int(np.any(a))
        relation_fail += int(np.any(jv + 6*a))
    return {'A_e1_e2_e4':A.tolist(),'Jcomm_e1_e2_e4':J.tolist(),
            'Jcross_e1_e2_e4':(J/4).tolist(),'ordered_imaginary_triples':343,
            'nonzero_associators':nonzero_A,'Jcomm_plus_6A_failures':relation_fail}

def generate():
    general=exact_general_identity_audit(); dims=dimension_countermodel_audit(); octa=octonion_audit()
    return {
      'cycle':110,
      'target':'PDT-II targets (1)/(2): test whether Jacobi coherence can be derived/used as a non-circular composition selector.',
      'classification':['PROVED','FALSIFIED','IMPORTED/KNOWN','NUMERICALLY_SUPPORTED','OPEN'],
      'breakthrough_candidate':False,
      'theorems':{
        'akivis_identity_convention':{'status':'PROVED / IMPORTED-KNOWN','statement':'For A=(xy)z-x(yz) and J_L=[x,[y,z]]+cyclic, J_L=-Alt(A).'},
        'alternative_boundary':{'status':'PROVED / IMPORTED-KNOWN','statement':'If A is alternating, Alt(A)=6A, hence J_L=-6A. Therefore in an alternative algebra the commutator satisfies Jacobi iff the product is associative.'},
        'jacobi_dimension_selector':{'status':'FALSIFIED','statement':'Jacobi of the commutator does not select n=3. A nonassociative Lie-admissible algebra exists in dimension 2 and extends by an abelian zero-product summand to every n>=2.'},
        'weaker_than_associativity_in_alternative_branch':{'status':'FALSIFIED','statement':'Within the alternative branch, Jacobi is not a weaker independent coherence axiom; it is equivalent to associativity.'}
      },
      'smallest_counterexample':{
        'dimension':2,
        'product':'e1*e2=e2; all other basis products zero',
        'associator':'A(e1,e1,e2)=-e2 != 0',
        'commutator':'[e1,e2]=e2, the 2D affine Lie algebra, so Jacobi holds identically.'
      },
      'general_identity_exact_audit':general,
      'dimension_audit':dims,
      'octonion_scaling_audit':octa,
      'prior_art_boundary':'Lie-admissible algebras, the Akivis identity, alternative algebras, and Malcev-admissibility of octonion commutators are established mathematics; no novelty is claimed for these algebraic facts.',
      'pdt_consequence':'Cycle 109 cannot be made non-circular merely by postulating Jacobi. Without cross-product/alternative structure Jacobi is dimension-blind; with alternativity it collapses to associativity. PDT still needs an operationally derived law that is neither generic Jacobi nor associativity in disguise.',
      'surviving_obligations':[
        'Derive a composition constraint from PDT distinction/resource operations before choosing a Lie/cross-product algebraic representation.',
        'Search for a measurable resource/revelation identity whose algebraic image excludes both the 2D Lie-admissible countermodel and the 7D octonionic branch.',
        'Do not claim an n=3 derivation or PDT-vs-QM probability departure from Jacobi alone.'
      ]
    }

if __name__=='__main__':
    d=generate(); Path('results').mkdir(exist_ok=True); Path('results/cycle110_jacobi_associator_boundary.json').write_text(json.dumps(d,indent=2)+'\n'); print(json.dumps(d,indent=2))
