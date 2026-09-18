"""Cycle 223 exact stress test: subsystem preservation need not survive extension.

No external dependencies. The binary obstruction is embedded into n=1..12.
"""
import json


def run(n: int):
    X = tuple(range(n))
    if n == 1:
        return {"n": n, "degenerate": True, "local_preserves": True, "extension_preserves": True}

    # f collapses label 1 to 0 and leaves all other labels fixed.
    def f(x):
        return 0 if x == 1 else x

    # Local free set chosen so f preserves it.
    F_X = {0}
    local_preserves = all(f(x) in F_X for x in F_X)

    # Correlated extended free set contains the diagonal binary witness plus
    # unused diagonal labels, so the obstruction embeds at every n>=2.
    F_XE = {(i, i) for i in X}
    image = {(f(x), e) for (x, e) in F_XE}
    extension_preserves = image <= F_XE
    witness = ((1, 1), (f(1), 1))

    assert local_preserves
    assert not extension_preserves
    assert witness[0] in F_XE and witness[1] not in F_XE
    return {
        "n": n,
        "degenerate": False,
        "local_preserves": local_preserves,
        "extension_preserves": extension_preserves,
        "smallest_witness_input": list(witness[0]),
        "smallest_witness_output": list(witness[1]),
    }


if __name__ == "__main__":
    rows = [run(n) for n in range(1, 13)]
    assert rows[0]["extension_preserves"]
    assert all(not r["extension_preserves"] for r in rows[1:])
    print(json.dumps(rows, indent=2))
