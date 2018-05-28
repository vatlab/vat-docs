+++
title = "output"
description = ""
weight = 12
+++




##  Output variants in a variant table 

### 1. Usage

    % vtools output -h
    

    usage: vtools output [-h] [--header [HEADER [HEADER ...]]] [-d DELIMITER]
                         [--na NA] [-l N] [--build BUILD] [-g [FIELD [FIELD ...]]]
                         [--all] [--order_by FIELD [FIELD ...]] [-v {0,1,2}]
                         table fields [fields ...]
    
    Output variants, variant info fields, annotation fields and expressions that
    involve these fields in a tab or comma separated format.
    
    positional arguments:
      table                 variants to output.
      fields                A list of fields that will be outputted. SQL-
                            compatible expressions or functions such as "pos-1",
                            "count(1)" or "sum(num)" are also allowed.
    
    optional arguments:
      -h, --help            show this help message and exit
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

Command `vtools output` outputs properties of variant in a specified variant table. The properties include fields from annotation databases and variant tables (e.g. sample frequency), basically fields outputted from command `vtools show fields`, and SQL-supported functions and expressions. 



#### 2.1 Basic usage of the command

The basic usage of `vtools output` is to output variant info fields of selected variants. You can use option `--limit` to limit the number of records, `--delimiter` to specify delimiter between output fields (default to tab). 

<details><summary> Examples: Load data and produce basic output</summary> Let us load a small project from online 

    % vtools init output
    % vtools admin --load_snapshot vt_quickStartGuide
    

    Downloading snapshot vt_quickStartGuide.tar.gz from online
    INFO: Snapshot vt_quickStartGuide has been loaded
    

This project has a single variant table and 8 variant info fields. To view variants with the fields, we can 



    % vtools output variant chr pos ref alt aa ac an dp -l 10
    

    1  1105366  T  C  T  4    114  3251
    1  1105411  G  A  G  1    106  2676
    1  1108138  C  T  c  7    130  2253
    1  1110240  T  A  T  1    178  7275
    1  1110294  G  A  A  29   158  7639
    1  3537996  T  C  C  156  156  1753
    1  3538692  G  C  G  13   178  8362
    1  3541597  C  T  C  1    178  8060
    1  3541652  G  A  G  27   202  5923
    1  3545211  G  A  G  1    178  11142
    

The first parameter is name of a variant table, which does not have to be the master variant table `variant`. For example, you can create a variant table using variants with `T` as ancestral allele, 

    % vtools select variant 'aa="T"' -t 'aa=T'
    

    Running: 2 661.8/s in 00:00:00
    INFO: 653 variants selected.
    

and view the content of this variant table as follows: 

    % vtools output 'aa=T' chr pos ref alt aa ac an dp -l 10
    

    1  1105366   T  C  T  4    114  3251
    1  1110240   T  A  T  1    178  7275
    1  6447088   T  C  T  12   172  4691
    1  6447275   T  C  T  9    176  6871
    1  11633148  T  G  T  34   98   1118
    1  20897488  C  T  T  106  164  3662
    1  20903629  T  C  T  38   164  6919
    1  35998535  T  C  T  145  202  6238
    1  36002845  T  G  T  1    180  6589
    1  40510176  T  C  T  38   202  6067
    

You can use comma to separate values using option `-d,` 

    % vtools output variant chr pos ref alt aa ac an dp -l 10 -d,
    

    1,1105366,T,C,T,4,114,3251
    1,1105411,G,A,G,1,106,2676
    1,1108138,C,T,c,7,130,2253
    1,1110240,T,A,T,1,178,7275
    1,1110294,G,A,A,29,158,7639
    1,3537996,T,C,C,156,156,1753
    1,3538692,G,C,G,13,178,8362
    1,3541597,C,T,C,1,178,8060
    1,3541652,G,A,G,27,202,5923
    1,3545211,G,A,G,1,178,11142
    

or option `-d'\t'` to produce tab-delimited output: 



    % vtools output variant chr pos ref alt aa ac an dp -l 10 -d'\t'
    

    1	1105366	T	C	T	4	114	3251
    1	1105411	G	A	G	1	106	2676
    1	1108138	C	T	c	7	130	2253
    1	1110240	T	A	T	1	178	7275
    1	1110294	G	A	A	29	158	7639
    1	3537996	T	C	C	156	156	1753
    1	3538692	G	C	G	13	178	8362
    1	3541597	C	T	C	1	178	8060
    1	3541652	G	A	G	27	202	5923
    1	3545211	G	A	G	1	178	11142
    

