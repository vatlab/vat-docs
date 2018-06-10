+++
title = "Subprojects"
weight = 16
hidden = true
+++




## Use of subprojects to manage large project -- a tutorial




### 1. Data

This tutorial uses the same data (whole genome-sequencing data for 44 cases, with SNV and indel data in separate files, and 200 exome controls) as [this tutorial][1], but demonstrates the uses of subproject to import and analyze data. Performance data is collected on a Mac Workstation with 2x2.26G Quad-Core Xeon processor with 8G RAM, using variant tools v1.0rc2. 



### 2. Create subprojects for groups of data

Importing indel data in a project named indel. Because we would like to use hg19 as the primary reference genome, we first import data in hg18, and run the liftover tool to add alternative coordinates in hg19. The `--flip` option flips the primary and alternative reference genomes and make hg19 the primary. 



It takes 3hr 30min to import 44 vcf files. 

    mkdir SNV
    cd SNV
    vtools init SNV 
    vtools import ../../data/hg18/*.vcf --build hg18
    vtools liftover hg19 --flip
    

We use another project for indel data: 



It takes 1hr 30min to import 44 indel files 

    cd ..
    mkdir indel
    cd indel
    vtools init indel
    vtools import ../../data/indel/*.indel --format pileup_indel --build hg18
    vtools liftover hg19 --flip
    

Import control data and add hg18 as alternative reference genome. 



It takes 15min to import 200 exome vcf files 

    cd ..
    mkdir ctrl
    cd ctrl
    vtools init ctrl
    vtools import ../../data/Ctrl/*.vcf --build hg19
    vtools liftover hg18
    



### 3. Create a master project from subprojects

We can then merge the subprojects into one large project: 



It takes 37min to merge 18M variants from three projects, peak memory usages is 5.3G 

    cd ..
    mkdir main
    cd main
    vtools init main --children ../indel ../SNV ../ctrl
    



### 4. Creating a subproject for each sample

If you have a large number of samples, and plenty of CPU and disk space to spare, it can be a good idea to 'pre-process' your samples by creating subprojects for groups of samples, because merging subprojects are generally faster than importing raw data. 

For example, perhaps on a cluster system, you can do, for each `$sample_name`, 



    mkdir ${sample_name}_hg18
    cd ${sample_name}_hg18
    vtools init $sample_name
    vtools import ../data/hg18/$sample_name.vcf --build hg18
    

Then, for 44 samples, we can merge it using commands 



This command takes 40min to complete. 

    mkdir SNV
    cd SNV
    vtools init SNV --children ../*_hg18
    

We can not merge this project to the main project because its primary reference genome is hg18, because we need to lift over our data from hg18 to hg19, and make hg19 the primary reference genome, we have to run 



    vtools liftover hg19 --flip
    



### 5. Create a subproject with part of the variants

If for a project that you are only interested in variants on chromosome 5, you can create a subproject from the main project with variants only on chromosome 5. To do that, you will need to first create a variant table with these variants: 

this takes 13s 

    vtools select variant 'chr="5"' -t chr5
    

Then, you can create another project using `main` as the parent project: 



This command takes 9 min to execute. 

    cd ..
    mkdir chr5
    cd chr5
    vtools init chr5 --parent ../main --variants chr5

 [1]:    /documentation/tutorials/case44ctrl20/
