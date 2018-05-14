+++
title = "compare"
description = ""
weight = 10
+++


# Compare two or more variant tables



## Usage

    % vtools compare -h
    

    usage: vtools compare [-h] [--union [TABLE [DESC ...]]]
                          [--intersection [TABLE [DESC ...]]]
                          [--difference [TABLE [DESC ...]]]
                          [--expression EXPR [DESC ...]]
                          [--mode {variant,site,genotype}]
                          [--samples [SAMPLES [SAMPLES ...]]] [-v {0,1,2}]
                          [tables [tables ...]]
    
    Get the difference, intersection and union of two or more variant tables,
    according to sites, variants, or genotypes of associated samples of these
    variants. Resulting variants can be counted or write to other variant tables.
    
    positional arguments:
      tables                variant tables to compare. Wildcard characters * and ?
                            can be used to specify multiple tables. A table name
                            will be automatically repeated for the comparison of
                            genotype of multiple samples if only one table is
                            specified.
    
    optional arguments:
      -h, --help            show this help message and exit
      --union [TABLE [DESC ...]]
                            Print the number (default) or save variants with TYPE
                            in the TYPE of any of the tables (T1 | T2 | T3 ...) to
                            TABLE if a name is specified. An optional message can
                            be added to describe the table.
      --intersection [TABLE [DESC ...]]
                            Print the number (default) or save variants with TYPE
                            in the TYPE of all the tables (T1 & T2 & T3 ...) to
                            TABLE if a name is specified. An optional message can
                            be added to describe the table.
      --difference [TABLE [DESC ...]]
                            Print the number (default) or save variants with TYPE
                            in the TYPE of the first, but not in the TYPE of
                            others (T1 - T2 - T3...) to TABLE if a name is
                            specified. An optional message can be added to
                            describe the table.
      --expression EXPR [DESC ...]
                            Evaluate a set expression with table names
                            representing variants in these tables. Operators |
                            (or), & (and), - (difference) and ^ (A or B but not
                            both) are allowed. The results will be saved to table
                            if the result is assigned to a name (e.g. --expression
                            'D=A-(B&C)'). The table names in the expression can be
                            written as _1, _2 etc if tables are listed before the
                            option, and be used to populate the list of tables if
                            it was left unspecified.
      --mode {variant,site,genotype}
                            Compare variants (chr, pos, ref, alt), site (chr,
                            pos), or genotype (chr, pos, ref, alt, GT for a
                            specified sample) of variants. The results are
                            variants from all input tables that match specified
                            condition. The default comparison TYPE compares
                            variants in input variant tables. For the comparison
                            of sites, the position of all variants are collected
                            and compared, and variants (in all tables) with site
                            in resulting set of sites are returned. For the
                            comparison of genotypes, the genotypes of specified
                            samples for all variants (see option --samples) are
                            collected and compared, and variants with genotype in
                            resulting set of genotypes are returned. The results
                            of genotype comparisons are affected by runtime option
                            treat_missing_as_wildtype because items with missing
                            genotype (chr, pos, ref, alt, NULL) are excluded if
                            treat_missing_as_wildtype is false (default), and are
                            treated as (chr, pos, ref, alt, 0) otherwise. The
                            default comparison type is variant, or genotype if
                            option --samples is specified.
      --samples [SAMPLES [SAMPLES ...]]
                            A list of sample names corresponding to the variant
                            tables to compare. An error will be raised if a sample
                            name matches no or multiple samples or if a sample
                            does not have any genotype.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).
    
    



## Details

Command `vtools compare` compares variants in two or more variant tables. In the basic form, this command identifies variants that appear in one table but not others (set difference), in one or the tables (set union), or in all tables (set intersection). The results can be counted or written to a variant table. 

The items being compare in this case are variants (namely `chr`, `pos`, `ref`, and `alt`), which can be reduced to sites (`chr` and `pos`), or expanded to genotypes of specified samples (`chr`, `pos`, `ref`, `alt`, and `GT` of an associated sample). The results are variants (from all involved tables) that belong to the resulting sites or genotypes. 



### Compare variants in variant tables

