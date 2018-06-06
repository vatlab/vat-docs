
+++
title = "SKAT test"
weight = 5
+++


## SNP-set (Sequence) Kernel Association Test Method 


### 1. Introduction

### 2. Details

#### 2.1 Command interface

    vtools show test SKAT
    



    Name:          SKAT
    Description:   SKAT (Wu et al 2011) wrapper of its original R implementation
    usage: vtools associate --method SKAT [-h] [--name NAME]
                                          [-k {linear,linear.weighted,IBS,IBS.weighted,quadratic,2wayIX}]
                                          [--beta_param BETA_PARAM BETA_PARAM]
                                          [-m {davies,liu,liu.mod,optimal}]
                                          [-i {fixed,random}]
                                          [--logistic_weights PARAM PARAM]
                                          [-r [CORR [CORR ...]]]
                                          [--missing_cutoff MISSING_CUTOFF]
                                          [--resampling N] [--small_sample]
                                          [--resampling_kurtosis N]
                                          {quantitative,disease}
    
    SNP-set (Sequence) Kernel Association Test (Wu et al 2011). This is a wrapper
    for the R package "SKAT" implemented & maintained by Dr. Seunggeun Lee, with a
    similar interface and minimal descriptions based on the SKAT package
    documentation (May 11, 2012). Please refer to
    http://http://cran.r-project.org/web/packages/SKAT/ for details of usage. To
    use this test you should have R installed with SKAT v0.75 or higher. The SKAT
    commands applied to the data will be recorded and saved in the project log
    file.
    
    positional arguments:
      {quantitative,disease}
                            Phenotype is quantitative trait or disease trait (0/1
                            coding). Default set to "quantitative"
    
    optional arguments:
      -h, --help            show this help message and exit
      --name NAME           Name of the test that will be appended to names of
                            output fields, usually used to differentiate output of
                            different tests, or the same test with different
                            parameters.
      -k {linear,linear.weighted,IBS,IBS.weighted,quadratic,2wayIX}, --kernel {linear,linear.weighted,IBS,IBS.weighted,quadratic,2wayIX}
                            A type of kernel. Default set to "linear.weighted".
                            Please refer to SKAT documentation for details.
      --beta_param BETA_PARAM BETA_PARAM
                            Parameters for beta weights. It is only used with
                            weighted kernels. Default set to (1,25). Please refer
                            to SKAT documentation for details.
      -m {davies,liu,liu.mod,optimal}, --method {davies,liu,liu.mod,optimal}
                            A method to compute the p-value. Default set to
                            "davies". Please refer to SKAT documentation for
                            details.
      -i {fixed,random}, --impute {fixed,random}
                            A method to impute missing genotypes. Default set to
                            "fixed". Please refer to SKAT documentation for
                            details.
      --logistic_weights PARAM PARAM
                            This option, if specified, will get the logistic
                            weights from genotype matrix Z and apply this weight
                            to SKAT. It requires two input parameters par1 and
                            par2. To use the SKAT default setting, type
                            `--logistic_weights 0.07 150'. Please refer to SKAT
                            documentation for details.
      -r [CORR [CORR ...]], --corr [CORR [CORR ...]]
                            The pho parameter of SKAT test. Default is 0. Please
                            refer to SKAT documentation for details.
      --missing_cutoff MISSING_CUTOFF
                            a cutoff of the missing rates of SNPs. Any SNPs with
                            missing rates higher than cutoff will be excluded from
                            the analysis. Default set to 0.15
      --resampling N        Number of resampling using bootstrap method. Set it to
                            '0' if you do not want to apply resampling.
      --small_sample        This option, if evoked, will apply small sample
                            adjustment "SKAT_Null_Model_MomentAdjust" for small
                            sample size and binary trait. Please refer to SKAT
                            documentation for details.
      --resampling_kurtosis N
                            Number of resampling to estimate kurtosis, for small
                            sample size adjustment. Set it to '0' if you do not
                            wnat to apply the adjustment. The SKAT default setting
                            is 10000. Please refer to SKAT documentation for
                            details.
    



#### 2.2 Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status -m "SKAT --name skat quantitative" --group_by refGene.name2 --\
    to_db skat -j8 > skat.txt
    



    INFO: 3180 samples are found
    INFO: 2632 groups are found
    INFO: Starting 8 processes to load genotypes
    Loading genotypes: 100% [=========================================================================================================================================] 3,180 32.8/s in 00:01:36
    Testing for association: 100% [================================================================================================================================] 2,632/147 8.9/s in 00:04:56
    INFO: Association tests on 2632 groups have completed. 147 failed.
    INFO: Using annotation DB skat in project test.
    INFO: Annotation database used to record results of association tests. Created on Wed, 30 Jan 2013 21:34:23
    



    vtools show fields | grep skat
    



    skat.refGene_name2           refGene_name2
    skat.sample_size_skat        Sample size
    skat.Q_stats_skat            Test statistic for SKAT, "Q"
    skat.pvalue_skat             p-value
    



    head skat.txt
    



    refGene_name2	sample_size_skat	Q_stats_skat	pvalue_skat
    AADACL4	3180	33707.7	0.379148
    ABCD3	3180	1178.25	0.961708
    AAMP	3180	5905.71	0.612598
    ABCB10	3180	55121.9	0.109206
    ABCB6	3180	16500.2	0.812062
    ABCG5	3180	9829.17	0.76832
    ABI2	3180	42491.9	0.0100467
    ABHD1	3180	1315.49	0.880286
    ABL2	3180	794.385	0.963097
    

</details>