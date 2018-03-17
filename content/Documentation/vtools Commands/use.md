
+++
title = "use"
description = ""
weight = 7
+++


# Use an annotation database 


## Usage

    % vtools use -h
    

    usage: vtools use [-h] [--as NAME] [-l [LINKED_BY [LINKED_BY ...]]]
                      [--anno_type {variant,position,range,field}]
                      [--linked_fields [LINKED_FIELDS [LINKED_FIELDS ...]]]
                      [-f [FILES [FILES ...]]] [--rebuild] [-j N] [-v {0,1,2}]
                      source
    
    Link an annotation database to the project, download it from the variant tools
    website or build it from source if needed.
    
    positional arguments:
      source                Use an annotation database ($source.DB or
                            $source.DB.gz) if it is available, download or build
                            the database if a description file ($source.ann) is
                            available. Otherwise, this command will download a
                            description file and the corresponding database from
                            web (c.f. runtime variable $search_path) and the
                            latest version of the datavase). If all means fail,
                            this command will try to download the source of the
                            annotation database (or use source files provided by
                            option --files).
    
    optional arguments:
      -h, --help            show this help message and exit
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).
    
    Basic link options:
      --as NAME             An alternative name for the linked database. This
                            option allows the use of shorter field names (e.g.
                            tg.chr instead of thousandGenomes.chr) and the use of
                            multiple versions of the same database.
      -l [LINKED_BY [LINKED_BY ...]], --linked_by [LINKED_BY [LINKED_BY ...]]
                            A list of fields that are used to link the annotation
                            database to tables in the existing project. This
                            parameter is required only for 'field' type of
                            annotation databases that link to fields of existing
                            tables.
    
    Advanced link options:
      --anno_type {variant,position,range,field}
                            This option overrides type of an existing annotation
                            database when it is attached to a project. It
                            corresponds to key anno_type of the data sources
                            section of an annotation file (with suffix .ann) but
                            does not affect the .ann file or the database built
                            from it.
      --linked_fields [LINKED_FIELDS [LINKED_FIELDS ...]]
                            An alternative set of fields that are used to link the
                            annotation database to the master variant table. It
                            should have four, two, and three values for database
                            of type variant, position, and range. Similar to
                            anno_type, this option does not affect the .ann file
                            or the database built from it.
    
    Build database from source:
      -f [FILES [FILES ...]], --files [FILES [FILES ...]]
                            A list of source files. If specified, vtools will not
                            try to download and select source files. These source
                            files will be compiled into a local annotation
                            database. This is used only when no local annotation
                            database is specified.
      --rebuild             If set, variant tools will always rebuild the
                            annotation database from source, ignoring existing
                            local and online database. In addition to $name.DB,
                            variant tools will also create $name-$version.DB.gz
                            that can be readily distributed.
      -j N, --jobs N        If need to build database from source, maximum number
                            of processes to use.
    



## Details

Command `vtools use` attaches an annotation database to the project, effectively making one or more attributes available to variants in the project. Four types of annotation databases can be used with variant tools: 



*   A **variant** annotation database is linked directly to the project by linking chromosome, position, reference and alternative allele to fields **`chr`**, **`pos`**, **`ref`**, and **`alt`** of the project. It provides variant-level annotation. 
*   A **position** annotation database is linked to the project using fields **`chr`** and **`pos`**. It provides annotation information for nucleotide locations. If there are more than one variants at a locus, the annotation information are used for all of them. 
*   A **range** annotation database is linked to the project by comparing fields **`chr`** and **`pos`** to chromosome, starting and ending positions of each range. It provides annotation information for all variants in chromosomal regions. 
*   A **field** annotation database can be linked to any **existing variant info or annotation fields** and provide annotation information for these fields. For example, a gene annotation table might provide description for some genes, which can be linked to the project through field `refGene.name2` that is provided by database `refGene`. Because attribute annotation databases are anchored to a project through existing attributes, **one or more fields must be specified to link the database to the project using parameter `--linked_by`.** 



