+++
title = "Annotation"
weight = 1
+++


## Variant annotation using variant tools


### 1. Annotation Functions of Variant tools

#### 1.1 Variant, info fields, and annotation fields

Variants in a variant tools project are stored in a **master variant table** after they are [imported][1] from external data files. Multiple **variant info fields** could be added to this table to describe these variant. These fields could be [imported from a file][1] when variants are imported, or [updated][2] from files after variants are imported, calculated from samples as sample statistics, or derived from other variant info or annotation fields. Variant info fields are part of a project and are usually project-specific. 

**Annotation fields** are provided in *annotation databases* and are available to a project after they are [linked to the project][3]. Conceptually, annotation databases add columns to the master variant table so that you can [select variants][4] based on these fields, or [output][5]variants with these annotation fields. A key difference between an variant info field and an annotation field is that variant info is unique for each variant whereas there can be multiple annotation values for a single variant. Note that annotation databases vary greatly in number of fields and coverage of variants and *usually do not provide annotation for all variants*. 



#### 1.2 Variant tools commands [use][3], [output][5], and [export][6]

The annotation features of variant tools involve mostly commands `vtools use`, `vtools output`, and `vtools export`. 

*   Command `vtools use` creates, downloads, and links annotation databases to a project. It accepts the name of an annotation database and try to locate it locally (current directory, `~/.variant_tools`), online (usually `<a class='urllink' href='http://vtools.houstonbioinformatics.org/annoDB' rel='nofollow'>http://vtools.houstonbioinformatics.org/annoDB</a>`), and build an annotation database from source files if no existing database could be found. When a database is linked to a project, all its annotation fields becomes available to the project. 


{{% notice tip %}}
Command `vtools show fields` lists all variant info and annotation fields of a project. 
{{% /notice %}}


*   Command `vtools output` outputs variants in a variant table along with their info fields and annotation fields. *Conceptually speaking, the master variant table and all the variant info and annotation fields form a huge table with variants as rows and fields as columns*. This command outputs subsets of variants and fields to the standard output. (As an advanced feature, this command can also outputs summary statistics of variants and fields). 

*   Command `vtools export` export variant in specific formats. This command is similar to `vtools output` but it exports variants and related fields in [user-specified formats][7]. 

We will demonstrate the use of these commands in the [Tutorial][8]. 



### 2. Annotation databases

Variant tools supports four different types of annotation databases where each type of databases links to variants using a different method. An annotation database can support one or more reference genomes and **it must match either the primary or the alternative reference genome of a project to be linked to the project**, unless it is a field database that annotate another field such as gene name. 



#### 2.1 Variant-based databases

**Variant-based annotation databases annotate specific variants**. They contain annotation information for variants (chr, pos, ref, alt). For example, the [dbNSFP][9] database lists, among about 20 annotation fields, reference and mutated amino acid, nonsynonymous-to-synonymous-rate ratio, SIFT, PolyPhen2, MutationTaster and other scores, allele frequencies in dbSNP and the 1000 genomes project. Variant tools currently provides the following variant-based annotation databases: 



*   [Exome Variant Server (EVS)][10]: NHLBI GO Exome Sequencing Project (ESP) variants with population-specific allele frequencies and various functional annotations (currently has two versions: `evs` was created from EVS on November 7, 2011 with approximately 2500 exomes; `evs_5400` was created from EVS on December 15, 2011 with approximately 5400 exomes). 
*   [dbNSFP][9]: non-synonymous variants of CCDS genes. 
*   [dbSNP][11]: NCBI's variant database. 
*   [1000 Genomes][12]: 1000 Genomes variants deposited in dbSNP. 
*   [1000 Genomes (provided through the European Bioinformatics Institute)][13]: This represents version 3 of an integrated variant call set based on both low coverage and exome whole genome sequence data from the 1000 Genomes project. 
*   [Coding and NonCoding variants from the COSMIC (Catalogue Of Somatic Mutations In Cancer) Project][14]



#### 2.2 Position-based databases

**Position-based databases annotate chromosomal locations**. Such databases provide annotation for all variants at a locus, mostly because there is no variant-specific information available. For example, the [gwasCatalog][15] database contains chromosomal locations of susceptibility loci of all published genome wide association studies. 



*   [gwasCatalog][15]: this annotation source can be used to annotate your variants with published GWA hits. The database is probably more useful as a range-based database however (see example of how to use this database as a range-based database [here][15]). 



#### 2.3 Range-based databases

