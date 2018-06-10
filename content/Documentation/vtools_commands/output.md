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
    % vtools import CEU_hg19.vcf --var_info AA AC AN DP --geno_info DP --build hg19
    
    

This project has a single variant table and 8 variant info fields. To view variants with the fields, we can 



    % vtools output variant chr pos ref alt aa ac an dp -l 10
    
    1   10533   G   C   .   6   120 423
    1   51479   T   A   .   29  120 188
    1   51928   G   A   .   5   120 192
    1   54586   T   C   C   2   120 166
    1   54676   C   T   T   2   120 131
    1   54708   G   C   g   7   120 135
    1   55299   C   T   c   20  120 166
    1   62203   T   C   C   18  120 159
    1   63671   G   A   G   18  120 243
    1   86028   T   C   .   11  120 182
    

The first parameter is name of a variant table, which does not have to be the master variant table `variant`. For example, you can create a variant table using variants with `T` as ancestral allele, 

    % vtools select variant 'aa="T"' -t 'aa=T'
    
    Running: 0 0.0/s in 00:00:00                                                  
    INFO: 22 variants selected.
    

and view the content of this variant table as follows: 

    % vtools output 'aa=T' chr pos ref alt aa ac an dp -l 10
    
    1   54676       C   T   T   2   120 131
    22  51158111    T   C   T   1   120 298
    22  51158301    T   C   T   7   120 169
    22  51162850    C   T   T   41  120 367
    22  51164115    C   T   T   52  120 357
    22  51164287    T   C   T   37  120 331
    22  51172460    T   C   T   3   120 274
    22  51174939    C   T   T   4   120 317
    22  51176164    T   C   T   3   120 380
    22  51186228    C   T   T   51  120 253
    

You can use comma to separate values using option `-d,` 

    % vtools output variant chr pos ref alt aa ac an dp -l 10 -d,
    
    1,10533,G,C,.,6,120,423
    1,51479,T,A,.,29,120,188
    1,51928,G,A,.,5,120,192
    1,54586,T,C,C,2,120,166
    1,54676,C,T,T,2,120,131
    1,54708,G,C,g,7,120,135
    1,55299,C,T,c,20,120,166
    1,62203,T,C,C,18,120,159
    1,63671,G,A,G,18,120,243
    1,86028,T,C,.,11,120,182

    

or option `-d'\t'` to produce tab-delimited output: 



    % vtools output variant chr pos ref alt aa ac an dp -l 10 -d'\t'
    
    1   10533   G   C   .   6   120 423
    1   51479   T   A   .   29  120 188
    1   51928   G   A   .   5   120 192
    1   54586   T   C   C   2   120 166
    1   54676   C   T   T   2   120 131
    1   54708   G   C   g   7   120 135
    1   55299   C   T   c   20  120 166
    1   62203   T   C   C   18  120 159
    1   63671   G   A   G   18  120 243
    1   86028   T   C   .   11  120 182

    

</details>

You can also specify a header to the output. There are three ways to specify headers: 



*   Use option `--header` without argument to output a default header 
*   Use option `--header V1 V2 ...` to output specified headers 
*   Use option `--header -` to read header from standard input. 

<details><summary> Examples: Specify a header to the output</summary> The easiest way to add a header is to use parameter `--header` and let *variant tools* generate a default header from field names: 

    % vtools output variant chr pos ref alt aa ac --header -l 10
    
    chr pos     ref alt aa  ac
    1   10533   G   C   .   6
    1   51479   T   A   .   29
    1   51928   G   A   .   5
    1   54586   T   C   C   2
    1   54676   C   T   T   2
    1   54708   G   C   g   7
    1   55299   C   T   c   20
    1   62203   T   C   C   18
    1   63671   G   A   G   18
    1   86028   T   C   .   11

    

