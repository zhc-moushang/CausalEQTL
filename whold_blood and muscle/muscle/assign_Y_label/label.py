import os
import sys
from tqdm import tqdm
from eqtl import eqtl
from chr_ensg import chr_ensg

tissue_list = os.listdir('muscle/peak/')
for chr in tqdm(tissue_list):
    label = '/muscle/peak/'+chr +'/'+ '/label'
    csv = '/muscle/peak/'+chr +'/'+ chr + '_GTEx_delete.csv'
    with open(csv,'r') as inf,open(label,'w+')as lab:
        next(inf)
        inf_list = []
        for line in inf:
            columns = line.strip().split(',')
            pos = columns[1]
            if pos in eqtl[chr_ensg[chr]]:
                inf_list.append(1)
            else:
                inf_list.append(0)
        for i in inf_list:
            lab.write(
                str(i) +'\n'
            )