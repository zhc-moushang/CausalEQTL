snpMap38=[]
count38=0
snpMap37=[]
count37=0
with open('dbsnp.gtex','r')as fr:
    for line in fr.readlines():
        snp=line.strip('\n').split('\t')
        snpMap38.append(snp[0]+','+snp[1])
        snpMap37.append(snp[5]+','+snp[6])
with open('1KG_4.csv','r')as fr:
    line=fr.readline()
    flag=True
    while(flag):
        line=fr.readline()
        if(not line):
            flag=False
            break
        else:
            data=line.strip('\n').split(',')
            key=data[0]+','+data[1]
            if( key in snpMap38):
                count38+=1
            if( key in snpMap37):
                print(key)
                count37+=1
print("1KG in 38:"+str(count38))
print("1KG in 37:"+str(count37))

