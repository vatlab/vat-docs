
+++
title = "RareCover test"
weight = 5
+++



## A "Covering Algorithm" for Rare and Low Frequency Variants  



### 1. Introduction

The RareCover test in (Bhatia et al 2010) is an efficient heuristic greedy algorithm to find an optimized combination of variants in a loci with the strongest association signal. It uses the same collapsing strategy and test statistic as in (Li and Leal, 2008) but scans over the loci, adding at each iteration the variants that contributes most to the statistic. 

RareCover is related to the [Variable Thresholds test][1] yet differs in the sequence by which rare variants are incorporated into the test. Variable thresholds test assumes a fixed yet unknown MAF boundary of rare causal variants, while RareCover does not have the assumption. Still, it does not mean that RareCover would perform exhaustive search for all combinations of variants in a loci region. The "coverage" of RareCover method depends on the convergence cut-off {$Q$}. 

RareCover method is implemented in this program as a two-sided test with the tuning parameter {$Q=0.5$}, as recommanded by the original paper. 



### 2. Details

#### 2.1 Command interface

    vtools show test RareCover
    



    Name:          RareCover
    Description:   A "covering" method for detecting rare variants association, Bhatia et
                   al 2010.
    usage: vtools associate --method RareCover [-h] [--name NAME] [-q1 MAFUPPER]
                                               [-q2 MAFLOWER] [-p N]
                                               [--adaptive C]
                                               [--moi {additive,dominant,recessive}]
    
    A "covering" method for detecting rare variants association, Bhatia et al
    2010. The algorithm combines a disparate collection of rare variants and
    maximize the association signal over the collection using a heuristic adaptive
    approach, which can be computationally intensive. Different from VT method, it
    does not require rare variants evaluated being adjacent in minor allele
    frequency ranking. RareCover test is a two-tailed test.
    
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
      --moi {additive,dominant,recessive}
                            Mode of inheritance. Will code genotypes as 0/1/2/NA
                            for additive mode, 0/1/NA for dominant or recessive
                            model. Default set to additive
    



#### 2.2 Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status -m "RareCover --name RareCover -p 5000" --group_by name2 --to_\
    db rarecover -j8 > rarecover.txt
    



    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [=============================] 3,180 32.8/s in 00:01:36
    Testing for association: 100% [===============================] 2,632/591 6.0/s in 00:07:17
    INFO: Association tests on 2632 groups have completed. 591 failed.
    INFO: Using annotation DB rarecover in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 05:40:44
    



    vtools show fields | grep RareCover
    



    rarecover.sample_size_RareCover sample size
    rarecover.num_variants_RareCover number of variants in each group (adjusted for specified MAF
    rarecover.total_mac_RareCover total minor allele counts in a group (adjusted for MOI)
    rarecover.statistic_RareCover test statistic.
    rarecover.pvalue_RareCover   p-value
    rarecover.std_error_RareCover Empirical estimate of the standard deviation of statistic under the
    rarecover.num_permutations_RareCover number of permutations at which p-value is evaluated
    



    head rarecover.txt
    



    name2   sample_size_RareCover   num_variants_RareCover  total_mac_RareCover     statistic_RareCover     pvalue_RareCover        std_error_RareCover     num_permutations_RareCover
    ABCG5   3180    6       87      0.991364        0.911089        3.32099 1000
    ABCB10  3180    6       122     5.54768 0.28971 3.25502 1000
    ABHD1   3180    5       29      0.262705        0.901099        3.76918 1000
    AAMP    3180    3       35      1.3233  0.667333        2.09356 1000
    ABCD3   3180    3       42      0.394182        0.949051        2.33258 1000
    AADACL4 3180    5       138     4.82996 0.200799        2.82611 1000
    ABCB6   3180    7       151     1.26936 0.895105        3.0108  1000
    ABL2    3180    4       41      0.344182        0.947053        3.3311  1000
    ACAP3   3180    3       17      2.87639 0.277722        2.90011 1000
    

<img src = "rarecover.jpg" width = 50> 

</details>

### Reference

Gaurav Bhatia, Vikas Bansal, Olivier Harismendy, Nicholas J. Schork, Eric J. Topol, Kelly Frazer and Vineet Bafna (2010) **A Covering Method for Detecting Genetic Associations between Rare Variants and Common Phenotypes**. *PLoS Computational Biology* doi:`10.1371/journal.pcbi.1000954`. <http://dx.plos.org/10.1371/journal.pcbi.1000954> 

Bingshan Li and Suzanne M. Leal (2008) **Methods for Detecting Associations with Rare Variants for Common Diseases: Application to Analysis of Sequence Data**. *The American Journal of Human Genetics* doi:`10.1016/j.ajhg.2008.06.024`. <http://linkinghub.elsevier.com/retrieve/pii/S0002929708004084> 

 [1]: /vat-docs/applications/association/single_gene/vt-test/