**Range-based databases annotate regions of chromosomes**. These databases are used to annotate regions of chromosomes, such as genes, exon regions of genes, and highly-conserved regions. Variant tools provides the following range-based annotation databases: 



*   [refGene][16]: specifies known human protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq). 
*   [knownGene][17]: defines gene predictions based on data from RefSeq, Genbank, CCDS and UniProt. 
*   [ccdsGene][18]: contains high-confidence gene annotations from the Consensus Coding Sequence (CCDS) project 
*   [phastCons][19]: defines phastCons scores (e.g., conservation scores) for blocks of the human genome. 
*   [cytoBand][20]: gives the approximate location of cytogenic bands as seen on Giemsa-stained chromosomes. 
*   [gwasCatalog][15]: this annotation source can be used to find published GWA hits that are "near" your variants. To use the annotation source as a range-based database, you must specify a coordinate range that describes how close your variant needs to be to the GWA hit (see [example][15]). 



#### 2.4 Field databases

**Field-based annotation databases annotate variants indirectly through other variant info or annotation fields**. For example, the [keggPathway][21] database lists all the pathways genes belong so it technically annotate gene IDs, not variants. To use this database, you will need to first link the project to a database that provides IDs of genes each variant belongs, and then link the keggPathway database to the project through gene ID. Therefore, **a --linked_by field is required to use a field-based database**. Variant tools provides the following field-based annotation databases: 



*   [keggPathway][21]: allows annotation of variants to KEGG pathways indirectly by using CCDS gene IDs. As a pre-requisite, first variants need to be annotated to CCDS gene IDs - if you use dbNSFP this is already done for you because dbNSFP annotates variants to CCDS gene IDs. 
*   [CancerGeneCensus][22]]: genes for which mutations have been causally implicated in cancer, maintained by [Cancer Genome Project][23] 
*   [gwasCatalog][15]: in addition to being used as a position- or range-based annotation source, gwasCatalog can be used as a field-based annotation source to find published GWA hits that are in the same cytoband as your project variants. To use gwasCatalog as a field-based database, you can link your variants to the [cytoBand][20] annotation source and then annotate your variant cytoBands to published GWA hits (see [example][15]). 
*   [Detailed annotation for each COSMIC (Catalogue Of Somatic Mutations In Cancer) Mutant][14] 



#### 2.5 Create your own annotation databases

If you would like to use an annotation database that is not provided by variant tools, you could write a [customized `.ann` file to][24] create your own annotation database. This file tells variant tools the type of annotation database, reference genome, URL to source files, version, and more importantly, the type of each annotation field and how to extract them from source files. A large number of [functors][25] are provided in case that you need to post-processing texts from input file to extract values of annotation fields. 



### 3. Citation for Variant Annotation Tools

Please cite 



F. Anthony San Lucas, Gao Wang, Paul Scheet, and Bo Peng (2012) [**Integrated annotation and analysis of genetic variants from next-generation sequencing studies with variant tools**][26], Bioinformatics 28 (3): 421-422. 

if you find Variant Annotation Tools helpful and use it in your publication. Thank you.

 [1]:    /documentation/vtools_commands/import/
 [2]:    /documentation/vtools_commands/update/
 [3]:    /documentation/vtools_commands/use/
 [4]:    /documentation/vtools_commands/select/
 [5]:    /documentation/vtools_commands/output/
 [6]:    /documentation/vtools_commands/export/
 [7]:    /documentation/customization/format/formats
 [8]:   /applications/annotation/tutorial/
 [9]:   /applications/annotation/variants/dbnsfp/
 [10]:   /applications/annotation/variants/esp/
 [11]:   /applications/annotation/variants/dbsnp/
 [12]:   /applications/annotation/variants/thousand/
 [13]:   /applications/annotation/variants/ebi/
 [14]:   /applications/annotation/variants/cosmic/
 [15]:   /applications/annotation/variants/gwas/
 [16]:   /applications/annotation/genes/refgene/
 [17]:   /applications/annotation/genes/knowngene/
 [18]:   /applications/annotation/genes/ccdsgene/
 [19]:   /applications/annotation/regions/phast_cons/
 [20]:   /applications/annotation/regions/cytoband/
 [21]:   /applications/annotation/misc/keggpathway/
 [22]:   /applications/annotation/genes/cancergenecensus/
 [23]: http://www.sanger.ac.uk/genetics/CGP/Census/
 [24]:   /applications/annotation/customized/
 [25]:    /documentation/customization/format/formats/functor/
 [26]: http://bioinformatics.oxfordjournals.org/content/28/3/421.abstract?sid=f64403e7-5050-4102-963c-e690efe003f7