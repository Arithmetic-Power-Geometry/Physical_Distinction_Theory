# Cycle 010 — Programmability kill test for the OSC dimension route

**Status: DECISIVE FALSIFICATION of one proposed derivation route / prior-art boundary clarified / NOT A BREAKTHROUGH**

## Question

Can Operational Self-Calibration (OSC) be justified by demanding that a single elementary system exactly and deterministically *program* every connected reversible control acting on another copy of the same system?

## Result

No. That exact-programming route is inadmissible in quantum theory and therefore cannot be used as a PDT-native derivation of OSC.

For deterministic exact programmable quantum processors, the Nielsen–Chuang no-programming theorem implies that distinct unitary operations require mutually orthogonal program states. A finite-dimensional program system therefore cannot exactly encode a continuous family of distinct unitaries. Consequently, replacing OSC by the stronger claim

`every reversible control has an exact program state in one finite-dimensional elementary system`

would fail even for the ordinary qubit.

## What survives

OSC itself is weaker and finite-resolution: it compares the **small-scale metric-entropy exponent** of the accessible control family with that of the elementary distinction state body. It does not require exact deterministic universal programming.

Thus the valid research target is an approximate operational principle of the form

`log N_G(epsilon) <= log N_X(c epsilon) + O(1)`

(or another experimentally justified resource inequality), not exact one-shot programming.

For a Euclidean elementary body `B^n` with full connected isotropy `SO(n)`, the exponents remain

`dim X = n`,

`dim SO(n) = n(n-1)/2`.

If an independently justified finite-resolution calibration/encoding principle yields the exponent inequality, then together with genuinely noncommuting reversibility the conditional `n=3` theorem from Cycle 009 still follows. This cycle does **not** supply that missing justification.

## Prior-art audit

The following established results directly constrain this route:

1. Nielsen and Chuang, *Programmable Quantum Gate Arrays*, Phys. Rev. Lett. 79, 321 (1997): deterministic exact universal programming of a continuous unitary family is impossible with a finite-dimensional program register.
2. Hillery, Ziman and Buzek, *Approximate programmable quantum processors*, Phys. Rev. A 73, 022345 (2006): finite-error programming is possible and the necessary program dimension admits nontrivial bounds.
3. Yang, Renner and Chiribella, *Optimal universal programming of unitary gates* (2020/2021): asymptotically optimal program-size scaling for approximate universal unitary programming is an established research problem/result.
4. Gschwendtner, Bluhm and Winter, *Programmability of covariant quantum channels*, Quantum 5, 488 (2021): symmetry-restricted channel families have separate programmability structure and program-dimension bounds.
5. Szarek, *Metric entropy of homogeneous spaces and Finsler geometry of classical Lie groups* (1997): covering-number asymptotics for classical compact groups are established mathematics.

Therefore any future PDT claim relating calibration-state capacity to reversible-control capacity must be distinguished carefully from existing approximate-programming and metric-entropy results.

## Kill-test conclusion

**FALSIFIED route:** derive OSC from exact deterministic self-programmability of a continuous reversible group by one finite-dimensional elementary program system.

**OPEN route:** derive a finite-resolution calibration-capacity inequality from genuinely PDT-native composition/resource principles, or test such an inequality experimentally.

This negative result is useful because it prevents a circular or physically impossible justification from being promoted as the missing `n=3` principle.
