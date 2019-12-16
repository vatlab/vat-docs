
+++
title = "phenotype"
weight = 4
+++



## Import and manipulate phenotypes 


### 1. Usage

    % vtools phenotype -h
    
    usage: vtools phenotype [-h] [-f [INPUT_FILE [INPUT_FILE ...]]]
                            [--set [EXPRESSION [EXPRESSION ...]]]
                            [--from_stat [EXPRESSION [EXPRESSION ...]]]
                            [--output [EXPRESSION [EXPRESSION ...]]] [-j N]
                            [-g [COND [COND ...]]] [-s [COND [COND ...]]]
                            [--header [HEADER [HEADER ...]]] [-d DELIMITER]
                            [--na NA] [-l LIMIT] [-v {0,1,2}]
    
    Import phenotypes from a file, or set phenotypes to constants, or to summary
    statistics of sample genotype fields.
    
    optional arguments:
      -h, --help            show this help message and exit
      -f [INPUT_FILE [INPUT_FILE ...]], --from_file [INPUT_FILE [INPUT_FILE ...]]
                            Import phenotype from a tab or space delimited file,
                            which can be standard input if a name - is specified.
                            Samples are determined by sample names in the first
                            column, or jointly by sample name and filename if
                            there is another column with header 'filename'. Names
                            of phenotype fields are determined by header of the
                            input file, or by names provided from option --header.
                            Non-alphanumeric characters in input filed names will
                            be replaced by '_'. If multiple samples in a project
                            share the same names, they will shared the imported
                            phenotypes. Optionally, a list of phenotypes (columns
                            of the file) can be specified after filename, in which
                            case only the specified phenotypes will be imported.
                            Parameter --samples could be used to limit the samples
                            for which phenotypes are imported. Values that match
                            value of parameter --na and cannot be converted to the
                            probed type of phenotype (e.g. '' in a column of
                            numbers) are recorded as missing values.
      --set [EXPRESSION [EXPRESSION ...]]
                            Set a phenotype to a constant (e.g. --set aff=1), or
                            an expression using other existing phenotypes (e.g.
                            --set ratio_qt=high_qt/all_qt (the ratio of the number
                            of high quality variants to the number of all
                            variants, where high_qt and all_qt are obtained from
                            sample statistics using parameter --from_stat).
                            Parameter --samples could be used to limit the samples
                            for which genotypes will be set.
      --from_stat [EXPRESSION [EXPRESSION ...]]
                            Set a phenotype to a summary statistics of a genotype
                            field. For example, "num=count(*)" sets phenotype num
                            to be the number of genotypes of a sample,
                            "GD=avg(DP)" sets phenotype DP to be the average depth
                            (if DP is one of the genotype fields) of the sample.
                            Multiple fields (e.g. '--from_stat "num=count(*)"
                            "GD=avg(DP)"') are also allowed. In addition to
                            standard SQL aggregation functions, variant tools
                            supports special functions #(GT), #(wtGT), #(mutGT),
                            #(alt), #(hom), #(het) and #(other), which counts the
                            number of genotypes (the same as count(*)), wildtype
                            genotypes, mutant genotypes alternative alleles,
                            homozygotes, heterozygotes, and genotypes with two
                            different alternative alleles. Parameters --genotypes
                            and --samples could be used to limit the genotypes to
                            be considered and the samples for which genotypes will
                            be set.
      --output [EXPRESSION [EXPRESSION ...]]
                            A list of phenotype to be outputted. SQL-compatible
                            expressions or functions such as "DP/DP_all" and
                            "avg(DP)" are also allowed
      -j N, --jobs N        Allow at most N concurrent jobs to obtain sample
                            statistics for parameter --from_stat.
      -g [COND [COND ...]], --genotypes [COND [COND ...]]
                            Limit the operation to genotypes that match specified
                            conditions. Use 'vtools show genotypes' to list usable
                            fields for each sample.
      -s [COND [COND ...]], --samples [COND [COND ...]]
                            Update phenotype for samples that match specified
                            conditions. Use 'vtools show samples' to list usable
                            fields in the sample table.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).
    
    Input/Output options:
      --header [HEADER [HEADER ...]]
                            A list of header names for input file if used with
                            option --from_file. Otherwise a complete header or a
                            list of names that will be joined by a delimiter
                            (parameter --delimiter), for option --output. If a
                            special name - is specified, the header will be read
                            from the standard input, which is the preferred way to
                            specify large multi-line headers (e.g. cat myheader |
                            vtools export --header -). If this parameter is given
                            without parameter, a default header will be derived
                            from field names.
      -d DELIMITER, --delimiter DELIMITER
                            Delimiter, default to tab, a popular alternative is
                            ',' for csv output
      --na NA               Input or output string for missing value..
      -l LIMIT, --limit LIMIT
                            Number of record to display. Default to all record.
    



### 2. Details

Unlike `vtools import` and `vtools update`, this command imports/adds properties to *samples* rather than to *variants*. These properties include: 



1.  Extra phenotype information imported from a tab-delimited file, via `--from_file FILE` 
2.  Some values calculated from other phenotype columns, via `--set "EXPRESSION"` 
3.  Summary statistics of genotype info of the samples, via `--from_stat "EXPRESSION"` 

Any properties of sample individuals are considered a *phenotype* in `vtools phenotype`, including sample genotype information such as genotype calls quality, genotype depth of coverage and homozygote/heterozygote counts, etc., which can be useful in data quality control processes. 



The difference between `--set` and `--from_stat` is that `--set` uses expressions with existing phenotype (fields in `vtools show samples`), and `--from_stat` uses expressions with genotype information. 



##### 2.1 Importing phenotypes from text files

The `vtools phenotype --from_file` command identifies a sample by its name but it can also identify a sample by a combination of sample name and file name because not all samples have names. The basic form of this command imports phenotype by sample names from a tab or comma delimited file. 

<details><summary> Examples: Create a new project</summary> To illustrate the use of this command, let's start a new project and import some variants/genotypes 



    % vtools init test -f
    % vtools admin --load_snapshot vt_testData_v3
    % vtools import CEU_hg38.vcf --build hg38 --var_info DP --geno_info DP_geno
    
    INFO: Importing variants from CEU_hg38.vcf (1/1)
    CEU_hg38.vcf: 100% [======================================] 306 21.4K/s in 00:00:00
    INFO: 292 new variants (292 SNVs) from 306 lines are imported.
    Importing genotypes: 100% [================================] 292 3.5K/s in 00:00:00

    

There are 60 samples without genotype 



    % vtools show samples -l 10
    
    sample_name filename
    NA06985     CEU_hg38.vcf
    NA06986     CEU_hg38.vcf
    NA06994     CEU_hg38.vcf
    NA07000     CEU_hg38.vcf
    NA07037     CEU_hg38.vcf
    NA07051     CEU_hg38.vcf
    NA07346     CEU_hg38.vcf
    NA07347     CEU_hg38.vcf
    NA07357     CEU_hg38.vcf
    NA10847     CEU_hg38.vcf
    (50 records omitted)

    

</details>

<details><summary> Examples: Import phenotype from a file</summary> 

    % head -10 phenotype.txt
    
    sample_name	aff	sex	BMI
    NA06985	2	F	19.64
    NA06986	1	M	None
    NA06994	1	F	19.49
    NA07000	2	F	21.52
    NA07037	2	F	23.05
    NA07051	1	F	21.01
    NA07346	1	F	18.93
    NA07347	2	M	19.2
    NA07357	2	M	20.61
    

To import phenotypes from this file, 



    % vtools phenotype --from_file phenotype.txt
    
    INFO: Adding phenotype aff of type INT
    INFO: Adding phenotype sex of type VARCHAR(1)
    INFO: Adding phenotype BMI of type FLOAT
    WARNING: Value "None" is treated as missing in phenotype BMI
    WARNING: 1 missing values are identified for phenotype BMI
    INFO: 3 field (3 new, 0 existing) phenotypes of 60 samples are updated.

This phenotype file now has 3 additional columns: affection status (1 or 2), gender (F or M) and BMI. The type of these columns are automatically determined, and the `None` value in the `BMI` column is treated as missing. 



    % vtools show phenotypes -l 10
    
    sample_name	aff	sex	BMI
    NA06985    	2  	F  	19.64
    NA06986    	1  	M  	.
    NA06994    	1  	F  	19.49
    NA07000    	2  	F  	21.52
    NA07037    	2  	F  	23.05
    NA07051    	1  	F  	21.01
    NA07346    	1  	F  	18.93
    NA07347    	2  	M  	19.2
    NA07357    	2  	M  	20.61
    NA10847    	2  	M  	14.6
    (50 records omitted)

</details>


{{% notice tip %}}
*variant tools* automatically probe the type of phenotype. Values that match value specified by parameter `--na` or cannot be converted to probed type (e.g. `''` or `None` in a column of numbers) will be treated as missing values. 
{{% /notice %}}

If you have a large number of phenotypes and you only need to import some of them, you can specify a list of phenotypes after the filename. 

<details><summary> Examples: Import selected phenotypes from a file</summary> 

Let us first remove the phenotypes we just loaded: 

    % vtools remove phenotypes aff sex BMI
    % vtools show phenotypes -l 10
    
    sample_name
    NA06985
    NA06986
    NA06994
    NA07000
    NA07037
    NA07051
    NA07346
    NA07347
    NA07357
    NA10847
    (50 records omitted)
    

and only import the sex phenotype from the file: 

    % vtools phenotype --from_file phenotype.txt sex
    
    INFO: Adding phenotype sex of type VARCHAR(1)
    INFO: 1 field (1 new, 0 existing) phenotypes of 60 samples are updated.



    % vtools show phenotypes -l 10
    
    sample_name	sex
    NA06985    	F
    NA06986    	M
    NA06994    	F
    NA07000    	F
    NA07037    	F
    NA07051    	F
    NA07346    	F
    NA07347    	M
    NA07357    	M
    NA10847    	M
    (50 records omitted)

</details>

Other features of this command include 

*   You can load phenotypes for only selected samples, which are specified by conditions such as `--samples 'sample_name like "<span class='NB'>"'`.</span> 
*   The input file can be tab, comma, or space delimited. The command will automatically detect the delimiter used. 
*   The input file can have windows or Linux newlines, even the lengendary `\M` newline that is still outputted by the MaxOSX version of Excel. 
*   The input file can be standard input if specify `-` as input filename. This allows you to use a pipe to send me phenotype file. 
*   *variant tools* automatically translate non-standard header names to a valid variant tools field name, by replacing non-alphanumeric characters with underscores (`'_'`). 

{{% notice tip%}}
If your input file does not have any header, you can use option `--header` to specify a list of headers. This is helpful for importing plink `.pfam` file, using a command similar to `vtools phenotype --from_file /tmp/test.tfam --header Family_ID sample_name Paternal_ID Maternal_ID Gender Status` 
{{% /notice %}}


#### 2.2 New columns based on other phenotypes

`vtools phenotype --set` command allows users to create new columns in the phenotype table based on other phenotypes. 

<details><summary> Examples: Create a column race from CEU samples having race=1</summary> 



    % vtools phenotype --set 'race=1' --samples 'filename like "%CEU%"'
    
    INFO: Adding phenotype race
    INFO: 60 values of 1 phenotypes (1 new, 0 existing) of 60 samples are updated.


    % vtools show samples -l 10
    
    sample_name filename        sex race
    NA06985     CEU_hg38.vcf    F   1
    NA06986     CEU_hg38.vcf    M   1
    NA06994     CEU_hg38.vcf    F   1
    NA07000     CEU_hg38.vcf    F   1
    NA07037     CEU_hg38.vcf    F   1
    NA07051     CEU_hg38.vcf    F   1
    ... ...

    

</details>

the `--samples` option specify the subset of samples to which the new column value will be appended. Note above that `None` is assigned to samples that does not match the specified `--samples` condition. More examples on the `--samples` option are documented in `vtools update`, `vtools select`, etc. 



#### 2.3 New columns based on sample genotype and genotype information

With `vtools show genotypes` we know the total number of genotypes and available genotype information in the sample. `vtools phenotype --from_stat` further allows calculation of specific sample genotype properties. 

<details><summary> Examples: Phenotype from genotype statistics</summary> 



    % vtools phenotype --from_stat "sample_total=#(GT)"
    % vtools phenotype --from_stat "sample_alt=#(alt)"
    % vtools phenotype --from_stat "sample_homo=#(hom)"
    % vtools phenotype --from_stat "sample_het=#(het)"
    % vtools phenotype --from_stat "sample_double_het=#(other)"
    % vtools show samples -l 10
    
    sample_name	filename  	sex	race	sample_total	sample_alt	sample_homo	sample_het	sample_double_het
    NA06985     CEU_hg38.vcf    F   1       292             110         40          30          0
    NA06986     CEU_hg38.vcf    M   1       292             126         31          64          0
    NA06994     CEU_hg38.vcf    F   1       292             131         37          57          0
    ... ...
    NA12873     CEU_hg38.vcf    F   1       288             137         37          63          0
    NA12874     CEU_hg38.vcf    M   1       292             101         30          41          0

    

gives statistic of different genotypes. 



*   Wild-type genotype can be directly calculated using `vtools phenotype --set "sample_wt=sample_total-sample_homo-sample_het-sample_double_het"` 

</details>

Another useful type of summary is the genotype information that usually summarizes genotype data quality. Notice that at the beginning of this example session we included genotype depth of coverage using option `--geno_info`. With this (and as many others as your `vcf` file provides) genotype information you can calculate summary statistics and append them to sample table. For example, `DP_geno` is the *read depth* for sample genotypes, a useful indicator of sample genotype quality. You may summarize `DP_geno` for each individual using the commands below: 

<details><summary> Examples: Phenotype calculated from statistics of genotype info fields</summary> 

    % vtools phenotype --from_stat "meanDP=avg(DP_geno)" "minDP=min(DP_geno)" "maxDP=max(DP_geno)"
    
    Calculating phenotype: 100% [===============================] 60 29.8/s in 00:00:02
    INFO: 180 values of 3 phenotypes (0 new, 3 existing) of 60 samples are updated.



    % vtools show samples -l 10
    
    sample_name filename        sex race    sample_total    sample_alt  sample_homo sample_het  sample_double_het   meanDP              minDP   maxDP
    NA06985     CEU_hg38.vcf    F   1       292             110         40          30          0                   2.2705479452054793  0.0     12.0
    NA06986     CEU_hg38.vcf    M   1       292             126         31          64          0                   10.736301369863014  0.0     29.0
    NA06994     CEU_hg38.vcf    F   1       292             131         37          57          0                   5.815068493150685   0.0     16.0
    ... ...
    NA12873     CEU_hg38.vcf    F   1       288             137         37          63          0                   3.952054794520548   0.0     16.0
    NA12874     CEU_hg38.vcf    M   1       292             101         30          41          0                   3.886986301369863   0.0     14.0


</details>



#### 2.4 Output selected phenotypes using option `--output`

The basic form of `vtools phenotype --output` is very similar to command `vtools show phenotypes`. They can both display all or a specified subset of phenotypes. 

<details><summary> Examples: Output specified phenotypes</summary> 
    
    % vtools phenotype --from_file phenotype.txt BMI
    % vtools phenotype --output sample_name BMI -l 10
    
    NA06985 19.64
    NA06986 NA
    NA06994 19.49
    NA07000 21.52
    NA07037 23.05
    ...
    

</details>

The power of command `vtools phenotype --output`, similar to `vtools output`, is its ability to output summary statistics of phenotypes. For example, you can use item `avg(meanDP)` to display the average of the `meanDP` field. Because pehnotype `meanDP` records average depth of all genotypes each sample, `avg(meanDP)` displays average depth of all genotypes of all samples. 

<details><summary> Examples: Output summary statistics of phenotypes</summary> 

For example, the following command outputs the wildtype genotype counts and BMI for each sample. 



    % vtools phenotype --output "count(filename)"
    
    60
    

    % vtools phenotype --output "avg(meanDP)"
    
    4.561244292237443
    

</details>