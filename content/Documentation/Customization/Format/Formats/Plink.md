+++
title = "plink"
weight = 3
+++

## Import variants and sample genotypes from PLINK format


### Introduction

`PLINK` is a widely used program for analyzing genotypic data for Genome-wide Association Studies (GWAS). It can be considered as standard input format for genotyping array data. An intermediate type of genetic data between genotyping arrays and exome sequencing is the exome genotyping array, or **exome chip**. Unlike its GWAS counterpart which focuses on relatively common variants, exome chips contain primarily non-singleton *coding* variants seen in existing whole genome and exome sequencing data, plus a small proportion of non-protein-altering variants such as GWAS tag SNPs, ancestry informative markers, etc. Since exome chips are essentially genotyping arrays, they are often distributed in `PLINK` data format. Variant tools can thus handle exome chip input and perform rare variants association analysis for exome chip samples. 

The standard `PLINK` files can be a bundle of plain text files (PED & MAP dataset, or its transpose, TPED & FAM dataset), or a bundle of binary files (BED, BIM & FAM). `PLINK` provides commands to convert between text and binary formats. Since `PLINK` files do not specify for a variant which allele is reference and which is alternative, importing data to a variant tools project requires matching each variant to the reference sequence to determine reference and alternative alleles; complementary strand will be used when necessary. Variant tools performs the matching procedure against hg18 or hg19 reference genomes. Other reference genome builds are not supported. 



Currently only `PLINK` binary format (BED, BIM & FAM) is valid input. You need to use `PLINK` to convert text to binary format if necessary. 



A variant locus will be ignored if it is not polymorphic in input data. 

## Format specification

    vtools show format plink
    

    Format:      plink
    
    Description: Input format for PLINK dataset. Currently only PLINK binary PED file
      is supported (*.bed, *.bim & *.fam)
    
    Preprocessor: PlinkConverter($build)
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr          Chromosome
      pos          1-based Position of the snp
      ref          Reference allele
      alt          Alternative allele
    
    Genotype:
      GT           Gentoype coded as 0 (ref ref), 1 (ref alt) and 2 (alt alt)
    
    No configurable parameter is defined for this format.
    

As with other `vtools import` formats, importing `PLINK` data requires specification of format file (`--format`) and input data. Unlike with other formats, however, input filename for `PLINK` binary data is the base file name without extension. For example if you have `X.bed`, `X.bim` and `X.fam` files then the import command should be 



    vtools import /path/to/X --format plink --build hg19 --jobs $N
    

    INFO: Preprocessing files X to generate intermediate input files for import
    INFO: Determining major/minor allele from data
    Decoding X: 100% [===============================] 149,141 9.1K/s in 00:00:16
    INFO: Importing variants from cache/X.plink (1/1)
    X.plink: 100% [========================] 162,433 49.3K/s in 00:00:03
    INFO: 149,141 new variants (149,141 SNVs) from 149,142 lines are imported.
    Importing genotypes: 100% [======================] 668,901,870 630.4K/s in 00:17:41
    Copying genotype: 100% [========================] 4,485 194.8/s in 00:00:23