### Basic usages of system-provided annotation databases

It is easy to use system-provided annotation databases. Generally speaking, you should 



*   Use command `vtools show annotations` to see a list of annotation databases, and identify annotation databases that match the reference genome of your project. 
*   Use command `vtools show annotation ANNODB` to check the details of an annotation database. 
*   Use command `vtools use ANNODB` to download (if needed) and link the database to your project. *variant tools* will automatically link the project to the database using appropriate fields. 



*   Position-aware annotation databases (variant, position, and range) are ref-genome dependent. Most such annotation databases are built for a particular build of reference genome, but some of them support multiple reference genomes. 
*   Newer databases usually contain more updated annotation information and usually use more recent build of reference genome. If you are using *hg18* and would like to use annotation databases that use build *hg19* of the reference genome, you can liftover your project to add *hg19* as an alternative reference genome. 

(:toggleexample Examples: Use system-provided annotation databases:) Let us get a project 



    % vtools init use --parent vt_simple
    

This project uses build `hg19` of the reference genome, as shown in the output of command `vtools show` 



    % vtools show
    

    Upgrading to 1.0.7: 100% [==============================] 3 202.2/s in 00:00:00
    Project name:                test
    Primary reference genome:    hg19
    Secondary reference genome:  None
    Runtime options:             verbosity=1
    Variant tables:              variant
    Annotation databases:
    

We then use command `vtools show annotations` to check all available databases, using option `-v0` to suppress descriptions of databases: 



    % vtools show annotations -v0 
    

    CancerGeneCensus-20111215
    CancerGeneCensus-20120315
    CancerGeneCensus
    CosmicCodingMuts-v61_260912
    CosmicCodingMuts
    CosmicMutantExport-v61_260912
    CosmicMutantExport
    CosmicNonCodingVariants-v61_260912
    CosmicNonCodingVariants
    ccdsGene-hg19_20110909
    ccdsGene-hg19_20111206
    ccdsGene
    ccdsGene_exon-hg19_20110909
    ccdsGene_exon-hg19_20111206
    ccdsGene_exon
    ccdsGene_exon_hg19-20111206
    ccdsGene_hg19-20111206
    cytoBand-hg18_20111216
    cytoBand-hg19_20111216
    cytoBand
    dbNSFP-hg18_hg19_1.1_2
    dbNSFP-hg18_hg19_1_3
    dbNSFP-hg18_hg19_2_0b4
    dbNSFP
    dbNSFP_light-hg18_hg19_1.0_0
    dbNSFP_light-hg18_hg19_1_3
    dbNSFP_light
    dbSNP-hg18_129
    dbSNP-hg18_130
    dbSNP-hg19_131
    dbSNP-hg19_132
    dbSNP-hg19_135-1
    dbSNP-hg19_135
    dbSNP-hg19_137
    dbSNP
    evs-6500
    evs-hg19_20111107
    evs
    evs_5400
    genomicSuperDups-hg19_20130626
    genomicSuperDups
    gwasCatalog-hg19_20111220
    gwasCatalog
    keggPathway-20110823
    keggPathway
    knownGene-hg18_20110909
    knownGene-hg18_20121219
    knownGene-hg19_20110909
    knownGene-hg19_20121219
    knownGene
    knownGene_exon-hg18_20110909
    knownGene_exon-hg19_20110909
    knownGene_exon
    phastCons-hg19_20110909
    phastCons-hg19_20130322
    phastCons
    phastConsElements-hg19_20130622
    phastConsElements
    refGene-hg18_20110909
    refGene-hg19_20110909
    refGene
    refGene_exon-hg18_20110909
    refGene_exon-hg19_20110909
    refGene_exon
    thousandGenomes-hg19_20110909
    thousandGenomes-hg19_201202
    thousandGenomes
    thousandGenomesEBI-hg19_phase1_release_v3_20101123
    thousandGenomesEBI
    

