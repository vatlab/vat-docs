
+++
title = "gwasCatalog"
weight = 7
+++

## Gwas Catalog

The gwasCatalog is NHGRI's collection of Genome-Wide Association (GWA) Studies SNPs. We downloaded the data for this annotation source from the UCSC Genome Browser database (<http://genome.ucsc.edu/cgi-bin/hgTables?command=start>). You can use this annotation source as a position, range or field-based annotation source. Examples for usage as a range-based and field-based annotation source are given on this page. (By default the usage for this annotation source is a position-based annotation source). 



### 1. Usage 

Here are the available gwasCatalog fields for annotation and filtering. 



    vtools show annotation gwasCatalog -v2
    

    Annotation database gwasCatalog (version hg19_20140112)
    Description:            This database contains single nucleotide polymorphisms
      (SNPs) identified by published Genome-Wide Association Studies (GWAS),
      collected in the Catalog of Published Genome-Wide Association Studies at the
      National Human Genome Research Institute (NHGRI). From
      http://www.genome.gov/gwastudies/:
    Database type:          position
    Number of records:      18,027
    Distinct positions:     13,980
    Reference genome hg19:  chr, position
    
    Field:                  chr
    Type:                   string
    Missing entries:        0
    Unique Entries:         36
    
    Field:                  position
    Type:                   integer
    Comment:                one-based position in chromosome
    Missing entries:        0
    Unique Entries:         13,974
    Range:                  5641 - 249168436
    
    Field:                  name
    Type:                   string
    Comment:                ID of SNP associated with trait
    Missing entries:        0
    Unique Entries:         12,003
    
    Field:                  pubMedId
    Type:                   integer
    Comment:                PubMed ID of publication of the study
    Missing entries:        0
    Unique Entries:         1,488
    Range:                  15761122 - 23894747
    
    Field:                  author
    Type:                   string
    Comment:                First author of publication
    Missing entries:        0
    Unique Entries:         1,129
    
    Field:                  pubDate
    Type:                   string
    Comment:                Date of publication
    Missing entries:        0
    Unique Entries:         899
    
    Field:                  journal
    Type:                   string
    Comment:                Journal of publication
    Missing entries:        0
    Unique Entries:         204
    
    Field:                  title
    Type:                   string
    Comment:                Title of publication
    Missing entries:        0
    Unique Entries:         1,488
    
    Field:                  trait
    Type:                   string
    Comment:                Disease or trait assessed in study
    Missing entries:        0
    Unique Entries:         865
    
    Field:                  initSample
    Type:                   string
    Comment:                Initial sample size
    Missing entries:        0
    Unique Entries:         1,579
    
    Field:                  replSample
    Type:                   string
    Comment:                Replication sample size
    Missing entries:        0
    Unique Entries:         1,064
    
    Field:                  region
    Type:                   string
    Comment:                Chromosome band / region of SNP
    Missing entries:        0
    Unique Entries:         871
    
    Field:                  genes
    Type:                   string
    Comment:                Reported gene(s)
    Missing entries:        0
    Unique Entries:         6,521
    
    Field:                  riskAllele
    Type:                   string
    Comment:                Strongest snp-risk allele
    Missing entries:        0
    Unique Entries:         12,631
    
    Field:                  riskAlFreq
    Type:                   string
    Comment:                risk allele frequency
    Missing entries:        0
    Unique Entries:         1,661
    
    Field:                  pValue
    Type:                   float
    Comment:                p-Value
    Missing entries:        0
    Unique Entries:         623
    Range:                  0 - NS
    
    Field:                  pValueDesc
    Type:                   string
    Comment:                p-Value description
    Missing entries:        0
    Unique Entries:         1,563
    
    Field:                  orOrBeta
    Type:                   string
    Comment:                Odds ratio or beta
    Missing entries:        0
    Unique Entries:         863
    
    Field:                  ci95
    Type:                   string
    Comment:                95% confidence interval
    Missing entries:        0
    Unique Entries:         5,604
    
    Field:                  platform
    Type:                   string
    Comment:                Platform and [SNPs passing QC]
    Missing entries:        0
    Unique Entries:         1,279
    
    Field:                  cnv
    Type:                   string
    Comment:                Y if copy number variant
    Missing entries:        0
    Unique Entries:         1
    



### 2. Details

#### 2.1 gwasCatalog: usage as a position-based annotation source (default)

To check if your variants contain any gwas hits, you can 



    vtools use gwasCatalog
    vtools select variant "gwasCatalog.chr is not NULL" -t gwasHits
    

