+++
title = "Import"
weight = 2
+++

## Import variants, genotypes and related information fields 


### 1. Usage

    % vtools import -h
    
    usage: vtools import [-h] [--build BUILD] [--format FORMAT]
                         [--sample_name [SAMPLE_NAME [SAMPLE_NAME ...]]] [-f]
                         [-j N] [-v {0,1,2}]
                         input_files [input_files ...]
    x
    Import variants and related sample genotype from one or more delimiter
    separated files (e.g. VCF and a number of indel formats).
    
    positional arguments:
      input_files           A list of failes that will be imported. The file should
                            be delimiter separated with format described by
                            parameter --format. Gzipped files are acceptable. If a
                            preprocessor is defined in the format, input files
                            will be processed by the preprocessor before they are
                            imported.
    
    optional arguments:
      -h, --help            show this help message and exit
      --build BUILD         Build version of the reference genome (e.g. hg18) of
                            the input data. If unspecified, it is assumed to be
                            the primary reference genome of the project. If a
                            reference genome that is different from the primary
                            reference genome of the project is specified, it will
                            become the alternative reference genome of the
                            project. The UCSC liftover tool will be automatically
                            called to map input coordinates between the primary
                            and alternative reference genomes. If you are
                            uncertain about the reference genome used in the data,
                            use a recent standard reference genome (e.g. hg19) and
                            validate it after the data is imported (c.f. "vtools
                            admin --validate_build").
      --format FORMAT       Format of the input text file. It can be one of the
                            variant tools supported file types such as VCF (cf.
                            'vtools show formats'), or a local format
                            specification file (with extension .fmt). If
                            unspecified, variant tools will try to guess format
                            from file extension. Some file formats accept
                            parameters (cf. 'vtools show format FMT') and allow
                            you to import additional or alternative fields defined
                            for the format.
      --sample_name [SAMPLE_NAME [SAMPLE_NAME ...]]
                            Name of the samples imported by the input files. The
                            same names will be used for all files if multiple
                            files are imported. If unspecified, headers of the
                            genotype columns of the last comment line (line starts
                            with #) of the input files will be used (and thus
                            allow different sample names for input files). If
                            sample names are specified for input files without
                            genotype, samples will be created without genotype. If
                            sample names cannot be determined from input file and
                            their is no ambiguity (only one sample is imported), a
                            sample with NULL sample name will be created.
      -f, --force           Import files even if the files have been imported
                            before. This option can be used to import from updated
                            file or continue disrupted import, but will not remove
                            wrongfully imported variants from the master variant
                            table.
      -j N, --jobs N        Number of processes to import input file. Variant
                            tools by default uses four processes to import
                            variants and samples genotypes in parallel, and you
                            can use more or less processes by adjusting this
                            parameter. Due to the overhead of inter-process
                            communication, more jobs do not automatically lead to
                            better performance.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).

    
### 2. Importing VCF files

VCF is the most commonly used format to store genetic variants and sample genotypes from next-gen sequencing studies. *variant tools* can import data from plain (`.vcf`) or compressed (`.vcf.gz`) vcf format (version 4.0 or higher). Depending on the number of samples a vcf file stores, *variant tools* can import only variants (even if the vcf file contains sample genotypes, see an example below), import variants with a sample without genotype, and import all samples in a vcf file using specified sample names or sample names obtained from the meta information (see examples above). A limitation is that *variant tools* ignores phase information of genotypes. 

##### Import variant and genotype info fields

The vcf format can store arbitary variant and genotype information fields. *variant tools* by default does not import any variant and info fields. However, you may specified the fields you'd like to import using option `--var_info` for variant fields and `--geno_info` for genotype fields. To import variant or genotype fields from a vcf file, you need to 

1.  know what fields are available from the input vcf file. That is to say, you need to open a file, read its header, and determine what fields are provided. 
2.  In the current version, genotype fields `DP`,`GQ`,`GD`,`HQ`,`AD`,`PL`,`MQ`,`NS` are supported. 
3.  use command `vtools import input_file.vcf --var_info var_fields --geno_info geno_fields` to import variants, genotypes and related fields. 


{{% notice tip %}}

 If your vcf file is bgzipped and tabix indexed (you can run compress and index your vcf file using commands `bgzip` and `tabix`), you can use command `vtools show track FILENAME.vcf.gz` to get details of the vcf file. The [`track`][5] function can also be used to retrieve such information when needed so you do not have to import variant info fields into the project. 
 {{% /notice %}}

 {{% notice tip %}}
 If your vcf file contains novel variant and/or geno info fields, or if you would like to import all variant and genotype info fields into the project, you can create a customized `.fmt` file to import these. This process can be simplified using pipeline import_vcf. The command to use is similar to `vtools execute import_vcf --input my_file.vcf --output myvcf.fmt --build hg19`.

{{% /notice %}}


<details><summary>Examples:create a project and load some sample data</summary>
 
Let us first create a project and download a sample project with a bunch of test datasets: 

    % vtools init import --parent vt_testData_v3
    
    
{{% notice tip %}}
You can use command `vtools show snapshots` to get a list of available snapshots 
{{% /notice %}}


