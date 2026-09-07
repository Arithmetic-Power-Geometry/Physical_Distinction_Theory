from pathlib import Path
import sys,json,subprocess
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
subprocess.run([sys.executable,'-m','pytest','-q'],cwd=ROOT,check=True)
subprocess.run([sys.executable,str(ROOT/'scripts'/'reproduce_all.py')],cwd=ROOT,check=True)
subprocess.run([sys.executable,str(ROOT/'scripts'/'export_latex.py')],cwd=ROOT,check=True)
s=json.loads((ROOT/'results'/'summary.json').read_text())
assert s['data_processing_violations']==0
assert s['classical_chsh']==2.0 and s['pr_box_chsh']==4.0
assert s['chsh_best']<=s['tsirelson']+1e-12
assert s['p2_max_parallelogram_defect']<1e-9
assert abs(s['born_refinement_minimizer_numeric']-2.0)<1e-5
assert abs(s['born_refinement_objective_at_2'])<1e-20
print('PDT full verification gate: PASS')
