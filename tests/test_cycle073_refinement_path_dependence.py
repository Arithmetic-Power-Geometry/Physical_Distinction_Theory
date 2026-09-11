from fractions import Fraction
from cycle073_refinement_path_dependence import witness, dimension_stress

def test_exact_path_dependence():
    w=witness()
    assert w['increments_a']==[Fraction(1),Fraction(0)]
    assert w['increments_b']==[Fraction(0),Fraction(1)]
    assert sum(w['increments_a'])==sum(w['increments_b'])==Fraction(1)

def test_dimensions_1_to_12():
    rows=dimension_stress(12)
    assert rows[0][1]=='DEGENERATE'
    assert all(status=='WITNESS' and dz==1 and dx==0 for _,status,dz,dx in rows[1:])
