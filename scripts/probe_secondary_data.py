"""Probe secondary public experimental datasets for reproducible PDT tests.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.
"""
from pathlib import Path
import urllib.request, zipfile, subprocess, os
OUT=Path('results/real_data'); OUT.mkdir(parents=True,exist_ok=True)

# Trapped-ion/atomic Ramsey experimental archive
ramsey_url='https://zenodo.org/records/15797402/files/Ramsey.zip?download=1'
ramsey=OUT/'ramsey_experimental.zip'
urllib.request.urlretrieve(ramsey_url,ramsey)
with zipfile.ZipFile(ramsey) as z:
    names=z.namelist()
    print('RAMSEY files',len(names))
    print('\n'.join(names[:120]))

# Quantum which-path detector supplement. The /s1 route is the publisher's public supplement link.
urls=[
 'https://www.mdpi.com/1099-4300/23/1/122/s1',
 'https://mdpi-res.com/d_attachment/entropy/entropy-23-00122/article_deploy/entropy-23-00122-s001.pdf',
 'https://mdpi-res.com/d_attachment/entropy/entropy-23-00122/article_deploy/entropy-23-00122-s001.pdf?version=1610985976',
]
for i,u in enumerate(urls):
    try:
        p=OUT/f'qwpath_supp_{i}.pdf'
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=40) as r:
            data=r.read()
            print('QWPD candidate',i,'status',getattr(r,'status',None),'type',r.headers.get('content-type'),'bytes',len(data),'final',r.geturl())
        p.write_bytes(data)
        if data[:4]==b'%PDF':
            try:
                subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
                txt=p.with_suffix('.txt').read_text(errors='ignore')
                print('QWPD TEXT START\n',txt[:16000])
            except Exception as e: print('pdftotext failed',e)
            break
    except Exception as e:
        print('QWPD candidate',i,'failed',repr(e))
