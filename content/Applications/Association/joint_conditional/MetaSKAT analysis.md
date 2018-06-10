
+++
title = "MetaSKAT"
weight = 6
+++


## Association Analysis with the Meta SKAT R Program 


The R extension for `RTest` is available [HERE][1]. For details on the format of this script please refer to the [`RTest` method documentation][2]. 



### 1. Example

We analyze association with a binary trait named `X6` conditioning on 3 covariates `X8, X9, X10`. Group information is provided by `race`. For each testing group, data is first cleaned by removing samples missing greater than 50% calls, then by removing variants missing 50% calls. 



#### 1.1 Basic command

The following command uses the default parameter settings in the R script: 



    vtools associate variant X6 --covariates X8 X9 X10 race \
           -m "RTest ~/MetaSKAT.VAT.R --name MetaSKAT --out_type 'D' --group_colname 'race' " \
           --discard_samples '%(NA)>0.5' --discard_variants '%(NA)>0.5' \
           --group_by 'refGene.name2' -j8 --to_db MetaSKAT > MetaSKAT.txt
    
    INFO: Loading R script '/home/gw/MetaSKAT.VAT.R'
    INFO: 252 samples are found
    INFO: 131 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [===================================] 252 72.5/s in 00:00:03
    Testing for association: 100% [==============================] 131/122 10.4/s in 00:00:12
    INFO: Association tests on 131 groups have completed. 122 failed.
    INFO: Using annotation DB MetaSKAT in project mskat.
    INFO: Annotation database used to record results of association tests. Created on Tue, 16 Apr 2013 01:40:03
    INFO: 131 out of 23242 refgene.name2 are annotated through annotation database MetaSKAT
    

Note that with such stringent cleaning criteria only 9 out of 131 groups are analyzed. In the R program we throw an error on having no samples, only one variant, or only one study group. Please take a look at the `*.log` file for details of the errors. 



    refGene_name2	pvalue_MetaSKAT	n_pop1_MetaSKAT	n_pop2_MetaSKAT	n_pop3_MetaSKAT
    gene1	0.686969	79	84	NAN
    gene2	0.0697923	84	68	NAN
    gene3	0.0684316	81	83	NAN
    gene4	0.426611	63	84	NAN
    gene5	0.591128	70	77	NAN
    gene6	0.00586012	84	81	NAN
    gene7	0.306343	77	84	NAN
    gene8	0.0951658	81	84	NAN
    gene9	0.0988938	84	84	84
    



#### 1.2 Use other parameters

From the way `MetaSKAT.VAT.R` is written we known `out_type` and `group_colname` are required. They have to be explicitly specified at all times. Other parameters have default values, which can be altered by passing them like, for example: 



    ... -m "RTest ~/MetaSKAT.VAT.R --name MetaSKAT \
       --out_type 'D' --group_colname 'race' --pval.method 'davies' " ...

 [1]: http://vtools.houstonbioinformatics.org/programs/RTest/MetaSKAT.VAT.R
 [2]:   /applications/association/create_your_test/running-r-programs/