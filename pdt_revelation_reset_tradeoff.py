"""Cycle 020: thermodynamic distinction revelation/reset tradeoff.

This module combines two imported/known facts under explicit assumptions:
(1) accessible classical information from a d-dimensional quantum record is at most log2(d) bits (Holevo dimension ceiling), and
(2) resetting an energetically degenerate classical memory Y isothermally with no useful side information dissipates at least k_B T ln(2) H(Y).

Since I(X:Y) <= H(Y), any record carrying r bits of operational branch revelation requires reset heat Q_reset >= k_B T ln(2) r. This is a conditional PDT resource corollary, not a novelty claim.
"""

import math

K_B = 1.380649e-23  # J/K, exact SI value


def dimension_information_ceiling_bits(d: int) -> float:
    if d < 1:
        raise ValueError("d must be >= 1")
    return math.log2(d)


def landauer_heat_for_bits(bits: float, temperature_k: float) -> float:
    if bits < 0:
        raise ValueError("bits must be nonnegative")
    if temperature_k < 0:
        raise ValueError("temperature must be nonnegative")
    return K_B * temperature_k * math.log(2.0) * bits


def revelation_reset_ceiling_bits(d: int, q_reset_j: float, temperature_k: float) -> float:
    """Maximum revelation allowed jointly by dimension and reset-heat resource.

    Assumes T>0 and standard no-side-information Landauer reset conditions.
    """
    if q_reset_j < 0:
        raise ValueError("q_reset_j must be nonnegative")
    if temperature_k <= 0:
        raise ValueError("temperature_k must be > 0")
    thermo = q_reset_j / (K_B * temperature_k * math.log(2.0))
    return min(dimension_information_ceiling_bits(d), thermo)


def perfect_uniform_revelation_heat_floor_j(k: int, temperature_k: float) -> float:
    if k < 1:
        raise ValueError("k must be >= 1")
    return landauer_heat_for_bits(math.log2(k), temperature_k)


def perfect_uniform_revelation_dimension_possible(k: int, d: int) -> bool:
    if k < 1 or d < 1:
        raise ValueError("k and d must be >= 1")
    return d >= k
