# CausalEQTL
An algorithm called CausalEQTL,which integrates L0+L1 penalized regression with an ensemble approach to localize eQTL, thereby enhancing prediction performance precisely.
## Preparation
In our work, the model uses R language. If you want to create an R language environment, then I recommend you to use conda.
```
conda create -n r
conda install r
```
If you need to install L0Learn, you can use the following R code in your R environment:
```
install.packages("L0Learn", repos = "http://cran.rstudio.com")
```
or
```
library(devtools)
install_github("hazimehh/L0Learn")
```
If you have installation issues we recommend you go to https://github.com/hazimehh/L0Learn
## Run
X is the genotype file of the gene, Y is the phenotype file of the gene, and out is the output file.
```
Rscript CausalEQTL.R --geno {X} --pheno {Y} --out {out}
```
Because we are using a different input format, you may need to modify the following code.
```
X <- read_csv(opt$geno)
X=X[,-c(1,2)]
X=as.data.frame(X)
X=t(X)
X=data.matrix(X)
Y=read.table(opt$pheno,header = TRUE,sep = '\t')[,-c(1)]
Y <- data.matrix(Y)
```
## Result
Our results for 48 organizations on the GTEx dataset are placed in CausaEQTL_result.
## Cite
If our work is helpful to you, we encourage you to cite our paper: https://doi.org/10.1016/j.csbj.2024.05.050
```
@article{wang2024optimal,
  title={Optimal variable identification for accurate detection of causal expression Quantitative Trait Loci with applications in heart-related diseases},
  author={Wang, Guishen and Zhang, Hangchen and Shao, Mengting and Tian, Min and Feng, Hui and Li, Qiaoling and Cao, Chen},
  journal={Computational and Structural Biotechnology Journal},
  volume={23},
  pages={2478--2486},
  year={2024},
  publisher={Elsevier}
}
```
