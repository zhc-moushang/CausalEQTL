import os
import sys

if __name__=='__main__':

    ch=sys.argv[1]
    with open('GTEx_male/head.csv','r')as fr,open('1KG_male/head.csv','r')as fr1:
        head=fr.readline()
        head1=fr1.readline()
    KG_male=['-1']*250000000
    GTEx_male=['-1']*250000000
    with open('GTEx_male/GTEx_male_'+ch+'.csv','r')as fr:
        for line in fr.readlines():
            snp=line.strip('\n').split(',')
            GTEx_male[int(snp[1])]=line
    with open('1KG_male/1KG_male_'+ch+'.csv','r')as fr:
        for line in fr.readlines():
            snp=line.strip('\n').split(',')
            KG_male[int(snp[1])]=line
    with open('peak_depart/peak_depart_chr' + ch + '.txt', 'r') as fr:
        for line in fr.readlines():
            peak = line.strip('\n').split('\t')
            name = peak[0].replace(':', '_').replace('-', '_')
            os.system('mkdir ' + '/peak_50k/' + name)
            # part = peak[1].split(':')[1].split('-')
            bottom = int(peak[2])
            top = int(peak[3])
            with open('peak_50k/' + name + '/' + name + '_GTEx.csv', 'w') as fw, \
                    open('peak_50k/' + name + '/' + name + '_1KG.csv',
                         'w') as fw1:
                fw.write(head)
                fw1.write(head1)
                for i in range(bottom, top + 1):
                    if (GTEx_male[i] != '-1'):
                        fw.write(GTEx_male[i])
                        fw1.write(KG_male[i])
