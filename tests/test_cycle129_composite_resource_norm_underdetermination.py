import importlib.util
from pathlib import Path

import numpy as np

MODULE_PATH = Path(__file__).resolve().parents[1] / "experiments" / "cycle129_composite_resource_norm_underdetermination.py"
spec = importlib.util.spec_from_file_location("cycle129", MODULE_PATH)
cycle129 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(cycle129)


def test_rank_one_all_schatten_norms_agree():
    x = np.array([1.0, -2.0, 3.0])
    y = np.array([4.0, 5.0, -1.0])
    matrix = np.outer(x, y)
    target = np.linalg.norm(x) * np.linalg.norm(y)
    for p in cycle129.PS:
        assert np.isclose(cycle129.schatten_norm(matrix, p), target, rtol=1e-12, atol=1e-12)


def test_zero_simple_tensor_edge_case():
    x = np.zeros(4)
    y = np.arange(1.0, 5.0)
    matrix = np.outer(x, y)
    for p in cycle129.PS:
        assert cycle129.schatten_norm(matrix, p) == 0.0


def test_local_orthogonal_covariance():
    rng = np.random.default_rng(129)
    matrix = rng.normal(size=(5, 5))
    left, _ = np.linalg.qr(rng.normal(size=(5, 5)))
    right, _ = np.linalg.qr(rng.normal(size=(5, 5)))
    transformed = left @ matrix @ right.T
    for p in cycle129.PS:
        assert np.isclose(
            cycle129.schatten_norm(matrix, p),
            cycle129.schatten_norm(transformed, p),
            rtol=1e-12,
            atol=1e-12,
        )


def test_smallest_decisive_counterexample_is_n2_identity():
    identity = np.eye(2)
    values = [cycle129.schatten_norm(identity, p) for p in cycle129.PS]
    assert np.isclose(values[0], 2.0)
    assert np.isclose(values[1], np.sqrt(2.0))
    assert np.isclose(values[2], 2.0 ** 0.25)
    assert np.isclose(values[3], 1.0)
    assert len({round(v, 12) for v in values}) == 4


def test_full_audit_has_no_regression_failures():
    result = cycle129.run_audit()
    assert result["rank_one_failures"] == 0
    assert result["local_orthogonal_invariance_failures"] == 0
    assert result["smallest_decisive_dimension"] == 2
    assert result["breakthrough_candidate"] is False
