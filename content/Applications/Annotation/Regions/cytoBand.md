
+++
title = "cytoBand"
weight = 3
+++

## Cyto Band

cytoBand defines cytogenic bands. This annotation source gives the approximate location of these bands as seen on Giemsa-stained chromosomes. This data was downloaded from the UCSC Genome Browser database (<http://genome.ucsc.edu/cgi-bin/hgTables>). 

The following fields are available for annotation. 



    vtools show annotation cytoBand -v2
    
    DEBUG: Opening project temp.proj
    DEBUG: Loading annotation database cytoBand
    DEBUG: Loading annotation database gwasCatalog
    Annotation database cytoBand (version hg19_20111216)
    Description: Cyto Band
    Database type: range
    Number of records: 862
    Number of distinct ranges: 862
    Reference genome hg19: ['chr', 'begin', 'end']
    
    Field:           chr
    Type:            chromosome
    Missing entries: 0 
    Unique Entries:  24
    
    Field:           begin
    Type:            integer
    Comment:         start position on chromosome
    Missing entries: 0 
    Unique Entries:  667
    Range:           1 - 243700001
    
    Field:           end
    Type:            integer
    Comment:         end position on chromosome
    Missing entries: 0 
    Unique Entries:  690
    Range:           2200000 - 249250621
    
    Field:           name
    Type:            string
    Comment:         name of cytogenic band
    Missing entries: 0 
    Unique Entries:  259
    
    Field:           gieStain
    Type:            string
    Comment:         giemsa stain results
    Missing entries: 0 
    Unique Entries:  8