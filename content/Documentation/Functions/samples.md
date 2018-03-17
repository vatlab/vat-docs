+++
title = "samples"
description = ""
weight = 5
+++


# Samples that harbor the variant




## Usage

The `samples` function is similar to `genotype` but it returns name of samples that contain the variant. When you use the function in command `vtools output var_table samples()`, this function will be evaluated for each variant in the variant table `var_table`. In its basic form, 



    samples()
    

returns a list of comma-separated names of samples that contain the variant, regardless the type of variant (homozygote etc). 



This function returns all samples that contain the variant, so it will return samples without genotype info (no `GT` column, and samples with homozygote wildtype allele (genotype with `GT=0`) as long as the variant is included in the sample. 



## Details

The `samples` function accepts an optional parameter with `&` separated `KEY=VAL` pairs. Supported `KEY` include 



*   `sample_filter`. A condition to select samples, using sample names of phenotype (e.g. `aff=1`). (c.f. command `vtools show samples` or `vtools show phenotypes`) 
*   `geno_filter`. Select samples by type of variant in the sample, using genotype type (`GT`) or genotype info fields (e.g. `DP_geno`). (c.f. command `vtools show genotypes`). For example, if you use condition `GT=2`, only samples with homozygote alternative alleles will be returned. 
*   `delimiter`. Delimiter to seprate sample names, default to `,`. You can set it to `\t` to output tab separated lists. 

For example, command 



    samples()
    samples('sample_filter=aff=1')
    samples('geno_filter=GT=1')
    

returns the 

1.  name of samples that contains the variant, 
2.  name of samples with phenotype `aff=1` (cases) that contains the variant 
3.  name of samples that contains heterzygote genotype of the variant. You can use condition `GT!=0` to output samples with only non-wildtype genotypes. 

(:toggleexample Examples: Use `samples` function to get samples that contain the variant:) Continue to use the project from the previous example, let us see which samples that contain the variants 



    % vtools admin --load_snapshot vt_simple
    % vtools admin --rename_samples "filename='V2.vcf'" SAMP2
    % vtools admin --rename_samples "filename='V3.vcf'" SAMP3
    % vtools output variant chr pos ref alt "samples()" -l 10
    

    1	4540 	G	A	SAMP1,SAMP3
    1	5683 	G	T	SAMP1
    1	5966 	T	G	SAMP1,SAMP2,SAMP3
    1	6241 	T	C	SAMP1,SAMP3
    1	9992 	C	T	SAMP1,SAMP3
    1	9993 	G	A	SAMP1,SAMP3
    1	10007	G	A	SAMP1,SAMP2,SAMP3
    1	10098	G	A	SAMP1
    1	14775	G	A	SAMP1,SAMP3
    1	16862	A	G	SAMP1,SAMP3
    

Just to show the results from `genotype()` and `samples()` match each other: 



    % vtools output variant chr pos ref alt "genotype('SAMP1')" "genotype('SAMP2')" \
        "genotype('SAMP3')" "samples()"  -l 10
    

    1	4540 	G	A	1	.	1	SAMP1,SAMP3
    1	5683 	G	T	1	.	.	SAMP1
    1	5966 	T	G	1	1	1	SAMP1,SAMP2,SAMP3
    1	6241 	T	C	1	.	1	SAMP1,SAMP3
    1	9992 	C	T	1	.	1	SAMP1,SAMP3
    1	9993 	G	A	1	.	1	SAMP1,SAMP3
    1	10007	G	A	1	1	1	SAMP1,SAMP2,SAMP3
    1	10098	G	A	2	.	.	SAMP1
    1	14775	G	A	2	.	2	SAMP1,SAMP3
    1	16862	A	G	2	.	2	SAMP1,SAMP3
    

You can limit the samples to those with a particular type of genotype 



    % vtools output variant chr pos ref alt "genotype('SAMP1')" "genotype('SAMP2')" \
        "genotype('SAMP3')" "samples('geno_filter=GT=2')"  -l 10
    

    1	4540 	G	A	1	.	1	.
    1	5683 	G	T	1	.	.	.
    1	5966 	T	G	1	1	1	.
    1	6241 	T	C	1	.	1	.
    1	9992 	C	T	1	.	1	.
    1	9993 	G	A	1	.	1	.
    1	10007	G	A	1	1	1	.
    1	10098	G	A	2	.	.	SAMP1
    1	14775	G	A	2	.	2	SAMP1,SAMP3
    1	16862	A	G	2	.	2	SAMP1,SAMP3
    

(:exampleend:) 



Because this function needs to scan the whole genotype tables of samples for each variant, it is expected to be much slower than batch operations that process all genotypes. For example, it would be much faster to export genotypes in batch (e.g. using command `vtools export` to export variants and genotypes in csv or vcf formats) if you need to list genotypes of a large number of variants.