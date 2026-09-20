from fractions import Fraction
import unittest


def kl(p, q):
    # Exact only for equality comparison under a common permutation: represent
    # the summands symbolically as ordered (p_i,q_i) pairs rather than logs.
    # Equality of KL under permutation follows because the multiset of terms
    # p_i log(p_i/q_i) is unchanged.
    return sorted(zip(p, q))


def permute(v):
    if len(v) <= 1:
        return list(v)
    return [v[-1], *v[:-1]]


def inverse_permute(v):
    if len(v) <= 1:
        return list(v)
    return [*v[1:], v[0]]


class Cycle270RecoverabilityDimensionBlind(unittest.TestCase):
    def witness(self, n):
        if n == 1:
            return [Fraction(1)], [Fraction(1)]
        p = [Fraction(1, n) for _ in range(n)]
        q = p.copy()
        delta = Fraction(1, 3 * n)
        q[0] += delta
        q[1] -= delta
        return p, q

    def test_exact_dimensions_1_through_12(self):
        for n in range(1, 13):
            with self.subTest(n=n):
                p, q = self.witness(n)
                pp, qq = permute(p), permute(q)
                self.assertEqual(inverse_permute(pp), p)
                self.assertEqual(inverse_permute(qq), q)
                self.assertEqual(kl(p, q), kl(pp, qq))
                if n >= 2:
                    self.assertNotEqual(p, q)

    def test_n2_counterdimension(self):
        p, q = self.witness(2)
        self.assertNotEqual(p, q)
        self.assertEqual(kl(p, q), kl(permute(p), permute(q)))

    def test_n4_defeats_upper_bound_three(self):
        p, q = self.witness(4)
        self.assertNotEqual(p, q)
        self.assertEqual(kl(p, q), kl(permute(p), permute(q)))


if __name__ == "__main__":
    unittest.main()