<details><summary> Examples: Load a sample project and create a few variant tables</summary> 

    % vtools init compare
    % vtools admin --load_snapshot vt_simple
    % vtools use refGene_exon-hg18_20110909
    % vtools use dbSNP-hg18_130
    % vtools select variant 'dbSNP.chr IS NOT NULL' -t inDbSNP 'In dbSNP database'
    % vtools select variant 'refGene_exon.chr IS NOT NULL' -t exonic 'In exonic regions of ref seq genes'
    % vtools select variant 'refGene_exon.name2 == "AGRN"' -t G_AGRN 'In gene AGRM'
    % vtools select variant 'refGene_exon.name2 == "FAM41C"' -t G_FAM41C 'In gene FAM41C'
    

</details>

In the default 'variant' comparison type, command `vtools compare` compares variants in two or more tables and look for variants that in one, all, or none of the tables. It either counts and prints the number of matching variants or write the variants to a variant table. For example, if the master variant table has 4 variants, and when we compare variant tables `T1` and `T2`, 



| **variant** | **tables** |
||
| **chr**     | **pos**    | **ref** | **alt** | T1 | T2 |
| 1           | 31705      | A       | G       | ✓  | ✓  |
| 1           | 50195      | T       | C       | ✓  |    |
| 1           | 50195      | T       | G       |    | ✓  |
| 1           | 50589      | C       | A       |    | ✓  |

The number of variants for each type of comparison would be 



    % vtools compare T1 T2 
    

    INFO: Reading approximately 2 variants in T1...
    INFO: Reading approximately 3 variants in T2...
    INFO: Number of variants in A but not B, B but not A, A and B, and A or B
    1	2	1	4
    

for variants `B`, `C` and `D`, `A`, and all four variants for the counts, if we name the four variants as variants `A`, `B`, `C`, and `D`. 

<details><summary> Examples: Compare two variant tables </summary> The project has a few variant tables that can be listed by command `vtools show tables` 

    % vtools show tables
    

    table       #variants     date message
    G_AGRN             24    Jul15 In gene AGRM
    G_FAM41C           51    Jul15 In gene FAM41C
    exonic            151    Jul15 In exonic regions of ref seq genes
    inDbSNP             9    Jul15 In dbSNP database
    variant         1,611
    

Variants that are in dbSNP database is in table `inDbSNP`. If you would like to get a list of variants that are not in dbSNP, you can do 



    % vtools compare variant inDbSNP --difference notInDbSNP 'variants that are not in dbSNP'
    

    INFO: Reading 1,611 variants in variant...
    INFO: Reading 9 variants in inDbSNP...
    Writing to notInDbSNP: 100% [===============================] 1,602 68.7K/s in 00:00:00
    

Or, you can check what variants in the `AGRN` table are exonic 

    % vtools compare G_AGRN exonic --intersection AGRN_exonic 'Exonic variants in gene AGRN'
    

    INFO: Reading 24 variants in G_AGRN...
    INFO: Reading 151 variants in exonic...
    Writing to AGRN_exonic: 100% [==================================] 24 1.7K/s in 00:00:00
    

If you only need to check the number of exonic variants in gene AGRN, you can use the `--intersection` option without parameter, 



    % vtools compare G_AGRN exonic --intersection
    

    INFO: Reading 24 variants in G_AGRN...
    INFO: Reading 151 variants in exonic...
    24
    

You can also get the number of variants that are not exonic, and in both tables etc using similar options, but a shortcut to get all counts is 

    % vtools compare G_AGRN exonic 
    

    INFO: Reading 24 variants in G_AGRN...
    INFO: Reading 151 variants in exonic...
    INFO: Output number of variants in A but not B, B but not A, A and B, and A or B
    0	127	24	151
    

</details>

More than two variant tables can be specified. Option `--intersection` and `--union` will select variants that belong to all or any of all tables, respectively. Option `--difference` will select variants that are in the first, but not in any of the rest of the tables (` A - B - C - D ...`). 

