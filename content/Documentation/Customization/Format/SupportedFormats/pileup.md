+++
title = "ANNNOVAR variants"
weight = 14
+++
## Pileup Indel

### 1. Sample data

    chr10   57162   D1      G       *       homo    26      3       6
    chr10   62899   I4      AAAA    *       hete    31      17      33
    chr10   85429   I1      A       *       homo    38      29      32
    chr10   87126   I24     TGCATTTACGTGATCTTGGCTCAC        *       hete    51      10      38
    chr10   87668   D3      CTC     *       hete    52      27      34
    chr10   89301   D1      A       *       hete    37      7       45
    chr10   89448   I3      AGG     *       hete    27      4       31
    chr10   93681   I1      G       *       hete    21      12      111
    chr10   94117   I3      CAA     *       hete    29      29      81
    chr10   94848   D3      TTA     *       hete    54      7       48
    chr10   95775   I1      T       *       hete    44      6       44
    chr10   97572   D1      T       *       hete    44      8       55
    chr10   98719   I1      T       *       hete    48      13      39
    chr10   99022   I1      T       *       homo    52      19      36
    chr10   100224  D6      CCCTAA  *       hete    41      12      31
    chr10   100433  D6      ACCCTC  *       hete    50      2       20
    chr10   100799  I1      G       *       hete    50      4       22
    chr10   101382  D1      G       *       hete    54      12      39
    chr10   101729  D3      GTA     *       hete    51      19      58
    chr10   103093  D1      T       *       homo    57      23      33
    chr10   103731  D2      GA      *       hete    46      6       28
    chr10   106207  D9      TTGTTTTTG       *       hete    46      6       24
    chr10   106216  D4      TTTT    *       homo    49      11      19
    chr10   107344  I1      C       *       hete    54      6       32
    chr10   108119  I1      G       *       hete    31      7       19
    chr10   108176  I1      A       *       hete    46      3       22
    chr10   110565  D2      AA      *       hete    47      4       11
    chr10   110582  D2      AG      *       hete    51      2       13
    chr10   110806  D7      TTTTTTT *       hete    55      5       14
    chr10   110829  I3      GGG     *       hete    45      2       13
    chr10   111125  I1      T       *       homo    52      11      14
    chr10   112581  D2      CC      *       homo    30      8       8
    chr10   113972  D1      G       *       hete    56      7       40
    chr10   114040  I1      A       *       hete    57      4       33
    chr10   114710  D1      C       *       hete    56      4       28
    chr10   117629  I8      CCAGATCC        *       hete    42      4       27
    chr10   123201  D1      C       *       homo    58      20      22
    



### 2. Format description

    vtools show format pileup_indel
    
    INFO: Opening project test.proj
    Format:      pileup_indels
    Description: Input format for samtools pileup indel caller. This format imports
        chr, pos, ref, alt and genotype.
    
    variant fields:
      chr:    Chromosome name
      pos:    Start position of the indel event.
      ref:    reference allele, '-' for insertion
      alt:    alternative allele, '-' for deletion
    
    Genotype field:
       genotype:    type of indel (homozygote or heterozygote)
    



### 3. Example

    vtools import --format pileup_indel pileup.indel --build hg18 

    INFO: Opening project test.proj
    INFO: Additional genotype fields: genotype
    INFO: Importing genotype from pileup.indel (1/1)
    DEBUG: Creating table sample
    pileup.indel: 30
    INFO: 30 new variants from 30 records are imported, with 0 SNVs, 14 insertions, 16 deletions, and 0 complex variants.
    

    vtools show table variant -l -1
    
    INFO: Opening project test.proj
    variant_id, bin, chr, pos, ref, alt
    1, 585, 10, 57162, G, -
    2, 585, 10, 62899, -, AAAA
    3, 585, 10, 85429, -, A
    4, 585, 10, 87126, -, TGCATTTACGTGATCTTGGCTCAC
    5, 585, 10, 87668, CTC, -
    6, 585, 10, 89301, A, -
    7, 585, 10, 89448, -, AGG
    8, 585, 10, 93681, -, G
    9, 585, 10, 94117, -, CAA
    10, 585, 10, 94848, TTA, -
    11, 585, 10, 95775, -, T
    12, 585, 10, 97572, T, -
    13, 585, 10, 98719, -, T
    14, 585, 10, 99022, -, T
    15, 585, 10, 100224, CCCTAA, -
    16, 585, 10, 100433, ACCCTC, -
    17, 585, 10, 100799, -, G
    18, 585, 10, 101382, G, -
    19, 585, 10, 101729, GTA, -
    20, 585, 10, 103093, T, -
    21, 585, 10, 103731, GA, -
    22, 585, 10, 106207, TTGTTTTTG, -
    23, 585, 10, 106216, TTTT, -
    24, 585, 10, 107344, -, C
    25, 585, 10, 108119, -, G
    26, 585, 10, 108176, -, A
    27, 585, 10, 110565, AA, -
    28, 585, 10, 110582, AG, -
    29, 585, 10, 110806, TTTTTTT, -
    30, 585, 10, 110829, -, GGG
