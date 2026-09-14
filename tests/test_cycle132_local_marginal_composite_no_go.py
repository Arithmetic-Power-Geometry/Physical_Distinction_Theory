import numpy as np

from cycle132_local_marginal_composite_no_go import DIMS, run_audit, witness


def test_local_profiles_match():
    for n in DIMS:
        a, b = witness(n)
        assert np.allclose(np.linalg.norm(a, axis=1), np.linalg.norm(b, axis=1), atol=1e-12)
        assert np.allclose(np.linalg.norm(a, axis=0), np.linalg.norm(b, axis=0), atol=1e-12)


def test_smallest_nontrivial_witness_is_decisive():
    result = run_audit()
    n2 = next(r for r in result["records"] if r["n"] == 2)
    assert abs(n2["schatten"]["1"]["gap_B_minus_A"]) > 1e-10
    assert abs(n2["schatten"]["4"]["gap_B_minus_A"]) > 1e-10
    assert abs(n2["schatten"]["inf"]["gap_B_minus_A"]) > 1e-10
    assert abs(n2["schatten"]["2"]["gap_B_minus_A"]) < 1e-10


def test_all_stress_dimensions():
    checks = run_audit()["checks"]
    assert checks["local_profile_failures"] == 0
    assert checks["p1_distinguishes_for_all_n_gt_1"]
    assert checks["p4_distinguishes_for_all_n_gt_1"]
    assert checks["pinf_distinguishes_for_all_n_gt_1"]
    assert not checks["p2_distinguishes_for_any_n_gt_1"]
