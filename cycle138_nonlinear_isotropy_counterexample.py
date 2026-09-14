import json
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 138
TOL = 1e-10

def B(x, y):
    """Dimension-independent nonlinear alternating SO(n)-equivariant counterfamily."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return float(y @ y) * x - float(x @ x) * y

def random_so(rng, n):
    if n == 1:
        return np.ones((1, 1))
    a = rng.normal(size=(n, n))
    q, _ = np.linalg.qr(a)
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1.0
    return q

def relative_residual(lhs, rhs):
    scale = max(1.0, np.linalg.norm(lhs), np.linalg.norm(rhs))
    return float(np.linalg.norm(lhs - rhs) / scale)

def run_audit():
    rng = np.random.default_rng(SEED)
    total = 0
    cov_failures = anti_failures = self_failures = 0
    max_cov = max_anti = max_self = 0.0
    per_dim = []
    for n in DIMS:
        reps = 100 if n <= 32 else 30
        dim_max_cov = 0.0
        for _ in range(reps):
            x = rng.normal(size=n)
            y = rng.normal(size=n)
            R = random_so(rng, n)
            cov = relative_residual(B(R @ x, R @ y), R @ B(x, y))
            anti = relative_residual(B(y, x), -B(x, y))
            self_r = float(np.linalg.norm(B(x, x)))
            max_cov = max(max_cov, cov)
            max_anti = max(max_anti, anti)
            max_self = max(max_self, self_r)
            dim_max_cov = max(dim_max_cov, cov)
            cov_failures += int(cov > TOL)
            anti_failures += int(anti > TOL)
            self_failures += int(self_r > TOL)
            total += 1
        per_dim.append({"n": n, "random_cases": reps,
                        "max_relative_covariance_residual": dim_max_cov,
                        "survives_nonlinear_counterfamily": True})

    x = np.array([1.0]); y = np.array([2.0])
    exact_witness = {
        "n": 1, "x": [1], "y": [2],
        "B_x_y": B(x, y).tolist(),
        "B_2x_y": B(2*x, y).tolist(),
        "two_B_x_y": (2*B(x, y)).tolist(),
        "bilinearity_gap_squared": float(np.sum((B(2*x, y)-2*B(x, y))**2)),
    }
    return {
        "cycle": 138, "seed": SEED, "tolerance": TOL, "dimensions": DIMS,
        "total_random_cases": total,
        "covariance_failures": cov_failures,
        "antisymmetry_failures": anti_failures,
        "self_null_failures": self_failures,
        "max_relative_covariance_residual": max_cov,
        "max_relative_antisymmetry_residual": max_anti,
        "max_self_null_residual": max_self,
        "smallest_decisive_bilinearity_counterexample": exact_witness,
        "per_dimension": per_dim,
        "classification": {
            "proved": "The explicit map is alternating/self-null and SO(n)-equivariant in every tested dimension; algebraically these identities hold for all n.",
            "falsified": "Alternation + self-nullness + full proper-rotation covariance alone select n=3.",
            "open": "Derive a linear-response/bilinearity principle from PDT-native operational primitives without assuming the n=3 conclusion.",
            "breakthrough_candidate": False,
        },
    }

if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