</details>

You can also specify a header to the output. There are three ways to specify headers: 



*   Use option `--header` without argument to output a default header 
*   Use option `--header V1 V2 ...` to output specified headers 
*   Use option `--header -` to read header from standard input. 

<details><summary> Examples: Specify a header to the output</summary> The easiest way to add a header is to use parameter `--header` and let *variant tools* generate a default header from field names: 

    % vtools output variant chr pos ref alt aa ac --header -l 10
    

    chr  pos      ref  alt  aa  ac
    1    1105366  T    C    T   4
    1    1105411  G    A    G   1
    1    1108138  C    T    c   7
    1    1110240  T    A    T   1
    1    1110294  G    A    A   29
    1    3537996  T    C    C   156
    1    3538692  G    C    G   13
    1    3541597  C    T    C   1
    1    3541652  G    A    G   27
    1    3545211  G    A    G   1
    

If you are unhappy about the default header, you can specify one manually 



    % vtools output variant chr pos ref alt aa ac --header chr pos ref alt 'ancestral allele' 'ancestral count' -l 10 -d,
    

    chr,pos,ref,alt,ancestral allele,ancestral count
    1,1105366,T,C,T,4
    1,1105411,G,A,G,1
    1,1108138,C,T,c,7
    1,1110240,T,A,T,1
    1,1110294,G,A,A,29
    1,3537996,T,C,C,156
    1,3538692,G,C,G,13
    1,3541597,C,T,C,1
    1,3541652,G,A,G,27
    1,3545211,G,A,G,1

If you have a longer header, or a header that is saved in a file, you can send the header to `vtools output` through its standard input 



    % echo chr pos ref alt 'ancestral allele' 'ancestral count' | \
       vtools output variant chr pos ref alt aa ac --header - -l 10
    

    chr pos ref alt ancestral allele ancestral count
    1  1105366  T  C  T  4
    1  1105411  G  A  G  1
    1  1108138  C  T  c  7
    1  1110240  T  A  T  1
    1  1110294  G  A  A  29
    1  3537996  T  C  C  156
    1  3538692  G  C  G  13
    1  3541597  C  T  C  1
    1  3541652  G  A  G  27
    1  3545211  G  A  G  1
    

</details>

You can sort the output by one or more fields using option `--order_by`. *variant tools* by default oder fields in ascending order. You can order by descending order by adding `DESC` to field name. 

<details><summary> Examples: Order output by one or more field names</summary> You can oder the output using option `--order_by`, for example 

    % vtools output variant chr pos ref alt aa ac --order_by ac aa -l 10
    

    6   30018679   G  T  .  0
    9   204719     C  T  C  0
    1   17822092   C  T  C  0
    5   140870754  G  A  G  0
    6   7176795    G  A  G  0
    7   156448542  G  A  G  0
    19  2199303    G  A  G  0
    2   237954632  G  A  G  0
    6   158452418  G  A  G  0
    8   134198127  A  G  G  0
    

You can order in descending oder by specifying `DESC` after field name, for example 

    % vtools output variant chr pos ref alt aa ac --order_by 'ac DESC' 'aa' -l 10
    

    4   95758290   G  A  A  210
    10  117065165  G  A  A  210
    12  27362133   G  A  A  210
    10  46507614   T  C  C  210
    1   195656991  A  G  G  210
    1   203542044  A  G  G  210
    1   204840282  A  G  G  210
    10  97182314   A  G  G  210
    1   157676358  G  T  T  210
    12  62759070   A  T  T  210
    

</details>

If your project has a primary and a secondary reference genomes, you can output variants in both coordinates. 

<details><summary> Examples: Output variants in alternative coordinates</summary> Our sample project uses the hg18 reference genome. We can add an alternative reference genome by mapping all variants from hg18 to hg19 coordinates: 

    % vtools liftover hg19
    

    INFO: Downloading liftOver tool from UCSC
    INFO: Downloading liftOver chain file from UCSC
    INFO: Exporting variants in BED format
    Exporting variants: 100% [==================================] 4,858 131.7K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating table variant: 100% [===============================] 4,858 33.5K/s in 00:00:00
    

