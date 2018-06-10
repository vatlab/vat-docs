+++
title = "Quick start"
weight = 1
hidden = true
+++


## Quick Start Guide


*variant tools* is a software toolset that facilitates the import, annotation and analysis of your variants. This 10-minute quick start guide steps you through a minimal real-world data set so that you can get a feel for the software and assess its helpfulness. For demonstrations on more real-world data analysis, please refer to the software [tutorials][2]


### 1. Installation

Required software: 

*   Python 2.7.2 or higher or Python 3.2 or higher 

Download the [current release][3] of vtools, extract the archive and install the software. 



    % tar -xvzf variant_tools-VERSION.tar.gz
    % cd variant_tools-VERSION
    % sudo python setup.py install
    

If you want to install on a windows system or use Python 3 see the detailed installation instructions [here][3]. 



### 2. Create a project

Create a directory to put all your project files in - lets call it `tutorial`. And then create a `vtools` project called `quickstart`. 



    % mkdir tutorial 
    % cd tutorial
    % vtools init quickstart
    

    INFO: variant tools 1.0.3 : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project quickstart
    



### 3. Import an example data set

Download these example VCF files, put them in your `tutorial` directory and unzip them. 



    ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/release/2010_07/exon/snps/CEU.exon.2010_03.sites.vcf.gz
    ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/pilot_data/release/2010_07/exon/snps/JPT.exon.2010_03.sites.vcf.gz
    

You can then import this data into your `quickstart` project. These example VCFs contain variants for the CEU and JPT populations from the 1000 Genomes project. 



    % vtools import CEU.exon.2010_03.sites.vcf.gz --build hg19 --sample_name CEU
    

    INFO: Importing variants from CEU.exon.2010_03.sites.vcf.gz (1/1)
    CEU.exon.2010_03.sites.vcf.gz: 100% [=======================] 3,500 10.3K/s in 00:00:00
    INFO: 3,489 new variants (3,489 SNVs) from 3,500 lines are imported.
    WARNING: No genotype column could be found from the input file. Assuming no genotype.
    Importing genotypes: 100% [==================================] 3,500 1.7K/s in 00:00:02
    Copying genotype: 100% [=========================================] 1 3.8K/s in 00:00:00
    



    % vtools import JPT.exon.2010_03.sites.vcf.gz --sample_name JPT
    

    INFO: Using primary reference genome hg19 of the project.
    Getting existing variants: 100% [==========================] 3,489 207.8K/s in 00:00:00
    INFO: Importing variants from JPT.exon.2010_03.sites.vcf.gz (1/1)
    JPT.exon.2010_03.sites.vcf.gz: 100% [=======================] 2,911 12.9K/s in 00:00:00
    INFO: 1,369 new variants (1,369 SNVs) from 2,910 lines are imported.
    WARNING: No genotype column could be found from the input file. Assuming no genotype.
    Importing genotypes: 100% [==================================] 2,910 1.5K/s in 00:00:02
    Copying genotype: 100% [=========================================] 1 2.4K/s in 00:00:00
    


{{% notice tip %}}
These two files do not have any sample names associated with them. We however give each file a sample name so that we can track the source of variants (CEU vs JPT). If you do not need to track variant membership, you can import the two files using a single command `vtools import *.vcf.gz --build hg19`. 
{{% /notice %}}

If for some reason you cannot download the source files from NCBI, you could download this sample project as a snapshot using command 



    % vtools admin --load_snapshot vt_quickStartGuide
    

    Downloading snapshot vt_quickStartGuide.tar.gz from online
    vt_quickStartGuide.tar.gz: 100% [============================] 112,837 81.8K/s in 00:00:01 
    INFO: Snapshot vt_quickStartGuide has been loaded
    



### 4. Annotate your variants

To annotate variants, you first need to download annotation sources. For more details see the [documentation][2][?][2] page. For this quick start, we will annotate variants to transcripts (CCDS IDs) and KEGG pathways. These first 2 `vtools use` commands downloads 2 annotation sources. 

This command downloads the **ccdsGene** data source allowing variants to be annotated to transcripts. 



    % vtools use ccdsGene
    

    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/ccdsGene.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/ccdsGene-hg19_20110909.DB.gz
    : Unsupported scheme.
    --18:47:23--  http://vtools.houstonbioinformatics.org/annoDB/ccdsGene-hg19_20110909.DB.gz
               => `./ccdsGene-hg19_20110909.DB.gz'
    Resolving vtools.houstonbioinformatics.org... 70.39.145.13
    Connecting to vtools.houstonbioinformatics.org[70.39.145.13]:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 744,834 [  /applications/x-gzip]
    
    100%[=============================================================================>] 744,834      370.44K/s             
    
    18:47:26 (369.03 KB/s) - `./ccdsGene-hg19_20110909.DB.gz' saved [744834/744834]
    
    
    FINISHED --18:47:26--
    Downloaded: 744,834 bytes in 1 files
    INFO: Using annotation DB ccdsGene in project quickstart.
    INFO: CCDS Genes
    

