
+++
title = "QC"
weight = 2
+++


## Data Exploration and Quality Control 



### 1. Overview

Quality control is a key step in association analysis. We may use a variety of criteria to clean our data (criteria directly from original vcf file or statistic summary we are interested in). Variants can also be subsetted based on these properties such as variant information, annotations, summary statistics, etc, which are displayed by `vtools show fields`. 



*   `vtools select` and `vtools exclude` commands implement variant and genotype level data selection and filtering. We could either focus on subsets of variants of interest (`vtools select`) or remove non-informative subsets of variants (`vtools exclude`) after such subsets are created. 
*   `vtools update` and `vtools phenotype` commands implement variant and sample level summary statistics. We could either get counts for different genotypes, functional variants (`vtools update`) or total/average of these counts per individual (`vtools phenotype`). 



### 2. QC Pipeline in Brief

*   Variant & Genotype Level QC (`vtools select` and `vtools exclude`) 
    *   remove low quality variants which do not pass the variants filter. 
    *   remove low quality genotypes with low genotype quality score (GQ) 
    *   remove low quality genotypes with low genotype depth of coverage (GD). 
    

*   Hardy–Weinberg equilibrium Filter (`vtools update`) 
    *   remove variants which does not pass Hardy–Weinberg equilibrium criterion (e.g. HWE pvalue < \\(10^{-8}\\)  ). 
    

*   Basic Summary Statistics on Variant Level (`vtools update`) 
    *   based on variant level, we can get basic counts of different genotypes (calls, wild types, mutation types, homozygote genotypes, heterozygote genotypes, alternative alleles, etc). 
    *   based on variant level, we can calculate alternative allele frequency, and subset variants by different allele frequency cutoff defined as common variants or rare variants. 
    *   based on variant level, we cat get counts of different functional types of variants (synonymous, missense, nonsense, etc). 
    *   based on variant level, we cat get counts of singletons and doubletons. 
    

*   Basic Summary Statistics on Sample Level (`vtools phenotype`) 
    *   based on individual level, we can get basic counts of different genotypes (calls, wild types, mutation types, homozygote genotypes, heterozygote genotypes, alternative alleles, etc) and calculate average counts. 
    *   based on individual level, we cat get counts of different types of variants (synonymous, missense, nonsense, etc), and calculate average counts. 
    *   based on individual level, we cat get counts of transitions and transversions, and calculate transitions V.S. transversions ratio (Ti/Tv ratio). 
    *   based on individual level, we cat get counts of singletons and doubletons, and calculate average counts. 



### 3. QC Pipeline in Detail

*   **Introductory tutorial**: a 30min tutorial using ~100 samples from 1000 Genomes Project [<img src="PDF.jpg" width = "25" height = "25" style = "display: inline" />][6]
    *   [Data bundle][2] 
*   **Basic tutorial**: a basic demonstration of quality control using exome sequencing data from European and Asian samples of the 1000 genomes project [<img src="html.png" width = "25" height = "25" style = "display: inline" />][4]
*   **Advanced tutorial**: an advanced demonstration of quality control using same dataset as the basic tutorial [<img src="PDF.jpg" width = "25" height = "25" style = "display: inline" />][6]


 [2]: http://downloads.statgen.us/VATData.tar.gz
 [4]:   /applications/association/qc/demon
 [6]: http://downloads.statgen.us/VATAdvanced.pdf