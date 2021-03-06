+++
title = "KBAC test"
weight = 3
+++



## Kernel Based Adaptive Clustering Method 



### 1. Introduction

This is implementation for the KBAC statistic in (Liu and Leal 2010). It carries out case-control association testing for rare variants for whole exome association studies. Briefly, consider a gene of length n which harbors m rare variants. Genotype on the m variant sites & the disease status (case/control) are known for each individual. The program takes as input the m-site genotype and disease status (case/control) data files, and computes a p-value indicating the significance of association. Permutation has to be used to obtain valid p-values. 

[An R package][1] is also available for use with standalone text dataset. 

Note a couple of differences between this implementation and the original version: 



*   The original paper provides 3 kernel options: hypergeometric, binomial and Gaussian kernels. The hypergeometric kernel generally performs best and is implemented. Other kernels are not implemented. 
*   The `--alternative 2` option implements the spirit of the RBT test (Ionita-Laza et al, 2011) by performing two KBAC tests under both *protective* and *deleterious* assumptions and use the larger of the two statistics thus calculated as the final KBAC statistic. 



### 2. Details

#### 2.1 Command interface

    vtools show test KBAC
    
    Name:          KBAC
    Description:   Kernel Based Adaptive Clustering method, Liu & Leal 2010
    usage: vtools associate --method KBAC [-h] [--name NAME] [-q1 MAFUPPER]
                                          [-q2 MAFLOWER] [--alternative TAILED]
                                          [-p N] [--adaptive C]
                                          [--moi {additive,dominant,recessive}]
    
    Kernel Based Adaptive Clustering method, Liu & Leal 2010. Genotype pattern
    frequencies, weighted by a hypergeometric density kernel function, is compared
    for differences between cases and controls. p-value is calculated using
    permutation for consistent estimate with different sample sizes (the
    approximation method of the original publication is not implemented). Two-
    sided KBAC test is implemented by calculating a second statistic with
    case/ctrl label swapped, and the larger of the two statistic is used as two-
    sided test statistic
    
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



    vtools associate rare status -m "KBAC --name kbac -p 5000" --group_by refGene.name2 --to_db\
     kbac -j8 > kbac.txt
    
    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [=====================] 3,180 34.4/s in 00:01:32
    Testing for association: 100% [=====================] 2,632/591 18.9/s in 00:02:19
    INFO: Association tests on 2632 groups have completed. 591 failed.
    INFO: Using annotation DB kbac in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 05:26:43
    

    vtools show fields | grep kbac

    kbac.refGene_name2           refGene_name2
    kbac.sample_size_kbac        sample size
    kbac.num_variants_kbac       number of variants in each group (adjusted for specified MAF
    kbac.total_mac_kbac          total minor allele counts in a group (adjusted for MOI)
    kbac.statistic_kbac          test statistic.
    kbac.pvalue_kbac             p-value
    kbac.std_error_kbac          Empirical estimate of the standard deviation of statistic
    kbac.num_permutations_kbac   number of permutations at which p-value is evaluated
    
    
    head kbac.txt

    refGene_name2   sample_size_kbac        num_variants_kbac       total_mac_kbac  statistic_kbac  pvalue_kbac     std_error_kbac  num_permutations_kbac
    ABCG5   3180    6       87      0.00610092      0.353646        0.00629806      1000
    ABCB6   3180    7       151     0.00375831      0.633367        0.00807416      1000
    ABCB10  3180    6       122     0.0157014       0.0973805       0.00733189      5000
    ABCG8   3180    12      152     -0.00160383     0.876124        0.00861691      1000
    ABCA4   3180    43      492     0.0293608       0.387612        0.0142427       1000
    ABHD1   3180    5       29      -0.000709548    0.732268        0.00400521      1000
    ABCA12  3180    28      312     0.015846        0.509491        0.011858        1000
    ABL2    3180    4       41      0.000628395     0.553447        0.00456862      1000
    ACADL   3180    5       65      0.00239811      0.501499        0.00545028      1000
    

</details>

### Reference
 
 Dajiang J. Liu and Suzanne M. Leal (2010) **A Novel Adaptive Method for the Analysis of Next-Generation Sequencing Data to Detect Complex Trait Associations with Rare Variants Due to Gene Main Effects and Interactions**. *PLoS Genetics* doi:`10.1371/journal.pgen.1001156`. <http://dx.plos.org/10.1371/journal.pgen.1001156>
 
 Iuliana Ionita-Laza, Joseph D. Buxbaum, Nan M. Laird and Christoph Lange (2011) **A New Testing Strategy to Identify Rare Variants with Either Risk or Protective Effect on Disease**. *PLoS Genetics* doi:`10.1371/journal.pgen.1001289`. <http://dx.plos.org/10.1371/journal.pgen.1001289>
 
  [1]: http://code.google.com/p/kbac-statistic-implementation/