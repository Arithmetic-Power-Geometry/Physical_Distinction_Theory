import pytest

from pdt_born_rule_lock import dimension_audit, escape_coordinates, status_for_dimension


def test_dimension_thresholds():
    assert not status_for_dimension(1).projective_gleason_lock
    assert not status_for_dimension(1).povm_gleason_type_lock
    assert not status_for_dimension(2).projective_gleason_lock
    assert status_for_dimension(2).povm_gleason_type_lock
    assert status_for_dimension(2).same_state_effect_noncontextual_lock
    for d in range(3, 101):
        s = status_for_dimension(d)
        assert s.projective_gleason_lock
        assert s.povm_gleason_type_lock
        assert s.same_state_effect_noncontextual_lock


def test_audit_1_through_12():
    rows = dimension_audit(1, 12)
    assert len(rows) == 12
    assert [r["dimension"] for r in rows] == list(range(1, 13))
    assert sum(r["projective_gleason_lock"] for r in rows) == 10
    assert sum(r["povm_gleason_type_lock"] for r in rows) == 11


def test_escape_boundary():
    assert escape_coordinates() == ()
    assert escape_coordinates(noncontextual=False) == ("contextual_probability",)
    assert escape_coordinates(same_effects=False) == ("changed_effect_structure",)
    assert set(escape_coordinates(same_state=False, normalized_additive=False)) == {
        "changed_state_or_dynamics",
        "nonstandard_probability_rule",
    }
    assert escape_coordinates(resource_physically_changes_experiment=True) == (
        "resource_physical_interaction",
    )


def test_invalid_dimensions():
    with pytest.raises(ValueError):
        status_for_dimension(0)
    with pytest.raises(ValueError):
        dimension_audit(4, 3)
