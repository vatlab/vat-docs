+++
title = "Performance"
weight = 3
hidden = true
+++


## Processing 44 whole genome cases and 200 exome controls 

### 1. Data source

Whole genome-sequencing data for 44 cases, with SNV and indel data in separate files, and 200 exome controls. This tutorial demonstrates the same set of commands used in the [home page presentation][1] but uses the complete dataset. The dataset used in this tutorial is not publicly available. 



### 2. Import data


Create a project 
    
    # Performance data is collected on a Mac Workstation with 2x2.26G Quad-Core Xeon processor with 8G RAM, using variant tools v1.0rc1.
    % vtools init RA 

    
Import control data in hg19. The presentation imports case data (hg18) first, but as discussed [here][2], it is better to use newer reference genome as the primary reference genome. 

    
    # It takes 15min to import a total of 12.8M variants (3M unique) and 12M genotypes. 
    % vtools import ../data/Ctrl/*.vcf --build hg19 --geno safe_GT
    

Here we use option `--geno safe_GT` because the data does not follow VCF format specification and do not put genotype as the first FORMAT field. 

Importing case data from 44 VCF files. Because the case data use a different reference genome, an alternative reference genome (hg18) is added to the project. Existing variants and new variants are mapped to hg18 and hg19, respectively, so that all variants have coordinates in both reference genomes (except for those that cannot be mapped). 



    # It takes 3hr 30min (3hr with `--jobs 2`) to import 161M variants (11M new distinct ones), 161M genotypes. Peak memory usage is 2.7G. 
    % vtools import ../data/hg18/*.vcf --build hg18
    

The indel data are stored in separate files in pileup format. They are imported using the alternative reference genome (hg18) and are mapped to hg19 afterwards. 



    # It takes 1hr 30min to import 36M variants (4.6M new), 36M genotypes. Peak memory usage is 3.8G. 
    % vtools import ../data/indel/*.indel --format pileup_indel --build hg18
    

After all three sets of data are imported, the project 

*   has 18M variants, including 1.8M insertions and 2.9M deletions 
*   has 210M genotypes in 288 samples (in variant tools term, because SNVs and INDELs of cases are stored separately) 
*   takes 4.2G diskspace (RA.proj: 1.25G, RA_genotype.DB: 2.92G) 

{{% notice tip %}}
If you have more data, you can create several subprojects, each import part of the data, and then merge the subprojects to create a parent project with all data. Because subprojects can import data simultaneously, this strategy allows you to import data more efficiently. Added benefits include separate (and faster) analysis in subprojects, faster re-creation of the main project if needed, and easy management of different batches/versions of data. Please refer to [this tutorial]([3]) for more details. 
{{% /notice %}}


### 3. Sample statistics


    # 3.8G RAM, 30min 
    % vtools update variant --from_stat 'num=#(alt)' 'hom=#(hom)' 'het=#(het)' 'other=#(other)'
    

You can then view the number of variants in the sample using command vtools output: 

    % vtools output variant chr pos ref alt num hom het -l 10
    

To calculate sample statistics in cases and controls, we mark samples with affection status according to their filenames 



    # finish within 1 second 
    % vtools phenotype --set aff=2 --samples 'filename like "%MG%"'
    % vtools phenotype --set aff=2 --samples 'filename like "%NA%"'
    % vtools phenotype --set aff=1 --samples 'aff is NULL'
    

Then, we can calculate number of variants in cases and controls separately: 



    # Use 25min and 5min respectively 
    % vtools update variant --from_stat 'case_num=#(alt)' --samples aff=2
    % vtools update variant --from_stat 'ctrl_num=#(alt)' --samples aff=1
    % vtools output variant chr pos ref alt num case_num ctrl_num  -l 5 
    



### 4. Annotate and select variants


    # Downloading dbNSFP can be SLOW, but using it is fast. 
    % vtools use dbNSFP
    % vtools output variant chr pos ref alt SIFT_score PolyPhen2_score -l 15
    

Select variants that belong to dbNSFP (nonsynonymous SNVs in CCDS genes), this will naturally exclude all indels: 

    # This step takes 20min, using 28M of RAM 
    % vtools select variant 'dbNSFP.chr is not NULL' -t NS
    % vtools output NS chr pos ref alt SIFT_score PolyPhen2_score -l 10
    

We can further select from the NS table using SIFT and PolyPhen 2 scores provided by dbNSFP. Note that in this database, higher scores indicate higher probability of damaging. 



    # These queries take 20, 5 and 5min. 
    % vtools select NS 'SIFT_score > 0.95' -t NS_damaging 
    % vtools select NS 'SIFT_score > 0.95' 'PolyPhen2_score > 0.95' -t NS_damaging_pp2 
    % vtools select NS 'SIFT_score > 0.95 OR PolyPhen2_score > 0.95' -t NS_or
    



    # All these operations are fast 
    % vtools show tables
    % vtools compare NS_damaging NS_or -c
    % vtools compare NS_damaging NS_or --B_diff_A NS_pp2
    % vtools output NS_pp2 chr pos ref alt SIFT_score PolyPhen2_score -l 10
    

Use ccds gene and keggPathway annotation databases to annotate variants with gene names 


    # These operations are fast 
    % vtools use ccdsGene
    % vtools use ccdsGene_exon
    % vtools use keggPathway --linked_by ccdsGene.name
    % vtools output NS chr pos ccdsGene.name KgDesc -l 20
    

Select variants that belong to certain pathway 

    % vtools select NS 'kgID="hsa00760"' --output chr pos ref alt ccdsGene.name kgDesc -l 20
    



### 5. Use annovar to provide gene-based annotation

The following commands export variants in table NS in ANNOVAR format, run ANNOVAR to annotate it, and import the result back: 



    # Update from ANNOVAR result takes 3m42s 
    % vtools export NS --format ANNOVAR annovar.input
    % ../annovar/annotate_variation.pl annovar.input ../annovar/humandb/ --build hg19
    % vtools update variant --from_file annovar.input.exonic_variant_function --format ANNOVAR_output
    



    # Returns instantly 
    % vtools select NS 'mut_type = "stopgain SNV"' --output chr pos ref alt mut_type -l 20
    



### 6. More examples on output and select

This command demonstrates the use of simple arithmetic in the output of fields 

    # It takes 3m11s to output 18M variants 
    % vtools output variant chr 'pos-1' pos ref alt  > Bed_output
    

You can also output fields from annotation databases. They all (conceptually) belong to the master variant table and can be use like other fields. 

{{% notice tip %}}
The first command take 19m to run, but the second command and repeated run of the first command take only 7s, because the underlying database engine has optimized such queries. 
{{% /notice %}}

    % vtools output NS chr pos ref alt case_num ctrl_num SIFT_score > outfile
    % vtools output NS chr pos ref alt case_num ctrl_num SIFT_score --build hg18 > outfile_hg18
    

Count the number of variants is easy. The following two commands count the number of insertions and deletions 

    # 30s each 
    % vtools select variant 'ref="-"' --count 
    % vtools select variant 'alt="-"' --count 
    

We can count the total number of genotypes using the sum of field `num`, which is the sample allele count for each variant. Similarly, we can count the total number of transition mutations. 

    # Two commands take 13s and 1min respectively. 
    % vtools output variant 'sum(num)' 
    % vtools select variant "(ref='A' AND alt='G') OR (ref='G' AND alt='A') \
       OR (ref='C' AND alt='T') OR (ref='T' AND alt='C')" --output 'sum(num)' 
    

The following command count the number of transition and transversion mutations and output transition/transversion ratio, for each allele count. 

    # This command takes 48min to execute 
    % vtools_report trans_ratio variant -n num --by_count

 [1]:  vtools.pdf/
 [2]:    /documentation/vtools_commands/import/
 [3]:    /documentation/tutorials/subprojects/