<details><summary> Examples: Comparing more than two tables</summary> 

    % vtools compare exonic 'G_*' --difference other 'Exonic variants not in AGRN and FAM41C'
    

    INFO: Reading 151 variants in exonic...
    INFO: Reading 24 variants in G_AGRN...
    INFO: Reading 51 variants in G_FAM41C...
    Writing to other: 100% [========================================] 76 5.2K/s in 00:00:00
    

</details>



This command allows the use of wildcard characters * and ? in the specification of table names, which can be handy if you have a large number of variant tables for, e.g. variants in a list of genes. 

Now, if you have more complex expressions that involve more than one types of set operations, you can use option `--expression` for it. For example 



    % vtools compare --expression 'A-(B|C)'
    

print out the number of variants in table `A`, but not in `B` or `C`. The allowed operations are 



*   `A | B`: In table `A` or `B` (`--union`) 
*   `A & B`: In table `A` and `B` (`--intersection`) 
*   `A - B`: In table `A` but not in `B` (`--difference`) 
*   `A ^ B`: In table `A` or `B` but not in both (`(A|B)-(A&B)`). 

If you need to save the result to a table, you can assign the expression to a table name, 



    % vtools compare --expression 'D=A-(B|C)' 'variants in A but not in B or C'
    

If you have a table with non-alpha-numeric characters, you should quote it inside the expression using either single or double quotes, for example, 



    % vtools compare --expression 'D="@TP32"-( B | C)'
    

Note that these commands are simplified version of 



    % vtools compare "@TP32" B C --expression 'D="@TP32"-( B | C)'
    

and if you do list the tables before the option, you could use `_1`, `_2` etc in place of table names, 



    % vtools compare "@TP32" B C --expression 'D=_1 - ( _2 | _3)' --union all_variants
    

This syntax is recommended if you would like to perform multiple operations for the same set of tables (e.g. `--expression` and `--union` in the above example), or if you would like to compare variants by genotypes, in which case a sample should be specified for each table. 

<details><summary> Examples: Use set expression to compare multiple tables</summary> 

If we would like to exclude variants that are not in DBSNP, but keep those in exonic regions, we can run 



    % vtools compare --expression 'variant - inDBSNP | exonic'
    

    INFO: Comparing tables variant, inDBSNP, exonic
    INFO: Reading 1,611 variants in variant...
    INFO: Reading 896 variants in inDBSNP...
    INFO: Reading 76 variants in exonic...
    785
    

This command is equivalent to 



    % vtools compare inDBSNP exonic variant --expression '_3 - _1 | _2'
    

    INFO: Reading 896 variants in inDBSNP...
    INFO: Reading 76 variants in exonic...
    INFO: Reading 1,611 variants in variant...
    785
    

Let us conclude this example with an expression that does not make much sense 



    % vtools compare --expression 'variant - (inDBSNP & exonic ^ G_AGRN) | G_FAM41C'
    

    INFO: Comparing tables variant, inDBSNP, exonic, G_AGRN, G_FAM41C
    INFO: Reading 1,611 variants in variant...
    INFO: Reading 896 variants in inDBSNP...
    INFO: Reading 76 variants in exonic...
    INFO: Reading 11 variants in G_AGRN...
    INFO: Reading 2 variants in G_FAM41C...
    1550
    

</details>



### Compare genotypes of multiple samples

If parameter `--samples` is specified, command `vtools compare` compares genotypes of specified samples. Although we usually compare all genotypes of samples using a command similar to (e.g. genotypes in `SAMP1` and `SAMP2` with variants in table `variant`) 



    % vtools compare variant --samples SAMP1 SAMP2 
    

you can compare a subset of genotypes using command 



    % vtools compare exonic --samples SAMP1 SAMP2 
    

or even different variants from each sample, as in 



    % vtools compare var1 var2 --samples SAMP1 SAMP2 
    

In these cases, genotypes that belong to specified variant table are selected and compared, and variants that belong to the resulting set of genotypes are returned. 

For example, suppose the master variant table `variant` has the following 4 variants, and two samples both have 2 genotypes, 



