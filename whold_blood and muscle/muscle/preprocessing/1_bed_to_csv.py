import csv
import os
from tqdm import tqdm
def txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as txtfile, open(csv_file, 'w', newline='') as csvfile:
        txt_reader = txtfile.readlines()
        csv_writer = csv.writer(csvfile)

        for line in txt_reader:
            # 将每一行内容以空格分割
            data = line.strip().split()
            # 将分割后的内容写入csv文件
            csv_writer.writerow(data)



txt_to_csv('Muscle.v8.normalized_expression.bed', 'muscle.csv')
