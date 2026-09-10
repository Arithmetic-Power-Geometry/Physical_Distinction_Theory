"""Deterministic exact-rational audit for cycle 050; stdlib only."""
from fractions import Fraction as F
import random
from cycle050_stochastic_revelation_accounting import exact_loss, stochastic_loss_rhs, equality_condition


def rand_prob(rng,n,limit=31):
    xs=[rng.randint(1,limit) for _ in range(n)]; s=sum(xs)
    return [F(x,s) for x in xs]


def rand_kernel(rng,m,n,limit=17):
    cols=[]
    for _ in range(n):
        xs=[rng.randint(0,limit) for _ in range(m)]
        if sum(xs)==0: xs[0]=1
        s=sum(xs); cols.append([F(x,s) for x in xs])
    return [[cols[i][j] for i in range(n)] for j in range(m)]


def run(trials=200):
    out=[]
    for n in range(1,13):
        rng=random.Random(5000+n); ident=eqfail=0; maxloss=F(0)
        for _ in range(trials):
            p=rand_prob(rng,n); q=rand_prob(rng,n); m=rng.randint(1,max(1,n))
            K=rand_kernel(rng,m,n); d=[a-b for a,b in zip(p,q)]
            loss=exact_loss(K,p,q)
            ident += loss != stochastic_loss_rhs(K,d)
            eqfail += ((loss == 0) != equality_condition(K,p,q))
            maxloss=max(maxloss,loss)
        out.append((n,trials,ident,eqfail,str(maxloss)))
    return out

if __name__ == '__main__':
    print('n,trials,identity_failures,equality_condition_failures,max_observed_loss')
    for row in run(): print(','.join(map(str,row)))