| **variant** | **genotypes** |
||
| **chr**     | **pos**       | **ref** | **alt** | **GT** of SAMP1 | **GT** of SAMP2 |
| 1           | 31705         | A       | G       | 2               | .               |
| 1           | 50195         | T       | C       | .               | .               |
| 1           | 50195         | T       | G       | 1               | 1               |
| 1           | 50589         | C       | A       | .               | 1               |

The first command would yield results 



    % vtools compare variant --samples SAMP1 SAMP2 
    

    INFO: Reading genotype of sample SAMP1 of approximately 4 variants in variant...
    INFO: Reading genotype of sample SAMP2 of approximately 4 variants in variant...
    INFO: Number of genotypes in A only, B only, in A and B, and in A or B
    INFO: 1	1	1	3
    INFO: Number of variants with genotypes in A only, B only, in A and B, and in A or B
    1	1	1	3
    

with variants `A` (for genotype `A2`), `D` (for genotype `D1`), `C` (for genotype `C1`), and `A,C,D` (for genotypes `A2`, `C1`, and `D1`) for the four counts, if we name the four variants A, B, C, and D. 

The result of such comparisons, however, is affected by runtime option `treat_missing_as_wildtype`. If we run 



    % vtools admin --set_runtime_option treat_missing_as_wildtype=1
    

    INFO: Option treat_missing_as_wildtype is set to True
    

The output of command changes to 



    % vtools compare variant --samples SAMP1 SAMP2 
    

    INFO: Reading genotype of sample SAMP1 of approximately 4 variants in variant...
    INFO: Reading genotype of sample SAMP2 of approximately 4 variants in variant...
    INFO: Number of genotypes in A only, B only, in A and B, and in A or B
    INFO: 2	2	2	6
    INFO: Number of variants with genotypes in A only, B only, in A and B, and in A or B
    2	2	2	4
    

with variants `A` and `D` (for genotypes `A2` and `D0`), `A` and `D` (for genotypes `A0` and `D1`), `B` and `C` (for genotypes `B0` and `C1`), and `A`, `B`, `C`, `D` (for genotypes `A0`, `A2`, `B0`, `C1`, `D0`, and `D1`) for the four counts. 

Although it is a bit confusing to return variants for a comparison of genotypes, this command is very useful to compare genotypes of two or more samples. 



#### Count or output of genotypes shared by two or more samples

<details><summary> Examples: identify genotypes that are identical across samples</summary> To make use of the sample project, we need to first assign different names to different samples because all our samples share the same name: 



    % vtools show samples
    

    sample_name	filename
    SAMP1	V1.vcf
    SAMP1	V2.vcf
    SAMP1	V3.vcf
    

To do that, we can run 



    % vtools admin --rename_samples "filename = 'V2.vcf'" SAMP2
    % vtools admin --rename_samples "filename = 'V3.vcf'" SAMP3
    % vtools show genotypes
    

    sample_name	filename	num_genotypes	sample_genotype_fields
    SAMP1	V1.vcf	989	GT
    SAMP2	V2.vcf	990	GT
    SAMP3	V3.vcf	988	GT
    

The following command shows number of genotypes that are shared by all three samples, 



    % vtools compare variant --intersection --samples SAMP1 SAMP2 SAMP3
    

    INFO: Reading genotypes of sample SAMP1 of approximately 1,611 geno in variant...
    INFO: Reading genotypes of sample SAMP2 of approximately 1,611 geno in variant...
    INFO: Reading genotypes of sample SAMP3 of approximately 1,611 geno in variant...
    INFO: Genotypes in all samples: 432
    432
    

Because each variant corresponds to one genotype in this case, the number of genotypes and variants are the same. As we can see, about half of genotypes of each sample are shared with other samples. 

</details>



#### Identify genotypes that are unique to one sample

There are two cases to consider here. The first one is that the mutation might exist in another sample, but with different genotype. This can be achieved using a straigforward genotype comparison: 

