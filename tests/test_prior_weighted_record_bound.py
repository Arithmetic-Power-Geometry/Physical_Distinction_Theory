import math
import numpy as np

from pdt_prior_weighted_record_bound import (
    discrimination_success,
    minimum_copies_dimension_necessary,
    postmeasurement_min_entropy_floor,
    random_stress,
    saturation_ensemble,
    source_min_entropy,
    success_upper_bound,
    uniform_copy_bound,
)


def test_uniform_reduces_to_previous_bound():
    for d in range(1, 101):
        for k in (1, d, d + 1, 2 * d + 3):
            priors = np.full(k, 1.0 / k)
            assert np.isclose(success_upper_bound(priors, (d,)), min(1.0, d / k))


def test_nonuniform_sharpness_nontrivial_regime():
    for D in range(1, 13):
        k = D + 5
        for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
            pmax = (1-frac) * (1/k) + frac * (1/D)
            priors, states, povm = saturation_ensemble(D, k, pmax)
            got = discrimination_success(states, povm, priors)
            assert np.isclose(got, D * pmax, atol=1e-12)
            assert np.isclose(got, success_upper_bound(priors, (D,)), atol=1e-12)


def test_composite_dimension_multiplies():
    priors = np.array([0.1] * 10)
    assert np.isclose(success_upper_bound(priors, (2, 3)), 0.6)
    assert success_upper_bound(priors, (2, 2, 3)) == 1.0


def test_min_entropy_form():
    priors = np.array([0.4, 0.3, 0.2, 0.1])
    assert np.isclose(source_min_entropy(priors), -math.log2(0.4))
    assert np.isclose(
        postmeasurement_min_entropy_floor(priors, (1,)),
        -math.log2(0.4),
    )
    assert postmeasurement_min_entropy_floor(priors, (2,)) >= 0.0


def test_uniform_copy_capacity_necessary_thresholds():
    assert uniform_copy_bound(2, 1, 5) == 0.4
    assert uniform_copy_bound(2, 2, 5) == 0.8
    assert uniform_copy_bound(2, 3, 5) == 1.0
    assert minimum_copies_dimension_necessary(2, 5) == 3
    assert minimum_copies_dimension_necessary(3, 10) == 3
    assert minimum_copies_dimension_necessary(1, 2) == math.inf


def test_random_nonuniform_dimensions_1_to_12():
    for d in range(1, 13):
        out = random_stress(d, d + 5, trials=40, seed=26090922)
        assert out["maximum_violation"] <= 1e-12
