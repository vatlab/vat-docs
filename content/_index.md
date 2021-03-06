## Home of Variant Tools

<figure>
  <p><a href="vtools.pdf"><img src="1.jpg"></a>
  <figcaption>A presentation about variant tools (Oct, 3rd, 2013)</figcaption>
</figure>

*Variant tools* is a software tool for the manipulation, annotation, selection, simulation, and analysis of *variants* in the context of next-gen sequencing analysis. Unlike some other tools used for Next-Gen sequencing analysis, variant tools is project based and provides a whole set of tools to manipulate and analyze genetic variants. Please refer to [what you can do with variant tools](#anchor) for a list of features provided by variant tools. 

### News

*   May 10, 2016: We have released a docker container for variant tools called \`mdabioinfo/varianttools\`, which allows users to test variant tools without installing it. 
*   Jan 20th, 2016: Release of variant tools 2.7.0, with significantly improved variant pipeline tools and support for arbitrary reference genome. 
*   Jan 15th, 2015: Release of variant tools 2.6.1, which fixes some issues with Python 3. 
*   Dec 20th, 2014: Release of variant tools 2.6.0. This version cleans up the pipeline code to assist users to write customized pipelines and actions. 
*   Nov 10th, 2014: Release of variant tools 2.5.1, which is a maintenance release that address a bug with 2.5.0 on the use of user-specified `temp_dir`. Manhattan and QQ plot engine is also updated to work with ggplot2 version 1.0.0 (backward compatibility is dropped). 
*   Oct 15th, 2014: Release of variant tools 2.5.0 with new variant tools repository. The variant tools repository used by variant tools 2.4.0 and earlier has been discontinued.  <font color=#FF0000>**Please upgrade to variant tools 2.5.0 to access the new repository**. </font>
*   Aug 15th, 2014: Release of variant tools 2.4.0. 
*   Feb 27th, 2014: Release of variant tools 2.3.0. 
*   Jan 16th, 2014: Release of variant tools 2.2.0. 
*   Nov 6th, 2013: Release of variant tools 2.1.0, which adds a few useful features such as functions [`genotype()`][47] and [`samples()`][48] SQL function, and the `--as` option to command [`vtools use`][3]. 
*   Oct 9, 2013: Release of variant tools 2.0.1, which is a maintenance release of version 2.0.0. 
*   Aug 27, 2013: Release of variant tools 2.0. This is a major release of variant tools with many new features. Please check [ChangeLog][4] for details. 

<details><summary>More...</summary>

*   May 16, 2013: Release of variant tools 1.0.6, which contains a lot of small features and bug fixes. 
*   Mar 20, 2013: Release of variant tools 1.0.5. This release adds commands `vtools admin --update_resource` and `vtools_report sequences`, and allows the use of arbitrary characters for names of variant tables. 
*   Feb 20, 2013: Release of variant tools 1.0.4. This release comes with numerous bug fixed and new minor features. Please check the ChangeLog for details. 
*   Oct 21, Nov 10, Nov 26, and Nov 29. 2012: Release of variant tools 1.0.3a, b, c and d to address various small issues. 
*   Sep 25, 2012: Release of variant tools version 1.0.3, with new features and improvements in `vtools associate`, `vtools update`, `vtools phenotype` and `vtools_report` commands. 
*   Jul 9th, 2012: Release of variant tools version 1.0.3rc1. Other than a few bug fixes and major performance improvements, this release introduces new commands `vtools associate` and `vtools admin`, with more than 20 association tests implemented under a unified association test framework. 
*   Jan 24th, 2012: Release of variant tools version 1.0.2. This release fixes a major bug that causes duplicate output in commands `vtools output` and `vtools export` when range-based annotation databases are used. All users are recommended to upgrade. 
*   Jan 2nd, 2012: Release of variant tools version 1.0.1. This version contains a few new features and bug fixes, and more importantly, dramatic performance improvement for many commands. Please refer to [ChangeLog][4] for details about this release. 
*   Dec 30th, 2011: the gwasCatalog annotation source is available for download. See [examples][5] of how to use [gwasCatalog][5] to find published GWA hits that are near your variants. 
*   Dec 15th, 2011: Two new annotation sources are available: Cancer Gene Census from the Cancer Genome Project, and the 5400 exomes EVS annotation database from the NHLBI Exome Sequencing Project. 
*   Dec 4th, 2011: An [application note][6] that describes variant tools has been published online in *Bioinformatics*. 
*   Nov 13, 2011: Release of variant tools version 1.0. 
*   Jan 24th, 2012: Release of variant tools version 1.0.2. This release fixes a major bug that causes duplicate output in commands `vtools output` and `vtools export` when range-based annotation databases are used. All users are recommended to upgrade. 
*   Jan 2nd, 2012: Release of variant tools version 1.0.1. This version contains a few new features and bug fixes, and more importantly, dramatic performance improvement for many commands. Please refer to [ChangeLog][4][?][4] for details about this release. 
*   Dec 30th, 2011: the gwasCatalog annotation source is available for download. See [examples][5] of how to use [gwasCatalog][5] to find published GWA hits that are near your variants. 
*   Dec 15th, 2011: Two new annotation sources are available: Cancer Gene Census from the Cancer Genome Project, and the 5400 exomes EVS annotation database from the NHLBI Exome Sequencing Project. 
*   Dec 4th, 2011: An [application note][6] that describes variant tools has been published online in *Bioinformatics*. 
*   Nov 13, 2011: Release of variant tools version 1.0. 
*   Nov 7, 2011: A new annotation source called **[EVS (Exome Variant Server)][7]** is available consisting of exome sequencing variants from the NHLBI Exome Sequencing Project (ESP). This data was retrieved from the project's EVS server and contains population-specific allele frequencies (currently for European Americans and African Americans) and various functional annotations for predicted variants in approximately 2500 exomes. 
*   Nov 2, 2011: Release of release candidate version 1.0rc3. This version adds option `--jobs` to a number of vtools commands and allow them to execute in multiple threads or processes. User interface is further cleaned for the final 1.0 release. As a result, support for the MySQL backend is temporarily disabled. 
*   Oct 16, 2011: Release of release candidate version 1.0rc2. This version has a new option `--children` for command `vtools init`, which allows the creation of a project by merging multiple subprojects. 
*   Oct 7, 2011: Release of release candidate version 1.0rc1. This version has a new `vtools export` command that can export in ANNOVAR and VCF formats. 
*   Sep 27, 2011: Release of the second beta. This version contains full Python 3 support and a much more powerful `vtools import` command. 
*   Sep 10, 2011: Release of 1.0 beta. 
*   July 15, 2011: Initial public release. 
</details>

### The integrative design of *variant tools*

If you have used other sequencing or association analysis tools such as bedtools and pseq, you will be surprised that *variant tools* usually does not give you a nice report with a list of variants or genes with some useful information after performing an analysis. Instead, **all the information, including results of analysis, are saved in the project in a consistent manner**. An extra step is needed to output the information you need. In other words, the management and presentation of information regarding variants are two different processes, and you typically add more and more information to your project during analysis of your data. The end result is that **you have immediate access to a large amount of information for the variants you are interested in, which can in turn help you perform more in-depth analysis**. Using a fabricated and unusually long command, 


```
% vtools output                                            # 2
            myvariants                                     # 1
            chr pos ref alt                                # 3
            hom_case hom_ctrl                              # 4
            dbNSFP.SIFT_score dbSNP.name refGene.name2     # 5
            asso1.p_value asso2.p_value                    # 6
            "ref_sequence(chr, pos - 5, pos + 5)"          # 7             
            "track('LP056A.BAM')"                          # 8
            "genotype('WGS1')"                             # 9
            "samples()"
```


1.  `myvariants` contains a list of variants, which is a subset of the *master variant table* (all the variant of your project) and is typically created using command `vtools select`. 
2.  Command `vtools output` output information for all variants in `myvariant`, which include 
3.  `chr`, `pos`, `ref`, `alt` constitute a *variant*, namely location and type of a mutation. 
4.  `hom_case` and `hom_ctrl` are number of homozygous genotypes of this variant in cases and controls. These are called *variant info fields* and are added to the project using command `vtools update --from_stat` 
5.  `dbNSFP.SIFT_score`, `dbSNP.name` and `refGene.name2` are annotation information from different annotation databases. Annotation databases are not part of the project. They are connected to the project using command `vtools use`. 
6.  `asso1.p_value` and `asso2.p_value` are results of two different association analysis. These are annotation databases created by command `vtools associate`. 
7.  [`ref_sequence`][23]
   is a function provided by *variant tools* to retrieve the reference sequence around the variant. Here 5 basepair of the up and downstream of each variant is returned. 
8.  [`track`][41]
        is a function to extract information from external files. In this example, the depth of coverage at the location of the variant in the specified bam file is returned. 
9.  [`genotype`][47]
 is another function to get the genotype of this variant in sample `WGS1`, for example, 1 for heterozygote and 2 for homozygote. Function `samples()` lists the samples that contain the variant. 

As you can see, individual commands such as `vtools use` and `vtools update` do not produce any output, but adds information to the project that can be displayed along with others. Then, it is important to remember that all such information can be used to select, prioritize, and analyze your variants. Another fabricated command would look like 



    % vtools select                                             # 1
               myvariants                                       # 2
               "refGene.name2='BRCA1'"                          # 3
               'dbNSFP.SIFT_score > 0.95'                   
               'hom_case > 15' 'hom_ctrl = 0'                   # 4
               'asso1.p_value < 0.05 OR asso2.p_value < 0.05'   # 5
               --to_table significant                           # 6


1.  Command `vtools select` selects variants according to their properties 
2.  It starts from table `myvariants`, which was itself selected using some other crieteria, 
3.  The variants must be in gene `BRCA1` and must have > 0.95 SIFT scores (probably damagin) 
4.  it should appear in at least 15 of the cases as homozygote, and not available (as homozygote) in any of the controls 
5.  and it should be significant in one of the association tests, 
6.  the selected variant are written to another table names `significant`. 

In summary, *variant tools* is NOT designed to be a black-box tool that analyzes your data and generates a nice-looking report with a list of candidate variants or genes. It is a platform under which you can analyze your data using several methods, compare and analyze results, re-compare and re-analyze, and again using different methods or annotation sources, based on the information abtained from your previous analyses.** The unique advantage of *variant tools* is that you generally do not need to write a bunch of scripts to *connect* input output of different tools and *parse* and *compare* results in different formats, and you have easy access to a huge amount of information that help you select, prioritize and analyze your variants, all from your command line. However, because of the uniqueness of this design, **please read through the [Concepts][8] section of this website before using *variant tools*.** 

<span id = "anchor"></span>

### Things you can do with variant tools

|**Catagory**|         **Tasks**       |
| ---------- | ----------------------- |
| Variant calling        | [Call variants from raw reads in FASTQ or BAM (convert to FASTQ first) formats using the GATK best practice pipeline.][9]                                                                                                                                             |
| Import variants        | [Import variants and genotypes in VCF format, with options to import specified variant and genotype info fields.][10]                                                                                                                                               |
|                        | [Import all info and genotype fields, including customized fields from VCF files.][11]                                                                                                                                                                                        |
|                        | Import [SNP][12] and [Indel][13] variants from the Illumina CASAVA pipeline before version 1.8 (text files), and variants called from the [Complete Genomics pipeline][14].                                                                                            |
|                        | [Pipeline to import variants from the recent versions of the Illumina CASAVA pipeline (in VCF format) that provides variant calls from two probabilistic models.][15]                                                                                               |
|                        | Import variants in [text][16] or [CSV][17] files.                                                                                                                                                                                                               |
|                        | Import variants from files in [Plink format][18].                                                                                                                                                                                                                    |
|                        | Import variants from [a list of rsnames (dbSNP IDs)][19], or [just chromsome and positions][20], variant information are retrieved from the dbSNP database.                                                                                                     |
|                        | Import data in arbitrary format by defining customized [format-description file][21].                                                                                                                                                                                  |
| Reference genome       | Native support for build `hg18` and `hg19` of the human genome, and other genomes such as the mouse genome. Reference genomes of the human genomes are downloaded automatically when they are used.                                                                           |
|                        | [Variants in different reference genomes can be imported and analyzed together][10], through automatic mapping between primary and alternative reference genomes.                                                                                                      |
|                        | Supports the use of annotations in a different reference genome by [mapping genomic coordinates across reference genomes][22].                                                                                                                                         |
|                        | [Easily retrieve reference sequences around variant sites through function `ref_sequence`][23]. This allows you to check if variants are in, for example, mononucleotide or short-tandem repeat sequences.                                                             |
|                        | [Validate the build of reference genome][24] if you are uncertain about the reference genome used in the data.                                                                                                                                                         |
| Variant annotation     | Standardize annotations from different sources so that you do not have to worry about inconsistencies between the use of chromosome names (with/without leading `chr`), genomic positions (0- or 1-based) and other nomenclatures.                                            |
|                        | Annotations are automatically downloaded from online repository, or build from source if needed. Annotation databases are automatically updated although you can use a prior version, or use different versions of the same annotation database at the same time.             |
|                        | Detailed descriptions of available annotation databases are readily available from command `vtools show annotation`.                                                                                                                                                          |
|                        | Supports [CCDS][25], [Entrez][26], [Known Gene][27], and [ref seq][28] definitions of genes, which allow you to identify variants in genes, exon regions, or upstream/downstream of these genes.                                                  |
|                        | Standardize gene names through the use of [HUGO Gene Nomenclature Committee approved gene names][29].                                                                                                                                                           |
|                        | Identify variants in [Catalogue of Somatic Mutations in Cancer][30] or within [Database of Genomic Variants][31].                                                                                                                                               |
|                        | Identify variants in [all versions of dbSNP databases][32], [Exome Sequencing project][7], the [thousand genomes project][33], and the [HapMap project][34].                                                                                      |
|                        | Annotate variants with SIFT, PolyPhen, MutationTaster and many other prediction scores from [dbNSFP][35].                                                                                                                                                              |
|                        | Check for variants that are in the [GWAS Catalog][5] database, or variants that are within certain range of GWAS hits.                                                                                                                                                  |
|                        | Identify variants in highly conserved regions through the [phastCons][36] database, or variants in [genomic duplication regions][37].                                                                                                                           |
|                        | Pipelines to automatically annotate variants using [ANNOVAR][38] and [snpEff][39].                                                                                                                                                                             |
|                        | Allow the [creation of annotation databases from your own data in vcf format][40].                                                                                                                                                                                     |
|                        | [Convert variants in a variant tools project to an annotation database to be used by another project][40], or [convert an annotation database to a project for detailed analysis][40].                                                                          |
|                        | Users can define and create their own annotation databases through [Annotation/New/customized annotation description files].                                                                                                                                                 |
| External Annotation    | Retrieve calls, reads, quality, and coverage information from [BAM files][41], filtered by quality score, strand, type, or flags, and use such information to select variants. This provides a command line alternative to IGV to check raw reads for called variants. |
|                        | Retreive variant info and genotype information from local or online [tabix indexed vcf.gz files][41], this allows you, for example, to obtain variant info from vcf files on the 1000 genomes website.                                                                 |
|                        | Retrive annotation from [bigWig][41] or [bigBed][41] files, from the ENCODE project.                                                                                                                                                                             |
| Samples and Phenotypes | Import and keep track of samples using filename and sample names.                                                                                                                                                                                                             |
|                        | [Rename samples][24] and [merge genotypes from multiple input files][24].                                                                                                                                                                                       |
|                        | Arbitrary sample information such as sex, BMI, and ethnicity can be saved as phenotype and used for sample selection or association analysis.                                                                                                                                 |
|                        | [Calculation of number of genotypes, alternative alleles, homozygotes, heterzygotes and other types of genotypes in all or subset of samples.][42]                                                                                                                     |
|                        | [Calculate minimal, maximum, average values of genotype info (e.g. quality score) across all or selected samples for each variant.][42]                                                                                                                             |
| Variant Selection      | [Use sample statistics to select, for example, homozygous variants with acceptable quality that appear only in cases.][43]                                                                                                                                             |
|                        | [Select variants based on their membership in annotation databases such as dbSNP and thousand genomes project.][43]                                                                                                                                                   |
|                        | [Select variants from multiple conditions that involves multiple variant and annotation info fields (e.g. SIFT score).][43]                                                                                                                                         |
|                        | Variants selected by different criteria are kept in multiple variant tables, with meta information.                                                                                                                                                                           |
|                        | [Compare variant tables and examine differences between two or more variant tables.][44]                                                                                                                                                                              |
|                        | [Identify De Novo mutations from family based samples, identify variants that share the same sites with an existing set of variants.][44]                                                                                                                           |
|                        | [Pipelines to identify de novo or recessive mutations that might cause the phenotype of an affected offspring in a family of unaffected parents.][45]                                                                                                                 |
| Output variants        | [Output a large number of variant info and annotation fields across different annotation databases altogether.][46]                                                                                                                                                    |
|                        | Output expressions of variant info and annotation fields, including vtools-specific SQL functions.                                                                                                                                                                            |
|                        | Output [reference sequence][23] around variant site, [genotypes][47] of one or more samples, and [samples][48] that harbor the variants.                                                                                                                 |
|                        | Output summary statistics (e.g. count, average) of variants and variant info fields, grouped by specified fields.                                                                                                                                                             |
| Export variants        | [Export][49] variants in vcf format, with variant and annotation info, and genotypes.                                                                                                                                                                                  |
|                        | Export variants in other formats such as [ANNOVAR][50] and [Plink][18] to be analyzed by these programs.                                                                                                                                                        |
|                        | Export variants with variant info and annotation fields in csv format.                                                                                                                                                                                                        |
| Association analysis   | [Use more than 20 association analysis methods to associate variants and genes with qualitative or quantitative traits.][51]                                                                                                                                           |
|                        | Execute multiple association tests across the genome using multiple processes.                                                                                                                                                                                                |
|                        | Results of association analyses are saved as annotation databases and are used to annotate individual variants, regardless of groups used to analyze data.                                                                                                                     |
|                        | [Draw manhantan and other figures][52] from association test results.                                                                                                                                                                                                  |
|                        | [Perform meta analysis][53] from association test results.                                                                                                                                                                                                              |
| Reports                | [Print reference sequences][54] for particular regions, or gene, exome etc.                                                                                                                                                                                            |
|                        | Calculate [discordance rate][55] between samples.                                                                                                                                                                                                                      |
|                        | Calculate [average depth of coverage][56], [number of SNPs and Indels][57] for all or selected samples.                                                                                                                                                         |
|                        | Calculate [transition transversion ratio][58] for all or selected variants.                                                                                                                                                                                            |
|                        | Scatter, box plot, histgram plots for [variant info fields][59], [genotype info fields][60], and [phenotypes][61].                                                                                                                                  |
| Data Management        | A project can be saved, transferred and loaded easily as [snapshots][24]. A number of online snapshots are provided for learning purposes.                                                                                                                             |
|                        | [Remove genotypes][62] based on different criteria (e.g. quality score), or [remove variants in a variant table][62].                                                                                                                                           |
|                        | [Merge data from several sub projects][63] (e.g. adding data from different batches).                                                                                                                                                                                  |
|                        | [Split project into sub projects][63] to focus on particular sets of variants or samples.                                                                                                                                                                              |
|                        | A resource management system to download and update resources on demand, or in batch.                                                                                                                                                                                         |
Please refer to [a list of tutorials][64] to get started. 







### Citation for variant tools


Please cite 

F. Anthony San Lucas, Gao Wang, Paul Scheet, and Bo Peng (2012) [**Integrated annotation and analysis of genetic variants from next-generation sequencing studies with variant tools**][65], Bioinformatics 28 (3): 421-422. 

for Variant Tools and 



Gao Wang, Bo Peng and Suzanne M. Leal (2014) [**Variant Association Tools for Quality Control and Analysis of Large-Scale Sequence and Genotyping Array Data**][66], The American Journal of Human Genetics 94 (5): 770–83. 

for Variant Association Tools, and 


Bo Peng (2014) [**Reproducible Simulations of Realistic Samples for Next-Generation Sequencing Studies Using Variant Simulation Tools**][67], Genetic Epidemiology. 

for Variant Simulation Tools if you find variant tools helpful and use it in your publication. Thank you.

 [3]:    /documentation/vtools_commands/use/
 [4]:   /development/changelog/
 [5]:   /applications/annotation/variants/gwas/
 [6]: http://bioinformatics.oxfordjournals.org/content/28/3/421
 [7]:   /applications/annotation/variants/esp/
 [8]:    /documentation/keyconcepts/
 [9]:    /documentation/pipelines/variant_calling/bwa_gatk28_hg19/
 [10]:    /documentation/vtools_commands/import/
 [11]:    /documentation/pipelines/other_pipelines/import_vcf/
 [12]:    /documentation/customization/format/supportedformats/casava18snps/
 [13]:    /documentation/customization/format/supportedformats/casava18indels/
 [14]:    /documentation/customization/format/supportedformats/cga/
 [15]:    /documentation/pipelines/other_pipelines/illumina/
 [16]:    /documentation/customization/format/supportedformats/txt/
 [17]:    /documentation/customization/format/supportedformats/csv/
 [18]:    /documentation/customization/format/supportedformats/plink/
 [19]:    /documentation/customization/format/supportedformats/rsname/
 [20]:    /documentation/customization/format/supportedformats/map/
 [21]:    /documentation/customization/format/supportedformats/new/
 [22]:    /documentation/vtools_commands/liftover/
 [23]:    /documentation/functions/ref_sequence/
 [24]:    /documentation/vtools_commands/admin/
 [25]:   /applications/annotation/genes/ccdsgene/
 [26]:   /applications/annotation/genes/entrezgene/
 [27]:   /applications/annotation/genes/knowngene/
 [28]:   /applications/annotation/genes/refgene/
 [29]:   /applications/annotation/genes/hugogene/
 [30]:   /applications/annotation/variants/cosmic/
 [31]:   /applications/annotation/variants/databaseof/
 [32]:   /applications/annotation/variants/dbsnp/
 [33]:   /applications/annotation/variants/thousand/
 [34]:   /applications/annotation/variants/hapmap/
 [35]:   /applications/annotation/variants/dbnsfp/
 [36]:   /applications/annotation/regions/phast_cons/
 [37]:   /applications/annotation/regions/genomic_super_dups/
 [38]:    /documentation/pipelines/other_pipelines/annovar/
 [39]:    /documentation/pipelines/other_pipelines/snpeff/
 [40]:    /documentation/pipelines/other_pipelines/anno_utils/
 [41]:    /documentation/functions/track/
 [42]:    /documentation/vtools_commands/update/
 [43]:    /documentation/vtools_commands/select/
 [44]:    /documentation/vtools_commands/compare/
 [45]:    /documentation/pipelines/other_pipelines/filtering/
 [46]:    /documentation/vtools_commands/output/
 [47]:    /documentation/functions/genotype/
 [48]:    /documentation/functions/samples/
 [49]:    /documentation/vtools_commands/export/
 [50]:    /documentation/customization/format/supportedformats/annovar/
 [51]:   /applications/association/
 [52]:    /documentation/vtools_report/plot_association
 [53]:    /documentation/vtools_report/meta_analysis
 [54]:    /documentation/vtools_report/sequence/
 [55]:    /documentation/vtools_report/discordance_rate/
 [56]:    /documentation/vtools_report/avg_depth/
 [57]:    /documentation/vtools_report/variant_stat/
 [58]:    /documentation/vtools_report/trans_ratio/
 [59]:    /documentation/vtools_report/plot_fields/
 [60]:    /documentation/vtools_report/plot_geno_fields/
 [61]:    /documentation/vtools_report/plot_pheno_fields/
 [62]:    /documentation/vtools_commands/remove/
 [63]:    /documentation/vtools_commands/init/
 [64]:    /documentation/tutorials/
 [65]: http://bioinformatics.oxfordjournals.org/content/28/3/421.abstract?sid=f64403e7-5050-4102-963c-e690efe003f7
 [66]: http://dx.doi.org/10.1016/j.ajhg.2014.04.004
 [67]: http://onlinelibrary.wiley.com/doi/10.1002/gepi.21867/abstract
