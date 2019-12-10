+++
title = "select"
description = ""
weight = 8
+++



## Select variants from a variant table 



### 1. Usage

    % vtools select -h

    usage: vtools select [-h] [-s [COND [COND ...]]] [-t [TABLE [DESC ...]]]
                         [-c | -o [FIELDS [FIELDS ...]]]
                         [--header [HEADER [HEADER ...]]] [-d DELIMITER] [--na NA]
                         [-l N] [--build BUILD] [-g [FIELD [FIELD ...]]] [--all]
                         [--order_by FIELD [FIELD ...]] [-v {0,1,2}]
                         from_table [condition [condition ...]]
    
    Select variants according to properties (variant and annotation fields) and
    membership (samples) of variant. The result can be counted, outputted, or
    saved to a variant table.
    
    positional arguments:
      from_table            Source variant table.
      condition             Conditions by which variants are selected. Multiple
                            arguments are automatically joined by 'AND' so 'OR'
                            conditions should be provided by a single argument
                            with conditions joined by 'OR'. If unspecified, all
                            variants (except those excluded by parameter
                            --samples) will be selected.
    
    optional arguments:
      -h, --help            show this help message and exit
      -s [COND [COND ...]], --samples [COND [COND ...]]
                            Limiting variants from samples that match conditions
                            that use columns shown in command 'vtools show sample'
                            (e.g. 'aff=1', 'filename like "MG%"').
      -t [TABLE [DESC ...]], --to_table [TABLE [DESC ...]]
                            Destination variant table.
      -c, --count           Output number of variant, which is a shortcut to '--
                            output count(1)'.
      -o [FIELDS [FIELDS ...]], --output [FIELDS [FIELDS ...]]
                            A list of fields that will be outputted. SQL-
                            compatible expressions or functions such as "pos-1",
                            "count(1)" or "sum(num)" are also allowed.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).
    
    Output options:
      --header [HEADER [HEADER ...]]
                            A complete header or a list of names that will be
                            joined by a delimiter (parameter --delimiter). If a
                            special name - is specified, the header will be read
                            from the standard input, which is the preferred way to
                            specify large multi-line headers (e.g. cat myheader |
                            vtools export --header -). If this parameter is given
                            without parameter, a default header will be derived
                            from field names.
      -d DELIMITER, --delimiter DELIMITER
                            Delimiter use to separate columns of output. The
                            default output uses multiple spaces to align columns
                            of output. Use '-d,' for csv output, or -d'\t' for
                            tab-delimited output.
      --na NA               Output string for missing value
      -l N, --limit N       Limit output to the first N records.
      --build BUILD         Output reference genome. If set to alternative build,
                            chr and pos in the fields will be replaced by alt_chr
                            and alt_pos
      -g [FIELD [FIELD ...]], --group_by [FIELD [FIELD ...]]
                            Group output by fields. This option is useful for
                            aggregation output where summary statistics are
                            grouped by one or more fields.
      --all                 Variant tools by default output only one of the
                            records if a variant matches multiple records in an
                            annotation database. This option tells variant tools
                            to output all matching records.
      --order_by FIELD [FIELD ...]
                            Order output by specified fields in ascending order,
                            or descending order if field name is followed by DESC
                            (e.g. --order_by 'num DESC')
    



### 2. Details

The basic form of command 



    vtools select table condition action
    

selects from a variant table *table* a subset of variants satisfying given *condition*, and perform an *action* of 



*   creating a new variant table if `--to_table` is specified. 
*   counting the number of variants if `--count` is specified. 
*   outputting selected variants if `--output` is specified (as if command `vtools output` is used on it). 

The *condition* should be a SQL expression using one or more fields in the project (shown in `vtools show fields`). If the *condition* argument is unspecified, then all variants in *table* will be selected. More details about the use of *conditions* could be found [here][1]. An optional condition `--samples [condition]` can also be used to limit selected variants to specified samples. 



#### 2.1 Basic usages of the command

<details><summary> Examples: Load a sample project</summary> Let us load a sample project simple from online: 

    % vtools init import --parent vt_testData_v3
    % vtools import V*_hg38.vcf --build hg38
    

The project has a master variant table with 1,611 variant, 

    % vtools show tables   

    table      #variants     date message
    variant        2,051    
    

