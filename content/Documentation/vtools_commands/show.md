+++
title = "show"
weight = 6
+++




## Display project and system information


### 1. Usage

    % vtools show -h
    
    usage: vtools show [-h] [-l N] [-v {0,1,2,3}]
                       [{project,tables,table,samples,phenotypes,genotypes,fields,annotations,annotation,track,formats,format,tests,test,runtime_options,runtime_option,snapshot,snapshots}]
                       [items [items ...]]
    
    Output information of all system and project related items such as variant
    tables, samples, phenotypes, annotation databases and fields.
    
    positional arguments:
      {project,tables,table,samples,phenotypes,genotypes,fields,annotations,annotation,track,formats,format,tests,test,runtime_options,runtime_option,snapshot,snapshots}
                            Type of information to display, which can be 'project'
                            for summary of a project, 'tables' for all variant
                            tables (or all tables if --verbosity=2), 'table TBL'
                            for details of a specific table TBL, 'samples [COND]'
                            for sample name, files from which samples are
                            imported, and associated phenotypes (can be supressed
                            by option --verbosity 0) of all or selected samples,
                            'phenotypes [P1 P2...]' for all or specified
                            phenotypes of samples, 'fields' for fields from
                            variant tables and all used annotation databases,
                            'annotations' for a list of all available annotation
                            databases, 'annotation ANN' for details about
                            annotation database ANN, 'track' for information of a
                            track file in tabixed vcf, bigWig, or bigBed format,
                            'formats' for all supported import and export formats,
                            'format FMT' for details of format FMT, 'tests' for a
                            list of all association tests, and 'test TST' for
                            details of an association test TST, 'runtime_options'
                            for a list of runtime options and their descriptions,
                            'runtime_option OPT' for value of specified runtime
                            option OPT, 'snapshot' for a particular snapshot by
                            name or filename, 'snapshots' for a list of publicly
                            available snapshots, and snapshots of the current
                            project saved by command 'vtools admin
                            --save_snapshots'. The default parameter of this
                            command is 'project'.
      items                 Items to display, which can be, for example, name of
                            table for type 'table', conditions to select samples
                            for type 'samples', a list of phenotypes for type
                            'phenotypes', name of an annotation database for type
                            'annotation', a pattern to selected annotation
                            databases for type 'annotations', name of a format for
                            type 'format', and name of an association test for
                            type 'test'.
    
    optional arguments:
      -h, --help            show this help message and exit
      -l N, --limit N       Limit output to the first N records.
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Output error and warning (0), info (1), debug (2) and
                            trace (3) information to standard output (default to
                            1).
    



### 2. Details

