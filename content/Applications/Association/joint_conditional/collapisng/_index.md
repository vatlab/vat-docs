
+++
title = "collapsing"
weight = 1
+++



## Collapsing Methods for Disease and Quantitative Traits 


### 1. Introduction

This is implementation of the fixed threshold collapsing methods for both disease and quantitative traits. *Collapsing* method for rare variants treats a genetic region as a test unit; based on observed genotype it assigns a numeric coding to the region {$X$}:{$$X = I\_(0,N)(\sum\_i^N X_i)$$} i.e., the observed genotype will be coded as {$1$} if there exists at least one mutation, and {$0$} otherwise. This coding theme has been used in (Li and Leal, 2008) and (Bhatia et al, 2010). 

Advantages in using collapsing methods instead of [aggregation methods][1] is in its robustness to LD of multiple rare variants in the region under investigation, which would potentially inflate type I error. However under additive assumptions of genetic effects, collapsing methods may be less powerful than aggregation methods. 

Our program implements the collapsing coding in a logistic regression framework for disease traits analysis (case control data) as `CollapseBt` method, and a linear regression framework for quantitative traits analysis as `CollapseQt` method. {$p$} value for collapsing method is based on asymptotic normal distribution of the Wald statistic in generalized linear models. One could incorporate a number of phenotype covariates in collapsing tests and evaluate the significance of the genetics component. 



#### 1.1 Adjust for missing genotypes

If the pattern of missing genotypes is not random in sample (e.g., missing ratio in cases is different from in controls), then type I error can be inflated. For small proportion of missing data, this issue can be alleviated using methods proposed by Auer et al 2013[^personal communication with Paul L. Auer at Fred Hutchinson Cancer Research Center^], which is implemented as an option `--NA_adjust`. 



### 2. Details

#### 2.1 Command interface

    % vtools show test CollapseBt
    



    Name:          CollapseBt
    Description:   Collapsing method for disease traits, Li & Leal 2008
    usage: vtools associate --method CollapseBt [-h] [--name NAME]
                                                [--mafupper MAFUPPER]
                                                [--alternative TAILED]
                                                [--NA_adjust]
                                                [--moi {additive,dominant,recessive}]
    
    Fixed threshold collapsing method for disease traits (Li & Leal 2008). p-value
    is based on the significance level of the regression coefficient for
    genotypes. If --group_by option is specified, variants within a group will be
    collapsed into a single binary coding using an indicator function (coding will
    be "1" if ANY locus in the group has the alternative allele, "0" otherwise)
    
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
    



    % vtools show test CollapseQt
    



    Name:          CollapseQt
    Description:   Collapsing method for quantitative traits, Li & Leal 2008
    usage: vtools associate --method CollapseQt [-h] [--name NAME]
                                                [--mafupper MAFUPPER]
                                                [--alternative TAILED]
                                                [--NA_adjust]
                                                [--moi {additive,dominant,recessive}]
    
    Fixed threshold collapsing method for quantitative traits (Li & Leal 2008).
    p-value is based on the significance level of the regression coefficient for
    genotypes. If --group_by option is specified, variants within a group will be
    collapsed into a single binary coding using an indicator function (coding will
    be "1" if ANY locus in the group has the alternative allele, "0" otherwise)
    
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
    



