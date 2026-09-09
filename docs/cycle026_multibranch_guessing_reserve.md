# Cycle 026 — Multi-branch guessing-reserve balance

## Result

Let a classical branch label \(X\) be encoded in a joint system–environment record \(SE\). Define

\[
G_{SE}(t)=P_{\rm guess}(X|SE)_t,\qquad
G_S(t)=P_{\rm guess}(X|S)_t,
\]

and the **guessing reserve**

\[
R_G(t)=G_{SE}(t)-G_S(t)\ge 0.
\]

Suppose the same CPTP evolution acts on the joint record from \(s\) to \(t\). Data processing for optimal guessing probability gives

\[
L_G:=G_{SE}(s)-G_{SE}(t)\ge0.
\]

Then, purely by substitution,

\[
\boxed{G_S(t)-G_S(s)=R_G(s)-R_G(t)-L_G.}
\]

Therefore

\[
\boxed{\Delta G_S\le R_G(s).}
\]

For a common reversible evolution, \(G_{SE}\) is invariant, so \(L_G=0\) and

\[
\boxed{\Delta G_S=-\Delta R_G.}
\]

This extends the binary trace-distance reserve balance to arbitrary numbers of branches and arbitrary priors, using an operational one-shot task: optimal exact branch identification.

## Same-input kill test

Under identical microscopic quantum inputs, identical priors, and a common CPTP process,

\[
P_{\rm guess}^{S}(t)-P_{\rm guess}^{S}(s)
>
P_{\rm guess}^{SE}(s)-P_{\rm guess}^{S}(s)
\]

is impossible. A PDT prediction crossing this boundary must change a physical ingredient (state/process/effect/probability rule, available subsystem, side information, copies, postselection accounting, or another declared resource).

## Proof status

**PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN.**

The operational identity \(P_{\rm guess}(X|B)=2^{-H_{\min}(X|B)}\) for classical \(X\) is established one-shot quantum information theory; the relevant data-processing monotonicity is standard. The reserve decomposition is therefore useful PDT bookkeeping but is not claimed as historically new mathematics.

Prior-art anchor:

- R. König, R. Renner, C. Schaffner, “The Operational Meaning of Min- and Max-Entropy,” *IEEE Transactions on Information Theory* 55(9), 4337–4347 (2009), DOI 10.1109/TIT.2009.2025545.

## Adversarial numerical audit

The executable audit uses the commuting/classical subtheory, where optimal guessing probability is exact:

\[
P_{\rm guess}(X|Z)=\sum_z \max_x p_x P(z|x).
\]

It samples nonuniform priors, multi-branch conditional records, irreversible common stochastic maps, and reversible permutation channels. Dimensions \(1\) through \(12\), plus \(16,24,32,48\), are tested with 200 fixed-seed trials each. The exact balance residual and the bound excess remain at floating-point roundoff.

## Interpretation

This does **not** create a PDT-vs-QM prediction. It removes a loophole: multi-branch local distinguishability revival cannot be called newly created distinction when the joint record already contained the corresponding one-shot guessing advantage.
