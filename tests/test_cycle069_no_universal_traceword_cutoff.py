import numpy as np

from cycle069_no_universal_traceword_cutoff import embedded_witness, moment_errors, operational_separator, witness


def test_cutoff_witnesses_dimensions_2_through_12():
    for d in range(2, 13):
        lam, mu, _ = witness(d)
        assert np.all(lam > 0)
        assert np.all(mu > 0)
        assert abs(lam.sum() - 1.0) < 1e-10
        assert abs(mu.sum() - 1.0) < 1e-8
        assert max(moment_errors(lam, mu, d - 1)) < 1e-8
        assert operational_separator(lam, mu)["gap"] > 1e-8
        assert abs(float(np.prod(lam) - np.prod(mu))) > 1e-22


def test_fixed_cutoff_six_survives_high_dimension_embedding():
    for n in (16, 24, 32, 48, 64, 96, 128):
        lam, mu = embedded_witness(n, cutoff=6)
        assert len(lam) == n
        assert len(mu) == n
        assert abs(lam.sum() - 1.0) < 1e-10
        assert abs(mu.sum() - 1.0) < 1e-8
        assert max(moment_errors(lam, mu, 6)) < 1e-8
        assert operational_separator(lam, mu)["gap"] > 1e-6
