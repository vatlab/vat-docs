
+++
title = "ChangeLog"
weight = 1
+++


## Change Log of variant tools 



### 1. Version 2.7.0 (Released on Jan 20, 2016)

MAJOR NEW FEATURES: 

*   Normalize variants using reference sequence information before importing variants. 
*   New file format for spec file of variant pipeline tools. 
*   Support arbitrary reference genome. 

BUG FIXES: 

*   Fix importing wildtype genotypes in some cases. 



### 2. Version 2.6.1 (Released on Jan 15, 2015)

*   Fix a few small bugs introduced in 2.6.0. 
*   Fix compatibility issues with Python 3. 



### 3. Version 2.6.0 (Released on Dec 15, 2014)

NEW FEATURES: 

*   Major cleanup of the pipeline code (`vtools execute` and `vtools simulate`), especially for the pipeline action interface. 
*   Add command `vtools show actions` and `vtools show action ACTION`. 
*   Select annotation databases automatically (the latest version for project annotation database) for command `vtools use annoDB` when no version information is given. 



### 4. Version 2.5.1 (Released on Nov 10, 2014)

BUG FIX: 

*   Nov 1st: Fix the handling of runtime option `temp_dir` 

NEW FEATURES: 

*   Nov 3rd: Add function `in_table`. 



### 5. Version 2.5.0 (Release on Oct 15, 2014)

MAJOR NEW FEATURE: 

*   Oct 2nd: Implement a mirrored file distribution system so that users can download resources from multiple servers. 
*   Oct 5th: Add `site_options.py` to allow system administrator to set up site-wide resource directory for variant tools users. 

NEW FEATURES: 

*   Oct 5th: Add md5 signature of database files to `.ann` files and re-decompress `.DB.gz` files if the decompressed `.DB` files are corrupted. 



### 6. Version 2.4.1 ((Released on August 20, 2014))

BUG FIX: 

*   Fix a python2/3 compatibility bug that prevents vtools from working properly under python2. 



### 7. Version 2.4.0 (Released on August 15, 2014)

MAJOR NEW FEATURE: 

*   June 10: Variant Simulation Tools is introduced to simulate genetic samples with common and rare variants. 

NEW FEATURE: 

*   Mar 13: Allow the specification of a header using option `--header` for command `vtools phenotype --from_file`. 
*   May 15: Progress bar for saving and loading snapshots. 
*   May 15: Use faster compression for local compressed snapshots. 
*   May 20: Add option `--translate` to command to output protein sequence of genes in specified region. 
*   Jun 5: Allow the execution of many information-based commands such as `vtools show annotations` without a project. 
*   Jun 26: New features in pipeline allows definitions of multiple steps using one section. 
*   July 5th: Add option `--build` to command `vtools init` 

BUGS: 

*   June 5: Allow the use of function `genotype()` when one or more samples do not have genotype. 



### 8. Version 2.3.0 (Released on Feb 27, 2014)

BUGS: 

*   Jan 26: Fix a bug with pipeline functor `DecompressFiles` when the input tar file contains directories. 
*   Feb 22: Fix a bug with wildcard match with table names having special characters such as `(` or `)`. 

NEW FEATURE: 

*   Feb 19: Add option `--expression` to command `vtools compare`. 
*   Feb 20: Add pipelines `filtering` to identify recessive and de novo mutations in families with unaffected parents and an affected offspring. 
*   Feb 20: Allow the use of snapshot files (or name of online snapshot name) as `--child` or `--parent` in command `vtools init`. 
*   Feb 22: Keep a copy of original variant tables when merging projects. 



### 9. Version 2.2.0 (Released on Jan 16, 2014)

MAJOR NEW FEATURES: 

*   Jan 12, 2014: Add parameters `type`, `show_seq`, `delimiter`, `limit` and `strand` to `track()` function for bam tracks. 
*   Dec 4nd: Add command `vtools admin --validate_sex` to check sample sex using genotypes on sex chromosomes. 
*   Dec 3nd: Add command `vtools_report inbreeding_coefficient` to compute individual level inbreeding coefficient, the F-statistic. 
*   Nov 15: Add sub-commands `plot_fields`, `plot_geno_fields` and `plot_pheno_fields` to `vtools_report`. These commands generate summary plots for specified variant/genotype/sample information. 
*   Dec 2nd: Add special function `maf()` to command `vtools update --from_stat` to calculate minor allele frequency. 

NEW FEATURES: 

