+++
title = "transmission"
description = ""
weight = 3
+++


# Identification of recessive and de novo variants for family-based design 


This pipeline is an extension to command `vtools_report transmission`, the differences are 



*   `vtools_report transmission` find recessive and de novo mutations and create variant tables for each offspring. This pipeline assumes the first offspring is the affected one and remove de novo and recessive variants of the second offspring from the list. It creates a single variant table for the results. 

*   This pipeline creates a bunch of variant tables for variants that are in different annotation databases. 



## Usage

    % vtools show pipeline transmission
    

    Pipelines to detect different types of variants that are transmitted from parents to offspring.
    
    Available pipelines: denovo, recessive
    
    Pipeline "denovo":  This pipeline identifies de novo mutations from a family of unaffected parents,
    affected offspring, and optional unaffected siblings. It can be applied either to the current project
    (no --input is specified), or a snapshot (--input) for which the snapshot will be loaded and
    overwrite the existing project. The parameter --parents and --offspring are required to specify the
    name of parents, proband (affected offspring), and one optional sibling. Parameter --name is
    recommended to give all variant tables a prefix. This pipeline will produce tables $name_denovo
    (variants that are observed only in the proband), A table $name_denovo_SNP will be created with all
    SNP markers in table $name_denovo. And, depending on values of parameter --databases, it can produce
    tables $table_1kg for variants in 1000 genomes project, $table_dbSNP for variants in dbSNP project,
    and $table_refGene, $table_refGene_exon, $table_ccdsGene, $table_ccdsGene_exon,
    $table_CancerGenomeCensus, $table_COSMIC, $table_dbNSFP, $table_phastCons, $table_phastConsElements,
    $table_genomicSuperDups for tables in respective annotation databases. It is up to you to select
    variants based on these membership tables using the 'vtools compare' command.  The project will be
    saved to a snapshot if a name (or filename with extension .tar or .tar.gz) is specified as the
    output.
      denovo_0:           Load specified snapshot if a snapshot is specified. Otherwise use the existing
                          project.
      denovo_5:           Check the version of variant tools (version 2.2.1 and above is required to
                          execute this pipeline)
      denovo_10:          Import all annotation databases
      denovo_20:          Locate de novo variants of the proband
      denovo_50:          Create variant tables according to their membership in different annotation
                          databases
      denovo_100:         Save the project to a snapshot if an output is specified.
      denovo_200:         Summarize the results.
    
    Pipeline "recessive":  This pipeline identifies recessive mutations from a family of unaffected
    parents, affected offspring, and optional unaffected siblings. Recessive variant is defined as
    variants that are homozygous in the affected offspring (proband), heterozygous in both parents, and
    heterozygous or wildtype in a sibling (if available). The pipeline can be applied either to the
    current project (no --input is specified), or a snapshot (--input) for which the snapshot will be
    loaded and overwrite the existing project. The parameter --parents and --offspring are required to
    specify the name of parents, proband (affected offspring), and one optional sibling. Parameter --name
    is recommended to give all variant tables a prefix. This pipeline will produce tables $name_recessive
    (variants that are observed only in the proband). A table $name_denovo_SNP will be created with all
    SNP markers in table $name_denovo. And, depending on values of parameter --databases, it can produce
    tables $table_1kg for variants in 1000 genomes project, $table_dbSNP for variants in dbSNP project,
    and $table_refGene, $table_refGene_exon, $table_ccdsGene, $table_ccdsGene_exon,
    $table_CancerGenomeCensus, $table_COSMIC, $table_dbNSFP, $table_phastCons, $table_phastConsElements,
    $table_genomicSuperDups for tables in respective annotation databases. It is up to you to select
    variants based on these membership tables using the 'vtools compare' command.  Two optional output
    files are allowed. The project will be saved to a snapshot if a name (or filename with extension .tar
    or .tar.gz) is specified as the output.
      recessive_0:        Load specified snapshot if a snapshot is specified. Otherwise use the existing
                          project.
      recessive_5:        Check the version of variant tools (version 2.2.1 and above is required to
                          execute this pipeline)
      recessive_10:       Import all annotation databases
      recessive_20:       Locate recessive variants of the proband (homozygous only in proband) and save
                          variants in table $name_recessive
      recessive_50:       Create variant tables according to their membership in different annotation
                          databases
      recessive_100:      Save the project to a snapshot if an output is specified.
      recessive_200:      Summarize the results.
    
    Pipeline parameters:
      parents
      offspring
      name                Name of the family. All generated tables will be prefixed with this name.
                          (default: family)
      databases           Databases for which membership tables will be produced. (default: thousandGenom
                          es,dbSNP,refGene,ccdsGene,refGene_exon,ccdsGene_exon,CosmicCodingMuts,CosmicNon
                          CodingVariants,dbNSFP,phastCons,phastConsElements,genomicSuperDups)
    



