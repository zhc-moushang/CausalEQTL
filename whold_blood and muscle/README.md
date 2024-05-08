## This part is the result of realizing the whole blood tissue and muscle tissue in the paper.

1.Data preprocessing follows the method in Data processing, we need the csv file and info file of each gene.  

2.Then, according to the method in assign_Y_label, each gene is assigned an expression value Y vector and a label vector label. The label vector label represents the information of real eQTLs.  

3.The number of samples in muscle tissue is different from the number of samples used in our simulations, so additional processing in processing is required.  

4.The purpose of CausalEQTL.py is to generate the command to run CausalEQTL.R, and then we use the script to execute each line of command.  