<details><summary> Examples: Identify genotypes are unique in one sample</summary> 



    % vtools compare variant --difference S1 --samples SAMP1 SAMP2 SAMP3 
    

    INFO: Reading genotypes of sample SAMP1 of approximately 1,611 geno in variant...
    INFO: Reading genotypes of sample SAMP2 of approximately 1,611 geno in variant...
    INFO: Reading genotypes of sample SAMP3 of approximately 1,611 geno in variant...
    INFO: Genotypes in sample SAMP1 only: 321
    WARNING: Existing table S1 is renamed to S1_Sep03_163613.
    Writing to S1: 100% [====================================] 321 21.8K/s in 00:00:00
    

Let us have a look at the genotypes of the variants in table `S1` in the samples 



    % vtools export S1 --samples 1 --format csv | head -10
    

    INFO: Genotypes of 3 samples are exported.
    Writing: 100% [================================================================================] 321 18.1K/s in 00:00:00
    INFO: 321 lines are exported from variant table S1
    1,5683,G,T,1,NA,NA
    1,10098,G,A,2,NA,NA
    1,29539,C,T,1,NA,NA
    1,39161,T,C,1,NA,2
    1,39378,G,A,1,NA,NA
    1,44579,C,T,1,NA,NA
    1,50589,C,A,1,NA,NA
    1,54504,A,G,1,NA,NA
    1,73865,G,A,2,1,1
    1,81004,G,T,1,NA,NA
    

As you can see, table `S1` contains variants with genotypes in sample `SAMP1` and are missing or with a different genotype in other samples. 

</details>

However, if you are interested in further divide the genotypes, namely to identify genotypes that only available in one sample (missing in others), or available in all samples (not missing in others), you will have to limit the search first. 

<details><summary> Examples: Identify genotypes only exist in one sample (missing in others)</summary> To obtain genotypes are are unique in one sample (and missing in others), you need to first identify genotypes that are not missing in other samples, 



    % vtools select variant --samples "sample_name = 'SAMP1'" -t varSAMP1
    % vtools select variant --samples "sample_name = 'SAMP2'" -t varSAMP2
    % vtools select variant --samples "sample_name = 'SAMP3'" -t varSAMP3
    % vtools show tables
    

    table              #variants     date message
    G_AGRN                    11    Sep03 In gene AGRM
    G_FAM41C                   2    Sep03 In gene FAM41C
    S1                       321    Sep03
    exonic                    76    Sep03 In exonic regions of ref seq genes
    inDbSNP                  896    Sep03 In dbSNP database
    varSAMP1                 989    Sep03
    varSAMP2                 990    Sep03
    varSAMP3                 988    Sep03
    variant                1,611
    

We can then identify genotypes that only appear in `SAMP1` using command 



    % vtools compare varSAMP1 varSAMP2 varSAMP3 --difference SAMP1_only
    

    INFO: Reading 989 variants in varSAMP1...
    INFO: Reading 990 variants in varSAMP2...
    INFO: Reading 988 variants in varSAMP3...
    Writing to SAMP1_only: 100% [==================================================================] 265 14.1K/s in 00:00:00
    

The genotypes associated with `SAMP1_only` only appear in `SAMP1`, 

    % vtools export SAMP1_only --samples 1 --format csv | head -10
    

    INFO: Genotypes of 3 samples are exported.
    Writing: 100% [================================================================================] 265 15.9K/s in 00:00:00
    INFO: 265 lines are exported from variant table SAMP1_only
    1,5683,G,T,1,NA,NA
    1,10098,G,A,2,NA,NA
    1,29539,C,T,1,NA,NA
    1,39378,G,A,1,NA,NA
    1,44579,C,T,1,NA,NA
    1,50589,C,A,1,NA,NA
    1,54504,A,G,1,NA,NA
    1,81004,G,T,1,NA,NA
    1,81119,A,G,1,NA,NA
    1,81131,G,A,1,NA,NA
    

Note that the following commands cannot be used in this case 

    % vtools compare varSAMP1 varSAMP2 varSAMP3 --difference --samples SAMP1 SAMP2 SAMP3
    

    INFO: Reading genotypes of sample SAMP1 of approximately 989 geno in varSAMP1...
    INFO: Reading genotypes of sample SAMP2 of approximately 990 geno in varSAMP2...
    INFO: Reading genotypes of sample SAMP3 of approximately 988 geno in varSAMP3...
    INFO: Genotypes in sample SAMP1 only: 321
    321
    