from two samples, 

    % vtools show samples    

    sample_name filename
    SAMP1       V1_hg38.vcf
    SAMP2       V2_hg38.vcf
    SAMP3       V3_hg38.vcf
    

</details>

Variant info fields provide annotation information for all variants in a project. They are usually imported from source data using command `vtools import`, and are listed as `variant.NAME` in the output of `vtools show fields`. You can use these fields to select variants from the master variant table, or another variant table. 

<details><summary> Examples: Select variants by variant info fields</summary> This project has the following fields 

    % vtools show fields
    
    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    

This project does not have many interesting fields, but we can at least select variants by chromosome, position, reference or alternative allele. 



    % vtools select variant 'pos < 200000' -t pos_20k 'variants with position < 20000'
    
    Running: 0 0.0/s in 00:00:00                                                                   
    INFO: 91 variants selected.
    

This command write selected variants to a table `pos_20k. A message is optional but is highly recommended because it helps you remember what variants this table contains. The message will be displayed in the output of `vtools show tables` and `vtools show table TBL@@, 



    % vtools show tables
    
    table      #variants     date message
    pos_20k           91    May28 variants with position < 20000
    variant        2,051    May28 Master variant table
    

You can use multiple conditions to select tables, as in 



    % vtools select variant 'pos < 200000' 'ref="T"' -t 'pos < 20k ref=T' \
    %     'Variants with position < 20000 and with reference allele T'
    
    Running: 0 0.0/s in 00:00:00
    INFO: 22 variants selected.
    

The resulting table has a name with space and special characters `<` and `=`. Such names are allowed but should be properly quoted. If you need to specify `OR` condition, you can do 



    % vtools select variant 'pos < 200000 OR ref="T"' -t 'pos < 20k or ref=T' \
    %     'Variants with position < 20000 or with reference allele T'

    Running: 2 1.3K/s in 00:00:00
    INFO: 521 variants selected.
    

</details>


{{% notice tip %}}
Name of variant tables can contain arbitrary characters so names such as `'TRA@'` and `'AA=T'` are acceptable. You should however properly quote such names to avoid accidental shell interpretation of these names (e.g. expansion of `*` and `?`). 
{{% /notice %}}

{{% notice tip %}}
Multiple conditions are allowed and are joined by `'AND'`. You can use a single condition with `OR` to specify `OR` condition (e.g. `DP > 10 OR pos<20000`). 
{{% /notice %}}

Variant info fields can also be added by command `vtools update`. The `--from_stat` option of this command is most useful because it can calculate genotype statistics (e.g. number of genotypes, number of homozygotes etc) for each variant across all or selected samples. Such information can then be used to select variants that are, for example, singletons in the database. 

<details><summary> Examples: Select variant by genotype statistics</summary> We can add a field `num` to present the number of genotypes in three samples 

    % vtools update variant --from_stat 'num=#(GT)'
    
    Counting variants: 100% [====================================] 3 25.9/s in 00:00:00
    INFO: Adding variant info field num with type INT
    Updating variant: 100% [================================] 2,051 58.8K/s in 00:00:00
    INFO: 2051 records are updated
    

The fields are now available to the project 

    % vtools show fields

    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    variant.num (int)       Created from stat "#(GT)"  with type INT on May28
    pos_20k.chr (char)      Chromosome name (VARCHAR)
    pos < 20k ref=T.chr (char) 
                            Chromosome name (VARCHAR)
    pos < 20k or ref=T.chr (char) 
                            Chromosome name (VARCHAR)
    

and can be used to select variants. For example, the following command select variants that appear in all three samples, 

    % vtools select variant 'num=3' -t inAllSamples 'variants that are in all three samples'


    Running: 1 592.0/s in 00:00:00                                           
    INFO: 646 variants selected.
    

</details>

You do not have to select from the master variant table, and in case that you only need to saved the selected variants, you can use option `--count` to output the number of selected variants, or use option `--output` to output variants. The latter option is equivalent to saving selected variants to a table and outputting variants in that table using command `vtools output`. Please refer to command `vtools output` for details. 

<details><summary> Examples: Count or output selected variants</summary> For example, the following command count the number of variants that appear in all samples from variants in table `pos < 20k or ref=T`. 



    % vtools select 'pos < 20k or ref=T' 'num=3' -c
    
    Counting variants: 0 0.0/s in 00:00:00
    154
    

