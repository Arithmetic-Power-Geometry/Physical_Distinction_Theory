import numpy as np
import pdt_lab as p


def test_capacity_geometry_and_ceu_cer_no_go():
    assert p.codebook_capacity_bits(2) == 1.0
    assert abs(p.parallelogram_defect([1, 0], [0, 1], 2.0)) < 1e-12
    assert abs(p.parallelogram_defect([1, 0], [0, 1], 3.0)) > 1e-3
    audit = p.ceu_cer_counterfamily([1.5, 2.0, 3.0])
    assert bool(audit.loc[audit.p == 2.0, "euclidean"].iloc[0])
    assert not bool(audit.loc[audit.p == 3.0, "euclidean"].iloc[0])


def test_rde_conditioned_euclidean_tools():
    R = np.array([[0, -1], [1, 0]], float)
    G = p.finite_group_invariant_metric([np.eye(2), R, R @ R, R @ R @ R])
    assert np.allclose(G, np.eye(2))
    assert abs(p.bqdc_residual([1, 2], [3, -1], G)) < 1e-12
    assert abs(p.polarization([1, 2], [3, 4]) - 11) < 1e-12


def test_born_and_general_bilinear_tsirelson():
    assert np.allclose(p.born_probabilities([1, 1j]), [0.5, 0.5])
    T = np.eye(2)
    a0 = np.array([1.0, 0.0]); a1 = np.array([0.0, 1.0])
    b0 = np.array([1.0, 1.0]) / np.sqrt(2)
    b1 = np.array([1.0, -1.0]) / np.sqrt(2)
    assert abs(p.operator_norm(T) - 1.0) < 1e-12
    assert abs(p.chsh_bilinear(a0, a1, b0, b1, T) - p.tsirelson_bound()) < 1e-12


def test_stinespring_global_and_local_distinction():
    r = np.diag([1, 0]).astype(complex)
    s = np.diag([0, 1]).astype(complex)
    k = p.amplitude_damping_kraus(0.41)
    assert p.global_distinction_residual(r, s, k) < 1e-12
    assert p.local_contraction_gap(r, s, k) >= -1e-12


def test_pure_and_mixed_record_relations():
    D = 0.6
    kap = p.overlap_from_pure_distinguishability(D)
    assert abs(p.pure_record_distinguishability(kap) - D) < 1e-12
    assert abs(2 ** (-p.coherence_record_bit(kap)) - kap) < 1e-12
    eta = np.diag([0.7, 0.3]).astype(complex)
    U0 = np.eye(2, dtype=complex)
    U1 = np.diag([1.0, np.exp(0.8j)])
    env = p.mixed_record_envelope(eta, U0, U1)
    assert env["left_residual"] >= -1e-10
    assert env["right_residual"] >= -1e-10


def test_phase_complete_adde():
    gamma, omega, t = 0.23, 1.7, 0.9
    chi = np.exp((-gamma + 1j * omega) * t)
    chi_dot = (-gamma + 1j * omega) * chi
    g, w = p.phase_complete_generator(chi, chi_dot)
    assert abs(g - gamma) < 1e-12
    assert abs(w - omega) < 1e-12


def test_total_distinction_tensor_exact_identity():
    G = np.array([[2.0, 0.2], [0.2, 1.3]])
    Gd = np.array([[0.1, -0.03], [-0.03, -0.04]])
    L = np.array([[-0.2, 0.1], [-0.05, -0.1]])
    X = np.array([0.7, -1.2])
    A = p.total_distinction_tensor(G, Gd, L)
    assert np.allclose(A, p.metric_motion_component(Gd) + p.state_flow_component(G, L))
    assert abs(p.total_tensor_identity_residual(X, G, Gd, L)) < 1e-12


def test_resource_relative_thermodynamic_tools():
    assert p.shannon_bits([0.99, 0.01]) < 1
    H = np.diag([0.0, 1e-23])
    rho = np.diag([0.8, 0.2]).astype(complex)
    effects = [np.diag([1.0, 0.0]), np.diag([0.0, 1.0])]
    gamma = p.gibbs_state(H, 300)
    beta = p.hypothesis_testing_beta(rho, gamma, effects, 0.25)
    assert np.isfinite(beta)


def test_synthetic_zero_fit_pdt_model():
    df, meta = p.synthetic_record_dataset(noise=0.004)
    tab = p.compare_models(df, meta)
    row = tab[tab.Model == "PDT/ADDE"].iloc[0]
    assert row.k_dyn == 0
    assert row.RMSE < 0.01


def test_manuscript_result_registry():
    assert len(p.theorem_status_matrix()) == 15
    assert p.evidence_count_summary() == {
        "N_real": 3,
        "N_independent_record": 1,
        "N_time_decay": 2,
        "N_decisive": 0,
    }
