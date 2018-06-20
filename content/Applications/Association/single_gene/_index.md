+++
title = "Single gene"
weight = 7
+++



## Single gene

### Association Tests for Single Gene and Case Control Phenotypes

The application of next-generation sequencing methods to the discovery of disease causal genes has been successful in finding rare genetic mutations responsible for a number of Mendalian disorders. There is growing evidence that rare variants contribute to the etiology of complex traits and whole genome (or exome) squencing in large populations provides valuable resource for identifying such variants. Although it is believed that effect size of rare variants to complex diseases is usually higher compare to common variants, due to the low frequency of rare variants large sample size is required to detect the effect. To improve power a number of methods have been proposed which analyze groups of variants together as a single unit. These methods are generally viewed as first moment methods (collapsing methods such as CMC, RareCover; aggregation methods such as WSS, KBAC, RBT, etc.) and second moment methods (such as $C(\alpha)$ and SKAT). 

Most statistical methods for rare variants were originally proposed for association analysis between single gene and case control phenotype, although many can be readily generalized into testing for association adjusting for phenotype covariates. Implementation of single gene analysis in `VAT` include: 



*   [CMC method][1]
*   [C$(\alpha)$ method][2] 
*   [KBAC method][3] 
*   [RBT method][4]
*   [RareCover method][5]
*   [VT method][6] 
*   [WSS method][7]
*   [aSum method][8] 



These **single gene analysis** methods are implemented in the form as they were originally published with minimal modifications or optimizations. They are good for analyzing gene and case control phenotype associations without adjusting for covariates. Please use [multivariate methods][9] if you want to perform conditional association analysis (`--covariates` option). The multivariate methods generalizes the scope of rare variant association tests to being able to handle both quantitative and case control data with flexible weighting and grouping approaches.

 [1]:   /applications/association/single_gene/cmctest/
 [2]:   /applications/association/single_gene/c_alpha-test/
 [3]:   /applications/association/single_gene/kbac-test/
 [4]:   /applications/association/single_gene/rbt-test/
 [5]:  /applications/association/single_gene/rarecover/
 [6]:   /applications/association/single_gene/vt-test/
 [7]:   /applications/association/single_gene/wss-test/
 [8]:   /applications/association/single_gene/asum/
 [9]:   /applications/association/joint_conditional/