Some databases uses `hg18`, but most uses `hg19`. The default databases (the ones without version number) generally refer to the latest databases that uses `hg19`, so you can use most databases as simple as 



    % vtools use refGene
    

    INFO: Downloading annotation database from annoDB/refGene.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/refGene-hg19_20110909.DB.gz
    INFO: Using annotation DB refGene in project test.
    INFO: refseq Genes
    



    % vtools use refGene_exon
    

    INFO: Downloading annotation database from annoDB/refGene_exon.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/refGene_exon-hg19_20110909.DB.gz
    INFO: Using annotation DB refGene_exon in project test.
    INFO: Exon locations of refseq Genes
    



    % vtools use dbNSFP
    

    INFO: Downloading annotation database from annoDB/dbNSFP.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/dbNSFP-hg18_hg19_2_0b4.DB.gz
    INFO: Using annotation DB dbNSFP in project test.
    INFO: dbNSFP version 2.0b4, maintained by Xiaoming Liu from UTSPH. Please cite "Liu X, Jian X, and Boerwinkle E. 2011. dbNSFP: a lightweight database of human non-synonymous SNPs and their functional predictions. Human Mutation. 32:894-899" if you find this database useful.
    



    % vtools use thousandGenomes
    

    INFO: Downloading annotation database from annoDB/thousandGenomes.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/thousandGenomes-hg19_201202.DB.gz
    INFO: Using annotation DB thousandGenomes in project test.
    INFO: 1000 Genomes VCF file (available from: ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/v4.0/00-All.vcf.gz).
    

The CancerGeneCensus database is a bit difficult to use because it is a field database that annotate gene names so you need to link it to `refGene.name2`, 



    % vtools use CancerGeneCensus --linked_by refGene.name2
    

    INFO: Downloading annotation database from annoDB/CancerGeneCensus.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/CancerGeneCensus-20130711.DB.gz
    INFO: Using annotation DB CancerGeneCensus in project test.
    INFO: This database contains variants from the Cancer Genome Project. It is
    an ongoing effort to catalogue those genes for which mutations have been causally
    implicated in cancer. The original census and analysis was published in Nature
    Reviews Cancer and supplemental analysis information related to the paper is also
    available. Currently, more than 1% of all human genes are implicated via mutation
    in cancer. Of these, approximately 90% have somatic mutations in cancer, 20% bear
    germline mutations that predispose to cancer and 10% show both somatic and
    germline mutations.
    INFO: 475 out of 23242 refgene.name2 are annotated through annotation database CancerGeneCensus
    WARNING: 9 out of 484 values in annotation database CancerGeneCensus are not linked to the project.
    

After you use these databases, you could get the details of them using command `vtools show annotation ANNODB`, 

    % vtools show annotation refGene
    

    WARNING: Resouce file annoDB/CancerGeneCensus.ann has been updated. Please update it using command "vtools admin --update_resource existing".
    Annotation database refGene (version hg19_20110909)
    Description:            refseq Genes
    Database type:          range
    Reference genome hg19:  chr, txStart, txEnd
      name                  Gene name
      chr
      strand                which DNA strand contains the observed alleles
      txStart               Transcription start position
      txEnd                 Transcription end position
      cdsStart              Coding region start
      cdsEnd                Coding region end
      exonCount             Number of exons
      score                 Score
      name2                 Alternative name
      cdsStartStat          cds start stat, can be 'non', 'unk', 'incompl', and
                            'cmp1'
      cdsEndStat            cds end stat, can be 'non', 'unk', 'incompl', and
                            'cmp1'
    



*   More detailed information such as statistics for each field are available if you specify option `-v2` to the `vtools show annotation` command 
*   If you need to see a list of available fields, use command `vtools show fields`. 

(:exampleend:) 



