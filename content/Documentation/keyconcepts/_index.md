+++
title = "Key concepts"
description = ""
weight = 1
+++

## Key concepts

### 1. Project

**Variant Tools** is project based. All data need to be imported to the project to be analyzed. A *variant tools* project **`$name`** consists of a project file **`$name.proj`**, a genotype database **$`name_genotype.DB`**, and a log file **`$name.log`**. After a project is created, subsequent **`vtools`** calls will automatically load the project in the current directory. Working from outside of a project directory is not allowed. 

<details> <summary> Examples </summary>

Let us create a sample project and import two datasets from the pilot phase of the 1000 genomes project: 

    % vtools init concept
    % wget http://ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/release/2010_07/exon/snps/CEU.exon.2010_03.sites.vcf.gz
    % wget http://ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/release/2010_07/exon/snps/JPT.exon.2010_03.sites.vcf.gz
    % vtools import CEU.exon.2010_03.sites.vcf.gz --build hg19 --sample_name CEU --var_info AA AC AN DP 
    % vtools import JPT.exon.2010_03.sites.vcf.gz --sample_name JPT --var_info AA AC AN DP
 

The project properties can be displayed as follows 

    % vtools show project
    
    Project name:                concept
    Created on:                  Sun May 27 21:13:47 2018
    Primary reference genome:    hg19
    Secondary reference genome:  
    Storage method:              sqlite
    Runtime options:             verbosity=1, shared_resource=/Users/iceli/.variant_tools, local_resource=/Users/iceli/.variant_tools
    Variant tables:              variant
    Annotation databases:         


</details>


{{% notice tip %}} 
*Variant Tools* can import and manage large projects with thousands of samples and millions of variants. Although it can be slow to import data from large whole genome sequencing projects (e.g. it takes around 3 days to import all genotype data from the 1000 genomes project, with raw data exceeding 1T in size), data analysis is relatively fast because imported data are properly organized (indexed) and readily accessible.
{{% /notice %}}

### 2. Variant & variant table

**Variants** refer to DNA sequence variations at a particular locus. Each variant consists of a *chromosome name* (1, 2, ..., X etc, without leading `chr`), a *position* (1-based), a *reference allele*, and an *alternative allele*, denoted by fields **`chr`**, **`pos`**, **`ref`**, and **`alt`**. variant tools currently supports [SNV, small indels, and MNP (Multiple-nucleotide polymorphism)][1]. All variants are assumed to be on the forward (`+`) strand. 

Unlike some other tools that can analyze variants in external files directly, **variants must be imported into a project before they are annotated or analyzed**. All variant tools project has a **master variant table** that consists of all variants in this project. These variants are usually [imported][2] from external files. A project can have many **variant tables** that consist of subsets of variants from the master variant table. They are usually created using command `vtools select` according to sample properties and annotation of variants. Information about variant tables can be listed by command `vtools show tables`. Names of variant tables can contain special characters such as '@'. 

<details> <summary> Examples </summary>

This project has a single **master variant table** with 4,858 variants: 

    % vtools show tables
    
    table      #variants     date message
    variant        4,858    May27 Master variant table
    

Each variant has chr, position, reference and alternative alleles, 

    % vtools output variant chr pos ref alt --limit 5
    
    1	1105366	T	C
    1	1105411	G	A
    1	1108138	C	T
    1	1110240	T	A
    1	1110294	G	A


We can select all variants with reference allele `T` and save the results to a **variant table** named `refT`, 

    % vtools select variant 'ref="T"' --to_table refT 'variants with reference allele T'
    
    Running: 3 647.4/s in 00:00:00                                                  
    INFO: 787 variants selected.
    

Now there are two variant tables `variant` and `refT` in this project 

    % vtools show tables
    
    table      #variants     date message
    refT             787    May27 variants with reference allele T
    variant        4,858    May27 Master variant table
    

As you can see, all variants in table `refT` have reference allele `T`: 

    % vtools output refT chr pos ref alt --limit 5
    
    1	1105366	T	C
    1	1110240	T	A
    1	3537996	T	C
    1	6447088	T	C
    1	6447275	T	C
    

</details>




### 3. Variant info & variant info field

