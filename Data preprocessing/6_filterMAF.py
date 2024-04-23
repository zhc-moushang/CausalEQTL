import sys




if __name__=='__main__':
    ch=sys.argv[1]
    snp=[]
    with open("INFO_"+ch+'.info','r')as fr,open('INFO_'+ch+'.info','w')as fw:
        for line in fr.readlines():
            info=line.strip('\n').split('\t')
            if(float(info[7])>=0.05 and float(info[7])<=0.95):
                snp.append(info[0]+','+info[1])
                fw.write(line)
    with open('GTEx/GTEx_'+ch+'.csv','r')as fr1,\
         open('1KG/1KG_'+ch+'.csv','r')as fr2,\
         open('GTEx_final/GTEx_'+ch+'.csv','w')as fw1,\
         open('1KG_final/1KG_'+ch+'.csv','w')as fw2:
        for line1 in fr1.readlines():
            line2=fr2.readline()
            data=line1.strip('\n').split(',')
            if(data[0]+','+data[1] in snp):
                fw1.write(line1)
                fw2.write(line2)