because genotype difference cannot remove variants with different genotypes in different samples. 

</details>

<details><summary> Examples: Identify mutations that exist in all sample</summary> 

To get a list of variants that are not-missing in all samples, we need to get the intersection of all variants 



    % vtools compare varSAMP1 varSAMP2 varSAMP3 --intersection varNotMissing
    

    INFO: Reading 989 variants in varSAMP1...
    INFO: Reading 990 variants in varSAMP2...
    INFO: Reading 988 variants in varSAMP3...
    Writing to varNotMissing: 100% [===============================================================] 511 25.6K/s in 00:00:00

We can then find variants that with different genotypes in `SAMP1`: 



    % vtools compare varNotMissing --samples SAMP1 SAMP2 SAMP3 --difference SAMP1_not_missing
    

    INFO: Reading genotypes of sample SAMP1 of approximately 511 geno in varNotMissing...
    INFO: Reading genotypes of sample SAMP2 of approximately 511 geno in varNotMissing...
    INFO: Reading genotypes of sample SAMP3 of approximately 511 geno in varNotMissing...
    INFO: Genotypes in sample SAMP1 only: 7
    Writing to SAMP1_not_missing: 100% [=============================================================] 7 456.4/s in 00:00:00
    

Only 7 variants that are not missing and have unique genotype in `SAMP1` exist: 

    % vtools export SAMP1_not_missing --samples 1 --format csv 2> /dev/null
    

    1,73865,G,A,2,1,1
    1,536560,A,G,1,2,2
    1,758116,A,C,2,1,1
    1,791956,G,A,2,1,1
    1,798494,G,A,2,1,1
    1,798791,C,T,2,1,1
    1,892860,G,A,1,2,2
    

Here we redirect all progress bar etc from stderr to /dev/null to check only the output sent to standard output. 

</details>



### Compare sites of variants (ignore multiple alternative alleles)



| **site** |         | **tables** |
||
| **chr**  | **pos** | **ref**    | **alt** | T1 | T2 |
| 1        | 31705   | A          | G       | ✓  | ✓  |
| 1        | 50195   | T          | C       | ✓  |    |
| 1        | 50195   | T          | G       |    | ✓  |
| 1        | 50589   | C          | A       |    | ✓  |

The number of variants for each type of comparison would be 



    % vtools compare T1 T2 --mode site
    

    INFO: Reading locations of approximately 2 variants in T1...
    INFO: Reading locations of approximately 3 variants in T2...
    INFO: Number of sites in A only, B only, in A and B, and in A or B
    INFO: 0	1	2	3
    INFO: Number of variants in both tables with locations in A only, B only, in A and B, and in A or B
    0	1	3	4
    

for 0 variant (no location is T1 only), variant `D` (location 50589), variants `B`, `C` and `D` (location 50195 and 50589), and all variants (for locations 31705, 50195, 50589). It is interesting to note that the site-intersection of two variant tables with 2 and 3 variants respectively produces a variant table of 3 variants. 



### Example: identification of de novo mutations

In a parent - offspring setting, we are often interested in locating variants of offspring that are not inherited from his or her parents (de novo mutations). Assuming that we have a project with three samples with names `offspring`, `father` and `mother`, we can first get variants from offspring and parents using commands such as 



    % vtools select variant --samples "sample_name='offspring'" -t WGS3_1
    % vtools select variant --samples "sample_name='father'" -t WGS3_2
    % vtools select variant --samples "sample_name='mother'" -t WGS3_3
    

We can compare these three tables by genotype, variant, and site, each have different meanings. 

The easiest one is to compare variants. The following command gets a list of `113,553` variants that are only available in offspring. 



    % vtools compare WGS3_1 WGS3_2 WGS3_3 --difference by_variant
    

    INFO: Reading 4,343,418 variants in WGS3_1...
    INFO: Reading 4,367,814 variants in WGS3_2...
    INFO: Reading 4,455,890 variants in WGS3_3...
    Writing to by_variant: 100% [================================] 113,553 171.2K/s in 00:00:00
    113553
    