About multiple versions of the same database: 

*   The default database without version name always refers to the latest version. For example, `dbSNP` could be `dbSNP-hg19_135`, and then `dbSNP-hg19_138` after version 138 becomes available. 
*   You can use a specific version of a database by specifying its full name. The database will appear without version name in your project (e.g. as `dbSNP`). 
*   You can use the `--as` option to give databases different names if you would like to use different versions of the same database in the project. 



### Advanced usages of annotation databases

Each database provide a number of fields and one or more default methods to link them to a project database. For example, if you look at the output of `vtools show annotation refGene`, you can see that this is a range-based database that is linked to a project using fields `chr`, `txStart`, and `txEnd`, which are chromosome name and start and ending of transcription region. The database, however, has other fields such as `cdsStart` and `cdsEnd` so you can link the database to a project using these two fields to identify variants in the coding regions of ref seq genes. You can even use regions such as `txStart-5000, txEnd+5000` to extend each region by 5k to include variants that are in vicinity of ref seq genes. 

(:toggleexample Examples: alternative ways to link range-based annotation databases:) There are 730 variants in the regular ref seq gene regions, 

    % vtools select variant 'refGene.chr is not NULL' -c
    

    Counting variants: 13 456.6/s in 00:00:00
    730
    

We can link to the refGene database using coding regions 



    % vtools use refGene --linked_fields chr cdsStart cdsEnd
    

    INFO: Downloading annotation database from annoDB/refGene.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/refGene-hg19_20110909.DB.gz
    Binning ranges: 100% [===============================================] 40,843 24.3K/s in 00:00:01
    INFO: Using annotation DB refGene in project test.
    INFO: refseq Genes
    

only 225 variants are selected, that means most variants are not in the coding regions, 

    % vtools select variant 'refGene.chr is not NULL' -c
    

    Counting variants: 13 965.9/s in 00:00:00
    225
    

You can also link the database by an expanded region of each transcription region (adding 5k before and after the region), 



    % vtools use refGene --linked_fields chr 'txStart-5000' 'txEnd+5000'
    

    INFO: Downloading annotation database from annoDB/refGene.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/refGene-hg19_20110909.DB.gz
    Binning ranges: 100% [================================================] 40,843 62.2K/s in 00:00:00
    INFO: Using annotation DB refGene in project test.
    INFO: refseq Genes
    

This time more variants are selected by the refGene database, 

    % vtools select variant 'refGene.chr is not NULL' -c
    

    Counting variants: 14 847.2/s in 00:00:00
    1170
    

(:exampleend:) 

In addition to the fields used to link to the project, you can even change the type of annotation database by specifying the appropriate values to options `--anno_type` and `--linked_fieleds`. For example, the gawsCatalog database records is a position-based annotation database that records GWAS hits. Because of the uncertainty of the exact locations of these findings, you can link it to the project as a range-based database that find variants that are close to these GWAS hits. 

(:toggleexample Examples: Link a position based database as a range-based database:) We would like to see if any of our variants has been identified by one of the Genome-wide association studies. `gwasCatalog` is a position-based database that records all identified variants by their positions. 



    % vtools use gwasCatalog
    

    INFO: Downloading annotation database from annoDB/gwasCatalog.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/gwasCatalog-hg19_20111220.DB.gz
    INFO: Using annotation DB gwasCatalog in project test.
    INFO: GWAS Catalog
    

No matching variant is found in our project 

    % vtools select variant 'gwasCatalog.chr is not null' -c
    

    Counting variants: 3 1.2K/s in 00:00:00
    0
    

However, we can link the database as a range-based database to check if there is any variant that falls in the vicinity of any GWA hits. 

    % vtools use gwasCatalog --anno_type range --linked_fields chr 'position - 10000' 'position + 10000'
    

    INFO: Downloading annotation database from annoDB/gwasCatalog.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/gwasCatalog-hg19_20111220.DB.gz
    Binning ranges: 100% [================================] 8,608 67.1K/s in 00:00:00
    INFO: Using annotation DB gwasCatalog in project test.
    INFO: GWAS Catalog
    