If you are unhappy about the default header, you can specify one manually 



    % vtools output variant chr pos ref alt aa ac --header chr pos ref alt 'ancestral allele' 'ancestral count' -l 10 -d,
    
    chr,pos,ref,alt,ancestral allele,ancestral count
    1,10533,G,C,.,6
    1,51479,T,A,.,29
    1,51928,G,A,.,5
    1,54586,T,C,C,2
    1,54676,C,T,T,2
    1,54708,G,C,g,7
    1,55299,C,T,c,20
    1,62203,T,C,C,18
    1,63671,G,A,G,18
    1,86028,T,C,.,11


If you have a longer header, or a header that is saved in a file, you can send the header to `vtools output` through its standard input 



    % echo chr pos ref alt 'ancestral allele' 'ancestral count' | \
       vtools output variant chr pos ref alt aa ac --header - -l 10   

    chr pos ref alt ancestral allele ancestral count
    1   10533   G   C   .   6
    1   51479   T   A   .   29
    1   51928   G   A   .   5
    1   54586   T   C   C   2
    1   54676   C   T   T   2
    1   54708   G   C   g   7
    1   55299   C   T   c   20
    1   62203   T   C   C   18
    1   63671   G   A   G   18
    1   86028   T   C   .   11
    

</details>

You can sort the output by one or more fields using option `--order_by`. *variant tools* by default oder fields in ascending order. You can order by descending order by adding `DESC` to field name. 

<details><summary> Examples: Order output by one or more field names</summary> You can oder the output using option `--order_by`, for example 

    % vtools output variant chr pos ref alt aa ac --order_by ac alt -l 10
    
    1   526727      G   A   .   1
    1   726440      G   A   .   1
    1   773106      G   A   g   1
    1   809700      G   A   -   1
    22  51158111    T   C   T   1
    22  51176004    G   C   G   1
    1   793947      A   G   N   1
    1   776876      C   T   c   1
    22  51197087    C   T   C   1
    1   88316       G   A   .   2
    

You can order in descending oder by specifying `DESC` after field name, for example 

    % vtools output variant chr pos ref alt aa ac --order_by 'ac DESC' 'aa' -l 10
    
    1   814790      C   T   c   7,2
    1   814790      C   G   c   7,2
    1   799463      T   C   N   120
    1   780027      G   T   t   120
    1   792480      C   T   t   120
    1   812751      T   C   N   119
    1   804540      T   C   t   119
    1   723891      G   C   .   114
    22  51173542    T   C   C   113
    22  51185848    G   A   A   110
    

</details>

If your project has a primary and a secondary reference genomes, you can output variants in both coordinates. 

<details><summary> Examples: Output variants in alternative coordinates</summary> Our sample project uses the hg18 reference genome. We can add an alternative reference genome by mapping all variants from hg18 to hg19 coordinates: 

    % vtools liftover hg38
    
    INFO: Downloading liftOver chain file from UCSC
    INFO: Exporting variants in BED format
    Exporting variants: 100% [================================] 288 69.0K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating table variant: 100% [============================] 288 537.9/s in 00:00:00

    

You can output variants in the primary reference genome, 

    % vtools output variant chr pos ref alt aa ac --header  --order_by ac --build hg19 -l 10
    
    chr pos         ref alt aa  ac
    1   526727      G   A   .   1
    1   726440      G   A   .   1
    1   773106      G   A   g   1
    1   776876      C   T   c   1
    1   793947      A   G   N   1
    1   809700      G   A   -   1
    22  51158111    T   C   T   1
    22  51176004    G   C   G   1
    22  51197087    C   T   C   1
    1   54586       T   C   C   2
    

or the alternative reference genome using option `--build` 

    % vtools output variant chr pos ref alt aa ac --header  --order_by ac --build hg38 -l 10
    
    chr pos         ref alt aa  ac
    1   591347      G   A   .   1
    1   791060      G   A   .   1
    1   837726      G   A   g   1
    1   841496      C   T   c   1
    1   858567      A   G   N   1
    1   874320      G   A   -   1
    22  50719683    T   C   T   1
    22  50737576    G   C   G   1
    22  50758659    C   T   C   1
    1   54586       T   C   C   2
    

</details>



