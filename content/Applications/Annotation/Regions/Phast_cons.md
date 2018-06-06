
+++
title = "PhastCons"
weight = 2
+++

## Phast Cons

The phastCons database annotates blocks of the genome with conservation scores using the phastCons algorithm (<http://compgen.bscb.cornell.edu/phast/help-pages/phastCons.txt>). The data that we are using was downloaded from the UCSC genome browser's phastCons46way track that contains conservation data for vertebrates. 


{{% notice tip%}}
PhastConsElements represents the most conserved regions so it covers a significantly percent of genome than the PhastCons database. 
{{%/notice%}}


### 1. PhastConsElements

    vtools show annotation PhastConsElements
    

    Description:            PhastCons Conservation Scores
    Database type:          range
    Number of records:      5,163,775
    Distinct ranges:        5,163,775
    Reference genome hg19:  chr, start, end
    
    Field:                  chr
    Type:                   string
    Missing entries:        0
    Unique Entries:         88
    
    Field:                  start
    Type:                   integer
    Comment:                Start position in chromosome
    Missing entries:        0
    Unique Entries:         5,093,542
    Range:                  1 - 249231389
    
    Field:                  end
    Type:                   integer
    Comment:                End position in chromosome
    Missing entries:        0
    Unique Entries:         5,093,841
    Range:                  12 - 249231641
    
    Field:                  name
    Type:                   string
    Comment:                Name of conserved region
    Missing entries:        0
    Unique Entries:         4,358
    
    Field:                  score
    Type:                   integer
    Comment:                Phast cons score from 0 to 1000
    Missing entries:        0
    Unique Entries:         580
    Range:                  177 - 1000
    



### 2. phastCons

The following example shows how you can use phastCons to annotate your variants with the average conservation score for the genomic block containing your variant. **phastCons.sum_data/phastCons.count** would give you this average score - see below to interpret these fields. This value could then be used to rank or filter your variants baed on the conservation score. 



    vtools output variant chr pos ref alt phastCons.sum_data/phastCons.count  -l 10
    

    1	10434	-	C	NA
    1	10440	C	-	NA
    1	54789	C	-	0.0587041015625
    1	54790	-	T	0.0587041015625
    1	63738	ACT	-	0.330704101563
    1	63738	ACT	CTA	0.330704101563
    1	81963	-	AA	0.161579101562
    1	82134	A	-	0.161579101562
    1	82135	-	AAAAAAAAAAAAAA	0.161579101562
    1	83120	A	-	0.136174804688
    

Below is a description of the phastCons fields. 



    vtools show annotation phastCons
    

    Annotation database phastCons (version hg19_20110909)
    Description: PhastCons Conservation Scores
    Database type: range
    Number of records: 2,808,750
    Number of distinct ranges: 2,808,750
    Reference genome hg19: ['chr', 'start', 'end']
    
    Field:           chr
    Type:            string
    Missing entries: 0 
    Unique entries:  92
    
    Field:           start
    Type:            integer
    Comment:         Start position in chromosome
    Missing entries: 0 
    Unique entries:  2,785,871
    Range:           1 - 249236922
    
    Field:           end
    Type:            integer
    Comment:         End position in chromosome
    Missing entries: 0 
    Unique entries:  2,785,911
    Range:           148 - 249237548
    
    Field:           name
    Type:            string
    Comment:         Name of conserved region
    Missing entries: 0 
    Unique entries:  2,808,750
    
    Field:           count
    Type:            integer
    Comment:         Number of values in this block
    Missing entries: 0 
    Unique entries:  1,024
    Range:           1 - 1024
    
    Field:           valid_count
    Type:            integer
    Comment:         Number of valid values in this block
    Missing entries: 0 
    Unique entries:  1,024
    Range:           1 - 1024
    
    Field:           lower_limit
    Type:            string
    Comment:         Lowest value in this block
    Missing entries: 0 
    Unique entries:  694
    
    Field:           data_range
    Type:            string
    Comment:         Spread of values in this block.  lower_limit + data_range =
                     upper_limit
    Missing entries: 0 
    Unique entries:  1,001
    
    Field:           sum_data
    Type:            string
    Comment:         Sum of values in this block (can be used for calculate average
                     and stddev of conservation scores)
    Missing entries: 0 
    Unique entries:  417,533
    
    Field:           sum_squares
    Type:            string
    Comment:         Sum of values squared in this block (can be used for
                     calculating stddev of conservation scores)
    Missing entries: 0 
    Unique entries:  1,501,657