</details>

<details><summary>Examples: importing variant and genotype info fields</summary>
If we have a look at the header of `CEU.vcf.gz`, we can see 

    % gzcat CEU_hg38.vcf | head -15

    ##fileformat=VCFv4.0
    ##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
    ##INFO=<ID=HM2,Number=0,Type=Flag,Description="HapMap2 membership">
    ##INFO=<ID=HM3,Number=0,Type=Flag,Description="HapMap3 membership">
    ##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele, ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/pilot_data/technical/reference/ancestral_alignments/README">
    ##reference=human_b36_both.fasta
    ##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
    ##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
    ##FORMAT=<ID=CB,Number=1,Type=String,Description="Called by S(Sanger), M(UMich), B(BI)">
    ##rsIDs=dbSNP b129 mapped to NCBI 36.3, August 10, 2009
    ##INFO=<ID=AC,Number=.,Type=Integer,Description="Allele count in genotypes">
    ##INFO=<ID=AN,Number=1,Type=Integer,Description="Total number of alleles in called genotypes">
    #CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  NA06985 NA06986 NA06994 NA07000 NA07037 NA07051 NA07346 NA07347 NA07357 NA10847 NA10851 NA11829 NA11830 NA11831 NA11832 NA11840 NA11881 NA11894 NA11918 NA11919 NA11920 NA11931 NA11992 NA11993 NA11994 NA11995 NA12003 NA12004 NA12005 NA12006 NA12043 NA12044 NA12045 NA12144 NA12154 NA12155 NA12156 NA12234 NA12249 NA12287 NA12414 NA12489 NA12716 NA12717 NA12749 NA12750 NA12751 NA12760 NA12761 NA12762 NA12763 NA12776 NA12812 NA12813 NA12814 NA12815 NA12828 NA12872 NA12873 NA12874
    1       10533   .       G       C       .       PASS    AA=.;AC=6;AN=120;DP=423  GT:DP:CB        0|0:6:SMB       0|0:14:SMB      0|0:4:SMB       0|0:3:SMB       0|0:7:SMB       0|0:4:SMB       1|0:6:MB        0|0:3:SMB       0|0:13:SMB      0|0:1:SMB       0|0:14:SMB      0|0:10:SMB      0|0:6:SB        0|0:2:SMB       0|0:6:SMB       0|0:4:SMB       0|0:2:SMB       0|0:15:SMB      0|0:2:SMB       0|0:1:SMB       0|0:26:SMB      0|0:6:SMB       0|1:14:MB       0|0:5:SMB       0|0:3:SMB       0|0:20:SMB      0|0:3:SMB       0|0:2:SMB       0|0:4:SMB       0|0:12:SMB      0|0:1:SMB       0|0:7:SMB       0|0:2:SMB       0|0:25:SMB      0|0:9:SMB       0|1:1:MB        0|0:9:SMB       0|0:1:SMB       0|0:6:SMB       0|0:12:SMB      0|0:7:SMB       0|0:18:SMB      0|0:2:SMB       0|0:2:SM        0|0:38:SMB      0|0:3:SM        0|0:3:SMB       0|0:5:SMB       0|0:5:SMB       0|0:3:SMB       0|0:0:MB        0|0:5:SMB       0|0:7:SMB       0|0:0:SMB       0|0:6:SMB       1|0:5:SMB       0|0:4:MB        0|0:5:SMB       1|0:5:MB        0|1:9:SMB


we can see that this file contains genotype info `AA`, `AC`, `AN`, and `DP`, and genotype info `DP` and `CB`. 

    % vtools init import -f
    % vtools import CEU_hg38.vcf --build hg38 --var_info AA AC AN DP --geno_info DP
    
    INFO: Importing variants from CEU_hg38.vcf (1/1)
    CEU_hg38.vcf: 100% [======================================] 306 10.6K/s in 00:00:00
    INFO: 292 new variants (292 SNVs) from 306 lines are imported.
    Importing genotypes: 100% [===============================] 292 2.7K/s in 00:00:00

    

The imported data now has variant info field `AA`, `AC`, `AN`, and `DP`, 

    % vtools show fields
    
    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    variant.AA (char)
    variant.AC (int)
    variant.AN (int)
    variant.DP (int)
    
and genotype info field DP 

    % vtools show genotypes -l 5

    sample_name filename        num_genotypes   sample_genotype_fields
    NA06985     CEU_hg38.vcf    292             DP,GT
    NA06986     CEU_hg38.vcf    292             DP,GT
    NA06994     CEU_hg38.vcf    292             DP,GT
    NA07000     CEU_hg38.vcf    292             DP,GT
    NA07037     CEU_hg38.vcf    292             DP,GT
    (55 records omitted)
    
</details>

In above example, `DP` appears in both `INFO` and genotype columns of the input vcf file. Since `DP` could be listed in `INFO` field to record the total depth of the genotype of all samples in the vcf file. 



