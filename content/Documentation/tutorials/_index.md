+++
title = "Tutorials"
weight = 2
+++

## Tutorials

These tutorials explain steps that are used to analyze real-world sequencing data. We will try to explain the steps in detail but command output are usually ignored for brevity and confidentiality reasons. 



### 1. Quick Start Guide

This is a 10-minute quick start guide using data from the 1000 genomes project. We encourage you to walk through this minimal real-world example to get a feel for the software and assess its helpfulness.
[<img src="html.png" width = "25" height = "25" style = "display: inline" />][1]



### 2. Presentations

*   [Variant Tools][2] 
*   [Variant Simulation Tools][3] 
*   [Variant Pipeline Tools][4] 



### 3. Introductory tutorials

*   A recent **presentation** about variant tools, with output of commands [<img src="PDF.jpg" width = "25" height = "25" style = "display: inline" />][2]
*   A tutorial session in the [ACM BCB 2014 meeting][5] [<img src="html.png" width = "25" height = "25" style = "display: inline" />][6]



### 4. Variants screening

*   Analyzing 44 whole genome cases and 200 exome controls, with detailed **performance measures** [<img src="html.png" width = "25" height = "25" style = "display: inline" />][7] 
*   Analyzing 5 whole-genome samples from **Illumina** [<img src="html.png" width = "25" height = "25" style = "display: inline" />][8] 
*   **Compare** variants from the same samples called by **Complete Genomics** and **Illumina** [<img src="html.png" width = "25" height = "25" style = "display: inline" />][9] 
*   **Select variants** belonging to specified genes [<img src="html.png" width = "25" height = "25" style = "display: inline" />][10] 
*   **Detailed analysis** of one variant [<img src="html.png" width = "25" height = "25" style = "display: inline" />][11] 



### 5. Import and export

*   Import all genotype data from the 1000 genomes project [<img src="html.png" width = "25" height = "25" style = "display: inline" />][12] 
*   Generate and import **annovar annotations** for variants already in vtools [<img src="html.png" width = "25" height = "25" style = "display: inline" />][13] 
*   Import variants from a list of variants in an **unsupported format** [<img src="html.png" width = "25" height = "25" style = "display: inline" />][14] 
*   Handling **genotypes imported from multiple files** (e.g. genotypes of samples are imported chromosome by chromosome) [<img src="html.png" width = "25" height = "25" style = "display: inline" />][15] 



### 6. Reference genomes and annotation databases

*   Working with mouse and other genomes [<img src="html.png" width = "25" height = "25" style = "display: inline" />][16] 



### 7. Annotation

*   Annotating variants using **multiple annotation databases** [<img src="html.png" width = "25" height = "25" style = "display: inline" />][17] 



### 8. Association analysis

*   **Quality control** using sequencing data [<img src="html.png" width = "25" height = "25" style = "display: inline" />][18] 
*   **Association analysis** using sequencing data [<img src="html.png" width = "25" height = "25" style = "display: inline" />][19] 

### 9. Run association analysis on cluster

*   Submit a pbs script to run vtools association command on cluster using PBS  [<img src="html.png" width = "25" height = "25" style = "display: inline" />][21] 
*   Submit a pbs script to run vtools association command on cluster using LSF  [<img src="html.png" width = "25" height = "25" style = "display: inline" />][22] 

## Parallelization

*   Use **subprojects** to manage large projects. This strategy can be used to parallelize variant processing using multiple processors or a cluster [<img src="html.png" width = "25" height = "25" style = "display: inline" />][10]

 [1]:    /documentation/tutorials/quickstartguide/
 [2]:  vtools.pdf
 [3]:  VST.pdf
 [4]:  VariantPipelineTools.pptx
 [5]:  http://www.cse.buffalo.edu/ACM-BCB2014/
 [6]:    /documentation/tutorials/acm-bcb/ 
 [7]:    /documentation/tutorials/case44ctrl20/
 [8]:    /documentation/tutorials/illumina5/
 [9]:    /documentation/tutorials/compare/
 [10]:    /documentation/tutorials/select/
 [11]:    /documentation/tutorials/analysis/
 [12]:    /documentation/tutorials/1000genome/
 [13]:    /documentation/tutorials/annovar/
 [14]:    /documentation/tutorials/form/
 [15]:    /documentation/tutorials/sample/
 [16]:    /documentation/tutorials/mouthgenome/
 [17]:    /documentation/tutorials/annotation/
 [18]:    /documentation/tutorials/association/
 [19]:    /documentation/tutorials/testing/
 [20]:    /documentation/tutorials/subprojects/
 [21]:    /documentation/tutorials/pbscluster/
 [22]:    /documentation/tutorials/lsfcluster/