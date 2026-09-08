from pdt_transitive_isotropy_no_go import (
    pcc_transitive_higher_dimensional_counterexamples,
    su_counterexample,
)


def test_su2_is_four_dimensional_transitive_pcc_counterexample():
    x = su_counterexample(2)
    assert x.real_dimension == 4
    assert x.sphere_dimension == 3
    assert x.base_size == 1
    assert x.connected and x.noncommuting and x.sphere_transitive and x.pcc


def test_su3_is_six_dimensional_transitive_pcc_counterexample():
    x = su_counterexample(3)
    assert x.real_dimension == 6
    assert x.sphere_dimension == 5
    assert x.base_size == 2
    assert x.connected and x.noncommuting and x.sphere_transitive and x.pcc


def test_pairwise_cutoff_for_natural_su_family():
    assert not su_counterexample(4).pcc
    witnesses = pcc_transitive_higher_dimensional_counterexamples(max_m=12)
    assert [x.m for x in witnesses] == [2, 3]
    assert [x.real_dimension for x in witnesses] == [4, 6]
