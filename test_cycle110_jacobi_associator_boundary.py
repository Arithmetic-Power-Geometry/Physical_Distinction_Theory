import itertools
import numpy as np
import cycle110_jacobi_associator_boundary as c

def test_general_akivis_sign_identity_exact():
    a=c.exact_general_identity_audit(); assert a['failures']==0 and a['max_abs_residual']==0

def test_smallest_2d_counterexample_nonassociative():
    C=c.lie_admissible_witness(2); e=lambda i:c.basis(2,i)
    assert np.array_equal(c.assoc(C,e(0),e(0),e(1)), np.array([0,-1]))

def test_smallest_2d_counterexample_jacobi():
    C=c.lie_admissible_witness(2); e=lambda i:c.basis(2,i)
    for i,j,k in itertools.product(range(2),repeat=3): assert not np.any(c.jacobi_left(C,e(i),e(j),e(k)))

def test_dimension_extensions_2_to_12():
    for row in c.dimension_countermodel_audit():
        if 2 <= row['n'] <= 12:
            assert row['nonassociative_witness']; assert row['jacobi_bad_basis_triples']==0

def test_octonion_witness_scaling():
    o=c.octonion_audit()
    A=np.array(o['A_e1_e2_e4']); J=np.array(o['Jcomm_e1_e2_e4'])
    assert np.array_equal(A, np.array([0,0,0,0,0,0,0,2]))
    assert np.array_equal(J, -6*A)
    assert np.allclose(np.array(o['Jcross_e1_e2_e4']), -1.5*A)

def test_octonion_alternative_relation_all_basis_triples():
    o=c.octonion_audit(); assert o['Jcomm_plus_6A_failures']==0; assert o['nonzero_associators']==168