*   Jan 16, 2014: Update gwas catalogue annotation database. 
*   Jan 16, 2014: Add annotation databases for Database of Genomic Variation (DGV). 
*   Jan 10, 2014: Add population-specific hapmap frequency annotations. 
*   Jan 6th, 2014: Add pipeline `import_vcf` to import all variant and genotype info from vcf file. 
*   Jan 6th, 2014: Add pipeline `anno_utils.annFileFromVcf` to make it easier to create an annotation database from vcf files. 
*   Nov 22: Add an annotation database for expanded exome regions of the Illumina Nextera Rapid Capture Expanded Exome Enrichment Kits. 
*   Nov 29: Add KING pipeline to perform global ancestry and kinship analysis. 

BUG FIXES: 

*   Jan 8: Do not abort `vtools remove genotypes` if genotypes from one of the samples fail to remove. 
*   Jan 4: Fix a multi-processing bug with functor `FieldFromDb`. 
*   Dec 2: Fix a regression bug for online vcf track. 
*   Nov 14: Fix the use of annotation field if the annotation database has the same name of a variant table. 
*   Nov 18: Fix import PLINK format to allow for arbitrary coding for unknown "sex" status in `fam` file. 
*   Nov 20: Properly handle meta analysis input with trailing white space in column names. 
*   Nov 27: Properly handle missing data in external weight for $vtools associate command. 



### 10. Version 2.1.0 (Released on Nov. 6th)

MAJOR NEW FEATURES: 

*   Nov 4: Add option `--as` to command `vtools use`, which allows the use of multiple versions of the same annotation databases. 
*   Oct 25: Add SQL function `samples()` to output samples that contain the variants. 
*   Oct 21: Add SQL function `genotype()` to output genotypes that contains the variants. 

NEW FEATURES: 

*   Nov 6: Add option `all=1` to parameter `field` of `track()` function and deprecate the third option. 
*   Oct 30: Add pipelines `ANNOVAR` and `snpEff` to facilitate the use of `ANNOVAR` and `snpEff` to get variant effect estimate. 
*   Oct 25: Allow the use of wildcast characters in the first (`filename`) parameter of the `track` function. 
*   Oct 22: Add descriptions to fields added to the project using command `vtools update --from_stat` and `vtools update --set`. 
*   Oct 22: Add option `--delimiter` to command `vtools associate`. 
*   Oct 17: Handle missing phenotypes more cleverly. 
*   Oct 10: Allow the output read tags and use of tags for read filtering in the track function of BAM tracks. 

BUGS: 

*   Oct 24: Fix a bug that caused misalignment of reads in the output of BAM track when the reads are clipped in CIGAR string. 
*   Oct 11: Fix a bug related to exporting a large number of samples (> 60) in vcf format. 



### 11. Version 2.0.1 (Released on Oct 7th, 2013)

NEW FEATURES: 

*   Oct 5: Update dbNSFP to version 2.1. 
*   Oct 3: align columns of output of command `vtools output` and `vtools show genotypes` using variable spaces. 
*   Sep 23: Save ${local_resource} in annoDB to increase portability of projects. 
*   Sep 2: Expand command `vtool compare` to compare location and genotypes as well. 

BUGS: 

*   Oct 5: Fix the vcf exporter for multiple variants at the same location. 
*   Oct 4: Fix indel track mismatch for vcf track files because position adjustment for indels. 
*   Oct 2: Fix a deadlock bug for flag info when using vcf track. 
*   Sep 18: Fix a bug in `vtools admin --merge_samples`. 
*   Sep 23: Fix a crash caused by unrecognized chromosome name or out of range positions in function `ref_sequence`. 
*   Sep 25: Fix a bug related to the use of arbitrary table name in command `vtools update`. 



### 12. Version 2.0.0 (Released on Aug. 27, 2013)

MAJOR NEW FEATURE: 

*   Aug. 15: Add function `track` to annotate variants using vcf, bigWig and bigBed tracks. 
*   Jun. 28: Add command `vtools execute pipeline` to execute variant tools pipelines. 
*   July 13: Add option `--all` to `vtools output`, `vtools select --output` and `vtools export` to remove duplicated lines without sorting output. 

NEW FEATURE: 

