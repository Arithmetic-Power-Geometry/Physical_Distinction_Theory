"""PDT Cycle 139: quadratic-null regularity bridge to the conditional n=3 selector.

This executable audit does not prove PDT primitives imply the hypotheses. It stress-tests
two exact counterfamilies used to isolate which hypotheses are necessary.
"""
import json
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 139
TOL = 1e-10

def degree2_counterfamily(x, y):
    return np.linalg.norm(y) * x - np.linalg.norm(x) * y

def cubic_counterfamily(x, y):
    return float(y @ y) * x - float(x @ x) * y

def random_so(rng, n):
    if n == 1:
        return np.ones((1, 1))
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1.0
    return q

def rel(a, b):
    return float(np.linalg.norm(a-b) / max(1.0, np.linalg.norm(a), np.linalg.norm(b)))

def audit():
    rng = np.random.default_rng(SEED)
    failures = {k: 0 for k in (
        "degree2_covariance", "degree2_antisymmetry", "degree2_null",
        "degree2_scaling", "cubic_covariance", "cubic_antisymmetry",
        "cubic_null", "cubic_degree3_scaling")}
    maxima = {k: 0.0 for k in failures}
    cubic_degree2_violations = 0
    cases = 0
    for n in DIMS:
        reps = 80 if n <= 32 else 25
        for _ in range(reps):
            x = rng.normal(size=n); y = rng.normal(size=n)
            R = random_so(rng, n); t = rng.uniform(0.15, 2.5); z = np.zeros(n)
            checks = {
                "degree2_covariance": rel(degree2_counterfamily(R@x,R@y), R@degree2_counterfamily(x,y)),
                "degree2_antisymmetry": rel(degree2_counterfamily(y,x), -degree2_counterfamily(x,y)),
                "degree2_null": np.linalg.norm(degree2_counterfamily(x,z))+np.linalg.norm(degree2_counterfamily(z,y)),
                "degree2_scaling": rel(degree2_counterfamily(t*x,t*y), t**2*degree2_counterfamily(x,y)),
                "cubic_covariance": rel(cubic_counterfamily(R@x,R@y), R@cubic_counterfamily(x,y)),
                "cubic_antisymmetry": rel(cubic_counterfamily(y,x), -cubic_counterfamily(x,y)),
                "cubic_null": np.linalg.norm(cubic_counterfamily(x,z))+np.linalg.norm(cubic_counterfamily(z,y)),
                "cubic_degree3_scaling": rel(cubic_counterfamily(t*x,t*y), t**3*cubic_counterfamily(x,y)),
            }
            for key, value in checks.items():
                maxima[key] = max(maxima[key], float(value)); failures[key] += int(value > TOL)
            cubic_degree2_violations += int(rel(cubic_counterfamily(t*x,t*y), t**2*cubic_counterfamily(x,y)) > TOL)
            cases += 1
    return {"cycle":139,"dimensions":DIMS,"seed":SEED,"tolerance":TOL,"cases_per_family":cases,
            "failures":failures,"max_residuals":maxima,"cubic_degree2_violations":cubic_degree2_violations,
            "exact_degree2_nonquadratic_witness":{"dimension":1,"u":[1,1],"v":[1,-1],"parallelogram_lhs":0,"parallelogram_rhs":4,"gap":-4}}

if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
