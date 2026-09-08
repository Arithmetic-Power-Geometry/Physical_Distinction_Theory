"""Orbit-completeness kill test for PDT dimension-selection proposals.

The key logical point is elementary but important.  Fix a reference x and let H=G_x
be its reversible stabilizer.  If the only declared scalar distinction about y is a
level value s_x(y), then saying that this scalar is a *complete invariant* of H-orbits
means exactly that each level set of s_x is one H-orbit.  For Euclidean angle or
distance this is precisely Two-Point Isotropy (TPI), not an independent derivation
of TPI.

This module also supplies explicit SU(m) witnesses: equal real Euclidean angle and
distance from x, but different complex inner products.  The latter is preserved by
the stabilizer of x, so the two points cannot lie in the same stabilizer orbit.
"""

from __future__ import annotations

from math import isclose, sqrt
from typing import Hashable, Iterable, Sequence


def _canonical_partition(labels: Sequence[Hashable]) -> set[frozenset[int]]:
    blocks: dict[Hashable, set[int]] = {}
    for i, label in enumerate(labels):
        blocks.setdefault(label, set()).add(i)
    return {frozenset(block) for block in blocks.values()}


def scalar_orbit_complete(
    scalar_levels: Sequence[Hashable], orbit_labels: Sequence[Hashable]
) -> bool:
    """Return True iff scalar-level classes coincide exactly with stabilizer orbits."""
    if len(scalar_levels) != len(orbit_labels):
        raise ValueError("scalar_levels and orbit_labels must have equal length")
    return _canonical_partition(scalar_levels) == _canonical_partition(orbit_labels)


def tpi_partition_test(
    scalar_levels: Sequence[Hashable], orbit_labels: Sequence[Hashable]
) -> bool:
    """Finite partition form of TPI: every scalar level set is one stabilizer orbit.

    This is deliberately implemented independently from scalar_orbit_complete so
    tests can audit the logical equivalence over adversarial/random partitions.
    """
    if len(scalar_levels) != len(orbit_labels):
        raise ValueError("scalar_levels and orbit_labels must have equal length")
    n = len(scalar_levels)
    for i in range(n):
        for j in range(n):
            same_level = scalar_levels[i] == scalar_levels[j]
            same_orbit = orbit_labels[i] == orbit_labels[j]
            if same_level != same_orbit:
                return False
    return True


def complex_inner(u: Sequence[complex], v: Sequence[complex]) -> complex:
    return sum(a.conjugate() * b for a, b in zip(u, v))


def euclidean_distance_sq(u: Sequence[complex], v: Sequence[complex]) -> float:
    return float(sum(abs(a - b) ** 2 for a, b in zip(u, v)))


def su_scalar_isotropy_witness(m: int, a: float = 0.5) -> dict[str, object]:
    """Construct an SU(m) witness against scalar-angle orbit completeness.

    x=e1, y=e2, z=i*a*e1+sqrt(1-a^2)*e2.  All are unit vectors and y,z have
    identical real Euclidean inner product (and distance) from x.  But their full
    complex inner products with x are 0 and i*a.  Any unitary fixing x preserves
    <x,.>, so y and z cannot be in the same stabilizer orbit.
    """
    if m < 2:
        raise ValueError("m must be at least 2")
    if not (0.0 < a < 1.0):
        raise ValueError("a must lie strictly between 0 and 1")

    x = [0j] * m
    y = [0j] * m
    z = [0j] * m
    x[0] = 1.0 + 0j
    y[1] = 1.0 + 0j
    z[0] = 1j * a
    z[1] = sqrt(1.0 - a * a) + 0j

    xy = complex_inner(x, y)
    xz = complex_inner(x, z)
    dxy2 = euclidean_distance_sq(x, y)
    dxz2 = euclidean_distance_sq(x, z)

    return {
        "m": m,
        "real_dimension": 2 * m,
        "real_inner_xy": xy.real,
        "real_inner_xz": xz.real,
        "distance_sq_xy": dxy2,
        "distance_sq_xz": dxz2,
        "complex_inner_xy": xy,
        "complex_inner_xz": xz,
        "same_scalar_level": isclose(xy.real, xz.real, abs_tol=1e-12)
        and isclose(dxy2, dxz2, abs_tol=1e-12),
        "same_stabilizer_orbit_possible": isclose(abs(xy - xz), 0.0, abs_tol=1e-12),
    }


def dimension_audit(max_real_dimension: int = 12) -> list[dict[str, object]]:
    """Return explicit SU(m) scalar-completeness failures up to a real dimension."""
    rows: list[dict[str, object]] = []
    for m in range(2, max_real_dimension // 2 + 1):
        w = su_scalar_isotropy_witness(m)
        rows.append(
            {
                "family": f"SU({m}) on C^{m}",
                "real_dimension": 2 * m,
                "same_euclidean_scalar": w["same_scalar_level"],
                "latent_complex_invariant_differs": not w["same_stabilizer_orbit_possible"],
                "scalar_orbit_complete": False,
                "status": "COUNTEREXAMPLE",
            }
        )
    return rows


if __name__ == "__main__":
    for row in dimension_audit(12):
        print(row)
