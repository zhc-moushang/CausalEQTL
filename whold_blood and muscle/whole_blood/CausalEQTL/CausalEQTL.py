import os
from tqdm import tqdm
file_list = os.listdir('whole_blood/peak')
for chr in tqdm(file_list):
    X = 'whole_blood/peak/'+chr+'/'+chr + '_GTEx.csv'
    Y = 'whole_blood/peak/'+chr + '/Y'
    result_path = 'whole_blood/peak/'+chr + '/l0l1.effect'
    with open('CausalEQTL.txt', 'a+') as f:
        f.write(
           'Rscript' + '\t' + 'CausalEQTL.R' + '\t' + '--geno' + '\t' + X + '\t'
           + '--pheno' + '\t' + Y + '\t' + '--out' + '\t' + result_path  + '\n'
       )
