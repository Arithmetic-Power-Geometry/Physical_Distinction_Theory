"""Probe secondary public experimental datasets for reproducible PDT tests.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.
"""
from pathlib import Path
import urllib.request, zipfile, io
from pypdf import PdfReader
import pandas as pd
OUT=Path('results/real_data'); OUT.mkdir(parents=True,exist_ok=True)

ramsey_url='https://zenodo.org/records/15797402/files/Ramsey.zip?download=1'
ramsey=OUT/'ramsey_experimental.zip'
urllib.request.urlretrieve(ramsey_url,ramsey)
with zipfile.ZipFile(ramsey) as z:
    names=z.namelist()
    xlsx=[n for n in names if n.lower().endswith('.xlsx')]
    print('RAMSEY files',len(names),'xlsx',len(xlsx))
    print('\n'.join(xlsx[:30]))
    for name in xlsx[:3]:
        data=z.read(name)
        xl=pd.ExcelFile(io.BytesIO(data))
        print('\nRAMSEY WORKBOOK',name,'sheets',xl.sheet_names)
        for sh in xl.sheet_names[:2]:
            df=pd.read_excel(io.BytesIO(data),sheet_name=sh,header=None)
            print('SHEET',sh,'shape',df.shape)
            print(df.head(25).to_string(index=False,header=False))

u='https://mdpi-res.com/d_attachment/entropy/entropy-23-00122/article_deploy/entropy-23-00122-s001.pdf'
p=OUT/'qwpath_supplement.pdf'
req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
with urllib.request.urlopen(req,timeout=40) as r: p.write_bytes(r.read())
reader=PdfReader(str(p))
txt='\n'.join((pg.extract_text() or '') for pg in reader.pages)
(OUT/'qwpath_supplement.txt').write_text(txt)
print('QWPD pages',len(reader.pages),'chars',len(txt))
print(txt[:30000])
