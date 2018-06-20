
+++
title = "weighted"
weight = 3
+++



## Weighted Burden Test for Disease and Quantitative Traits

### 1.1 Introduction

This implements a collection of **weighted** aggregation tests. Different from plain [aggregation methods][1] which assumes equal contribution of each locus from the genetic region under investigation, the weighted methods assigns a "weight" to each variant site such that each site differs from another by the weight they are assigned, and these weights will contribute to the aggregated "burden", e.g., $$X=\sum\_i^N\omega\_iX\_i$$ where $\omega\_i$ are the weights. The weights often reflect the relative importance of a variant in terms of its contribution to phenotype. 

The weighting approach was first proposed by (Madsen and Browning, 2010) with the assumption that "rarer" variants tend to be more important (the [WSS statistic][2]). This weighting theme is by far the most popular weights and has been adapted into a number of methods emerged later, such as (Lin and Tang, 2011) and (Wu et al, 2011). Other weighting themes such as KBAC and RBT weightings have different assumptions but they are also based solely on internal information from data. (Price et al, 2010) proposed the use of "external" weights, i.e., using functional annotation sources to calculate weight for rare variants. This weighting theme can also be naturally integrated into many rare variants methods. 

Implementation of `WeightedBurdenBt` and `WeightedBurdenQt` are similar to [aggregation methods][1] but allows the use of the following weighting themes: 



*   [WSS][2] weight, based on entire sample 
*   [WSS][2] weight, based on controls or sample with above/below average phenotype values 
*   [RBT][3] weight 
*   [KBAC][4] weight 
*   External weights from annotation 

Permutation methods have to be used to obtain $p$ value for WSS (control based), KBAC and RBT weighting themes. 



### 2. Details

