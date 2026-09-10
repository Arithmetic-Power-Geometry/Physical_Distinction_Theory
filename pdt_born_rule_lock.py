"""Cycle 043: status/audit helpers for the PDT Born-rule same-input lock.

The rigorous mathematical input is Gleason/Gleason-type theory; this module does not
re-prove those theorems numerically. It makes the PDT hypothesis boundary explicit
and machine-auditable across dimensions.
"""
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True)
class LockStatus:
    dimension: int
    projective_gleason_lock: bool
    povm_gleason_type_lock: bool
    same_state_effect_noncontextual_lock: bool


def status_for_dimension(d: int) -> LockStatus:
    if d < 1:
        raise ValueError("Hilbert dimension must be positive")
    projective = d >= 3
    povm = d >= 2
    # Same-input lock is asserted only where a cited Gleason/Gleason-type route applies.
    same_input = d >= 2
    return LockStatus(d, projective, povm, same_input)


def escape_coordinates(
    same_state: bool = True,
    same_effects: bool = True,
    normalized_additive: bool = True,
    noncontextual: bool = True,
    resource_physically_changes_experiment: bool = False,
):
    """Return which hypotheses must be abandoned for a same-input deviation.

    Empty output means the standard Born-rule lock hypotheses are all retained.
    """
    escapes = []
    if not same_state:
        escapes.append("changed_state_or_dynamics")
    if not same_effects:
        escapes.append("changed_effect_structure")
    if not normalized_additive:
        escapes.append("nonstandard_probability_rule")
    if not noncontextual:
        escapes.append("contextual_probability")
    if resource_physically_changes_experiment:
        escapes.append("resource_physical_interaction")
    return tuple(escapes)


def dimension_audit(lo: int = 1, hi: int = 12):
    if lo < 1 or hi < lo:
        raise ValueError("invalid dimension range")
    return [asdict(status_for_dimension(d)) for d in range(lo, hi + 1)]


if __name__ == "__main__":
    print(json.dumps(dimension_audit(), indent=2))
