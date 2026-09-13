from experiments.cycle_120_sector_resource_equivalence import (
    compose_leaking,
    compose_preserving,
    hidden_resource,
    run,
    visible_pair_equivalence,
)


def test_smallest_leak_witness():
    closure, monotone, h = visible_pair_equivalence(compose_leaking, [1], [1])
    assert closure is False
    assert monotone is False
    assert h == 1


def test_preserving_visible_pair():
    closure, monotone, h = visible_pair_equivalence(compose_preserving, [2], [3])
    assert closure is True
    assert monotone is True
    assert h == 0


def test_equivalence_stress_audit():
    out = run()
    assert out["equivalence_mismatches"] == 0
    assert out["pair_checks"] == 5216
    assert out["leaking_nonzero_hidden_outputs"] == 1094
    assert out["preserving_nonzero_hidden_outputs"] == 0


def test_hidden_resource_is_faithful_coordinate_model():
    assert hidden_resource([0, 0, 0]) == 0
    assert hidden_resource([0, 1, 0]) > 0


def test_nonseparating_observation_family_has_kernel():
    # Observing only first n-1 coordinates leaves e_n invisible.
    n = 5
    e_n = [0] * n
    e_n[-1] = 1
    observed = e_n[:-1]
    assert observed == [0] * (n - 1)
    assert hidden_resource(e_n) == 1


def test_full_coordinate_family_separates():
    vectors = ([0, 0, 0], [1, 0, 0], [0, -2, 0], [1, 2, 3])
    for m in vectors:
        assert (hidden_resource(m) == 0) == all(x == 0 for x in m)
