from fractions import Fraction

from cycle049_exact_revelation_accounting import (
    tv,
    coarse_pushforward,
    cancellation_loss,
    is_sign_pure,
    exact_identity,
    exact_random_audit,
)


def test_smallest_full_revelation_witness():
    p = [Fraction(1), Fraction(0)]
    q = [Fraction(0), Fraction(1)]
    part = [0, 0]
    fine, coarse, loss, ok = exact_identity(p, q, part)
    assert fine == 1
    assert coarse == 0
    assert loss == 1
    assert ok
    assert not is_sign_pure(p, q, part)


def test_zero_loss_iff_sign_pure_examples():
    p = [Fraction(3, 5), Fraction(1, 5), Fraction(1, 5)]
    q = [Fraction(1, 5), Fraction(1, 5), Fraction(3, 5)]
    pure_part = [0, 1, 2]
    mixed_part = [0, 1, 0]
    assert is_sign_pure(p, q, pure_part)
    assert cancellation_loss(p, q, pure_part) == 0
    assert tv(p, q) == tv(coarse_pushforward(p, pure_part), coarse_pushforward(q, pure_part))
    assert not is_sign_pure(p, q, mixed_part)
    assert cancellation_loss(p, q, mixed_part) > 0


def test_exact_random_audit_dimensions_1_to_12():
    for n in range(1, 13):
        err, _, _, failures = exact_random_audit(n, trials=200)
        assert err == 0
        assert failures == 0
