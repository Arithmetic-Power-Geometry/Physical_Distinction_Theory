import math
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
EPS = 0.1
SEED = 148
TOL = 1e-10


def resource(q, eps=EPS):
    """Continuous symmetric homogeneous counterfamily.

    For nonnegative q with total S>0, let p=q/S and c=sum_i p_i^2. Then

        F(q)=S[1+eps*c*(1-c)*sin^2(pi/c)].

    This is zero-padding stable and agrees with the additive ledger on every
    equal-support uniform vector because c=1/k there and sin(pi*k)=0.
    """
    q = np.asarray(q, dtype=float)
    if np.any(q < 0):
        raise ValueError("q must be nonnegative")
    S = float(np.sum(q))
    if S == 0.0:
        return 0.0
    p = q / S
    c = float(np.dot(p, p))
    return float(S * (1.0 + eps * c * (1.0 - c) * math.sin(math.pi / c) ** 2))


def uniform(total, n):
    return np.full(n, total / n, dtype=float)


def audit():
    rng = np.random.default_rng(SEED)
    failures = {
        "uniformization_nonincrease": 0,
        "permutation": 0,
        "homogeneity": 0,
        "zero_padding": 0,
    }
    max_relative_residual = 0.0
    cases = 0

    for n in DIMS:
        reps = 80 if n <= 32 else 30
        for _ in range(reps):
            q = rng.lognormal(mean=0.0, sigma=2.0, size=n)
            total = float(np.sum(q))
            fq = resource(q)

            # Maximal equalization/coarse-graining never increases F.
            fu = resource(uniform(total, n))
            if fu > fq + TOL * max(1.0, abs(fq)):
                failures["uniformization_nonincrease"] += 1

            fp = resource(q[rng.permutation(n)])
            res = abs(fp - fq) / max(1.0, abs(fq))
            failures["permutation"] += int(res > TOL)
            max_relative_residual = max(max_relative_residual, res)

            a = 10.0 ** rng.uniform(-6.0, 6.0)
            fh = resource(a * q)
            target = a * fq
            res = abs(fh - target) / max(1.0, abs(target))
            failures["homogeneity"] += int(res > TOL)
            max_relative_residual = max(max_relative_residual, res)

            fz = resource(np.concatenate([q, np.zeros(3)]))
            res = abs(fz - fq) / max(1.0, abs(fq))
            failures["zero_padding"] += int(res > TOL)
            max_relative_residual = max(max_relative_residual, res)
            cases += 1

    # Exact majorization chain: (1,0) majorizes (3/4,1/4), which majorizes
    # (1/2,1/2). Endpoints both have F=1, while the interior has F>1.
    vertex = np.array([1.0, 0.0])
    interior = np.array([0.75, 0.25])
    equal = np.array([0.5, 0.5])

    return {
        "cycle": 148,
        "seed": SEED,
        "dimensions": DIMS,
        "random_cases": cases,
        "failures": failures,
        "max_relative_residual": max_relative_residual,
        "majorization_chain": {
            "vertex": vertex.tolist(),
            "interior": interior.tolist(),
            "uniform": equal.tolist(),
            "F_vertex": resource(vertex),
            "F_interior": resource(interior),
            "F_uniform": resource(equal),
            "interior_excess": resource(interior) - 1.0,
        },
        "classification": {
            "PROVED": "The explicit counterfamily has the stated algebraic properties.",
            "FALSIFIED": "Maximal uniformization monotonicity plus calibration implies global Schur monotonicity.",
            "NUMERICALLY_SUPPORTED": "Dimension/random stress audit is a regression check only.",
            "OPEN": "Derive arbitrary partial T-transform monotonicity from PDT-native operations.",
            "BREAKTHROUGH_CANDIDATE": False,
        },
    }


if __name__ == "__main__":
    import json
    print(json.dumps(audit(), indent=2))
