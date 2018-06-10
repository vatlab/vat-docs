
+++
title = "C-alpha test"
weight = 2
+++




## C-alpha Test for Protective Variants 


### 1. Introduction

This implements the {$C(\alpha)$} test (Neale et al 2011) for disease traits, to test for the hypothesis of rare variants disease association under the particular assumption that rare variants observed in cases and controls is a mixture of phenotypically deleterious, protective and neutral variants. Instead of using a cumulative dosage (or "burden") based summary statistic over a gene region, it directly contrasts the observed and expected distribution of minor alleles in cases and controls at each locus as an evidence of "unusual distribution", and combine evidences from multiple loci (whether it be an evidence of protective or deleterious) to formulate the 
\\(C(\alpha)\\) statistic:

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
$$T=\sum\_{i=1}^m[(y\_i-n\_ip\_0)^2-n\_ip\_0(1-p_0)]$$


The original paper evaluates p-value of the test under large sample normal assumption, which usually would not hold for the real world data. Implementation in this program also allows permutation based {$C(\alpha)$} test, if parameter `-p/--permutations` is set greater than 0. 



### 2. Details

#### 2.1 Command interface

    vtools show test Calpha

    Name:          Calpha
    Description:   c-alpha test for unusual distribution of variants between cases and
                   controls, Neale et al 2011
    usage: vtools associate --method Calpha [-h] [--name NAME] [-q1 MAFUPPER]
                                            [-q2 MAFLOWER] [-p N] [--adaptive C]
                                            [--moi {additive,dominant,recessive}]
    
    c-alpha test for unusual distribution of variants between cases and controls,
    Neale et al 2011. It tests for deviation of variance of minor allele counts in
    cases/ctrls from its exception based on binomial distribution. The statistic
    is asymptotically normally distributed. p-value can be evaluated using either
    permutation or asymptotic distribution as described in Neale et al 2011,
    although it is recommended to use permutation to estimate a reliable p-value.
    Calpha test is a two-tailed test
    
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



    vtools associate rare status -m "Calpha --name Calpha -p 5000" --group_by name2 --to_db cal\
    pha -j8 > calpha.txt
    
    INFO: 3180 samples are found
    INFO: 2632 groups are found
    Loading genotypes: 100% [=====================] 3,180 27.6/s in 00:01:55
    Testing for association: 100% [=====================] 2,632/591 11.6/s in 00:03:46
    INFO: Association tests on 2632 groups have completed. 591 failed.
    INFO: Using annotation DB calpha in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 15:54:03
    



    vtools show fields | grep calpha

    calpha.refGene_name2         refGene_name2
    calpha.sample_size_Calpha    sample size
    calpha.num_variants_Calpha   number of variants in each group (adjusted for specified MAF
    calpha.total_mac_Calpha      total minor allele counts in a group (adjusted for MOI)
    calpha.statistic_Calpha      test statistic.
    calpha.pvalue_Calpha         p-value
    



    head calpha.txt
    
    name2	sample_size_Calpha	num_variants_Calpha	total_mac_Calpha	statistic_Calpha	pvalue_Calpha	std_error_Calpha	num_permutations_Calpha
    AADACL4	3180	5	138	0.0229344	0.407592	1.08434	1000
    AAMP	3180	3	35	-0.444631	0.601399	0.896954	1000
    ABCD3	3180	3	42	-0.911816	0.93007	1.0528	1000
    ABCB6	3180	7	151	-0.751779	0.757243	1.05563	1000
    ABCG8	3180	12	152	-0.0149743	0.36963	0.981793	1000
    ABHD1	3180	5	29	-0.744439	0.845155	1.0768	1000
    ABCB10	3180	6	122	1.14261	0.12094	1.02364	2000
    ABL2	3180	4	41	-0.76715	0.966034	0.866904	1000
    ACADL	3180	5	65	-0.50523	0.642358	0.943209	1000
    

</details>

### Reference

Benjamin M. Neale, Manuel A. Rivas, Benjamin F. Voight, David Altshuler, Bernie Devlin, Marju Orho-Melander, Sekar Kathiresan, Shaun M. Purcell, Kathryn Roeder and Mark J. Daly (2011) **Testing for an Unusual Distribution of Rare Variants**. *PLoS Genetics* doi:`10.1371/journal.pgen.1001322`. <http://dx.plos.org/10.1371/journal.pgen.1001322>