You can output variants in the primary reference genome, 

    % vtools output variant chr pos ref alt aa ac --header  --build hg18 -l 10
    

    chr  pos      ref  alt  aa  ac
    1    1105366  T    C    T   4
    1    1105411  G    A    G   1
    1    1108138  C    T    c   7
    1    1110240  T    A    T   1
    1    1110294  G    A    A   29
    1    3537996  T    C    C   156
    1    3538692  G    C    G   13
    1    3541597  C    T    C   1
    1    3541652  G    A    G   27
    1    3545211  G    A    G   1
    

or the alternative reference genome using option `--build` 

    % vtools output variant chr pos ref alt aa ac --header  --build hg19 -l 10
    

    chr  pos      ref  alt  aa  ac
    1    1115503  T    C    T   4
    1    1115548  G    A    G   1
    1    1118275  C    T    c   7
    1    1120377  T    A    T   1
    1    1120431  G    A    A   29
    1    3548136  T    C    C   156
    1    3548832  G    C    G   13
    1    3551737  C    T    C   1
    1    3551792  G    A    G   27
    1    3555351  G    A    G   1
    

</details>



#### 2.2 Output fields from annotation databases (option `--all`)

You can output fields from one or more annotation databases in the same way as variant info fields. To output annotation fields of variants, you simply need to 

*   Link annotation databases to the project using command `vtools use` 
*   Use command `vtools show annotation ANNODB` or `vtools show fields` to check name and meaning of available fields 
*   Output annotation fields along with variant info fields. Name of annotation database can be ignored if there is no ambiguity. 

<details><summary> Examples: Output fields of annotation fields</summary> Let us use annotation databases `refGene` and `dbSNP`, 

    % vtools use refGene
    

    INFO: Downloading annotation database from annoDB/refGene.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/refGene-hg19_20110909.DB.gz
    INFO: Using annotation DB refGene in project output.
    INFO: refseq Genes
    



    % vtools use dbSNP
    

    INFO: Downloading annotation database from annoDB/dbSNP.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/dbSNP-hg19_137.DB.gz
    INFO: Using annotation DB dbSNP in project output.
    INFO: dbSNP version 137
    

because this project uses both hg18 and hg19, it can make use of the latest version of `refGene` and `dbSNP` databases that use hg19. 

