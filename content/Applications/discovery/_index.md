+++
title = "Discovery"
weight = 2
+++



## Discover informative variants from a large number of variants



#### Introduction

Once you have [imported][1] variants and samples of an exome or whole-genome sequencing project, you are typically facing a master variant table with millions of variants. Depending on the phenotypes of interest and particular research topics, you might want to filter variants for subsequent association analysis, or select variants that are more informative than others for further lab-based analysis. For example, you might be interested in 



*   Variants in a specific list of genes (cancer genes?) 
*   Variants are that novel (not in dbSNP and 1000 genomes project) 
*   Variants that exist only in cases but not in control, 
*   Variants that are non-synonymous, frame-shifting, predicted to be damaging, or highly conserved during evolution, 
*   Variants that are in exon regions of genes, 
*   Variants that are in particular pathways 



#### Variant info and annotation fields

Variants that satisfies these conditions can be selected from either project-specific properties (sample statistics, quality score etc) or annotation databases (dbSNP or 1000 genome project membership, gene regions etc). Required variant info and annotation fields could be prepared by 



*   [Import][1]or [update][2] variant info fields from source files, 
*   [Calculate sample statistics][2] as variant info fields, and 
*   [Download and link][3] project to various annotation databases. 

Please refer to relevant documentation pages for details. 



#### Selection and management of variants

After you have required variant info and annotation fields in place, you have conceptually a huge table with variant as rows and variant info and annotation fields as columns. It is then relatively easy to use command `vtools select` or `vtools exclude` to select variants of interest. For example, if you have a field `num_case` as number of alternative alleles in the cases (affected individuals), `num_control` as number of alternative alleles in controls (unaffected individuals), `SIFT_score` from database [dbNSFP][4], you could use condition 



    'num_case>0' 'num_control=0' 'SIFT_score>0.95' 'dbSNP.chr is NULL'
    

to select variants that are available in cases (`num_case>0`), not in control (`num_control=0`), predicted to be damaging (`SIFT_score>0.95`), and is not in dbSNP (`dbSNP.chr is NULL`). The last condition looks a bit strange but it merely means that there is no value (`NULL`) for field `dbSNP.chr` in the large virtual table we have imagined, meaning variants that are not in the `dbSNP` database. 

Selected variants could be outputted directly but they are more frequently saved to a separate **variant table** for future reference. Many variant tables could be created based on different selection criteria, and you could use any of these tables whenever a variant table is needed (e.g. after commands `vtools select`, `vtools exclude`, `vtools output`, and `vtools export`). 



#### Tutorials

For more information on the use of these commands, please refer to the following tutorials: 



*   Analyzing 44 whole genome cases and 200 exome controls, with detailed **performance measures** [<img src="html.png" width = "25" height = "25" style = "display: inline" />][6] 
*   Analyzing 5 whole-genome samples from **Illumina** [<img src="html.png" width = "25" height = "25" style = "display: inline"/>][8] 
*   **Compare** variants from the same samples called by **Complete Genomics** and **Illumina**
[<img src="html.png" width = "25" height = "25" style = "display: inline" />][10] 
*   **Select variants** belonging to specified genes [<img src="html.png" width = "25" height = "25" style = "display: inline" />][12]

 [1]: /vat-docs/documentation/vtools_commands/import/
 [2]: /vat-docs/documentation/vtools_commands/update/
 [3]: /vat-docs/documentation/applications/annotation/
 [4]:  /vat-docs/applications/annotation/variants/dbnsfp/
 [6]: /vat-docs/documentation/tutorials/case44ctrl20/
 [8]: /vat-docs/documentation/tutorials/illumina5/
 [10]: /vat-docs/documentation/tutorials/compare/
 [12]: /vat-docs/documentation/tutorials/select/