*   Aug. 14: Add item `fmt` to field definitions used to output fields. 
*   Aug. 14: Add functors `InfoFormatter` and `FlagFormatter` to output fields in vcf format. 
*   Aug. 13: Add SQL functions `ref_sequence`. 
*   Aug. 12: Add runtime option check_update. 
*   Jul. 11: Allow .ann files to use preprocessor to process files before importing. 
*   Jul. 11: Add a preprocessor `Dos2Unix` to convert files with `\r` as newline character to unix format. 
*   Jul. 10: Change the output of `vtools show table TABLE` to make it more informative. 
*   Jul. 5: Allow exporting genotypes in format csv. 
*   Jun. 29: Add a feature that allows `vtools admin --rename_samples COND NAME1 NAME2` to rename samples by replacing the first incidence of `NAME1` in selected samples to `NAME2`. 
*   Jun. 29: Add annotation database [genomicSuperDups][1] and [phast cons elements][2] 
*   May 24: Check duplicate genotypes after samples are imported. 
*   Jun. 25: Allow importing csv files for command `vtools phenotype --from_file`. 
*   Jun. 25: Add command `vtools show phenotypes P1 P2`. 
*   Jun. 25: Allow command `vtools show samples` to show a selected list of samples. 



### 13. Version 1.0.6 (Released on May 16th, 2013)

NEW FEATURE: 

*   May 16: Allow the merge of projects with different phenotypes. 
*   May 14: Adding a few fields to vcf.fmt for Illumina data. 
*   May 6: Extend `vtools update --from_file` to update genotype info from non-original input file, and without genotype. 
*   Apr. 15: Allow the use of wildcard characters in command vtools compare 
*   Apr. 22: Allow the merge of project with different variant tables and fields 

BUG FIXES: 

*   May 16: Allow the use of non-ascii table name in commands `vtools export` and `output`/ 
*   May 15: Remove statistics missing from vtools phenotype because it is not meaningful. 
*   May 10: Fix runtime variable `local_resource` 
*   May 10: Fix importing data in binary plink format. 



### 14. Version 1.0.5 (Released on Mar. 20, 2013)

NEW FEATURES: 

*   March, 2013: Allow the use of arbitrary characters in name of variant tables. 
*   March, 2013: Add command vtools admin --update_resource to download all relevant resources. 
*   March 18, 2013: Add command vtools_report sequence to output nucleotide sequence at specified chromosome region. 

BUG FIXES: 

*   Feb 26, Fix a bug with command `vtools select --samples` when there are more than 50 specified samples. 



### 15. Version 1.0.4 (Released on Feb 22, 2013)

NEW FEATURES: 

*   Oct 20, 2012: Allow users to list and download online snapshots, which are used for training and documentation purposes. 
*   Oct 20, 2012: Use colors to differentiate debug, info, warning and error message. 
*   Nov 2, 2012: Define runtime option local_resource and use resources from this directory first. 
*   Nov 3, 2012: Add command `vtools admin --validate_build`. 



### 16. Version 1.0.3 (Released on Sep 21, 2012)

NEW FEATURES: 

*   Jul 11, 2012: Add command `vtools admin --reset_runtime_option` and `vtools show runtime_options`. 
*   Jul 4, 2012: Reorganize the association test to improve the efficiency of `vtools associate`. 
*   Jun 16, 2012: Reorganize the import process to substantially improve the efficiency of `vtools import` when it is used to import files with a large number of samples. 
*   Jun 15, 2012: Add command `vtools admin --rename_table` and `vtools admin --describe_table` to change the name and meta information of variant tables. 
*   Jun 12, 2012: Allow a comment string when a variant table is created from command `vtools select`, `vtools exclude`, and `vtools compare`. 
*   May 21, 2012: Add [Exact Tests of Hardy-Weinberg Equilibrium][3] and Fisher's exact test for case/ctrl associations to `vtools update` 
*   May 12, 2012: Add command `vtools admin`. 
*   Jan 27, 2012: Analyze project database automatically (if needed) to improve the performance of queries. 
*   Feb 29, 2012: Completion of the interface of command `vtools associate` 
*   Mar 1, 2012: add output formatting options `--header`, `--na`, `--delimiter` and `--limit` to `vtools phenotype` 
*   Mar 5, 2012: add parameter `--genotypes` to command `vtools init --parent`. (This option was defined but not implemented). 

BUGS: 

*   Jan 27, 2012: Correctly handle missing data when exporting genotype in TPEF format 
*   Feb 9, 2012: Allow the use of single field name (e.g. ccdsid instead of dbNSFP.ccdsid) for parameter `--linked_by` of command `vtools use` 
*   Feb 17, 2012: Fix a bug with exporting deletion in vcf format, for python2 version of variant tools. 



