import numpy as np
from cycle066_petz_family_nonclosure import endpoint_witness, stress, base_witness, petz_moment, R4, S4, hadamard


def test_endpoint_witness_same_ns_different_trace_distance():
    w=endpoint_witness()
    assert w["dimension"]==4
    assert w["max_ns_difference"] < 1e-14
    assert w["separation"] > 0.07


def test_all_sampled_petz_moments_identical():
    for alpha in [0.1,0.25,0.5,0.9,1.1,1.5,2.0,3.0]:
        a=petz_moment(alpha,R4,S4,hadamard(0.0))
        b=petz_moment(alpha,R4,S4,hadamard(np.pi))
        assert abs(a-b) < 1e-13


def test_dimension_stress():
    out=stress()
    for rec in out["records"]:
        if rec.get("witness_available"):
            assert rec["max_ns_drift"] < 1e-13
            assert rec["trace_distance_spread"] > 1e-3
