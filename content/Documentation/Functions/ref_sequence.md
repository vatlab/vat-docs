+++
title = "ref_sequence"
weight = 1
+++


## Reference sequence around variant site



### 1. Usage

Function `ref_sequence(chr, start, end)` returns the reference sequence between `start` and `end` on chromosome `chr` of the reference genome (primary reference genome unless parameter `--build` is used to specify an alternative reference genome). If `end` is unspecified, `ref_sequence(chr, pos)` returns the reference allele at the specified location. This function is very useful in output the context of variants or select variants based on the contexts (e.g. select variants in CpG islands). 

Simply put, function `ref_sequence` in 



    % vtools output variant chr pos 'ref_sequence(chr, pos)'
    

returns the nucleotide at the variant site, and 



    % vtools output variant chr pos 'ref_sequence(chr, pos, pos+5)'
    

returns the 5-base sequence at and after the variant sites, for all variants in the master variant table. 



### 2. Details

<details><summary> Examples: output reference sequence around variants</summary> Let us get a test project 

    % vtools admin --load_snapshot vt_simple   

    Downloading snapshot vt_simple.tar.gz from online
    INFO: Snapshot vt_simple has been loaded
    

We can check if the imported reference alleles is consistent with the reference genome: 



    % vtools output variant chr pos ref 'ref_sequence(chr, pos)' -l 10

    1	4540	G	G
    1	5683	G	G
    1	5966	T	T
    1	6241	T	T
    1	9992	C	C
    1	9993	G	G
    1	10007	G	G
    1	10098	G	G
    1	14775	G	G
    1	16862	A	A
    

This means that we used the correct build of reference genome to import the data (c.f. `vtools admin --validate_build`). If we are interested in the up and down stream sequence of variants, we can use function `ref_sequence`, 



    % vtools output variant chr pos ref 'ref_sequence(chr, pos-5, pos+5)' -l 10
    
    1	4540	G	GGGGGGAAGGT
    1	5683	G	CTGCTGCTTCT
    1	5966	T	GTGTGTGGGGG
    1	6241	T	AGGAATGGGGA
    1	9992	C	GGCCGCGGTGA
    1	9993	G	GCCGCGGTGAG
    1	10007	G	CAGGGGCCAGC
    1	10098	G	ATCTCGAGTCA
    1	14775	G	GGAGCGTCAGA
    1	16862	A	CCAGGAAGGTG
    

Now, if you are interested in checking if the variants happen in a region with high concentration of reference alleles (e.g. a repeatitive region), you can use an expression to calculate the concentration of reference allele in the region. For example, the following expression first gets the reference sequence of length 11 around the variant (`(ref_sequence(chr, pos-5, pos+5)`), remove all occurance of reference allele (`replace(SEQ, ref, "")`, and count the number of remaining alleles: 



    % vtools update variant --set 'nRef=11-length(replace(ref_sequence(chr, pos-5, pos+5), ref, ""))'

    INFO: Adding variant info field nRef
    

The resulting new column `nRef` records the number of reference alleles in the 11 basepair regions around the variants: 



    % vtools output variant chr pos ref 'ref_sequence(chr, pos-5, pos+5)' nRef -l 10
    
    1	4540	G	GGGGGGAAGGT	8
    1	5683	G	CTGCTGCTTCT	2
    1	5966	T	GTGTGTGGGGG	3
    1	6241	T	AGGAATGGGGA	1
    1	9992	C	GGCCGCGGTGA	3
    1	9993	G	GCCGCGGTGAG	6
    1	10007	G	CAGGGGCCAGC	5
    1	10098	G	ATCTCGAGTCA	2
    1	14775	G	GGAGCGTCAGA	5
    1	16862	A	CCAGGAAGGTG	3
    

</details>