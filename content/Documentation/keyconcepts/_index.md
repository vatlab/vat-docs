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
    % vtools import CEU_hg38_all.vcf --build hg38 --sample_name CEU --var_info AA AC AN DP
    % vtools import JPT_hg38_all.vcf --sample_name JPT --var_info AA AC AN DP

 

The project properties can be displayed as follows 

    % vtools show project
    
    Project name:                concept
    Primary reference genome:    hg38
    Secondary reference genome:  
    Storage method:              hdf5
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
    variant        4,839    May30 Master variant table
    

Each variant has chr, position, reference and alternative alleles, 

    % vtools output variant chr pos ref alt --limit 5
    
    1   1180123 T   C
    1   1180168 G   A
    1   1182895 C   T
    1   1184997 T   A
    1   1185051 G   A


We can select all variants with reference allele `T` and save the results to a **variant table** named `refT`, 

    % vtools select variant 'ref="T"' --to_table refT 'variants with reference allele T'
    
    Running: 3 1.5K/s in 00:00:00
    INFO: 780 variants selected.
    

Now there are two variant tables `variant` and `refT` in this project 

    % vtools show tables
    
    table      #variants     date message
    refT             780    May30 variants with reference allele T
    variant        4,839    May30 Master variant table
    

As you can see, all variants in table `refT` have reference allele `T`: 

    % vtools output refT chr pos ref alt --limit 5
    
    1   1180123 T   C
    1   1184997 T   A
    1   3631572 T   C
    1   6464441 T   C
    1   6464628 T   C
    

</details>




### 3. Variant info & variant info field

**Variant info** refers to information that describes a variant, such as the INFO fields of a [vcf file][3]. It usually consists of annotation information such as membership in dbSNP, or sample statistics such as sample frequency of each variant. The names of these info are called **variant info fields** and can be displayed using command `vtools show fields`. 

<details><summary>Examples:</summary> The project has 4 variant info fields `AA`, `AC`, `AN`, and `DP`, as shown by the following command 

    % vtools show fields
    
    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    variant.AA (char)
    variant.AC (int)
    variant.AN (int)
    variant.DP (int)
    refT.chr (char)         Chromosome name (VARCHAR)

    

These fields are imported from the INFO fields of the vcf file, and are the ancestral allele, total number of alternate alleles in called genotypes, total number of alleles in called genotypes, and Read Depth from MOSAIK BAM, respectively, for each variant. These fields could be outputted for each variant, 



    % vtools  output refT chr pos ref alt AA AC AN DP --limit 5
    
    1   1180123 T   C   T   4   114 3251
    1   1184997 T   A   T   1   178 7275
    1   3631572 T   C   C   156 156 1753
    1   6464441 T   C   T   12  172 4691
    1   6464628 T   C   T   9   176 6871
    

More variant info fields could be added to the project using command `vtools update`. 



    % vtools update variant --from_file CEU_hg38_all.vcf --var_info id 
    
    INFO: Using primary reference genome hg38 of the project.
    Getting existing variants: 100% [=======================] 4,839 372.4K/s in 00:00:00
    INFO: Updating variants from CEU_hg38_all.vcf (1/1)
    CEU_hg38_all.vcf: 100% [==================================] 3,512 7.4K/s in 00:00:00
    Getting existing variants: 100% [=======================] 4,839 368.5K/s in 00:00:00



    $ vtools output refT chr pos ref alt id AA AC AN DP -l 5
    
    1   1180123 T   C   .           T   4   114 3251
    1   1184997 T   A   .           T   1   178 7275
    1   3631572 T   C   rs2760321   C   156 156 1753
    1   6464441 T   C   rs11800462  T   12  172 4691
    1   6464628 T   C   rs3170675   T   9   176 6871
    

</details>



### 4. Annotation databases & annotation fields

**Annotation databases** are databases that provide annotation information for variants. They are not part of a project but they provide additional **annotation fields** to a project when they are [linked][4] to a project. Conceptually speaking, attaching annotation databases to a project adds info fields to variants of the project, although annotation databases usually annotate only part of the variants, leaving a lot of `NULL` values for these fields. 

