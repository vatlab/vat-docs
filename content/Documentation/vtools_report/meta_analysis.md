
+++
title = "meta_analysis"
weight = 9
+++



## Meta-analysis for Association Testing Results 



### 1. Introduction

`vtools_report meta_analysis` implements meta-analysis methods detailed in (Willer et al, 2010). Two statistics are available: the sample size based statistic and inverse variance based statistic. Input of this command are multiple text or compressed text files of association results delimited by tabs. 



### 2. Details

#### 2.1 Command interface

    % vtools_report meta_analysis -h

    usage: vtools_report meta_analysis [-h] [--beta col] [--pval col] [--se col]
                                       [-n col] [--link col [col ...]] [-m method]
                                       [--to_db database] [-v {0,1,2}]
                                       file [file ...]
    
    positional arguments:
      file                  Input text files in the format of \\(vtools associate
                            output (supports plain text, gz or bz2 compressed text
                            files)
    
    optional arguments:
      -h, --help            show this help message and exit
      --beta col            column number of beta
      --pval col            column number of p-value
      --se col              column number of standard error
      -n col, --size col    column number of sample size
      --link col [col ...]  columns that links entries of two datasets
      -m method, --method method
                            Method (choose from "ssb" for sample based method and
                            "ivb" for inverse variance based method), default set
                            to "ssb"
      --to_db database      will write the results also to a sqlite3 database
                            compatible with vtools associate result format
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.
    



#### 2.2 Example

Input files are 



    % zless study1.gz

    refGene_name2   sample_size_VT  num_variants_VT total_mac_VT    beta_x_VT       pvalue_VT       std_error_VT    num_permutations_VT     MAF_threshold_VT
    A1BG    159     2       24      0.0191151       0.891109        0.213265        1000    0.00628931
    A1BG-AS1        309     2       43      -0.409899       0.563437        0.27416 1000    0.00161812
    A1CF    327     6       10      0.274825        0.275724        0.18807 1000    0.00152905
    A2M     330     6       21      -0.0123306      0.985015        0.153102        1000    0.00151515
    A2ML1   331     8       19      -0.280548       0.25974 0.159701        1000    0.00151057
    ...
    

`study2.gz` is in the same format. The effect size is the 5th column, p-value the 6th column and sample size 1st column. The two data-sets are matched by gene name, i.e., the first column. The meta analysis command is: 



    % vtools_report meta_analysis study1.gz study2.gz --beta 5 --pval 6 --size 2 --link 1 \
    % --to_db study1and2 > study1and2.txt
    

Result are outputted to both text file and database. 



    % less study1and2.txt
    
    refGene_name2	p_meta	sample_size_meta	beta_x_VT_1	pvalue_VT_1	sample_size_VT_1	beta_x_VT_2	pvalue_VT_2	sample_size_VT_2
    RESP18	6.380E-01	238	0.570054	0.1998	119	-0.228113	0.537463	119
    STX6	8.583E-01	633	0.010475	0.875125	302	-0.434853	0.691309	331
    ARFGEF2	7.984E-01	645	0.161718	0.417582	314	-0.169275	0.251748	331
    TSEN34	3.459E-01	104	0.604153	0.323676	52	0.461471	0.729271	52
    ...
    

To load the meta analysis result to the project 



    % vtools use study1and2.DB --linked_by name2

    INFO: Using annotation DB study1and2 in project SSc.
    INFO: Combined association tests result database. Created on Thu, 14 Mar 2013 17:35:44
    INFO: 7459 out of 23242 refGene.name2 are annotated through annotation database study1and2
    
### Reference

C. J. Willer, Y. Li and G. R. Abecasis (2010). **METAL: fast and efficient meta-analysis of genomewide association scans**. *Bioinformatics*