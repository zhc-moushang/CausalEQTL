import os
import numpy as np
from dic_ensg_chr import dic_ensg_chr
from tqdm import tqdm
dic_ensg_exp = {}
with open('Whole_Blood.v8.normalized_expression.bed','r') as f:
    next(f)
    for line in f:
        line = line.strip().split()
        ensg = line[3]
        exp = line[4:]
        dic_ensg_exp[ensg] = exp
for item in tqdm(dic_ensg_chr.items()):
    ensg = item[0]
    chr = item[1]
    if 'chrX' in chr or 'chrY' in chr or 'chrXY'in chr :
        continue
    Y = dic_ensg_exp[ensg]
    if not os.path.exists('peak_50k/' + chr + '/whole_blood/'):
        os.mkdir('peak_50k/' + chr + '/whole_blood/')
    with open('peak_50k/'+chr+'/whole_blood/Y','w+') as f:
        f.write('ID\tSim_Pheno_0\n')
        for i in Y:
            f.write('demo\t'+i+'\n')

# dic_ensg_chr.py 是从 gene_hg19.txt文件中找基因名存在于Whole_Blood.v8.egenes.txt 中的基因.之后生成的 gene_id ：chr start end 的字典