We can compare by genotype, that is to say, we only exclude variants that have different genotypes from the offspring. 



    % vtools compare WGS3_1 WGS3_2 WGS3_3 --difference by_genotype --samples offspring father mother
    

    INFO: Reading genotypes of sample WGS3_1 of approximately 4,343,418 geno in WGS3_1...
    INFO: Reading genotypes of sample WGS3_2 of approximately 4,367,814 geno in WGS3_2...
    INFO: Reading genotypes of sample WGS3_3 of approximately 4,455,890 geno in WGS3_3...
    INFO: Genotypes in sample WGS3_1 only: 808425
    Writing to by_genotype: 100% [=======================================================] 808,425 174.9K/s in 00:00:04
    808425
    

Or, we can exclude all variants that have any other variants at the same locations. 



    % vtools compare WGS3_1 WGS3_2 WGS3_3 --difference by_site --mode site
    

    INFO: Reading locations of approximately 4,343,418 sites in WGS3_1...
    INFO: Unique sites in table WGS3_1: 4326495
    INFO: Reading locations of approximately 4,367,814 sites in WGS3_2...
    INFO: Unique sites in table WGS3_2: 4348488
    INFO: Reading locations of approximately 4,455,890 sites in WGS3_3...
    INFO: Unique sites in table WGS3_3: 4435967
    INFO: Unique sites in table WGS3_1 only: 95373
    Writing to by_site: 100% [============================================================] 95,653 169.2K/s in 00:00:00
    95653
    

As we can see, excluding by genotype keeps the most of the variants. This should **not** be the method to use because offspring genotype can naturally be different from his or her parents (e.g. homozygote father + wildtype mother ==> heterzygote offspring). Let us see if this is the case: 



    % vtools compare by_genotype by_variant by_site --difference by_genotype_only
    

    INFO: Reading 808,425 variants in by_genotype...
    INFO: Reading 113,553 variants in by_variant...
    INFO: Reading 95,653 variants in by_site...
    Writing to by_genotype_only: 100% [==================================================] 694,872 179.9K/s in 00:00:03
    694872
    



    % vtools output by_genotype_only "genotype('offspring')" "genotype('father')" "genotype('mother')" -l 10
    

    2	1	.
    2	1	1
    2	1	.
    1	.	2
    1	2	.
    1	2	.
    1	2	.
    1	.	2
    1	2	.
    2	1	.
    

We can see that the variants have offspring genotypes that are different from his or her parents. It is strange that we observe a few homozygotes when only one of the parents have heterozygotes of this genotype. This can be due to variant calling errors that should be validated from original sources (e.g. check bam files). 

Site-difference produces a list that is a strict subset of varant-difference, as confirmed by 



    % vtools compare by_site by_variant
    

    INFO: Reading approximately 95,653 variants in by_site...
    INFO: Reading approximately 113,553 variants in by_variant...
    INFO: Number of variants in A but not B, B but not A, A and B, and A or B
    0	17900	95653	113553
    

but what exactly are the differences? Let us check the genotypes at these variant-only variants: 



    % vtools compare by_variant by_site --difference by_variant_only
    

    INFO: Reading 113,553 variants in by_variant...
    INFO: Reading 95,653 variants in by_site...
    Writing to by_site_only: 100% [=======================================================] 17,900 180.6K/s in 00:00:00
    17900
    

We can only confirm that these variants do not have any genotype for father and mother. 



    % vtools output by_variant_only "genotype('offspring')" "genotype('father')" "genotype('mother')" -l 10
    

    1 	.	.
    1 	.	.
    1 	.	.
    -1	.	.
    -1	.	.
    1 	.	.
    1 	.	.
    1 	.	.
    2 	.	.
    -1	.	.
    

