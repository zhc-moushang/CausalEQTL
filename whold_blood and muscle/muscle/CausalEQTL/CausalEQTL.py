import os
from tqdm import tqdm
file_list = os.listdir('/peak_50k')
for chr in tqdm(file_list):
    X = 'muscle/peak_50k/'+chr+'/'+chr + '_GTEx.csv'
    Y = 'muscle/peak/'+chr + '/Y'
    result_path = 'muscle/peak/'+chr + '/l0l1.effect'
    with open('CausalEQTL.txt', 'a+') as f:
        f.write(
           'Rscript' + '\t' + 'CausalEQTL.R' + '\t' + '--geno' + '\t' + X + '\t'
           + '--pheno' + '\t' + Y + '\t' + '--out' + '\t' + result_path  + '\n'
       )
