import sys

file=sys.argv[1]

arr=['-1']*250000000
with open(file,'r')as fr:
    for line in fr.readlines():
        snp=line.strip('\n').split(',')
        if(arr[int(snp[1])]!='-1'):
            print(snp[1])
        arr[int(snp[1])]=line
with open(file+'_sorted','w')as fw:
    for ele in arr:
        if(ele!='-1'):
            fw.write(ele)
