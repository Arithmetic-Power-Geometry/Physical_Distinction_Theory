import json
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 140
TOL = 1e-10

def B(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return np.linalg.norm(y) * x - np.linalg.norm(x) * y

def random_so(rng, n):
    if n == 1:
        return np.ones((1, 1))
    a = rng.normal(size=(n, n))
    q, _ = np.linalg.qr(a)
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1.0
    return q

def rel(lhs, rhs):
    s = max(1.0, float(np.linalg.norm(lhs)), float(np.linalg.norm(rhs)))
    return float(np.linalg.norm(lhs-rhs)/s)

def run_audit():
    rng = np.random.default_rng(SEED)
    totals = dict(cases=0, covariance_failures=0, homogeneity_failures=0, antisymmetry_failures=0, sector_null_failures=0)
    max_cov = max_hom = 0.0
    for n in DIMS:
        reps = 50 if n <= 32 else 20
        for _ in range(reps):
            x = rng.normal(size=n); y = rng.normal(size=n)
            R = random_so(rng, n); t = float(rng.uniform(0.05,3.0))
            cov = rel(B(R@x,R@y), R@B(x,y))
            hom = rel(B(t*x,t*y), t*t*B(x,y))
            anti = rel(B(y,x), -B(x,y))
            sec = max(np.linalg.norm(B(x,np.zeros(n))), np.linalg.norm(B(np.zeros(n),y)))
            totals['cases'] += 1
            totals['covariance_failures'] += int(cov>TOL)
            totals['homogeneity_failures'] += int(hom>TOL)
            totals['antisymmetry_failures'] += int(anti>TOL)
            totals['sector_null_failures'] += int(sec>TOL)
            max_cov=max(max_cov,cov); max_hom=max(max_hom,hom)
    ux,uy=np.array([1.0]),np.array([0.0])
    vx,vy=np.array([0.0]),np.array([-1.0])
    gap=B(ux+vx,uy+vy)+B(ux-vx,uy-vy)-2*B(ux,uy)-2*B(vx,vy)
    return {'cycle':140,'dimensions':DIMS,**totals,'max_covariance_residual':max_cov,'max_positive_quadratic_homogeneity_residual':max_hom,'smallest_non_hessian_witness':{'n':1,'parallelogram_gap':gap.tolist(),'gap_squared':float(np.sum(gap*gap))},'breakthrough_candidate':False}

if __name__ == '__main__':
    print(json.dumps(run_audit(), indent=2))
