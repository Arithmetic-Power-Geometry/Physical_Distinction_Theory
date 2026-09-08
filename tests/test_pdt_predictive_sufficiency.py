import numpy as np

from pdt_predictive_sufficiency import (
    audit_predictive_sufficiency,
    exact_factorization_criterion,
    total_variation,
)


def test_total_variation_extremes():
    assert np.isclose(total_variation([1, 0], [0, 1]), 1.0)
    assert np.isclose(total_variation([0.4, 0.6], [0.4, 0.6]), 0.0)


def test_exact_sufficiency_when_predictions_constant_on_fibres():
    labels = ["same", "same", "other"]
    predictions = [[0.7, 0.3], [0.7, 0.3], [0.2, 0.8]]
    audits, sufficient, lower = audit_predictive_sufficiency(labels, predictions)
    assert sufficient
    assert np.isclose(lower, 0.0)
    assert all(np.isclose(row.tv_diameter, 0.0) for row in audits)
    assert exact_factorization_criterion(labels, predictions)


def test_insufficient_statistic_has_nonzero_unavoidable_error():
    labels = ["same-output", "same-output"]
    predictions = [[1.0, 0.0], [0.0, 1.0]]
    audits, sufficient, lower = audit_predictive_sufficiency(labels, predictions)
    assert not sufficient
    assert len(audits) == 1
    assert np.isclose(audits[0].tv_diameter, 1.0)
    assert np.isclose(lower, 0.5)
    assert not exact_factorization_criterion(labels, predictions)