Then, how can we find variants that share the same locations as these in table `by_variant_only`. This is a little bit tricky but we can achive it in two steps: The first step finds all variants that do not share location with the variants of interest, and the second step find the complement of them. 



    % vtools compare variant by_variant_only --difference not_at_variant_site --mode site
    

    INFO: Reading locations of approximately 10,126,300 sites in variant...
    INFO: Unique sites in table variant: 8725216
    INFO: Reading locations of approximately 17,900 sites in by_variant_only...
    INFO: Unique sites in table by_variant_only: 17728
    INFO: Unique sites in table variant only: 8707488
    Writing to not_at_variant_site: 100% [=============================================] 8,978,176 182.3K/s in 00:00:49
    8978176
    



    % compare variant not_at_variant_site --difference at_variant_site
    

    INFO: Reading 10,126,300 variants in variant...
    INFO: Reading 8,978,176 variants in not_at_variant_site...
    Writing to at_variant_site: 100% [====================================================] 61,905 172.0K/s in 00:00:00
    61905
    

As we can see, there are `61905` variants that share the same sites with `17900` variants of interest. To confirm this, 



    % vtools compare by_variant_only at_variant_site
    

    INFO: Reading approximately 17,900 variants in by_variant_only...
    INFO: Reading approximately 61,905 variants in at_variant_site...
    INFO: Number of variants in A but not B, B but not A, A and B, and A or B
    0	44005	17900	61905
    



    % vtools compare by_variant_only at_variant_site --mode site
    

    INFO: Reading locations of approximately 17,900 variants in by_variant_only...
    INFO: Reading locations of approximately 61,905 variants in at_variant_site...
    INFO: Number of sites in A only, B only, in A and B, and in A or B
    INFO: 0	0	17728	17728
    INFO: Number of variants in both tables with locations in A only, B only, in A and B, and in A or B
    0	0	61905	61905
    



    % vtools output at_variant_site chr pos "genotype('offspring')" "genotype('father')" \
        "genotype('mother')" ref alt --order_by chr pos -l 20
    

    1	54721 	1	.	.	T    	-
    1	54721 	.	.	1	TTTCT	-
    1	817121	1	.	.	-    	CTTTAAGATTCAACCTGAA
    1	817121	.	.	1	-    	TTACCTTTAAGATTCAACCTGAA
    1	817121	.	.	1	-    	CTTCAAGATTCAACCTGAATAAGTC
    1	822005	1	.	.	T    	A
    1	822005	.	1	1	T    	G
    1	825767	1	.	.	-    	ACTCTGGAAGCTGAGGCAGGAGAATCACTTGAATCTGGGAGGTGGAGATTG
    1	825767	.	1	.	-    	TACTCTGGAAGCTGAGGCAGGAGAATCACTTGGACCCGAGAGGCAGAGATTG
    1	825767	.	.	.	-    	AACCCGGGAGGCAGAGATTG
    1	825767	.	.	.	-    	CCCAGCTACTCTGGAAGCTGAGGCAGGAGAATCACTTGGACCCGAGAGGCAGAGATTG
    1	884042	1	.	.	-    	GGCTGCACCCTGGTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	1	.	-    	CCCTGGTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	.	.	-    	TGCACCCTGGTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	.	1	-    	GCTGCACCCTGGTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	.	.	-    	GTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	.	.	-    	GGTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	.	.	-    	CCTGGTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	.	.	-    	GCACCCTGGTCCCCCTGGTCCCTTTGGCCCTGCA
    1	884042	.	.	.	-    	CACCCTGGTCCCCCTGGTCCCTTTGGCCCTGCA
    

It appears that most differences come from indels with different lengths. For example, both parents have mutants `T-G` at `chr1:822005` and the offspring have mutation `T->A`, and parents and offspring have different insertions at some other locations. 

In summary, when we identify offspring-only variants, the command 



    %  vtools compare WGS3_1 WGS3_2 WGS3_3 --difference by_variant
    

identifies all variants (113,553 in this example) that are available only in offspring. These include the true de novo mutations (or genotype calling errors, 95,653 in this example) idenfified by 



    %  vtools compare WGS3_1 WGS3_2 WGS3_3 --difference by_site --mode site
    

and these with different variants but at the same sites (see the output of the last command). It is up to individual analysis pipeline to determine how to handle these de novo mutations.