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
    

    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project quickstart
    


### 3. Import an example data set


You could first download the sample project as a snapshot using command 

    % vtools admin --load_snapshot vt_quickStartGuide_v3

    
You can then import data into your `quickstart` project. These example VCFs contain variants for the CEU and JPT populations from the 1000 Genomes project. 

 
    % vtools import CEU_hg38_all.vcf --build hg38 --sample_name CEU
    

    Getting existing variants: 100% [========================] 292 245.2K/s in 00:00:00
    INFO: Importing variants from CEU_hg38_all.vcf (1/1)
    CEU_hg38_all.vcf: 100% [=================================] 3,512 6.8K/s in 00:00:00
    INFO: 3,470 new variants (3,470 SNVs, 31 unsupported) from 3,512 lines are imported.
    WARNING: No genotype column could be found from the input file. Assuming no genotype.
    Importing genotypes: 100% [=============================] 3,470 13.5K/s in 00:00:00
    



    % vtools import JPT_hg38_all.vcf --build hg38 --sample_name JPT
    

    Getting existing variants: 100% [======================] 3,762 380.9K/s in 00:00:00
    INFO: Importing variants from JPT_hg38_all.vcf (1/1)
    JPT_hg38_all.vcf: 100% [================================] 2,920 15.9K/s in 00:00:00
    INFO: 1,369 new variants (1,369 SNVs, 31 unsupported) from 2,920 lines are imported.
    WARNING: No genotype column could be found from the input file. Assuming no genotype.
    Importing genotypes: 100% [==============================] 1,369 4.7K/s in 00:00:00

    


{{% notice tip %}}
These two files do not have any sample names associated with them. We however give each file a sample name so that we can track the source of variants (CEU vs JPT). If you do not need to track variant membership, you can import the two files using a single command `vtools import *.vcf.gz --build hg19`. 
{{% /notice %}}
    



### 4. Annotate your variants

To annotate variants, you first need to download annotation sources. For more details see the [documentation][2][?][2] page. For this quick start, we will annotate variants to transcripts (CCDS IDs) and KEGG pathways. These first 2 `vtools use` commands downloads 2 annotation sources. 

This command downloads the **ccdsGene** data source allowing variants to be annotated to transcripts. 



    % vtools use ccdsGene
    

    INFO: Choosing version ccdsGene-hg38_20171008 from 4 available databases.
    INFO: Downloading annotation database annoDB/ccdsGene-hg38_20171008.ann
    INFO: /Users/jma7/.variant_tools/annoDB/ccdsGene-hg38_20171008.DB: MD5 signature mismatch, the database might have been upgraded locally.
    INFO: Using annotation DB ccdsGene as ccdsGene in project quickstart.
    INFO: High-confidence human gene annotations from the Consensus Coding Sequence (CCDS) project.
        

    This command downloads the **keggPathway** annotation source allowing variants to be annotated to KEGG pathways indirectly through transcript annotations (provided by the **ccdsGene** annotation source). 



    % vtools use keggPathway --linked_by ccdsGene.name
    

    INFO: Choosing version keggPathway-20110823 from 1 available databases.
    INFO: Downloading annotation database annoDB/keggPathway-20110823.ann
    INFO: Using annotation DB keggPathway as keggPathway in project quickstart.
    INFO: kegg pathway for CCDS genes
    INFO: 6745 out of 32508 ccdsGene.ccdsGene.name are annotated through annotation database keggPathway
    WARNING: 204 out of 6949 values in annotation database keggPathway are not linked to the project.
    

Now lets filter all of our variants to include only those involved in metabolic pathways. This command uses the pathway annotation source that we just downloaded to find all variants that are on transcripts of proteins known to be involved in metabolic pathways. These variants are then stored in a table called `metabolic`. 



    % vtools select variant 'kgDesc="Metabolic pathways"' -t metabolic                                                                                     
    

    Running: 54 1.2K/s in 00:00:00
    INFO: 280 variants selected.
    

Now lets create a table of the metabolic pathway variants that are seen in the CEU population. 



    % vtools select metabolic --samples "sample_name='CEU'" -t metabolic_CEU
    

    Running: 3 592.3/s in 00:00:00                                                                              
    INFO: 197 variants selected.
    

Lets to the same for the JPT population 



    % vtools select metabolic --samples "sample_name='JPT'" -t metabolic_JPT
    

    Running: 2 453.6/s in 00:00:00                                                  
    INFO: 168 variants selected.
    


### 5. Basic analysis of variants

The `vtools sample_stat` command and `vtools_report`s provide analysis capabilities that use sample genotypes. In our current data set we don't have genotypes but you can see examples of these types of analyses in our tutorials in the [documentation][2][?][2]. Here we will show a simple `compare` command. This identifies which of the metabolic pathway variants are seen in the CEU population but are not seen in the JPT population. 



    % vtools compare metabolic_CEU metabolic_JPT --difference unique_CEU_metabolic
    

    INFO: Reading 197 variants in metabolic_CEU...
    INFO: Reading 168 variants in metabolic_JPT...
    Writing to unique_CEU_metabolic: 100% [===================] 112 14.4K/s in 00:00:00
    112



### 6. Export reports

Report of **metabolic pathway variants unique to the CEU population** (when analyzed with the JPT population). 



    % vtools output unique_CEU_metabolic chr pos ref alt ccdsGene.name kgDesc > unique_CEU_metabolic_variants.txt
    

    1   26022754    C   T   CCDS271.1   Metabolic pathways
    1   43899601    C   T   CCDS492.1   Metabolic pathways
    1   43899619    C   T   CCDS492.1   Metabolic pathways
    1   76412118    C   T   CCDS672.1   Metabolic pathways
    1   76628653    T   C   CCDS672.1   Metabolic pathways
    1   109628106   G   A   CCDS30796.1 Metabolic pathways
    1   109628244   C   T   CCDS30796.1 Metabolic pathways
    1   109628739   C   T   CCDS30796.1 Metabolic pathways
    1   119422310   T   C   CCDS902.1   Metabolic pathways
    1   162566204   A   G   CCDS1240.1  Metabolic pathways
    ...
    

Simple report to list **all CEU and JPT variants involved in metabolic pathways**. 



    % vtools output metabolic chr pos ref alt ccdsGene.name kgDesc > metabolic_variants.txt
    

    1   26022754    C   T   CCDS271.1   Metabolic pathways
    1   26031165    C   A   CCDS271.1   Metabolic pathways
    1   26031176    G   A   CCDS271.1   Metabolic pathways
    1   43824858    A   G   CCDS492.1   Metabolic pathways
    1   43899601    C   T   CCDS492.1   Metabolic pathways
    1   43899619    C   T   CCDS492.1   Metabolic pathways
    1   76412118    C   T   CCDS672.1   Metabolic pathways
    1   76627495    C   A   CCDS672.1   Metabolic pathways
    1   76628653    T   C   CCDS672.1   Metabolic pathways
    ...
    

The example here was very simplistic using only 2 samples and the VCFs did not have genotype information within them. But hopefully this gives you a feel for how the software works. For more involved tutorials and details of `vtools` capabilities, please see our [documentation][2].


 [2]:    /documentation/tutorials/
 [3]:  /installation/