## Details

### Identification of de novo variants in a family with affected offspring

This pipeline executes a series of vtools commands to identify de novo variants in a family with affected offsprng, unaffected parents, and an optional unaffected sibling. 

The pipeline either applies to the existing project, or load a snapshot if a snapshot is specified using parameter `--input`. For a project with two unaffected parents, affected offspring (proband), and an optional sibling, this pipeline 



1.  identify variants for each sample 
2.  identify variants that appear only in the affected offspring, save it to a variant table `$name_denovo` 
3.  identify a subset of variants that have no other parental variants at the variant sites, save it to table `$name_denovo_site` 
4.  identify variants that belong to a number of annotation databases and save them to their respective variant tables. 

The pipeline writes a summary of tables created to the standard output, and save the project to a snapshot if a name or filename is assigned to parameter `--output`. 

For example, the following command 



    % vtools execute transmission denovo --input poly_data.tar \
      --parents WGS3_2 WGS3_3 --offspring WGS3_1  --output denovo.tar \
      > logfile
    

produces a log file 



    % cat logfile
    

    SUMMARY: Identification of de novo variants for family family
    
    Members: WGS3_2 WGS3_3 (unaffected parents), WGS3_1 (affected offspring)
    
    Number of genotypes:
    WGS3_2 : 4367814 
    WGS3_3 : 4455890
    WGS3_1 : 4343418
    
    de novo variants:
    family_denovo : 113553 (de novo variants for family family )
    family_denovo_SNP: 63578 (de novo SNP variants for family family )
    
    Database membership:
    family_denovo_in_thousandGenomes: 18330 (de novo variants in database thousandGenomes)
    family_denovo_in_dbSNP: 71921 (de novo variants in database dbSNP)
    family_denovo_in_refGene: 40037 (de novo variants in database refGene)
    family_denovo_in_ccdsGene: 28427 (de novo variants in database ccdsGene)
    family_denovo_in_refGene_exon: 1099 (de novo variants in database refGene_exon)
    family_denovo_in_ccdsGene_exon: 235 (de novo variants in database ccdsGene_exon)
    family_denovo_in_CosmicCodingMuts: 73 (de novo variants in database CosmicCodingMuts)
    family_denovo_in_CosmicNonCodingVariants: 111 (de novo variants in database CosmicNonCodingVariants)
    family_denovo_in_dbNSFP: 148 (de novo variants in database dbNSFP)
    family_denovo_in_phastCons: 101916 (de novo variants in database phastCons)
    family_denovo_in_phastConsElements: 3502 (de novo variants in database phastConsElements)
    family_denovo_in_genomicSuperDups: 24836 (de novo variants in database genomicSuperDups)
    



### Identification of recessive variants in a family with affected offspring

This pipeline works similarly to the `denovo` pipeline (with the same input, output and other options), but tried to identify variants that are recessive in the affected offspring, heterozygous in parents, and wildtype or heterozygous in the unaffected sibling, if available. 



Variants on sex chromosomes are handled in the same way as variants on autosomes. There must be some genotyping error if you observe recessive variants on chromosome Y. If you observe recessive variants on chromosome X, it means the variant is heterozygous for mother, and exists in father. 



### What is next?

The pipelines identify recessive or de novo variants and create a bunch of tables. You usually should filter the list more using combination of memberships, quality scores, and other information. For example, if you are looking for novel variants that are not in 1000 genomes, in exon regions, with high conservation score, not in genomic duplication regions, you can select the variants using command 



    % vtools compare --expression 'mylist=family_denovo - family_denovo_in_thousandGenomes - \
        (family_denovo - (family_denovo_in_refGene_exon | family_denovo_phastConsElements)) - \
        family_denovo_genomicSuperDups'
    

and start looking closely at these variants, using commands such as 



    % vtools output mylist chr pos ref alt 'ref_sequence(chr, pos, pos+20)' "track('mydata.bam', 'reads')"