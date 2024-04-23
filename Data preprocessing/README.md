##This part introduces our data preprocessing  
#We conducted experiments on a large cluster, so our code is also designed to facilitate parallel computing.  

1.Convert GTEx vcf file to csv file  
2.GTEx version converted from GRCH38 to GRCH37  
3.Determine whether the 1000G SNP is GRCH37 or GRCH38 version  
4.Sort by position  
5.Positional alignment of GTEx and 1000G  
6.Filter SNPs whose maf is too small or too large  
7.Cut according to gene range  
8.Cut the info file of each gene  
