import unittest

from pdt_tensor_dimension_closure import (
    direct_sum_dimension,
    finite_tensor_selector_no_go,
    is_tensor_closed,
    tensor_dimension,
    tensor_power_ladder,
    universal_single_dimension_survives,
)


class TensorDimensionClosureTests(unittest.TestCase):
    def test_tensor_rule_dimensions_1_to_12(self):
        for a in range(1, 13):
            for b in range(1, 13):
                self.assertEqual(tensor_dimension(a, b), a * b)

    def test_only_singleton_fixed_point_is_one(self):
        survivors = [d for d in range(1, 257) if universal_single_dimension_survives(d)]
        self.assertEqual(survivors, [1])

    def test_three_generates_infinite_tensor_ladder(self):
        self.assertEqual(
            tensor_power_ladder(3, 12),
            [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441],
        )

    def test_previous_ndc_sets_are_not_tensor_closed(self):
        for admissible in ({3}, {3, 7}, {1, 3, 7}):
            self.assertTrue(finite_tensor_selector_no_go(set(admissible)))
            self.assertFalse(is_tensor_closed(set(admissible)))

    def test_finite_sets_with_nontrivial_dimension_fail_if_claimed_closed(self):
        examples = [{2}, {3}, {4, 16}, {2, 4, 8, 16}, {3, 9, 27, 81}]
        for admissible in examples:
            self.assertTrue(finite_tensor_selector_no_go(admissible))

    def test_degenerate_unit_exception(self):
        self.assertTrue(is_tensor_closed({1}))
        self.assertTrue(universal_single_dimension_survives(1))
        self.assertFalse(finite_tensor_selector_no_go({1}))

    def test_alternative_direct_sum_rule_is_also_extensive(self):
        for d in range(1, 13):
            self.assertEqual(direct_sum_dimension(d, d), 2 * d)
            self.assertGreater(direct_sum_dimension(d, d), d)


if __name__ == "__main__":
    unittest.main()