This command downloads the **keggPathway** annotation source allowing variants to be annotated to KEGG pathways indirectly through transcript annotations (provided by the **ccdsGene** annotation source). 



    % vtools use keggPathway --linked_by ccdsGene.name
    

    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/keggPathway.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/keggPathway-20110823.DB.gz
    : Unsupported scheme.
    --18:54:24--  http://vtools.houstonbioinformatics.org/annoDB/keggPathway-20110823.DB.gz
               => `./keggPathway-20110823.DB.gz'
    Resolving vtools.houstonbioinformatics.org... 70.39.145.13
    Connecting to vtools.houstonbioinformatics.org[70.39.145.13]:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 350,847 [  /applications/x-gzip]
    
    100%[=============================================================================>] 350,847      330.94K/s             
    
    18:54:26 (329.78 KB/s) - `./keggPathway-20110823.DB.gz' saved [350847/350847]
    
    
    FINISHED --18:54:26--
    Downloaded: 350,847 bytes in 1 files
    INFO: Using annotation DB keggPathway in project quickstart.
    INFO: kegg pathway for CCDS genes
    

Now lets filter all of our variants to include only those involved in metabolic pathways. This command uses the pathway annotation source that we just downloaded to find all variants that are on transcripts of proteins known to be involved in metabolic pathways. These variants are then stored in a table called `metabolic`. 



    % vtools select variant 'kgDesc="Metabolic pathways"' -t metabolic                                                                                        
    

    Running: 2,788 2.1K/s in 00:00:01
    INFO: 109 variants selected.
    

Now lets create a table of the metabolic pathway variants that are seen in the CEU population. 



    % vtools select metabolic --samples "sample_name='CEU'" -t metabolic_CEU
    

    INFO: 1 samples are selected by condition: sample_name='CEU'
    Running: 3 488.8/s in 00:00:00                                                                                           
    INFO: 71 variants selected.
    

Lets to the same for the JPT population 



    % vtools select metabolic --samples "sample_name='JPT'" -t metabolic_JPT
    

    INFO: 1 samples are selected by condition: sample_name='JPT'
    Running: 2 330.8/s in 00:00:00                                                                                           
    INFO: 67 variants selected.
    



### 5. Basic analysis of variants

The `vtools sample_stat` command and `vtools_report`s provide analysis capabilities that use sample genotypes. In our current data set we don't have genotypes but you can see examples of these types of analyses in our tutorials in the [documentation][2][?][2]. Here we will show a simple `compare` command. This identifies which of the metabolic pathway variants are seen in the CEU population but are not seen in the JPT population. 



    % vtools compare metabolic_CEU metabolic_JPT --difference unique_CEU_metabolic
    

    INFO: Reading 71 variants in metabolic_CEU...
    INFO: Reading 67 variants in metabolic_JPT...
    Writing to unique_CEU_metabolic: 100.0% [=======================================================>] 42 3.5K/s in 00:00:00
    



### 6. Export reports

Report of **metabolic pathway variants unique to the CEU population** (when analyzed with the JPT population). 



    % vtools output unique_CEU_metabolic chr pos ref alt ccdsGene.name kgDesc > unique_CEU_metabolic_variants.txt
    

    1	76650391	C	T	CCDS672.1	Glycosphingolipid biosynthesis - ganglio series
    1	76650391	C	T	CCDS672.1	Metabolic pathways
    1	76866926	T	C	CCDS672.1	Glycosphingolipid biosynthesis - ganglio series
    1	76866926	T	C	CCDS672.1	Metabolic pathways
    2	154866325	A	G	CCDS2199.1	O-Glycan biosynthesis
    2	154866325	A	G	CCDS2199.1	Metabolic pathways
    2	154960831	C	T	CCDS2199.1	O-Glycan biosynthesis
    2	154960831	C	T	CCDS2199.1	Metabolic pathways
    2	158120947	T	G	CCDS2203.1	O-Glycan biosynthesis
    ...
    

Simple report to list **all CEU and JPT variants involved in metabolic pathways**. 



    % vtools output metabolic chr pos ref alt ccdsGene.name kgDesc > metabolic_variants.txt
    

    1	20916748	A	G	CCDS210.1	Pyrimidine metabolism
    1	20916748	A	G	CCDS210.1	Drug metabolism - other enzymes
    1	20916748	A	G	CCDS210.1	Metabolic pathways
    1	76650391	C	T	CCDS672.1	Glycosphingolipid biosynthesis - ganglio series
    1	76650391	C	T	CCDS672.1	Metabolic pathways
    1	76865768	C	A	CCDS672.1	Glycosphingolipid biosynthesis - ganglio series
    1	76865768	C	A	CCDS672.1	Metabolic pathways
    1	76866926	T	C	CCDS672.1	Glycosphingolipid biosynthesis - ganglio series
    1	76866926	T	C	CCDS672.1	Metabolic pathways
    ...
    

The example here was very simplistic using only 2 samples and the VCFs did not have genotype information within them. But hopefully this gives you a feel for how the software works. For more involved tutorials and details of `vtools` capabilities, please see our [documentation][2].


 [2]:    /documentation/tutorials/
 [3]:  installation
