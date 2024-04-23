

map_1KG={}
with open('1KG_sorted.csv','r')as fr:
    head1=fr.readline()
    for line in fr.readlines():
        record=line.strip('\n').split(',')
        map_1KG.update({record[0]+','+record[1]:line})
with open('GTEx37_sorted.csv','r')as fr1,open('1KG_sorted_same.csv','w')as fw,open('GTEx37_sorted_same.csv','w')as fw1:
    fw.write(head1)
    fw1.write(fr1.readline())
    for line in fr1.readlines():
        record=line.strip('\n').split(',')
        key=record[0]+','+record[1]
        if( key in map_1KG.keys()):
            fw.write(map_1KG[key])
            fw1.write(line)