This time, 24 variants are identified as within 10k distance of one of the GWA hits. 

(:exampleend:) 

Because field-based databases can link to arbitrary fields, you do not have to use the default linking fields. For example, the `CancerGeneCensus` database by default links to the `refGene.name2` field by 'gene name'. It can also be linked to a knownGene ID because the CancerGeneCensus database has this field. 

(:toggleexample Examples: Linking a field database using an alternative field:) The `CancerGeneCensus` database by default links to the `refGene.name2` field by 'gene name'. 



    % vtools use CancerGeneCensus --linked_by refGene.name2
    

    INFO: Downloading annotation database from annoDB/CancerGeneCensus.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/CancerGeneCensus-20130711.DB.gz
    INFO: Using annotation DB CancerGeneCensus in project test.
    INFO: This database contains variants from the Cancer Genome Project. It is
    an ongoing effort to catalogue those genes for which mutations have been causally
    implicated in cancer. The original census and analysis was published in Nature
    Reviews Cancer and supplemental analysis information related to the paper is also
    available. Currently, more than 1% of all human genes are implicated via mutation
    in cancer. Of these, approximately 90% have somatic mutations in cancer, 20% bear
    germline mutations that predispose to cancer and 10% show both somatic and
    germline mutations.
    INFO: 471 out of 23242 refgene.name2 are annotated through annotation database CancerGeneCensus
    WARNING: 16 out of 487 values in annotation database CancerGeneCensus are not linked to the project.
    

From the output of `vtools show annotation CancerGeneCensus`, you can see that this database also provides `kgID` for each record. This allows you to link the database to the project using `kgID`, 



    % vtools use knownGene
    

    INFO: Downloading annotation database from annoDB/knownGene.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/knownGene-hg19_20121219.DB.gz
    INFO: Using annotation DB knownGene in project test.
    INFO: UCSC Known Genes
    

    % vtools use CancerGeneCensus --linked_fields kgID --linked_by knownGene.name
    

    INFO: Downloading annotation database from annoDB/CancerGeneCensus.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/CancerGeneCensus-20130711.DB.gz
    INFO: Using annotation DB CancerGeneCensus in project test.
    INFO: This database contains variants from the Cancer Genome Project. It is
    an ongoing effort to catalogue those genes for which mutations have been causally
    implicated in cancer. The original census and analysis was published in Nature
    Reviews Cancer and supplemental analysis information related to the paper is also
    available. Currently, more than 1% of all human genes are implicated via mutation
    in cancer. Of these, approximately 90% have somatic mutations in cancer, 20% bear
    germline mutations that predispose to cancer and 10% show both somatic and
    germline mutations.
    INFO: 433 out of 80922 knowngene.name are annotated through annotation database CancerGeneCensus
    WARNING: 54 out of 487 values in annotation database CancerGeneCensus are not linked to the project.
    

Note that you can link `GeneSymbol` (the default link-out field in the database) to `knowGene.name` because none of the names will match 



    % vtools use CancerGeneCensus --linked_by knownGene.name
    

    INFO: Downloading annotation database from annoDB/CancerGeneCensus.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/CancerGeneCensus-20130711.DB.gz
    INFO: Using annotation DB CancerGeneCensus in project test.
    INFO: 0 out of 80922 knowngene.name are annotated through annotation database CancerGeneCensus
    WARNING: 487 out of 487 values in annotation database CancerGeneCensus are not linked to the project.
    

(:exampleend:) 

There is also nothing prevents you from using other annotation database as a field-based database. For example, the `gwasCatalog` database has a field `region` that records the cytoband of each GWAS signal belongs. If you link this field to database `cytoBand`, you can provide a list of GWAS hits within each cytoband. 

