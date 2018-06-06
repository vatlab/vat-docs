
+++
title = "ccdsGene"
weight = 1
+++

## CcdsGene

This database contains high-confidence human gene annotations from the Consensus Coding Sequence (CCDS) project. It was constructed from the UCSC Genome Browser ccdsGene track. If you would like to annotate your variants to these genes, you can use the simpler **ccdsGene** database. If you would like to determine the exons that your variants are in, use the **ccdsGene_exon** database. See the available annotation fields for each database below. 



### 1. ccdsGene

    % vtools show annotation ccdsGene -v2
    

    Annotation database ccdsGene (version hg19_20130904)
    Description:            High-confidence human gene annotations from the
      Consensus Coding Sequence (CCDS) project.
    Database type:          range
    Number of records:      27,762
    Distinct ranges:        23,393
    Reference genome hg19:  chr, cdsStart, cdsEnd
    
    Field:                  name
    Type:                   string
    Comment:                Gene name (usually a CCDS transcript ID)
    Missing entries:        0
    Unique Entries:         27,731
    
    Field:                  chr
    Type:                   string
    Missing entries:        0
    Unique Entries:         24
    
    Field:                  strand
    Type:                   string
    Comment:                which DNA strand contains the observed alleles
    Missing entries:        0
    Unique Entries:         2
    
    Field:                  cdsStart
    Type:                   integer
    Comment:                Coding region start
    Missing entries:        0
    Unique Entries:         20,946
    Range:                  41608 - 249211537
    
    Field:                  cdsEnd
    Type:                   integer
    Comment:                Coding region end
    Missing entries:        0
    Unique Entries:         21,000
    Range:                  46385 - 249212562
    
    Field:                  exonCount
    Type:                   integer
    Comment:                Number of exons
    Missing entries:        0
    Unique Entries:         107
    Range:                  1 - 362
    
    Field:                  score
    Type:                   integer
    Comment:                Score
    Missing entries:        0
    Unique Entries:         1
    Range:                  0 - 0
    
    Field:                  name2
    Type:                   string
    Comment:                Alternate name
    Missing entries:        0
    Unique Entries:         1
    
    Field:                  cdsStartStat
    Type:                   string
    Comment:                cds start stat, can be 'non', 'unk', 'incompl', and
                            'cmp1'
    Missing entries:        0
    Unique Entries:         1
    
    Field:                  cdsEndStat
    Type:                   string
    Comment:                cds end stat, can be 'non', 'unk', 'incompl', and
                            'cmp1'
    Missing entries:        0
    Unique Entries:         1
    



### 2. ccdsGene_exon

    % vtools show annotation ccdsGene_exon -v2
    

    Annotation database ccdsGene_exon (version hg19_20130904)
    Description:            High-confidence human gene annotations from the
      Consensus Coding Sequence (CCDS) project. This database contains all exon
      regions of the CCDS genes.
    Database type:          range
    Number of records:      291,746
    Distinct ranges:        192,096
    Reference genome hg19:  chr, exon_start, exon_end
    
    Field:                  name
    Type:                   string
    Comment:                CCDS gene name
    Missing entries:        0
    Unique Entries:         27,731
    
    Field:                  chr
    Type:                   string
    Missing entries:        0
    Unique Entries:         24
    
    Field:                  strand
    Type:                   string
    Comment:                which DNA strand contains the observed alleles
    Missing entries:        0
    Unique Entries:         2
    
    Field:                  cdsStart
    Type:                   integer
    Comment:                Coding region start
    Missing entries:        0
    Unique Entries:         20,946
    Range:                  41608 - 249211537
    
    Field:                  cdsEnd
    Type:                   integer
    Comment:                Coding region end
    Missing entries:        0
    Unique Entries:         21,000
    Range:                  46385 - 249212562
    
    Field:                  exonCount
    Type:                   integer
    Comment:                Number of exons
    Missing entries:        0
    Unique Entries:         107
    Range:                  1 - 362
    
    Field:                  exon_start
    Type:                   integer
    Comment:                exon start position
    Missing entries:        0
    Unique Entries:         189,635
    Range:                  41608 - 249211537
    
    Field:                  exon_end
    Type:                   integer
    Comment:                exon end position
    Missing entries:        0
    Unique Entries:         189,690
    Range:                  41627 - 249212562
    
    Field:                  score
    Type:                   integer
    Comment:                Score
    Missing entries:        0
    Unique Entries:         1
    Range:                  0 - 0
    
    Field:                  name2
    Type:                   string
    Comment:                Alternative name
    Missing entries:        0
    Unique Entries:         1
    
    Field:                  cdsStartStat
    Type:                   string
    Comment:                cds start stat, can be 'non', 'unk', 'incompl', and
                            'cmp1'
    Missing entries:        0
    Unique Entries:         1
    
    Field:                  cdsEndStat
    Type:                   string
    Comment:                cds end stat, can be 'non', 'unk', 'incompl', and
                            'cmp1'
    Missing entries:        0
    Unique Entries:         1