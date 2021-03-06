
+++
title = "GroupStat&Write"
weight = 1
+++



## Basic Statistics for Association Testing Units 



### 1. Introduction

`GroupStat` and `GroupWrite` are "ancillary" features for the collection of `VAT` association tests. Instead of carrying out association analysis, `GroupStat` reports summary statistics of an association test unit such as total allele counts, total variant counts, number of samples, etc., while `GroupWrite` output genotype and phenotype information (into zipped bundles) in the format compatible with the [SCORE-Seq software][1] such that the data can be closely examined or manipulated using other software tools. 



Although the `vtools export` function may also write variant/genotype data into VCF and other formats with variants annotated and genotype calls cleaned after quality control, it will not be able to output result from fine-scale QC for each test unit (see the [usage of][2] `--discard_samples` and `--discard_variants`). The `GroupWrite` will output the exact dataset that goes into association testing methods 

It is recommended to run `GroupStat` and `GroupWrite` simultaneously with other association methods, as documented [here][2]. 



### 2. Details

#### 2.1 Command interface

    vtools show test GroupStat
    vtools show test GroupWrite
    
    Name:          GroupWrite
    Description:   Write data to disk for each testing group
    usage: vtools associate --method GroupWrite [-h] [--name NAME] directory
    
    Group data writer. It will create 3 files for each group: a phenotype file
    with rows representing samples , the 1st column is sample name, the 2nd column
    is the quantitative or binary phenotype and remaining columns are covariates
    if there are any; a genotype file with rows representing variants and the
    columns represent sample genotypes (order of the rows matches the genotype
    file). Coding of genotypes are minor allele counts (0/1/2). Missing values are
    denoted as NA; a mapping file that matches the group ID and variant ID
    in pairs.
    
    positional arguments:
      directory    Output data will be written to the directory specified.
    
    optional arguments:
      -h, --help   show this help message and exit
      --name NAME  Name of the test that will be appended to names of output
                   fields.
    



#### 2.2 Application

<details><summary> Example using **snapshot** `vt_ExomeAssociation`</summary> 



    vtools associate rare status -m "GroupStat ... " "GroupWrite /path/to/outputdir" --group_by\
     name2 --to_db gstat -j8 > gstat.txt
    

</details>

 [1]: http://www.bios.unc.edu/~dlin/software/SCORE-Seq/
 [2]:   /applications/association/