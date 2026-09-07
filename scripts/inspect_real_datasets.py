"""Inspect public real experimental datasets used for PDT benchmarking.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.
"""
from pathlib import Path
import urllib.request, zipfile, io
import pandas as pd

OUT=Path('results/real_data'); OUT.mkdir(parents=True,exist_ok=True)

url='https://zenodo.org/records/8363718/files/modelling_non_markovian_noise_in_driven_superconducting_qubits_experiment_results.csv?download=1'
p=OUT/'npl_experiment_results.csv'
urllib.request.urlretrieve(url,p)
df=pd.read_csv(p)
print('NPL shape',df.shape)
print('NPL columns',list(df.columns))
print(df.head(12).to_string())
print('\nNPL dtypes\n',df.dtypes)
for c in df.columns:
    try:
        print('UNIQUE',c,df[c].dropna().astype(str).unique()[:20])
    except Exception: pass
