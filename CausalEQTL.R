library(readr)
library(optparse)
library(glmnet)
library(L0Learn)

maxSize= 10
minSize= 0
mum_sites=6157
maf_weights= 1.0
args_list=list(
make_option("--geno",type="character",default = NULL,help="INPUT:genotype file",metavar="character"),
make_option("--pheno",type="character",default = NULL,help="INPUT:phenotype file",metavar="character"),
make_option("--out",type="character",default = NULL,help="OUTPUT:output path",metavar="character")
)
opt_parser = OptionParser(option_list=args_list)
opt = parse_args(opt_parser)

X <- read_csv(opt$geno)
X=X[,-c(1,2)]
X=as.data.frame(X)
X=t(X)
X=data.matrix(X)
Y=read.table(opt$pheno,header = TRUE,sep = '\t')[,-c(1)]
Y <- data.matrix(Y)

cvfit = L0Learn.cvfit(X, Y, nFolds=5, seed=2, penalty="L0L1", nGamma=10, gammaMin=0.001, gammaMax=1.0, maxSuppSize=maxSize, intercept= FALSE, algorithm="CDPSI")
optimalLambda  = 0.0001
optimalGammaIndex= which(unlist(lapply(cvfit$cvMeans, min)) == min(unlist(lapply(cvfit$cvMeans, min))))
tmp =coef(cvfit, lambda=optimalLambda, gamma=cvfit$fit$gamma[optimalGammaIndex])
write.table(as.data.frame(as.matrix(tmp)),file=opt$out,row.names = F,col.names = F,quote = F)
