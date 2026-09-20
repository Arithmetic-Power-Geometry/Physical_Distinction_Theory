from fractions import Fraction
import unittest


def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def cyclic(v):
    if len(v) <= 1:
        return list(v)
    return [v[-1], *v[:-1]]


def uniformize(v):
    # Exact action of the n x n matrix with every entry 1/n.
    n = len(v)
    total = sum(v)
    return [total / n for _ in range(n)]


class Cycle269DistinctionConservation(unittest.TestCase):
    def test_exact_dimensions_1_through_12(self):
        for n in range(1, 13):
            with self.subTest(n=n):
                if n == 1:
                    p = q = [Fraction(1, 1)]
                    self.assertEqual(tv(p, q), 0)
                    continue

                # Exact rational states with nonzero distinction in every n>=2.
                # p is uniform; q transfers 1/(2n) from coordinate 1 to 0.
                p = [Fraction(1, n) for _ in range(n)]
                delta = Fraction(1, 2 * n)
                q = p.copy()
                q[0] += delta
                q[1] -= delta

                d = tv(p, q)
                self.assertGreater(d, 0)

                # Reversible cyclic relabelling conserves distinction exactly.
                self.assertEqual(tv(cyclic(p), cyclic(q)), d)

                # Uniformizing stochastic coarse-graining erases this distinction.
                pu = uniformize(p)
                qu = uniformize(q)
                self.assertLessEqual(tv(pu, qu), d)
                self.assertEqual(tv(pu, qu), 0)

    def test_n2_is_nontrivial_counterdimension(self):
        p = [Fraction(1, 2), Fraction(1, 2)]
        q = [Fraction(3, 4), Fraction(1, 4)]
        self.assertGreater(tv(p, q), 0)
        self.assertEqual(tv(cyclic(p), cyclic(q)), tv(p, q))

    def test_n4_defeats_upper_bound_three(self):
        n = 4
        p = [Fraction(1, n) for _ in range(n)]
        q = [Fraction(3, 8), Fraction(1, 8), Fraction(1, 4), Fraction(1, 4)]
        self.assertEqual(sum(q), 1)
        self.assertGreater(tv(p, q), 0)
        self.assertEqual(tv(cyclic(p), cyclic(q)), tv(p, q))


if __name__ == "__main__":
    unittest.main()