### 17. Version 1.0.2 (released on Jan 24, 2012)

NEW FEATURES: 

*   Jan 4, 2012: add parameter `--style` to format tped to allow output of genotype in numeric style 
*   Jan 4, 2012: allow command `vtools phenotype --from_stat` to use conditions that involve variant tables in the project. 
*   Jan 23, 2012: Add a new import format map. A new functor is created to retrieve reference and alternative alleles from dbSNP. 

BUGS: 

*   Jan 11, 2012: Fix a bug that prevents the removal of genotype in command `vtools remove variant` if the genotype tables are not indexed. 
*   Jan 11-13, 2012: Fix the use of vtools_report under python 3. 
*   Jan 17, 2012: Fix the use of annotation database when exporting in TPED format. 
*   Jan 23, 2012: Remove the use of COLLATE in a query to avoid potential compatibility problems. 
*   Jan 23, 2012: Fix a bug that causes duplicate output in commands `vtools output` and `vtools export`. 
*   Jan 23, 2012: Fix a bug for the detection of the existence of indexes. 



### 18. Version 1.0.1 (released on Jan 2nd, 2012)

NEW FEATURES: 

*   Nov 20, 2011: associate command can now be executed under python 3 
*   Nov 27, 2011: Add entry `encoding` to `.ann` and `.fmt` in order to import files with non-ascii characters 
*   Dec 06, 2011: Give a warning when duplicated records are outputted 
*   Dec 13, 2011: Stop altering user-provided headers for command `vtools output`. 
*   Dec 13, 2011: Add a parameter `--order_by` to order output from commands `select`, `exclude` and `output`. 
*   Dec 13, 2011: Add a new format `csv.fmt` in order to output fields in csv format (with properly quoted fields) 
*   Dec 14, 2011: Add a keyword `sort_output_by` to file format specification in order to sort variants by specified fields. 
*   Dec 14, 2011: Allow command `vtools output` to read a header from standard input using option `--header -`. 
*   Dec 15, 2011: Add parameters `anno_type` and `linked_fields` to command `vtools use` in order to allow the flexibility of how an annotation database it linked. 
*   Dec 15, 2011: Beautify output of `vtools show` when there are multiple variant tables and annotation databases. 
*   Dec 15, 2011: Adding a new interface for command `vtools compare` and allow the comparison of more than two tables, using new parameters `--intersection`, `--difference`, and `--union`. The old interface still exits and functional, but has been marked as deprecated. 
*   Dec 28, 2011: Allow the use of wildcard characters `?` and `*` in table names in command `vtools remove tables`. 

DEPRECATED: 

*   Dec 14, 2011: Parameter `filename` for command `vtools export` is deprecated. Using a pipe to save output to a file is recommended. 
*   Dec 15, 2011: Parameter `--A_and_B`, `--A_or_B`, `--A_diff_B`, and `--B_diff_A` are deprecated. Parameters `--intersection`, `--difference`, and `--union` should be used instead. 
*   Dec 29, 2011: Use of name 'field annotation database' instead of 'attribute annotation database' for consistency considerations. Both names are however allowed in .ann file for backward compatibility considerations. 

BUGS: 

*   Dec 15, 2011: Fix a bug when number of genotype is counted when one or more samples do not have genotype field `GT`. 
*   Dec 15, 2011: Fix a bug where `vtools update table --set FIELD=NULL` fails because variant tools cannot determine the type of the RHS value. This should be allowed when the LHS is an existing field. 
*   Jan 1, 2012: Fix `vtools export --format vcf` for the output of genotype when there are two different alternative alleles. 

REGRESSIONS: 

*   Dec 14, 2011: parameter `--header` of command `vtools export` is redesigned to work similarly to parameter `--header` of the `vtools output` command. 

INTERNAL IMPROVEMENTS: 

*   Nov 17, 2011: Improve efficiency of commands `vtools compare` by using direct SQL query in the case of `--verbosity 0` 
*   Nov 17, 2011: Improve efficiency of `vtools remove variants` by creating indexes for genotype tables before removing variants. 
*   Nov 25, 2011: Improve efficiency of `vtools select` by creating indexes of relevant fields of the annotation database. 
*   Dec 28, 2011: Improve efficiency of commands `vtools select` for ranged based queries by creating auxiliary binning tables.

 [1]: /vat-docs/applications/annotation/regions/genomic_super_dups/
 [2]: /vat-docs/applications/annotation/regions/phast_cons/
 [3]: /vat-docs/documentation/vtools_commands/update/