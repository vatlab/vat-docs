
+++
title = "linkage-physical map"
description = ""
weight = 4
+++



The rutgersMap database was created from Rutgers Combined Linkage-Phsycal Map[^T. C. Matise, F. Chen, W. Chen, F. M. De La Vega, M. Hansen, C. He, F. C.L. Hyland, G. C. Kennedy, X. Kong, S. S. Murray, J. S. Ziegle, W. C.L. Stewart and S. Buyske (2007). **A second-generation combined linkage physical map of the human genome**. *Genome Research*^]. The current version contains interpolated genetic positions for variants from dbSNP build 134. It is also possible to provide a list of variants with physical positions to the [Rutgers Map Interpolator][1] and create your own annotation database using the rutgersMap format with `--file` option for `vtools use` command. 

Description of the data from [Rutgers Computational Genetics Lab][2]: 



We have constructed de novo a high-resolution genetic map that includes the largest set of polymorphic markers for which genotype data are publicly available: it combines genotype data from both the CEPH and deCODE pedigrees (for some markers), incorporates SNPs, also incorporates sequence-based positional information. The position of most markers on our map is corroborated by both genomic sequence and recombination-based data. This specific combination of features maximizes marker inclusion, coverage, and resolution, making this map uniquely suited as a comprehensive resource for determining genetic map information (order and distances) for any large set of polymorphic markers. 



## rutgersMap

    % vtools show annotation rutgersMap -v2
    

    Annotation database rutgersMap (version b134)
    Description:            Rutgers Combined Linkage-Physical Map
    Database type:          position
    Reference genome hg19:  chr, position
      chr
      position              one-based position in chromosome
      cm_avg                map distance (cM), averaged
      cm_female             map distance (cM), female
      cm_male               map distance (cM), male
    

[^#^]

 [1]: http://compgen.rutgers.edu/mapinterpolator
 [2]: http://compgen.rutgers.edu/maps