"""Cycle 054: exact qubit steering witness against ensemble-contextual nonlinear response.

The witness compares two remote ensemble decompositions of rho=I/2:
  Z ensemble: {|0>,|1>} with equal weights
  X ensemble: {|+>,|->} with equal weights
For E=|0><0| and nonlinear pure-state response g(x)=x^2, the ensemble-averaged
probabilities are 1/2 and 1/4 although the density operator is identical.
If the remote decomposition is selectable by a spacelike-separated party, this
produces a signalling channel. The arithmetic is exact using Fraction.
"""
from fractions import Fraction


def avg_response(overlaps, response):
    n = len(overlaps)
    return sum(response(x) for x in overlaps) / n


def square_response(x):
    return x * x


def born_response(x):
    return x


def witness():
    z_overlaps = [Fraction(1, 1), Fraction(0, 1)]
    x_overlaps = [Fraction(1, 2), Fraction(1, 2)]
    return {
        "born_z": avg_response(z_overlaps, born_response),
        "born_x": avg_response(x_overlaps, born_response),
        "nonlinear_z": avg_response(z_overlaps, square_response),
        "nonlinear_x": avg_response(x_overlaps, square_response),
    }


def test_exact_witness():
    out = witness()
    assert out["born_z"] == Fraction(1, 2)
    assert out["born_x"] == Fraction(1, 2)
    assert out["nonlinear_z"] == Fraction(1, 2)
    assert out["nonlinear_x"] == Fraction(1, 4)
    assert out["nonlinear_z"] != out["nonlinear_x"]


def test_affine_response_is_decomposition_invariant():
    z = [Fraction(1, 1), Fraction(0, 1)]
    x = [Fraction(1, 2), Fraction(1, 2)]
    for a in [Fraction(-2, 1), Fraction(0, 1), Fraction(3, 5), Fraction(4, 1)]:
        for b in [Fraction(-1, 2), Fraction(0, 1), Fraction(7, 3)]:
            f = lambda t, a=a, b=b: a * t + b
            assert avg_response(z, f) == avg_response(x, f)


if __name__ == "__main__":
    test_exact_witness()
    test_affine_response_is_decomposition_invariant()
    print(witness())
