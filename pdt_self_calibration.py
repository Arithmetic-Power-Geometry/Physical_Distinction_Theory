"""Operational self-calibration (OSC) audit for PDT dimension selection.

This module contains only the finite-dimensional counting consequences of the
OSC hypothesis documented in docs/cycle009_operational_self_calibration.md.
It does not assert that OSC is a fundamental physical law.
"""


def so_dimension(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return n * (n - 1) // 2


def state_entropy_slope(n: int) -> int:
    """Metric-entropy exponent of an n-dimensional Euclidean state body."""
    if n < 1:
        raise ValueError("n must be positive")
    return n


def control_entropy_slope(n: int) -> int:
    """Metric-entropy exponent of SO(n), equal to its manifold dimension."""
    return so_dimension(n)


def osc_passes(n: int) -> bool:
    """OSC: control calibration complexity grows no faster than state complexity."""
    return control_entropy_slope(n) <= state_entropy_slope(n)


def noncommuting_reversibility_passes(n: int) -> bool:
    """SO(n) has genuinely non-abelian connected reversible dynamics iff n >= 3."""
    if n < 1:
        raise ValueError("n must be positive")
    return n >= 3


def osc_ncr_selects(n: int) -> bool:
    return osc_passes(n) and noncommuting_reversibility_passes(n)


def audit_dimensions(start: int = 1, stop: int = 12):
    if start < 1 or stop < start:
        raise ValueError("require 1 <= start <= stop")
    rows = []
    for n in range(start, stop + 1):
        state = state_entropy_slope(n)
        control = control_entropy_slope(n)
        rows.append(
            {
                "n": n,
                "state_entropy_slope": state,
                "control_entropy_slope": control,
                "slope_margin": state - control,
                "osc": osc_passes(n),
                "ncr": noncommuting_reversibility_passes(n),
                "selected": osc_ncr_selects(n),
            }
        )
    return rows
