
+++
title = "WSS test"
weight = 7
+++



## Weighted Sum Statistic via Rank Test 



### 1. Introduction

The method proposed by Madsen and Browning 2009 first introduced the idea of assigning "weights" to rare variants within a genetic region before they are collapsed. In this case the variants having higher weights will have more substantial contribution to the collapsed variant score. In the Madsen & Browning paper the "weights" are defined as <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script> \\(\sqrt{n\_iq\_i(1-q\_i)}\\) with the assumption that the "rarer" the variant, the larger the risk effect it is to a phenotype. The \\(q\_i\\) in the original paper was based on observed control sample, which might result in inflated type I error(Mathieu Lemire, 2011). Implementation of the WSS statistic in the `WSSRankTest` method uses the same definition for \\(q\_i\\) but the Mann-Whitney U test ([definition and C++ implementation for this program][1]) now relies on a full permutation procedure rather than normal approximation, such that the bias is correctly accounted for. 

As with the [Varible Thresholds strategy][2], the idea of weighting can be applied to many other rare variant methods. The `WeightedBurdenBt` and `WeightedBurdenQt` methods implements the Madsen & Browning weighting based on controls (or samples with low quantitative phenotypic values) or the entire population, and tests for association for both case control and quantitative traits with/without presence of phenotype co-variates. 



### 2. Details

#### 2.1 Command interface

    vtools show test WSSRankTest

    Name:          WSSRankTest
    Description:   Weighted sum method using rank test statistic, Madsen & Browning 2009
    usage: vtools associate --method WSSRankTest [-h] [--name NAME] [-q1 MAFUPPER]
                                                 [-q2 MAFLOWER]
                                                 [--alternative TAILED] [-p N]
                                                 [--adaptive C]
                                                 [--moi {additive,dominant,recessive}]
    
    Weighted sum method using rank test statistic, Madsen & Browning 2009. p-value
    is based on the significance level of the Wilcoxon rank-sum test. Two methods
    are available for evaluating p-value: a semi-asymptotic p-value based on
    normal distribution, or permutation based p-value. Variants will be weighted
    by 1/sqrt(nP*(1-P)) and the weighted codings will be summed up for rank test.
    Two-sided test is available for the asymptotic version, which will calculate
    two p-values based on weights from controls and cases respectively, and use
    the smaller of them with multiple testing adjustment. For two-sided
    permutation based p-value please refer to "vtools show test WeightedBurdenBt"
    
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
                            ("2"). Note that two-sided test is only available for
                            asymptotic version of the test. Default set to 1
      -p N, --permutations N
                            Number of permutations. Set it to zero to use the
                            asymptotic version. Default is zero
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



    % vtools associate rare status -m "WSSRankTest --name wss -p 5000" --group_by name2 --to_db w\
    ss -j8 > wss.txt

    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [=========================================] 3,180 33.7/s in 00:01:34
    Testing for association: 100% [================================================] 2,632/591 10.7/s in 00:04:06
    INFO: Association tests on 2632 groups have completed. 591 failed.
    INFO: Using annotation DB wss in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 16:18:43
    



    % vtools show fields | grep wss

    wss.name2                    name2
    wss.sample_size_wss          sample size
    wss.num_variants_wss         number of variants in each group (adjusted for specified MAF
    wss.total_mac_wss            total minor allele counts in a group (adjusted for MOI)
    wss.statistic_wss            test statistic.
    wss.pvalue_wss               p-value
    wss.std_error_wss            Empirical estimate of the standard deviation of statistic
    wss.num_permutations_wss     number of permutations at which p-value is evaluated
    



    % head wss.txt
    
    name2	sample_size_wss	num_variants_wss	total_mac_wss	statistic_wss	pvalue_wss	std_error_wss	num_permutations_wss
    AADACL4	3180	5	138	34206	0.911089	11215.6	1000
    ABCD3	3180	3	42	12967	0.63037	6602.73	1000
    ABCG5	3180	6	87	37794	0.248751	8912.03	1000
    AAMP	3180	3	35	16160	0.290709	5777.64	1000
    ABCB10	3180	6	122	56091	0.145854	10409.2	1000
    ABHD1	3180	5	29	9825	0.605395	5363.56	1000
    ABCB6	3180	7	151	49949	0.608392	11831.6	1000
    ABL2	3180	4	41	16097	0.438561	6499.52	1000
    ACADM	3180	4	103	19070	0.967033	9782.51	1000
    

</details>

### Reference

Bo Eskerod Madsen and Sharon R. Browning (2009) **A Groupwise Association Test for Rare Mutations Using a Weighted Sum Statistic**. *PLoS Genetics* doi:`10.1371/journal.pgen.1000384`. <http://dx.plos.org/10.1371/journal.pgen.1000384>

Mathieu Lemire (2011) **Defining rare variants by their frequencies in controls may increase type I error**. *Nature Genetics* doi:`10.1038/ng.818`. <http://www.nature.com/doifinder/10.1038/ng.818>


 [1]: http://www.alglib.net/hypothesistesting/mannwhitneyu.php
 [2]:   /applications/association/single_gene/vt-test/