+++
title = "ANNNOVAR"
weight = 8
+++

## Importing ANNOVAR input file

### 1. Format description

<http://www.openbioinformatics.org/annovar/annovar_input.html> 

*"ANNOVAR takes text-based input files, where each line corresponds to one variant. On each line, the first five space- or tab- delimited columns represent chromosome, start position, end position, the reference nucleotides and the observed nucleotides. Additional columns can be supplied and will be printed out in identical form. For convenience, users can use “0” to fill in the reference nucleotides, if this information is not readily available. Insertions, deletions or block substitutions can be readily represented by this simple file format, by using “–” to represent a null nucleotide. One example is given below (this example is included as ex1.human file in the ANNOVAR package), with extra columns that serve as comments on the variants. By default, 1-based coordinate system will be assumed; if --zerostart argument is issued, a half-open zero-based coordinate system will be used in ANNOVAR instead."* 



### 2. Sample input

    1 161003087 161003087 C T comments: rs1000050, a SNP in Illumina SNP arrays
    1 84647761 84647761 C T comments: rs6576700 or SNP_A-1780419, a SNP in Affymetrix SNP arrays
    1 13133880 13133881 TC - comments: rs59770105, a 2-bp deletion
    1 11326183 11326183 - AT comments: rs35561142, a 2-bp insertion
    1 105293754 105293754 A ATAAA comments: rs10552169, a block substitution
    1 67478546 67478546 G A comments: rs11209026 (R381Q), a SNP in IL23R associated with Crohn's disease
    2 233848107 233848107 T C comments: rs2241880 (T300A), a SNP in the ATG16L1 associated with Crohn's disease
    16 49303427 49303427 C T comments: rs2066844 (R702W), a non-synonymous SNP in NOD2
    16 49314041 49314041 G C comments: rs2066845 (G908R), a non-synonymous SNP in NOD2
    16 49321279 49321279 - C comments: rs2066847 (c.3016_3017insC), a frameshift SNP in NOD2
    13 19661686 19661686 G - comments: rs1801002 (del35G), a frameshift mutation in GJB2, associated with hearing loss
    13 19695176 20003944 0 - comments: a 342kb deletion encompassing GJB6, associated with hearing loss
    



### 3. How to import

Saving the above example file as `ex1.human`, one can import it using command 



    vtools import --format ANNOVAR ex1.human --build hg18
    
    INFO: Importing genotype from ex1.human (1/1)
    ex1.human: 12
    INFO: 0 new variants from 11 records are imported, with 0 SNVs, 0 insertions,
    0 deletions, and 0 complex variants. 1 invalid records are ignored
    

The inputted variants can be displayed using 



    vtools output variant chr pos ref alt
    
    1	161003087	C	T
    1	84647761	C	T
    1	13133880	TC	-
    1	11326183	-	AT
    1	105293755	-	TAAA
    1	67478546	G	A
    2	233848107	T	C
    16	49303427	C	T
    16	49314041	G	C
    16	49321279	-	C
    13	19661686	G	-
    



variant tools does not recognize missing reference allele in the last line of input (a large deletion) and only imports 11 variants from the input file. 

See an [export][1] example.

 [1]: http://varianttools.sourceforge.net/Vtools/Export#toc4