You can also have a look at these variants without saving them to a table 



    % vtools select 'pos < 20k or ref=T' 'num=3' --output chr pos ref alt num -l 10
    
    1   16103   T   G   3
    1   20144   G   A   3
    1   30860   G   C   3
    1   30923   G   T   3
    1   41842   A   G   3
    1   54380   T   C   3
    1   54490   G   A   3
    1   54676   C   T   3
    1   57999   G   T   3
    1   62203   T   C   3
    

</details>



#### 2.2 Select variants using annotation fields

You can select variants from a variant table based on fields from external annotation databases. Although annotation databases have different types and are linked to the project in different ways (e.g. variant databases link to individual variants, and range databases annotate groups of variants), they appear the same from a user point of view. 

In contrast to variant info fields that annotate all variants, **annotation databases usually do not cover all variants in the project and variants that are not annotated have value `NULL` for these annotation fields**. Because almost all annotation databases has a field `chr`, the most frequently used queries for these databases are probably the membership queies such as **`XXX.chr IS NOT NULL`@**, and **`@XXX.chr is NULL`**. The former identifies all variants that are in the database, and the latter identifies all variants that are not in the database. 

<details><summary> Examples: Select variants based on database membership</summary> Let us first link the project to the dbSNP database 



    % vtools use dbSNP
    
    INFO: Choosing version dbSNP-hg38_143 from 10 available databases.
    INFO: Downloading annotation database annoDB/dbSNP-hg38_143.ann
    INFO: Using annotation DB dbSNP as dbSNP in project select.
    INFO: dbSNP version 143, created using vcf file downloaded from NCBI
    

then find out all the variants that are in the dbSNP database: 



    % vtools select variant 'dbSNP.chr IS NOT NULL' -t inDbSNP 'variants in dbSNP version 130'
    
    Running: 6 97.9/s in 00:00:00                                                                               
    INFO: 1429 variants selected.
    

We can see the rsname of these variants 



    % vtools output inDbSNP chr pos ref alt dbSNP.name --all
    
    1   14677   G   A   rs201327123
    1   15820   G   T   rs2691315
    1   16103   T   G   rs78376469
    ... ...
  
    

Here we use the `--all` option of command `vtools output` because a variant can have multiple rsnames, and this is indeed the case for mutation `A->G` at `chr1:746775`. 

The syntax is the same for range-based databases. For example, if we use the refGene database, 



    % vtools use refGene
    
    INFO: Choosing version refGene-hg38_20170201 from 5 available databases.
    INFO: Downloading annotation database annoDB/refGene-hg38_20170201.ann
    INFO: Using annotation DB refGene as refGene in project select.
    INFO: Known human protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq).
    

we can find out all the variants that are not in dbSNP but in one of the ref seq genes, 



    % vtools select variant 'dbSNP.chr IS NULL' 'refGene.chr IS NOT NULL' -t inRefGene 'variants that are in refGene but not dbSNP'
    
    Running: 7 567.6/s in 00:00:00                                            
    INFO: 32 variants selected.
    

</details>

You of course do not have to limit yourself to the membership conditions because annotation databases provides many fields that can be used to select variants. For example, the dbNSFP database provides SIFT and PolyPhen2 scores for non-synonymous variants in CCDS genes, you can select variants that are probably damaging based on such information. 

<details><summary> Examples: Select variants by values of annotation fields</summary> Let us first link the dbNSFP database, 

    % vtools use dbNSFP  

    INFO: Downloading annotation database from annoDB/dbNSFP.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/dbNSFP-hg18_hg19_2_0b4.DB.gz
    INFO: Using annotation DB dbNSFP in project select.
    INFO: dbNSFP version 2.0b4, maintained by Xiaoming Liu from UTSPH. Please cite "Liu X, Jian X, and Boerwinkle E. 2011. dbNSFP: a lightweight database of human non-synonymous SNPs and their functional predictions. Human Mutation. 32:894-899" if you find this database useful.
    

you can select variants that are in this database using the memebership query 

    % vtools select variant 'dbNSFP.chr IS NOT NULL' -t ns 'non-synonymous variants in dbNSFP database'
    
    Running: 3 63.7/s in 00:00:00
    INFO: 12 variants selected.
    

