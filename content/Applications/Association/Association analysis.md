
+++
title = "Association analysis"
description = ""
weight = 3
+++




# Association Analysis 



## Statistical Tests for Genotype/phenotype Associations

### The `VAT` association command

We will introduce the basic usage of this command without diving into each association test. For a complete demonstration of all the tests please refer to the documentation for `VAT` (on the sidebar of this webpage). 



### Getting started

The general interface of `vtools associate` is as follows 



    % vtools associate -h
    

    usage: vtools associate [-h] [--covariates [COVARIATES [COVARIATES ...]]]
                            [--var_info [VAR_INFO [VAR_INFO ...]]]
                            [--geno_info [GENO_INFO [GENO_INFO ...]]]
                            [-m METHODS [METHODS ...]]
                            [-g [GROUP_BY [GROUP_BY ...]]] [-s [COND [COND ...]]]
                            [--genotypes [COND [COND ...]]]
                            [--discard_samples [EXPR [EXPR ...]]]
                            [--discard_variants [EXPR [EXPR ...]]]
                            [--to_db annoDB] [-f] [-j N] [-v {0,1,2}]
                            variants phenotypes
    
    Call one or more statistical association tests and return test results as
    fields to variants tested.
    
    optional arguments:
      -h, --help            show this help message and exit
      -j N, --jobs N        Number of processes to carry out association tests.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).
    
    Genotype, phenotype, and covariates:
      variants              Table of variants to be tested.
      phenotypes            A list of phenotypes that will be passed to the
                            association statistics calculator. Currently only a
                            single phenotype is allowed.
      --covariates [COVARIATES [COVARIATES ...]]
                            Optional phenotypes that will be passed to statistical
                            tests as covariates. Values of these phenotypes should
                            be integer or float.
      --var_info [VAR_INFO [VAR_INFO ...]]
                            Optional variant information fields (e.g. minor allele
                            frequency from 1000 genomes project) that will be
                            passed to statistical tests. The fields could be any
                            annotation fields of with integer or float values,
                            including those from used annotation databases (use
                            "vtools show fields" to see a list of usable fields).
      --geno_info [GENO_INFO [GENO_INFO ...]]
                            Optional genotype fields (e.g. quality score of
                            genotype calls, cf. "vtools show genotypes") that will
                            be passed to statistical tests. Note that the fields
                            should exist for all samples that are tested.
    
    Association tests:
      -m METHODS [METHODS ...], --methods METHODS [METHODS ...]
                            Method of one or more association tests. Parameters
                            for each method should be specified together as a
                            quoted long argument (e.g. --method "m --alternative
                            2" "m1 --permute 1000"), although the common method
                            parameters can be specified separately, as long as
                            they do not conflict with command arguments. (e.g.
                            --method m1 m2 -p 1000 is equivalent to --method "m1
                            -p 1000" "m2 -p 1000".). You can use command 'vtools
                            show tests' for a list of association tests, and
                            'vtools show test TST' for details about a test.
                            Customized association tests can be specified as
                            mod_name.test_name where mod_name should be a Python
                            module (system wide or in the current directory), and
                            test_name should be a subclass of NullTest.
      -g [GROUP_BY [GROUP_BY ...]], --group_by [GROUP_BY [GROUP_BY ...]]
                            Group variants by fields. If specified, variants will
                            be separated into groups and are tested one by one.
    
    Select and filter samples and genotypes:
      -s [COND [COND ...]], --samples [COND [COND ...]]
                            Limiting variants from samples that match conditions
                            that use columns shown in command 'vtools show sample'
                            (e.g. 'aff=1', 'filename like "MG%"'). Each line of
                            the sample table (vtools show samples) is considered
                            as samples. If genotype of a physical sample is
                            scattered into multiple samples (e.g. imported
                            chromosome by chromosome), they should be merged using
                            command vtools admin.
      --genotypes [COND [COND ...]]
                            Limiting genotypes to those matching conditions that
                            use columns shown in command 'vtools show genotypes'
                            (e.g. 'GQ>15'). Genotypes failing such conditions will
                            be regarded as missing genotypes.
      --discard_samples [EXPR [EXPR ...]]
                            Discard samples that match specified conditions within
                            each test group (defined by parameter --group_by).
                            Currently only expressions in the form of "%(NA)>p" is
                            providedted to remove samples that have more 100*p
                            percent of missing values.
      --discard_variants [EXPR [EXPR ...]]
                            Discard variant sites based on specified conditions
                            within each test group. Currently only expressions in
                            the form of '%(NA)>p' is provided to remove variant
                            sites that have more than 100*p percent of missing
                            genotypes. Note that this filter will be applied after
                            "--discard_samples" is applied, if the latter also is
                            specified.
    
    Output of test statistics:
      --to_db annoDB        Name of a database to which results from association
                            tests will be written. Groups with existing results in
                            the database will be ignored unless parameter --force
                            is used.
      -f, --force           Analyze all groups including those that have recorded
                            results in the result database.
    

Each association test method (`-m/--method`) has its own commandline interface. To show all available association tests, 



    % vtools show tests
    

    BurdenBt              Burden test for disease traits, Morris & Zeggini 2009
    BurdenQt              Burden test for quantitative traits, Morris & Zeggini
                          2009
    CFisher               Fisher's exact test on collapsed variant loci, Li & Leal
                          2008
    ....
    

To show usage of a particular test, 



    % vtools show test CFisher
    

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
    

A basic association test requires the following input: 



*   variants to be analyzed (see vtools show tables) 
*   a variant table previously created for a subset of variants 
*   phenotype to be analyzed (see vtools show samples `-l1`) 
*   phenotype covariates to be incorporated (`--covariates`) 
*   samples to be analyzed (`--samples`) 
*   genotype quality conditions, if low quality genotypes are not previously purged from database (`--genotypes`) 
*   missing data filters (`--discard_samples` and `--discard_variants`) 
*   association analysis method 
*   association testing group unit (`--group_by`. Will perform single variant analysis if unspecified.) 
*   output database filename (`--to_db`) 
*   number of CPU processors to be used for parallel computing 



Missing values are not allowed in phenotype/covariates data. Samples having missing values in phenotype or any covariates will be removed and you will receive a warning message. If you want to retain samples having missing values in covariates we suggest you manually fill them with specified values (`vtools phenotype --set ... --samples ...`). For quantitative traits the value can be the sample mean, and for qualitative traits be the most likely category. 

In this tutorial we demonstrate basic association analysis of a disease phenotype and a quantitative phenotype (simulated traits `status` and `bmi`). We choose to include covariate phenotypes *gender* and *age* when we demonstrate the multivariate analysis. 



#### Association analysis for common variants

For single variant analysis with disease trait: 



    % vtools associate common status \
    	       --covariates gender age \
    	       --discard_variants "%(NA)>0.1" \
    	       --method "LogitRegBurden --name SNV --alternative 2" \
    	       --to_db SNV \
    	       -j8 > SNV.txt
    

    

{$p$} values calculated by this command are based on Wald statistic of logistic regression analysis. To evaluate p-values empirically, 



    % vtools associate common status \
    	       --covariates gender age \
    	       --discard_variants "%(NA)>0.1" \
    	       --method "LogitRegBurden --name SNV_permute --alternative 2 -p 100000000 --\
    adaptive 5e-5" \
    	       --to_db SNV \
    	       -j8 > SNV_permute.txt
    

we use a maximum of 100 million permutations per test, with an adaptive criteria {$p=5 \times 10^{-5}$}. It takes about 15 seconds to complete the analysis on 1711 groups analytically and about 15 minutes on the same data using permutation based p-value evaluations. 



By setting `--name` (inside the `--method` option) to a different name `SNV_permute` it is possible to insert new results from permutation tests to the same database `SNV.DB` while keeping the results from the previous non-permutation based analysis intact. 



#### Association analysis for rare variants

Instead of analyzing them individually, rare variants are usually grouped into association units and are analyzed by groups. For exome analysis association units are genes. The `--group_by/-g` option can be used to create flexible grouping themes for rare variant analysis from variant fields or annotation databases. For example the name2 field in the *refGene* database can be used to classify variants into genes for analysis: 



    % vtools associate rare status \
    	       --covariates gender age \
    	       --discard_samples "%(NA)>0.1" \
    	       --discard_variants "%(NA)>0.1" \
    	       --method "BurdenBt --name BurdenTest --alternative 2" \
    	       --group_by name2 \
    	       --to_db BurdenTest \
    	       -j8 > BurdenTest.txt
    

    

Permutation based analysis and other association methods (`vtools show tests` for disease traits and quantitative traits) are available but will not be demonstrated here. 



#### Resuming previously terminated analysis

Exome-wide association scan typically consists of thousands of tests for gene-based analysis, and up to a million tests for single variant analysis. In many cases an association command may be interrupted before all tests are completed (e.g., commands terminated due to running out of reserved CPU time on clusters, etc). If you have used `--to_db` option in the previous command, then resuming the analysis is simple: just re-run the exact command that was interrupted. The program will skip the records that exist in the result database and only carry out the ones that are missing. If you want to start all over, you may apply a `--force` option to the association command so that the existing result database will be overwritten, regardless of the data it already contains. 



#### Setting a *timeout* for permutation based association analysis

    Although with the "adaptive permutation" approach most permutation tests in an exome-wide a\
    ssociation scan would terminate early after a few thousand permutations, for scans involvin\
    g up to a million association tests you are likely to see some tests running for hours, rep\
    orting very small p-values in the end. These tests will temporarily hold up the computation\
     resource (they have to be finished first before the rest of tests get started). We provide\
     an option to set a time limit per test, in addition to using the adaptive permutation. Thi\
    s option is useful particularly when your computation resource is tight, or if you use a cl\
    uster that offers limited walltime, or if your sample size is small and result in extreme v\
    alues of test statistic. To set the association timeout to 1 hour (3600s):
    



    % vtools admin --set_runtime_option association_timeout=3600
    % vtools show
    



    

After association scan is complete you can track and redo these timed out tests with larger or no timeout value, 



    % vtools select variant "test_pvalue < 0" --table TO_REDO
    % vtools admin --reset_runtime_option association_timeout
    

and re-run the association command with `--force` option so that the updated results will be written to the database previously generated with the `--to_db` option. 



#### Reset temporary data folder for association analysis

We implemented a mechanism to optimally organize and access the genotype data for association testing. Temporary association databases will be generated on the fly and removed after the analysis is complete. By default these databases will be placed in the operating system's temp path (usually /tmp or /var/tmp on Unix-like system). We may need to specify a temporary folder for association testing that 1) has large disk space and 2) locates on a different physical harddrive than the original project database bundle. Using a small disk for the temporary data may cause program crash (in which case you will receive an error message complaining about disk space) or degraded performance (in which case you will receive a warning message). To reset the temp folder, use 



    % vtools admin --set_runtime_option temp_dir=/path/to/an/empty/directory
    



#### Other runtime options for association analysis

Two other runtime options `associate_num_of_readers` and `treat_missing_as_wildtype` for association testing are available but will not be discussed here. Please use the following command to see the usage of these runtime options: 



    % vtools show runtime_options
    



### Viewing and Interpreting Association Results

#### View association analysis results

(This feature is under development) 

`vtools_report` commands `plot_qq` and `plot_manhattan` to present the association analysis results in QQ plot or Manhattan plot: 



    usage: aviewer [-h] [--version] {qq,manhattan,manhattan_plain} ...
    
    Association Viewer, generating QQ / Manhattan plots of p-values from
    association analysis. Input data should be in the format of the output from
    'vtools associate' command and be piped to the program as stdin.
    
    positional arguments:
      {qq,manhattan,manhattan_plain}
        qq                  QQ plot via ggplot2
        manhattan           Manhattan plot via ggplot2
        manhattan_plain     Manhattan plot implementation not using ggplot2
    
    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
    

This program generates graphs for {$p$} values, allowing for 



*   multiple association results plotted on the same / different pages 
*   various color, shape and legend themes to choose from 
*   text labels for siginificant p-values on the graph 
*   text labels for specified variants/genes on the graph 
*   marks for significance levels (Bonforroni correction or user specified value) 



## Online Dataset Examples

You can use our snapshot for association `vt_ExomeAssociation` to test out the `VAT` association features. This is a non-trivial dataset of ~30k variants and ~3k samples with simulated phenotypes 



    % vtools init test
    % vtools show snapshots
    % vtools admin --load_snapshot vt_ExomeAssociation