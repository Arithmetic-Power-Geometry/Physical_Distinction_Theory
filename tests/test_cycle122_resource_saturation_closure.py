from cycle122_resource_saturation_closure import (
    DIMS,
    hidden_resource,
    leaking_split,
    run_audit,
    saturation_forces_closure,
)


def test_exact_saturation_forces_zero_hidden_resource():
    for B in [0, 1, 2, 7, 100, 10_000]:
        assert saturation_forces_closure(B, B)
        assert hidden_resource(B, B) == 0


def test_total_conservation_alone_allows_hidden_allocation():
    qvis, hidden = leaking_split(6, 1)
    assert qvis + hidden == 6
    assert hidden > 0
    assert not saturation_forces_closure(6, qvis)


def test_smallest_decisive_budget_witness():
    qvis, hidden = leaking_split(1, 1)
    assert (qvis, hidden) == (0, 1)


def test_dimension_stress_audit():
    audit = run_audit(seed=122, trials_per_dimension=10)
    assert audit.dimensions[:12] == list(range(1, 13))
    assert audit.dimensions[-1] == 128
    assert audit.saturation_failures == 0
    assert audit.leaking_total_conservation_witnesses > 0


def test_nonnegative_domain_guard():
    try:
        saturation_forces_closure(-1, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("negative resources must be rejected")
