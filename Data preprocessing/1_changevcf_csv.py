def change(i):
    data=i.split('|')
    count=0
    if(data[0]=='1'):
        count+=1
    if(data[1]=='1'):
        count+=1
    return str(count)

with open('GTEx.ALL.vcf','r')as fr,open('GTEx.ALL.csv','w')as fw:
    for i in range(82):
        fr.readline()
    name=fr.readline().strip('\n').split('\t')
    head='CHR,LOC'
    for i in name[9:]:
        head=head+','+i
    head+='\n'
    fw.write(head)
    for line in fr.readlines():
	
        data=line.strip('\n').split('\t')
        record=data[0]+','+data[1]
        for i in data[9:]:
            record=record+','+change(i)
        record+='\n'
        fw.write(record)
        
