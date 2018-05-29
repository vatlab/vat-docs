
+++
title = "Introduction"
description = ""
weight = 1
+++



# Single gene

## Association Tests for Single Gene and Case Control Phenotypes

The application of next-generation sequencing methods to the discovery of disease causal genes has been successful in finding rare genetic mutations responsible for a number of Mendalian disorders. There is growing evidence that rare variants contribute to the etiology of complex traits and whole genome (or exome) squencing in large populations provides valuable resource for identifying such variants. Although it is believed that effect size of rare variants to complex diseases is usually higher compare to common variants, due to the low frequency of rare variants large sample size is required to detect the effect. To improve power a number of methods have been proposed which analyze groups of variants together as a single unit. These methods are generally viewed as first moment methods (collapsing methods such as CMC, RareCover; aggregation methods such as WSS, KBAC, RBT, etc.) and second moment methods (such as {$C(\alpha)$} and SKAT). 

Most statistical methods for rare variants were originally proposed for association analysis between single gene and case control phenotype, although many can be readily generalized into testing for association adjusting for phenotype covariates. Implementation of single gene analysis in `VAT` include: 



*   [CMC method][1][?][1] 
*   [C{$(\alpha)$} method][2][?][2] 
*   [KBAC method][3][?][3] 
*   [RBT method][4][?][4] 
*   [RareCover method][5][?][5] 
*   [VT method][6][?][6] 
*   [WSS method][7][?][7] 
*   [aSum method][8][?][8] 



These **single gene analysis** methods are implemented in the form as they were originally published with minimal modifications or optimizations. They are good for analyzing gene and case control phenotype associations without adjusting for covariates. Please use [multivariate methods][9][?][9] if you want to perform conditional association analysis (`--covariates` option). The multivariate methods generalizes the scope of rare variant association tests to being able to handle both quantitative and case control data with flexible weighting and grouping approaches.

 [1]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.CMC?action=edit
 [2]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.CALPHA?action=edit
 [3]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.KBAC?action=edit
 [4]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.RBT?action=edit
 [5]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.RareCover?action=edit
 [6]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.VariableThresholds?action=edit
 [7]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.WSS?action=edit
 [8]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.ASUM?action=edit
 [9]: http://localhost/~iceli/wiki/pmwiki.php?n=Association.Multivariate?action=edit