#### 2.1 Command interface

    vtools show test WeightedBurdenBt
    
    Name:          WeightedBurdenBt
    Description:   Weighted genotype burden tests for disease traits, using one or many
                   arbitrary external weights as well as one of 4 internal
                   weighting themes
    usage: vtools associate --method WeightedBurdenBt [-h] [--name NAME]
                                                      [--mafupper MAFUPPER]
                                                      [--alternative TAILED]
                                                      [-p N] [--permute_by XY]
                                                      [--adaptive C]
                                                      [--extern_weight [EXTERN_WEIGHT [EXTERN_WEIGHT ...]]]
                                                      [--weight {Browning_all,Browning,KBAC,RBT}]
                                                      [--NA_adjust]
                                                      [--moi {additive,dominant,recessive}]
    
    Weighted genotype burden tests for disease traits, using one or many arbitrary
    external weights as well as one of 4 internal weighting themes. External
    weights (variant/genotype annotation field) are passed into the test by
    --var_info and --geno_info options. Internal weighting themes are one of
    "Browning_all", "Browning", "KBAC" or "RBT". p-value is based on logistic
    regression analysis and permutation procedure has to be used for "Browning",
    "KBAC" or "RBT" weights.
    
    optional arguments:
      -h, --help            show this help message and exit
      --name NAME           Name of the test that will be appended to names of
                            output fields, usually used to differentiate output of
                            different tests, or the same test with different
                            parameters.
      --mafupper MAFUPPER   Minor allele frequency upper limit. All variants
                            having sample MAF<=m1 will be included in analysis.
                            Default set to 0.01
      --alternative TAILED  Alternative hypothesis is one-sided ("1") or two-sided
                            ("2"). Default set to 1
      -p N, --permutations N
                            Number of permutations
      --permute_by XY       Permute phenotypes ("Y") or genotypes ("X"). Default
                            is "Y"
      --adaptive C          Adaptive permutation using Edwin Wilson 95 percent
                            confidence interval for binomial distribution. The
                            program will compute a p-value every 1000 permutations
                            and compare the lower bound of the 95 percent CI of
                            p-value against "C", and quit permutations with the
                            p-value if it is larger than "C". It is recommended to
                            specify a "C" that is slightly larger than the
                            significance level for the study. To disable the
                            adaptive procedure, set C=1. Default is C=0.1
      --extern_weight [EXTERN_WEIGHT [EXTERN_WEIGHT ...]]
                            External weights that will be directly applied to
                            genotype coding. Names of these weights should be in
                            one of '--var_info' or '--geno_info'. If multiple
                            weights are specified, they will be applied to
                            genotypes sequentially. Note that all weights will be
                            masked if --use_indicator is evoked.
      --weight {Browning_all,Browning,KBAC,RBT}
                            Internal weighting themes inspired by various
                            association methods. Valid choices are:
                            'Browning_all', 'Browning', 'KBAC' and 'RBT'. Default
                            set to 'Browning_all'. Except for 'Browning_all'
                            weighting, tests using all other weighting themes has
                            to calculate p-value via permutation. For details of
                            the weighting themes, please refer to the online
                            documentation.
      --NA_adjust           This option, if evoked, will replace missing genotype
                            values with a score relative to sample allele
                            frequencies. The association test will be adjusted to
                            incorporate the information. This is an effective
                            approach to control for type I error due to
                            differential degrees of missing genotypes among
                            samples.
      --moi {additive,dominant,recessive}
                            Mode of inheritance. Will code genotypes as 0/1/2/NA
                            for additive mode, 0/1/NA for dominant or recessive
                            model. Default set to additive
    

    vtools show test WeightedBurdenQt

    Name:          WeightedBurdenQt
    Description:   Weighted genotype burden tests for quantitative traits, using one or
                   many arbitrary external weights as well as one of 4
                   internal weighting themes
    usage: vtools associate --method WeightedBurdenQt [-h] [--name NAME]
                                                      [--mafupper MAFUPPER]
                                                      [--alternative TAILED]
                                                      [-p N] [--permute_by XY]
                                                      [--adaptive C]
                                                      [--extern_weight [EXTERN_WEIGHT [EXTERN_WEIGHT ...]]]
                                                      [--weight {Browning_all,Browning,KBAC,RBT}]
                                                      [--NA_adjust]
                                                      [--moi {additive,dominant,recessive}]
    
    Weighted genotype burden tests for quantitative traits, using one or many
    arbitrary external weights as well as one of 4 internal weighting themes.
    External weights (variant/genotype annotation field) are passed into the test
    by --var_info and --geno_info options. Internal weighting themes are one of
    "Browning_all", "Browning", "KBAC" or "RBT". p-value is based on linear
    regression analysis and permutation procedure has to be used for "Browning",
    "KBAC" or "RBT" weights.
    
    optional arguments:
      -h, --help            show this help message and exit
      --name NAME           Name of the test that will be appended to names of
                            output fields, usually used to differentiate output of
                            different tests, or the same test with different
                            parameters.
      --mafupper MAFUPPER   Minor allele frequency upper limit. All variants
                            having sample MAF<=m1 will be included in analysis.
                            Default set to 0.01
      --alternative TAILED  Alternative hypothesis is one-sided ("1") or two-sided
                            ("2"). Default set to 1
      -p N, --permutations N
                            Number of permutations
      --permute_by XY       Permute phenotypes ("Y") or genotypes ("X"). Default
                            is "Y"
      --adaptive C          Adaptive permutation using Edwin Wilson 95 percent
                            confidence interval for binomial distribution. The
                            program will compute a p-value every 1000 permutations
                            and compare the lower bound of the 95 percent CI of
                            p-value against "C", and quit permutations with the
                            p-value if it is larger than "C". It is recommended to
                            specify a "C" that is slightly larger than the
                            significance level for the study. To disable the
                            adaptive procedure, set C=1. Default is C=0.1
      --extern_weight [EXTERN_WEIGHT [EXTERN_WEIGHT ...]]
                            External weights that will be directly applied to
                            genotype coding. Names of these weights should be in
                            one of '--var_info' or '--geno_info'. If multiple
                            weights are specified, they will be applied to
                            genotypes sequentially. Note that all weights will be
                            masked if --use_indicator is evoked.
      --weight {Browning_all,Browning,KBAC,RBT}
                            Internal weighting themes inspired by various
                            association methods. Valid choices are:
                            'Browning_all', 'Browning', 'KBAC' and 'RBT'. Default
                            set to 'Browning_all'. Except for 'Browning_all'
                            weighting, tests using all other weighting themes has
                            to calculate p-value via permutation. For details of
                            the weighting themes, please refer to the online
                            documentation.
      --NA_adjust           This option, if evoked, will replace missing genotype
                            values with a score relative to sample allele
                            frequencies. The association test will be adjusted to
                            incorporate the information. This is an effective
                            approach to control for type I error due to
                            differential degrees of missing genotypes among
                            samples.
      --moi {additive,dominant,recessive}
                            Mode of inheritance. Will code genotypes as 0/1/2/NA
                            for additive mode, 0/1/NA for dominant or recessive
                            mode. Default set to additive
    



