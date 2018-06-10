+++
title = "demon"
weight = 1
hidden = "true"
+++


## Demonstration of Quality Control and Association Analysis 




### 1. Getting Started

This section describes the data-set, required software and computational environment for the exome association analysis to be demonstrated in this tutorial. 



#### 1.1 Data Source

We use the exome data from the **1000 genomes project**. The entire data-set can be found at the [NCBI ftp site][1]. This release (version 3.0, April 30th, 2012) contains phased genotype calls on 1092 samples in VCF format, with 38.2M SNVs, 3.9M Short Indels and 14K Large Deletions. Data from different sources are pooled together. Targets for exome sequencing can be found at the [1000 genomes ftp site][2]. 

We created a snapshot dataset for this demonstration with the original exome data plus simulated genotype quality scores and phenotype values. The dataset is 2.1GB and can be automatically downloaded and loaded for use with the following commands: 



    vtools init qc
    vtools admin --load_snapshot vt_qc
    

<details><summary> Details about this snapshot data </summary>



##### Genotypes

Exome variant sites with higher coverage are extracted from the original VCF files, resulting the `g1000exomesnv.vcf.gz` (411MB) input exome data file. 
 
    #!bin/bash
    chrs='1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X' 
    data\_dir="/home/guest/Data1000g" 
    zcat $data\_dir/ALL.chr1.phase1\_release\_v3.20101123.snps\_indels\_svs.genotypes.vcf.gz | head -500 |grep -        P "^#" | bgzip -c > g1000exomesnv.header.vcf.gz 
    for chr in $chrs
    do 
        echo $chr
        zcat $data_dir/ALL.chr$chr.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz 	  | grep -v -P                  "^#" | grep -P "SNPSOURCE=EXOME" | grep -P "VT=SNP" | bgzip -c > g1000exomesnv_chr$chr.vcf.gz
    done
    fn=\`for i in $chr; do echo g1000exomesnv_chr$i.vcf.gz; done\` zcat g1000exomesnv.header.vcf.gz $fn | bgzip         -c > g1000exomesnv.vcf.gz 



##### Genotype attributes

The VCF file from 1000 genomes project has two genotype attributes, *Genotype dosage from MaCH/Thunder* and *Genotype Likelihoods*. To demonstrate the data QC procedures we need to have additional attributes such as *Genotype Depth* (GD) and *Genotype Quality* (GQ). We randomly simulate GD and GQ scores and append them to each genotype call, which is neither based on genotype dosage nor on genotype likelihoods. These scores will be used in QC for demonstration purposes. 



##### Phenotypes

Two simulated phenotypes *BMI* and *smoking* combined with the original [PED file][3] will be used as phenotype data for this demonstration. 

</details>



#### 1.2 Software

Quality control and association analysis will be performed with *variant association tools* (`vtools update`, `vtools select` and `vtools associate`) with simple annotations from [*variant association tools*][4]. A few other software are occasionally needed for certain tasks along the pipeline. 

<details><summary> Other software</summary>



##### ANNOVAR

We will use the [`ANNOVAR`][5] program to determine which variants should be analyzed in association tests based on their functionality (nonsynonymous, splicing sites, etc). 



##### KING

We will use [`KING`][6] program for phenotype level quality control, i.e., to infer kinship and population structure. [`PLINK`][7] program is needed to convert output to KING compatible format. 



##### R with ggplot2

`vtools report` requires R with ggplot2 in order to produce QQ plot and Manhattan plot. To install it in `R`: 

    install.packages("ggplot2")

</details>



#### 1.3 Computer Environment

Demonstrative analysis for this tutorial are not computationally intensive and can be efficiently carried out in a reasonably powered computer. We have applied similar analysis on ~6,500 whole exome sequencing samples with a total of ~2 million variants and experienced satisfactory performance on a regular Debian GNU/Linux based workstation. 

<details><summary> Read the workstation configurations</summary>



##### CPU

*   product: AMD FX(tm)-8150 Eight-Core Processor 
*   vendor: Advanced Micro Devices [AMD] 
*   size: 3600MHz 
*   capacity: 3600MHz 
*   width: 64 bits 
*   clock: 200MHz 



##### RAM (4X4=16GB)

*   description: DIMM Synchronous 1066 MHz (0.9 ns) 
*   size: 4GiB (each, 16GB total) 
*   width: 64 bits 
*   clock: 1066MHz (0.9ns) 



##### Cache

*   description: L1 cache 
*   size: 384KiB 
*   capacity: 384KiB 
*   clock: 1GHz (1.0ns) 
*   description: L2 cache 
*   size: 8MiB 
*   capacity: 8MiB 
*   clock: 1GHz (1.0ns) 
*   description: L3 cache 
*   size: 8MiB 
*   capacity: 8MiB 
*   clock: 1GHz (1.0ns) 



##### Motherboard

*   product: Crosshair V Formula 
*   vendor: ASUSTeK COMPUTER INC. 



##### Harddrive (2X2TB)

*   product: ST32000641AS 
*   vendor: Seagate 
*   version: CC13 
*   serial: 9WM6ZQJG 
*   size: 1863GiB 

</details>



### 2. Initializing a Project

for convenience and portability of commands, we set `bash` variables: 



    script_dir="./cache"
    data_dir="./data"
    



#### 2.1 Preparing input format configuration file

A "data format configuration file" *.fmt is required to build a project. This mechanism allows importing variants/samples from a number of arbitrary input format. It is always good practice to review and adapt a template fmt file for a specific data-set. We provide a few [FMT templates][8], among which a vcf format template is available. A modified version of the template `vcf.fmt` results in `g1000vcf.fmt`. We created this file by extracting the meta information of the source vcf file and make changes accordingly on the `fmt` template. You should find this file in your project directory if you have loaded our snapshot `vt_qc`. Using this snapshot, you do not need to import any data for this tutorial. However you can modify and use the configuration files for your other projects. 


{{% notice info%}}
`g1000vcf.fmt` is configured such that it will not import variant INFO fields (we will create separated annotation database for it) and genotype likelihood GL field (we will not use it in the analysis) 

{{% /notice %}}

##### Optimize the performance

If you have a large volume of data to import, it is important to set "runtime optimization" parameters to speed up the process. Please read [this documentation][8] for details. 



##### Import from multiple sources

If your dataset is stored in multiple VCF file, please read [this documentation][8] for properly importing such dataset. 



#### 2.2 Creating Annotations

Annotations of variants can be incorporated to the project via 



*   building/using annotation databases (`vtools use`) 

or, 



*   adding annotation fields to variant database (`vtools update`). 

We will demonstrate both approaches. 



##### Annotations from the source VCF file

Two files are required to create annotation database: the source data and the `.ann` configuration file. A number of [ANN templates][9] are provided. To [create customized annotation configuration][10] please refer to the online documentation. 

The snapshot we provided has intentionally left out information in the `INFO` field of the VCF file, which you will find in the file `variants.tsv.gz` in this snapshot, as well as the `g1000.ann` file to build annotation database from the `INFO` field of VCF file. 



    vtools use $script_dir/g1000.ann --file $data_dir/g1000exomesnv.vcf.gz -j8
    



    INFO: Importing annotation data from variants.tsv.gz
    variants.tsv.gz: 100% [================] 142,403 7.8K/s in 00:00:18
    INFO: 291088 records are handled, 0 ignored.
    INFO: Using annotation DB g1000 in project g1000.
    INFO: 1000genome VCF file
    

Available annotation fields can be viewed by either 



    vtools show annotation g1000
    

or 



    vtools show fields
    

<details><summary> which will show all the variant fields in current project.</summary>



    variant.variant_id
    variant.bin
    variant.chr
    variant.pos
    variant.ref
    variant.alt
    g1000.chr                    Chromosome
    g1000.pos                    1-based position
    g1000.dbsnp_id               variant id (rs number or other IDs)
    g1000.ref                    Reference allele, '-' for insertion.
    g1000.alt                    Alternative allele, '-' for deletion.
    g1000.qual                   phred-scaled quality score for the assertion made in
                                 ALT. High QUAL scores indicate high
                                 confidence calls.
    g1000.filter                 PASS if this position has passed all filters, i.e. a
                                 call is made at this position. Otherwise,
                                 if the site has not passed all filters, a
                                 semicolon-separated list of codes for
                                 filters that fail.
    g1000.LDAF                   MLE Allele Frequency Accounting for LD
    g1000.AVGPOST                Average posterior probability from MaCH/Thunder
    g1000.RSQ                    Genotype imputation quality from MaCH/Thunder
    g1000.ERATE                  Per-marker Mutation rate from MaCH/Thunder
    g1000.THETA                  Per-marker Transition rate from MaCH/Thunder
    g1000.CIEND                  Confidence interval around END for imprecise variants
    g1000.CIPOS                  Confidence interval around POS for imprecise variants
    g1000.END                    End position of the variant described in this
                                 record
    g1000.HOMLEN                 Length of base pair identical micro-homology at event
                                 breakpoints
    g1000.HOMSEQ                 Sequence of base pair identical micro-homology at
                                 event breakpoints
    g1000.SVLEN                  Difference in length between REF and ALT alleles
    g1000.SVTYPE                 Type of structural variant
    g1000.AN                     Total Allele Count
    g1000.AC                     Alternate Allele Count
    g1000.AA                     Ancestral Allele, ftp://ftp.1000genomes.ebi.ac.uk/
                                 vol1/ftp/pilot_data/technical/reference/a
                                 ncestral_alignments/README
    g1000.AF                     Global Allele Frequency based on AC/AN
    g1000.AMR_AF                 Allele Frequency for samples from AMR based on AC/AN
    g1000.ASN_AF                 Allele Frequency for samples from ASN based on AC/AN
    g1000.AFR_AF                 Allele Frequency for samples from AFR based on AC/AN
    g1000.EUR_AF                 Allele Frequency for samples from EUR based on AC/AN
    g1000.VT                     indicates what type of variant the line represents
                                 (eg: INDEL, SNP)
    g1000.SNPSOURCE              indicates if a snp was called when analysing the low
                                 coverage or exome alignment data (eg:
                                 EXOME, LOWCOV)
    

</details>



##### `ANNOVAR` Annotations

We want to annotate variants with `ANNOVAR` for variants functionality so that we can focus on functional variants in rare variants association analysis. Although all variants in this dataset should be found in the large collection of readily available annotation databases in `variant annotation tools`, we want to demonstrate here the use of customized text based annotation sources. For readily usable annotation please refer to documentation of [`variant annotation tools`][11]. 

Firstly we output the variants for `ANNOVAR` to annotate: 



    vtools output variant chr pos pos ref alt > $data_dir/exomesnv.txt
    /path/to/annotate_variation.pl $data_dir/exomesnv.txt $data_dir/humandb/ -buildver hg19
    



    NOTICE: The --geneanno operation is set to ON by default
    NOTICE: Reading gene annotation from humandb/hg19_refGene.txt ... Done with 40272 transcripts (including 6670 without coding sequence annotation) for 23416 unique genes
    NOTICE: Reading FASTA sequences from /home/min/HD1s/humandb/hg19_refGeneMrna.fa ... Done with 29603 sequences
    NOTICE: Finished gene-based annotation on 291088 genetic variants in exomesnv.txt
    NOTICE: Output files were written to exomesnv.txt.variant_function, exomesnv.txt.exonic_variant_function
    


{{% notice tip %}}
We use *refGene* hg19 database in `ANNOVAR`, although there are other options (see `ANNOVAR` website for details). 
{{% /notice %}}

Then we import the annotated result into the project database, using two of our template format configurations: 



    vtools update variant --format ANNOVAR_exonic_variant_function \
    	       --from_file $data_dir/exomesnv.txt.exonic_variant_function \
    	       --var_info mut_type function genename
    vtools update variant --format ANNOVAR_variant_function \
    	       --from_file $data_dir/exomesnv.txt.variant_function \
    	       --var_info region_type region_name
    



    INFO: Using primary reference genome hg19 of the project.
    Getting existing variants: 100% [========================] 291,088 385.1K/s in 00:00:00
    INFO: Updating variants from cache/exomesnv.txt.exonic_variant_function (1/1)
    exomesnv.txt.exonic_variant_function: 100% [========================] 184,931 3.5K/s in 00:00:53
    INFO: Fields mut_type, function, genename of 184,931 variants are updated
    INFO: Using primary reference genome hg19 of the project.
    Getting existing variants: 100% [==============================] 291,088 395.1K/s in 00:00:00
    INFO: Updating variants from cache/exomesnv.txt.variant_function (1/1)
    exomesnv.txt.variant_function: 100% [============================] 291,088 5.8K/s in 00:00:50
    INFO: Fields region_type, region_name of 291,088 variants are updated
    


{{% notice tip %}}
`vtools show format ANNOVAR_exonic_variant_function` and `vtools show format ANNOVAR_variant_function` will display details of these configuration formats 
{{% /notice %}}


    vtools show format ANNOVAR_exonic_variant_function
    



    Format:      ANNOVAR_exonic_variant_function
    Description: Output from ANNOVAR, generated from command
      "path/to/annovar/annotate_variation.pl annovar.txt
      path/to/annovar/humandb/". This format imports chr, pos, ref, alt
      and ANNOVAR annotations. For details please refer to
      http://www.openbioinformatics.org/annovar/annovar_gene.html
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr          Chromosome
      pos          1-based position, hg18
      ref          Reference allele, '-' for insertion.
      alt          Alternative allele, '-' for deletion.
    
    Variant info:
      mut_type     the functional consequences of the variant.
    
    Other fields (usable through parameters):
      genename     Gene name (for the first exon if the variant is in more than one
                   exons, but usually the names for all exons are the
                   same).
      function     the gene name, the transcript identifier and the sequence change in
                   the corresponding transcript
    
    Format parameters:
      var_info     Fields to be outputted, can be one or both of mut_type and function.
                   (default: mut_type)
    



    vtools show format ANNOVAR_variant_function
    



    Format:      ANNOVAR_variant_function
    Description: Output from ANNOVAR for files of type "*.variant_function", generated
      from command "path/to/annovar/annotate_variation.pl annovar.txt
      path/to/annovar/humandb/". This format imports chr, pos, ref, alt
      and ANNOVAR annotations. For details please refer to
      http://www.openbioinformatics.org/annovar/annovar_gene.html
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr          Chromosome
      pos          1-based position, hg18
      ref          Reference allele, '-' for insertion.
      alt          Alternative allele, '-' for deletion.
    
    Variant info:
      region_type The genomic region type (i.e., intergenic, ncRNA_intronic, etc) where
                   this variant lies.
    
    Other fields (usable through parameters):
      region_name Genomic region name that corresponds to the region_type. If the
                   variant lies in an intergenic region, this field will
                   specify the closest known regions upstream and
                   downstream of this variant.
    
    Format parameters:
      var_info     Fields to be outputted, can be one or both of region_type and
                   region_name. (default: region_type)
    

A few additioanl fields regarding variant functionality are added to the variant table. They will be useful for selecting, filtering and grouping variants for association analysis. 



    vtools show table variant -l3
    



    variant_id, bin, chr, pos, ref, alt, region_type, region_name
    1, 585, 1, 69536, C, T, exonic, OR4F5
    2, 591, 1, 861275, C, T, intronic, SAMD11
    3, 591, 1, 861315, G, A, UTR5, SAMD11
    (291085 records omitted, use parameter --limit to display more or all records)
    



### 3. Basic Quality Control & Data Preprocessing

Quality control is a crucial yet tedious step in association analysis. To facilitate this step, we provide a variety of summary statistic along with a number of sample/variant selection and filtering operations for quality control purpose. In this section we will demonstrate some basic quality control procedures. Please refer to our [data exploration tutorial][12] for advanced summary statistics and QC measures. 



#### 3.1 Variant & Genotype Level QC

`vtools select` and `vtools exclude` commands implement variant level data selection and filtering. Variants can be subsetted on the basis of criteria defined by variant properties (variant information, annotations, summary statistics, etc) displayed by vtools show fields. We could either focus on subsets of variants of interest or remove non-informative subsets of variants after variants are subsetted. 



##### Low quality variants filter

We have made the `FILTER` column from the original vcf file available as annotation field `g1000.filter`. It can be used directly to remove low quality variants from the database. We select variants of good quality into a separate table, and use this table (instead of using table `variant`) for next steps of analysis. 



    vtools select variant "g1000.filter='PASS'" -t variant_pass
    

An alternative approach would be applying `vtools remove` so that variants of low quality are removed from the variant table. **Note that the remove command is irreversible.** 



    vtools exclude variant "g1000.filter='PASS'" -t variant_to_rm
    vtools remove variants variant_to_rm
    



##### Low quality genotypes filter

Information on genotype calls (displayed in FORMAT column for each variant in VCF files) can be used for quality control of individual genotypes. To list available genotype information fields, 



    vtools show genotypes -l 4
    



    sample_name	filename	num_genotypes	sample_genotype_fields
    HG00096	simulatedQc1000g.tar.gz	291088	GT,DS,GD,GQ
    HG00097	simulatedQc1000g.tar.gz	291088	GT,DS,GD,GQ
    HG00099	simulatedQc1000g.tar.gz	291088	GT,DS,GD,GQ
    HG00100	simulatedQc1000g.tar.gz	291088	GT,DS,GD,GQ
    (1088 records omitted, use parameter --limit to display more or all records)
    

The `GT` and `DS` genotype fields are genotypes and genotype dosage from MaCH/Thunder. Both of them are from the original 1000 genomes project data. `GQ` and `GD` are simulated *genotype quality* and *genotype depth of coverage*. Genotype level filtering can be performed by removing genotype calls of given quality measure, which will **irreversibly** remove genotypes of low coverage and quality: 



    vtools remove genotypes "GD<10 or GQ<20"
    


{{% notice tip %}}
In many cases, however, we do not want to remove genotypes at the early stage of analysis, since we may later decide to change the QC criteria. It is possible to always calculate various statistics conditioning on genotypes defined by expressions such as `GD>10` and `GQ>20`, for example: 
  `vtools update variant --from_stat ... --genotypes <em>GD>10 and GQ>20</em>` 
In this way we obtain statistic over genotype calls *excluding* the low quality genotypes. This approach is more flexible and allows evaluation of the same statistic conditional on different criteria. 
{{% /notice %}}


##### QC statistics conditioned on genotype information

We will demonstrate here the calculation of summary statistics conditioning on genotype information. We set up a genotype condition expression from genotype information fields `GD` and `GQ`. The calculation of various statistic will skip genotypes failing to satisfy this expression, as you can see by comparing the counts of total genotypes and minor allele counts after executing the following commands. 

Statistic without genotype condition constraints: 



    vtools update variant --from_stat 'total=#(GT)' 'num=#(alt)' \
           'het=#(het)' 'hom=#(hom)' 'other=#(other)' \
           'wildtype=#(wtGT)' 'mutants=#(mutGT)' 'missing=#(missing)'
    



    Counting variants: 100% [===================] 1,092 1.5/s in 00:12:08
    INFO: Adding field num
    INFO: Adding field hom
    INFO: Adding field het
    INFO: Adding field other
    INFO: Adding field total
    Updating variant: 100% [=================] 291,088 79.2K/s in 00:00:03
    INFO: 291087 records are updated
    

Statistic with genotype condition constraints: 



    vtools update variant --from_stat 'total_GD10GQ20=#(GT)' 'num_GD10GQ20=#(alt)' \
           'het_GD10GQ20=#(het)' 'hom_GD10GQ20=#(hom)' 'other_GD10GQ20=#(other)' \
           'wildtype_GD10GQ20=#(wtGT)' 'mutants_GD10GQ20=#(mutGT)' 'missing_GD10GQ20=#(missing)\
    '\
           --genotypes "GD>10 and GQ>20"
    



    Counting variants: 100% [================] 1,092 15.2/s in 00:01:11
    INFO: Adding field num_GD10GQ20
    INFO: Adding field hom_GD10GQ20
    INFO: Adding field het_GD10GQ20
    INFO: Adding field other_GD10GQ20
    INFO: Adding field total_GD10GQ20
    Updating variant: 100% [======================] 290,999 79.1K/s in 00:00:03
    Updating missing variants in variant: 100% [=======================] 89 60.6K/s in 00:00:00
    

Compare the statistic from original data vs. statistic conditional on genotype info scores: 



    vtools output variant chr pos ref alt total total_GD10GQ20 num num_GD10GQ20 missing missing\
    _GD10GQ20 -l4 --header
    



    chr     pos     ref     alt     total   total_GD10GQ20  num     num_GD10GQ20    missing missing_GD10GQ20
    1       69536   C       T       1092    1088    0       0       0       4
    1       861275  C       T       1092    1091    1       1       0       1
    1       861315  G       A       1092    1091    2       2       0       1
    1       865488  A       G       1092    1092    1       1       0       0
    

Looking at the first variant "1:69536" we see the original total count is 1092 genotype calls; after conditioning on *GD>10 and GQ>20*, 4 genotype calls are skipped, resulting in 1088 counts. If all genotype calls in a variant site fail the genotype quality constraint, the total count will be zero. These variants are: 



    vtools select variant "total_GD10GQ20 == 0" -o chr pos ref alt
    



    1       10719967        C       T
    1       11199698        T       C
    1       11210331        C       T
    1       40432550        C       T
    1       44057597        C       T
    1       44063508        C       T
    1       203452763       G       A
    1       212506861       C       T
    1       212506964       G       A
    1       212530649       G       A
    ...
    

A more informative use of the statistic would be for example a ratio of the two total fields: 



    vtools update variant --set "missing_ratio = missing_GD10GQ20/(total * 1.0)"
    



    chr	pos	ref	alt	missing_ratio
    1       69536   C       T       0.003663003663
    1       861275  C       T       0.000915750915751
    1       861315  G       A       0.000915750915751
    1       865488  A       G       0.0
    1       865545  G       A       0.0
    ...
    

This calculates the proportion of genotypes having **low quality scores per variant**. Such variant level statistics can be useful in creating customized variant level quality control criteria. 

The statistics calculated above are for demonstration only and will not be used in our next analysis steps. We will not pursue any QC related summary statistic calculations for now, since groups of samples have to be defined before statistics of subset of samples can be calculated (e.g., population specific minor allele frequency). In the next section we will demonstrate manipulation of sample information. 



#### 3.2 Processing Phenotype / Sample Level Information

We discuss in this section the organization and use of sample phenotype information. This snapshot provides a phenotype file that we can load phenotype data from: 



    vtools phenotype --from_file $data_dir/g1000_simulated_phenotypes.txt
    



    INFO: Adding field Family_ID
    INFO: Adding field Paternal_ID
    INFO: Adding field Maternal_ID
    INFO: Adding field Gender
    INFO: Adding field Population
    INFO: Adding field BMI
    INFO: Adding field smoking
    INFO: 7 field (7 new, 0 existing) phenotypes of 1092 samples are updated.
    

To view the phenotypes available, 



    vtools show samples -l10
    



    sample_name	filename	Family_ID	Paternal_ID	Maternal_ID	Gender	Population	BMI	smoking
    HG00096 simulatedQc1000g.vcf.gz HG00096 0 0 1 GBR 23.04 0
    HG00097 simulatedQc1000g.vcf.gz HG00097 0 0 2 GBR 37.09 0
    HG00099 simulatedQc1000g.vcf.gz HG00099 0 0 2 GBR 28.87 0
    HG00100 simulatedQc1000g.vcf.gz HG00100 0 0 2 GBR 24.12 1
    HG00101 simulatedQc1000g.vcf.gz HG00101 0 0 1 GBR 27.72 0
    

To view specific phenotypes, 



    vtools phenotype --output sample_name Population BMI smoking
    



    HG00096	GBR	23.04	0
    HG00097	GBR	37.09	0
    HG00099	GBR	28.87	0
    HG00100	GBR	24.12	1
    HG00101	GBR	27.72	0
    HG00102	GBR	27.41	0
    



##### Creating sample information columns based on sample genotypes

Individual level genotype summary can be generated and appended to the sample information table. For example we want to calculate the number of alternative alleles per individual: 



    vtools phenotype --from_stat "allele_counts=#(alt)" -j8
    



    Calculating phenotype: 100% [==================] 1,092 90.9/s in 00:00:12
    INFO: 1092 values of 1 phenotypes (1 new, 0 existing) of 1092 samples are updated.
    

Similar to variant level genotype summary, genotype information condition can be applied, for example: 



    vtools phenotype --from_stat "allele_counts_GD10GQ20=#(alt)" --genotypes 'GD>10 and GQ>20' \
    -j8
    

Two additional sample information fields `allele_counts` and `allele_counts_ds` are added to the database. 



    vtools phenotype --output sample_name allele_counts allele_counts_GD10GQ20 -l 3 --header
    



    sample_name	allele_counts	allele_counts_GD10GQ20
    HG00096	1232	1182
    HG00097	1317	1263
    HG00099	1431	1363
    


{{% notice tip %}}
Sample information thus created can be useful in individual genotype level quality control. For example, we may want to remove sample having too many low quality or missing genotype calls from the analysis (`vtools remove samples`). Advanced use of phenotype `--from_stat` command include calculating sample level **'transition-transversion ratio**', or **'synonymous-nonsynonymous SNV ratio**", see this [tutorial]. 
{{% /notice%}}

##### Creating *phenotypes* based on existing sample information

`vtools phenotype --set` accepts arithmetic operations on existing columns, producing new useful sample information, or *phenotypes*. For example, 



    vtools phenotype --set "ds_proportion=allele_counts_ds / (allele_counts * 1.0)"
    

Or, to create a new phenotype `BMI_bin` on the basis of existing phenotypes (note the use of `--samples` condition): 



    vtools phenotype --set "BMI_bin=1" --samples "BMI>25"
    vtools phenotype --set "BMI_bin=0" --samples "BMI<=25"
    



    INFO: 590 values of 1 phenotypes (1 new, 0 existing) of 590 samples are updated.
    INFO: 502 values of 1 phenotypes (0 new, 1 existing) of 502 samples are updated.
    

In later sections we will demonstrate the association analysis using both the quantitative trait `BMI` and the binary trait `BMI_bin`. 



##### Updating sample information for association testing

There are 14 different population groups in our data-set 



    vtools phenotype --output Population | sort -u | wc -l # 14
    

also there are a few related individuals 



    vtools phenotype --output sample_name Paternal_ID Maternal_ID \
           --samples "Maternal_ID != 0 or Paternal_ID != 0"
    



    HG00155	0	HG00144
    NA07048	NA07034	NA07055
    NA10847	NA12146	NA12239
    NA10851	NA12056	NA12057
    NA19129	NA19128	NA19127
    NA19434	0	NA19432
    NA19444	0	NA19432
    NA19469	0	NA19470
    NA19675	NA19679	NA19678
    NA19685	NA19661	NA19660
    

We choose to group and analyze some unrelated European populations (CEU, BGR and TSI) in association tests. Firstly we define a new phenotype `Unrelated_Europeans`: 



    vtools phenotype --set "Unrelated_Europeans='yes'" \
           --samples "Population in ('CEU', 'GBR', 'TSI') and Maternal_ID == 0 and Paternal_ID \
    == 0"
    vtools phenotype --set "Unrelated_Europeans='no'" \
           --samples "Population not in ('CEU', 'GBR', 'TSI') or Maternal_ID != 0 or Paternal_I\
    D != 0"
    



    INFO: Adding field Unrelated_Europeans
    INFO: 268 values of 1 phenotypes (1 new, 0 existing) of 268 samples are updated.
    INFO: 824 values of 1 phenotypes (0 new, 1 existing) of 824 samples are updated.
    

There are 268 samples having a *yes* tag for being unrelated Europeans. Within these European samples, there are population substructures which we would want to control for by incorporating **principle components** (PC) from MDS analysis as covariates. We calculated the PC for the 268 samples using the `KING` program, and import the output into the database: 



    vtools phenotype --from_file $data_dir/European_PC.txt
    



    INFO: Adding field PC1
    INFO: Adding field PC2
    INFO: 3 field (2 new, 1 existing) phenotypes of 268 samples are updated.
    


{{% notice info %}}
Population structure determination and selection of unrelated samples is very important in exome association analysis. Even though the 1000 genomes data comes with self-reported kinship and population information, it is still necessary to conduct population structure and kinship analysis. One can use the same technique as has been applied in GWAS studies. 
{{% /notice %}}


#### 3.3 Variant and Sample Selection for Association Analysis

##### Alternative allele frequency calculations

We calculate AF within the 268 European samples, by first calculate total genotypes and number of alternative alleles, then calculate AF from them. 



    vtools update variant --from_stat 'total_ie=#(GT)' 'num_ie=#(alt)' 'het_ie=#(het)' \
    	       'hom_ie=#(hom)' 'other_ie=#(other)' --samples "Unrelated_Europeans='yes'" \\
    
                   --genotypes "GD>10 and GQ>20"
    vtools update variant --set 'af_ie=num_ie/(total_ie * 2.0)'
    

Notice that 



*   As was previously discussed, genotype conditions `--genotypes` can be applied with specified criteria. 
*   Several other fields `num_ie, het_ie, hom_ie, other_ie` are calculated and will be used in HWE analysis. 



Allele frequency thus calculated af=num/(total * 2.0) will be wrong for variants on X chromosome if males present in samples. Correct allele frequency can be calculated using more involved vtools update command, which we will not demonstrate here. 

A new allele frequency field is added to the database. We can look at variants having non-trivial `af_ie` field and compare it with the allele frequency estimate based on the entire data-set 



    vtools select variant "af_ie>0" -o chr pos ref alt g1000.AF af_ie -l5
    



    1	874551	G	A	0.0005	0.0018656716417910447
    1	874706	A	G	0.0005	0.0018656716417910447
    1	878709	C	T	0.0014	0.0018656716417910447
    1	878712	C	T	0.0015	0.0018656716417910447
    1	878744	G	C	0.0057	0.0018656716417910447
    

Note that all the 5 variants displayed above are singletons ({$MAF=\frac{1}{268\times2}$}). We can explore the variants distribution in the 268 samples using `select` commands 

<details><summary> variant counts by type</summary>

arr=(\`vtools select variant -c -v0\`) arr+=(\`vtools select variant "af\_ie>0" -c -v0\`) for i in 1 2 3 do arr+=(\`vtools select variant "num\_ie=$i" -c -v0\`) done echo ${arr[1]} "out of a total of" ${arr[0]} "variants are selected in our sample, among which" ${arr[2]} "are singletons," ${arr[3]} "are doubletons and" ${arr[4]} "are tripletons".

</details>

The output says: **60896 out of a total of 291088 variants are selected in our sample, among which 49813 are singletons, 5663 are doubletons and 1546 are tripletons.** 



##### HWE filter

Exact Test of Hardy-Weinberg Equilibrium is implemented as in Wigginton et al (2005)[^J WIGGINTON, D CUTLER and G ABECASIS (2005) **A Note on Exact Tests of Hardy-Weinberg Equilibrium**. *The American Journal of Human Genetics* doi:`10.1086/429864`. <http://linkinghub.elsevier.com/retrieve/pii/S0002929707607356>^] to detect and filter out variants deviating from HWE. 



    vtools update variant --set "hwe=HWE_exact(num_ie, het_ie, hom_ie, other_ie)"
    

An `hwe` field is created with *p-values* from the HWE test. We want to filter out variant sites with {$HWE<5\times10^{-8}$}, which is 1132 variants. It turns out most of these variants have MAF greater than 0.01. 



    vtools select variant 'hwe<5e-8' -c
    



##### Creating common and rare variant subsets

Unlike traditional GWAS analysis, exome association analysis will study both common variants (variants having relatively high minor allele frequency) and rare variants (variants having relatively low minor allele frequency). Statistical methods for analyzing common and rare variants are different. It is thus necessary to subset variants based on minor allele frequency. We define common variants as having MAF greater than 1%, and rare variants MAF smaller than 1%. 



    vtools select variant "af_ie>=0.01 and af_ie<=0.99 and hwe>=5e-8" \
    	       -t common_var "common variants for the 268 unrelated European samples, hwe \
    and quality pass"
    vtools select variant "((af_ie<0.01 and af_ie>0.0) or (af_ie>0.99 and af_ie<1.0)) and hwe>=\
    5e-8" \
    	       -t rare_var "rare variants for the 268 unrelated European samples, hwe and \
    quality pass"
    vtools show tables
    



    table                 #variants     date  message
    variant                 291,088
    common_var                1,711    Jul10  common variants for the 268 unrelated European samples,
    			  			hwe and quality pass
    rare_var                 58,053    Jul10  rare variants for the 268 unrelated European samples,
    			  			hwe and quality pass
    



The 1% cutoff for rare/common variants is arbitrary. For this small demonstration data-set (60k variants, 268 individuals) using 1% cut off we have 58062 rare variants and 2825 common variants. Alternatively, for single variant association tests (common variants analysis) one could analyze all variants except for singletons and doubletons regardless of their MAF classification; for aggregated variants analysis (rare variants analysis) one may want to use other MAF cutoffs depending on the available sample size, and particularly, for *variable thresholds* or *RareCover* methods, the cutoff should be higher (say, 5%). 



##### Selecting functional rare variants

Rare variants analysis typically focus only on variants that effect protein function. We have already annotated the variants with `ANNOVAR`. The annotation fields can be used to select functional rare variants for association studies. 



    vtools select rare_var "mut_type like 'nonsynonymous%'" \
    	       -t rare_nonsyn "nonsynonymous variants selected from table rare_var"
    vtools select rare_var "mut_type like 'nonsynonymous%' OR mut_type like 'stoploss%' OR mut_\
    type like 'stopgain%' OR mut_type like 'splicing%'" \
    	       -t rare_fvar "nonsynonymous, stoploss, stopgain and splicing variants selec\
    ted from table rare_var"
    vtools show tables
    



    rare_nonsyn              23,207    Jul10  nonsynonymous variants selected from table rare_var
    rare_fvar                23,757    Jul10  nonsynonymous, stoploss, stopgain and splicing variants
    						selected from table rare_var
    



##### Summary

We originally have a total of 291,088 variants. After 



*   Restricting the variants to only 268 selected samples 
*   Filtering for low variants/genotypes quality 
*   Filtering for HWE 
*   Sub-setting into common/rare variants 
*   Filtering rare variants by functionality 

we end up having 1,711 common variants and 23,757 rare variants for association analysis. 



#### 3.4 Additional QC for Missing Data

Although there is no missing genotype calls in our test data (or, missing genotype calls have already being imputed), in practice it is not always the case. In addition to missing calls, low quality genotypes will be regarded missing in effect. As has already been discussed, we can use `--genotypes` conditions to skip low quality genotypes. The overall missingness of data per variant can be evaluated on both variant level and individual level. 



##### Variant level missingness

    vtools update variant --from_stat "mnum=#(missing)" --genotypes CONDITION
    vtools update variant --set "missing_ratio = mnum/(N * 1.0)"
    

where {$N$} is the total sample size. 



##### Individual level missingness

    vtools phenotype --from_stat "num=#(missing)" --genotypes CONDITION
    vtools phenotype --set "missing_ratio = mnum/(M * 1.0)"
    

where {$M$} is the total number of variant sites. 



##### Group specific filtering of missing data for rare variant association analysis

After the variant/sample information field `missing_ratio` is calculated, an overall variant/sample level filtering can be performed. However we do not recommend the overall filtering for rare variant association analysis. In practice the distribution of missing genotype calls are not uniform. Some samples may not have data on a particular genetic region while other samples have (due to different exome capture arrays). To fully exploit the data we will filter variants and samples for missing data specific to each small genomic unit while carrying out association tests, as will be introduced in the next section of this tutorial. 


 [1]: ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/release/20110521/
 [2]: ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/exome_pull_down_targets/
 [3]: ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/supporting/phase1_samples_integrated_20101123.ped
 [4]:    /documentation/tutorials/association/
 [5]: http://www.openbioinformatics.org/annovar/
 [6]: http://people.virginia.edu/~wc9c/KING/
 [7]: http://pngu.mgh.harvard.edu/~purcell/plink
 [8]:    /documentation/vtools_commands/import/
 [9]:   /applications/annotation/
 [10]:   /applications/annotation/customized/
 [11]:    /documentation/tutorials/annotation/
 [12]:   /applications/association/qc/
