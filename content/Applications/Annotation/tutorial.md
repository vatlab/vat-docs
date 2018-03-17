

+++
title = "Tutorial"
description = ""
weight = 2
+++


# Annotating variants using multiple annotation databases, a tutorial 



## Getting annotation databases

This tutorial demonstrates how to use various databases to annotate variants in a variant tools project. These databases will be automatically downloaded and saved in directory `~/.variant_tools` when they are used in a project. The amount of time required to download these databases depends on the speed of your internet connection, server load, and size of the databases. If you do no want to wait for the downloads and if you have enough disk space, you can download all variant tools resources into your local resource directory using the following commands: 



    % wget --mirror http://vtools.houstonbioinformatics.org
    % rm -rf ~/.variant_tools   # remove existing directory if exists
    % mv vtools.houstonbioinformatics.org ~/.variant_tools
    

The amount of data to download is 29G as of October 2012, and is expected to grow over time. The `--mirror` option allows command `wget` to get all files recursively, skipping files that exist locally. 



## Download a snapshot project with some variants

Let us create a project and download a snapshot project called `vt_quickStartGuide`. 



    % vtools init anno
    

    INFO: variant tools 2.0.0 : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project anno
    



    % vtools admin --load_snapshot vt_quickStartGuide
    

    Downloading snapshot vt_quickStartGuide.tar.gz from online
    INFO: Snapshot vt_quickStartGuide has been loaded
    

This project has variants from CEU and JPT populations of the 1000 genomes pilot study. As we can see from the following commands, it has 4,858 variants from two samples: 



    % vtools show samples
    

    sample_name	filename
    CEU	CEU.exon...3.sites.vcf.gz
    JPT	JPT.exon...3.sites.vcf.gz
    



    % vtools show tables
    

    table                 #variants     date  message
    variant                   4,858   
    



## Annotating variants

### Listing available annotation databases

These are available annotation databases (as of October 2012) that can be downloaded and used automatically to annotate variants within a *variant tools* project. You can use the following command to list currently available databases. 



    % vtools show annotations
    

    CancerGeneCensus-20111215
    CancerGeneCensus
    ccdsGene-hg19_20110909
    ccdsGene-hg19_20111206
    ccdsGene
    ccdsGene_exon-hg19_20110909
    ccdsGene_exon-hg19_20111206
    ccdsGene_exon
    dbNSFP-hg18_hg19_1.1_2
    dbNSFP
    dbNSFP_light-hg18_hg19_1.0_0
    dbNSFP_light
    dbSNP-hg18_129
    dbSNP-hg18_130
    dbSNP-hg19_131
    dbSNP-hg19_132
    dbSNP
    evs-hg19_20111107
    evs
    evs_5400
    keggPathway-20110823
    keggPathway
    knownGene-hg18_20110909
    knownGene-hg19_20110909
    knownGene
    knownGene_exon-hg18_20110909
    knownGene_exon-hg19_20110909
    knownGene_exon
    phastCons-hg19_20110909
    phastCons
    refGene-hg18_20110909
    refGene-hg19_20110909
    refGene
    refGene_exon-hg18_20110909
    refGene_exon-hg19_20110909
    refGene_exon
    thousandGenomes-hg19_20110909
    thousandGenomes
    



### How do I add an annotation database to my project?

To add a gene-based annotation source such as **ccdsGene** to your project, the following command will accomplish this. If you haven't already downloaded this annotation database with this or another project, vtools will automatically download the database and associate **ccdsGene** annotations to your project. 



    % vtools use ccdsGene
    



### What genes do my variants belong to?

There are several annotation sources that could be used to annotate your variants to gene transcripts. Some examples include **refGene**, **knownGene** and **ccdsGene**. To get more details of these databases use `vtools show annotation ccdsGene -v2` (or a similar command with refGene or knownGene) as described previously. This command downloads the **ccdsGene** data source allowing variants to be annotated to transcripts. 



### What about the exon?

Gene-based annotation sources such as **ccdsGene**, **refGene** and **knownGene** have corresponding annotation sources that are exon-based: **ccdsGene_exon**, **refGene_exon** and **knownGene_exon** respectively (provided indirectly through the UCSC Genome Browser database). These exon-based annotation sources contain exon start and end coordinates that are used in lieu of gene start and end coordinates for linking the annotations to your variants. 



    % vtools use ccdsGene_exon
    



### What pathways do my variants belong to? 

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
    Length: 350,847 [application/x-gzip]
    
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