However, because GWA studies use tagging SNPs to identify associated (hopefully) causal variants, your dataset might not contain the exact SNP that is reported in gwas catalog. It might contains the casual variant or other associations that are in vicinity (in LD) with the reported gwas hits. Therefore, it make more sense to find variants that are close to the reported gwas hits. 



#### 2.2 gwasCatalog: usage as a range-based annotation source

The most flexible way to use this annotation source is to link your variants to GWA hits with a position range. The following links your variant positions to GWA hits using variant chromosomal locations that are +/- 5000bp within the GWA hit. 



    vtools use gwasCatalog --anno_type range --linked_fields chr position-5000 position+5000
    

Then you can generate a useful report showing what known gwas hits are near your variants. The following command generates a report showing Type 2 diabetes hits near your variants. 



    vtools select variant "gwasCatalog.trait == 'Type 2 diabetes'" -o variant.chr variant.pos variant.ref variant.alt 
     gwasCatalog.trait gwasCatalog.name gwasCatalog.position gwasCatalog.pValue gwasCatalog.journal
     gwasCatalog.title > variants_near_diabetes_gwas_hits.txt
    

    1       207653395       C       A       Type 2 diabetes rs17045328      207652176       7e-06   PLoS Genet      Transferability of type 2 diabetes implicated loci in multi-ethnic cohorts from Southeast Asia.
    11      17408630        C       T       Type 2 diabetes rs5215  17408630        4e-07   Nat Genet       Meta-analysis of genome-wide association data and large-scale replication identifies additional susceptibility loci for type 2 diabetes.
    11      17408630        C       T       Type 2 diabetes rs5215  17408630        5e-11   Science Replication of genome-wide association signals in UK samples reveals risk loci for type 2 diabetes.
    11      17408630        C       T       Type 2 diabetes rs5219  17409572        1e-07   Science Genome-wide association analysis identifies loci for type 2 diabetes and triglyceride levels.
    11      17408630        C       T       Type 2 diabetes rs5219  17409572        1e-09   Diabetes        Adiposity-related heterogeneity in patterns of type 2 diabetes susceptibility observed in genome-wide association data.
    11      17408630        C       T       Type 2 diabetes rs5219  17409572        5e-07   Diabetes        Adiposity-related heterogeneity in patterns of type 2 diabetes susceptibility observed in genome-wide association data.
    11      17408630        C       T       Type 2 diabetes rs5219  17409572        7e-11   Science A genome-wide association study of type 2 diabetes in Finns detects multiple susceptibility variants.
    11      17409069        G       A       Type 2 diabetes rs5215  17408630        4e-07   Nat Genet       Meta-analysis of genome-wide association data and large-scale replication identifies additional susceptibility loci for type 2 diabetes.
    11      17409069        G       A       Type 2 diabetes rs5215  17408630        5e-11   Science Replication of genome-wide association signals in UK samples reveals risk loci for type 2 diabetes.
    11      17409069        G       A       Type 2 diabetes rs5219  17409572        1e-07   Science Genome-wide association analysis identifies loci for type 2 diabetes and triglyceride levels.
    11      17409069        G       A       Type 2 diabetes rs5219  17409572        1e-09   Diabetes        Adiposity-related heterogeneity in patterns of type 2 diabetes susceptibility observed in genome-wide association data.
    11      17409069        G       A       Type 2 diabetes rs5219  17409572        5e-07   Diabetes        Adiposity-related heterogeneity in patterns of type 2 diabetes susceptibility observed in genome-wide association data.
    11      17409069        G       A       Type 2 diabetes rs5219  17409572        7e-11   Science A genome-wide association study of type 2 diabetes in Finns detects multiple susceptibility variants.
    11      17409572        T       C       Type 2 diabetes rs5215  17408630        4e-07   Nat Genet       Meta-analysis of genome-wide association data and large-scale replication identifies additional susceptibility loci for type 2 diabetes.
    11      17409572        T       C       Type 2 diabetes rs5215  17408630        5e-11   Science Replication of genome-wide association signals in UK samples reveals risk loci for type 2 diabetes.
    11      17409572        T       C       Type 2 diabetes rs5219  17409572        1e-07   Science Genome-wide association analysis identifies loci for type 2 diabetes and triglyceride levels.
    11      17409572        T       C       Type 2 diabetes rs5219  17409572        1e-09   Diabetes        Adiposity-related heterogeneity in patterns of type 2 diabetes susceptibility observed in genome-wide association data.
    11      17409572        T       C       Type 2 diabetes rs5219  17409572        5e-07   Diabetes        Adiposity-related heterogeneity in patterns of type 2 diabetes susceptibility observed in genome-wide association data.
    11      17409572        T       C       Type 2 diabetes rs5219  17409572        7e-11   Science A genome-wide association study of type 2 diabetes in Finns detects multiple susceptibility variants.
    12      51354803        C       T       Type 2 diabetes rs12304921      51357542        7e-06   Nature  Genome-wide association study of 14,000 cases of seven common diseases and 3,000 shared controls.
    15      91524841        G       T       Type 2 diabetes rs8042680       91521337        2e-10   Nat Genet       Twelve type 2 diabetes susceptibility loci identified through large-scale association analysis.
    15      91525197        C       T       Type 2 diabetes rs8042680       91521337        2e-10   Nat Genet       Twelve type 2 diabetes susceptibility loci identified through large-scale association analysis.
    4       6302519 G       A       Type 2 diabetes rs1801214       6303022 3e-08   Nat Genet       Twelve type 2 diabetes susceptibility loci identified through large-scale association analysis.
    4       6302707 C       T       Type 2 diabetes rs1801214       6303022 3e-08   Nat Genet       Twelve type 2 diabetes susceptibility loci identified through large-scale association analysis.
    4       6303022 C       T       Type 2 diabetes rs1801214       6303022 3e-08   Nat Genet       Twelve type 2 diabetes susceptibility loci identified through large-scale association analysis.
    4       6303354 G       A       Type 2 diabetes rs1801214       6303022 3e-08   Nat Genet       Twelve type 2 diabetes susceptibility loci identified through large-scale association analysis.
    4       6303955 G       A       Type 2 diabetes rs1801214       6303022 3e-08   Nat Genet       Twelve type 2 diabetes susceptibility loci identified through large-scale association analysis.
    .....
    