Here is another example importing multiple VCF files:

<details><summary>Examples: import multiple VCF files</summary>
If we have a look at the meta information of `V1.vcf`, 

    % head -14 V1_hg38.vcf

    ##fileformat=VCFv4.0
    ##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of Samples With Data">
    ##INFO=<ID=DP,Number=1,Type=Integer,Description="Total Depth">
    ##INFO=<ID=AF,Number=.,Type=Float,Description="Allele Frequency">
    ##INFO=<ID=AA,Number=1,Type=String,Description="Ancestral Allele">
    ##INFO=<ID=DB,Number=0,Type=Flag,Description="dbSNP membership, build 129">
    ##INFO=<ID=H2,Number=0,Type=Flag,Description="HapMap2 membership">
    ##FILTER=<ID=q10,Description="Quality below 10">
    ##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
    ##FORMAT=<ID=GQ,Number=1,Type=Integer,Description="Genotype Quality">
    ##FORMAT=<ID=DP,Number=1,Type=Integer,Description="Read Depth">
    ##FORMAT=<ID=HQ,Number=2,Type=Integer,Description="Haplotype Quality">
    ##INFO=<ID=REMAP_ALIGN,Number=1,Type=String,Description="Alignment type used for remapping (FP=first pass, SP=second pass)">
    #CHROM  POS ID  REF ALT QUAL    FILTER  INFO    FORMAT  SAMP1
    1   14677   .   G   A   32  PASS    DP=6;NS=1;REMAP_ALIGN=FP    GT  0/1
    

`DP` is listed as a INFO field, along with `NS`, we can import `V1_hg38.vcf`, `V2_hg38.vcf` and `V3_hg38.vcf` using command 



    % vtools init import -f
    % vtools import V*_hg38.vcf --build hg38 --geno_info DP NS
    
    INFO: Importing variants from V1_hg38.vcf (1/3)
    V1_hg38.vcf: 100% [==================================] 1,619 5.0K/s in 00:00:00
    INFO: 1,273 new variants (1,273 SNVs, 332 unsupported) from 1,619 lines are imported.
    Importing genotypes: 100% [==========================] 1,273 9.6K/s in 00:00:00
    INFO: Importing variants from V2_hg38.vcf (2/3)
    V2_hg38.vcf: 100% [==================================] 1,601 5.2K/s in 00:00:00
    INFO: 449 new variants (1,258 SNVs, 329 unsupported) from 1,599 lines are imported.
    Importing genotypes: 100% [==========================] 1,722 14.3K/s in 00:00:00
    INFO: Importing variants from V3_hg38.vcf (3/3)
    V3_hg38.vcf: 100% [==================================] 1,589 5.3K/s in 00:00:00
    INFO: 329 new variants (1,274 SNVs, 301 unsupported) from 1,589 lines are imported.
    Importing genotypes: 100% [==========================] 2,051 17.1K/s in 00:00:00
    


`DP` and `NS` will be imported as genotype info for each genotype, 

    % vtools show fields

    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)

    % vtools show genotypes
    
    sample_name filename    num_genotypes   sample_genotype_fields
    SAMP1       V1_hg38.vcf 1273            DP,GT,NS
    SAMP2       V2_hg38.vcf 1258            DP,GT,NS
    SAMP3       V3_hg38.vcf 1274            DP,GT,NS
    
If you need total depth, you can obtained from the corresponding genotype field 

    % vtools update variant --from_stat 'DP=sum(DP)' 'NS=sum(NS)'
    
    INFO: Adding variant info field DP with type INT
    INFO: Adding variant info field NS with type INT
    Updating variant: 100% [================================] 2,051 49.1K/s in 00:00:00
    INFO: 2051 records are updated

Here `DP=sum(DP)` looks strange but the first `DP` is a new variant info and the second `DP` is the existing genotype info. Now, variant info field `DP` stands for total depth and `NS` stands for number of times a variant shows up in the samples. 

    % vtools output variant chr pos ref alt DP NS -l 5
    
    1   14677   G   A   15  2
    1   15820   G   T   7   1
    1   16103   T   G   76  3
    1   16378   T   C   41  2
    1   20129   C   T   24  2
    

</details>

##### Using customized or alternative fields to import genotypes

The vcf format accepts a number of parameters to customize the way how genotypes are imported. For example, the `--geno` option accepts a genotype field. The default `GT` field import all genotypes assuming that `GT` is the first field in the genotype columns. However, 

*   You can use option `--geno` without value to specify an empty genotype field so that variant tools will not process any genotype. 
*   In `vcf.fmt` we import wild-type genotypes as numeric value 0. This is important for the purpose of association studies. If you are only interested in exploring variants of your sample, and you do not care to discriminate wild-type genotypes from missing genotype calls, you may set `--wildtype_value None`, which will leave out all wild-type genotypes, resulting in much quicker import and smaller database size. 
*   The `GT` field assumes that `GT` is the first field in the `FORMAT` column. However, some variant-calling software produce non-standard vcf files that do not follow this standard. In this case, an alternative field `safe_GT` can be used (e.g. `--geno safe_GT`) to import genotypes according to the location of `GT` in the `FORMAT` string. 

