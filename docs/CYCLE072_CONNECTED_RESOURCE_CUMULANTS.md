# Cycle 072 — Connected Resource-Cumulant Composition Hierarchy

## Target

PDT-II target (1): find a defensible composition law after Cycle 071 proved that two local resource quotients cannot determine an arbitrary correlated composite.

## Result

**Classification:** `PROVED + FALSIFIED (pairwise truncation) + IMPORTED/KNOWN + NUMERICALLY/EXACTLY SUPPORTED`.

**BREAKTHROUGH CANDIDATE:** No.

This cycle supplies an exact structural closure, but the underlying partition-lattice cumulant/Ursell construction and reduced-density-matrix cumulant hierarchy are established mathematics. The PDT contribution here is only the resource-indexed interpretation and the explicit identification of the Cycle-071 correlation remainder with the first connected sector.

## 1. Exact connected-sector decomposition

For every nonempty party set `S`, let `q_S` denote the resource-restricted joint functional on the accessible observables of those parties. Define connected sectors `kappa_S` recursively by

```text
q_S = sum_{pi in Pi(S)} tensor_{B in pi} kappa_B,
```

where `Pi(S)` is the set-partition lattice of `S`. Equivalently,

```text
kappa_S = q_S - sum_{pi in Pi(S), pi != {S}} tensor_{B in pi} kappa_B.
```

This is triangular in subset size, hence the connected sectors exist and are unique. It is the usual moment-cumulant/Mobius inversion on the partition lattice.

For two parties,

```text
q_AB = q_A tensor q_B + kappa_AB.
```

Therefore the undifferentiated Cycle-071 remainder `Gamma_R` is exactly the two-party connected resource sector `kappa_AB`.

For three parties,

```text
q_ABC = q_A tensor q_B tensor q_C
      + kappa_AB tensor q_C
      + kappa_AC tensor q_B
      + kappa_BC tensor q_A
      + kappa_ABC.
```

Thus correlated composition is not closed by one universal pairwise correction: a genuine three-party connected sector is generally required.

## 2. Independent-cut law

If the resource functional factorizes across a bipartition `L|R`,

```text
q_S = q_{S intersect L} tensor q_{S intersect R},
```

then every connected sector that intersects both sides vanishes:

```text
kappa_S = 0  whenever  S intersects L != empty  and  S intersects R != empty.
```

This follows by substitution into the partition identity, or equivalently from the standard connected-cumulant factorization theorem. It gives a precise composition rule: connected resource sectors encode only correlations that cannot be decomposed across an independent cut.

## 3. Decisive kill test for pairwise truncation

For local dimension `d >= 2`, embed the two-level family

```text
rho(c) = 1/2 (|000><000| + |111><111|)
       + c/2 (|000><111| + |111><000|),    |c| <= 1.
```

All one-party and two-party reduced states are independent of `c`. Hence every local and pairwise resource statistic obtainable from those reduced states is identical throughout the family.

Let `X_01 = |0><1| + |1><0|`. Then

```text
Tr[rho(c) X_01 tensor X_01 tensor X_01] = c.
```

Every one-body and two-body `X_01` moment is zero, so on this observable triple

```text
kappa_ABC = c.
```

The endpoints `c=+1` and `c=-1` therefore have identical one- and two-party marginals but a triple-statistic separation of exactly `2`. These endpoints are pure GHZ phase states; values `|c|<1` give mixed witnesses. The smallest local dimension is `d=2`. Dimension `d=1` is explicitly degenerate.

Therefore:

```text
local sectors + all pairwise sectors  !=  complete general composition law.
```

The surviving exact hierarchy must permit connected sectors of every order allowed by the declared multipartite resource window.

## 4. Audits

The executable audit uses exact rational arithmetic for the combinatorial law. Across party counts 2 through 6, 120 randomized independent-cut constructions per party count produced:

- `8,378` crossing connected sectors checked;
- `0` crossing-sector failures;
- `0` reconstruction failures.

The GHZ-coherence witness was evaluated analytically for local dimensions

```text
1,2,...,12,16,24,32,48,64,96,128
```

and for `c = -1,-3/4,-1/2,0,1/2,3/4,1`. Dimension 1 is degenerate; all tested dimensions `d>=2` retain exactly the same lower marginals while `kappa_ABC` follows `c`. The grid includes both pure and mixed states.

The theorem is algebraic. These audits are regression/counterexample stress tests rather than substitutes for proof. Norm choice, reversible-group choice, Markovianity and thermodynamic dynamics are not invoked by this kinematic partition identity, so no irrelevant dynamical test is claimed.

## 5. Prior-art boundary

This is **not** promoted as a breakthrough. Kutzelnigg and Mukherjee's reduced-density-matrix cumulant formalism explicitly treats two-particle cumulants as two-particle correlation and the three-particle cumulant as genuine three-particle correlation, with higher connected sectors forming a hierarchy:

- W. Kutzelnigg and D. Mukherjee, *Cumulant expansion of the reduced density matrices*, Journal of Chemical Physics 110, 2800–2809 (1999), DOI `10.1063/1.478189`.
- W. Kutzelnigg, *n-Electron problem and its formulation in terms of k-particle density cumulants*, International Journal of Quantum Chemistry 95, 404–423 (2003), DOI `10.1002/qua.10751`.

The standard cumulant/connected-correlation literature therefore blocks any claim that the hierarchy itself is PDT-native novelty.

## 6. Surviving PDT-II obligation

Cycle 072 sharply relocates the open problem. PDT no longer needs to guess an arbitrary `Gamma_R`; it needs to derive, from physical PDT principles, **which connected sectors are accessible at a declared resource window, how their resource cost scales, and whether PDT imposes a new constraint on those sectors that differs from standard quantum/GPT composition**.

Until such a restriction or new physical prediction is derived, the connected hierarchy is an exact bookkeeping architecture, not a new law of nature.