then select variants that are probably damaging according to SIFT scores 

    % vtools select ns 'SIFT_score < 0.05' -t damaging 'probably damaging'
    
    Running: 0 0.0/s in 00:00:00
    INFO: 5 variants selected.
    

You can check if the SIFT score - selected damaging variants are also damaging according to other criteria/scores, 



    % vtools select ns 'SIFT_score < 0.05' --output chr pos ref alt SIFT_score \
         dbNSFP.MutationAssessor_pred PolyPhen2_HDIV_score PolyPhen2_HDIV_pred

    1  879501  G  C  .     medium   .                  .
    1  908247  G  T  0.03  low      0.999;0.998;0.998  D;D;D
    1  909364  G  T  0.03  low      0.99;0.999;0.997   D;D;D
    1  909861  A  T  0.02  neutral  0.358;0.062;0.358  B;B;B
    1  909873  A  T  0.0   low      0.95;0.98;0.899    P;D;P
    

As you can see, one of the variants with small SIFT score is predicted to be benign according to polyphen2 HDIV prediction. 

Because these scores do not agree with each other too well, we sometimes use them together and consider a variant to be damaging if it is declared so by one of the scores: 



    % vtools select ns 'SIFT_score < 0.05 or PolyPhen2_HDIV_pred like "%D%"' -t damaging 'Damaging predicted by either SIFT or polyphen2'
    
    WARNING: Existing table damaging is renamed to damaging_Jul14_214229.
    Running: 0 0.0/s in 00:00:00
    INFO: 6 variants selected.
    6
    

Because a table `damage` has been created before, the existing table is renamed before a new table is created. If you do not need such backup tables, you can remove them using command `vtools remove tables`, 



    % vtools remove tables '*Jul*'
    
    INFO: Removing table damaging_Jul14_214229
    

here a wildcard pattern is used to remove all backup tables created in July. 

</details>

One of the common use of annotation databases is to identify variants that belong to certain genes, exonic regions of genes, or pathways. Databases that are useful for these operations are `refGene`, `refGene_exon`, `knownGene`, `knownGene_exon`, and `keggPathway`. 

<details><summary> Examples: Select variants by gene, exon regions and pathway membership</summary> Let us first load the keggPathway database. Because this database is a field database that annotates ccdsGene ID, it should be linked to a database that contains CCDS ID: 



    % vtools use ccdsGene  

    INFO: Choosing version ccdsGene-hg38_20171008 from 4 available databases.
    INFO: Downloading annotation database annoDB/ccdsGene-hg38_20171008.ann
    INFO: Using annotation DB ccdsGene as ccdsGene in project select.
    INFO: High-confidence human gene annotations from the Consensus Coding Sequence (CCDS) project.
    



    % vtools use keggPathway --linked_by ccdsGene.name
    
    INFO: Choosing version keggPathway-20110823 from 1 available databases.
    INFO: Downloading annotation database annoDB/keggPathway-20110823.ann
    INFO: Using annotation DB keggPathway as keggPathway in project select.
    INFO: kegg pathway for CCDS genes
    INFO: 6745 out of 32508 ccdsGene.ccdsGene.name are annotated through annotation database keggPathway
    WARNING: 204 out of 6949 values in annotation database keggPathway are not linked to the project.
    

As you can see from the above output, the KEGG pathway database contains 6881 CCDS genes, but also has 68 IDs that are not recognizable by the current version of the CCDS database. 

Anyway, the following command lists all CCDS genes and refGenes that contain one or more variants in the project, 

    % vtools output variant ccdsGene.name refGene.name2 | sort | uniq
    
       .   .
    .   AGRN
    .   B3GALT6
    .   C1orf159
    .   FAM41C
    .   FAM87B
    .   ISG15
    .   KLHL17
    .   LINC00115
    .   LINC01128
    .   LINC01342
    .   LOC100130417
    .   LOC100288069
    .   LOC100288175
    .   LOC100288778
    .   MIR6723
    .   PERM1
    .   PLEKHN1
    .   RNF223
    .   SAMD11
    .   SDF4
    .   TTLL10
    .   UBE2J2
    .   WASH7P
    CCDS10.1    TNFRSF18
    CCDS11.1    TNFRSF4
    CCDS12.1    SDF4
    CCDS14.1    UBE2J2
    CCDS2.2 SAMD11
    CCDS3.1 NOC2L
    CCDS30547.1 OR4F5
    CCDS30550.1 KLHL17
    CCDS30551.1 AGRN
    CCDS4.1 PLEKHN1
    CCDS44036.1 TTLL10
    CCDS6.1 ISG15
    CCDS7.2 C1orf159
    CCDS76083.1 PERM1
    CCDS8.1 TTLL10

    