<details><summary>Ignore genotypes of input vcf file</summary>

    % vtools init import -f
    % vtools import CEU_hg38.vcf --build hg38 --var_info AA AC AN DP --geno

    INFO: Importing variants from CEU_hg38.vcf (1/1)
    CEU_hg38.vcf: 100% [======================================] 306 13.1K/s in 00:00:00
    INFO: 292 new variants (292 SNVs) from 306 lines are imported.

With this command, no genotype is imported 

    % vtools show genotypes     

    sample_name filename    num_genotypes   sample_genotype_fields
    
</details>


##### Using a customized format file to import additional fields (This function is only supoorted when STOREMODE is set to sqlite.)

If you have a field that you would like to import, but does not exist in `vcf.fmt`, you can add it to a customized format file and use this format file to import the data. 

<details><summary>Examples: Using a customized .fmt file to import additional fields</summary>
For example, the `CB` genotype field is commonly used and is not defined in `vcf.fmt`, according to the meta information, this field is a string. You can then copy `~/.variant_tools/format/vcf.fmt` as `my_vcf.fmt` and add 

    [CB_geno]
    index=9, 10:
    adj=FieldFromFormat('CB', ':')
    type=VARCHAR(3)
    comment=Called by S(Sanger), M(UMich), B(BI)

at the end of this file, and import this field using 

    % vtools init import -f
    % export STOREMODE="sqlite"
    % vtools import CEU_hg38.vcf --format my_vcf.fmt --build hg38 --var_info AA AC AN DP --geno_info DP_geno CB_geno

    INFO: Importing variants from CEU.vcf.gz (1/1)
    CEU.vcf.gz: 100% [====================================================] 300 12.4K/s in 00:00:00
    INFO: 288 new variants (288 SNVs) from 300 lines are imported.
    Importing genotypes: 100% [=========================================] 18,000 9.0K/s in 00:00:02
    Copying genotype: 100% [==============================================] 60 484.0K/s in 00:00:00

    % vtools show genotypes -l5
    
    sample_name filename    num_genotypes   sample_genotype_fields
    NA06985 CEU.vcf.gz  287 GT,DP_geno,CB_geno
    NA06986 CEU.vcf.gz  287 GT,DP_geno,CB_geno
    NA06994 CEU.vcf.gz  287 GT,DP_geno,CB_geno
    NA07000 CEU.vcf.gz  287 GT,DP_geno,CB_geno
    NA07037 CEU.vcf.gz  287 GT,DP_geno,CB_geno
    (55 records omitted)

</details>






### 3. General usages and options

Command `` vtools import `` imports variants, sample genotypes and related information fields from formats other than VCF as well. The imported variants are saved to the master variant table `variant` of the project, along with their information fields. 

{{% notice tip %}}
Variant tools can import SNVs, Indels and complex variants with reference and alternative alleles explicitly listed in the source files. It cannot yet handle structural variants such as large indels listed in vcf file as `<INS>` or `DUP:TANDEM>`. For details about how different types of variants are imported into *variant tools*, please refer to [here]([1]).
{{% /notice %}}

{{% notice tip %}}
It is sometimes useful to import only variants to a project. The variant info could be added later using command [`vtools update`](Documentation/vtools Commands/update.md), or built into an annotation database to reduce the size of the project. 
{{% /notice %}}


#### 3.1 File formats and format specification files (.fmt) (option `--format`)

`` vtools import `` can handle input file in many different formats (e.g. `.vcf`) and their gzipped or bzipped versions (e.g. `.vcf.gz`). variant tools relies on [format specification files](Documentation/Customization/Format/_index.md)  to describe a file format. These files (with extension `.fmt`) tell variant tools how to read from an input file. They are available online and will be downloaded automatically to the local resource directory of variant tools. Please refer to the variant tools [input file format](Documentation/Customization/Format/supportedformats/_index.md) for a list of supported formats, or use command `vtools show formats` to get a list of formats, and `vtools show format FMT` for details of a format. 

A format specification file defines how to import variants (fields `chr`, `pos`, `ref`, and `alt`), variant info fields, genotypes, and genotype infor fields from input files. It basically tells command `vtools import` what fields are available from input file, from which column each field should be read, how to post-process input (e.g convert 0-based positions to 1-based), and how to store the data (data type). 


{{% notice tip %}}
Although variants consists of chromosome, position, reference and alternative alleles, your input does not have to contain all such information. For example, using format `rsname`, variant tools can import variants from a list of dbSNP IDs. 
{{% /notice %}}

<details><summary>Examples: Show supported file formats and details of a format</summary>