#### 2.2 Output fields from annotation databases (option `--all`)

You can output fields from one or more annotation databases in the same way as variant info fields. To output annotation fields of variants, you simply need to 

*   Link annotation databases to the project using command `vtools use` 
*   Use command `vtools show annotation ANNODB` or `vtools show fields` to check name and meaning of available fields 
*   Output annotation fields along with variant info fields. Name of annotation database can be ignored if there is no ambiguity. 

<details><summary> Examples: Output fields of annotation fields</summary> Let us use annotation databases `refGene` and `dbSNP`, 

    % vtools use refGene
    
    INFO: Choosing version refGene-hg38_20170201 from 5 available databases.
    INFO: Downloading annotation database annoDB/refGene-hg38_20170201.ann
    INFO: Using annotation DB refGene as refGene in project output.
    INFO: Known human protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq).
        

    % vtools use dbSNP
    
    INFO: Choosing version dbSNP-hg38_143 from 10 available databases.
    INFO: Downloading annotation database annoDB/dbSNP-hg38_143.ann
    INFO: Using annotation DB dbSNP as dbSNP in project output.
    INFO: dbSNP version 143, created using vcf file downloaded from NCBI
    

because this project uses both hg18 and hg19, it can make use of the latest version of `refGene` and `dbSNP` databases that use hg19. 

