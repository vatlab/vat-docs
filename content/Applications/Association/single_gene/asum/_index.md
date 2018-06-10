+++
title = "aSum test"
weight = 8
+++



## Data-adaptive Sum Test for Protective and Deleterious Variants 



### 1. Introduction

The data-adaptive sum test (aSum) by (Han and Pan, 2010) is the first method that took into consideration the difference in direction of effects (protective or deleterious) of rare variants in the same genetic region analyzed by a rare variant association test. It is a two-stage approach. In the first stage the effect size of each rare variant is evaluated in a multivariate regression analysis, identifying the variants having significant "protective" effects, i.e., variants with a negative log odds ratio associated with a \\(p\\) value smaller than <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script> \\(0.1\\). In the second stage, variants are collapsed across the genetic region similar to (Morris and Zeggini, 2010) but with the coding for protective variants *flipped*. The test statistic is a score test for logistic regression for case control data. 

The implementation of stage 1 in this program differs from the original paper. Instead of evaluating the effect size for each variant, it evaluates the difference in MAF of each variant between case and controls via an exact test to determine which variants are to be re-coded in stage 2. The same \\(p<0.1\\) criteria is used for stage 1, but in effect is more stringent than the original criteria for a multivariate logistic regression analysis. 



### 2. Details

#### 2.1 Command interface

    vtools show test aSum
    
    Name:          aSum
    Description:   Adaptive Sum score test for protective and deleterious variants, Han &
                   Pan 2010
    usage: vtools associate --method aSum [-h] [--name NAME] [-q1 MAFUPPER]
                                          [-q2 MAFLOWER] [-p N] [--adaptive C]
    
    Adaptive Sum score test for protective and deleterious variants, Han & Pan
    2010. In the first stage of the test, each variant site are evaluated for
    excess of minor alleles in controls and genotype codings are flipped, and the
    second stage performs a burden test similar to BRV (Morris & Zeggini 2009).
    This two-stage test is robust to a mixture of protective/risk variants within
    one gene, yet is computationally intensive. aSum test is a two-tailed test.
    
    optional arguments:
      -h, --help            show this help message and exit
      --name NAME           Name of the test that will be appended to names of
                            output fields, usually used to differentiate output of
                            different tests, or the same test with different
                            parameters.
      -q1 MAFUPPER, --mafupper MAFUPPER
                            Minor allele frequency upper limit. All variants
                            having sample MAF<=m1 will be included in analysis.
                            Default set to 0.01
      -q2 MAFLOWER, --maflower MAFLOWER
                            Minor allele frequency lower limit. All variants
                            having sample MAF>m2 will be included in analysis.
                            Default set to 0.0
      -p N, --permutations N
                            Number of permutations
      --adaptive C          Adaptive permutation using Edwin Wilson 95 percent
                            confidence interval for binomial distribution. The
                            program will compute a p-value every 1000 permutations
                            and compare the lower bound of the 95 percent CI of
                            p-value against "C", and quit permutations with the
                            p-value if it is larger than "C". It is recommended to
                            specify a "C" that is slightly larger than the
                            significance level for the study. To disable the
                            adaptive procedure, set C=1. Default is C=0.1
    



#### 2.2 Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status -m "aSum --name aSum -p 5000" --group_by name2 --to_db asum -j\
    8 > asum.txt

    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [=================================] 3,180 32.6/s in 00:01:37
    Testing for association: 100% [=========================================] 2,632/591 10.3/s in 00:04:14
    INFO: Association tests on 2632 groups have completed. 591 failed.
    INFO: Using annotation DB asum in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 16:32:32
    



    vtools show fields | grep asum
    
    asum.name2                   name2
    asum.sample_size_aSum        sample size
    asum.num_variants_aSum       number of variants in each group (adjusted for specified MAF
    asum.total_mac_aSum          total minor allele counts in a group (adjusted for MOI)
    asum.statistic_aSum          test statistic.
    asum.pvalue_aSum             p-value
    asum.std_error_aSum          Empirical estimate of the standard deviation of statistic
    asum.num_permutations_aSum   number of permutations at which p-value is evaluated
    



    head asum.txt
    
    name2	sample_size_aSum	num_variants_aSum	total_mac_aSum	statistic_aSum	pvalue_aSum	std_error_aSum	num_permutations_aSum
    AADACL4	3180	5	138	2.59057	0.32967	3.85368	1000
    ABCG5	3180	6	87	1.90472	0.335664	3.00098	1000
    ABCD3	3180	3	42	-0.873585	0.635365	2.17424	1000
    ABCB6	3180	7	151	-0.521698	0.632368	3.97958	1000
    ABHD1	3180	5	29	-0.365094	0.548452	1.81627	1000
    ABCG8	3180	12	152	-5.63774	0.95005	4.06417	1000
    ABL2	3180	4	41	0.242453	0.565435	1.98108	1000
    ACADL	3180	5	65	0.457547	0.58042	3.00258	1000
    ACAP3	3180	3	17	0.0273585	0.404595	1.26823	1000
    

<img src  = "asum.jpg" width = 500> 

</details>

## Reference

Fang Han and Wei Pan (2010) **A Data-Adaptive Sum Test for Disease Association with Multiple Common or Rare Variants**. *Human Heredity* doi:`10.1159/000288704`. <http://www.karger.com/doi/10.1159/000288704>

Andrew P. Morris and Eleftheria Zeggini (2010) **An evaluation of statistical approaches to rare variant analysis in genetic association studies**. *Genetic Epidemiology* doi:`10.1002/gepi.20450`. <http://doi.wiley.com/10.1002/gepi.20450> 