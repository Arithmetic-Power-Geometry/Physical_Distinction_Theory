from fractions import Fraction as F
from cycle050_stochastic_revelation_accounting import (
    exact_loss, stochastic_loss_rhs, equality_condition, is_column_stochastic
)


def test_exact_identity_strict_loss():
    p=[F(1),F(0)]; q=[F(0),F(1)]
    K=[[F(1),F(1)]]
    assert is_column_stochastic(K)
    assert exact_loss(K,p,q) == F(1)
    assert stochastic_loss_rhs(K,[F(1),F(-1)]) == F(1)
    assert not equality_condition(K,p,q)


def test_equality_when_outputs_do_not_mix_signs():
    p=[F(3,4),F(1,4),F(0)]; q=[F(1,4),F(1,4),F(1,2)]
    K=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(1)]]
    assert exact_loss(K,p,q) == 0
    assert equality_condition(K,p,q)


def test_fractional_kernel_identity():
    p=[F(1,2),F(1,3),F(1,6)]; q=[F(1,6),F(1,3),F(1,2)]
    K=[[F(1,2),F(1,4),F(1,2)],[F(1,2),F(3,4),F(1,2)]]
    d=[a-b for a,b in zip(p,q)]
    assert is_column_stochastic(K)
    assert exact_loss(K,p,q) == stochastic_loss_rhs(K,d)