#### 2.3 gwasCatalog: usage as a field-based annotation source

In this usage, you can annotate your variants with published GWA hits that are in the same cytoband as your project variants. You can link your variants to the cytoBand annotation source and then annotate your variant cytoBands to published GWA hits 



    vtools use cytoBand
    vtools use gwasCatalog --anno_type field --linked_fields region --linked_by 'cytoBand.name'
    

Then you can generate a useful report showing what known gwas hits are in the same cytobands as your variants. Once again, the following command generates a report showing Type 2 diabetes hits near your variants - except this time "near" means GWA hits that are within the same cytoband as your variants. 



    vtools select variant "gwasCatalog.trait == 'Type 2 diabetes'" -o variant.chr variant.pos variant.ref variant.alt
      gwasCatalog.trait gwasCatalog.name gwasCatalog.position gwasCatalog.pValue gwasCatalog.journal
      gwasCatalog.title > variants_near_diabetes_gwas_hits.txt
    

    1       117841245       C       T       Height  rs17038182      118868405       5e-07   Nat Genet       A large-scale genome-wide association study of Asian populations uncovers genetic factors influencing eight quantitative traits.
    1       117841245       C       T       Height  rs12735613      118883973       4e-11   Nat Genet       Genome-wide association analysis identifies 20 loci that influence adult height.
    1       117841245       C       T       Waist-hip ratio rs984222        119503843       9e-25   Nat Genet       Meta-analysis identifies 13 new loci associated with waist-hip ratio and reveals sexual dimorphism in the genetic basis of fat distribution.
    1       117841245       C       T       Type 2 diabetes rs10923931      120517959       4e-08   Nat Genet       Meta-analysis of genome-wide association data and large-scale replication identifies additional susceptibility loci for type 2 diabetes.
    1       117847270       A       G       Height  rs17038182      118868405       5e-07   Nat Genet       A large-scale genome-wide association study of Asian populations uncovers genetic factors influencing eight quantitative traits.
    1       117847270       A       G       Height  rs12735613      118883973       4e-11   Nat Genet       Genome-wide association analysis identifies 20 loci that influence adult height.
    1       117847270       A       G       Waist-hip ratio rs984222        119503843       9e-25   Nat Genet       Meta-analysis identifies 13 new loci associated with waist-hip ratio and reveals sexual dimorphism in the genetic basis of fat distribution.
    1       117847270       A       G       Type 2 diabetes rs10923931      120517959       4e-08   Nat Genet       Meta-analysis of genome-wide association data and large-scale replication identifies additional susceptibility loci for type 2 diabetes.
    .....