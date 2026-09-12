import math, pathlib, sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import cycle105_infimal_quotient_no_go as c

def test_l1_parallelogram_decisive_failure():
    w=c.parallelogram_residual_l1(); assert w['lhs']==8.0 and w['rhs']==4.0 and w['residual']==4.0

def test_all_exact_coordinate_chains():
    rows=c.coordinate_chain_exact_ledger(); assert rows and all(r['path_independent_exact'] for r in rows); assert any(not r['quadratic'] for r in rows)

def test_finite_infimal_pushforward_with_unreachable():
    cost={0:7,1:2,2:9}; q1={0:'a',1:'b',2:'a'}; ys=['a','b','ghost']; cy=c.finite_infimal_pushforward(cost,q1,ys); q2={'a':'u','b':'u','ghost':'v'}
    via=c.finite_infimal_pushforward(cy,q2,['u','v']); direct=c.finite_infimal_pushforward(cost,{x:q2[q1[x]] for x in cost},['u','v'])
    assert via==direct and math.isinf(via['v'])

def test_random_finite_fiber_audit():
    assert c.randomized_finite_fiber_audit(trials=1000,seed=105)['violations']==0

def test_random_coordinate_numeric_audit():
    a=c.random_coordinate_numeric_audit(trials=1000,seed=105); assert a['violations_gt_1e-12']==0 and a['nonquadratic_cases']>0

def test_p2_and_nonp2_parallelogram_witnesses():
    rows=c.p_norm_parallelogram_table(); p2=next(r for r in rows if r['p']==2.0); p1=next(r for r in rows if r['p']==1.0); pinf=next(r for r in rows if r['p']=='inf')
    assert abs(p2['residual'])<1e-12 and abs(p1['residual'])>1e-12 and abs(pinf['residual'])>1e-12
