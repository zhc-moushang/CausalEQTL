from dic_ensg_chr import ensg_chr
from tqdm import tqdm
dic_ensg_exp = {}
with open('muscle_delete.csv','r') as f:
    next(f)
    for line in f:
        line = line.strip().split(',')
        ensg = line[3]
        exp = line[4:]
        dic_ensg_exp[ensg] = exp

for item in tqdm(ensg_chr.items()):
    ensg = item[0]
    chr = item[1]
    Y = dic_ensg_exp[ensg]
    with open('/gpfs/chencao/eqtlporj/muscle/peak/'+chr+'/Y','w+') as f:
        f.write('ID\tSim_Pheno_0\n')
        for i in Y:
            f.write('demo\t'+i+'\n')

