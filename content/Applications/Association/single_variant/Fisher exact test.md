
+++
title = "Fisher exact test"
weight = 1
+++


## Fisher's Exact Test for Single Variant Analysis 



### 1. Introduction

Genetic association studies of common variants in case control samples usually compare directly the differences in frequencies of an allele or genotype between case and control populations, with the assumption that a significant difference in frequencies is indication to association between the locus and increase risk of disease. Many statistical tests for binomial or multinomial proportions can be used for such analysis, including Fisher's exact test, {$\chi^2$} test and Cochran-Armitage Trend Test. For rare variants association tests, single variant analysis will be underpowered (see Sahai H. 1996(H. Sahai and A. Khurshid (1996) **Formulas and tables for the determination of sample sizes and power in clinical trials for testing differences in proportions for the matched pair design: a review**. *Fundamental & Clinical Pharmacology* doi:`10.1111/j.1472-8206.1996.tb00614.x`. <http://doi.wiley.com/10.1111/j.1472-8206.1996.tb00614.x>) for power and sample size estimation for tests for proportions). Still single variant tests can be useful when only summary statistics is avaiable for controls (e.g., only MAF is available from public database), or one wants to compare the differences in frequency between populations for other purposes. For single variants analysis we offer the Fisher's exact test routine which is abit conservative but guarantees type I error control for small sample sizes. Fisher's test method in `VAT` is implemented as a special function for `vtools update` command, which is very efficient. 

For Single variant tests adjusting for covariates, or tests for quantitative phenotypes, please refer to the [multivariate methods][1] in `VAT`. 



### 2. Usage

The function `Fisher_exact(num_var_alleles_case, num_var_alleles_ctrl, 2*num_gt_case, 2*num_gt_ctrl)` tests for association of an alternate allele with a phenotype (i.e., case or control) status. Given a variant site to be tested, the function takes in the following 4 parameters, that are obtainable through `vtools` functions: 



*   `num_var_alleles_case`: number of alternative alleles for the case samples 
*   `num_var_alleles_ctrl`: number of alternative alleles for the control samples 
*   `num_gt_case`: total number of genotypes for the case samples 
*   `num_gt_ctrl`: total number of genotypes for the control samples 

<details><summary> Examples: Fisher's exact test for case/ctrl association</summary> First, we compute statistics separately in cases and ctrls: 



    vtools update variant --from_stat 'num_gt_case=#(GT)' 'num_var_alleles_case=#(alt)' --samples "filename in ('V1.vcf', 'V2.vcf')"
    

    Counting variants: 100% [================================] 2 69.2/s in 00:00:00
    INFO: Adding field num_var_alleles_case
    INFO: Adding field num_gt_case
    Updating variant: 100% [==============================] 1,341 41.9K/s in 00:00:00
    INFO: 1340 records are updated
    



    vtools update variant --from_stat "num_gt_ctrl=#(GT)" "num_var_alleles_ctrl=#(alt)" --samples "filename = 'V3.vcf'"
    

    Counting variants: 100% [===============================] 1 220.3/s in 00:00:00
    INFO: Adding field num_var_alleles_ctrl
    INFO: Adding field num_gt_ctrl
    Updating variant: 100% [=============================] 988 42.7K/s in 00:00:00
    INFO: 987 records are updated
    

And calcualte p-value for the Fisher's exact test: 



    vtools update variant --set "prop_pval=Fisher_exact(num_var_alleles_case, num_var_alleles_ctrl, 2*num_gt_case, 2*num_gt_ctrl)"
    

    INFO: Adding field prop_pva
    

</details>

 [1]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.Multivariate?action=edit