
+++
title = "knownGene"
weight = 4
+++

## Known Gene

The knownGene database is based on the UCSC Genome Browser knownGene track. knownGene shows gene predictions based on data from RefSeq, Genbank, CCDS and UniProt. If you would like to annotate your variants to these genes, you can use the simpler **knownGene** database. If you would like to determine the exons that your variants are in, use the **knownGene_exon** database. See the available annotation fields for each database below. 



### 1. knownGene

    % vtools show annotation knownGene -v2
    

    Annotation database knownGene (version hg19_20130904)
    Description:            Gene predictions based on data from RefSeq, Genbank,
      CCDS and UniProt, from the UCSC KnownGene track.
    Database type:          range
    Number of records:      82,960
    Distinct ranges:        60,726
    Reference genome hg19:  chr, txStart, txEnd
    
    Field:                  name
    Type:                   string
    Comment:                Name of gene such as uc001aaa.3
    Missing entries:        0
    Unique Entries:         82,960
    
    Field:                  chr
    Type:                   string
    Missing entries:        0
    Unique Entries:         60
    
    Field:                  strand
    Type:                   string
    Comment:                which DNA strand contains the observed alleles
    Missing entries:        0
    Unique Entries:         2
    
    Field:                  txStart
    Type:                   integer
    Comment:                Transcription start position
    Missing entries:        0
    Unique Entries:         48,720
    Range:                  1 - 249211537
    
    Field:                  txEnd
    Type:                   integer
    Comment:                Transcription end position
    Missing entries:        0
    Unique Entries:         48,713
    Range:                  368 - 249213345
    
    Field:                  cdsStart
    Type:                   integer
    Comment:                Coding region start
    Missing entries:        0
    Unique Entries:         51,789
    Range:                  1 - 249211537
    
    Field:                  cdsEnd
    Type:                   integer
    Comment:                Coding region end
    Missing entries:        0
    Unique Entries:         51,745
    Range:                  0 - 249212562
    
    Field:                  exonCount
    Type:                   integer
    Comment:                Number of exons
    Missing entries:        0
    Unique Entries:         119
    Range:                  1 - 5065
    



### 2. knownGene_exon

    % vtools show annotation knowGene_exon -v2
    



    Annotation database knownGene_exon (version hg19_20130904)
    Description:            Gene predictions based on data from RefSeq, Genbank,
      CCDS and UniProt, from the UCSC KnownGene track. This database contains all
      exome regions of the UCSC known gene database.
    Database type:          range
    Number of records:      742,493
    Distinct ranges:        289,953
    Reference genome hg19:  chr, exon_start, exon_end
    
    Field:                  chr
    Type:                   string
    Missing entries:        0
    Unique Entries:         60
    
    Field:                  strand
    Type:                   string
    Comment:                which DNA strand contains the observed alleles
    Missing entries:        0
    Unique Entries:         2
    
    Field:                  txStart
    Type:                   integer
    Comment:                Transcription start position
    Missing entries:        0
    Unique Entries:         48,720
    Range:                  1 - 249211537
    
    Field:                  txEnd
    Type:                   integer
    Comment:                Transcription end position
    Missing entries:        0
    Unique Entries:         48,713
    Range:                  368 - 249213345
    
    Field:                  cdsStart
    Type:                   integer
    Comment:                Coding region start
    Missing entries:        0
    Unique Entries:         51,789
    Range:                  1 - 249211537
    
    Field:                  cdsEnd
    Type:                   integer
    Comment:                Coding region end
    Missing entries:        0
    Unique Entries:         51,745
    Range:                  0 - 249212562
    
    Field:                  exonCount
    Type:                   integer
    Comment:                Number of exons
    Missing entries:        0
    Unique Entries:         119
    Range:                  1 - 5065
    
    Field:                  exon_start
    Type:                   integer
    Comment:                exon start position
    Missing entries:        0
    Unique Entries:         276,580
    Range:                  1 - 249211537
    
    Field:                  exon_end
    Type:                   integer
    Comment:                exon end position
    Missing entries:        0
    Unique Entries:         276,718
    Range:                  368 - 249213345