(:toggleexample Examples: Use a position-based database as a field database to annotate cytoBand:) The gwasCatalog database has a field `region` that records the cytoband of each GWAS hit. If we first use `cytoBand`, 

    % vtools use cytoBand
    

    INFO: Downloading annotation database from annoDB/cytoBand.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/cytoBand-hg19_20111216.DB.gz
    INFO: Using annotation DB cytoBand in project test.
    INFO: Cyto Band
    

and link the `gwasCatalog` database (originally a position-based database) to it through field `region`, 



    % vtools use gwasCatalog --anno_type field --linked_fields region --linked_by cytoBand.name
    

    INFO: Downloading annotation database from annoDB/gwasCatalog.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/gwasCatalog-hg19_20111220.DB.gz
    INFO: Using annotation DB gwasCatalog in project test.
    INFO: GWAS Catalog
    INFO: 745 out of 862 cytoband.name are annotated through annotation database gwasCatalog
    WARNING: 1 out of 746 values in annotation database gwasCatalog are not linked to the project.
    

For each variant, we have cytoband information as `cytoBand.name` (as well as `gwasCatalog.region`), and all GWAS hits for that belong to that region, 



    % vtools output variant chr pos cytoBand.name gwasCatalog.genes gwasCatalog.trait --all -l 10
    

    1	4540	1p36.33	PRKCZ	Reasoning
    1	5683	1p36.33	PRKCZ	Reasoning
    1	5966	1p36.33	PRKCZ	Reasoning
    1	6241	1p36.33	PRKCZ	Reasoning
    1	9992	1p36.33	PRKCZ	Reasoning
    1	9993	1p36.33	PRKCZ	Reasoning
    1	10007	1p36.33	PRKCZ	Reasoning
    1	10098	1p36.33	PRKCZ	Reasoning
    1	14775	1p36.33	PRKCZ	Reasoning
    1	16862	1p36.33	PRKCZ	Reasoning
    

Although in this case we should use option `--all` to list all GAWS hits 

    % vtools output variant chr pos cytoBand.name gwasCatalog.genes gwasCatalog.trait --all -l 10
    

    1	4540	1p36.33	NR	Body mass index
    1	4540	1p36.33	PRKCZ	Height
    1	4540	1p36.33	PRKCZ	Reasoning
    1	5683	1p36.33	NR	Body mass index
    1	5683	1p36.33	PRKCZ	Height
    1	5683	1p36.33	PRKCZ	Reasoning
    1	5966	1p36.33	NR	Body mass index
    1	5966	1p36.33	PRKCZ	Height
    1	5966	1p36.33	PRKCZ	Reasoning
    1	6241	1p36.33	NR	Body mass index
    

Obviously, all variants belonging to the same cytoband will have the same gwas hits as annotations. (:exampleend:) 



### Create your own annotation databases

You may create your own annotation databases to annotate, prioritize, and filter variants in your project. For example if you have a huge amount of data and you do not want to import all of them into a project (to reduce size and improve performance of the main project database), you can create annotation databases from input data. 

The general process to create an annotation database is 

1.  Write a `.ann` file that describe your annotation source (<http://varianttools.sourceforge.net/Annotation/New>). You can usually start from one of the system `.ann` files under `~/.varianttools/annoDB`. 
2.  Use command `vtools use NAME.ann` to create an annotation database and use it in the project. You can specify source files using option `--files`. A option `--rebuild` will force the rebuild of database from source file and generate a versioned and compressed `.DB.gz` file. 



The [anno_utils][1][?][1] pipelines provide a few pipelines that can help you create annotation databases from various resources. For example, if you have a project with variants from unaffected individuals, you can export the variants as an annotation database. This database can be used by other projects to filter variants.

 [1]: http://localhost/~iceli/wiki/pmwiki.php?n=Pipeline.AnnoUtils?action=edit