These two databases bring in a large number of annotation fields, as listed by command 

    % vtools show fields
    
    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    variant.AA (char)
    variant.AC (int)
    variant.AN (int)
    variant.DP (int)
    variant.alt_chr (char)
    variant.alt_pos (int)
    aa=T.chr (char)         Chromosome name (VARCHAR)
    refGene.name (char)     Gene name
    refGene.chr (char)
    refGene.strand (char)   which DNA strand contains the observed alleles
    refGene.txStart (int)   Transcription start position (1-based)
    refGene.txEnd (int)     Transcription end position
    refGene.cdsStart (int)  Coding region start (1-based)
    refGene.cdsEnd (int)    Coding region end
    refGene.exonCount (int) Number of exons
    refGene.exonStarts (char)
                            Starting point of exons (adjusted to 1-based positions)
    refGene.exonEnds (char) Ending point of exons
    refGene.score (int)     Score
    refGene.name2 (char)    Alternative name
    refGene.cdsStartStat (char)
                            cds start stat, can be 'non', 'unk', 'incompl', and 'cmp1'
    refGene.cdsEndStat (char)
                            cds end stat, can be 'non', 'unk', 'incompl', and 'cmp1'
    refGene.exonFrames (char)
                            Exon frame {0,1,2}, or -1 if no frame for exon
    dbSNP.chr (char)
    dbSNP.pos (int)
    dbSNP.name (char)       DB SNP ID (rsname)
    dbSNP.ref (char)        Reference allele (as on the + strand)
    dbSNP.alt (char)        Alternative allele (as on the + strand)
    dbSNP.FILTER (char)     Inconsistent Genotype Submission For At Least One Sample
    dbSNP.RS (int)          dbSNP ID (i.e. rs number)
    dbSNP.RSPOS (int)       Chr position reported in dbSNP
    dbSNP.RV (int)          RS orientation is reversed
    dbSNP.VP (char)         Variation Property.  Documentation is at ftp://ftp.ncbi.nlm.nih.gov/snp/specs/dbSNP_BitField_latest.pdf
    dbSNP.GENEINFO (char)   Pairs each of gene symbol:gene id.  The gene symbol and id are delimited by a colon (:) and each pair is delimited by a vertical bar (|)
    dbSNP.dbSNPBuildID (int)
                            First dbSNP Build for RS
    dbSNP.SAO (int)         Variant Allele Origin: 0 - unspecified, 1 - Germline, 2 - Somatic, 3 - Both
    dbSNP.SSR (int)         Variant Suspect Reason Codes (may be more than one value added together) 0 - unspecified, 1 - Paralog, 2 - byEST, 4 - oldAlign, 8 - Para_EST, 16 - 1kg_failed, 1024 - other
    dbSNP.WGT (int)         Weight, 00 - unmapped, 1 - weight 1, 2 - weight 2, 3 - weight 3 or more
    dbSNP.VC (char)         Variation Class
    dbSNP.PM_flag (int)     Variant is Precious(Clinical,Pubmed Cited)
    dbSNP.TPA_flag (int)    Provisional Third Party Annotation(TPA) (currently rs from PHARMGKB who will give phenotype data)
    dbSNP.PMC_flag (int)    Links exist to PubMed Central article
    dbSNP.S3D_flag (int)    Has 3D structure - SNP3D table
    dbSNP.SLO_flag (int)    Has SubmitterLinkOut - From SNP->SubSNP->Batch.link_out
    dbSNP.NSF_flag (int)    Has non-synonymous frameshift A coding region variation where one allele in the set changes all downstream amino acids. FxnClass = 44
    dbSNP.NSM_flag (int)    Has non-synonymous missense A coding region variation where one allele in the set changes protein peptide. FxnClass = 42
    dbSNP.NSN_flag (int)    Has non-synonymous nonsense A coding region variation where one allele in the set changes to STOP codon (TER). FxnClass = 41
    dbSNP.REF_flag_flag (int)
                            Has reference A coding region variation where one allele in the set is identical to the reference sequence. FxnCode = 8
    dbSNP.SYN_flag (int)    Has synonymous A coding region variation where one allele in the set does not change the encoded amino acid. FxnCode = 3
    dbSNP.U3_flag (int)     In 3' UTR Location is in an untranslated region (UTR). FxnCode = 53
    dbSNP.U5_flag (int)     In 5' UTR Location is in an untranslated region (UTR). FxnCode = 55
    dbSNP.ASS_flag (int)    In acceptor splice site FxnCode = 73
    dbSNP.DSS_flag (int)    In donor splice-site FxnCode = 75
    dbSNP.INT_flag (int)    In Intron FxnCode = 6
    dbSNP.R3_flag (int)     In 3' gene region FxnCode = 13
    dbSNP.R5_flag (int)     In 5' gene region FxnCode = 15
    dbSNP.OTH_flag (int)    Has other variant with exactly the same set of mapped positions on NCBI refernce assembly.
    dbSNP.CFL_flag (int)    Has Assembly conflict. This is for weight 1 and 2 variant that maps to different chromosomes on different assemblies.
    dbSNP.ASP_flag (int)    Is Assembly specific. This is set if the variant only maps to one assembly
    dbSNP.MUT_flag (int)    Is mutation (journal citation, explicit fact): a low frequency variation that is cited in journal and other reputable sources
    dbSNP.VLD_flag (int)    Is Validated.  This bit is set if the variant has 2+ minor allele count based on frequency or genotype data.
    dbSNP.G5A_flag (int)    >5% minor allele frequency in each and all populations
    dbSNP.G5_flag (int)     >5% minor allele frequency in 1+ populations
    dbSNP.HD_flag (int)     Marker is on high density genotyping kit (50K density or greater).  The variant may have phenotype associations present in dbGaP.
    dbSNP.GNO_flag (int)    Genotypes available. The variant has individual genotype (in SubInd table).
    dbSNP.KGValidated_flag (int)
                            1000 Genome validated
    dbSNP.KGPhase1_flag (int)
                            1000 Genome phase 1 (incl. June Interim phase 1)
    dbSNP.KGPilot123_flag (int)
                            1000 Genome discovery all pilots 2010(1,2,3)
    dbSNP.KGPROD_flag (int) Has 1000 Genome submission
    dbSNP.OTHERKG_flag (int)
                            non-1000 Genome submission
    dbSNP.PH3_flag (int)    HAP_MAP Phase 3 genotyped: filtered, non-redundant
    dbSNP.CDA_flag (int)    Variation is interrogated in a clinical diagnostic assay
    dbSNP.LSD_flag (int)    Submitted from a locus-specific database
    dbSNP.MTP_flag (int)    Microattribution/third-party annotation(TPA:GWAS,PAGE)
    dbSNP.OM_flag (int)     Has OMIM/OMIA
    dbSNP.NOC_flag (int)    Contig allele not present in variant allele list. The reference sequence allele at the mapped position is not present in the variant allele list, adjusted for orientation.
    dbSNP.WTD_flag (int)    Is Withdrawn by submitter If one member ss is withdrawn by submitter, then this bit is set.  If all member ss' are withdrawn, then the rs is deleted to SNPHistory
    dbSNP.NOV_flag (int)    Rs cluster has non-overlapping allele sets. True when rs set has more than 2 alleles from different submissions and these sets share no alleles in common.
    dbSNP.CAF (char)        An ordered, comma delimited list of allele frequencies based on 1000Genomes, starting with the reference allele followed by alternate alleles as ordered in the ALT column. Where a 1000Genomes
                            alternate allele is not in the dbSNPs alternate allele set, the allele is added to the ALT column.  The minor allele is the second largest value in the list, and was previuosly reported in
                            VCF as the GMAF.  This is the GMAF reported on the RefSNP and EntrezSNP pages and VariationReporter
    dbSNP.COMMON (int)      RS is a common SNP.  A common SNP is one that has at least one 1000Genomes population with a minor allele of frequency >= 1% and for which 2 or more founders contribute to that minor allele
                            frequency.
    

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
    
    1   54676       C   T   rs2462492   .           .
    22  51158111    T   C   rs73174428  NM_033517   SHANK3
    22  51158301    T   C   rs117910162 NM_033517   SHANK3
    22  51162850    C   T   rs5770822   NM_033517   SHANK3
    22  51164115    C   T   rs5770996   NM_033517   SHANK3
    22  51164287    T   C   rs6009957   NM_033517   SHANK3
    22  51172460    T   C   rs5770824   .           .
    22  51174939    C   T   rs73174435  NR_134637   LOC105373100
    22  51176164    T   C   rs76593947  NR_134637   LOC105373100
    22  51186228    C   T   rs3865766   .           .

    

