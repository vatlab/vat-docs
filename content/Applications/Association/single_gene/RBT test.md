
+++
title = "RBT test"
weight = 4
+++



## Replication Based Test for Protective Variants 



### 1. Introduction

This is implementation for the replication base test in (Ionita-Laza et al 2011). The key of this method is *replication*, i.e., in the two-sided test of RBT it computes evidences to reject each of the two hypothesis 



*   Deleterious rare variants are enriched in cases 
*   Protective rare variants are enriched in controls 

The final statistic is based on the stronger of the two evidences, adjusted for multiple testing. To increase the power of this approach a weighting theme is applied to variant counts in case or control group using a transformation of the probability of observing such counts under a Poisson model. 

Implementation of RBT in this program has both one-sided and two-sided versions via the `--alternative` parameter. The one-sided testing strategy tests for the presence of variants conferring risk to disease by focusing on variants that have higher observed frequency in cases compared with controls. Permutation procedure is used in both one-sided and two-sided tests to obtain valid $p$ value. 



### 2. Details

#### 2.1 Command interface

    vtools show test RBT

    Name:          RBT
    Description:   Replication Based Test for protective and deleterious variants,
                   Ionita-Laza et al 2011
    usage: vtools associate --method RBT [-h] [--name NAME] [-q1 MAFUPPER]
                                         [-q2 MAFLOWER] [--alternative TAILED]
                                         [-p N] [--adaptive C]
                                         [--moi {additive,dominant,recessive}]
    
    Replication Based Test for protective and deleterious variants, Ionita-Laza et
    al 2011. Variant sites are scored based on -log transformation of probability
    of having more than observed variants in cases/ctrls; the RBT statistic is
    defined as sum of the variant sites scores. One-sided RBT is implemented in
    addition to the two-sided statistic described in the RBT paper. p-value is
    estimated via permutation test.
    
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
      --alternative TAILED  Alternative hypothesis is one-sided ("1") or two-sided
                            ("2"). Default set to 1
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
      --moi {additive,dominant,recessive}
                            Mode of inheritance. Will code genotypes as 0/1/2/NA
                            for additive mode, 0/1/NA for dominant or recessive
                            model. Default set to additive
    



#### 2.2 Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status -m "RBT --name RBT -p 5000" --group_by name2 --to_db rbt -j8 >\
     rbt.txt

    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [===========================] 3,180 34.0/s in 00:01:33
    Testing for association: 100% [===================================] 2,632/591 14.3/s in 00:03:03
    INFO: Association tests on 2632 groups have completed. 591 failed.
    INFO: Using annotation DB rbt in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 05:32:45
    



    vtools show fields | grep RBT

    rbt.sample_size_RBT          sample size
    rbt.num_variants_RBT         number of variants in each group (adjusted for specified MAF
    rbt.total_mac_RBT            total minor allele counts in a group (adjusted for MOI)
    rbt.statistic_RBT            test statistic.
    rbt.pvalue_RBT               p-value
    rbt.std_error_RBT            Empirical estimate of the standard deviation of statistic
    rbt.num_permutations_RBT     number of permutations at which p-value is evaluated
    



    head rbt.txt
    
    name2   sample_size_RBT num_variants_RBT        total_mac_RBT   statistic_RBT   pvalue_RBT      std_error_RBT   num_permutations_RBT
    AADACL4 3180    5       138     1.37261 0.898102        2.99763 1000
    ABCB6   3180    7       151     4.94419 0.665335        3.29949 1000
    ABCG5   3180    6       87      5.1935  0.413586        2.98032 1000
    ABCG8   3180    12      152     4.96566 0.769231        4.03695 1000
    ABL2    3180    4       41      2.67589 0.456543        2.29237 1000
    ACADL   3180    5       65      2.18841 0.696304        2.64459 1000
    ACADM   3180    4       103     2.04935 0.678322        2.58183 1000
    ACAP3   3180    3       17      2.32431 0.422577        1.95933 1000
    ABCD3   3180    3       42      1.10394 0.797203        2.16152 1000
    

</details>


### Reference
Iuliana Ionita-Laza, Joseph D. Buxbaum, Nan M. Laird and Christoph Lange (2011) **A New Testing Strategy to Identify Rare Variants with Either Risk or Protective Effect on Disease**. *PLoS Genetics* doi:`10.1371/journal.pgen.1001289`. <http://dx.plos.org/10.1371/journal.pgen.1001289>