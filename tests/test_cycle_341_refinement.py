def revelation(d1, candidate_values):
    d2 = max([d1] + list(candidate_values))
    return d2, d2-d1


def test_saturation_counterexample_n2_to_n12():
    for n in range(2, 13):
        d2, inc = revelation(1.0, [0.0, 0.25, 0.5])
        assert d2 == 1.0
        assert inc == 0.0


def test_strictness_criterion_positive_case():
    d2, inc = revelation(0.4, [0.3, 0.7])
    assert d2 == 0.7
    assert inc > 0


def test_strictness_criterion_null_case():
    d2, inc = revelation(0.7, [0.2, 0.7])
    assert d2 == 0.7
    assert inc == 0