A consequence of this is that duplicated records can be displayed if the field that lead to multiple records is not outputted: 

    % vtools output 'aa=T' chr pos ref alt dbSNP.name  refGene.name2 --all -l 10
    
    1   54676       C   T   rs2462492   .
    22  51158111    T   C   rs73174428  SHANK3
    22  51158301    T   C   rs117910162 SHANK3
    22  51162850    C   T   rs5770822   SHANK3
    22  51164115    C   T   rs5770996   SHANK3
    22  51164287    T   C   rs6009957   SHANK3
    22  51172460    T   C   rs5770824   .
    22  51174939    C   T   rs73174435  LOC105373100
    22  51176164    T   C   rs76593947  LOC105373100
    22  51186228    C   T   rs3865766   .
    

This is why the output of command `vtools output --all` is usually piped to command `uniq`, 

    % vtools output 'aa=T' chr pos ref alt dbSNP.name  refGene.name2 --all -l 10 | uniq
    

although `uniq` cannot suppress all duplicated records in all cases because it only removes adjacent duplicated records. 

</details>



#### 2.3 Output expressions of fields

In addition to values of variant info and annotation fields, command `vtools output` can be used to output SQL-acceptable expressions that involves multiple fields. For example, 

*   Because *variant tools* uses 1-based coordinates, you might want to output `pos-1` instead of `pos` to generate output with 0-based indexes, 
*   You can output allele frequency by dividing number of alternative alleles by total number of alleles, 

In addition to basic arithmetic operations, *variant tools* accept additional mathematical and string extension functions for SQL queries using the loadable extensions mechanism from [HERE][1], including mathematical functions `acos, asin, atan, atn2, atan2, acosh, asinh, atanh, difference, degrees, radians, cos, sin, tan, cot, cosh, sinh, tanh, coth, exp, log, log10, power, sign, sqrt, square, ceil, floor, pi`, and string operations `replicate, charindex, leftstr, rightstr, ltrim, rtrim, trim, replace, reverse, proper, padl, padr, padc, strfilter`. 

