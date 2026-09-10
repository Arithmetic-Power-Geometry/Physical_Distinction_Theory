"""Deterministic exact-rational audit for cycle055.

Writes CSV-compatible rows to stdout. Seed and trial counts match the committed audit.
"""
from fractions import Fraction as F
import random
from cycle055_distinction_profile_composition import verify_product_law


def rand_prob(n, rng):
    xs=[rng.randint(1,20) for _ in range(n)]
    z=sum(xs)
    return [F(x,z) for x in xs]


def run():
    rng=random.Random(20260910)
    print("dimension,trials,profile_failures,tv_failures,arithmetic")
    for n,trials in [(i,200) for i in range(1,13)]+[(16,50),(24,50),(32,50),(48,50),(64,50)]:
        pf=tf=0
        for _ in range(trials):
            p,q,r,s=(rand_prob(n,rng) for _ in range(4))
            a,b=verify_product_law(p,q,r,s)
            pf += int(not a)
            tf += int(not b)
        print(f"{n},{trials},{pf},{tf},exact_rational")

if __name__ == "__main__":
    run()
