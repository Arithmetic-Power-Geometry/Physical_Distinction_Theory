"""Cycle 254: exact no-hiding dimension stress.

Witness: the SWAP unitary maps |psi>_S|0>_E -> |0>_S|psi>_E.
For computational basis inputs this script checks the induced permutation exactly
for n=1..12 and verifies that S is input-independent while E retains the label.
This is a regression witness, not a proof of the general no-hiding theorem.
"""

import json


def swap_index(n: int, s: int, e: int) -> tuple[int, int]:
    assert 0 <= s < n and 0 <= e < n
    return e, s


def check_dimension(n: int) -> dict:
    system_outputs = []
    env_outputs = []
    for i in range(n):
        s_out, e_out = swap_index(n, i, 0)
        system_outputs.append(s_out)
        env_outputs.append(e_out)
    return {
        "n": n,
        "system_constant_zero": all(x == 0 for x in system_outputs),
        "environment_recovers_basis_label": env_outputs == list(range(n)),
        "swap_involution": all(swap_index(n, *swap_index(n, s, e)) == (s, e)
                               for s in range(n) for e in range(n)),
    }


def main() -> None:
    rows = [check_dimension(n) for n in range(1, 13)]
    assert all(r["system_constant_zero"] for r in rows)
    assert all(r["environment_recovers_basis_label"] for r in rows)
    assert all(r["swap_involution"] for r in rows)
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