<details><summary> Examples: Output expressionf of fields</summary> This example demonstrates the use of SQL expressions in command `vtools output`. Note that the sqlite string concatenation operator is `||`. 

    % vtools output "aa=T" chr 'pos-1' 'refGene.name2 || "." || refGene.name' 'log(DP)' --header -l 10
    
    chr pos_1       refGene_name2_refGene_name  log_DP_
    1   54675       .                           4.875197323201151
    22  51158110    SHANK3.NM_033517            5.697093486505405
    22  51158300    SHANK3.NM_033517            5.1298987149230735
    22  51162849    SHANK3.NM_033517            5.905361848054571
    22  51164114    SHANK3.NM_033517            5.877735781779639
    22  51164286    SHANK3.NM_033517            5.802118375377063
    22  51172459    .                           5.6131281063880705
    22  51174938    LOC105373100.NR_134637      5.75890177387728
    22  51176163    LOC105373100.NR_134637      5.940171252720432
    22  51186227    .                           5.53338948872752
    

As you can see, the default header that *variant tools* generates replaces all non-alphanumeric characters by underscores, and you should most likely specify your own headers in these cases. 

</details>



#### 2.4 Output summary statistics of fields using SQL aggregating functions (option `--group_by`)

In addition to functions that operate on values of the same field, you can use SQL aggregating functions to output summary statistics of fields. For example, you can use function `count(*)` to count the number of records, `sum(DP)` to get the sum of depth for all variants. More usefully, these operations can be applied to groups of variants defined by option `--group_by`. 

Command `vtools output` accepts the following aggregating functions: 

*   All sqlite3 functions listed [HERE][2] are supported. The most useful ones are `count`, `sum`, `avg`, `min` and `max`. 
*   Additional aggregation functions such as `stdev, variance, mode, median, lower_quartile, upper_quartile` defined [HERE][1]. 

<details><summary> Examples: Output summary statistics of fields</summary> The following command calculate the average depth for all variants: 



    % vtools output variant 'avg(DP)'
   
    271.875
    

You can also output average of depth, grouped by variants that belong to genes, 



    % vtools output variant refGene.name2 'count(*)' 'avg(DP)' --group_by refGene.name2 -l 10    

    .               161 281.1366459627329
    ACR             5   240.6
    FAM41C          19  294.7894736842105
    FAM87B          8   214.875
    LINC00115       1   122.0
    LINC01128       24  242.29166666666666
    LOC100288069    4   236.75
    LOC105373100    6   332.6666666666667
    RABL2B          22  219.5
    RPL23AP82       20  293.1

    

Here `count(*)` is used to count the number of variants in each gene, and `NA` is a special group for variants that do not belong to any gene, which can be confirmed by command 



    % vtools select variant 'refGene.chr is NULL' --output 'avg(DP)'
    

    281.1366459627329
    

Option `--all` should not be used in these commands because this option will lead to multiple entries for some variants, and biase the results. For example, the output of the following command differs from the previous one: 

    % vtools output variant refGene.name2 'count(*)' 'avg(DP)' --group_by refGene.name2 --all -l 10   

    .               161 281.1366459627329
    ACR             5   240.6
    FAM41C          19  294.7894736842105
    FAM87B          8   214.875
    LINC00115       1   122.0
    LINC01128       128 243.03125
    LOC100288069    4   236.75
    LOC105373100    6   332.6666666666667
    RABL2B          484 219.5
    RPL23AP82       44  256.22727272727275

    

</details>

{{% notice warning %}}
Using option `--all` along with aggregating function will most likely lead to erroneous results because the aggregating function will be applied to a dataset with duplicated entries, unless you intentionally would like to count, for example, number of duplicated entries for each variant.
{{% /notice %}}

 [1]: http://www.sqlite.org/contrib
 [2]: http://www.sqlite.org/lang_aggfunc.html