<details><summary>Examples:</summary> Let us download and use an annotation database `dbSNP` version 135 for reference genome hg19

    % vtools use dbSNP
    
    INFO: Choosing version dbSNP-hg38_143 from 10 available databases.
    INFO: Downloading annotation database annoDB/dbSNP-hg38_143.ann
    INFO: Using annotation DB dbSNP as dbSNP in project concept.
    INFO: dbSNP version 143, created using vcf file downloaded from NCBI

This database provides the following **annotation fields** 

    % vtools show annotation dbSNP
    
    Annotation database dbSNP (version hg38_143)
    Description:            dbSNP version 143, created using vcf file downloaded from NCBI
    Database type:          variant
    Reference genome hg38:  chr, pos, ref, alt
      chr (char)
      pos (int)
      name (char)           DB SNP ID (rsname)
      ref (char)            Reference allele (as on the + strand)
      alt (char)            Alternative allele (as on the + strand)
      FILTER (char)         Inconsistent Genotype Submission For At Least One Sample
      RS (int)              dbSNP ID (i.e. rs number)
      RSPOS (int)           Chr position reported in dbSNP
      RV (int)              RS orientation is reversed
      VP (char)             Variation Property.  Documentation is at ftp://ftp.ncbi.nlm.nih.gov/snp/specs/dbSNP_BitField_latest.pdf
      GENEINFO (char)       Pairs each of gene symbol:gene id.  The gene symbol and id are delimited by a colon (</summary>and each pair is delimited by a vertical bar (|)
      dbSNPBuildID (int)    First dbSNP Build for RS
      SAO (int)             Variant Allele Origin: 0 - unspecified, 1 - Germline, 2 - Somatic, 3 - Both
      SSR (int)             Variant Suspect Reason Codes (may be more than one value added together) 0 - unspecified, 1 - Paralog, 2 - byEST, 4 - oldAlign, 8 - Para_EST, 16 - 1kg_failed,
                            1024 - other
      WGT (int)             Weight, 00 - unmapped, 1 - weight 1, 2 - weight 2, 3 - weight 3 or more
      VC (char)             Variation Class
      PM_flag (int)         Variant is Precious(Clinical,Pubmed Cited)
      TPA_flag (int)        Provisional Third Party Annotation(TPA) (currently rs from PHARMGKB who will give phenotype data)
      PMC_flag (int)        Links exist to PubMed Central article
      S3D_flag (int)        Has 3D structure - SNP3D table
      SLO_flag (int)        Has SubmitterLinkOut - From SNP->SubSNP->Batch.link_out
      NSF_flag (int)        Has non-synonymous frameshift A coding region variation where one allele in the set changes all downstream amino acids. FxnClass = 44
      NSM_flag (int)        Has non-synonymous missense A coding region variation where one allele in the set changes protein peptide. FxnClass = 42
      NSN_flag (int)        Has non-synonymous nonsense A coding region variation where one allele in the set changes to STOP codon (TER). FxnClass = 41
      REF_flag_flag (int)   Has reference A coding region variation where one allele in the set is identical to the reference sequence. FxnCode = 8
      SYN_flag (int)        Has synonymous A coding region variation where one allele in the set does not change the encoded amino acid. FxnCode = 3
      U3_flag (int)         In 3' UTR Location is in an untranslated region (UTR). FxnCode = 53
      U5_flag (int)         In 5' UTR Location is in an untranslated region (UTR). FxnCode = 55
      ASS_flag (int)        In acceptor splice site FxnCode = 73
      DSS_flag (int)        In donor splice-site FxnCode = 75
      INT_flag (int)        In Intron FxnCode = 6
      R3_flag (int)         In 3' gene region FxnCode = 13
      R5_flag (int)         In 5' gene region FxnCode = 15
      OTH_flag (int)        Has other variant with exactly the same set of mapped positions on NCBI refernce assembly.
      CFL_flag (int)        Has Assembly conflict. This is for weight 1 and 2 variant that maps to different chromosomes on different assemblies.
      ASP_flag (int)        Is Assembly specific. This is set if the variant only maps to one assembly
      MUT_flag (int)        Is mutation (journal citation, explicit fact): a low frequency variation that is cited in journal and other reputable sources
      VLD_flag (int)        Is Validated.  This bit is set if the variant has 2+ minor allele count based on frequency or genotype data.
      G5A_flag (int)        >5% minor allele frequency in each and all populations
      G5_flag (int)         >5% minor allele frequency in 1+ populations
      HD_flag (int)         Marker is on high density genotyping kit (50K density or greater).  The variant may have phenotype associations present in dbGaP.
      GNO_flag (int)        Genotypes available. The variant has individual genotype (in SubInd table).
      KGValidated_flag (int)
                            1000 Genome validated
      KGPhase1_flag (int)   1000 Genome phase 1 (incl. June Interim phase 1)
      KGPilot123_flag (int) 1000 Genome discovery all pilots 2010(1,2,3)
      KGPROD_flag (int)     Has 1000 Genome submission
      OTHERKG_flag (int)    non-1000 Genome submission
      PH3_flag (int)        HAP_MAP Phase 3 genotyped: filtered, non-redundant
      CDA_flag (int)        Variation is interrogated in a clinical diagnostic assay
      LSD_flag (int)        Submitted from a locus-specific database
      MTP_flag (int)        Microattribution/third-party annotation(TPA:GWAS,PAGE)
      OM_flag (int)         Has OMIM/OMIA
      NOC_flag (int)        Contig allele not present in variant allele list. The reference sequence allele at the mapped position is not present in the variant allele list, adjusted for
                            orientation.
      WTD_flag (int)        Is Withdrawn by submitter If one member ss is withdrawn by submitter, then this bit is set.  If all member ss' are withdrawn, then the rs is deleted to
                            SNPHistory
      NOV_flag (int)        Rs cluster has non-overlapping allele sets. True when rs set has more than 2 alleles from different submissions and these sets share no alleles in common.
      CAF (char)            An ordered, comma delimited list of allele frequencies based on 1000Genomes, starting with the reference allele followed by alternate alleles as ordered in the
                            ALT column. Where a 1000Genomes alternate allele is not in the dbSNPs alternate allele set, the allele is added to the ALT column.  The minor allele is the
                            second largest value in the list, and was previuosly reported in VCF as the GMAF.  This is the GMAF reported on the RefSNP and EntrezSNP pages and
                            VariationReporter
      COMMON (int)          RS is a common SNP.  A common SNP is one that has at least one 1000Genomes population with a minor allele of frequency >= 1% and for which 2 or more founders
                            contribute to that minor allele frequency.

    

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
    dbSNP.pos (int)
    dbSNP.name (char)       DB SNP ID (rsname)
    dbSNP.ref (char)        Reference allele (as on the + strand)
    dbSNP.alt (char)        Alternative allele (as on the + strand)
    dbSNP.FILTER (char)     Inconsistent Genotype Submission For At Least One Sample
    dbSNP.RS (int)          dbSNP ID (i.e. rs number)
    dbSNP.RSPOS (int)       Chr position reported in dbSNP
    dbSNP.RV (int)          RS orientation is reversed
    dbSNP.VP (char)         Variation Property.  Documentation is at ftp://ftp.ncbi.nlm.nih.gov/snp/specs/dbSNP_BitField_latest.pdf
    dbSNP.GENEINFO (char)   Pairs each of gene symbol:gene id.  The gene symbol and id are delimited by a colon (</summary>and each pair is delimited by a vertical bar (|)
    dbSNP.dbSNPBuildID (int)
                            First dbSNP Build for RS
    dbSNP.SAO (int)         Variant Allele Origin: 0 - unspecified, 1 - Germline, 2 - Somatic, 3 - Both
    dbSNP.SSR (int)         Variant Suspect Reason Codes (may be more than one value added together) 0 - unspecified, 1 - Paralog, 2 - byEST, 4 - oldAlign, 8 - Para_EST, 16 - 1kg_failed,
                            1024 - other
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
    dbSNP.NOC_flag (int)    Contig allele not present in variant allele list. The reference sequence allele at the mapped position is not present in the variant allele list, adjusted for
                            orientation.
    dbSNP.WTD_flag (int)    Is Withdrawn by submitter If one member ss is withdrawn by submitter, then this bit is set.  If all member ss' are withdrawn, then the rs is deleted to
                            SNPHistory
    dbSNP.NOV_flag (int)    Rs cluster has non-overlapping allele sets. True when rs set has more than 2 alleles from different submissions and these sets share no alleles in common.
    dbSNP.CAF (char)        An ordered, comma delimited list of allele frequencies based on 1000Genomes, starting with the reference allele followed by alternate alleles as ordered in the
                            ALT column. Where a 1000Genomes alternate allele is not in the dbSNPs alternate allele set, the allele is added to the ALT column.  The minor allele is the
                            second largest value in the list, and was previuosly reported in VCF as the GMAF.  This is the GMAF reported on the RefSNP and EntrezSNP pages and
                            VariationReporter
    dbSNP.COMMON (int)      RS is a common SNP.  A common SNP is one that has at least one 1000Genomes population with a minor allele of frequency >= 1% and for which 2 or more founders
                            contribute to that minor allele frequency.



These fields can be used just like **variant info fields**, 

    % vtools output refT chr pos ref alt dbSNP.name --limit 5
    
    1   1180123 T   C   rs111751804
    1   1184997 T   A   rs116321663
    1   3631572 T   C   rs2760321
    1   6464441 T   C   rs11800462
    1   6464628 T   C   rs3170675
    

As you can see, not all variants are in dbSNP. If we select variants that are in dbSNP, about half of variants are in dbSNP, 

    % vtools select variant 'dbSNP.chr is not NULL' -t inDBSNP 'variants in dbSNP version 143'
    
    Running: 18 8.3/s in 00:00:02
    INFO: 4833 variants selected.
    

We can check the details of variants in dbSNP using 

    % vtools output inDBSNP chr pos ref alt name GENEINFO --limit 5
    
   1    1180123 T   C   rs111751804 TTLL10:254173|TTLL10-AS1:100506376
    1   1180168 G   A   rs114390380 TTLL10:254173|TTLL10-AS1:100506376
    1   1182895 C   T   rs61733845  TTLL10:254173
    1   1184997 T   A   rs116321663 TTLL10:254173
    1   1185051 G   A   rs1320571   TTLL10:254173
    

</details>



### 5. Track

A **track** file is a file that contains annotation information for variants and regions that can be displayed on the UCSC genome browser. It provides another source of annotation to *variant tools* through function `track(filename, field)`. *variant tools* currently support track files in tabix-indexed [vcf][3], indexed BAM, [bigBed][5], and [bigWig][6] formats. 

<details><summary>Examples:</summary> If we download a [bigWig annotation file](http://www.iq-darwin.cremag.org/resources/encode/hg19/pliki/wgEncodeGisRnaSeqH1hescCellPapPlusRawRep1.bigWig) from the [UCSC ENCODE website][7], you can use it to annotate and select variants, 



    % vtools output variant chr pos ref alt 'track("wgEncodeGisRnaSeqH1hescCellPapPlusRawRep1.bigWig")' -l 10
    

    

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
    
    sample_name filename
    CEU         CEU_hg38_all.vcf
    JPT         JPT_hg38_all.vcf


However, for this particular project, the samples are just lists of variants so there is no genotype and genotype fields. 

    % vtools show genotypes
    
    sample_name filename            num_genotypes   sample_genotype_fields
    CEU         CEU_hg38_all.vcf    3470            GT
    JPT         JPT_hg38_all.vcf    2878            GT  
    

</details>



### 7. Phenotype

**Phenotypes** in variant tools are generally any properties of samples, such as blood pressure, weight, height, ethnicity, affection status, ID, and ID of parents. It could be [imported][8] from a text file, calculated from samples (e.g. average quality score of all variants of a sample could be a phenotype of the sample), or from other phenotypes. Phenotypes are frequently used to identify groups of samples (e.g. by affection status using parameter `--samples 'aff=1'`), and in genotype-phenotype association analysis. 

<details><summary>Examples:</summary> This project does not have any genotype and existing phenotype, we can add a phenotype `num` as the number of variants in each sample: 

    % vtools phenotype --from_stat 'num=#(GT)'
    
    Calculating phenotype: 100% [==========================================] 2 2.0/s in 00:00:01
    INFO: 2 values of 1 phenotypes (1 new, 0 existing) of 2 samples are updated.

    

The samples are now have a phenotype called `num`, 

    % vtools show samples
    
    sample_name filename            num
    CEU         CEU_hg38_all.vcf    3470
    JPT         JPT_hg38_all.vcf    2878
    

</details>



### 8. Primary & alternative reference genome

Variant Tools supports build hg18, hg19 and hg38 of the human genome natively. For reference genome of other species, you will need to provide fasta sequences of the reference genome and use command `vtools admin --fasta2crr` to convert it to a binary format that can be used by variant tools. 

Because the same variants might have different coordinates on different reference genomes, it is very important to know the build of the reference genome of your data, which can be hg18, hg19 or hg38 for the human genome. The build information is important because it tells variant tools what annotation databases should be used. If you are uncertain about the reference genome used for your data, you could use a recent build and command `vtools admin --validate_build` to check if you have specified the correct build. 

A sequencing analysis project might sometimes need to handle data using different reference genomes. For example, you might need to use a new batch of sample with variants called using a more recent reference genome, or some public control data that use an older reference genome. Variant tools allows you to important data in an **alternative reference genome** in addition to a **primary reference genome** that the project uses. Variant tools will automatically convert between different coordinates so you do not have to worry about matching variants across datasets. 


{{% notice tip %}}
 Please use name `hg19` if your data uses `b37`, because the name `hg19` is used for all annotation databases. Note that variant tools uses `1`, `2` etc (for `b37`) instead of `chr1`, `chr2` etc (`for hg19`) internally but it can handle data sources with `chr1` etc. 
{{% /notice %}}
 
{{% notice tip %}}
Whereas projects with a single reference genome will have unique coordinates for variants (chr, pos), projects with two reference genomes might have missing or duplicate coordinates for each reference genome. This is because not all genomic locations could be mapped from one reference genome to another and two locations might be mapped to the same location on another reference genome. 
{{% /notice %}}


<details><summary>Examples:</summary> Our project uses reference genome hg38 so we used dbSNP version 143 . If you would like to use another version of dbSNP for this project, you can first add an alternative reference genome to the project by lifting over existing variants: 



    % vtools liftover hg19
    
    INFO: Downloading liftOver chain file from UCSC
    INFO: Exporting variants in BED format
    Exporting variants: 100% [===========================] 4,839 250.8K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating table variant: 100% [========================] 4,839 735.4/s in 00:00:06


    

The project now has two reference genomes 



    % vtools show project

    Project name:                concept
    Primary reference genome:    hg38
    Secondary reference genome:  hg19
    Storage method:              hdf5
    Variant tables:              inDBSNP
                                 refT
                                 variant
    Annotation databases:        dbSNP (~/.variant_tools/annoDB/dbSNP, hg38_143)


Now if we remove and re-link to dbSNP, we can use version 141 of the database 

    % vtools remove annotations dbSNP
    % vtools use dbSNP-hg19_141
    
    INFO: Downloading annotation database annoDB/dbSNP-hg19_141.ann
    INFO: Using annotation DB dbSNP as dbSNP in project concept.
    INFO: dbSNP version 141

    % vtools select variant 'dbSNP.chr is not NULL' -t inDBSNP 'variants in dbSNP version 141'
    
    Running: 18 484.7/s in 00:00:00
    INFO: 4833 variants selected.
    
<!-- 
A lot more variants are selected, showing the importance of using the latest version of database: 

    % vtools show tables -->
    

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