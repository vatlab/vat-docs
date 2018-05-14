
+++
title = "CMC test"
description = ""
weight = 2
+++



# Combined and Multivariate Collapsing Method for Rare Variants 




## Introduction

This is the Combined and Multivariate Collapsing (CMC, Li and Leal, 2008[^Bingshan Li and Suzanne M. Leal (2008) **Methods for Detecting Associations with Rare Variants for Common Diseases: Application to Analysis of Sequence Data**. *The American Journal of Human Genetics* doi:`10.1016/j.ajhg.2008.06.024`. <http://linkinghub.elsevier.com/retrieve/pii/S0002929708004084>^]) test for rare variants. CMC method considers all variants in a test unit (e.g., a gene). It "collapses" all rare variants in the gene region such that the region is coded "0" if all loci are wildtype, and "1" if any one locus has a minor allele. Then it "combines" this coding with the rest of common variants in the gene region into a multivariate problem that tests for the null hypothesis that the gene region is not associated with a disease or quantitative trait. The statistic for CMC method can be {$\chi^2$} test for collapsed rare variants, Hotelling's {$T^2$} or multivariate regression analysis for joint analysis of common and rare variants. This program implements CMC method for rare variants with Fisher's exact test for evaluating association between rare variants and disease phenotypes (case/ctrl data). The use of Fisher's test results in exact p-value, avoiding the computationally intensive permutation procedure. 

This test only works for case control data without covariates. Please refer to `CollapseBt` and `CollapseQt` for case control and quantitative traits using the collapsing theme under regression framework that incorporates covariates. 



## Details

### Command interface

    vtools show test CFisher
    



    Name:          CFisher
    Description:   Fisher's exact test on collapsed variant loci, Li & Leal 2008
    usage: vtools associate --method CFisher [-h] [--name NAME] [-q1 MAFUPPER]
                                             [-q2 MAFLOWER] [--alternative TAILED]
                                             [--midp]
                                             [--moi {additive,dominant,recessive}]
    
    Collapsing test for case-control data (CMC test, Li & Leal 2008). Different
    from the original publication which jointly test for common/rare variants
    using Hotelling's t^2 method, this version of CMC will binaries rare variants
    (default frequency set to 0.01) within a group defined by "--group_by" and
    calculate p-value via Fisher's exact test. A "mid-p" option is available for
    one-sided test to obtain a less conservative p-value estimate.
    
    optional arguments:
      -h, --help            show this help message and exit
      --name NAME           Name of the test that will be appended to names of
                            output fields, usually used to differentiate output of
                            different tests, or the same test with different
                            parameters. Default set to "CFisher"
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
      --midp                This option, if evoked, will use mid-p value
                            correction for one-sided Fisher's exact test.
      --moi {additive,dominant,recessive}
                            Mode of inheritance. Will code genotypes as 0/1/2/NA
                            for additive mode, 0/1/NA for dominant or recessive
                            model. Default set to additive
    



### Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status -m "CFisher --name Fisher --alternative 2" --group_by name2 --\
    to_db cfisher -j8 > cfisher.txt
    



    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [======================================] 3,180 32.9/s in 00:01:36
    Testing for association: 100% [====================================] 2,632/147 26.5/s in 00:01:39
    INFO: Association tests on 2632 groups have completed. 147 failed.
    INFO: Using annotation DB cfisher in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 22:06:07
    



    vtools show fields | grep cfisher
    



    cfisher.name2                name2
    cfisher.sample_size_Fisher   sample size
    cfisher.num_variants_Fisher  number of variants in each group (adjusted for specified MAF
    cfisher.total_mac_Fisher     total minor allele counts in a group (adjusted for MOI)
    cfisher.statistic_Fisher     test statistic.
    cfisher.pvalue_Fisher        p-value
    



    head cfisher.txt
    



    name2	sample_size_Fisher	num_variants_Fisher	total_mac_Fisher	statistic_Fisher	pvalue_Fisher
    AAMP	3180	3	35	1.27335	0.593442
    ABCD3	3180	3	42	0.821622	1
    ABCB10	3180	6	122	1.33481	0.250852
    ABCB6	3180	7	151	0.91265	0.895567
    ABHD1	3180	5	29	0.913443	1
    ABCG8	3180	12	152	0.641297	0.15483
    ABCA12	3180	28	312	0.979172	1
    ABI2	3180	1	25	3.00046	0.020062
    ACADM	3180	4	103	0.477756	0.0807384
    

**QQ-plot**  Attach:cfisher.jpg 

</details>



### Using Mid-P values for exact test

This collapsing test for rare variant is based on an exact test which guarantees to control for type I error yet may be overly conservative. Mid-P values are a reasonable compromise between the conservativeness of the ordinary exact test and the uncertain adequacy of large-sample methods. `--midp` switch gives Mid-P values for one-sided exact test 

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status -m "CFisher --name FisherMidP --alternative 1 --midp" --group_\
    by name2 --to_db cfisher -j8 > cfisher-midp.txt
    



    INFO: 3180 samples are found
    INFO: 2632 groups are found
    Loading genotypes: 100% [==========================] 3,180 33.3/s in 00:01:35
    Testing for association: 100% [================================] 2,632/147 25.9/s in 00:01:41
    INFO: Association tests on 2632 groups have completed. 147 failed.
    INFO: Using annotation DB cfisher in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 22:14:57
    



    vtools show fields | grep cfisher
    



    cfisher.name2                name2
    cfisher.sample_size_FisherMidP sample size
    cfisher.num_variants_FisherMidP number of variants in each group (adjusted for specified MAF
    cfisher.total_mac_FisherMidP total minor allele counts in a group (adjusted for MOI)
    cfisher.statistic_FisherMidP test statistic.
    cfisher.pvalue_FisherMidP    p-value
    



    head cfisher-midp.txt
    



    name2	sample_size_FisherMidP	num_variants_FisherMidP	total_mac_FisherMidP	statistic_FisherMidP	pvalue_FisherMidP
    AAMP	3180	3	35	1.27335	0.298742
    ABCB6	3180	7	151	0.91265	0.620991
    ABCG5	3180	6	87	1.26073	0.228907
    ABHD1	3180	5	29	0.913443	0.529454
    ABI2	3180	1	25	3.00046	0.0127947
    ABL2	3180	4	41	1.05884	0.431808
    ABCG8	3180	12	152	0.641297	0.932016
    ABCA4	3180	43	492	1.01841	0.448273
    ABCA12	3180	28	312	0.979172	0.535912
    

**QQ-plot**  Attach:cfisher-midp.jpg </details>

[^#^]