As you can see, CCDS genes are more conservative and do not contain some of the ref seq genes. If you need to find out all the variants that belong to a particular gene, you can use 

    % vtools select variant 'refGene.name2 = "AGRN"' -t AGRN
    
    Running: 21 1.0K/s in 00:00:00                                                                             
    INFO: 111 variants selected
    

You can also output the pathway that this gene belong as follows: 

    % vtools select variant 'refGene.name2 = "AGRN"' --output \
         chr pos ref alt refGene.name2 keggpathway.kgID keggPathway.kgDesc -l 10 --all
    
    1   1021740 G   C   AGRN    hsa04512    ECM-receptor interaction
    1   1021740 G   C   AGRN    hsa04512    ECM-receptor interaction
    1   1022868 A   G   AGRN    hsa04512    ECM-receptor interaction
    1   1022868 A   G   AGRN    hsa04512    ECM-receptor interaction
    1   1023351 A   G   AGRN    hsa04512    ECM-receptor interaction
    1   1023351 A   G   AGRN    hsa04512    ECM-receptor interaction
    1   1023525 A   G   AGRN    hsa04512    ECM-receptor interaction
    1   1023525 A   G   AGRN    hsa04512    ECM-receptor interaction
    1   1023573 A   G   AGRN    hsa04512    ECM-receptor interaction
    1   1023573 A   G   AGRN    hsa04512    ECM-receptor interaction
    

</details>


{{% notice warning %}}
Please read the description of fields from the output of `vtools show fields` carefully to avoid wrongful interpretation of annotation values. For example, `SIFT_score` provided by dbNSFP verion 1.0 are normalized (1-original score) so a higher score means higher probability of being damaging. It is no longer normalized in version 2.0 and latter so a smaller score (e.g. < 0.05) means more damaging. 
{{% /notice %}}

{{% notice tip %}}
If you select variants based on some condition, and then its NOT condition, you might be surprised to find that some variants belong to both sets. This is because some variants match multiple records in the annotation database, and are selected by these seemingly contradicting conditions. For example, a variant can belong to multipe isoforms of a gene might be benign in one gene and damaging in another. The variant will be selected by both benigh and damaging conditions. 
{{% /notice %}}


#### 2.3 Select variants according to sample genotypes

It is sometimes useful to select variants based on sample genotypes, to answer questions such as what variants are available in the affected individuals. Command `vtools select` accepts a parameter `--samples` and will select variants that belong to selected samples. This parameter accepts one or more conditions by which samples are selected. For example `--samples 1` selects all samples (condition `True`), `--samples 'sample_name = "CEU"'` selects a sample with name `CEU`, and `--samples 'filename like "<span class='CEU'>"'` selects all samples that are imported from files with filename containing `CEU`. </span> 

<details><summary> Examples: Select variants that belong to some or all samples</summary> Our project contains three samples with the same name `SAMP1`, which is not unusual for pipelines that produce `.vcf` files with a default name. 



    % vtools show samples

    sample_name  filename
    SAMP1       V1_hg38.vcf
    SAMP2       V2_hg38.vcf
    SAMP3       V3_hg38.vcf
    

We can rename samples using command `vtools admin --rename_samples` but we can also identify samples by filename here. For example, the following command selects all variants imported from `V1.vcf` to a table V1. 



    % vtools select variant --samples 'filename = "V1.vcf"' -t V1 'variants imported from V1.vcf'
    
    INFO: 1 samples are selected by condition: filename = "V1.vcf"
    Running: 3 1.0K/s in 00:00:00                                                                           
    INFO: 1269 variants selected.
    

</details>




{{% notice tip %}}   
 Samples without genotype information can be imported from data without genotype by specifying sample names. Such 'samples' can help you identify the source of variants. 
{{% /notice%}}

{{% notice tip %}}  
Variants do not have to belong to any sample so it is not surprising that `vtools select TABLE --sample 1` do not have to select all variants in `TABLE`.
{{% /notice%}}

 [1]:    /documentation/help/