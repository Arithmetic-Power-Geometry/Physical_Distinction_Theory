import random

from pdt_orbit_completeness import (
    scalar_orbit_complete,
    su_scalar_isotropy_witness,
    tpi_partition_test,
)


def test_scalar_completeness_is_tpi_on_adversarial_partitions():
    rng = random.Random(20260909)
    for n in range(1, 40):
        for _ in range(50):
            levels = [rng.randrange(max(1, n // 3 + 1)) for _ in range(n)]
            orbits = [rng.randrange(max(1, n // 3 + 1)) for _ in range(n)]
            assert scalar_orbit_complete(levels, orbits) == tpi_partition_test(levels, orbits)


def test_su_counterexamples_real_dimensions_4_to_12():
    for m in range(2, 7):
        witness = su_scalar_isotropy_witness(m, a=0.5)
        assert witness["real_dimension"] == 2 * m
        assert witness["same_scalar_level"] is True
        assert witness["same_stabilizer_orbit_possible"] is False
        assert abs(witness["distance_sq_xy"] - 2.0) < 1e-12
        assert abs(witness["distance_sq_xz"] - 2.0) < 1e-12


def test_su_witness_parameter_stress():
    for m in range(2, 20):
        for a in (1e-6, 0.1, 0.25, 0.5, 0.9, 1.0 - 1e-6):
            witness = su_scalar_isotropy_witness(m, a=a)
            assert witness["same_scalar_level"] is True
            assert witness["same_stabilizer_orbit_possible"] is False
