import numpy as np

from cycle063_quantum_operational_closure_audit import (
    _random_density,
    _random_kernel,
    _random_povm,
    _random_unitary,
    pdt_closed_probabilities,
    qm_probabilities,
    run_audit,
)


def test_cycle063_dimension_sweep_passes():
    result = run_audit(dimensions=range(1, 13), trials_low=8, trials_high=8, seed=63063)
    assert result["status"] == "PASS"
    assert result["failures"] == 0


def test_cycle063_resource_postprocessing_preserves_equality():
    rng = np.random.default_rng(63)
    for d in (1, 2, 3, 4, 8, 12):
        rho = _random_density(d, rng, pure=False)
        effects = _random_povm(d, 4, rng)
        p = qm_probabilities(rho, effects)
        q = pdt_closed_probabilities(rho, effects)
        K = _random_kernel(3, 4, rng)
        assert np.allclose(K @ p, K @ q, atol=5e-11, rtol=0)


def test_cycle063_common_unitary_dynamics_preserves_equality():
    rng = np.random.default_rng(630)
    for d in (2, 3, 5, 7, 12):
        rho = _random_density(d, rng, pure=True)
        effects = _random_povm(d, 3, rng)
        U = _random_unitary(d, rng)
        evolved = U @ rho @ U.conj().T
        assert np.allclose(
            qm_probabilities(evolved, effects),
            pdt_closed_probabilities(evolved, effects),
            atol=5e-11,
            rtol=0,
        )