Command `vtools show formats` lists all supported file formats with a short description. 

    % vtools show formats
    
    INFO: Upgrading variant tools project to version 2.7.20
    ANNOVAR                 Input format of ANNOVAR. No genotype is defined.
    ANNOVAR_exonic_variant_function Output from ANNOVAR for files of type *exonic_variant_function, generated
                            from command "path/to/annovar/annotate_variation.pl annovar.txt
                            path/to/annovar/humandb/". This format imports chr, pos, ref, alt and ANNOVAR
                            annotations. For details please refer to
                            http://www.openbioinformatics.org/annovar/annovar_gene.html
    ANNOVAR_output          Output from ANNOVAR, generated from command "path/to/annovar/annotate_variation.pl
                            annovar.txt path/to/annovar/humandb/". This format imports chr, pos, ref, alt and
                            ANNOVAR annotations. For details please refer to
                            http://www.openbioinformatics.org/annovar/annovar_gene.html
    ANNOVAR_variant_function Output from ANNOVAR for files of type "*.variant_function", generated from command
                            "path/to/annovar/annotate_variation.pl annovar.txt path/to/annovar/humandb/". This
                            format imports chr, pos, ref, alt and ANNOVAR annotations. For details please refer
                            to http://www.openbioinformatics.org/annovar/annovar_gene.html
    CASAVA18_indels         Input format illumina indels.txt file, created by CASAVA version 1.8
                            (http://www.illumina.com/support/documentation.ilmn). This format imports chr, pos,
                            ref, alt of most likely genotype, and a Q score for the most likely genotype.
    CASAVA18_snps           Input format illumina snps.txt file, created by CASAVA version 1.8
                            (http://www.illumina.com/support/documentation.ilmn). This format imports chr, pos,
                            ref, alt of most likely genotype, and a Q score for the most likely genotype.
    CGA                     Input format from Complete Genomics Variant file masterVarBeta-[ASM-ID].tsv.bz2,
                            created by Complete Genomcis Analysis Tools (GSA Tools 1.5 or eariler,
                            http://www.completegenomics.com/sequence-data/cgatools/, http://media.completegenom
                            ics.com/documents/DataFileFormats+Standard+Pipeline+2.0.pdf). This format imports
                            chr, pos, ref, alt of only variants that have been fully called and are not equals
                            to ref. (E.g. records with zygosity equal to no-call and half, and varType equal to
                            ref are discarded.)
    basic                   A basic variant import/export format that import variants with four tab-delimited
                            columns (chr, pos, ref, alt), and export variants, optional variant info fields and
                            genotypes.
    csv                     Import variants (chr, pos, ref, alt) in csv format, or output arbitrary specified
                            fields in csv format
    map                     This input format imports variants from files in MAP format (with columns chr, name
                            gen_dist, pos), or any delimiter-separated format with columns chr and pos. Because
                            these input files do not contain reference and alternative alleles of variants,
                            this format queries such information from the dbSNP database using chr and pos.
                            Records that does not exist in dbSNP will be discarded. Records with multiple
                            alternative alleles will lead to multiple records.
    pileup_indel            Input format for samtools pileup indel caller. This format imports chr, pos, ref,
                            alt and genotype.
    plink                   Input format for PLINK dataset. Currently only PLINK binary PED file format is
                            supported (*.bed, *.bim & *.fam)
    polyphen2               To be used to export variants in a format that is acceptable by the polyphen2
                            server http://genetics.bwh.harvard.edu/pph2/bgi.shtml, and to import the FULL
                            report returned by this server.
    rsname                  Import variants (chr, pos, ref, alt) that are queried from dbSNP database using
                            provided rsnames
    tped                    Output to TPED format with the first four columns chr name gen_pos pos, and the
                            rest for genotypes. Variant tools cannot import from this format because it does
                            not contain information about reference genome.
    twoalleles              Import variants (chr, pos, ref, alt) from chr, pos, allele1, and allele2, using a
                            reference genome to determine which one is reference
    vcf                     Import vcf


{{% notice tip %}}
You can suppress descriptions to formats using option `-v0` to command @@vtools show formats 
{{% /notice %}}

If you are interested in a particular format, you can 



    % vtools show format basic

    A basic variant import/export format that import variants with four tab-delimited columns (chr, pos, ref,
    alt), and export variants, optional variant info fields and genotypes.

    Columns:
      1                     chromosome
      2                     variant position, set --pos_adj to -1 to export variants in 0-based positions.
      3                     reference allele
      4                     alternative allele
      5                     Output variant info fields as one column
      6                     genotype in numeric style
    Formatters are provided for fields: gt

    variant:
      chr                   Chromosome
      pos                   1-based position, set --pos_adj to 1 if input position is 0 based.
      ref                   Reference allele, '-' for insertion.
      alt                   Alternative allele, '-' for deletion.

    Format parameters:
      chr_col               Column index for the chromosome field (default: 1)
      pos_col               Column index for the position field (default: 2)
      ref_col               Column index for the reference field (default: 3)
      alt_col               Column index for the alternative field (default: 4)
      pos_adj               Set to 1 to import variants with 0-based positions, or to -1 to export variants in
                            0-based positions. (default: 0)
      fields                Fields to output, simple arithmetics are allowed (e.g. pos+1) but aggregation
                            functions are not supported. (default: )


From the description, we can that format `basic` import variants from a text file, with fields `chr`, `pos`, `ref`, and `alt` import from columns 1, 2, 3 and 4. The input columns could be adjust by format parameters `chr_col`, `pos_col`, `ref_col`, and `alt_col`. This format assumes a 1-based position. If the input data uses 0-based position, parameter `pos_adj` can be used to adjust input. </details>

</details>

If your input file matches the description of a format, you can use this format to import data. The format should be specified by parameter `--format`, although this parameter could be ignored if file format can be detected automatically from file extension (e.g. format `vcf` will be used automatically for files with extension `.vcf` and `.vcf.gz`). 

<details><summary>Examples: Import variants using format `basic`</summary>
    File `variants.txt` has a list of variants as follows 

    % head variants_hg38.txt 

    1   1014042 G   A
    1   1014143 C       T
    1   1014143 C       T
    1   1042136 T       TC
    1   1043288 G       A
    1   6469122 T       TTCC
    1   6473391 C       T
    2   272223  G       A
    2   1436380 A       G
    2   1542533 C       CT
    

You can import variants using format `basic` as follows: 



    % vtools import variants_hg38.txt --format basic --build hg38

    INFO: Importing variants from variants_hg38.txt (1/1)
    variants_hg38.txt: 100% [=======================================================================================================================================================================] 14 1.4K/s in 00:00:00
    INFO: 12 new variants (9 SNVs, 4 insertions, 1 unsupported) from 13 lines are imported.
    Importing genotypes: 0 0.0/s in 00:00:00                                                                                                                                                                               
Copying samples: 0 0.0/s in 00:00:00

    % vtools output variant chr pos ref alt -l 10

    1   1014042 G   A
    1   1014143 C   T
    1   1042137 -   C
    1   1043288 G   A
    1   6469123 -   TCC
    1   6473391 C   T
    2   272223  G   A
    2   1436380 A   G
    2   1542534 -   T
    10  6018115 G   A

</details>

Format parameters can be used to adjust how data are imported using a particular format. For example, fields `chr`, `pos`, `ref`, and `alt` are by default imported from columns 1, 2, 3 and 4 using format `basic`. The input columns could be adjust by format parameters `chr_col`, `pos_col`, `ref_col`, and `alt_col`. If the input data uses 0-based position, parameter `pos_adj` can be used to adjust input. 

<details><summary>Use format parameters to adjust how data are imported</summary>
If the position used in `variants.txt` is zero-based (like all data downloaded from UCSC), you can use format parameter `--pos_adj 1` to add `1` to import positions: 



    % vtools init import -f
    % vtools import variants.txt --format basic --pos_adj 1 --build hg38

    INFO: Importing variants from variants.txt (1/1)
    variants.txt: 100% [================================================================] 20 2.0K/s in 00:00:00
    INFO: 20 new variants (17 SNVs, 1 insertions, 1 deletions, 1 complex variants) from 20 lines are imported.
    Importing genotypes: 0 0.0/s in 00:00:00                                                                   
    Copying samples: 0 0.0/s in 00:00:00    

    % vtools output variant chr pos ref alt -l 10

    1	203148113	T	-
    1	203148169	G	A
    1	203148203	G	C
    1	203148225	G	A
    1	203148266	GG	T
    1	203148285	T	C
    1	203148295	G	T
    1	203148360	C	A
    1	203148361	G	A
    1	203148361	G	C
    

</details>


#### 3.2 Sample genotypes, sample names, and samples without genotype (option `--sample_name`)

An input file can have genotype data for zero (e.g. a list of variants), one, or more than one samples (many `.vcf` files), and genotypes for a sample might be stored in more than one files, it can be confusing how samples are handled in *variant tools*. 



1.  A list of variants without genotype is by default imported without creating a sample. The variants will be imported to the master variant table and there is no way to trace the origin of the variants if variants from multiple files are imported. 
2.  A list of variants can be imported as a sample without genotype if a sample name is given. The variants will be imported to the master variant table. A sample will be created with these variants. You can use `vtools select variant --samples CONDITION` to locate variants belonging to this sample. 
3.  One or more samples will be created for an input file with one or more samples. Variant tools will try to use sample names specified by parameter `--sample_name`, or names from header of input file. A NULL sample name will be used if no sample name could be determined. 


{{% notice tip %}}
Sample names could be changed using command `vtools admin --rename_samples` after they are imported. 
{{% /notice %}}

{{% notice tip %}}
If genotypes for samples are stored in separate files (e.g. chromosome by chromosome), they will be imported as separate samples. If proper sample names are provided, samples with the same names (and belong to the same physical sample) could be merged using command `vtools admin --merge_samples`. 
{{% /notice %}}

<details><summary> Examples: import a list variants and create a sample without genotype</summary>
If there is no genotype in the input file, no sample is created by default. This is the case for the previous example where only variants are imported: 



    % vtools show samples

    sample_name	filename
    

However, if you would like to trace what variants have been imported from each input file, you can create a `sample` (without genotype information) by providing parameter `--sample_name`. 

    % vtools init import -f
    % vtools import variants_hg38.txt --format basic --build hg38 --sample_name noGT
    
    INFO: Importing variants from variants_hg38.txt (1/1)
variants_hg38.txt: 100% [===============================] 14 1.5K/s in 00:00:00
INFO: 12 new variants (9 SNVs, 4 insertions, 1 unsupported) from 13 lines are imported.
Importing genotypes: 100% [=============================] 13 6.5/s in 00:00:02
Copying samples: 100% [=================================] 2 8.6K/s in 00:00:00
Current storage mode is HDF5, transfrom genotype storage mode.....
Creating indexes: 100% [================================] 1 638.2/s in 00:00:00
Selecting genotypes: 100% [=============================] 2 2.0/s in 00:00:01
Getting existing variants: 100% [=======================] 12 85.2K/s in 00:00:00



    

There is a sample called `noGT`, 

    % vtools show samples    

    sample_name	filename
    noGT	variants.txt

although this sample does not have any genotype fields: 

    % vtools show genotypes
    
    sample_name	filename	num_genotypes	sample_genotype_fields
    noGT	variants.txt	20
    

</details> 



#### 3.3 Primary and alternative reference genomes (option `--build`)

Sometimes you can different batches of data that use different reference genomes. For example, your project might involve multiple batches of data over the years and variants from the old and new batches are processed using different versions of pipelines with different reference genome. In addition, you might want to a previous collection of samples or some public dataset as controls to your project, but they might use a different reference genome than your project. *variant tools* allows you to import data in two reference genomes. All you need to do is to specify the correct build of reference genome for each batch of data using option `--build`. 

<details><summary>Import datasets in hg19 and hg38</summary>
Variants from `CEU.vcf.gz` uses build `hg18` of the reference genome, 

    % vtools init import -f
    % vtools import CEU_hg19.vcf --build hg19
    
    INFO: Importing variants from CEU_hg19.vcf (1/1)
    CEU_hg19.vcf: 100% [==================================] 309 17.8K/s in 00:00:00
    INFO: 288 new variants (288 SNVs) from 309 lines are imported.
    Importing genotypes: 100% [===========================] 288 3.1K/s in 00:00:00

    

Data from `variants.txt` are in `hg19`, so we use option `--build hg19` to import them, 

    % vtools import variants_hg38.txt --format basic --build hg38
    
    WARNING: The new files uses a different reference genome (hg38) from the primary reference genome (hg19) of the project.
    INFO: Adding an alternative reference genome (hg38) to the project.
    INFO: Downloading liftOver tool from UCSC
    liftOver: 100% [====================================] 3,383,268.0 1.3M/s in 00:00:02
    INFO: Downloading liftOver chain file from UCSC
    hg19ToHg38.over.chain.gz: 100% [====================] 140,346.0 132.7K/s in 00:00:01
    INFO: Exporting variants in BED format
    Exporting variants: 100% [=================================] 288 19.5K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating table variant: 100% [==============================] 288 6.6K/s in 00:00:00
    Getting existing variants: 100% [==========================] 288 97.4K/s in 00:00:00
    INFO: Importing variants from variants_hg38.txt (1/1)
    variants_hg38.txt: 100% [===================================] 14 1.9K/s in 00:00:00
    INFO: 12 new variants (9 SNVs, 4 insertions, 1 unsupported) from 13 lines are imported.
    WARNING: Sample information is not recorded for a file without genotype and sample name.
    Importing genotypes: 0 0.0/s in 00:00:00
    Copying genotype: 0 0.0/s in 00:00:00
    INFO: Mapping new variants at 12 loci from hg38 to hg19 reference genome
    INFO: Downloading liftOver chain file from UCSC
    hg38ToHg19.over.chain.gz: 100% [====================] 231,197.0 503.6K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating coordinates: 100% [================================] 13 4.2K/s in 00:00:00
    INFO: Coordinates of 12 (13 total, 0 failed to map) new variants are updated.
    

When you execute the second command, *variant tools* will 

1.  Liftover the existing project to hg38 using the UCSC liftover tool 
2.  Get all coordinates from the hg19 input files and map them to hg38. 
3.  Import the hg38 data files using mapped coordinates, while keeping their hg19 coordinates as alternative coordinates. 

variants inputted in this way can be accessed using both reference genomes. 

    % vtools output variant chr pos ref alt --build hg19  | tail -10
    
    1   977517      -   C
    1   978668      G   A
    1   6529183     -   TCC
    1   6533451     C   T
    2   272223      G   A
    2   1440152     A   G
    2   1546306     -   T
    10  6060078     G   A
    10  6066273     G   A
    10  8116242     -   AA

    

    % vtools output variant chr pos ref alt --build hg38 | tail -10
    
    1   1042137     -   C
    1   1043288     G   A
    1   6469123     -   TCC
    1   6473391     C   T
    2   272223      G   A
    2   1436380     A   G
    2   1542534     -   T
    10  6018115     G   A
    10  6024310     G   A
    10  8074279     -   AA    
    
</details>

{{% notice warning %}}
Because the UCSC liftover tool does not guarantee all coordinates can be mapped between reference genomes, variants that cannot be mapped back to the primary reference genome will have missing primary coordinates. **These variants (with missing primary coordinates) can only be retrieved and annotated through the alternative reference genome**. 
Different variants in one reference genome might be mapped to the same variant in another (e.g. variant 90460203 and 91680930 in hg19 are both mapped to 91044656 in hg18). If two (or more) variants imported from the alternative reference genome are mapped to the same coordinates in the primary reference genome, **duplicate entries will appear in the primary reference genome**. If you have data in both reference genome (e.g. hg18, hg19), it is suggested that you **use the more recent reference genome (e.g. hg19) as the primary reference genome**, because latter reference genomes have more variants and less probability of coordinate collision. 
{{% /notice %}}


#### 3.4 Validate build of reference genome and variant positions 

If you are uncertain about the reference genome of your input data, or if the variant positions are 0- or 1-based, you can use command `vtools admin --validate_build` to compare reference alleles with the alleles at the corresponding locations on the reference genome. You will notice a large number of mismatch variants if you have used incorrect reference genome or failed to adjust positions of variants from 0-based positions to 1-based. 

<details><summary>Examples: validate if the correct reference genome has been specified</summary>

Let us import variants from `variants.txt` using hg18, 

    % vtools init import -f
    % vtools import variants_hg38.txt --format basic --build hg19
    % vtools admin --validate_build
    
    Validate reference alleles: 100% [=======================] 12/3 10.3K/s in 00:00:00
    INFO: 8 non-insertion variants are checked. 3 mismatch variants found.
    

3 mismatchs are identified, so we let us try using the `hg38` build of reference genome, 

    % vtools init import -f
    % vtools import variants_hg38.txt --format basic --build hg38
    % vtools admin --validate_build
    
    Validate reference alleles: 100% [========================] 12 9.4K/s in 00:00:00
    INFO: 8 non-insertion variants are checked. 0 mismatch variants found.
    
The variants are more likely created using `hg38`. The mismatch variants can be found in the project log file, or be listed with option `-v2`. It should be verified or removed from the project. 
</details>

#### 3.5 Performance optimization (option `--jobs` and other techniques)

*variant tools* by default uses multiple processes to load data (`--jobs 4`), which works well for most datasets under most computing environments. Compared to importing data using a single process (`--jobs 1`), it performs slightly worse for small datasets, but is significantly faster for large files, especially when multiple files are imported. If you have high speed harddrive (e.g. disk array, SSD), you can use more processes to import data although more processes do not automatically translate to better performance due to the overhead of multi-processing and disk I/O scheduling. 

##### The following discussion is useful if you set STOREMODE to sqlite.

Depending on your computing environment (amount of RAM, speed of harddrive), *vtools import* could be optimized by setting appropriate runtime options that are compatible with your computer hardware environment. One optimization is to **temporarily** set an *in-ram journal mode*, and in-ram cache if the computer has large RAM: 

    % vtools admin --set_runtime_option 'sqlite_pragma=synchronous=OFF,journal_mode=MEMORY,cachesize=10000'
    

The in-ram journal mode will lessen the disk I/O burden, but compromises the database's failure recovery capability. It is therefore recommended to revert the setting after the import is done. 

Another optimization is to move the temporary directory to a large, separate physical disk. By default the temporary directory locates in one of the system's temporary folders (e.g., `/tmp` or `/var/tmp` for Linux). '''Moving `$temp_dir` to a different physical disk will greatly improve the performance of `vtools import` (and `vtools associate`) because of significantly less movement of reading head of harddrives. 


    % vtools admin --set_runtime_option 'temp_dir=/home/HD1/tmp_some_random_name'
    

The folder's name is arbitrary. It will be created each time a command starts and deleted upon completion of the command. 
{{% notice warning %}}
It is very important to make sure that for import and associate commands there is sufficient disk space in the temporary directory, since potentially large temp files will be generated by these commands. 
{{% /notice %}}
After data import is finished, we will set *journal_mode* back to default, for reasons previously discussed. 



    % vtools admin --reset_runtime_option sqlite_pragma
    

Finally, if you need to import a large amount of data from multiple files, it can be helpful to create multiple project, import files one by one (or group by group), and create a parent project from these children projects. 


{{% notice tip %}}
[This tutorial][4] demonstrates how to import all genotype data from the 1000 genomes project using different techniques. It contains some tips on how to import a large amount of data (the uncompressed 1000 genome data exceed 1 Tb). 
{{% /notice %}}





 
 [1]: http://docs.python.org/library/configparser.html
 [2]: http://docs.python.org/2/library/re.html#re.match
 [3]: mailto:varianttools-devel@lists.sourceforge.net
 [4]: http://vtools.houstonbioinformatics.org/format/ANNOVAR.fmt
 [5]: http://vtools.houstonbioinformatics.org/format/CASAVA18_snps.fmt
 
 