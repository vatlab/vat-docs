
+++
title = "Illumnina"
description = ""
weight = 4
+++


# Pipelines to assist the analysis of illumina data



## Usage

    $ vtools show pipeline illumina
    

    A pipeline to handle illumina data prepared by CASAVA 1.8+. It imports
    variants from SNPs.vcf and Indel.vcf of multiple samples, separate maxgt and
    poly into different projects, calculate a few standard statistics and apply a
    few filters. All results are saved as variant tools snapshots. This pipeline
    uses command vtools so multi-processing is not supported.
    
    Available pipelines: load_data
    
    Pipeline "load_data":  This pipeline accepts a list of directories under which
    SNPs and Indels are listed in files Variations/SNPs.vcf and
    Variations/Indels.vcf. It reads all variants and save the project to a
    snapshot with raw data. It then removes MAXGT or POLY samples, rename samples,
    merge SNP and Indels remove variants without any genotype in all samples,
    create variant tables (all, SNVs and Indels) for each sample, and save results
    to two other snapshots for maxgt and poly data respectively.
      load_data_10:       Load SNP and Indel variants from Variations/SNPs.vcf and
                          Variations/Indels.vcf under specified directory. Save
                          all inputted variants to the first snapshot file
                          specified by --output
      load_data_20:       Remove _POLY samples, merge SNPs and INDELs, remove
                          genotypes that does not pass filter (filter != "PASS"),
                          calculate genotype count of all variants, remove
                          variants without any genotype, and save results to the
                          second  snapshot file specified by --output
      load_data_30:       Remove _POLY samples, merge SNPs and INDELs, remove
                          genotypes that does not pass filter (filter != "PASS"),
                          calculate genotype count of all variants, remove
                          variants without any genotype, and save results to the
                          second  snapshot file specified by --output
    
    Pipeline parameters:
      geno_info           Genotype information fields imported from VCF
                          files (default: filter qual DP_geno GQ_geno
                          PL_geno)
      build               Build of reference genome of the project.
                          (default: hg19)
    
    



## Details

(:toggleexample Examples: Import illumina data:) 

    $ vtools init test --force
    $ vtools execute illumina load_data --input /path/to/data/LP* \
       --output raw_data.tar maxgt_data.tar poly_data.tar
    

(:exampleend:)