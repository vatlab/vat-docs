+++
title = "ACM-BCB tutorial"
weight = 17
hidden = true
+++

## Tutorial (ACM-BCB2014): Integrated analysis of next-gen sequencing data using variant tools


This tutorial explains the concepts of variant tools and demonstrates, through examples, how to use variant tools to import, select, and annotate genetic variants. You will need to have variant tools installed (Linux or Mac OSX) to follow this tutorial. Please also download sample data from [<font color=#FF0000 size = 6px> here </font>][1]. 



### 1. Getting help (`--help`, `` `vtools show ``)

Getting details of commands 



    \\( vtools -h
    \\( vtools init -h
    


{{% notice tip %}}

The [variant tools website](https://vatlab.github.io/vat-docs/) has detailed explanation and examples for all commands, utilities and pipelines.

{{% /notice %}}

Getting details of file formats, fields, pipelines, association tests, file tracks, runtime options, annotation databases, snapshots, pipelines and simulation models. 

Getting a list of all supported file formats: 

    \\( vtools show formats -v0
    

    CASAVA18_snps
    CASAVA18_indels
    plink
    rsname
    ANNOVAR_output
    ANNOVAR
    pileup_indel
    ANNOVAR_exonic_variant_function
    ANNOVAR_variant_function
    twoalleles
    map
    polyphen2
    basic
    vcf
    CGA
    csv
    tped
    

and details of a particular format: 

    \\( vtools show format basic
    

    A basic variant import/export format that import variants with four tab-
    delimited columns (chr, pos, ref, alt), and export variants, optional variant
    info fields and genotypes.
    
    Columns:
      1                     chromosome
      2                     variant position, set --pos_adj to -1 to export
                            variants in 0-based positions.
      3                     reference allele
      4                     alternative allele
      5                     Output variant info fields as one column
      6                     genotype in numeric style
    Formatters are provided for fields: gt
    
    variant:
      chr                   Chromosome
      pos                   1-based position, set --pos_adj to 1 if input
                            position is 0 based.
      ref                   Reference allele, '-' for insertion.
      alt                   Alternative allele, '-' for deletion.
    
    Format parameters:
      chr_col               Column index for the chromosome field (default: 1)
      pos_col               Column index for the position field (default: 2)
      ref_col               Column index for the reference field (default: 3)
      alt_col               Column index for the alternative field (default: 4)
      pos_adj               Set to 1 to import variants with 0-based positions,
                            or to -1 to export variants in 0-based positions.
                            (default: 0)
      fields                Fields to output, simple arithmetics are allowed
                            (e.g. pos+1) but aggregation functions are not
                            supported. (default: )
    



### 2. Create a project (`init`)

Create an empty project 

    \\( vtools init tutorial
    

    INFO: variant tools 2.4.0 : Copyright (c) 2011 - 2014 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project tutorial
    

You cannot create a project in a folder with another project 

    \\( vtools init tutorial
    

    ERROR: A project can only be created in a directory without another project.
    

but you can use option `--force` to override this 

    \\( vtools init tutorial -f
    

    INFO: variant tools 2.4.0 : Copyright (c) 2011 - 2014 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project tutorial
    



### 3. Load data (`` `vtools import ``)

Let us have a look at the data 

    \\( gzcat CEU.vcf.gz | head -10
    

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
    bpeng1@BCBMC02MG1WJF6T:~/temp\\)  gzcat CEU.vcf.gz | head -14
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
    #CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	NA06985	NA06986	NA06994	NA07000	NA07037	NA07051	NA07346	NA07347	NA07357	NA10847	NA10851	NA11829	NA11830	NA11831	NA11832	NA11840	NA11881	NA11894	NA11918	NA11919	NA11920	NA11931	NA11992	NA11993	NA11994	NA11995	NA12003	NA12004	NA12005	NA12006	NA12043	NA12044	NA12045	NA12144	NA12154	NA12155	NA12156	NA12234	NA12249	NA12287	NA12414	NA12489	NA12716	NA12717	NA12749	NA12750	NA12751	NA12760	NA12761	NA12762	NA12763	NA12776	NA12812	NA12813	NA12814	NA12815	NA12828	NA12872	NA12873	NA12874
    1	533	.	G	C	.	PASS	AA=.;AC=6;AN=120;DP=423	GT:DP:CB	0|0:6:SMB	0|0:14:SMB	0|0:4:SMB	0|0:3:SMB	0|0:7:SMB	0|0:4:SMB	1|0:6:MB	0|0:3:SMB	0|0:13:SMB	0|0:1:SMB	0|0:14:SMB	0|0:10:SMB	0|0:6:SB	0|0:2:SMB	0|0:6:SMB	0|0:4:SMB	0|0:2:SMB	0|0:15:SMB	0|0:2:SMB	0|0:1:SMB	0|0:26:SMB	0|0:6:SMB	0|1:14:MB	0|0:5:SMB	0|0:3:SMB	0|0:20:SMB	0|0:3:SMB	0|0:2:SMB	0|0:4:SMB	0|0:12:SMB	0|0:1:SMB	0|0:7:SMB	0|0:2:SMB	0|0:25:SMB	0|0:9:SMB	0|1:1:MB	0|0:9:SMB	0|0:1:SMB	0|0:6:SMB	0|0:12:SMB	0|0:7:SMB	0|0:18:SMB	0|0:2:SMB	0|0:2:SM	0|0:38:SMB	0|0:3:SM	0|0:3:SMB	0|0:5:SMB	0|0:5:SMB	0|0:3:SMB	0|0:0:MB	0|0:5:SMB	0|0:7:SMB	0|0:0:SMB	0|0:6:SMB	1|0:5:SMB	0|0:4:MB	0|0:5:SMB	1|0:5:MB	0|1:9:SMB
    

If the compressed .vcf file is indexed (with `.tbi` file), you can use `vtools` to show its information 



    \\( vtools show track CEU.vcf.gz
    

    Version                 VCF v4.0
    Number of fields:       69
    
    Header: (excluding INFO and FORMAT lines)
                            ##reference=human_b36_both.fasta
                            ##rsIDs=dbSNP b129 mapped to NCBI 36.3, August 10, 2009
    
    Available fields (with type VARCHAR if unspecified or all=1):
    0 (INTEGER)             1 if matched
    chr (1, chrom)          chromosome
    pos (2, INTEGER)        position (1-based)
    name (3)                name of variant
    ref (4)                 reference allele
    alt (5)                 alternative alleles
    qual (6)                qual
    filter (7)              filter
    info (8, default)       variant info fields
    info.DP (INTEGER)       Total Depth
    info.HM2 (INTEGER, flag) HapMap2 membership
    info.HM3 (INTEGER, flag) HapMap3 membership
    info.AA                 Ancestral Allele, ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/pilot_data/technical/reference/ancestral_alignments/README
    info.AC (INTEGER)       Allele count in genotypes
    info.AN (INTEGER)       Total number of alleles in called genotypes
    format (9)              genotype format
    NA06985 (10)            genotype for sample NA06985
    NA06985.GT              Genotype for sample NA06985
    NA06985.DP (INTEGER)    Read Depth for sample NA06985
    NA06985.CB              Called by S(Sanger), M(UMich), B(BI) for sample NA06985
    ...
    

Looking for 

*   reference genome used 
*   fields that can be imported 

Import data with one variant information field `AA`, 

    \\( vtools import CEU.vcf.gz --var_info AA --build hg18
    

    INFO: Importing variants from CEU.vcf.gz (1/1)
    CEU.vcf.gz: 100% [=================================================] 300 16.8K/s in 00:00:00
    INFO: 288 new variants (288 SNVs) from 300 lines are imported.
    Importing genotypes: 100% [======================================] 18,000 9.0K/s in 00:00:02
    Copying samples: 100% [==============================================] 79 78.9/s in 00:00:01
    

Show the status of the project 

    \\( vtools show
    

    Project name:                tutorial
    Created on:                  Fri Sep 19 06:09:40 2014
    Primary reference genome:    hg18
    Secondary reference genome:  
    Runtime options:             verbosity=1
    Variant tables:              variant
    Annotation databases:        
    

available variant tables 

    \\( vtools show tables
    

    table      #variants     date message
    variant          288    Sep19 Master variant table
    

details of a variant table 

    \\( vtools show table variant
    

    Name:                   variant
    Description:            Master variant table
    Creation date:          Sep19
    Command:
    Fields:                 variant_id, bin, chr, pos, ref, alt, AA
    Number of variants:     288
    

all genotypes 

    \\( vtools show genotypes -l 10
    

    sample_name	filename  	num_genotypes	sample_genotype_fields
    NA06985    	CEU.vcf.gz	287          	GT
    NA06986    	CEU.vcf.gz	287          	GT
    NA06994    	CEU.vcf.gz	287          	GT
    NA07000    	CEU.vcf.gz	287          	GT
    NA07037    	CEU.vcf.gz	287          	GT
    NA07051    	CEU.vcf.gz	287          	GT
    NA07346    	CEU.vcf.gz	288          	GT
    NA07347    	CEU.vcf.gz	287          	GT
    NA07357    	CEU.vcf.gz	287          	GT
    NA10847    	CEU.vcf.gz	287          	GT
    

Information fields for each variant 

    \\( vtools show fields
    

    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    variant.AA (char)
    

Output variants in a specified variant table with specified info fields 

    \\( vtools output variant chr pos ref alt AA -l 10
    

    1	533  	G	C	.
    1	41342	T	A	.
    1	41791	G	A	.
    1	44449	T	C	C
    1	44539	C	T	T
    1	44571	G	C	g
    1	45162	C	T	c
    1	52066	T	C	C
    1	53534	G	A	G
    1	75891	T	C	.
    



### 4. Sample statistics (`` `vtools update ``)

Command update adds more variant info fields to the project. 



#### 4.1 import additional information from the source files

    \\( vtools update variant --from_file CEU.vcf.gz --var_info DP
    

    INFO: Using primary reference genome hg18 of the project.
    Getting existing variants: 100% [================================================] 288 197.1K/s in 00:00:00
    INFO: Updating variants from CEU.vcf.gz (1/1)
    CEU.vcf.gz: 100% [=================================================================] 300 9.4K/s in 00:00:00
    INFO: Field DP of 288 variants are updated
    

A new field `DP` is added, 

    \\( vtools show fields
    

    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an deletion)
    variant.AA (char)
    variant.DP (int)
    



    \\( vtools output variant chr pos ref alt AA DP -l 10
    

    1	533  	G	C	.	423
    1	41342	T	A	.	188
    1	41791	G	A	.	192
    1	44449	T	C	C	166
    1	44539	C	T	T	131
    1	44571	G	C	g	135
    1	45162	C	T	c	166
    1	52066	T	C	C	159
    1	53534	G	A	G	243
    1	75891	T	C	.	182
    



#### 4.2 Add sample statistics as variant info fields

Count the number of alternative alleles (not genotypes), homozygotes, heterozygotes, and calculate minior allele frequency for each variant 



    \\( vtools update variant --from_stat 'num=#(alt)' 'hom=#(hom)' 'het=#(het)' 'maf=maf()'
    

    Counting variants: 100% [==================================] 60 1.1K/s in 00:00:00
    INFO: Adding variant info field num with type INT
    INFO: Adding variant info field hom with type INT
    INFO: Adding variant info field het with type INT
    INFO: Adding variant info field maf with type FLOAT
    Updating variant: 100% [=================================] 288 65.0K/s in 00:00:00
    INFO: 288 records are updated
    



    \\( vtools output variant chr pos ref alt num hom het maf -l 10
    

    1	533  	G	C	6 	0	6 	0.05
    1	41342	T	A	29	3	23	0.241666666667
    1	41791	G	A	5 	0	5 	0.0416666666667
    1	44449	T	C	2 	0	2 	0.0166666666667
    1	44539	C	T	2 	0	2 	0.0166666666667
    1	44571	G	C	7 	0	7 	0.0583333333333
    1	45162	C	T	20	4	12	0.166666666667
    1	52066	T	C	18	1	16	0.15
    1	53534	G	A	18	0	18	0.15
    

We can also calculate sample statistics for a subset of samples (e.g. in cases and controls) 



    \\( vtools show samples -l 10
    

    sample_name	filename
    NA06985    	CEU.vcf.gz
    NA06986    	CEU.vcf.gz
    NA06994    	CEU.vcf.gz
    NA07000    	CEU.vcf.gz
    NA07037    	CEU.vcf.gz
    NA07051    	CEU.vcf.gz
    NA07346    	CEU.vcf.gz
    NA07347    	CEU.vcf.gz
    NA07357    	CEU.vcf.gz
    NA10847    	CEU.vcf.gz
    (50 records omitted)
    



    \\( vtools update variant --from_stat 'num12=#(alt)' 'hom12=#(hom)' 'het12=#(het)' \
        'maf12=maf()' --samples "sample_name like 'NA12%'"
    

    INFO: 34 samples are selected
    Counting variants: 100% [==================================] 34 1.9K/s in 00:00:00
    INFO: Adding variant info field num12 with type INT
    INFO: Adding variant info field hom12 with type INT
    INFO: Adding variant info field het12 with type INT
    INFO: Adding variant info field maf12 with type FLOAT
    Updating variant: 100% [=================================] 288 45.9K/s in 00:00:00
    INFO: 288 records are updated
    



    \\( vtools output variant chr pos num maf num12 maf12 -l 10
    

    1	533  	6 	0.05           	4 	0.0588235294118
    1	41342	29	0.241666666667 	16	0.235294117647
    1	41791	5 	0.0416666666667	2 	0.0294117647059
    1	44449	2 	0.0166666666667	2 	0.0294117647059
    1	44539	2 	0.0166666666667	2 	0.0294117647059
    1	44571	7 	0.0583333333333	7 	0.102941176471
    1	45162	20	0.166666666667 	11	0.161764705882
    1	52066	18	0.15           	14	0.205882352941
    1	53534	18	0.15           	8 	0.117647058824
    1	75891	11	0.0916666666667	9 	0.132352941176
    



    \\( vtools show fields
    

    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an
                                 insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an
                                 deletion)
    variant.AA (char)
    variant.DP (int)
    variant.num (int)       Created from stat "#(alt)" with type INT on Sep19
    variant.hom (int)       Created from stat "#(hom)" with type INT on Sep19
    variant.het (int)       Created from stat "#(het)" with type INT on Sep19
    variant.maf (float)     Created from stat "maf()" with type FLOAT on Sep19
    variant.num12 (int)     Created from stat "#(alt)" for samples ["sample_name like
                                 'NA12%'"]with type INT on Sep19
    variant.hom12 (int)     Created from stat "#(hom)" for samples ["sample_name like
                                 'NA12%'"]with type INT on Sep19
    variant.het12 (int)     Created from stat "#(het)" for samples ["sample_name like
                                 'NA12%'"]with type INT on Sep19
    variant.maf12 (float)   Created from stat "maf()" for samples ["sample_name like
                                 'NA12%'"]with type FLOAT on Sep19
    



### 5. Phenotypes (`` `vtools phenotype ``)

    \\( vtools show phenotypes -l 10
    

    sample_name
    NA06985
    NA06986
    NA06994
    NA07000
    NA07037
    NA07051
    NA07346
    NA07347
    NA07357
    NA10847
    (50 records omitted)
    



    \\( head -5 phenotype.txt 
    

    sample_name	aff	sex	BMI
    NA06985	2	F	19.64
    NA06986	1	M	None
    NA06994	1	F	19.49
    NA07000	2	F	21.52
    



    \\( vtools phenotype --from_file phenotype.txt 
    

    INFO: Adding phenotype aff of type INT
    INFO: Adding phenotype sex of type VARCHAR(1)
    INFO: Adding phenotype BMI of type FLOAT
    WARNING: Value "None" is treated as missing in phenotype BMI
    WARNING: 1 missing values are identified for phenotype BMI
    



    \\( vtools show phenotypes -l 10
    

    sample_name	aff	sex	BMI
    NA06985    	2  	F  	19.64
    NA06986    	1  	M  	.
    NA06994    	1  	F  	19.49
    NA07000    	2  	F  	21.52
    NA07037    	2  	F  	23.05
    NA07051    	1  	F  	21.01
    NA07346    	1  	F  	18.93
    NA07347    	2  	M  	19.2
    NA07357    	2  	M  	20.61
    NA10847    	2  	M  	14.6
    (50 records omitted)
    


{{% notice tip %}}
Phenotypes can be used to select samples. 
{{% /notice %}}


    \\( vtools show samples -l 10
    

    sample_name	filename  	aff	sex	BMI
    NA06985    	CEU.vcf.gz	2  	F  	19.64
    NA06986    	CEU.vcf.gz	1  	M  	.
    NA06994    	CEU.vcf.gz	1  	F  	19.49
    NA07000    	CEU.vcf.gz	2  	F  	21.52
    NA07037    	CEU.vcf.gz	2  	F  	23.05
    NA07051    	CEU.vcf.gz	1  	F  	21.01
    NA07346    	CEU.vcf.gz	1  	F  	18.93
    NA07347    	CEU.vcf.gz	2  	M  	19.2
    NA07357    	CEU.vcf.gz	2  	M  	20.61
    NA10847    	CEU.vcf.gz	2  	M  	14.6
    (50 records omitted)
    



    \\( vtools update variant --from_stat 'nCase=#(alt)' --samples 'aff=2'
    

    INFO: 35 samples are selected
    Counting variants: 100% [=============================] 35 1.4K/s in 00:00:00
    INFO: Adding variant info field nCase with type INT
    Updating variant: 100% [============================] 288 72.3K/s in 00:00:00
    INFO: 288 records are updated
    



    \\( vtools update variant --from_stat 'nCtrl=#(alt)' --samples 'aff=1'
    

    INFO: 25 samples are selected
    Counting variants: 100% [=============================] 25 2.0K/s in 00:00:00
    INFO: Adding variant info field nCtrl with type INT
    Updating variant: 100% [============================] 288 78.5K/s in 00:00:00
    INFO: 288 records are updated
    



### 6. Variant Selection (`` `vtools select ``)

The master variant table `variant` contains all variants in the project, we can select subsets of variants from this table and create multiple variant tables. 



    \\( vtools show fields
    

    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an
                            insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an
                            deletion)
    variant.AA (char)
    variant.DP (int)
    variant.num (int)       Created from stat "#(alt)" with type INT on Sep19
    variant.hom (int)       Created from stat "#(hom)" with type INT on Sep19
    variant.het (int)       Created from stat "#(het)" with type INT on Sep19
    variant.maf (float)     Created from stat "maf()" with type FLOAT on Sep19
    variant.num12 (int)     Created from stat "#(alt)" for samples ["sample_name like
                            'NA12%'"]with type INT on Sep19
    variant.hom12 (int)     Created from stat "#(hom)" for samples ["sample_name like
                            'NA12%'"]with type INT on Sep19
    variant.het12 (int)     Created from stat "#(het)" for samples ["sample_name like
                            'NA12%'"]with type INT on Sep19
    variant.maf12 (float)   Created from stat "maf()" for samples ["sample_name like
                            'NA12%'"]with type FLOAT on Sep19
    variant.nCase (int)     Created from stat "#(alt)" for samples ['aff=2']with type INT
                            on Sep19
    variant.nCtrl (int)     Created from stat "#(alt)" for samples ['aff=1']with type INT
                            on Sep19
    

Select variant and output to another table (option `--to_table`) 

    \\( vtools select variant 'maf > 0.1' -t common 'Variants with MAF > 0.1'
    

    Running: 0 0.0/s in 00:00:00                                                          
    INFO: 89 variants selected.
    



    \\( vtools show tables
    

    table      #variants     date message
    common            89    Sep19 Variants with MAF > 0.1
    variant          288    Sep19 Master variant table
    



    \\( vtools output common chr pos ref alt AA maf -l 10
    

    1	41342 	T	A	.	0.241666666667
    1	45162 	C	T	c	0.166666666667
    1	52066 	T	C	C	0.15
    1	53534 	G	A	G	0.15
    1	98173 	T	C	.	0.483333333333
    1	225792	G	A	.	0.116666666667
    1	742429	G	A	g	0.141666666667
    1	742584	A	G	a	0.141666666667
    1	743268	C	A	a	0.116666666667
    1	743288	T	C	t	0.308333333333
    

Count the number of variants 



    \\( vtools select common 'hom > 2' --count
    

    Counting variants: 0 0.0/s in 00:00:00                                                
    45
    

or output them, 



    \\( vtools select common 'hom > 2' -o chr pos hom het maf -l 10
    

    1	41342 	3 	23	0.241666666667
    1	45162 	4 	12	0.166666666667
    1	98173 	10	38	0.483333333333
    1	742429	43	17	0.141666666667
    1	742584	43	17	0.141666666667
    1	743268	46	14	0.116666666667
    1	743288	29	25	0.308333333333
    1	743712	5 	25	0.291666666667
    1	744197	44	16	0.133333333333
    1	744366	43	17	0.141666666667
    

You can also select variants from specified samples 



    \\( vtools select common --samples "sample_name = 'NA12776'" -t common_in_12776
    

    INFO: 1 samples are selected by condition: sample_name = 'NA12776'
    Running: 0 0.0/s in 00:00:00                                                          
    INFO: 88 variants selected.
    



### 7. Annotation databases (`` `vtools use ``)

    \\( vtools show annotations -v0 -l 10
    

    CancerGeneCensus-20130711
    CancerGeneCensus
    CosmicCodingMuts-v67_20131024
    CosmicCodingMuts
    CosmicMutantExport-v67_241013
    CosmicMutantExport
    CosmicNonCodingVariants-v67_241013
    CosmicNonCodingVariants
    DGV-hg18_20130723
    DGV-hg19_20130723
    (77 records omitted)
    



#### 7.1 Genes 

    \\( vtools use refGene
    

    INFO: Downloading annotation database from annoDB/refGene.ann
    ERROR: Annotation database cannot be used because it is based on a reference genome that
    is different from the one used by the project. Please use a version of annotation databse
    for the project (vtools show annotations), or liftover the existing project (vtoos liftover)
    to make it compatible with the annotation database.
    



    \\( vtools liftover hg19
    

    INFO: Downloading liftOver chain file from UCSC
    INFO: Exporting variants in BED format
    Exporting variants: 100% [==================================] 288 137.0K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating table variant: 100% [================================] 288 1.6K/s in 00:00:00
    

Coordinates in hg18 

    \\( vtools output variant chr pos ref alt -l 10
    

    1	533  	G	C
    1	41342	T	A
    1	41791	G	A
    1	44449	T	C
    1	44539	C	T
    1	44571	G	C
    1	45162	C	T
    1	52066	T	C
    1	53534	G	A
    1	75891	T	C
    

Coordinates in hg19 

    \\( vtools output variant chr pos ref alt -l 10 --build hg19
    

    1	10533	G	C
    1	51479	T	A
    1	51928	G	A
    1	54586	T	C
    1	54676	C	T
    1	54708	G	C
    1	55299	C	T
    1	62203	T	C
    1	63671	G	A
    1	86028	T	C
    



    \\( vtools use refGene
    

    INFO: Downloading annotation database from annoDB/refGene.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/refGene-hg19_20130904.DB.gz
    INFO: Using annotation DB refGene as refGene in project tutorial.
    INFO: Known human protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq).
    



    \\( vtools show annotation refGene
    

    Annotation database refGene (version hg19_20130904)
    Description:            Known human protein-coding and non-protein-coding genes taken
      from the NCBI RNA reference sequences collection (RefSeq).
    Database type:          range
    Reference genome hg19:  chr, txStart, txEnd
      name (char)           Gene name
      chr (char)
      strand (char)         which DNA strand contains the observed alleles
      txStart (int)         Transcription start position (1-based)
      txEnd (int)           Transcription end position
      cdsStart (int)        Coding region start (1-based)
      cdsEnd (int)          Coding region end
      exonCount (int)       Number of exons
      exonStarts (char)     Starting point of exons (adjusted to 1-based positions)
      exonEnds (char)       Ending point of exons
      score (int)           Score
      name2 (char)          Alternative name
      cdsStartStat (char)   cds start stat, can be 'non', 'unk', 'incompl', and 'cmp1'
      cdsEndStat (char)     cds end stat, can be 'non', 'unk', 'incompl', and 'cmp1'
    



    \\( vtools show fields
    

    variant.chr (char)      Chromosome name (VARCHAR)
    variant.pos (int)       Position (INT, 1-based)
    variant.ref (char)      Reference allele (VARCHAR, - for missing allele of an
                            insertion)
    variant.alt (char)      Alternative allele (VARCHAR, - for missing allele of an
                            deletion)
    variant.AA (char)
    variant.DP (int)
    variant.num (int)       Created from stat "#(alt)" with type INT on Sep19
    variant.hom (int)       Created from stat "#(hom)" with type INT on Sep19
    variant.het (int)       Created from stat "#(het)" with type INT on Sep19
    variant.maf (float)     Created from stat "maf()" with type FLOAT on Sep19
    variant.num12 (int)     Created from stat "#(alt)" for samples ["sample_name like
                            'NA12%'"]with type INT on Sep19
    variant.hom12 (int)     Created from stat "#(hom)" for samples ["sample_name like
                            'NA12%'"]with type INT on Sep19
    variant.het12 (int)     Created from stat "#(het)" for samples ["sample_name like
                            'NA12%'"]with type INT on Sep19
    variant.maf12 (float)   Created from stat "maf()" for samples ["sample_name like
                            'NA12%'"]with type FLOAT on Sep19
    variant.nCase (int)     Created from stat "#(alt)" for samples ['aff=2']with type INT
                            on Sep19
    variant.nCtrl (int)     Created from stat "#(alt)" for samples ['aff=1']with type INT
                            on Sep19
    variant.alt_chr (char)
    variant.alt_pos (int)
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
    



    \\( vtools output variant chr pos refGene.name refGene.name2 -l10
    

    1	533  	.	.
    1	41342	.	.
    1	41791	.	.
    1	44449	.	.
    1	44539	.	.
    1	44571	.	.
    1	45162	.	.
    1	52066	.	.
    1	53534	.	.
    1	75891	.	.
    



    \\( vtools select variant 'refGene.chr IS NOT NULL' -t in_gene
    

    Running: 4 902.7/s in 00:00:00                                                        
    INFO: 121 variants selected.
    



    \\( vtools output in_gene chr pos refGene.name refGene.name2 -l10
    

    1	695745	NR_033908	LOC100288069
    1	697749	NR_033908	LOC100288069
    1	703777	NR_033908	LOC100288069
    1	703882	NR_033908	LOC100288069
    1	743268	NR_103536	FAM87B
    1	743288	NR_103536	FAM87B
    1	743404	NR_103536	FAM87B
    1	743712	NR_103536	FAM87B
    1	744074	NR_103536	FAM87B
    1	744197	NR_103536	FAM87B
    



#### 7.2 dbSNP, dbNSFP, 1000 genomes

    \\( vtools use dbSNP
    

    INFO: Downloading annotation database from annoDB/dbSNP.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/dbSNP-hg19_138.DB.gz
    INFO: Using annotation DB dbSNP as dbSNP in project tutorial.
    INFO: dbSNP version 138, created using vcf file downloaded from NCBI
    



    \\( vtools select common 'dbSNP.chr IS NOT NULL' -t in_dbSNP
    

    Running: 0 0.0/s in 00:00:00                                                          
    INFO: 83 variants selected.
    



    \\( vtools output in_dbSNP chr pos ref alt dbSNP.name -l 10
    

    1	41342 	T	A	rs116400033
    1	45162 	C	T	rs10399749
    1	52066 	T	C	rs28402963
    1	53534 	G	A	rs116440577
    1	98173 	T	C	rs74747225
    1	225792	G	A	rs200488504
    1	742429	G	A	rs3094315
    1	742584	A	G	rs3131972
    1	743268	C	A	rs61770173
    1	743288	T	C	rs3131970
    

Select damaging variants 



    \\( vtools use dbNSFP
    

    INFO: Downloading annotation database from annoDB/dbNSFP.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/dbNSFP-hg18_hg19_2_4.DB.gz
    INFO: Decompressing /Users/bpeng1/.variant_tools/annoDB/dbNSFP-hg18_hg19_2_4.DB.gz
    INFO: Using annotation DB dbNSFP as dbNSFP in project tutorial.
    INFO: dbNSFP version 2.4, maintained by Xiaoming Liu from UTSPH. Please cite
    "Liu X, Jian X, and Boerwinkle E. 2011. dbNSFP: a lightweight database of human
    non-synonymous SNPs and their functional predictions. Human Mutation. 32:894-899" and
    "Liu X, Jian X, and Boerwinkle E. 2013. dbNSFP v2.0: A Database of Human Nonsynonymous
    SNVs and Their Functional Predictions and Annotations. Human Mutation. 34:E2393-E2402."
    if you find this database useful.
    

Unfortunately, this dataset does not have any nonsynonymous variants recorded in dbNSFP 

    \\( vtools select variant 'dbNSFP.chr is not NULL' -c
    

    Counting variants: 0 0.0/s in 00:00:00                                                
    0
    



### 8. Slightly more advanced features

#### 8.1 Function `ref_genome`

    \\( vtools output common chr pos ref 'ref_sequence(chr, pos)' -l 10 
    

    1	41342 	T	T
    1	45162 	C	C
    1	52066 	T	T
    1	53534 	G	G
    1	98173 	T	T
    1	225792	G	G
    1	742429	G	G
    1	742584	A	A
    1	743268	C	C
    1	743288	T	T
    



    \\( vtools output common chr pos ref 'ref_sequence(chr, pos-5, pos+5)' -l 10 
    

    1	41342 	T	TGTATTTTATG
    1	45162 	C	CTATGCGACCT
    1	52066 	T	TATTATATTTT
    1	53534 	G	TCGTCGGCTCA
    1	98173 	T	TTCCATAAGAA
    1	225792	G	TTTTCGTGTGC
    1	742429	G	GAAACGTTTGA
    1	742584	A	GGAAAAGGGAA
    1	743268	C	GATGGCGGGAA
    1	743288	T	CTCTGTGGGCC
    



#### 8.2 Function `genotype` and `samples`

You can check the genotype of variants in a particular sample 

    \\( vtools output common chr pos ref alt "genotype('NA07037')" -l 10
    

    1	41342 	T	A	0
    1	45162 	C	T	2
    1	52066 	T	C	0
    1	53534 	G	A	1
    1	98173 	T	C	1
    1	225792	G	A	0
    1	742429	G	A	2
    1	742584	A	G	2
    1	743268	C	A	2
    1	743288	T	C	2
    

or in all samples 

    \\( vtools output common chr pos "genotype()" -l 2
    

    1	41342	0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,2,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,2,1,1,1,0,0,0,1,1,2,0,1,0,0,1,1,0,0,0,0
    1	45162	0,0,0,1,2,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,1,0,1,0,1,2,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,2,0,0,0
    

Function `samples` outputs name of samples that harbor the variants 

    \\( vtools output common "samples('geno_filter=GT!=0')" -l 2
    

    NA06986,NA06994,NA07051,NA07347,NA07357,NA11830,NA11840,NA11918,NA11920,NA11992,NA11993,NA11994,NA12005,NA12044,NA12154,NA12234,NA12414,NA12489,NA12716,NA12717,NA12760,NA12761,NA12762,NA12776,NA12814,NA12815
    NA07000,NA07037,NA07051,NA11829,NA11840,NA11894,NA11995,NA12004,NA12144,NA12155,NA12234,NA12249,NA12761,NA12763,NA12814,NA12828
    



#### 8.3 Function `track`

A track is an external file that contains information about variants, which can be in format `vcf`, `bam` and `BigWig` and `BigBed`. 

    \\( vtools output common chr pos ref alt "track('CEU.vcf.gz')" -l 10
    

    1	41342 	T	A	AA=.;AC=29;AN=120;DP=188
    1	45162 	C	T	AA=c;AC=20;AN=120;DP=166;HM2
    1	52066 	T	C	AA=C;AC=18;AN=120;DP=159
    1	53534 	G	A	AA=G;AC=18;AN=120;DP=243
    1	98173 	T	C	AA=.;AC=58;AN=120;DP=184
    1	225792	G	A	AA=.;AC=14;AN=120;DP=464
    1	742429	G	A	AA=g;AC=103;AN=120;DP=314;HM2
    1	742584	A	G	AA=a;AC=103;AN=120;DP=366;HM3
    1	743268	C	A	AA=a;AC=106;AN=120;DP=64
    1	743288	T	C	AA=t;AC=83;AN=120;DP=69
    


{{% notice tip %}}
The `track` function is particularly useful for checking reads that cover a variant in BAM files. 
{{% /notice %}}


#### 8.4 Pipeline `ANNOVA`

    \\( vtools show pipeline ANNOVAR 
    

    Pipeline to call ANNOVAR and import results as variant info fields.
    
    Available pipelines: geneanno
    
    Pipeline "geneanno":  This pipeline exports variants in specified variant table (parameter
    --var_table, default to variant), executes ANNOVAR's gene-based annotation
    (annotate_variantion.pl --geneanno), and imports specified fields from output of the command.
    Four fields (two for all variants and two for exonic variants) will be imported unless you
    disable some of them using parameters --variant_info and --exonic_info. No input or output
    file is required for this pipeline, but a snapshot could be specified, in which case the
    snapshot will be loaded (and overwrite the present project).
      geneanno_0:         Load specified snapshot if a snapshot is specified. Otherwise use the
                          existing project.
      geneanno_10:        Check the existence of ANNOVAR's annotate_variation.pl command.
      geneanno_11:        Determine the humandb path of ANNOVAR
      geneanno_14:        Download gene database for specified --dbtype if they are unavailable
      geneanno_20:        Export variants in ANNOVAR format
      geneanno_30:        Execute ANNOVAR annotate_variation.pl --geneanno
      geneanno_40:        Importing results from ANNOVAR output .variant_function if
                          --variant_info is specified
      geneanno_50:        Importing results from ANNOVAR output .exonic_variant_function if
                          --exonic_info is specified
    
    Pipeline parameters:
      var_table           Variant table for the variants to be analyzed. (default: variant)
      annovar_path        Path to a directory that contains annotate_variation.pl, if the script
                          is not in the default \\(PATH.
      dbtype              --dbtype parameter that will be passed to annotate_variation.pl
                          --dbtype. The default value if refGene, but you can also use knownGene,
                          ensGene. (default: refGene)
      variant_info        Fields to import from the first two columns of .variant_function output
                          of ANNOVAR. (default: region_type, region_name)
      exonic_info         Fields to import from the .exonic_variant_function output of ANNOVAR.
                          It has to be zero, one or more of mut_type and function. (default:
                          mut_type, function)
    

Using ANNOVAR to annotate variants 

    \\( vtools execute ANNOVAR --annovar_path ~/bin/annovar/ 
    

    INFO: Executing ANNOVAR.geneanno_0: Load specified snapshot if a snapshot is specified. Otherwise use the existing project.
    INFO: Executing ANNOVAR.geneanno_10: Check the existence of ANNOVAR's annotate_variation.pl command.
    INFO: Command /Users/bpeng1/bin/annovar//annotate_variation.pl is located.
    INFO: Executing ANNOVAR.geneanno_11: Determine the humandb path of ANNOVAR
    INFO: Running which /Users/bpeng1/bin/annovar//annotate_variation.pl > cache/annovar.path
    INFO: Executing ANNOVAR.geneanno_14: Download gene database for specified --dbtype if they are unavailable
    INFO: Running /Users/bpeng1/bin/annovar//annotate_variation.pl --buildver hg18 -downdb refGene /Users/bpeng1/bin/annovar//humandb
    INFO: Executing ANNOVAR.geneanno_20: Export variants in ANNOVAR format
    INFO: Running vtools export variant --format ANNOVAR --output cache/annovar_input
    INFO: Executing ANNOVAR.geneanno_30: Execute ANNOVAR annotate_variation.pl --geneanno
    INFO: Running /Users/bpeng1/bin/annovar//annotate_variation.pl --geneanno --dbtype refGene --buildver hg18 cache/annovar_input /Users/bpeng1/bin/annovar//humandb
    INFO: Executing ANNOVAR.geneanno_40: Importing results from ANNOVAR output .variant_function if --variant_info is specified
    INFO: Using primary reference genome hg18 of the project.
    Getting existing variants: 100% [==================================] 288 206.3K/s in 00:00:00
    INFO: Updating variants from cache/annovar_input.variant_function (1/1)
    annovar_input.variant_function: 100% [==============================] 288 20.8K/s in 00:00:00
    INFO: Fields region_type, region_name of 288 variants are updated
    INFO: Running vtools update variant --from_file cache/annovar_input.variant_function --format ANNOVAR_variant_function --var_info region_type, region_name
    INFO: Executing ANNOVAR.geneanno_50: Importing results from ANNOVAR output .exonic_variant_function if --exonic_info is specified
    INFO: Using primary reference genome hg18 of the project.
    Getting existing variants: 100% [==================================] 288 160.6K/s in 00:00:00
    INFO: Updating variants from cache/annovar_input.exonic_variant_function (1/1)
    annovar_input.exonic_variant_function: 0 0.0/s in 00:00:00                                   
    INFO: Fields mut_type, function of 0 variants are updated
    INFO: Running vtools update variant --from_file cache/annovar_input.exonic_variant_function --format ANNOVAR_exonic_variant_function --var_info mut_type, function
    



#### 8.5 Snapshots

Save a snapshot of the project 



    \\( vtools admin --save_snapshot ACM-BCB2014-tutorial.tgz 'Tutorial section for AVM BCB meeting'
    

    ACM-BCB2014-tutorial.tgz: 100% [================================] 358,722 13.6M/s in 00:00:00
    INFO: Snapshot ACM-BCB2014-tutorial.tgz has been saved
    

You can load it using command 



    \\( vtools admin --load_snapshot ACM-BCB2014-tutorial.tgz 
    

    Extracting ACM-BCB2014-tutorial.tgz:   0.0% [>                                 ]  in 00:00:00
    Extracting ACM-BCB2014-tutorial.tgz: 100% [=======================] 74,928 4.5M/s in 00:00:00
    INFO: Snapshot ACM-BCB2014-tutorial.tgz has been loaded
    

It is strongly recommended that you save copies of your project (snapshots) during the analysis of real-world projects.

 [1]:    /documentation/tutorials/acm-bcb/ACM-BCB2014-tutorial-data.tgz
