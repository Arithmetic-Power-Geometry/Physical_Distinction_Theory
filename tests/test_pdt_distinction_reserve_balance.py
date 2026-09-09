import numpy as np
from pdt_distinction_reserve_balance import (
    apply_unitary, balance_terms, depolarize, inaccessible_reserve
)


def random_density(rng, d):
    a = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    x = a @ a.conj().T
    return x / np.trace(x)


def random_unitary(rng, d):
    a = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    q, r = np.linalg.qr(a)
    p = np.diag(r); p = p / np.abs(p)
    return q @ np.diag(p.conj())


def test_reserve_nonnegative_dimensions_1_to_12():
    rng = np.random.default_rng(25025)
    for ds in range(1,13):
        d = 2*ds
        for _ in range(10):
            a,b = random_density(rng,d), random_density(rng,d)
            assert inaccessible_reserve(a,b,ds,2) >= -1e-12


def test_exact_unitary_balance_and_gain_bound():
    rng = np.random.default_rng(250250)
    for ds in range(1,13):
        d=2*ds
        for _ in range(10):
            a,b=random_density(rng,d),random_density(rng,d)
            u=random_unitary(rng,d)
            out=balance_terms(a,b,apply_unitary(a,u),apply_unitary(b,u),ds,2)
            assert abs(out["global_loss"]) < 1e-10
            assert abs(out["balance_residual"]) < 1e-10
            assert out["gain"] <= out["reserve_initial"] + 1e-10


def test_cptp_loss_corrected_balance():
    rng=np.random.default_rng(250251)
    for ds in (1,2,3,4,8,12,16,24):
        d=2*ds
        a,b=random_density(rng,d),random_density(rng,d)
        u=random_unitary(rng,d)
        x,y=apply_unitary(a,u),apply_unitary(b,u)
        x,y=depolarize(x,0.37),depolarize(y,0.37)
        out=balance_terms(a,b,x,y,ds,2)
        assert out["global_loss"] >= -1e-10
        assert abs(out["balance_residual"]) < 1e-10
        assert out["gain"] <= out["reserve_initial"] + 1e-10
