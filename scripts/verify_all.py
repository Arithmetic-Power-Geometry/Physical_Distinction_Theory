from pathlib import Path
import json, subprocess, sys
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,'-m','pytest','-q'],cwd=root,check=True)
subprocess.run([sys.executable,'scripts/reproduce_all.py'],cwd=root,check=True)
s=json.loads((root/'results'/'summary.json').read_text())
assert s['data_processing_violations']==0
assert abs(s['chsh_best']-s['tsirelson'])<0.01
print('PDT verification PASS')