#### 2.2 Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    # create a project and download sample project
    % vtools init asso --parent vt_ExomeAssociation
    % vtools associate rare status --covariates age gender bmi exposure -m "CollapseBt --name Col\
    lapseBt --alternative 2" --group_by name2 --to_db collapseBt -j8 > collapseBt.txt
    



    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [=============================] 3,180 32.8/s in 00:01:36
    Testing for association: 100% [=====================] 2,632/147 5.7/s in 00:07:37
    INFO: Association tests on 2632 groups have completed. 147 failed.
    INFO: Using annotation DB collapseBt in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 23:10:09
    



    % vtools show fields | grep collapseBt
    



    collapseBt.name2             name2
    collapseBt.sample_size_CollapseBt sample size
    collapseBt.num_variants_CollapseBt number of variants in each group (adjusted for specified MAF
    collapseBt.total_mac_CollapseBt total minor allele counts in a group (adjusted for MOI)
    collapseBt.beta_x_CollapseBt test statistic. In the context of regression this is estimate of
    collapseBt.pvalue_CollapseBt p-value
    collapseBt.wald_x_CollapseBt Wald statistic for x (beta_x/SE(beta_x))
    collapseBt.beta_2_CollapseBt estimate of beta for covariate 2
    collapseBt.beta_2_pvalue_CollapseBt p-value for covariate 2
    collapseBt.wald_2_CollapseBt Wald statistic for covariate 2
    collapseBt.beta_3_CollapseBt estimate of beta for covariate 3
    collapseBt.beta_3_pvalue_CollapseBt p-value for covariate 3
    collapseBt.wald_3_CollapseBt Wald statistic for covariate 3
    collapseBt.beta_4_CollapseBt estimate of beta for covariate 4
    collapseBt.beta_4_pvalue_CollapseBt p-value for covariate 4
    collapseBt.wald_4_CollapseBt Wald statistic for covariate 4
    collapseBt.beta_5_CollapseBt estimate of beta for covariate 5
    collapseBt.beta_5_pvalue_CollapseBt p-value for covariate 5
    collapseBt.wald_5_CollapseBt Wald statistic for covariate 5
    



    % head collapseBt.txt
    



    name2   sample_size_CollapseBt  num_variants_CollapseBt total_mac_CollapseBt    beta_x_CollapseBt       pvalue_CollapseBt       wald_x_CollapseBt       beta_2_CollapseBt    beta_2_pvalue_CollapseBt        wald_2_CollapseBt       beta_3_CollapseBt       beta_3_pvalue_CollapseBt        wald_3_CollapseBt       beta_4_CollapseBt    beta_4_pvalue_CollapseBt        wald_4_CollapseBt       beta_5_CollapseBt       beta_5_pvalue_CollapseBt        wald_5_CollapseBt
    AADACL4 3180    5       138     -0.2941 0.368956        -0.89843        0.0312903       4.30942E-09     5.87186 -0.296598       0.0154271       -2.42219    0.129942 1.83369E-40     13.3174 0.437372        0.00133613      3.2081
    AAMP    3180    3       35      0.00135633      0.997852        0.0026919       0.0312624       4.39097E-09     5.86875 -0.298944       0.0146254       -2.44152     0.130231        1.24946E-40     13.346  0.43547 0.00139464      3.19576
    ABCB10  3180    6       122     0.333178        0.219379        1.22818 0.0312644       4.40563E-09     5.8682  -0.301597       0.013796        -2.46253    0.130493 9.8029E-41      13.3641 0.431826        0.00154525      3.16605
    ABCG8   3180    12      152     -0.432823       0.171192        -1.36838        0.0314772       3.67916E-09     5.89801 -0.295762       0.0157794       -2.41398     0.130108        1.52929E-40     13.331  0.440976        0.001228        3.2323
    ABCB6   3180    7       151     -0.0619203      0.825828        -0.220056       0.0312972       4.27575E-09     5.87316 -0.299244       0.0145216       -2.4441      0.130203        1.22141E-40     13.3477 0.435756        0.00138398      3.19797
    ABHD1   3180    5       29      -0.129748       0.840786        -0.200889       0.0312418       4.49451E-09     5.86488 -0.298341       0.0148474       -2.43608     0.130264        1.16331E-40     13.3513 0.43624 0.00137271      3.20033
    ABCG5   3180    6       87      0.35312 0.287604        1.06339 0.0312942       4.1554E-09      5.87789 -0.298364       0.0148076       -2.43705        0.130389     9.49319E-41     13.3665 0.440212        0.00124756      3.22778
    ABCD3   3180    3       42      -0.255649       0.662305        -0.436732       0.0312799       4.33855E-09     5.87074 -0.301233       0.0139678       -2.45809     0.130221        1.02858E-40     13.3605 0.436902        0.00134823      3.20551
    ABCA4   3180    43      492     -0.00909763     0.95585 -0.0553619      0.0312634       4.37388E-09     5.8694  -0.298919       0.0146254       -2.44153    0.130239 1.15466E-40     13.3519 0.435484        0.00139409      3.19587
    

**QQ-plot**  Attach:collapseBt.jpg 



    % vtools associate rare bmi --covariates age gender exposure -m "CollapseQt --name CollapseQt\
     --alternative 2" --group_by name2 --to_db collapseQt -j8 > collapseQt.txt
    



    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [=======================] 3,180 33.4/s in 00:01:35
    Testing for association: 100% [====================] 2,632/147 26.2/s in 00:01:40
    INFO: Association tests on 2632 groups have completed. 147 failed.
    INFO: Using annotation DB collapseQt in project test.
    INFO: Annotation database used to record results of association tests. Created on Thu, 31 Jan 2013 03:48:21
    



    % vtools show fields | grep collapseQt
    



    collapseQt.name2             name2
    collapseQt.sample_size_CollapseQt sample size
    collapseQt.num_variants_CollapseQt number of variants in each group (adjusted for specified MAF
    collapseQt.total_mac_CollapseQt total minor allele counts in a group (adjusted for MOI)
    collapseQt.beta_x_CollapseQt test statistic. In the context of regression this is estimate of
    collapseQt.pvalue_CollapseQt p-value
    collapseQt.wald_x_CollapseQt Wald statistic for x (beta_x/SE(beta_x))
    collapseQt.beta_2_CollapseQt estimate of beta for covariate 2
    collapseQt.beta_2_pvalue_CollapseQt p-value for covariate 2
    collapseQt.wald_2_CollapseQt Wald statistic for covariate 2
    collapseQt.beta_3_CollapseQt estimate of beta for covariate 3
    collapseQt.beta_3_pvalue_CollapseQt p-value for covariate 3
    collapseQt.wald_3_CollapseQt Wald statistic for covariate 3
    collapseQt.beta_4_CollapseQt estimate of beta for covariate 4
    collapseQt.beta_4_pvalue_CollapseQt p-value for covariate 4
    collapseQt.wald_4_CollapseQt Wald statistic for covariate 4
    



    % head collapseQt.txt
    



    name2   sample_size_CollapseQt  num_variants_CollapseQt total_mac_CollapseQt    beta_x_CollapseQt       pvalue_CollapseQt       wald_x_CollapseQt       beta_2_CollapseQt    beta_2_pvalue_CollapseQt        wald_2_CollapseQt       beta_3_CollapseQt       beta_3_pvalue_CollapseQt        wald_3_CollapseQt       beta_4_CollapseQt    beta_4_pvalue_CollapseQt        wald_4_CollapseQt
    ABCD3   3180    3       42      -0.487474       0.571152        -0.566415       0.0149956       0.0588415       1.89006 -0.0808192      0.693535        -0.394098    -0.941867       2.64731E-05     -4.20804
    ABCB6   3180    7       151     -0.532616       0.24625 -1.15972        0.0151515       0.056238        1.90989 -0.0810239      0.692719        -0.395204   -0.944219        2.5176E-05      -4.21945
    ABHD1   3180    5       29      0.18344 0.859929        0.176479        0.0150381       0.0581416       1.89531 -0.0794273      0.698569        -0.387288   -0.94411 2.54398E-05     -4.21708
    ABCA12  3180    28      312     -0.415972       0.211796        -1.24889        0.0151627       0.0560493       1.91135 -0.0789784      0.700073        -0.385257    -0.937093       2.90651E-05     -4.18676
    ABCG8   3180    12      152     -0.56687        0.212912        -1.24585        0.0151496       0.0562578       1.90973 -0.0744998      0.716361        -0.363359    -0.939062       2.78992E-05     -4.1961
    ABCA4   3180    43      492     0.0984281       0.721612        0.356337        0.0150102       0.0586022       1.89185 -0.0792212      0.699266        -0.386347    -0.942427       2.61944E-05     -4.21045
    ABI2    3180    1       25      1.19633 0.276415        1.0886  0.0150043       0.0586562       1.89144 -0.081478       0.691101        -0.397397       -0.941765    2.64399E-05     -4.20833
    ABL2    3180    4       41      -0.613866       0.475633        -0.713429       0.0150498       0.0579226       1.89697 -0.0781101      0.703263        -0.380954    -0.945432       2.46814E-05     -4.22394
    ACADL   3180    5       65      1.33815 0.0528276       1.93705 0.0150444       0.0578831       1.89727 -0.082882       0.685934        -0.404416       -0.941384    2.64356E-05     -4.20836
    

<img src = "collapseBt.jpg" width = 500>

</details>

### Reference

Bingshan Li and Suzanne M. Leal (2008) **Methods for Detecting Associations with Rare Variants for Common Diseases: Application to Analysis of Sequence Data**. *The American Journal of Human Genetics* doi:`10.1016/j.ajhg.2008.06.024`. <http://linkinghub.elsevier.com/retrieve/pii/S0002929708004084>


Gaurav Bhatia, Vikas Bansal, Olivier Harismendy, Nicholas J. Schork, Eric J. Topol, Kelly Frazer and Vineet Bafna (2010) **A Covering Method for Detecting Genetic Associations between Rare Variants and Common Phenotypes**. *PLoS Computational Biology* doi:`10.1371/journal.pcbi.1000954`. <http://dx.plos.org/10.1371/journal.pcbi.1000954>


 [1]: /vat-docs/applications/association/joint_conditional/aggre/
 
