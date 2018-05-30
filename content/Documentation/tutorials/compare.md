+++
title = "Compare"
weight = 5
hidden = true
+++


## Compare variants for the same samples called by complete genomics and illumina




### 1. Data

Samples from two patients were sent to Complete Genomics and Illumina for whole-genome sequencing analysis. The variants are called by Complete Genomics using Complete Genomics Anslysis (CGA) package, and CASAVA 1.8 by Illumina. Before we do any further analysis, we are interested in knowing whether or not these two platforms yield comparable results. 

As always, we need to find an empty directory and create a new project: 



    % vtools init comparison
    



### 2. Loading data from two platforms

#### 2.1 Loading data from Complete Genomics data

For each sample, the variants are saved in a single file `ASM/masterVarBeta-$ID-ASM.tsv.bz2`, which can be imported directly using format `CGA`. 



    % vtools import --format CGA /path/to/ASM/masterVarBeta-CG1-ASM.tsv.bz2 \
        -j2 --sample_name CG1 --build hg19
    % vtools import --format CGA /path/to/ASM/masterVarBeta-CG2-ASM.tsv.bz2 \
        -j2 --sample_name CG2
    



#### 2.2 Loading data from Illumina

SNVs and INDELs are called separately and are saved by chromosomes. They can be imported using format `CASAVA18_snp` and `CASAVA_indel`. 



    % vtools import --format CASAVA18_snp /path/to/S1/Variations/snps/chr*.txt \
        --sample_name Illumina1
    % vtools import --format CASAVA18_snp /path/to/S2/Variations/snps/chr*.txt \
        --sample_name Illumina2
    % vtools import --format CASAVA18_indel /path/to/S1/Variations/indels/chr*.txt \
        --sample_name Illumina1
    % vtools import --format CASAVA18_indel /path/to/S2/Variations/indels/chr*.txt \
        --sample_name Illumina2
    

Although each genotypes from each sample consist of multiple *samples* (in variant tools term), they can be identified by their names. 

{{% notice tip %}}
Use command `vtools show samples` to see samples and their phenotypes. 
{{% /notice %}}

#### 2.3 Separate variants into their own variant tables

All samples are imported to the master variant table so we need to separate them into separate variant tables according their sample names. This can be done using commands 



    % vtools select variant --samples 'sample_name="CG1"' -t CG1
    % vtools select variant --samples 'sample_name="CG2"' -t CG2
    % vtools select variant --samples 'sample_name="Illumina1"' -t Illumina1
    % vtools select variant --samples 'sample_name="Illumina2"' -t Illumina2
    

We can use `vtools_report variant_stat` to calculate number of different types of variants in each table, or we can do that explicitly using commands 



    % for table in CG1 CG2 Illumina1 Illumina2
    % do
        vtools select $table 'alt!="-"' 'ref!="-"' 'length(alt)=1' 'length(ref)=1' -c
        vtools select $table 'ref="-"' -c
        vtools select $table 'alt="-"' -c
        vtools select $table 'alt!="-"' 'ref!="-"' 'length(alt) > 1 OR length(ref) > 1' -c
    % done
    

Of course, for the total number of variants in each table, you can simply call 



    % vtools show tables
    



### 3. Compare variants

To find common sets of variants, we can use command `vtools compare` to compare tables: 



    % vtools compare CG1 CG2 -c
    % vtools compare Illumina1 Ilumina2 -c
    % vtools compare CG1 Illumina1 -c
    % vtools compare CG2 Illumina2 -c
    

The first two commands compare two samples called using the same platform, the latter two commands compare variants from the same sample, called by different platforms. If you would like to know the exact differences, you can run commands such as 



    % vtools compare CG1 Illumina1 --difference CG_not_illumina
    % vtools compare Illumina1 CG1 --difference Illumina_not_CG
    

to get lists of variants differentially called by two platforms. 



### 4. Quality of variants

Different quality scores are used for different platforms and variant types. The following command calculates the average quality scores per-sample, and adds six **phenotypes** to the sample table. 

    % vtools phenotype --from_stat 'mean_Q_indel=avg(Q_indel)' 'mean_Q_snv=avg(Q_max_gt)' \
        'mean_VAF1=avg(allele1VarScoreVAF)' 'mean_VAF2=avg(allele2VarScoreVAF)' \
        'mean_EAF1=avg(allele1VarScoreEAF)' 'mean_EAF2=avg(allele2VarScoreEAF)'
