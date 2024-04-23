import sys


def geneInfo(name,snpMap):
    with open('peak_50k/'+name+'/'+name+'.info','w')as fw,open('peak_50k/'+name+'/'+name+'_GTEx.csv','r')as fr:
        fr.readline()
        fw.write("#CHR\tPOS\tRS_ID\tREF\tALT\tORIGIN\tCOEFF\tMAF\n")
        for line in fr.readlines():
            record=line.strip('\n').split(',')
            key=record[0]+','+record[1]
            if(key in snpMap.keys()):
                fw.write(snpMap[key])


if __name__=='__main__':
    name=sys.argv[1]
    ch=name.split('_')[0].replace('chr','')
    snpMap={}
    with open('INFO_filter/INFO_'+ch+'.info','r')as fr:
        for line in fr.readlines():
            snp=line.strip('\n').split('\t')
            key=snp[0]+','+snp[1]
            snpMap.update({key:line})
    geneInfo(name,snpMap)