**Variant info** refers to information that describes a variant, such as the INFO fields of a [vcf file][3]. It usually consists of annotation information such as membership in dbSNP, or sample statistics such as sample frequency of each variant. The names of these info are called **variant info fields** and can be displayed using command `vtools show fields`. 

<details><summary>Examples:</summary> The project has 4 variant info fields `AA`, `AC`, `AN`, and `DP`, as shown by the following command 

    % vtools show fields
    
    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an
                            insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an
                            deletion)
    variant.AA (char)
    variant.AC (int)
    variant.AN (int)
    variant.DP (int)
    refT.chr (char)         Chromosome name (VARCHAR)

    

These fields are imported from the INFO fields of the vcf file, and are the ancestral allele, total number of alternate alleles in called genotypes, total number of alleles in called genotypes, and Read Depth from MOSAIK BAM, respectively, for each variant. These fields could be outputted for each variant, 



    % vtools  output refT chr pos ref alt AA AC AN DP --limit 5
    
    1	1105366	T	C	T	4	114	3251
    1	1110240	T	A	T	1	178	7275
    1	3537996	T	C	C	156	156	1753
    1	6447088	T	C	T	12	172	4691
    1	6447275	T	C	T	9	176	6871
    

More variant info fields could be added to the project using command `vtools update`. 



    % vtools update variant --from_file CEU.exon.2010_03.sites.vcf.gz --var_info id
    
    INFO: Using primary reference genome hg19 of the project.
    Getting existing variants: 100% [============================] 4,858 261.1K/s in 00:00:00
    INFO: Updating variants from CEU.exon.2010_03.sites.vcf.gz (1/1)
    CEU.exon.2010_03.sites.vcf.gz: 100% [==========================] 3,500 5.2K/s in 00:00:00
    INFO: Field id of 3,489 variants are updated


    $ vtools output refT chr pos ref alt id AA AC AN DP -l 5
    
    1	1105366	T	C	.         	T	4  	114	3251
    1	1110240	T	A	.         	T	1  	178	7275
    1	3537996	T	C	rs2760321 	C	156	156	1753
    1	6447088	T	C	rs11800462	T	12 	172	4691
    1	6447275	T	C	rs3170675 	T	9  	176	6871
    

</details>



### 4. Annotation databases & annotation fields

**Annotation databases** are databases that provide annotation information for variants. They are not part of a project but they provide additional **annotation fields** to a project when they are [linked][4] to a project. Conceptually speaking, attaching annotation databases to a project adds info fields to variants of the project, although annotation databases usually annotate only part of the variants, leaving a lot of `NULL` values for these fields. 

<details><summary>Examples:</summary> Let us download and use an annotation database `dbSNP` version 135 for reference genome hg19

    % vtools use dbSNP-hg19_135
    
    INFO: Downloading annotation database annoDB/dbSNP-hg19_135.ann
    INFO: Downloading annotation database from annoDB/dbSNP-hg19_135.DB.gz
    dbSNP-hg19_135.DB.gz: 100% [=========================] 1,719,968,746.0 1.5M/s in 00:18:49
    INFO: Decompressing /Users/iceli/.variant_tools/annoDB/dbSNP-hg19_135.DB.gz
    Upgrading dbSNP-hg19_135: 100% [=========================] 54,182,943 28.3K/s in 00:31:52
    INFO: 2831938 variants are updated
    INFO: Using annotation DB dbSNP as dbSNP in project concept.
    INFO: dbSNP version 135

