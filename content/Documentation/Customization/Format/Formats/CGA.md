+++
title = "CGA"
weight = 9
+++


# HomePage

## Sample data

    ASSEMBLY_ID    XXXX
    #CNV_WINDOW_WIDTH       2000
    #COSMIC COSMIC v48
    #DBSNP_BUILD    dbSNP build 132
    #DGV_VERSION    9
    #FORMAT_VERSION 1.7
    #GENERATED_AT   XXX
    #GENERATED_BY   cgatools
    #GENE_ANNOTATIONS       NCBI build 37.2
    #GENOME_REFERENCE       NCBI build 37
    #MIRBASE_VERSION        miRBase version 16
    #PFAM_DATE      XXX
    #REPMASK_GENERATED_AT   XXX
    #SAMPLE XXX
    #SEGDUP_GENERATED_AT    XXX
    #SOFTWARE_VERSION       1.12.0.47
    #TYPE   VAR-OLPL
    
    >locus  ploidy  chromosome      begin   end     zygosity        varType reference       allele1Seq      allele2Seq      allele1Score    allele2Score    allele1HapLink  allele2HapLink  xRef    evidenceIntervalId      allele1ReadCount        allele2ReadCount        referenceAlleleReadCount        totalReadCount  allele1Gene     allele2Gene     pfam    miRBaseId       repeatMasker    segDupOverlap   relativeCoverage        calledPloidy
    1       2       chr1    0       10000   no-call no-ref  =       ?       ?                                                                                                                          
    2       2       chr1    10000   11090   no-call complex =       ?       ?                                                                                                                                       1.13    N
    3       2       chr1    11090   11105   hom     ref     =       =       =                                                                                                                                       1.13    N
    4       2       chr1    11105   11170   no-call complex =       ?       ?                                                                                                                                       1.13    N
    5       2       chr1    11170   11195   hom     ref     =       =       =                                                                                                                                       1.13    N
    6       2       chr1    11195   11211   no-call complex =       ?       ?                                                                                                                                       1.13    N
    7       2       chr1    11211   11227   hom     ref     =       =       =                                                                                                                                       1.13    N
    
    



## Example

    vtools import --format CGA /path/to/masterVarBeta$ID.tsv.bz2 --build hg19
