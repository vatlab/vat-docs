+++
title = "mut_sequence"
description = ""
weight = 2
+++



# Mutated sequence around variant site




## Usage

Function `mut_sequence(chr, start, end)` returns the mutated sequence between `start` and `end` on chromosome `chr` of the reference genome (primary reference genome unless parameter `--build` is used to specify an alternative reference genome). If `end` is unspecified, `mut_sequence(chr, pos)` returns the mutated allele at the specified location. 

Simply put, function `mut_sequence` in 



    % vtools output variant chr pos 'mut_sequence(chr, pos)'
    

returns the alternative allele at the variant site for SNPs, `-` for deletion, and `XXXR` for insertion of `XXX` before reference allele `R`. 



    % vtools output variant chr pos 'mut_sequence(chr, pos, pos+5)'
    

returns the 5-base sequence at and after the variant sites with the variant for all variants in the master variant table. 



Function `mut_sequence` will be identical to `ref_sequence` if the variant is outside of the specified region (e.g. different `chr`). 



## Details

(:toggleexample Examples: output mutated sequence around variants:) Let us get a test project 

    % vtools admin --load_snapshot vt_simple
    

    Downloading snapshot vt_simple.tar.gz from online
    INFO: Snapshot vt_simple has been loaded
    

It is not very useful but we can see the mutated sequence at the variant location, 

    % vtools output variant chr pos ref alt 'mut_sequence(chr, pos)' -l 10
    

    1	4540 	G	A	A
    1	5683 	G	T	T
    1	5966 	T	G	G
    1	6241 	T	C	C
    1	9992 	C	T	T
    1	9993 	G	A	A
    1	10007	G	A	A
    1	10098	G	A	A
    1	14775	G	A	A
    1	16862	A	G	G
    

It is more useful to see the context of the variants 



    % vtools output variant chr pos ref alt 'ref_sequence(chr, pos-1, pos+1)' 'mut_sequence(chr, pos-1, pos+1)' -l 10
    

    1	4540 	G	A	GGA	GAA
    1	5683 	G	T	TGC	TTC
    1	5966 	T	G	GTG	GGG
    1	6241 	T	C	ATG	ACG
    1	9992 	C	T	GCG	GTG
    1	9993 	G	A	CGG	CAG
    1	10007	G	A	GGC	GAC
    1	10098	G	A	CGA	CAA
    1	14775	G	A	CGT	CAT
    1	16862	A	G	GAA	GGA
    

Let us import some indels 



    % vtools init test -f
    % vtools import SAMP3_complex_variants.vcf --build hg19
    

    INFO: Importing variants from /Users/bpeng1/vtools/test/vcf/SAMP3_complex_variants.vcf (1/1)
    SAMP3_complex_variants.vcf: 100% [=======================] 184 20.8K/s in 00:00:00
    INFO: 135 new variants (1 SNVs, 77 insertions, 58 deletions, 7 complex variants) from 184 lines are imported.
    Importing genotypes: 0 0.0/s in 00:00:00                                                                                                                                                                                                                                                            
    Copying samples: 0 0.0/s in 00:00:00      
    

and check how the sequences are affected 



    % vtools output variant chr pos ref alt 'ref_sequence(chr, pos-1, pos+1)' 'mut_sequence(chr, pos-1, pos+1)' -l 10
    

    1	10434	-  	C             	ACC	ACCC
    1	10440	C  	-             	ACC	A-C
    1	54788	C  	-             	TCC	T-C
    1	54790	-  	T             	CTT	CTTT
    1	63737	TAC	-             	CTA	C--
    1	63738	ACT	CTA           	TAC	TCT
    1	81963	-  	AA            	TAA	TAAAA
    1	82134	-  	AAAAAAAAAAAAAA	CAA	CAAAAAAAAAAAAAAAA
    1	82134	A  	-             	CAA	C-A
    1	83119	A  	-             	CAA	C-A
    

(:exampleend:)