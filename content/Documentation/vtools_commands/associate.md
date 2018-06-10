+++
title = "associate"
description = ""
weight = 11
+++


## Identify genotype - phenotype association 


### 1. Usage

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
                            quoted long argument (e.g. --methods "m --alternative
                            2" "m1 --permute 1000"), although the common method
                            parameters can be specified separately, as long as
                            they do not conflict with command arguments. (e.g.
                            --methods m1 m2 -p 1000 is equivalent to --methods "m1
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
    



### 2. Details

Please check [the VAT homepage][1] for details.

 [1]:  