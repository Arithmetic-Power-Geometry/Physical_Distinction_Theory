"""Auditable counterexamples to transitivity-based PDT dimension selection.

This module records exact group-action facts used in the no-go note. It does not
numerically approximate Lie groups; it checks the dimension/base-size logic for
the natural SU(m) actions that already provide decisive higher-dimensional
counterexamples.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SUCounterexample:
    m: int
    real_dimension: int
    sphere_dimension: int
    base_size: int
    connected: bool
    noncommuting: bool
    sphere_transitive: bool
    pcc: bool


def su_counterexample(m: int) -> SUCounterexample:
    if m < 2:
        raise ValueError("m must be >= 2")
    base_size = m - 1
    return SUCounterexample(
        m=m,
        real_dimension=2 * m,
        sphere_dimension=2 * m - 1,
        base_size=base_size,
        connected=True,
        noncommuting=m >= 2,
        sphere_transitive=True,  # SU(m)/SU(m-1) ~= S^(2m-1)
        pcc=base_size <= 2,
    )


def pcc_transitive_higher_dimensional_counterexamples(max_m: int = 12):
    """Return SU(m) witnesses with n>3 satisfying transitivity+PCC+NCR."""
    return [
        x
        for m in range(2, max_m + 1)
        if (x := su_counterexample(m)).real_dimension > 3
        and x.connected
        and x.noncommuting
        and x.sphere_transitive
        and x.pcc
    ]


if __name__ == "__main__":
    for witness in pcc_transitive_higher_dimensional_counterexamples():
        print(witness)
