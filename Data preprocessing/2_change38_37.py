snpMap={}
with open('dbsnp.gtex','r')as fr:
    for line in fr.readlines():
        snp=line.strip('\n').split('\t')
        key=snp[0]+','+snp[1]
        value=snp[5]+','+snp[6]
        snpMap.update({key:value})
with open('GTEx.ALL.csv','r')as fr,open('GTEx_37.csv','w')as fw:
    fw.write(fr.readline())
    for line in fr.readlines():
        snp=line.strip('\n').split(',')
        key=snp[0]+','+snp[1]
        if(key in snpMap.keys()):
            record=snpMap[key]
            for i in snp[2:]:
                record=record+','+i
            record+='\n'
            fw.write(record)
