import importlib.util
from pathlib import Path

import numpy as np

MODULE_PATH = Path(__file__).resolve().parents[1] / "cycle093_isotropic_symmetric_companion_no_go.py"
spec = importlib.util.spec_from_file_location("cycle093", MODULE_PATH)
cycle093 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(cycle093)


def test_pi_rotation_is_so_and_flips_two_axes():
    for n in range(2, 13):
        r = cycle093.pi_rotation(n)
        assert np.allclose(r.T @ r, np.eye(n))
        assert np.isclose(np.linalg.det(r), 1.0)
        assert np.allclose(r[:, 0], -np.eye(n)[:, 0])
        assert np.allclose(r[:, 1], -np.eye(n)[:, 1])


def test_fixed_axis_candidate_has_decisive_residual_two():
    for n in list(range(2, 13)) + [16, 24, 32, 48, 64, 96, 128]:
        r = cycle093.pi_rotation(n)
        u = np.zeros(n)
        u[0] = 1.0
        assert np.isclose(cycle093.vector_equivariance_residual(r, u, u, u), 2.0)


def test_scalar_inner_product_survives_full_so_isotropy():
    rng = np.random.default_rng(93002)
    for n in range(2, 13):
        for _ in range(5):
            r = cycle093.random_so(n, rng)
            x = rng.normal(size=n)
            y = rng.normal(size=n)
            assert cycle093.scalar_invariance_residual(r, x, y) < 1e-10


def test_exact_status_boundary():
    assert cycle093.exact_status(1)["same_space_SO_n_symmetric_companion"] == "NONZERO_ALLOWED"
    for n in range(2, 13):
        assert cycle093.exact_status(n)["same_space_SO_n_symmetric_companion"] == "ZERO_ONLY"


def test_frozen_audit_has_requested_dimensions_and_no_breakthrough_claim():
    result = cycle093.run_audit(trials=2)
    tested = [row["n"] for row in result["dims"]]
    assert tested == list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    assert result["breakthrough_candidate"] is False
    assert result["smallest_nondegenerate_obstruction"] == 2
