
+++
title = "genomicSuperDups"
weight = 3
+++


See this blog [Why You Should Care About Segmental Duplications][1] for some nice explanation. 



    vtools show annotation genomicSuperDups -v2
    

    Annotation database genomicSuperDups (version hg19_20130626)
    Description:            Duplications of >1000 Bases of Non-RepeatMasked
      Sequence (>90 percent similar).
    Database type:          range
    Number of records:      51,599
    Distinct ranges:        40,832
    Reference genome hg19:  chr, start, end
    
    Field:                  chr
    Type:                   string
    Comment:                Reference sequence chromosome or scaffold
    Missing entries:        0
    Unique Entries:         80
    
    Field:                  start
    Type:                   integer
    Comment:                Start position in chromosome
    Missing entries:        0
    Unique Entries:         30,451
    Range:                  1 - 249235635
    
    Field:                  end
    Type:                   integer
    Comment:                End position in chromosome
    Missing entries:        0
    Unique Entries:         30,690
    Range:                  1832 - 249240008
    
    Field:                  name
    Type:                   string
    Comment:                Other chromosome involved
    Missing entries:        0
    Unique Entries:         30,525
    
    Field:                  otherChr
    Type:                   string
    Comment:                Other chromosome or scaffold
    Missing entries:        0
    Unique Entries:         80
    
    Field:                  otherStart
    Type:                   integer
    Comment:                Start position of other region
    Missing entries:        0
    Unique Entries:         30,451
    Range:                  0 - 249235634
    
    Field:                  otherEnd
    Type:                   integer
    Comment:                End position in chromosome
    Missing entries:        0
    Unique Entries:         30,690
    Range:                  1832 - 249240008
    
    Field:                  otherSize
    Type:                   integer
    Comment:                Total size of other chromosome
    Missing entries:        0
    Unique Entries:         80
    Range:                  19913 - 249250621
    
    Field:                  alignL
    Type:                   integer
    Comment:                spaces/positions in alignment
    Missing entries:        0
    Unique Entries:         13,141
    Range:                  1001 - 777920
    
    Field:                  indelN
    Type:                   integer
    Comment:                number of indels
    Missing entries:        0
    Unique Entries:         436
    Range:                  0 - 993
    
    Field:                  indelS
    Type:                   integer
    Comment:                indel spaces
    Missing entries:        0
    Unique Entries:         4,617
    Range:                  0 - 92315
    
    Field:                  matchB
    Type:                   integer
    Comment:                aligned bases that match
    Missing entries:        0
    Unique Entries:         12,497
    Range:                  1000 - 766171
    
    Field:                  mismatchB
    Type:                   integer
    Comment:                aligned bases that do not match
    Missing entries:        0
    Unique Entries:         12,623
    Range:                  900 - 766171
    
    Field:                  transitionsB
    Type:                   integer
    Comment:                number of transitions
    Missing entries:        0
    Unique Entries:         2,659
    Range:                  0 - 9703
    
    Field:                  transversionsB
    Type:                   integer
    Comment:                number of transversions
    Missing entries:        0
    Unique Entries:         1,880
    Range:                  0 - 5953
    
    Field:                  fracMatch
    Type:                   float
    Comment:                fraction of matching bases
    Missing entries:        0
    Unique Entries:         1,442
    Range:                  0 - 4002
    
    Field:                  fracMatchIndel
    Type:                   float
    Comment:                fraction of matching bases with indels
    Missing entries:        0
    Unique Entries:         21,193
    Range:                  0.9 - 1
    
    Field:                  jcK
    Type:                   float
    Comment:                K-value calculated with Jukes-Cantor
    Missing entries:        0
    Unique Entries:         21,393
    Range:                  0.88604 - 1
    
    Field:                  k2K
    Type:                   float
    Comment:                Kimura K
    Missing entries:        0
    Unique Entries:         23,215
    Range:                  0 - 0.107326

 [1]: http://blog.goldenhelix.com/?p=1153