Command `` `vtools show `` displays various project and system information. It accepts type of item to display as its first parameter, followed by names of items if information about particular items are needed. Generally speaking: 



*   plural form of output type (e.g. `tables`, `tests`) lists all available items. Options are usually available to limit the items to display. 
*   single form of output type (e.g. `table`, `test`) list details of a single item. 
*   The verbosity level can be used to adjust output. For example, `-v0` can usually be used to suppress description of items, and `-v2` can be used to show more information. 



#### 2.1 Show project (`project`)

Command `` `vtools show `` without parameter and `` `vtools show project `` displays general information about a project, including project name, reference genome, existing variant tables, and used annotation databases. 

<details><summary> Examples: Show summary of a downloaded project</summary> 

Let us load a fairly large project from an online snapshot `vt_ExomeAssociation`, 



    % vtools init show
    % vtools admin --load_snapshot vt_ExomeAssociation   

    Downloading snapshot vt_ExomeAssociation.tar.gz from online
    INFO: Load genotypes
    INFO: Snapshot vt_ExomeAssociation has been loaded
    
    
    % vtools show
    
    Project name:                show
    Primary reference genome:    hg19
    Secondary reference genome:  None
    Runtime options:             verbosity=1
    Variant tables:              rare
                                 variant
    Annotation databases:
    

The project has 2 variant tables, the master variant table and another variant tables `rare`. It uses the hg19 reference genome, and has not been connected to any annotation database. 

</details>



#### 2.2 Show variant and other tables (`tables` and `table`)

Command `vtools show tables` lists all variant tables, their creation dates and comments (if available). This command does not accept any additional parameter. 

<details><summary> Examples: Show all variant tables </summary> 

    % vtools show tables 

    table      #variants     date  message
    rare          19,785    Jan24  rare variants
    variant       26,797
    

</details>

`vtools show tables` lists all variant tables of a project, with creation date and comment. If you only need to know information about a particular variant table, it is easier and faster to use command `vtools show table TABLE`. This command lists date of creation, a short description, number of variants and fields (only the master variant table has multiple fields). Perhaps more interestingly, it shows the command that has been used to create this variant table, which usually contain import information regarding from which table this table is drawn, and what criteria has been used. 

<details><summary> Examples: Show details of a variant table</summary> Show details of a table `rare`, note that you can specify multiple tables after command `vtools show table`. 

    % vtools show table rare   

    Name:                   rare
    Type:                   variant
    Description:            rare variants
    Creation date:          Jan24
    Command:                vtools select variant 'af<0.01 OR af>0.99' -t rare
                            'rare variants'
    Fields:                 variant_id
    Number of variants:     19785
    

</details>



#### 2.3 Show samples (`samples`)

Command `vtools show samples` lists samples, files from which samples are imported, and phenotypes associated with each samples. The command by default lists all samples and phenotypes, but you can list part of the information by 



*   Option `--limit` limit the output to the first few records 
*   Option `--samples` can limit the samples to those that match specified criteria 
*   Option `-v 0` (`--verbosity 0`) supress phenotypes. This is useful when there are a large number of phenotypes 
*   Option `-v 2` lists full filenames. The default output lists part of the filenames if they are too long. Increasing verbosity level will show complete information. 

<details><summary> Examples: Show all or selected samples, with or without phenotype</summary> Show all samples: 

    % vtools show samples -l 10

    sample_name  filename       gender  age  bmi          status  exposure
    SAMP10       assoctest.dat  1       44   27.93818994  0       0
    SAMP100      assoctest.dat  1       47   33.47268746  0       0
    SAMP1000     assoctest.dat  1       50   26.4845      0       0
    SAMP1001     assoctest.dat  2       59   24.02405     0       1
    SAMP1002     assoctest.dat  2       61   26.32636     0       0
    SAMP1003     assoctest.dat  1       49   24.4131      0       1
    SAMP1004     assoctest.dat  1       57   30.57549     0       0
    SAMP1005     assoctest.dat  2       57   28.40909     0       1
    SAMP1006     assoctest.dat  2       48   28.7642      0       0
    SAMP1007     assoctest.dat  1       65   24.14179     0       0
    (3170 records omitted)
    

Show only male samples using condition `gender=1` to select samples 

    % vtools show samples 'gender=1' -l 10
    
    sample_name  filename       gender  age  bmi          status  exposure
    SAMP10       assoctest.dat  1       44   27.93818994  0       0
    SAMP100      assoctest.dat  1       47   33.47268746  0       0
    SAMP1000     assoctest.dat  1       50   26.4845      0       0
    SAMP1003     assoctest.dat  1       49   24.4131      0       1
    SAMP1004     assoctest.dat  1       57   30.57549     0       0
    SAMP1007     assoctest.dat  1       65   24.14179     0       0
    SAMP1008     assoctest.dat  1       48   28.20037     0       1
    SAMP1010     assoctest.dat  1       56   23.67424     0       1
    SAMP1014     assoctest.dat  1       47   23.54056     0       0
    SAMP1016     assoctest.dat  1       60   23.8961      0       0
    (3170 records omitted)
    

Suppressing phenotypes and only show basic sample information 

    % vtools show samples  -l 10 -v0 

    sample_name  filename
    SAMP10       assoctest.dat
    SAMP100      assoctest.dat
    SAMP1000     assoctest.dat
    SAMP1001     assoctest.dat
    SAMP1002     assoctest.dat
    SAMP1003     assoctest.dat
    SAMP1004     assoctest.dat
    SAMP1005     assoctest.dat
    SAMP1006     assoctest.dat
    SAMP1007     assoctest.dat
    (3170 records omitted)
    

</details>



#### 2.4 Show all or selected phenotypes (`phenotypes`)

Command `vtools show phenotypes` is similar to `vtools show samples` but it does not show filename information and can display only specified phenotypes. 

<details><summary> Examples: Show all or selected phenotypes</summary> Show all phenotypes 

    % vtools show phenotypes -l 10

    sample_name  gender  age  bmi          status  exposure
    SAMP10       1       44   27.93818994  0       0
    SAMP100      1       47   33.47268746  0       0
    SAMP1000     1       50   26.4845      0       0
    SAMP1001     2       59   24.02405     0       1
    SAMP1002     2       61   26.32636     0       0
    SAMP1003     1       49   24.4131      0       1
    SAMP1004     1       57   30.57549     0       0
    SAMP1005     2       57   28.40909     0       1
    SAMP1006     2       48   28.7642      0       0
    SAMP1007     1       65   24.14179     0       0
    (3170 records omitted)
    

Show values of specified phenotypes 

    % vtools show phenotypes exposure -l 10
    
    sample_name  exposure
    SAMP10       0
    SAMP100      0
    SAMP1000     0
    SAMP1001     1
    SAMP1002     0
    SAMP1003     1
    SAMP1004     0
    SAMP1005     1
    SAMP1006     0
    SAMP1007     0
    (3170 records omitted)
    

</details>


{{% notice tip%}}
Another command `vtools phenotype --output` can also output selected phenotypes. It is more powerful in that it has better control of the format of output, and more importantly, allow output of summary statistics of phenotypes. 
{{%/notice %}}


#### 2.5 Show genotype information for each sample (`genotypes`)

Command `vtools show genotypes shows the number of genotypes and names of genotype info fields of each sample. Such information are useful for the calculation of summary statistics of genotypes (e.g. depth of coverage) using commands `vtools phenotype --from_stat` (statistics for each sample) and `vtools update --from_stat@@ (statistics for each variant). 

<details><summary> Examples: Show details of genotypes</summary> 

    % vtools show genotypes -l 10	
    
    sample_name  filename       num_genotypes  sample_genotype_fields
    SAMP2        assoctest.dat  26612          GT
    SAMP3        assoctest.dat  26613          GT
    SAMP4        assoctest.dat  26600          GT
    SAMP5        assoctest.dat  26600          GT
    SAMP6        assoctest.dat  26603          GT
    SAMP7        assoctest.dat  26584          GT
    SAMP8        assoctest.dat  26612          GT
    SAMP9        assoctest.dat  26585          GT
    SAMP10       assoctest.dat  26613          GT
    SAMP11       assoctest.dat  26588          GT
    (3170 records omitted)
    

</details>



#### 2.6 Show variant info and annotation fields (`fields`)

Command `vtools show fields`) lists all variant info fields (fields in the master variant table) and annotation fields (fields provided by annotation databases). Although these fields are from different sources, they can be used in the same manner to identify and filter variants (c.f. `vtools select`). If you only need to see a list of available fields, you can use option `-v0` to suppress comments. 

<details><summary> Examples: Show all variant info and annotation fields</summary> This project uses annotation database `knownGene` so all fields from that database are available in the project: 

    % vtools show fields
    
    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of
                            an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of
                            an deletion)
    variant.cnt (int)
    variant.hom (int)
    variant.het (int)
    variant.other (int)
    variant.num (int)
    variant.missing (int)
    variant.wtGT (int)
    variant.mutGT (int)
    variant.af (float)


You can use option `-v0` to suppress comments (which can be long): 

    % vtools show fields -v0 

    variant.chr
    variant.pos
    variant.ref
    variant.alt
    variant.cnt
    variant.hom
    variant.het
    variant.other
    variant.num
    variant.missing
    variant.wtGT
    variant.mutGT
    variant.af

</details>



#### 2.7 Show annotation databases (`annotations` and `annotation`)

Command `vtools show annotations` displays all available annotation databases with their descriptions. Because of the growing number of annotation databases, the output of this command can be very long. You can however 

*   Limit the databases by specifying a number of patterns. A database is eligible if its name contains any of the patterns. 
*   Use option `--limit` to limit the number of annotation database displayed, or 
*   Use option `-v 0` to suppress descriptions of databases. 

<details><summary> Examples: Show all annotation databases</summary> Show all annotation databases. With this command, `variant tools` connects to its ftp server and list all available annotation databases. 



    % vtools show annotations | head -50
    
    CancerGeneCensus-20111215 Cancer Genome Project
    CancerGeneCensus-20120315 Cancer Genome Project
    CancerGeneCensus        Cancer Genome Project
    CosmicCodingMuts-v61_260912 Cosmic coding mutation database.  This data
                            contains mutations affecting 10 or less nucleotides in
                            REF.  The mutation data was obtained from the Sanger
                            Institute Catalogue Of Somatic Mutations In Cancer web
                            site, http://www.sanger.ac.uk/cosmic.  Bamford et al
                            (2004). The COSMIC (Catalogue of Somatic Mutations in
                            Cancer) database and website. Br J Cancer, 91,355-358.
    CosmicCodingMuts        Cosmic coding mutation database.  This data contains
                            mutations affecting 10 or less nucleotides in REF.
                            The mutation data was obtained from the Sanger
                            Institute Catalogue Of Somatic Mutations In Cancer web
                            site, http://www.sanger.ac.uk/cosmic.  Bamford et al
                            (2004). The COSMIC (Catalogue of Somatic Mutations in
                            Cancer) database and website. Br J Cancer, 91,355-358.
    CosmicMutantExport-v61_260912 Cosmic mutant export.  This data contains all
                            coding point mutations.  The mutation data was
                            obtained from the Sanger Institute Catalogue Of
                            Somatic Mutations In Cancer web site,
                            http://www.sanger.ac.uk/cosmic.  Bamford et al (2004).
                            The COSMIC (Catalogue of Somatic Mutations in Cancer)
                            database and website. Br J Cancer, 91,355-358.
    CosmicMutantExport      Cosmic mutant export.  This data contains all coding
                            point mutations.  The mutation data was obtained from
                            the Sanger Institute Catalogue Of Somatic Mutations In
                            Cancer web site, http://www.sanger.ac.uk/cosmic.
                            Bamford et al (2004). The COSMIC (Catalogue of Somatic
                            Mutations in Cancer) database and website. Br J
                            Cancer, 91,355-358.
    CosmicNonCodingVariants-v61_260912 Cosmic non-coding mutation database.  This
                            data contains mutations affecting 10 or less
                            nucleotides in REF.  The mutation data was obtained
                            from the Sanger Institute Catalogue Of Somatic
                            Mutations In Cancer web site,
                            http://www.sanger.ac.uk/cosmic.  Bamford et al (2004).
                            The COSMIC (Catalogue of Somatic Mutations in Cancer)
                            database and website. Br J Cancer, 91,355-358.
    CosmicNonCodingVariants Cosmic non-coding mutation database.  This data
                            contains mutations affecting 10 or less nucleotides in
                            REF.  The mutation data was obtained from the Sanger
                            Institute Catalogue Of Somatic Mutations In Cancer web
                            site, http://www.sanger.ac.uk/cosmic.  Bamford et al
                            (2004). The COSMIC (Catalogue of Somatic Mutations in
                            Cancer) database and website. Br J Cancer, 91,355-358.
    ccdsGene-hg19_20110909  CCDS Genes
    ccdsGene-hg19_20111206  CCDS Genes
    ccdsGene                CCDS Genes
    ccdsGene_exon-hg19_20110909 CCDS exons
    

You can list a subset of annotation databases by specifying one or more patterns: 



    % vtools show annotations thousand ccds
    
    ccdsGene-hg19_20110909  CCDS Genes
    ccdsGene-hg19_20111206  CCDS Genes
    ccdsGene-hg19_20130904  High-confidence human gene annotations from the Consensus Coding
                            Sequence (CCDS) project.
    ccdsGene-hg38_20171008  High-confidence human gene annotations from the Consensus Coding
                            Sequence (CCDS) project.
    ccdsGene_exon-hg19_20110909 CCDS exons
    ccdsGene_exon-hg19_20111206 CCDS exons
    ccdsGene_exon-hg19_20130904 High-confidence human gene annotations from the Consensus Coding
                            Sequence (CCDS) project. This database contains all exon regions of the
                            CCDS genes.
    ccdsGene_exon-hg38_20171008 CCDS exons
    ccdsGene_exon_hg19-20111206 CCDS exons
    ccdsGene_hg19-20111206  CCDS Genes
    thousandGenomes-hg19_20130502 Phase 3 data of the thousand genomes project, created from
                            ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20130502/ALL.wgs.p
                            hase3_shapeit2_mvncall_integrated_v5a.20130502.sites.vcf.gz
    thousandGenomes-hg19_v3_20101123 1000 Genomes VCF file analyzed in March 2012 from data
                            generated from phase 1 of the project (available from: ftp://ftp.1000ge
                            nomes.ebi.ac.uk/vol1/ftp/release/20110521/ALL.wgs.phase1_release_v3.201
                            01123.snps_indels_sv.sites.vcf.gz).
    thousandGenomes-hg19_v5b_20130502 1000 Genomes VCF file analyzed in February 2015 from data
                            generated from phase 1 of the project (available from: ftp://ftp.1000ge
                            nomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.wgs.phase3_shapeit2_mvnca
                            ll_integrated_v5b.20130502.sites.vcf.gz.)
    

If you only need to see a list annotation databases without description, you can pass the `-v0` option, 

    % vtools show annotations gene -v0
    
    CancerGeneCensus-20111215
    CancerGeneCensus-20120315
    CancerGeneCensus-20130711
    CancerGeneCensus-20170912
    EntrezGene-20131028
    EntrezGene-20170919
    EntrezGene2RefSeq-20131028
    EntrezGene2RefSeq-20170919
    ccdsGene-hg19_20110909
    ccdsGene-hg19_20111206
    ccdsGene-hg19_20130904
    ccdsGene-hg38_20171008
    ccdsGene_exon-hg19_20110909
    ccdsGene_exon-hg19_20111206
    ccdsGene_exon-hg19_20130904
    ccdsGene_exon-hg38_20171008
    ccdsGene_exon_hg19-20111206
    ccdsGene_hg19-20111206
    dbNSFP_gene-2_0
    dbNSFP_gene-2_1
    dbNSFP_gene-2_3
    dbNSFP_gene-2_4
    dbNSFP_gene-2_7
    dbNSFP_gene-3_5a
    knownGene-hg18_20110909
    knownGene-hg18_20121219
    knownGene-hg19_20110909
    knownGene-hg19_20121219
    knownGene-hg19_20130904
    knownGene-hg38_20160328
    knownGene_exon-hg18_20110909
    knownGene_exon-hg19_20110909
    knownGene_exon-hg19_20130904
    knownGene_exon-hg38_20160328
    refGene-hg18_20110909
    refGene-hg19_20110909
    refGene-hg19_20130904
    refGene-hg38_20170201
    refGene-mm10_20141201
    refGene_coding-hg19_20130904
    refGene_exon-hg18_20110909
    refGene_exon-hg19_20110909
    refGene_exon-hg19_20130904
    refGene_exon-mm10_20141201
    refGene_exon-mm10_20171008

</details>

After using an annotation database with command `vtools use`, you can view the details of the annotation database using command `vtools show annotation ANNODB`. By default, this command displays basic information of the annotation database (type, number of records etc), and name and comment of each annotation field. If an `-v 2` option is specified, it will also list the details of each fields, including range, unique values, and number of missing values. 

<details><summary> Examples: Show details of an annotation database</summary> 

    % vtools show annotation knownGene   

    Annotation database knownGene (version hg19_20121219)
    Description:            UCSC Known Genes
    Database type:          range
    Reference genome hg19:  chr, txStart, txEnd
      name                  Name of gene such as uc001aaa.3
      chr
      strand                which DNA strand contains the observed alleles
      txStart               Transcription start position
      txEnd                 Transcription end position
      cdsStart              Coding region start
      cdsEnd                Coding region end
      exonCount             Number of exons
    



    % vtools show annotation knownGene -v2
    
    DEBUG: 
    DEBUG: show annotation knownGene -v2
    DEBUG: Using temporary directory /tmp/tmp3fjnagg2/_tmp_135971
    Annotation database knownGene (version hg19_20130904)
    Description:            Gene predictions based on data from RefSeq, Genbank, CCDS and UniProt, from the
      UCSC KnownGene track.
    Database type:          range
    Number of records:      82,960
    Distinct ranges:        60,726
    Reference genome hg19:  chr, txStart, txEnd

    Field:                  name
    Type:                   string
    Comment:                Name of gene such as uc001aaa.3
    Missing entries:        0 
    Unique Entries:         82,960

    Field:                  chr
    Type:                   string
    Missing entries:        0 
    Unique Entries:         60

    Field:                  strand
    Type:                   string
    Comment:                which DNA strand contains the observed alleles
    Missing entries:        0 
    Unique Entries:         2

    Field:                  txStart
    Type:                   integer
    Comment:                Transcription start position
    Missing entries:        0 
    Unique Entries:         48,720
    Range:                  1 - 249211537

    Field:                  txEnd
    Type:                   integer
    Comment:                Transcription end position
    Missing entries:        0 
    Unique Entries:         48,713
    Range:                  368 - 249213345

    Field:                  cdsStart
    Type:                   integer
    Comment:                Coding region start
    Missing entries:        0 
    Unique Entries:         51,789
    Range:                  1 - 249211537

    Field:                  cdsEnd
    Type:                   integer
    Comment:                Coding region end
    Missing entries:        0 
    Unique Entries:         51,745
    Range:                  0 - 249212562

    Field:                  exonCount
    Type:                   integer
    Comment:                Number of exons
    Missing entries:        0 
    Unique Entries:         119
    Range:                  1 - 5065
    

</details>



#### 2.8 Show details of annotation tracks (`track`)

*variant tools* supports the use of annotation tracks to annotate and select variants. These tracks can be in tabix-indexed vcf files, indexed BAM file, bigBed and bigWig format and provides differnt fields through the second parameter of function `track(filename, field)`. Command `vtools show track` is provided to display the details of each track file. 

<details><summary> Examples: show details of a local vcf track </summary> Show details of a local vcf track file: 



    % vtools show track CEU_hg38.vcf | head -30
    
    Version                 VCF v4.0
    Number of fields:       69
    
    Header: (exclude INFO and FORMAT lines)
                            ##reference=human_b36_both.fasta
                            ##rsIDs=dbSNP b129 mapped to NCBI 36.3, August 10, 2009
    
    Available columns (with default type VARCHAR):
    0 (INTEGER)             1 if matched
    chr (1, chrom)          chromosome
    pos (2 for INTEGER)     position (1-based)
    name (3)                name of variant
    ref (4)                 reference allele
    alt (5)                 alternative alleles
    qual (6)                qual
    filter (7)              filter
    info (8, default)       variant info fields
    info.DP                 Total Depth
    info.HM2                HapMap2 membership
    info.HM3                HapMap3 membership
    info.AA                 Ancestral Allele, ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/pilot_data/technical/reference/ancestral_alignments/README
    info.AC                 Allele count in genotypes
    info.AN                 Total number of alleles in called genotypes
    format (9)              genotype format
    NA06985 (10)            genotype for sample NA06985
    NA06985.GT              Genotype for sample NA06985
    NA06985.DP              Read Depth for sample NA06985
    NA06985.CB              Called by S(Sanger), M(UMich), B(BI) for sample NA06985
    NA06986 (11)            genotype for sample NA06986
    NA06986.GT              Genotype for sample NA06986
    

</details>


{{% notice tip%}}
Although cannot be used as track files, `vtools show track` can display information of plain vcf file (not compressed, with extension `.vcf`), which can be used to show useful information of the header of such files. 
{{% /notice%}}
<details><summary> Examples: show details of an online vcf track </summary> 



    % vtools show track http://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20110521/ALL.chr1.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz | head -30
    

    Version                 VCF v4.1
    Number of fields:       1101
    
    Header: (exclude INFO and FORMAT lines)
                            ##ALT=<ID=DEL,Description="Deletion">
                            ##reference=GRCh37
                            ##reference=GRCh37
    
    Available columns (with default type VARCHAR):
    0 (INTEGER)             1 if matched
    chr (1, chrom)          chromosome
    pos (2 for INTEGER)     position (1-based)
    name (3)                name of variant
    ref (4)                 reference allele
    alt (5)                 alternative alleles
    qual (6)                qual
    filter (7)              filter
    info (8, default)       variant info fields
    info.LDAF               MLE Allele Frequency Accounting for LD
    info.AVGPOST            Average posterior probability from MaCH/Thunder
    info.RSQ                Genotype imputation quality from MaCH/Thunder
    info.ERATE              Per-marker Mutation rate from MaCH/Thunder
    info.THETA              Per-marker Transition rate from MaCH/Thunder
    info.CIEND              Confidence interval around END for imprecise variants
    info.CIPOS              Confidence interval around POS for imprecise variants
    info.END                End position of the variant described in this record
    info.HOMLEN             Length of base pair identical micro-homology at event breakpoints
    info.HOMSEQ             Sequence of base pair identical micro-homology at event breakpoints
    info.SVLEN              Difference in length between REF and ALT alleles
    info.SVTYPE             Type of structural variant
    

</details>

<details><summary> Examples: show details of a bigBed track </summary> 



    % vtools show track wgEncodeDukeDnase8988T.fdr01peaks.hg19.bb  

    Version:                4
    Item count:             196180
    Primary data size:      1806867
    Zoom levels:            8
    Chrom count:            23
    Chrom size:
        chr1                249250621
        chr10               135534747
        chr11               135006516
        chr12               133851895
        chr13               115169878
        chr14               107349540
        chr15               102531392
        chr16               90354753
        chr17               81195210
        chr18               78077248
        chr19               59128983
        chr2                243199373
        chr20               63025520
        chr21               48129895
        chr22               51304566
        chr3                198022430
        chr4                191154276
        chr5                180915260
        chr6                171115067
        chr7                159138663
        chr8                146364022
        chr9                141213431
        chrX                155270560
    Bases covered           29405430
    Mean depth:             1.000734
    Min depth:              1.000000
    Max depth:              2.000000
    Std of depth:           0.027074
    Number of fields:       10
    
    Available columns (with default type VARCHAR):
    chrom (1)               Name of the chromosome (or contig, scaffold, etc.).
    chromStart (2 as INTEGER) The starting position of the feature in the chromosome
                            or scaffold. The first base in a chromosome is numbered
                            0.
    chromEnd (3 as INTEGER) The ending position of the feature in the chromosome or
                            scaffold. The chromEnd base is not included in the display
                            of the feature. For example, the first 100 bases of a chromosome
                            are defined as chromStart=0, chromEnd=100, and span the
                            bases numbered 0-99.
    name (4)                Name given to a region (preferably unique). Use '.' if no
                            name is assigned.
    score (5 as INTEGER)    Indicates how dark the peak will be displayed in the browser
                            (0-1000). If all scores were '0' when the data were submitted
                            to the DCC, the DCC assigned scores 1-1000 based on signal
                            value. Ideally the average signalValue per base spread
                            is between 100-1000.
    strand (6)              +/- to denote strand or orientation (whenever applicable).
                            Use '.' if no orientation is assigned.
    signalValue (7 as FLOAT) Measurement of overall (usually, average) enrichment for
                            the region
    pValue (8 as FLOAT)     Measurement of statistical significance (-log10, -1 if no
                            pValue is assigned)
    qValue (9 as FLOAT)     Measurement of statistical significance using false discovery
                            rate (-log10, -1 if no qValue is assigned)
    peak (10 as INTEGER)    Point-source called for this peak; 0-based offset from chromStart
                            (-1 if no point-source called)
    

</details>

<details><summary> Examples: show details of a bigWig track </summary> 



    % vtools show track ~/vtools/wgEncodeGisRnaSeqH1hescCellPapPlusRawRep1.bigWig
    

    Version:                4
    Primary data size       226114375
    Zoom levels:            10
    Chrom count:            25
    Chrom size:
        chr1                249250621
        chr10               135534747
        chr11               135006516
        chr12               133851895
        chr13               115169878
        chr14               107349540
        chr15               102531392
        chr16               90354753
        chr17               81195210
        chr18               78077248
        chr19               59128983
        chr2                243199373
        chr20               63025520
        chr21               48129895
        chr22               51304566
        chr3                198022430
        chr4                191154276
        chr5                180915260
        chr6                171115067
        chr7                159138663
        chr8                146364022
        chr9                141213431
        chrM                16571
        chrX                155270560
        chrY                59373566
    Bases covered:          84281746
    Mean:                   10.253978
    Min:                    1.000000
    Max:                    46751.000000
    std:                    119.977095
    Number of fields:       4
    
    Available columns (with default type VARCHAR):
    0 (INTEGER)             1 if matched
    chrom (1)               chromosome
    chromStart (2 as INTEGER) start position (0-based)
    chromEnd (3 as INTEGER) end position (1-based)
    value (4 as FLOAT)      value
    

</details>

<details><summary> Examples: show details of an online BAM track </summary> For indexed BAM file, this command lists the header of the BAM file, size of chromosomes, and available fields: 



    % vtools show track ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data/HG00096/alignment/HG00096.chrom11.ILLUMINA.bwa.GBR.low_coverage.20120522.bam 

    [bam_index_load] attempting to download the remote index file.
    [bam_index_load] attempting to download the remote index file.
    Header:
    @HD	VN:1.0	SO:coordinate
    @SQ	SN:1	LN:249250621	M5:1b22b98cdeb4a9304cb5d48026a85128	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:2	LN:243199373	M5:a0d9851da00400dec1098a9255ac712e	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:3	LN:198022430	M5:fdfd811849cc2fadebc929bb925902e5	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:4	LN:191154276	M5:23dccd106897542ad87d2765d28a19a1	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:5	LN:180915260	M5:0740173db9ffd264d728f32784845cd7	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:6	LN:171115067	M5:1d3a93a248d92a729ee764823acbbc6b	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:7	LN:159138663	M5:618366e953d6aaad97dbe4777c29375e	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:8	LN:146364022	M5:96f514a9929e410c6651697bded59aec	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:9	LN:141213431	M5:3e273117f15e0a400f01055d9f393768	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:10	LN:135534747	M5:988c28e000e84c26d552359af1ea2e1d	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:11	LN:135006516	M5:98c59049a2df285c76ffb1c6db8f8b96	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:12	LN:133851895	M5:51851ac0e1a115847ad36449b0015864	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:13	LN:115169878	M5:283f8d7892baa81b510a015719ca7b0b	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:14	LN:107349540	M5:98f3cae32b2a2e9524bc19813927542e	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:15	LN:102531392	M5:e5645a794a8238215b2cd77acb95a078	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:16	LN:90354753	M5:fc9b1a7b42b97a864f56b348b06095e6	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:17	LN:81195210	M5:351f64d4f4f9ddd45b35336ad97aa6de	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:18	LN:78077248	M5:b15d4b2d29dde9d3e4f93d1d0f2cbc9c	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:19	LN:59128983	M5:1aacd71f30db8e561810913e0b72636d	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:20	LN:63025520	M5:0dec9660ec1efaaf33281c0d5ea2560f	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:21	LN:48129895	M5:2979a6085bfe28e3ad6f552f361ed74d	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:22	LN:51304566	M5:a718acaa6135fdca8357d5bfe94211dd	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:X	LN:155270560	M5:7e0e2e580297b7764e31dbc80c2540dd	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:Y	LN:59373566	M5:1fa3474750af0948bdf97d5a0ee52e51	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:MT	LN:16569	M5:c68f52674c9fb33aef52dcf399755519	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000207.1	LN:4262	M5:f3814841f1939d3ca19072d9e89f3fd7	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000226.1	LN:15008	M5:1c1b2cd1fccbc0a99b6a447fa24d1504	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000229.1	LN:19913	M5:d0f40ec87de311d8e715b52e4c7062e1	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000231.1	LN:27386	M5:ba8882ce3a1efa2080e5d29b956568a4	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000210.1	LN:27682	M5:851106a74238044126131ce2a8e5847c	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000239.1	LN:33824	M5:99795f15702caec4fa1c4e15f8a29c07	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000235.1	LN:34474	M5:118a25ca210cfbcdfb6c2ebb249f9680	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000201.1	LN:36148	M5:dfb7e7ec60ffdcb85cb359ea28454ee9	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000247.1	LN:36422	M5:7de00226bb7df1c57276ca6baabafd15	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000245.1	LN:36651	M5:89bc61960f37d94abf0df2d481ada0ec	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000197.1	LN:37175	M5:6f5efdd36643a9b8c8ccad6f2f1edc7b	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000203.1	LN:37498	M5:96358c325fe0e70bee73436e8bb14dbd	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000246.1	LN:38154	M5:e4afcd31912af9d9c2546acf1cb23af2	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000249.1	LN:38502	M5:1d78abec37c15fe29a275eb08d5af236	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000196.1	LN:38914	M5:d92206d1bb4c3b4019c43c0875c06dc0	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000248.1	LN:39786	M5:5a8e43bec9be36c7b49c84d585107776	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000244.1	LN:39929	M5:0996b4475f353ca98bacb756ac479140	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000238.1	LN:39939	M5:131b1efc3270cc838686b54e7c34b17b	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000202.1	LN:40103	M5:06cbf126247d89664a4faebad130fe9c	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000234.1	LN:40531	M5:93f998536b61a56fd0ff47322a911d4b	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000232.1	LN:40652	M5:3e06b6741061ad93a8587531307057d8	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000206.1	LN:41001	M5:43f69e423533e948bfae5ce1d45bd3f1	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000240.1	LN:41933	M5:445a86173da9f237d7bcf41c6cb8cc62	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000236.1	LN:41934	M5:fdcd739913efa1fdc64b6c0cd7016779	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000241.1	LN:42152	M5:ef4258cdc5a45c206cea8fc3e1d858cf	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000243.1	LN:43341	M5:cc34279a7e353136741c9fce79bc4396	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000242.1	LN:43523	M5:2f8694fc47576bc81b5fe9e7de0ba49e	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000230.1	LN:43691	M5:b4eb71ee878d3706246b7c1dbef69299	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000237.1	LN:45867	M5:e0c82e7751df73f4f6d0ed30cdc853c0	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000233.1	LN:45941	M5:7fed60298a8d62ff808b74b6ce820001	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000204.1	LN:81310	M5:efc49c871536fa8d79cb0a06fa739722	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000198.1	LN:90085	M5:868e7784040da90d900d2d1b667a1383	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000208.1	LN:92689	M5:aa81be49bf3fe63a79bdc6a6f279abf6	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000191.1	LN:106433	M5:d75b436f50a8214ee9c2a51d30b2c2cc	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000227.1	LN:128374	M5:a4aead23f8053f2655e468bcc6ecdceb	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000228.1	LN:129120	M5:c5a17c97e2c1a0b6a9cc5a6b064b714f	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000214.1	LN:137718	M5:46c2032c37f2ed899eb41c0473319a69	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000221.1	LN:155397	M5:3238fb74ea87ae857f9c7508d315babb	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000209.1	LN:159169	M5:f40598e2a5a6b26e84a3775e0d1e2c81	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000218.1	LN:161147	M5:1d708b54644c26c7e01c2dad5426d38c	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000220.1	LN:161802	M5:fc35de963c57bf7648429e6454f1c9db	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000213.1	LN:164239	M5:9d424fdcc98866650b58f004080a992a	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000211.1	LN:166566	M5:7daaa45c66b288847b9b32b964e623d3	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000199.1	LN:169874	M5:569af3b73522fab4b40995ae4944e78e	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000217.1	LN:172149	M5:6d243e18dea1945fb7f2517615b8f52e	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000216.1	LN:172294	M5:642a232d91c486ac339263820aef7fe0	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000215.1	LN:172545	M5:5eb3b418480ae67a997957c909375a73	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000205.1	LN:174588	M5:d22441398d99caf673e9afb9a1908ec5	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000219.1	LN:179198	M5:f977edd13bac459cb2ed4a5457dba1b3	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000224.1	LN:179693	M5:d5b2fc04f6b41b212a4198a07f450e20	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000223.1	LN:180455	M5:399dfa03bf32022ab52a846f7ca35b30	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000195.1	LN:182896	M5:5d9ec007868d517e73543b005ba48535	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000212.1	LN:186858	M5:563531689f3dbd691331fd6c5730a88b	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000222.1	LN:186861	M5:6fe9abac455169f50470f5a6b01d0f59	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000200.1	LN:187035	M5:75e4c8d17cd4addf3917d1703cacaf25	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000193.1	LN:189789	M5:dbb6e8ece0b5de29da56601613007c2a	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000194.1	LN:191469	M5:6ac8f815bf8e845bb3031b73f812c012	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000225.1	LN:211173	M5:63945c3e6962f28ffd469719a747e73c	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:GL000192.1	LN:547496	M5:325ba9e808f669dfeee210fdd7b470ac	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:NC_007605	LN:171823	M5:6743bd63b3ff2b5b8985d8933c53290a	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @SQ	SN:hs37d5	LN:35477943	M5:5b6a4b3a81a2d3c134b7d14bf6ad39f1	UR:ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz        AS:NCBI37       SP:Human
    @RG	ID:SRR062634	LB:2845856850	SM:HG00096	PI:206	CN:WUGSC	PL:ILLUMINA	DS:SRP001294
    @RG	ID:SRR062635	LB:2845856850	SM:HG00096	PI:206	CN:WUGSC	PL:ILLUMINA	DS:SRP001294
    @RG	ID:SRR062641	LB:2845856850	SM:HG00096	PI:206	CN:WUGSC	PL:ILLUMINA	DS:SRP001294
    @PG	ID:bwa_index	PN:bwa	VN:0.5.9-r16	CL:bwa index -a bwtsw $reference_fasta
    @PG	ID:bwa_aln_fastq	PN:bwa	PP:bwa_index	VN:0.5.9-r16	CL:bwa aln -q 15 -f $sai_file $reference_fasta $fastq_file
    @PG	ID:bwa_sam	PN:bwa	PP:bwa_aln_fastq	VN:0.5.9-r16	CL:bwa sampe -a 618 -r $rg_line -f $sam_file $reference_fasta $sai_file(s) $fastq_file(s)
    @PG	ID:sam_to_fixed_bam	PN:samtools	PP:bwa_sam	VN:0.1.17 (r973:277)	CL:samtools view -bSu $sam_file | samtools sort -n -o - samtools_nsort_tmp | samtools fixmate /dev/stdin /dev/stdout | samtools sort -o - samtools_csort_tmp | samtools fillmd -u - $reference_fasta > $fixed_bam_file
    @PG	ID:gatk_target_interval_creator	PN:GenomeAnalysisTK	PP:sam_to_fixed_bam	VN:1.2-29-g0acaf2d	CL:java $jvm_args -jar GenomeAnalysisTK.jar -T RealignerTargetCreator -R $reference_fasta -o $intervals_file -known $known_indels_file(s)
    @PG	ID:bam_realignment_around_known_indels	PN:GenomeAnalysisTK	PP:gatk_target_interval_creator	VN:1.2-29-g0acaf2d	CL:java $jvm_args -jar GenomeAnalysisTK.jar -T IndelRealigner -R $reference_fasta -I $bam_file -o $realigned_bam_file -targetIntervals $intervals_file -known $known_indels_file(s) -LOD 0.4 -model KNOWNS_ONLY -compress 0 --disable_bam_indexing
    @PG	ID:bam_count_covariates	PN:GenomeAnalysisTK	PP:bam_realignment_around_known_indels	VN:1.2-29-g0acaf2d	CL:java $jvm_args -jar GenomeAnalysisTK.jar -T CountCovariates -R $reference_fasta -I $bam_file -recalFile $bam_file.recal_data.csv -knownSites $known_sites_file(s) -l INFO -L '1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;X;Y;MT' -cov ReadGroupCovariate -cov QualityScoreCovariate -cov CycleCovariate -cov DinucCovariate
    @PG	ID:bam_recalibrate_quality_scores	PN:GenomeAnalysisTK	PP:bam_count_covariates	VN:1.2-29-g0acaf2d	CL:java $jvm_args -jar GenomeAnalysisTK.jar -T TableRecalibration -R $reference_fasta -recalFile $bam_file.recal_data.csv -I $bam_file -o $recalibrated_bam_file -l INFO -compress 0 --disable_bam_indexing
    @PG	ID:bam_calculate_bq	PN:samtools	PP:bam_recalibrate_quality_scores	VN:0.1.17 (r973:277)	CL:samtools calmd -Erb $bam_file $reference_fasta > $bq_bam_file
    @PG	ID:bam_merge	PN:picard	PP:bam_calculate_bq	VN:1.53	CL:java $jvm_args -jar MergeSamFiles.jar INPUT=$bam_file(s) OUTPUT=$merged_bam VALIDATION_STRINGENCY=SILENT
    @PG	ID:bam_mark_duplicates	PN:picard	PP:bam_merge	VN:1.53	CL:java $jvm_args -jar MarkDuplicates.jar INPUT=$bam_file OUTPUT=$markdup_bam_file ASSUME_SORTED=TRUE METRICS_FILE=/dev/null VALIDATION_STRINGENCY=SILENT
    @PG	ID:bam_merge.1	PN:picard	PP:bam_mark_duplicates	VN:1.53	CL:java $jvm_args -jar MergeSamFiles.jar INPUT=$bam_file(s) OUTPUT=$merged_bam VALIDATION_STRINGENCY=SILENT
    @CO	$known_indels_file(s) = ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_mapping_resources/ALL.wgs.indels_mills_devine_hg19_leftAligned_collapsed_double_hit.indels.sites.vcf.gz
    @CO	$known_indels_file(s) .= ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_mapping_resources/ALL.wgs.low_coverage_vqsr.20101123.indels.sites.vcf.gz
    @CO	$known_sites_file(s) = ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_mapping_resources/ALL.wgs.dbsnp.build135.snps.sites.vcf.gz
    
    Chrom size:             86
        1                   249250621
        2                   243199373
        3                   198022430
        4                   191154276
        5                   180915260
        6                   171115067
        7                   159138663
        8                   146364022
        9                   141213431
        10                  135534747
        11                  135006516
        12                  133851895
        13                  115169878
        14                  107349540
        15                  102531392
        16                  90354753
        17                  81195210
        18                  78077248
        19                  59128983
        20                  63025520
        21                  48129895
        22                  51304566
        X                   155270560
        Y                   59373566
        MT                  16569
        GL000207.1          4262
        GL000226.1          15008
        GL000229.1          19913
        GL000231.1          27386
        GL000210.1          27682
        GL000239.1          33824
        GL000235.1          34474
        GL000201.1          36148
        GL000247.1          36422
        GL000245.1          36651
        GL000197.1          37175
        GL000203.1          37498
        GL000246.1          38154
        GL000249.1          38502
        GL000196.1          38914
        GL000248.1          39786
        GL000244.1          39929
        GL000238.1          39939
        GL000202.1          40103
        GL000234.1          40531
        GL000232.1          40652
        GL000206.1          41001
        GL000240.1          41933
        GL000236.1          41934
        GL000241.1          42152
        GL000243.1          43341
        GL000242.1          43523
        GL000230.1          43691
        GL000237.1          45867
        GL000233.1          45941
        GL000204.1          81310
        GL000198.1          90085
        GL000208.1          92689
        GL000191.1          106433
        GL000227.1          128374
        GL000228.1          129120
        GL000214.1          137718
        GL000221.1          155397
        GL000209.1          159169
        GL000218.1          161147
        GL000220.1          161802
        GL000213.1          164239
        GL000211.1          166566
        GL000199.1          169874
        GL000217.1          172149
        GL000216.1          172294
        GL000215.1          172545
        GL000205.1          174588
        GL000219.1          179198
        GL000224.1          179693
        GL000223.1          180455
        GL000195.1          182896
        GL000212.1          186858
        GL000222.1          186861
        GL000200.1          187035
        GL000193.1          189789
        GL000194.1          191469
        GL000225.1          211173
        GL000192.1          547496
        NC_007605           171823
        hs37d5              35477943
    
    Tags that can be outputed or used in filters, with values from the 1st record:
    X0                      c (int8)   : 10
    X1                      c (int8)   : 0
    MD                      Z (string) : 0A99
    RG                      Z (string) : SRR062634
    AM                      c (int8)   : 0
    NM                      c (int8)   : 1
    SM                      c (int8)   : 0
    MQ                      c (int8)   : 0
    XT                      A (char)   : R
    BQ                      Z (string) : C[Y@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    Parameters min_qual, min_mapq and TAG=VAL can be used to limit the reads to the
    ones with mapq and qual scores that exceed the specified value, and with specified TAG.
    

</details>


{{% notice tip%}}
The header of BAM track provides many important information about the bam file. You should consult the SAM format specification for the meaning of them, but briefly: 


*   `HD - header`: `VN` is for file format version, `SO` for sort order, which can be unsorted, queryname or coordinate. 
*   `SQ - Sequence dictionary`: `SN` is sequence name, @LN` is sequence length. This might repeat the chromome length information listed below. `AS` reference genome used for assembly, `SP@@ for species. 
*   `RG - Read group`: `ID` for read group identifier, `SM` for sample, `LB` for library, `DS` for description, `PU` for platform unit, `DT` for date the run was produced, `PL` for platform (e.g. illumina). 
*   `PG - Program`: `ID` for program name, `VN` for program version, `CL` for command line. 
*   `CO - Comment` 
{{% /notice %}}

{{% notice tip%}}
The tags are also important if you need to filter reads by tag values. For example, `RG` can be used to differentiate reads that belong to different samples if the bam file contains reads from multiple samples. 

{{% /notice %}}


#### 2.9 Show supported input and output file formats (`formats` and `format`)

*variant tools* repository has a number of file format description files `.fmt` that defines a formats of files that can be used for commands `vtools import`, `vtools update --from_file`, and `vtools export`. To get a complete list of supported file formats, you can use command `vtools show formats`. Options `-v0` and `--limit` are supported to suppress comment and limit number of formats to display, respectively. 

<details><summary> Examples: Show a list of supported input/output file formats</summary> Command `vtools show formats` display a long list of file formats that are supported by variant tools: 

    % vtools show formats | head -50
    
    CASAVA18_snps           Input format illumina snps.txt file, created by CASAVA
                            version 1.8
                            (http://www.illumina.com/support/documentation.ilmn).
                            This format imports chr, pos, ref, alt of most likely
                            genotype, and a Q score for the most likely genotype.
    plink                   Input format for PLINK dataset. Currently only PLINK
                            binary PED file format is supported (*.bed, *.bim &
                            *.fam)
    ANNOVAR                 Input format of ANNOVAR. No genotype is defined.
    pileup_indel            Input format for samtools pileup indel caller. This
                            format imports chr, pos, ref, alt and genotype.
    ANNOVAR_exonic_variant_function Output from ANNOVAR, generated from command
                            "path/to/annovar/annotate_variation.pl annovar.txt
                            path/to/annovar/humandb/". This format imports chr,
                            pos, ref, alt and ANNOVAR annotations. For details
                            please refer to http://www.openbioinformatics.org/anno
                            var/annovar_gene.html
    ANNOVAR_variant_function Output from ANNOVAR for files of type
                            "*.variant_function", generated from command
                            "path/to/annovar/annotate_variation.pl annovar.txt
                            path/to/annovar/humandb/". This format imports chr,
                            pos, ref, alt and ANNOVAR annotations. For details
                            please refer to http://www.openbioinformatics.org/anno
                            var/annovar_gene.html
    CGA                     Input format from Complete Genomics Variant file
                            masterVarBeta-[ASM-ID].tsv.bz2, created by Complete
                            Genomcis Analysis Tools (GSA Tools 1.5 or eariler,
                            http://www.completegenomics.com/sequence-
                            data/cgatools/, http://media.completegenomics.com/docu
                            ments/DataFileFormats+Standard+Pipeline+2.0.pdf). This
                            format imports chr, pos, ref, alt of only variants
                            that have been fully called and are not equals to ref.
                            (E.g. records with zygosity equal to no-call and half,
                            and varType equal to ref are discarded.)
    map                     This input format imports variants from files in MAP
                            format (with columns chr, name gen_dist, pos), or any
                            delimiter-separated format with columns chr and pos.
                            Because these input files do not contain reference and
                            alternative alleles of variants, this format queries
                            such information from the dbSNP database using chr and
                            pos. Records that does not exist in dbSNP will be
                            discarded. Records with multiple alternative alleles
                            will lead to multiple records.
    polyphen2               To be used to export variants in a format that is
                            acceptable by the polyphen2 server
                            http://genetics.bwh.harvard.edu/pph2/bgi.shtml, and to
                            import the FULL report returned by this server.
    basic                   A basic variant input format with four columns: chr,
                            pos, ref, alt.
    vcf                     Import vcf
    

Comments can be suppressed using option `-v0`, 

    % vtools show formats -v0
    
    CASAVA18_snps
    plink
    ANNOVAR
    pileup_indel
    ANNOVAR_exonic_variant_function
    ANNOVAR_variant_function
    CGA
    map
    polyphen2
    basic
    vcf
    CASAVA18_indels
    csv
    tped
    

</details>

You can use command `vtools show format FMT` to list the details of a format. Note that 

*   `Columns` are used to direct output. If no column is specified, the format cannot be used for command `vtools export`. 
*   A input file format can have type `variant`, `position`, and `range`. Command `vtools import` can only import data from variant-based files (because it imports variants). In comparison, command `vtools update` can update existing variant using all three types of input files. 
*   Format options can be used to customized how to import/export data using the format. 

<details><summary> Examples: Show details of a format</summary> If you would like to know the details of one specific format, you can use command `vtools show format FORMAT`, 



    % vtools show format map    

    Format:                 map
    Description:            This input format imports variants from files in MAP
      format (with columns chr, name gen_dist, pos), or any delimiter-separated
      format with columns chr and pos. Because these input files do not contain
      reference and alternative alleles of variants, this format queries such
      information from the dbSNP database using chr and pos. Records that does not
      exist in dbSNP will be discarded. Records with multiple alternative alleles
      will lead to multiple records.
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr                   Chromosome
      pos                   1-based position
      ref                   Reference allele, '-' for insertion.
      alt                   Alternative allele obtained from another database
    
    Format parameters:
      db_file                (default: dbSNP.DB)
      pos_idx               Index of column for pyhysical location in the map
                            file, should be 4 for a standard map file with chr,
                            pos, gen_dist, pos. (default: 4)
      ref_field             Name of ref field from the annotation database, used
                            to retrieve reference allele at specified location.
                            (default: refNCBI)
      alt_field             Name of alt field from the annotation database, used
                            to retrieve alternative allele at specified location.
                            (default: alt)
      chr_field             Name of chr field from the annotation database, used
                            to locate variants from the dbSNP database. (default:
                            chr)
      pos_field             Name of pos field from the annotation database, used
                            to locate variants from the dbSNP database. (default:
                            start)
      separator             Separator of the input file, default to space or tab.
                            (default: None)
    

</details>



#### 2.10 Show association tests (`tests` and `test`)

Command `vtools show tests` shows a list of association tests that can be used in command `vtools associate`. Similar to other commands, option `-v0` and `--limit` can be used to suppress description of tests and limit the number of tests to display. 

<details><summary> Examples: Show a list of supported association tests</summary> List all available association tests. 



    % vtools show tests   

    BurdenBt                Burden test for disease traits, Morris & Zeggini 2009
    BurdenQt                Burden test for quantitative traits, Morris & Zeggini
                            2009
    CFisher                 Fisher's exact test on collapsed variant loci, Li &
                            Leal 2008
    Calpha                  c-alpha test for unusual distribution of variants
                            between cases and controls, Neale et al 2011
    CollapseBt              Collapsing method for disease traits, Li & Leal 2008
    CollapseQt              Collapsing method for quantitative traits, Li & Leal
                            2008
    GroupStat               Calculates basic statistics for each testing group
    GroupWrite              Write data to disk for each testing group
    KBAC                    Kernel Based Adaptive Clustering method, Liu & Leal
                            2010
    LinRegBurden            A versatile framework of association tests for
                            quantitative traits
    LogitRegBurden          A versatile framework of association tests for disease
                            traits
    RBT                     Replication Based Test for protective and deleterious
                            variants, Ionita-Laza et al 2011
    RTest                   A general framework for association analysis using R
                            programs
    RareCover               A "covering" method for detecting rare variants
                            association, Bhatia et al 2010.
    SKAT                    SKAT (Wu et al 2011) and SKAT-O (Lee et al 2012)
    SSeq_common             Score statistic / SCORE-Seq software (Tang & Lin
                            2011), for common variants analysis
    SSeq_rare               Score statistic / SCORE-Seq software (Tang & Lin
                            2011), for rare variants analysis
    VTtest                  VT statistic for disease traits, Price et al 2010
    VariableThresholdsBt    Variable thresholds method for disease traits, in the
                            spirit of Price et al 2010
    VariableThresholdsQt    Variable thresholds method for quantitative traits, in
                            the spirit of Price et al 2010
    WSSRankTest             Weighted sum method using rank test statistic, Madsen
                            & Browning 2009
    WeightedBurdenBt        Weighted genotype burden tests for disease traits,
                            using one or many arbitrary external weights as well
                            as one of 4 internal weighting themes
    WeightedBurdenQt        Weighted genotype burden tests for quantitative
                            traits, using one or many arbitrary external weights
                            as well as one of 4 internal weighting themes
    aSum                    Adaptive Sum score test for protective and deleterious
                            variants, Han & Pan 2010
    

Display only the first 5 tests without description: 

    % vtools show tests -v0 -l 5
    
    BurdenBt
    BurdenQt
    CFisher
    Calpha
    CollapseBt
    (19 records omitted)
    

</details>

If you are interested in more details of a particular test, you can use command `vtools show test TEST`. This should give you a detailed description of the test, and all the options the test accept. 

<details><summary> Examples: Show details of an association test</summary> 

    % vtools show test LogitRegBurden
    
    Name:          LogitRegBurden
    Description:   A versatile framework of association tests for disease traits
    usage: vtools associate --method LogitRegBurden [-h] [--name NAME]
                                                    [-q1 MAFUPPER] [-q2 MAFLOWER]
                                                    [--alternative TAILED]
                                                    [--use_indicator] [-p N]
                                                    [--permute_by XY]
                                                    [--adaptive C]
                                                    [--variable_thresholds]
                                                    [--extern_weight [EXTERN_WEIGHT [EXTERN_WEIGHT ...]]]
                                                    [--weight {Browning_all,Browning,KBAC,RBT}]
                                                    [--NA_adjust]
                                                    [--moi {additive,dominant,recessive}]
    
    Logistic regression test. p-value is based on the significance level of the
    regression coefficient for genotypes. If --group_by option is specified, it
    will collapse the variants within a group into a generic genotype score
    
    optional arguments:
      -h, --help            show this help message and exit
      --name NAME           Name of the test that will be appended to names of
                            output fields, usually used to differentiate output of
                            different tests, or the same test with different
                            parameters.
      -q1 MAFUPPER, --mafupper MAFUPPER
                            Minor allele frequency upper limit. All variants
                            having sample MAF<=m1 will be included in analysis.
                            Default set to 1.0
      -q2 MAFLOWER, --maflower MAFLOWER
                            Minor allele frequency lower limit. All variants
                            having sample MAF>m2 will be included in analysis.
                            Default set to 0.0
      --alternative TAILED  Alternative hypothesis is one-sided ("1") or two-sided
                            ("2"). Default set to 1
      --use_indicator       This option, if evoked, will apply binary coding to
                            genotype groups (coding will be "1" if ANY locus in
                            the group has the alternative allele, "0" otherwise)
      -p N, --permutations N
                            Number of permutations
      --permute_by XY       Permute phenotypes ("Y") or genotypes ("X"). Default
                            is "Y"
      --adaptive C          Adaptive permutation using Edwin Wilson 95 percent
                            confidence interval for binomial distribution. The
                            program will compute a p-value every 1000 permutations
                            and compare the lower bound of the 95 percent CI of
                            p-value against "C", and quit permutations with the
                            p-value if it is larger than "C". It is recommended to
                            specify a "C" that is slightly larger than the
                            significance level for the study. To disable the
                            adaptive procedure, set C=1. Default is C=0.1
      --variable_thresholds
                            This option, if evoked, will apply variable thresholds
                            method to the permutation routine in burden test on
                            aggregated variant loci
      --extern_weight [EXTERN_WEIGHT [EXTERN_WEIGHT ...]]
                            External weights that will be directly applied to
                            genotype coding. Names of these weights should be in
                            one of '--var_info' or '--geno_info'. If multiple
                            weights are specified, they will be applied to
                            genotypes sequentially. Note that all weights will be
                            masked if --use_indicator is evoked.
      --weight {Browning_all,Browning,KBAC,RBT}
                            Internal weighting themes inspired by various
                            association methods. Valid choices are:
                            'Browning_all', 'Browning', 'KBAC' and 'RBT'. Except
                            for 'Browning_all' weighting, tests using all other
                            weighting themes has to calculate p-value via
                            permutation. For details of the weighting themes,
                            please refer to the online documentation.
      --NA_adjust           This option, if evoked, will replace missing genotype
                            values with a score relative to sample allele
                            frequencies. The association test will be adjusted to
                            incorporate the information. This is an effective
                            approach to control for type I error due to
                            differential degrees of missing genotypes among
                            samples.
      --moi {additive,dominant,recessive}
                            Mode of inheritance. Will code genotypes as 0/1/2/NA
                            for additive mode, 0/1/NA for dominant or recessive
                            mode. Default set to additive

</details>



#### 2.11 Show currently available snapshots (`snapshots` and `snapshot`)

You can save snapshots of the current project and revert to them later. This allows you to recover a project when it is damaged by wrong operations or system failure, and more importantly, allows you to explore different processing pipelines with a saved baseline stage. The command `vtools show snapshots` lists information about all snapshots. Names starting with `vt_` are online snapshots that will be downloaded automatically using command `vtools admin --load_snapshot NAME`. These snapshots contain sample projects and data and are ideal for learning *variant tools*. 

Note that: 

*   Project-specific snapshots are stored under the project cache directory and are listed by command `vtools show snapshots`. 
*   Snapshots saved locally (use a filename with `vtools admin --save_snapshot`) can be saved in any directory and will not be listed by command `vtools show snapshots`. Command `vtools show snapshot FILENAME` can be used to show details of such snapshots. 

<details><summary> Examples: Show a list of local and online snapshots</summary> 

    % vtools show snapshots
    
    vt_qc                   snapshot for QC tutorial, exome data of 1000 genomes
                            project with simulated GD and GQ scores (online
                            snapshot)
    vt_ExomeAssociation     Data with ~26k variants from chr1 and 2, ~3k samples,
                            3 phenotypes, ready for association testing. (online
                            snapshot)
    vt_quickStartGuide      A simple project with variants from the CEU and JPT
                            pilot data of the 1000 genome project (online
                            snapshot)
    vt_illuminaTestData     Test data with 1M paired reads (online snapshot)
    vt_simple               A simple project with variants imported from three vcf
                            files (online snapshot)
    vt_testData             An empty project with some test datasets (online
                            snapshot)

If we create a snapshot, 

    % vtools admin --save_snapshot test1 'a test snapshot'
    
    INFO: Copying genotypes
    INFO: Snapshot test1 has been saved
    

It will be displayed in the list 



    % vtools show snapshots
    
    test1                   a test snapshot  (created: Jul12 16:37:00)
    vt_ExomeAssociation     Data with ~26k variants from chr1 and 2, ~3k samples,
                            3 phenotypes, ready for association testing.
                            (created: Jul12 03:35:50)
    vt_qc                   snapshot for QC tutorial, exome data of 1000 genomes
                            project with simulated GD and GQ scores (online
                            snapshot)
    vt_ExomeAssociation     Data with ~26k variants from chr1 and 2, ~3k samples,
                            3 phenotypes, ready for association testing. (online
                            snapshot)
    vt_quickStartGuide      A simple project with variants from the CEU and JPT
                            pilot data of the 1000 genome project (online
                            snapshot)
    vt_illuminaTestData     Test data with 1M paired reads (online snapshot)
    vt_simple               A simple project with variants imported from three vcf
                            files (online snapshot)
    vt_testData             An empty project with some test datasets (online
                            snapshot)
    

Such local snapshots are stored in the project cache directory and are listed automatically. However, if you create a local snapshot by specifying a filename (with suffix `.tar` or `.tar.gz`), such snapshots will not be displayed. 



    % vtools admin --save_snapshot local_snapshot.tar 'a local snapshot'
    
    INFO: Copying genotypes
    INFO: Snapshot local_snapshot.tar has been saved
    



    % vtools show snapshots -l 2 -v0
    
    test1
    vt_ExomeAssociation
    

You can show the details of such snapshots using command `vtools show snapshot NAME` though. 

    % vtools show snapshot local_snapshot.tar
    
    Name:                   local_snapshot.tar
    Source:                 local
    Creation date:          Jul12 16:39:24
    Description:            a local snapshot
    

</details>



#### 2.12 Show a list of runtime options (`runtime_options` and `runtime_option`)

*variant tools* provides a number of runtime options that can be used to fine-tune the behavior of commands. You can use command `vtools show runtime_options` to get the name and description of these options. If you simply need to see a list of options, you can pass option `-v0` to suppress descriptions. Please see command `vtools admin --set_runtime_option` for details. 

<details><summary> Examples: Show a list of runtime options</summary> 

    % vtools show runtime_options | head -50
    
    associate_num_of_readers None (default)
                            Use specified number of processes to read genotype
                            data for association tests. The default value is the
                            minimum of value of option --jobs and 8. Note that a
                            large number of reading processes might lead to
                            degraded performance or errors due to disk access
                            limits.
    association_timeout     None (default)
                            Cancel associate test and return special values when a
                            test lasts more than specified time (in seconds). The
                            default value of this option is None, which stands for
                            no time limit.
    import_num_of_readers   2 (default)
                            variant tools by default uses two processes to read
                            from input files during multi-process importing
                            (--jobs > 0). You can want to set it to zero if a
                            single process provides better performance or reduces
                            disk traffic.
    local_resource          ~/.variant_tools (default)
                            A directory to store variant tools related resources
                            such as reference genomes and annotation database.
                            Files under this directory is usually downloaded
                            automatically upon use, but can also be synchronized
                            directly from
                            http://vtools.houstonbioinformatics.org/.
    logfile_verbosity       2 (default)
                            Verbosity level of the log file, can be 0 for warning
                            and error only, 1 for general information, or 2 for
                            general and debug information.
    search_path             .;http://vtools.houstonbioinformatics.org/ (default)
                            A ;-separated list of directories and URLs that are
                            used to locate annotation database (.ann, .DB), file
                            format (.fmt) and other files. Reset this option
                            allows alternative local or online storage of such
                            files. variant tools will append trailing directories
                            such as annoDB for certain types of data so only root
                            directories should be listed in this search path.
    sqlite_pragma            (default)
                            pragmas for sqlite database that can be used to
                            optimize the performance of database operations.
    temp_dir                None (default)
                            Use the specified temporary directory to store
                            temporary files to improve performance (use separate
                            disks for project and temp files), or avoid problems
                            due to insufficient disk space.
    treat_missing_as_wildtype False (default)
                            Treat missing values as wildtype alleles for
                            association tests. This option is used when samples
                            are called individuals or in batch so genotypes for
                            some samples are ignored and treated as missing if
    

to see a list of runtime options, use command 

    % vtools show runtime_options -v0
    
    associate_num_of_readers
    association_timeout
    import_num_of_readers
    local_resource
    logfile_verbosity
    search_path
    sqlite_pragma
    temp_dir
    treat_missing_as_wildtype
    verbosity
    

Furthermore, if you only need to check the exiting value of a runtime option, you can use command `vtools show runtime_option OPT`, 

    % vtools show runtime_option local_resource
    
    ~/.variant_tools
    

</details>