
+++
title = "thousandGenomes"
weight = 9
+++

## Thousand Genome

### thousandGenomes

The samples for the 1000 Genomes Project mostly are anonymous and have no associated medical or phenotype data. Variants in this annotation database are sometimes considered to be 'neutral' and could be removed if the goal of a study is to look for variants with high penetrance that dispose to rare Mendelian diseases. This database contains all of the variants supplied by the 1000 Genomes Project. The original vcf file can be obtained from here: 

[ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/ALL.wgs.phase1\_release\_v3.20101123.snps\_indels\_sv.sites.vcf.gz][1] 

All of the annotation data supplied through the INFO fields in the VCF file can be used to annotate, filter or select project variants. A description of the fields available in the database are listed below. 



    % vtools show annotation thousandGenomes -v2
    
    Annotation database thousandGenomes (version hg19_v3_20101123)
    Description:            1000 Genomes VCF file analyzed in March 2012 from data
      generated from phase 1 of the project (available from: ftp://ftp.1000genomes
      .ebi.ac.uk/vol1/ftp/release/20110521/ALL.wgs.phase1_release_v3.20101123.snps
      _indels_sv.sites.vcf.gz).
    Database type:          variant
    Number of records:      39,701,227
    Distinct variants:      39,701,227
    Reference genome hg19:  chr, pos, ref, alt
    
    Field:                  chr
    Type:                   string
    Missing entries:        0
    Unique Entries:         23
    
    Field:                  pos
    Type:                   integer
    Missing entries:        0
    Unique Entries:         35,755,441
    Range:                  56 - 249239465
    
    Field:                  dbsnp_id
    Type:                   string
    Comment:                DB SNP ID
    Missing entries:        0
    Unique Entries:         39,628,006
    
    Field:                  ref
    Type:                   string
    Comment:                Reference allele (as on the + strand)
    Missing entries:        0
    Unique Entries:         50,996
    
    Field:                  alt
    Type:                   string
    Comment:                Alternative allele (as on the + strand)
    Missing entries:        0
    Unique Entries:         19,919
    
    Field:                  LDAF_INFO
    Type:                   float
    Comment:                MLE Allele Frequency Accounting for LD
    Missing entries:        0
    Unique Entries:         10,001
    Range:                  0 - 1
    
    Field:                  AVGPOST_INFO
    Type:                   float
    Comment:                Average posterior probability from MaCH/Thunder
    Missing entries:        0
    Unique Entries:         4,365
    Range:                  0.5242 - 1
    
    Field:                  RSQ_INFO
    Type:                   float
    Comment:                Genotype imputation quality from MaCH/Thunder
    Missing entries:        0
    Unique Entries:         9,500
    Range:                  0 - 1
    
    Field:                  ERATE_INFO
    Type:                   float
    Comment:                Per-marker Mutation rate from MaCH/Thunder
    Missing entries:        0
    Unique Entries:         1,395
    Range:                  0.0001 - 0.2051
    
    Field:                  THETA_INFO
    Type:                   float
    Comment:                Per-marker Transition rate from MaCH/Thunder
    Missing entries:        0
    Unique Entries:         828
    Range:                  0 - 0.1493
    
    Field:                  CIEND_INFO
    Type:                   string
    Comment:                Confidence interval around END for imprecise variants
    Missing entries:        39,692,293 (100.0% of 39,701,227 records)
    Unique Entries:         1,097
    
    Field:                  CIPOS_INFO
    Type:                   string
    Comment:                Confidence interval around POS for imprecise variants
    Missing entries:        39,692,293 (100.0% of 39,701,227 records)
    Unique Entries:         984
    
    Field:                  END_INFO
    Type:                   integer
    Comment:                End position of the variant described in this record
    Missing entries:        39,692,293 (100.0% of 39,701,227 records)
    Unique Entries:         1,097
    Range:                  -10,145 - 0,0
    
    Field:                  HOMLEN_INFO
    Type:                   integer
    Comment:                Length of base pair identical micro-homology at event
                            breakpoints
    Missing entries:        39,692,371 (100.0% of 39,701,227 records)
    Unique Entries:         162
    Range:                  0 - 415
    
    Field:                  HOMSEQ_INFO
    Type:                   string
    Comment:                Sequence of base pair identical micro-homology at
                            event breakpoints
    Missing entries:        39,694,177 (100.0% of 39,701,227 records)
    Unique Entries:         2,465
    
    Field:                  SVLEN_INFO
    Type:                   integer
    Comment:                Difference in length between REF and ALT alleles
    Missing entries:        39,692,293 (100.0% of 39,701,227 records)
    Unique Entries:         5,540
    Range:                  -964078 - 190
    
    Field:                  SVTYPE_INFO
    Type:                   string
    Comment:                Type of structural variant
    Missing entries:        39,692,293 (100.0% of 39,701,227 records)
    Unique Entries:         1
    
    Field:                  AC_INFO
    Type:                   integer
    Comment:                Alternate allele count
    Missing entries:        0
    Unique Entries:         2,185
    Range:                  0 - 2184
    
    Field:                  AN_INFO
    Type:                   integer
    Comment:                Total allele count
    Missing entries:        0
    Unique Entries:         2
    Range:                  1659 - 2184
    
    Field:                  AA_INFO
    Type:                   string
    Comment:                Ancestral Allele, ftp://ftp.1000genomes.ebi.ac.uk/vol1
                            /ftp/pilot_data/technical/reference/ancestral_alignmen
                            ts/README
    Missing entries:        8,934 (0.0% of 39,701,227 records)
    Unique Entries:         37,047
    
    Field:                  AF_INFO
    Type:                   float
    Comment:                Global allele frequency based on AC/AN
    Missing entries:        0
    Unique Entries:         10,001
    Range:                  0 - 1
    
    Field:                  AMR_AF_INFO
    Type:                   float
    Comment:                Allele frequency for samples from AMR based on AC/AN
    Missing entries:        19,038,919 (48.0% of 39,701,227 records)
    Unique Entries:         102
    Range:                  0.0028 - 1
    
    Field:                  ASN_AF_INFO
    Type:                   float
    Comment:                Allele frequency for samples from ASN based on AC/AN
    Missing entries:        24,655,050 (62.1% of 39,701,227 records)
    Unique Entries:         104
    Range:                  0.0017 - 1
    
    Field:                  AFR_AF_INFO
    Type:                   float
    Comment:                Allele frequency for samples from AFR based on AC/AN
    Missing entries:        12,995,707 (32.7% of 39,701,227 records)
    Unique Entries:         103
    Range:                  0.002 - 1
    
    Field:                  EUR_AF_INFO
    Type:                   float
    Comment:                Allele frequency for samples from EUR based on AC/AN
    Missing entries:        22,081,461 (55.6% of 39,701,227 records)
    Unique Entries:         105
    Range:                  0.0013 - 1
    
    Field:                  VT_INFO
    Type:                   string
    Comment:                Variant type
    Missing entries:        0
    Unique Entries:         3
    
    Field:                  SNPSOURCE_INFO
    Type:                   string
    Comment:                indicates if a snp was called when analyzing the low
                            coverage or exome alignment data
    Missing entries:        1,452,448 (3.7% of 39,701,227 records)
    Unique Entries:         3

 [1]: ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/ALL.wgs.phase1_release_v3.20101123.snps_indels_sv.sites.vcf.gz