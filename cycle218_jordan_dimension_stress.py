"""Cycle 218 exact stress test for Jordan-family dimension non-uniqueness.

No external dependencies. Checks n=1..12 and a higher-dimensional range.
"""


def d_real(n: int) -> int:
    return n * (n + 1) // 2


def d_complex(n: int) -> int:
    return n * n


def d_quaternionic(n: int) -> int:
    return n * (2 * n - 1)


def check_range(lo: int, hi: int) -> None:
    for n in range(lo, hi + 1):
        dims = (d_real(n), d_complex(n), d_quaternionic(n))
        if n == 1:
            assert dims == (1, 1, 1)
        else:
            assert len(set(dims)) == 3, (n, dims)
            assert dims[0] < dims[1] < dims[2], (n, dims)


def test_exact_n1_to_n12() -> None:
    check_range(1, 12)


def test_higher_dimensions() -> None:
    check_range(13, 10000)


def test_n3_witness() -> None:
    assert (d_real(3), d_complex(3), d_quaternionic(3)) == (6, 9, 15)


if __name__ == "__main__":
    test_exact_n1_to_n12()
    test_higher_dimensions()
    test_n3_witness()
    print("Cycle 218 PASS: Jordan rank does not uniquely fix matrix-state dimension for n>=2.")
    for n in range(1, 13):
        print(n, d_real(n), d_complex(n), d_quaternionic(n))
