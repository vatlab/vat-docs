+++
title = "Other functions"
description = ""
weight = 7
+++


# Other customized SQL functions



## `vcf_variant`: Output variants in vcf format with padding alleles 

Function `vcf_variant(chr, pos, ref, alt, name=".")` returns a string that represent variants in vcf format. If the variant is a SNV, the output merely connects input by tab ('\t'). If the variant is an indel, it will pad reference (for insertion) or alternative (for deletion) allele with the allele before variant, adjust position, and generate an output that is acceptable by vcf. For example, if the variant is 



    1	9468278	G	-
    1	9468279	-	GA
    

Function `vcf_variant(chr, pos, ref, alt, dbSNP.name)` will produce 



    1	9468277	rs111651373	GG	G
    1	9468278	rs111651373	G	GGA
    

for these variants. Here `dbSNP.name` is used to add rsname to the output. You can use a contant `"."` if dbSNP is not available. If no name is specified, the output will have only four columns. 

(:toggleexample Examples: output indels with padding alleles:) Because the SNV case is simple, let us import some indels from an online snapshot 



    % vtools init test -f
    % vtools admin --load_snapshot vt_testData
    % vtools import indels.vcf --build hg19
    

    INFO: Importing variants from indels.vcf (1/1)
    indels.vcf: 100% [======================================================================] 184 15.4K/s in 00:00:00
    INFO: 137 new variants (1 SNVs, 77 insertions, 58 deletions, 7 complex variants) from 184 lines are imported.
    Importing genotypes: 0 0.0/s in 00:00:00
    Copying samples: 0 0.0/s in 00:00:00
    

The variants in vcf files are 



    % sort indels.vcf -n -k2 | tail -5 | cut -f1-5
    

    1	819516	rs71315270	A	AT
    1	819612	rs34487673	TC	T
    1	819612	rs71315271	TC	T
    1	819703	rs111948412	TC	T,TCTATGTGTC
    1	819703	rs77305433	TCTATGTGTCT	T,TCTATGTGTC
    

If we output the variants, we can see that the padding alleles are removed, the positions have been adjusted, duplicates are removed (even if they have different rsnames) and variants are separated: 



    % vtools output variant chr pos ref alt --order_by chr pos | tail -6
    

    1	819517	-	T
    1	819613	C	-
    1	819704	CTATGTGTCT	-
    1	819704	C	-
    1	819705	-	TATGTGTC
    1	819713	T	-
    

We can output the variants in vcf format using function `vcf_variant`, 



    % vtools output variant 'vcf_variant(chr, pos, ref, alt)' --order_by chr pos | tail -6
    

    1	819516	A	AT
    1	819612	TC	T
    1	819703	TCTATGTGTCT	T
    1	819703	TC	T
    1	819704	C	CTATGTGTC
    1	819712	CT	C
    

The result does not match lines in the vcf exactly, because variants at different positions are not combined, and a padding of length 1 is used. 

Anyway, to produce vcf-like output, a name is needed. We can use a default value `"."`, 



    % vtools output variant 'vcf_variant(chr, pos, ref, alt, ".")' --order_by chr pos | tail -6
    

    1	819516	.	A	AT
    1	819612	.	TC	T
    1	819703	.	TCTATGTGTCT	T
    1	819703	.	TC	T
    1	819704	.	C	CTATGTGTC
    1	819712	.	CT	C
    

or name from dbSNP 



    % vtools use dbSNP
    % vtools output variant 'vcf_variant(chr, pos, ref, alt, dbSNP.name)' --order_by chr pos | tail -6
    

    1	819516	rs71315270	A	AT
    1	819612	rs34487673	TC	T
    1	819703	rs77305433	TCTATGTGTCT	T
    1	819703	rs148493754	TC	T
    1	819704	rs148493754	C	CTATGTGTC
    1	819712	rs77305433	CT	C
    

For variants with multiple entries in the `dbSNP` database, we can use option `--all` to output all of them 



    % vtools output variant 'vcf_variant(chr, pos, ref, alt, dbSNP.name)' --order_by chr pos --all | tail -8
    

    1	819516	rs71315270	A	AT
    1	819612	rs34487673	TC	T
    1	819703	rs77305433	TCTATGTGTCT	T
    1	819703	rs111948412	TC	T
    1	819703	rs148493754	TC	T
    1	819704	rs111948412	C	CTATGTGTC
    1	819704	rs148493754	C	CTATGTGTC
    1	819712	rs77305433	CT	C
    