These two databases bring in a large number of annotation fields, as listed by command 

    % vtools show fields
    

    variant.chr
    variant.pos
    variant.ref
    variant.alt
    variant.AA
    variant.AC
    variant.AN
    variant.DP
    variant.alt_chr
    variant.alt_pos
    refGene.name                 Gene name
    refGene.chr
    refGene.strand               which DNA strand contains the observed alleles
    refGene.txStart              Transcription start position
    refGene.txEnd                Transcription end position
    refGene.cdsStart             Coding region start
    refGene.cdsEnd               Coding region end
    refGene.exonCount            Number of exons
    refGene.score                Score
    refGene.name2                Alternative name
    refGene.cdsStartStat         cds start stat, can be 'non', 'unk', 'incompl', and 'cmp1'
    refGene.cdsEndStat           cds end stat, can be 'non', 'unk', 'incompl', and 'cmp1'
    dbSNP.chr
    dbSNP.start                  start position in chrom (1-based)
    dbSNP.end                    end position in chrom (1-based). start=end means
                                 zero-length feature
    dbSNP.name                   dbSNP reference SNP identifier
    dbSNP.strand                 which DNA strand contains the observed alleles
    dbSNP.refNCBI                Reference genomic sequence from dbSNP
    dbSNP.refUCSC                Reference genomic sequence from UCSC lookup of
                                 chrom,chromStart,chromEnd
    dbSNP.observed               Strand-specific observed alleles
    dbSNP.alt                    alternate allele on the '+' strand
    dbSNP.molType                sample type, can be one of unknown, genomic or cDNA
    dbSNP.class                  Class of variant (single, in-del, het, named, mixed,
                                 insertion, deletion etc
    dbSNP.valid                  validation status, can be unknown, by-cluster, by-
                                 frequency, by-submitter, by-2hit-2allele,
                                 by-hapmap, and by-1000genomes
    dbSNP.avHet                  Average heterozygosity from all observations
    dbSNP.avHetSE                Standard error for the average heterozygosity
    dbSNP.func                   Functional cetegory of the SNP (coding-synon,
                                 coding-nonsynon, intron, etc.)
    dbSNP.locType                Type of mapping inferred from size on reference.
    dbSNP.submitterCount         Number of distinct submitter handles for submitted SNPs for
                                 this ref SNP
    dbSNP.submitters             List of submitter handles
    

You can output annotation fields as follows: 



    % vtools output 'aa=T' chr pos ref alt dbSNP.name refGene.name refGene.name2 -l 10
    

    1  1105366   T  C  rs111751804  NM_001130045  TTLL10
    1  1110240   T  A  rs116321663  NM_001130045  TTLL10
    1  6447088   T  C  rs11800462   NM_003790     TNFRSF25
    1  6447275   T  C  rs3170675    NM_003790     TNFRSF25
    1  11633148  T  G  rs9614       NM_012168     FBXO2
    1  20897488  C  T  rs522496     NM_001122819  KIF17
    1  20903629  T  C  rs2296225    NM_001122819  KIF17
    1  35998535  T  C  rs7537203    NM_022111     CLSPN
    1  36002845  T  G  rs115614983  NM_022111     CLSPN
    1  40510176  T  C  rs2076697    NM_005857     ZMPSTE24
    

</details>

This looks simple but the problem is more complicated than what is shown here, because **a variant can match multiple records in annotation databases**. For example, mutation `T->C` at position `1105366` on chr1 belongs to reference sequences `NM_153254` and `NM_001130045` of the reference sequence database. Because **`vtools output` by default only displays a random record of multiple records**, its output can miss important information. To address this problem, an option `--all` is provided to output all annotation records. This option has its own problem though. For example, if you do not output the differentiating field that lead to multiple records, you can see a bunch of duplicated records. 

<details><summary> Examples: Use option --all to list all annotation records</summary> Using option `--all`, command `vtools output` can display multiple records for a variant: 

    % vtools output 'aa=T' chr pos ref alt dbSNP.name refGene.name refGene.name2 --all -l 10
    

    1  1105366  T  C  rs111751804  NM_153254     TTLL10
    1  1105366  T  C  rs111751804  NM_001130045  TTLL10
    1  1110240  T  A  rs116321663  NM_153254     TTLL10
    1  1110240  T  A  rs116321663  NM_001130045  TTLL10
    1  6447088  T  C  rs11800462   NM_001039664  TNFRSF25
    1  6447088  T  C  rs11800462   NM_148970     TNFRSF25
    1  6447088  T  C  rs11800462   NM_148967     TNFRSF25
    1  6447088  T  C  rs11800462   NM_148966     TNFRSF25
    1  6447088  T  C  rs11800462   NM_148965     TNFRSF25
    1  6447088  T  C  rs11800462   NM_003790     TNFRSF25
    

A consequence of this is that duplicated records can be displayed if the field that lead to multiple records is not outputted: 

    % vtools output 'aa=T' chr pos ref alt dbSNP.name  refGene.name2 --all -l 10
    

    1  1105366  T  C  rs111751804  TTLL10
    1  1105366  T  C  rs111751804  TTLL10
    1  1110240  T  A  rs116321663  TTLL10
    1  1110240  T  A  rs116321663  TTLL10
    1  6447088  T  C  rs11800462   TNFRSF25
    1  6447088  T  C  rs11800462   TNFRSF25
    1  6447088  T  C  rs11800462   TNFRSF25
    1  6447088  T  C  rs11800462   TNFRSF25
    1  6447088  T  C  rs11800462   TNFRSF25
    1  6447088  T  C  rs11800462   TNFRSF25
    

This is why the output of command `vtools output --all` is usually piped to command `uniq`, 

    % vtools output 'aa=T' chr pos ref alt dbSNP.name  refGene.name2 --all -l 10 | uniq
    

    1  1105366  T  C  rs111751804  TTLL10
    1  1110240  T  A  rs116321663  TTLL10
    1  6447088  T  C  rs11800462   TNFRSF25
    

although `uniq` cannot suppress all duplicated records in all cases because it only removes adjacent duplicated records. 

</details>



#### 2.3 Output expressions of fields

In addition to values of variant info and annotation fields, command `vtools output` can be used to output SQL-acceptable expressions that involves multiple fields. For example, 

*   Because *variant tools* uses 1-based coordinates, you might want to output `pos-1` instead of `pos` to generate output with 0-based indexes, 
*   You can output allele frequency by dividing number of alternative alleles by total number of alleles, 

In addition to basic arithmetic operations, *variant tools* accept additional mathematical and string extension functions for SQL queries using the loadable extensions mechanism from [HERE][1], including mathematical functions `acos, asin, atan, atn2, atan2, acosh, asinh, atanh, difference, degrees, radians, cos, sin, tan, cot, cosh, sinh, tanh, coth, exp, log, log10, power, sign, sqrt, square, ceil, floor, pi`, and string operations `replicate, charindex, leftstr, rightstr, ltrim, rtrim, trim, replace, reverse, proper, padl, padr, padc, strfilter`. 

<details><summary> Examples: Output expressionf of fields</summary> This example demonstrates the use of SQL expressions in command `vtools output`. Note that the sqlite string concatenation operator is `||`. 

    % vtools output "aa=T" chr 'pos-1' 'refGene.name2 || "." || refGene.name' 'log(DP)' --header -l 10
    

    chr  pos_1     refGene_name2___________refGene_name  log_DP_
    1    1105365   TTLL10.NM_001130045                   8.0867179203
    1    1110239   TTLL10.NM_001130045                   8.89219909204
    1    6447087   TNFRSF25.NM_001039664                 8.45340105833
    1    6447274   TNFRSF25.NM_001039664                 8.83506493503
    1    11633147  FBXO2.NM_012168                       7.01929665372
    1    20897487  KIF17.NM_001122819                    8.20576472523
    1    20903628  KIF17.NM_001122819                    8.8420265295
    1    35998534  CLSPN.NM_022111                       8.73841489717
    1    36002844  CLSPN.NM_022111                       8.79315687091
    1    40510175  ZMPSTE24.NM_005857                    8.71061952794
    

As you can see, the default header that *variant tools* generates replaces all non-alphanumeric characters by underscores, and you should most likely specify your own headers in these cases. 

</details>



#### 2.4 Output summary statistics of fields using SQL aggregating functions (option `--group_by`)

In addition to functions that operate on values of the same field, you can use SQL aggregating functions to output summary statistics of fields. For example, you can use function `count(*)` to count the number of records, `sum(DP)` to get the sum of depth for all variants. More usefully, these operations can be applied to groups of variants defined by option `--group_by`. 

Command `vtools output` accepts the following aggregating functions: 

*   All sqlite3 functions listed [HERE][2] are supported. The most useful ones are `count`, `sum`, `avg`, `min` and `max`. 
*   Additional aggregation functions such as `stdev, variance, mode, median, lower_quartile, upper_quartile` defined [HERE][1]. 

<details><summary> Examples: Output summary statistics of fields</summary> The following command calculate the average depth for all variants: 



    % vtools output variant 'avg(DP)'
    

    6264.00102923
    

You can also output average of depth, grouped by variants that belong to genes, 



    % vtools output variant refGene.name2 'count(*)' 'avg(DP)' --group_by refGene.name2 -l 10
    

    .         20  5928.05
    AARD      1   3919.0
    AASDHPPT  2   7834.0
    AATF      4   8590.0
    ABCB9     3   3469.66666667
    ABCC6     18  4963.27777778
    ABLIM3    6   8895.5
    ABTB2     3   6922.0
    ACHE      4   5159.25
    ACIN1     15  8962.73333333
    

Here `count(*)` is used to count the number of variants in each gene, and `NA` is a special group for variants that do not belong to any gene, which can be confirmed by command 



    % vtools select variant 'refGene.chr is NULL' --output 'avg(DP)'
    

    5928.05
    

Option `--all` should not be used in these commands because this option will lead to multiple entries for some variants, and biase the results. For example, the output of the following command differs from the previous one: 

    % vtools output variant refGene.name2 'count(*)' 'avg(DP)' --group_by refGene.name2 --all -l 10
    

    .         20  5928.05
    AARD      1   3919.0
    AASDHPPT  2   7834.0
    AATF      4   8590.0
    ABCB9     15  3469.66666667
    ABCC6     18  4963.27777778
    ABLIM3    6   8895.5
    ABTB2     3   6922.0
    ACHE      8   5159.25
    ACIN1     47  8719.21276596
    

</details>

{{% notice warning %}}
Using option `--all` along with aggregating function will most likely lead to erroneous results because the aggregating function will be applied to a dataset with duplicated entries, unless you intentionally would like to count, for example, number of duplicated entries for each variant.
{{% /notice %}}

 [1]: http://www.sqlite.org/contrib
 [2]: http://www.sqlite.org/lang_aggfunc.html