This database provides the following **annotation fields** 

    % vtools show annotation dbSNP
    
    Annotation database dbSNP (version hg19_135)
    Description:            dbSNP version 135
    Database type:          variant
    Reference genome hg19:  chr, start, refNCBI, alt
      chr (char)
      start (int)           start position in chrom (1-based)
      end (int)             end position in chrom (1-based). start=end means zero-length
                            feature
      name (char)           dbSNP reference SNP identifier
      strand (char)         which DNA strand contains the observed alleles
      refNCBI (char)        Reference genomic sequence from dbSNP
      refUCSC (char)        Reference genomic sequence from UCSC lookup of
                            chrom,chromStart,chromEnd
      observed (char)       Strand-specific observed alleles
      alt (char)            alternate allele on the '+' strand
      molType (char)        sample type, can be one of unknown, genomic or cDNA
      class (char)          Class of variant (single, in-del, het, named, mixed, insertion,
                            deletion etc
      valid (char)          validation status, can be unknown, by-cluster, by-frequency, by-
                            submitter, by-2hit-2allele, by-hapmap, and by-1000genomes
      avHet (float)         Average heterozygosity from all observations
      avHetSE (float)       Standard error for the average heterozygosity
      func (char)           Functional cetegory of the SNP (coding-synon, coding-nonsynon,
                            intron, etc.)
      locType (char)        Type of mapping inferred from size on reference.
    

The fields are now available in the project, 

    % vtools show fields
    
    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    variant.AA (char)
    variant.AC (int)
    variant.AN (int)
    variant.DP (int)
    variant.id (char)
    refT.chr (char)         Chromosome name (VARCHAR)
    dbSNP.chr (char)
    dbSNP.start (int)       start position in chrom (1-based)
    dbSNP.end (int)         end position in chrom (1-based). start=end means zero-length
                            feature
    dbSNP.name (char)       dbSNP reference SNP identifier
    dbSNP.strand (char)     which DNA strand contains the observed alleles
    dbSNP.refNCBI (char)    Reference genomic sequence from dbSNP
    dbSNP.refUCSC (char)    Reference genomic sequence from UCSC lookup of
                            chrom,chromStart,chromEnd
    dbSNP.observed (char)   Strand-specific observed alleles
    dbSNP.alt (char)        alternate allele on the '+' strand
    dbSNP.molType (char)    sample type, can be one of unknown, genomic or cDNA
    dbSNP.class (char)      Class of variant (single, in-del, het, named, mixed, insertion,
                            deletion etc
    dbSNP.valid (char)      validation status, can be unknown, by-cluster, by-frequency, by-
                            submitter, by-2hit-2allele, by-hapmap, and by-1000genomes
    dbSNP.avHet (float)     Average heterozygosity from all observations
    dbSNP.avHetSE (float)   Standard error for the average heterozygosity
    dbSNP.func (char)       Functional cetegory of the SNP (coding-synon, coding-nonsynon,
                            intron, etc.)
    dbSNP.locType (char)    Type of mapping inferred from size on reference.

These fields can be used just like **variant info fields**, 

    % vtools output refT chr pos ref alt dbSNP.name --limit 5
    
    1	1105366	T	C	.
    1	1110240	T	A	.
    1	3537996	T	C	.
    1	6447088	T	C	.
    1	6447275	T	C	.
    

As you can see, not all variants are in dbSNP. If we select variants that are in dbSNP, about half of variants are in dbSNP, 

    % vtools select variant 'dbSNP.chr is not NULL' -t inDBSNP 'variants in dbSNP version 135'
    
    Running: 11 44.6/s in 00:00:00                                                           
    INFO: 12 variants selected.
    

We can check the details of variants in dbSNP using 

    % vtools output inDBSNP chr pos ref alt name strand func --limit 5
    
    1 	17786644 	G	A	rs149108668	+	unknown
    1 	150649639	C	T	rs148931998	+	intron
    2 	219318677	A	G	rs116720220	+	untranslated-3
    7 	128150523	G	A	rs146202908	+	unknown
    16	67424843 	C	T	rs144127847	+	missense
    

</details>



### 5. Track

A **track** file is a file that contains annotation information for variants and regions that can be displayed on the UCSC genome browser. It provides another source of annotation to *variant tools* through function `track(filename, field)`. *variant tools* currently support track files in tabix-indexed [vcf][3], indexed BAM, [bigBed][5], and [bigWig][6] formats. 

<details><summary>Examples:</summary> If we download a [bigWig annotation file](http://www.iq-darwin.cremag.org/resources/encode/hg19/pliki/wgEncodeGisRnaSeqH1hescCellPapPlusRawRep1.bigWig) from the [UCSC ENCODE website][7], you can use it to annotate and select variants, 



    % vtools output variant chr pos ref alt 'track("wgEncodeGisRnaSeqH1hescCellPapPlusRawRep1.bigWig")' -l 10
    
    1	1105366	T	C	3.0
    1	1105411	G	A	2.0
    1	1108138	C	T	.
    1	1110240	T	A	.
    1	1110294	G	A	.
    1	3537996	T	C	.
    1	3538692	G	C	.
    1	3541597	C	T	.
    1	3541652	G	A	1.0
    1	3545211	G	A	.
    

</details>



### 6. Sample, genotype & genotype info

A **sample** in variant tools refers to a collection of variants with optional associated **genotypes**, and **genotype info fields**. Here **genotype** refers to type of variants (homozygote, heterozygote or others) of a particular sample at a particular locus. If there is only one variant at a locus, a genotype can be `0` (all wildtype alleles), `1` (heterozygote), or `2` (homozygous alternative alleles). If there are more then one variants at a locus, a genotype can be `-1`, referring to two different alternative alleles. *variant tools currently does not consider phase of genotypes*. 

Each genotype can have any number of **genotype info fields**, which are information that describes a genotype, usually quality scores of each called variant. 

**Sample names** are important but not unique identifiers of samples. For example, genotypes belonging to the same physical sample might be imported from several files (e.g. chromosome by chromosome), resulting in several variant tools samples that share the same name. (In this case, you can use commands "`vtools admin --merge_samples`" to merge them into one sample). Samples are usually identified by an SQL query so you could use sample name, filenames from which samples are imported, and arbitrary phenotypes (e.g. affection status) to specify samples. 


{{% notice tip %}}
Not all samples have genotypes because variant tools can treat a list of variants as a sample. 
{{% /notice %}}

<details><summary>Examples:</summary> This project has two samples with names `CEU` and `JPT`: 

    % vtools show samples
    
    sample_name	filename
    CEU        	CEU.exon...3.sites.vcf.gz
    JPT        	JPT.exon...3.sites.vcf.gz


However, for this particular project, the samples are just lists of variants so there is no genotype and genotype fields. 

    % vtools show genotypes
    
    sample_name	filename                 	num_genotypes	sample_genotype_fields
    CEU        	CEU.exon...3.sites.vcf.gz	3489         	
    JPT        	JPT.exon...3.sites.vcf.gz	2900   
    

</details>



### 7. Phenotype

**Phenotypes** in variant tools are generally any properties of samples, such as blood pressure, weight, height, ethnicity, affection status, ID, and ID of parents. It could be [imported][8] from a text file, calculated from samples (e.g. average quality score of all variants of a sample could be a phenotype of the sample), or from other phenotypes. Phenotypes are frequently used to identify groups of samples (e.g. by affection status using parameter `--samples 'aff=1'`), and in genotype-phenotype association analysis. 

<details><summary>Examples:</summary> This project does not have any genotype and existing phenotype, we can add a phenotype `num` as the number of variants in each sample: 

    % vtools phenotype --from_stat 'num=#(GT)'
    
    Calculating phenotype: 100% [==========================================] 2 2.0/s in 00:00:01
    INFO: 2 values of 1 phenotypes (1 new, 0 existing) of 2 samples are updated.

    

The samples are now have a phenotype called `num`, 

    % vtools show samples
    
    sample_name	filename                 	num
    CEU        	CEU.exon...3.sites.vcf.gz	3489
    JPT        	JPT.exon...3.sites.vcf.gz	2900
    

</details>



### 8. Primary & alternative reference genome

Variant Tools supports build hg18 and hg19 of the human genome natively. For reference genome of other species, you will need to provide fasta sequences of the reference genome and use command `vtools admin --fasta2crr` to convert it to a binary format that can be used by variant tools. 

Because the same variants might have different coordinates on different reference genomes, it is very important to know the build of the reference genome of your data, which can be hg18 or hg19 for the human genome. The build information is important because it tells variant tools what annotation databases should be used. If you are uncertain about the reference genome used for your data, you could use a recent build and command `vtools admin --validate_build` to check if you have specified the correct build. 

A sequencing analysis project might sometimes need to handle data using different reference genomes. For example, you might need to use a new batch of sample with variants called using a more recent reference genome, or some public control data that use an older reference genome. Variant tools allows you to important data in an **alternative reference genome** in addition to a **primary reference genome** that the project uses. Variant tools will automatically convert between different coordinates so you do not have to worry about matching variants across datasets. 


{{% notice tip %}}
 Please use name `hg19` if your data uses `b37`, because the name `hg19` is used for all annotation databases. Note that variant tools uses `1`, `2` etc (for `b37`) instead of `chr1`, `chr2` etc (`for hg19`) internally but it can handle data sources with `chr1` etc. 
{{% /notice %}}
 
{{% notice tip %}}
Whereas projects with a single reference genome will have unique coordinates for variants (chr, pos), projects with two reference genomes might have missing or duplicate coordinates for each reference genome. This is because not all genomic locations could be mapped from one reference genome to another and two locations might be mapped to the same location on another reference genome. 
{{% /notice %}}


<details><summary>Examples:</summary> Our project uses reference genome hg19 so we used dbSNP version 135 because the latter versions of dbSNP make use of reference genome hg38. If you would like to use a newer version of dbSNP for this project, you can first add an alternative reference genome to the project by lifting over existing variants: 



    % vtools liftover hg38
    
    INFO: Downloading liftOver chain file from UCSC
    hg19ToHg38.over.chain.gz: 100% [=========================] 227,698.0 202.0K/s in 00:00:01
    INFO: Exporting variants in BED format
    Exporting variants: 100% [===================================] 4,858 196.3K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    INFO: 97 records failed to map.
    Updating table variant: 100% [=================================] 4,761 2.2K/s in 00:00:02

    

The project now has two reference genomes 



    % vtools show project

    Project name:                concept
    Created on:                  Sun May 27 21:13:47 2018
    Primary reference genome:    hg19
    Secondary reference genome:  hg38
    Storage method:              sqlite
    Runtime options:             verbosity=1, shared_resource=/Users/iceli/.variant_tools, local_resource=/Users/iceli/.variant_tools
    Variant tables:              inDBSNP
                                 refT
                                 variant
    Annotation databases:        dbSNP (~/.variant_tools/annoDB/dbSNP, hg19_135)


Now if we remove and re-link to dbSNP, we can use version 143 of the database 

    % vtools remove annotations dbSNP
    % vtools use dbSNP
    
    INFO: Removing annotation database dbSNP from the project
    INFO: Choosing version dbSNP-hg38s_143 from 10 available databases.
    INFO: Downloading annotation database annoDB/dbSNP-hg38_143.ann
    INFO: Downloading annotation database from annoDB/dbSNP-hg38_143.DB.gz
    dbSNP-hg38_143.DB.gz: 100% [============================] 1,892,708,890.0 5.5M/s in 00:35:44
    INFO: Decompressing /Users/iceli/.variant_tools/annoDB/dbSNP-hg38_143.DB.gz
    INFO: Using annotation DB dbSNP as dbSNP in project concept.
    INFO: dbSNP version 143

Now we can select variants in dbSNP 141 and save to another table 

    % vtools select variant 'dbSNP.chr is not NULL' -t inDBSNP143 'variants in dbSNP version 143'
    
    Running: 18 39.6/s in 00:00:00                                                              
    INFO: 4858 variants selected.
    

A lot more variants are selected, showing the importance of using the latest version of database: 

    % vtools show tables
    
    table         #variants     date message
    inDBSNP           2,550    May27 variants in dbSNP version 130
    inDBSNP141        4,858    May27 variants in dbSNP version 141
    refT                787    May27 variants with reference allele T
    variant           4,858    May27 Master variant table

</details>



### 9. Pipeline

**Pipelines** are sequences of commands defined in pipeline configuration files, and are executed by command `vtools execute`. Pipelines are used, among many possibilities, to use external commands such as `bwa` and `gatk` to align raw reads and call genetic variants from aligned reads.

 [1]: /vat-docs/documentation/keyconcepts/supportedtypes/
 [2]: /vat-docs/documentation/vtools_commands/import/
 [3]: http://www.1000genomes.org/wiki/Analysis/Variant%20Call%20Format/vcf-variant-call-format-version-41
 [4]: /vat-docs/documentation/vtools_commands/use/
 [5]: http://genome.ucsc.edu/goldenPath/help/bigBed.html
 [6]: http://genome.ucsc.edu/goldenPath/help/bigWig.html
 [7]: http://genome.ucsc.edu/ENCODE/
 [8]: /vat-docs/documentation/vtools_commands/phenotype/