(:exampleend:) 

 

## `least_not_null`: a version of `min(x,y)` that ignores `NULL` 

This function is similar to `min(x,y,...)` but it ignores `NULL` values so `least(2, NULL, 4)` returns `2`. 

 

## `HWE_exact`: exact Tests of Hardy-Weinberg Equilibrium 

Special function `HWE_exact` implements a bi-allelic HWE exact test based on equation 2 of [this paper][1]. It requires 3 fields as input: 



*   `total`: total number of genotypes 
*   `het`: number of heterozygote (genotype 0/1 or 0/2) 
*   `hom`: number of homozygote (genotype 1/1 or 2/2) 

and an optional field: 



*   `other`: number of heterozygote with two alternative alleles (genotype 1/2, which is rarely observed in sequencing data) 

If the optional field `other` is specified, then genotype 1/2 will be collapsed with genotype 1/1 or 2/2 to maintain a bi-allelic system. Otherwise it will be ignored (treated as homozygote wildtype). The resulting field is p-value of the test. 

(:toggleexample Examples: test of Hardy-Weinberg Equilibrium:) We can calculate HWE p-value based on existing fields `total`, `het`, and `hom`, 

    % vtools update variant --set "hwe=HWE_exact(total, het, hom)"
    

    INFO: Adding field hwe
    

Because of the small sample size, there are not many choices for p-values: 

    % vtools output variant chr pos ref alt hwe -l5
    

    1	4540	G	A	1.0
    1	5683	G	T	1.0
    1	5966	T	G	0.4
    1	6241	T	C	1.0
    1	9992	C	T	1.0
    

(:exampleend:) 

 

## `Fisher_exact`: Fisher's exact test for case/ctrl associaiton 

The function `Fisher_exact(num_var_alleles_case, num_var_alleles_ctrl, 2*num_gt_case, 2*num_gt_ctrl)` tests for association of an alternate allele with a phenotype (i.e., case or control) status. Given a variant site to be tested, the function takes in the following 4 parameters, that are obtainable through `vtools` functions: 



*   `num_var_alleles_case`: number of alternative alleles for the case samples 
*   `num_var_alleles_ctrl`: number of alternative alleles for the control samples 
*   `num_gt_case`: total number of genotypes for the case samples, so twice of the number is total number of alleles for case samples 
*   `num_gt_ctrl`: total number of genotypes for the control samples, so twice of the number is total number of alleles for ctrl samples 

(:toggleexample Examples: Fisher's exact test for case/ctrl association:) To perform Fisher's exact test for case/ctrl association we can try to separate them into cases and controls and calculate statistics separately: 



    % vtools update variant a --from_stat 'num_gt_case=#(GT)' 'num_var_alleles_case=#(alt)' --samples "phen1=1"
    

    INFO: 1000 samples are selected
    Counting variants: 100% [=======================================] 1,000 11.1K/s in 00:00:00
    INFO: Adding field num_var_alleles_case
    INFO: Adding field num_gt_case
    Updating variant: 100% [=======================================] 27 38.3K/s in 00:00:00
    INFO: 26 records are updated
    



    % vtools update variant a --from_stat 'num_gt_ctrl=#(GT)' 'num_var_alleles_ctrl=#(alt)' --samples "phen1=0"
    

    INFO: 1000 samples are selected
    Counting variants: 100% [=====================================] 1,000 11.4K/s in 00:00:00
    INFO: Adding field num_var_alleles_ctrl
    INFO: Adding field num_gt_ctrl
    Updating variant: 100% [======================================] 27 38.8K/s in 00:00:00
    INFO: 26 records are updated
    

And calculate p-value for the Fisher's exact test: 



    % vtools update variant --set "prop_pval=Fisher_exact(num_var_alleles_case, num_var_alleles_ctrl, 2*num_gt_case, 2*num_gt_ctrl)"
    

    INFO: Adding field prop_pval
    

Again, there are not many possible p-values due to small sample size ... 



    % vtools output variant chr pos ref alt prop_pval | sort -k5 | head -5
    

    22	49522870	G	C	0.148032884657
    22	49529883	C	T	0.236820419247
    1	742456	        T	G	0.249812453115
    22	49534747	G	C	0.265775831399
    22	49534781	C	T	0.337597625574
    

(:exampleend:)

 [1]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1199378/