+++
title = "1000 genomes"
weight = 8
hidden = true
+++

## Import all genotype data from the 1000 genome project

The genotype data for all 60 samples from consists of 23 `.vcf.gz` files with a total of 142G. Because of the size of data, it can be slow to import all these files into *variant tools*. Depending on your computing environment, you can 



### 1. Import all files together

The most straightforward method is to import all files together: 



    mkdir p1000g_all
    cd p1000g_all
    vtools init p1000g_all
    vtools admin --set_runtime_option "temp_dir=/Volumes/AnotherDisk/tmp/p1000g_all"
    vtools admin --set_runtime_option 'sqlite_pragma=synchronous=OFF,journal_mode=MEMORY'
    vtools import /path/to/ALL.chr*.vcf.gz -j8 --build hg19
    vtools admin --merge_samples
    

Command `vtools admin --merge_samples` is needed because genotypes for these samples are imported chromosome by chromosome, and appear as multiple samples with same names. 



### 2. Import data chromosome by chromosome into subprojects

If you have a cluster system to spread the workload, you could create multiple projects and import genotypes chromosome by chromosome. That is to say, for chromosome 1, ..., 22 and X, you can create bash scripts such as 



    chr=1
    mkdir p1000g_$chr
    cd p1000g_$chr
    vtools init p1000g_$chr -f
    vtools admin --set_runtime_option "temp_dir=/Volumes/AnotherDisk/tmp/p1000g_$chr"
    vtools admin --set_runtime_option 'sqlite_pragma=synchronous=OFF,journal_mode=MEMORY'
    vtools import /path/to/ALL.chr${chr}.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz -j4 --build hg19
    

After all jobs are completed, you can merge the projects using command. The project and sample merge steps can be slow (about 1 day), but this method leaves 23 subprojects, which are much smaller than the master project and can be useful if you are only interested in data on a particular chromosome. 



    mkdir p1000g_merged
    cd p1000g_merged
    vtools init p1000g_merged --children ../p1000g_* -j8
    vtools admin --merge_samples
    



### 3. Merge vcf files before importing

To avoid merging samples, you could merge the vcf files using vcftools before importing them 



    mkdir p1000g_single
    cd p1000g_single
    vcf-concat /path/to/ALL.chr*.vcf.gz > ALL.vcf
    vtools admin --set_runtime_option "temp_dir=/Volumes/AnotherDisk/tmp/p1000g_all"
    vtools admin --set_runtime_option 'sqlite_pragma=synchronous=OFF,journal_mode=MEMORY'
    vtools import ALL.vcf -j8 --build hg19
    

This appears to be the most efficient method to import this dataset.
