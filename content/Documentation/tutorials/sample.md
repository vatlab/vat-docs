+++
title = "Sample"
weight = 11
hidden = true
+++


##  Handling sample genotypes that imported from multiple files


When `vtools import` imports a file, it creates one or more samples associated with this file. This works well if all genotypes belong to a sample are contained in one file, but not so if the genotypes are scattered in multiple files (e.g. chromosome by chromosome). This tutorial demonstrates how to use `vtools admin` command to handle sample genotypes that are imported from multiple files. 



### 1. Data

#### 1.1 Create project and import data

We import genotypes for two samples, with names `MG1000` and `MG1004`. SNV and Indels are imported from different files but are imported with the same sample names. 



    vtools init proj
    vtools import snv/MG1000-240.snp.txt.vcf --build hg18 --sample_name MG1000
    vtools import snv/MG1004-200.snp.txt.vcf --sample_name MG1004
    vtools import indel/MG1000-240.pileup.indel --format pileup_indel --sample_name MG1000
    vtools import indel/MG1004-200.pileup.indel --format pileup_indel --sample_name MG1004
    


{{% notice tip %}}
variant tools treats each line in the sample table as a separate sample, even if some of them share the same sample names. 
{{% /notice %}}

when we list the samples in this project, we can see four samples: 



    vtools show samples
    

    sample_name	filename
    MG1000	snv/MG1000-240.snp.txt.vcf
    MG1000	indel/MG1000-240.pileup.indel
    MG1004	snv/MG1004-200.snp.txt.vcf
    MG1004	indel/MG1004-200.pileup.indel
    

If we try to, for example, count the number of variants in each sample, we can use the `vtools phenotype` command: 



    vtools phenotype --from_stat 'het=#(het)' 'hom=#(hom)' 'GT=#(GT)'
    

    Calculating phenotype: 100% [==========================================>] 4 0.4/s in 00:00:09
    INFO: 12 values of 3 phenotypes (3 new, 0 existing) of 4 samples are updated.
    

The statistics (phenotypes) are available in the sample table 



    vtools show samples
    

    sample_name	filename	het	hom	GT
    MG1000	snv/MG1000-240.snp.txt.vcf	2384712	1319373	3708513
    MG1000	indel/MG1000-240.pileup.indel	623571	224378	847949
    MG1004	snv/MG1004-200.snp.txt.vcf	2372093	1328117	3704532
    MG1004	indel/MG1004-200.pileup.indel	605539	231405	836944
    

which can also be displayed using command `vtools phenotype --output` if you are only interested in a subset of phenotypes: 



    vtools phenotype --output sample_name hom het GT
    



    sample_name	filename	het	hom	GT
    MG1000	1319373	2384712	3708513
    MG1004	1328117	2372093	3704532
    MG1000	224378	623571	847949
    MG1004	231405	605539	836944
    



### 2 Merge samples

The problem is that genotypes imported from `snv` and `indel` folders belong to the same physical samples. Although it is useful to know the number of SNVs and Indels separately, genotypes belongs to the same physical sample should better be treated together because 



*   **handling of phenotype**: Phenotypes such as blood pressure, sex, and weight are defined for physical samples. Although command `vtools phenotype` allows you to import phenotype by sample name and will automatically replicate phenotypes to all samples with the same sample name, it is confusing to have several ""samples"" with the same phenotypes. 

*   **association analysis**: Association analysis are based on samples and sometimes use sample size for its analysis. Spreading genotypes that belong to the same physical sample into several samples will lead to erroneous results. 

*   **export variants**: variants are exported by samples. SNVs and indels will be exported as different samples in this example. 



#### 2.1 Prepare to merge

Because samples are merged by their names, it is important to double check the names of samples before you merge samples. Because samples are imported with correct names in this tutorial, we do not have to rename samples. Otherwise, you might have to rename samples using command `vtools admin --rename_samples`. For example, assuming that we did not use any of the `--sample_name` option during import, we would get a sample table as follows: 



    sample_name	filename	het	hom	GT
    SAMPLE	snv/MG1000-240.snp.txt.vcf	2384712	1319373	3708513
    None	indel/MG1000-240.pileup.indel	623571	224378	847949
    SAMPLE	snv/MG1004-200.snp.txt.vcf	2372093	1328117	3704532
    None	indel/MG1004-200.pileup.indel	605539	231405	836944
    

Samples imported from vcf files have a dummy sample name obtained from the header of the vcf files, others have `None` because the pileup.indel format does not have a header. If you merge samples, SNVs and Indels would be merged together as samples `SAMPLE` and `None`, which is definitely not we want. 


{{% notice warning %}}
`vtools admin --merge_samples` are used to merge genotypes of the same physical samples. If samples share genotypes for the same variants, this command will fail with an error message. 
{{% /notice %}}

To correct this problem, we can run 



    vtools admin --rename_samples 'filename like "%MG1000%"' MG1000
    vtools admin --rename_samples 'filename like "%MG1004%"' MG1004
    



#### 2.2 Merge samples

After we make sure that samples to be merged share the same sample names, we can merge samples using command `vtools admin --merge_samples`: 



    vtools admin --merge_samples
    

    INFO: 4 samples that share identical names are merged to 2 samples
    Merging MG1004: 100% [=====================================================>] 5 2.2/s in 00:00:02
    Merging MG1000: 100% [=====================================================>] 5 2.1/s in 00:00:02
    

The new sample table looks like: 



    vtools show samples
    

    sample_name	filename	het	hom	GT
    MG1000	snv/MG1000-240.snp.txt.vcf,indel/MG1000-240.pileup.indel	2384712	1319373	3708513
    MG1004	snv/MG1004-200.snp.txt.vcf,indel/MG1004-200.pileup.indel	2372093	1328117	3704532
    



#### 2.3 Update phenotype 

Merging samples will merge genotypes from original samples. Source filenames will also be updated. Phenotypes, if any, are copied from one of the original samples. The number of homozygotes, heterozygotes, and genotypes are therefore wrong in the above sample table and we need to update them by running `vtools phenotype --from_stat` again. 



    vtools phenotype --from_stat 'het=#(het)' 'hom=#(hom)' 'GT=#(GT)'
    

    Calculating phenotype: 100% [=========================================>] 2 0.5/s in 00:00:04
    INFO: 6 values of 3 phenotypes (0 new, 3 existing) of 2 samples are updated.
    

The statistics (phenotypes) are now 



    vtools show samples
    

    sample_name	filename	het	hom	GT
    MG1000	snv/MG1000-240.snp.txt.vcf,indel/MG1000-240.pileup.indel	3008283	1543751	4556462
    MG1004	snv/MG1004-200.snp.txt.vcf,indel/MG1004-200.pileup.indel	2977632	1559522	4541476
