"""Generate all software-derived PDT manuscript tables and figures into results/."""
from pathlib import Path
import json
import sys
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import pdt_lab as p

OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)


def logic_svg() -> str:
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="560" viewBox="0 0 1100 560">
<style>text{font-family:Arial,sans-serif;font-size:18px}.box{fill:white;stroke:black;stroke-width:2}.a{stroke:black;stroke-width:2;fill:none;marker-end:url(#m)}.d{stroke-dasharray:8 6}.dot{stroke-dasharray:2 7}</style>
<defs><marker id="m" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="black"/></marker></defs>
<rect class="box" x="40" y="70" width="150" height="70" rx="8"/><text x="115" y="100" text-anchor="middle">physical</text><text x="115" y="125" text-anchor="middle">distinction</text>
<rect class="box" x="260" y="70" width="150" height="70" rx="8"/><text x="335" y="100" text-anchor="middle">resource</text><text x="335" y="125" text-anchor="middle">window</text>
<rect class="box" x="480" y="70" width="170" height="70" rx="8"/><text x="565" y="100" text-anchor="middle">state-resolved</text><text x="565" y="125" text-anchor="middle">geometry</text>
<rect class="box" x="760" y="70" width="150" height="70" rx="8"/><text x="835" y="100" text-anchor="middle">Euclidean</text><text x="835" y="125" text-anchor="middle">B^n</text><text x="700" y="52" text-anchor="middle" font-size="16">CEU+CER+RDE</text>
<rect class="box" x="730" y="280" width="220" height="80" rx="8"/><text x="840" y="310" text-anchor="middle">B^3 / quantum</text><text x="840" y="338" text-anchor="middle">elementary system</text><text x="930" y="225" font-size="16">classification</text>
<rect class="box" x="475" y="285" width="180" height="70" rx="8"/><text x="565" y="315" text-anchor="middle">environmental</text><text x="565" y="340" text-anchor="middle">records</text>
<rect class="box" x="245" y="280" width="190" height="80" rx="8"/><text x="340" y="310" text-anchor="middle">ADDE + total</text><text x="340" y="338" text-anchor="middle">distinction tensor</text>
<rect class="box" x="25" y="280" width="180" height="80" rx="8"/><text x="115" y="310" text-anchor="middle">resource-relative</text><text x="115" y="338" text-anchor="middle">thermodynamics</text>
<rect class="box" x="455" y="450" width="220" height="75" rx="8"/><text x="565" y="480" text-anchor="middle">spacetime / gravity</text><text x="565" y="507" text-anchor="middle">frontier</text>
<path class="a" d="M190 105 H250"/><path class="a" d="M410 105 H470"/><path class="a d" d="M650 105 H750"/><path class="a" style="stroke-width:4" d="M835 140 V270"/>
<path class="a" d="M730 320 H665"/><path class="a" d="M475 320 H445"/><path class="a d" d="M245 320 H215"/><path class="a dot" d="M565 355 V440"/>
</svg>'''


def rmse_svg(table2: pd.DataFrame) -> str:
    det = table2[table2["Statistics"] == "Deterministic"].set_index("Model")
    order = ["PDT/ADDE", "GKLS", "Non-Markovian", "Schrodinger"]
    vals = [float(det.loc[m, "RMSE"]) for m in order]
    bars = []
    for i, (name, val) in enumerate(zip(order, vals)):
        x = 95 + i * 145
        h = 300 * val / 0.4
        y = 390 - h
        bars.append(f'<rect x="{x}" y="{y:.2f}" width="70" height="{h:.2f}" fill="white" stroke="black"/><text x="{x+35}" y="420" text-anchor="middle" font-size="14">{name}</text><text x="{x+35}" y="{y-8:.2f}" text-anchor="middle" font-size="13">{val:.6f}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="470" viewBox="0 0 700 470"><style>text{{font-family:Arial,sans-serif}}</style><text x="350" y="30" text-anchor="middle" font-size="19">Synthetic controlled-record RMSE (deterministic values shown)</text><line x1="70" y1="390" x2="650" y2="390" stroke="black"/><line x1="70" y1="60" x2="70" y2="390" stroke="black"/><text x="20" y="225" transform="rotate(-90 20 225)" text-anchor="middle">RMSE</text>{''.join(bars)}</svg>'''


def table3_from_refreshed_results() -> pd.DataFrame:
    rdir = OUT / "real_experimental"
    try:
        q = json.loads((rdir / "qwpd_summary.json").read_text())
        n = json.loads((rdir / "npl_summary.json").read_text())
        r = json.loads((rdir / "ramsey_summary.json").read_text())
        return pd.DataFrame([
            ["Photonic qubit + quantum which-path detector", "Independent system coherence and detector distinguishability", f"Pure-record zero-fit RMSE {q['zero_fit_pure_record_RMSE']:.6f}; MAE {q['zero_fit_pure_record_MAE']:.6f}", "Not decisive: detector records are mixed/imperfect; a mixed same-input microscopic baseline is required."],
            ["NPL driven superconducting qubits", f"{n['raw_rows']} raw rows; {n['usable_XY_traces']} reconstructed X/Y coherence traces", f"Median RMSE: Schrodinger {n['median_schrodinger_RMSE']:.6f}; GKLS {n['median_GKLS_RMSE']:.6f}; non-Markovian {n['median_nonmarkovian_RMSE']:.6f}", "Not decisive: no independent environment record in the public file."],
            ["Ramsey experimental archive", f"{r['n_delay_points']} visibility-delay points", f"Schrodinger RMSE {r['schrodinger_RMSE']:.6f}; fitted GKLS {r['GKLS_RMSE']:.6f}; fitted gamma={r['fitted_gamma']:.8f}", "Not decisive: no independent environment record."],
        ], columns=["Dataset", "Observable audit", "Main result", "Status"])
    except (FileNotFoundError, KeyError, TypeError):
        return p.real_data_audit_table()


def main():
    p.ceu_cer_counterfamily().to_csv(OUT / "geometry_audit.csv", index=False)
    table1 = p.core_numerical_audit()
    table1.to_csv(OUT / "table1_core_numerical_audit.csv", index=False)

    parts = []
    for poisson in (False, True):
        df, meta = p.synthetic_record_dataset(poisson=poisson)
        tab = p.compare_models(df, meta)
        tab.insert(0, "Statistics", "Poisson" if poisson else "Deterministic")
        parts.append(tab)
    table2 = pd.concat(parts, ignore_index=True)
    table2.to_csv(OUT / "table2_synthetic_model_comparison.csv", index=False)
    table2.to_csv(OUT / "model_comparison.csv", index=False)

    table3_from_refreshed_results().to_csv(OUT / "table3_real_data_audit.csv", index=False)
    p.theorem_status_matrix().to_csv(OUT / "table4_proof_status_matrix.csv", index=False)

    rng = np.random.default_rng(20260907)
    tensor_rows = []
    for i in range(20):
        M = rng.normal(size=(3, 3)); G = M.T @ M + np.eye(3)
        D = rng.normal(size=(3, 3)); Gd = 0.5 * (D + D.T)
        L = rng.normal(size=(3, 3)) * 0.1; X = rng.normal(size=3)
        A = p.total_distinction_tensor(G, Gd, L)
        tensor_rows.append({"case": i, "identity_residual": p.total_tensor_identity_residual(X, G, Gd, L), "A_min_eigenvalue": float(np.linalg.eigvalsh(A).min())})
    tensor = pd.DataFrame(tensor_rows)
    tensor.to_csv(OUT / "total_tensor_verification.csv", index=False)

    eta = np.diag([0.7, 0.3]).astype(complex)
    U0 = np.eye(2, dtype=complex); U1 = np.diag([1.0, np.exp(0.8j)])
    pd.DataFrame([p.mixed_record_envelope(eta, U0, U1)]).to_csv(OUT / "mixed_record_envelope_example.csv", index=False)

    (OUT / "figure1_pdt_logical_architecture.svg").write_text(logic_svg())
    (OUT / "figure2_synthetic_rmse.svg").write_text(rmse_svg(table2))

    summary = {
        "paper_tables_generated": 4,
        "paper_figures_generated": 2,
        "evidence_counts": p.evidence_count_summary(),
        "tensor_max_abs_identity_residual": float(tensor.identity_residual.abs().max()),
        "table1": dict(zip(table1.Quantity, table1.Result)),
    }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