#### 2.2 Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status --covariates age gender bmi exposure -m "WeightedBurdenBt --na\
    me WeightedBurdenBt --alternative 2" --group_by name2 --to_db weightedburdenBt -j8 > weight\
    edburdenBt.txt

    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [===============================================] 3,180 23.6/s in 00:02:15
    Testing for association: 100% [=====================================================] 2,632/195 4.5/s in 00:09:48
    INFO: Association tests on 2632 groups have completed. 195 failed.
    INFO: Using annotation DB weightedburdenBt in project test.
    INFO: Annotation database used to record results of association tests. Created on Thu, 31 Jan 2013 21:36:29
    

    vtools show fields | grep weightedburdenBt

    weightedburdenBt.name2       name2
    weightedburdenBt.sample_size_WeightedBurdenBt sample size
    weightedburdenBt.num_variants_WeightedBurdenBt number of variants in each group (adjusted for specified MAF
    weightedburdenBt.total_mac_WeightedBurdenBt total minor allele counts in a group (adjusted for MOI)
    weightedburdenBt.beta_x_WeightedBurdenBt test statistic. In the context of regression this is estimate of
    weightedburdenBt.pvalue_WeightedBurdenBt p-value
    weightedburdenBt.wald_x_WeightedBurdenBt Wald statistic for x (beta_x/SE(beta_x))
    weightedburdenBt.beta_2_WeightedBurdenBt estimate of beta for covariate 2
    weightedburdenBt.beta_2_pvalue_WeightedBurdenBt p-value for covariate 2
    weightedburdenBt.wald_2_WeightedBurdenBt Wald statistic for covariate 2
    weightedburdenBt.beta_3_WeightedBurdenBt estimate of beta for covariate 3
    weightedburdenBt.beta_3_pvalue_WeightedBurdenBt p-value for covariate 3
    weightedburdenBt.wald_3_WeightedBurdenBt Wald statistic for covariate 3
    weightedburdenBt.beta_4_WeightedBurdenBt estimate of beta for covariate 4
    weightedburdenBt.beta_4_pvalue_WeightedBurdenBt p-value for covariate 4
    weightedburdenBt.wald_4_WeightedBurdenBt Wald statistic for covariate 4
    weightedburdenBt.beta_5_WeightedBurdenBt estimate of beta for covariate 5
    weightedburdenBt.beta_5_pvalue_WeightedBurdenBt p-value for covariate 5
    weightedburdenBt.wald_5_WeightedBurdenBt Wald statistic for covariate 5
    

    head weightedburdenBt.txt
    
    name2	sample_size_WeightedBurdenBt	num_variants_WeightedBurdenBt	total_mac_WeightedBurdenBt	beta_x_WeightedBurdenBt	pvalue_WeightedBurdenBt	wald_x_WeightedBurdenBt	beta_2_WeightedBurdenBt	beta_2_pvalue_WeightedBurdenBt	wald_2_WeightedBurdenBt	beta_3_WeightedBurdenBt	beta_3_pvalue_WeightedBurdenBt	wald_3_WeightedBurdenBt	beta_4_WeightedBurdenBt	beta_4_pvalue_WeightedBurdenBt	wald_4_WeightedBurdenBt	beta_5_WeightedBurdenBt	beta_5_pvalue_WeightedBurdenBt	wald_5_WeightedBurdenBt
    AAMP	3180	3	35	0.0449657	0.979459	0.0257468	0.0312612	4.39155E-09	5.86873	-0.298905	0.0146383	-2.44121	0.130226	1.2303E-40	13.3472	0.435497	0.00139398	3.19589
    AADACL4	3180	5	138	-2.46402	0.191324	-1.30667	0.0313048	4.31926E-09	5.87148	-0.294729	0.0160925	-2.40681	0.129824	2.23801E-40	13.3025	0.437296	0.00134129	3.207
    ABHD1	3180	5	29	-1.40549	0.502329	-0.67083	0.0312599	4.37216E-09	5.86946	-0.297393	0.0151487	-2.42881	0.13027	1.21612E-40	13.348	0.437962	0.00131275	3.21318
    ABCG8	3180	12	152	-0.597925	0.598611	-0.526399	0.0313146	4.24769E-09	5.87425	-0.297519	0.0151294	-2.42927	0.130098	1.44734E-40	13.3351	0.436695	0.00135537	3.20399
    ABI2	3180	1	25	4.90399	0.0422609	2.03094	0.0311325	4.9292E-09	5.84954	-0.30075	0.0140623	-2.45567	0.129821	1.95802E-40	13.3125	0.436794	0.00135518	3.20403
    ABCA12	3180	28	312	-0.387274	0.567616	-0.571566	0.0312492	4.47694E-09	5.86553	-0.298553	0.0147626	-2.43815	0.13023	1.19773E-40	13.3492	0.437199	0.00134108	3.20704
    ABCA4	3180	43	492	-0.0845646	0.866958	-0.167524	0.0312627	4.36946E-09	5.86956	-0.298887	0.0146353	-2.44128	0.130242	1.12648E-40	13.3537	0.435417	0.00139682	3.19531
    ABCB6	3180	7	151	-0.349842	0.782487	-0.276079	0.0313125	4.21645E-09	5.87547	-0.299545	0.0144307	-2.44636	0.130211	1.1897E-40	13.3497	0.435621	0.00138786	3.19716
    ABCD3	3180	3	42	-1.24687	0.595311	-0.531156	0.0312676	4.44499E-09	5.86672	-0.301058	0.0139996	-2.45727	0.130189	1.06821E-40	13.3577	0.436778	0.00135205	3.2047
    

**QQ-plot** 
<img src = "weightedburdenQt.jpg" width = 500>


    vtools associate rare bmi --covariates age gender exposure -m "WeightedBurdenQt --name Weig\
    htedBurdenQt --alternative 2" --group_by name2 --to_db weightedburdenQt -j8 > weightedburde\
    nQt.txt
    
    INFO: 3180 samples are found
    INFO: 2632 groups are found
    Loading genotypes: 100% [===============================] 3,180 24.4/s in 00:02:10
    Testing for association: 100% [===================================] 2,632/147 22.2/s in 00:01:58
    INFO: Association tests on 2632 groups have completed. 147 failed.
    INFO: Using annotation DB weightedburdenQt in project test.
    INFO: Annotation database used to record results of association tests. Created on Thu, 31 Jan 2013 21:51:44
    

    vtools show fields | grep weightedburdenQt
    
    weightedburdenQt.name2       name2
    weightedburdenQt.sample_size_WeightedBurdenQt sample size
    weightedburdenQt.num_variants_WeightedBurdenQt number of variants in each group (adjusted for specified MAF
    weightedburdenQt.total_mac_WeightedBurdenQt total minor allele counts in a group (adjusted for MOI)
    weightedburdenQt.beta_x_WeightedBurdenQt test statistic. In the context of regression this is estimate of
    weightedburdenQt.pvalue_WeightedBurdenQt p-value
    weightedburdenQt.wald_x_WeightedBurdenQt Wald statistic for x (beta_x/SE(beta_x))
    weightedburdenQt.beta_2_WeightedBurdenQt estimate of beta for covariate 2
    weightedburdenQt.beta_2_pvalue_WeightedBurdenQt p-value for covariate 2
    weightedburdenQt.wald_2_WeightedBurdenQt Wald statistic for covariate 2
    weightedburdenQt.beta_3_WeightedBurdenQt estimate of beta for covariate 3
    weightedburdenQt.beta_3_pvalue_WeightedBurdenQt p-value for covariate 3
    weightedburdenQt.wald_3_WeightedBurdenQt Wald statistic for covariate 3
    weightedburdenQt.beta_4_WeightedBurdenQt estimate of beta for covariate 4
    weightedburdenQt.beta_4_pvalue_WeightedBurdenQt p-value for covariate 4
    weightedburdenQt.wald_4_WeightedBurdenQt Wald statistic for covariate 4
    

    head weightedburdenQt.txt

    name2	sample_size_WeightedBurdenQt	num_variants_WeightedBurdenQt	total_mac_WeightedBurdenQt	beta_x_WeightedBurdenQt	pvalue_WeightedBurdenQt	wald_x_WeightedBurdenQt	beta_2_WeightedBurdenQt	beta_2_pvalue_WeightedBurdenQt	wald_2_WeightedBurdenQt	beta_3_WeightedBurdenQt	beta_3_pvalue_WeightedBurdenQt	wald_3_WeightedBurdenQt	beta_4_WeightedBurdenQt	beta_4_pvalue_WeightedBurdenQt	wald_4_WeightedBurdenQt
    AADACL4	3180	5	138	-3.3906	0.159775	-1.40616	0.0150701	0.0575284	1.89996	-0.0698905	0.733286	-0.340787	-0.940103	2.72704E-05	-4.20129
    AAMP	3180	3	35	5.33715	0.0927374	1.68164	0.0148223	0.0617461	1.86878	-0.0767246	0.708183	-0.374331	-0.939547	2.75008E-05	-4.19938
    ABCB10	3180	6	122	0.652166	0.773271	0.288123	0.0150189	0.0584545	1.89296	-0.0795645	0.698049	-0.38799	-0.945327	2.49634E-05	-4.22137
    ABCB6	3180	7	151	-0.938172	0.653007	-0.449631	0.0151034	0.0571025	1.90322	-0.0803477	0.695236	-0.391795	-0.943322	2.57074E-05	-4.21471
    ABCG5	3180	6	87	-3.04695	0.171201	-1.36867	0.0147558	0.0630148	1.85974	-0.0732971	0.720746	-0.357493	-0.953839	2.10114E-05	-4.26027
    ABHD1	3180	5	29	-1.47831	0.509375	-0.659886	0.0150935	0.05722	1.90232	-0.0777012	0.704752	-0.378948	-0.940358	2.73267E-05	-4.20082
    ABCG8	3180	12	152	-2.29054	0.152981	-1.42942	0.0151166	0.0567651	1.90581	-0.0738058	0.71887	-0.360001	-0.940705	2.69354E-05	-4.2041
    ABI2	3180	1	25	5.96983	0.276415	1.0886	0.0150043	0.0586562	1.89144	-0.081478	0.691101	-0.397397	-0.941765	2.64399E-05	-4.20833
    ABL2	3180	4	41	-1.52705	0.578314	-0.555906	0.0150917	0.057261	1.902	-0.0773202	0.706151	-0.377064	-0.943905	2.54124E-05	-4.21733
    
**QQ-plot** 
<img src = "weightedburdenQt.jpg" width = 500>

</details>


### Reference 

Bo Eskerod Madsen and Sharon R. Browning (2009) **A Groupwise Association Test for Rare Mutations Using a Weighted Sum Statistic**. *PLoS Genetics* doi:`10.1371/journal.pgen.1000384`. <http://dx.plos.org/10.1371/journal.pgen.1000384>

Bo Eskerod Madsen and Sharon R. Browning (2009) **A Groupwise Association Test for Rare Mutations Using a Weighted Sum Statistic**. *PLoS Genetics* doi:`10.1371/journal.pgen.1000384`. <http://dx.plos.org/10.1371/journal.pgen.1000384> 

MichaelC. Wu, Seunggeun Lee, Tianxi Cai, Yun Li, Michael Boehnke and Xihong Lin (2011) **Rare-Variant Association Testing for Sequencing Data with the Sequence Kernel Association Test**. *The American Journal of Human Genetics* doi:`10.1016/j.ajhg.2011.05.029`. <http://linkinghub.elsevier.com/retrieve/pii/S0002929711002229>

Alkes L. Price, Gregory V. Kryukov, Paul I.W. de Bakker, Shaun M. Purcell, Jeff Staples, Lee-Jen Wei and Shamil R. Sunyaev (2010) **Pooled Association Tests for Rare Variants in Exon-Resequencing Studies**. *The American Journal of Human Genetics* doi:`10.1016/j.ajhg.2010.04.005`. <http://linkinghub.elsevier.com/retrieve/pii/S0002929710002077>


 [1]:   /applications/association/joint_conditional/aggre/
 [2]:   /applications/association/single_gene/wss-test/
 [3]:   /applications/association/single_gene/rbt-test/
 [4]:   /applications/association/single_gene/kbac-test/