+++
title = "genotype"
weight = 4
+++


## genotypes of one or more samples 



### 1. Usage

##### This function is only supported when STOREMODE is set to sqlite. 

Genotype information for a variant is not directly available in variant tools commands such as `vtools output` because these commands only output variant info or annotation fields. Function `genotype` can be used to retrieve genotypes of one or more samples from the genotype tables. In its single-sample mode, this function accepts a sample name and an optional field to display, 



    genotype(sample_name, params='')
    

where params can have be multiple parameters joined by `&`. For example, functions 



    genotype('WGS1')
    genotype('WGS1', 'field=DP')
    

returns the genotype (0 for homozygous wild type, 1 for heterzygous alternative, 2 for homozygous alternative, and -1 for one of the double alternative alleles) or genotype field `DP` of sample `WGS1`. `'.'` will be returned if sample `WGS1` does not contain the variant. 



### 2. Details

<details><summary> Examples: Use `genotype` function to get genotypes of samples</summary> 

Let us get a simple project and name the samples properly 

    % vtools admin --load_snapshot vt_simple
    % vtools admin --rename_samples "filename='V2.vcf'" SAMP2
    % vtools admin --rename_samples "filename='V3.vcf'" SAMP3
    % vtools show samples
    

    sample_name	filename
    SAMP1      	V1.vcf
    SAMP2      	V2.vcf
    SAMP3      	V3.vcf
    

There are about 1000 genotypes in three samples: 



    % vtools show genotypes
    

    sample_name	filename	num_genotypes	sample_genotype_fields
    SAMP1      	V1.vcf  	989          	GT
    SAMP2      	V2.vcf  	990          	GT
    SAMP3      	V3.vcf  	988          	GT
    

Now, in addition to the variant inforation, we would like to see the genotype of variants in sample `SAMP1` 



    % vtools output variant chr pos ref alt "genotype('SAMP1')" -l 10
    

    1	4540 	G	A	1
    1	5683 	G	T	1
    1	5966 	T	G	1
    1	6241 	T	C	1
    1	9992 	C	T	1
    1	9993 	G	A	1
    1	10007	G	A	1
    1	10098	G	A	2
    1	14775	G	A	2
    1	16862	A	G	2
    

The `genotype` can also be used to select variants. For example, the following command select variants when their genotypes in `SAMP1` is heterzygous. When we output genotypes of these variants in two samples, some of them are not available in `SAMP2` and are displayed as missing (`.`). 



    % vtools select variant "genotype('SAMP1')=1" --output chr pos ref alt \
        "genotype('SAMP1')" "genotype('SAMP2')" -l 10
    

    1	4540 	G	A	1	.
    1	5683 	G	T	1	.
    1	5966 	T	G	1	1
    1	6241 	T	C	1	.
    1	9992 	C	T	1	.
    1	9993 	G	A	1	.
    1	10007	G	A	1	1
    1	20723	G	C	1	1
    1	29539	C	T	1	.
    1	39161	T	C	1	.
    

In addition to genotype, you can use the `genotype()` funciton to display other genotype info fields (c.f. `vtools show genotypes`, for example, for a project with genotype info field `DP_geno`, we can specify name of the genotype info field as a second parameter: 



    % vtools init genotype -f
    % vtools import CEU.vcf.gz --geno_info DP_geno --build hg18
    % vtools output variant chr pos ref alt "genotype('NA12874')" "genotype('NA12874', 'field=DP_geno')" -l 10
    

    1	533  	G	C	1	9
    1	41342	T	A	0	3
    1	41791	G	A	0	2
    1	44449	T	C	0	0
    1	44539	C	T	0	0
    1	44571	G	C	0	0
    1	45162	C	T	0	1
    1	52066	T	C	1	3
    1	53534	G	A	0	0
    1	75891	T	C	0	0
    

</details>

The first parameter can also be a condition based on which several samples are selected (default to all samples). In this case, this function will return a list of genotypes (for default `field='GT'`) or other fields. Two additional parameters are acceptable (joined by `&`): 



*   `delimiter`: Delimiter, defalt to `,`. 
*   `missing`: If a sample does not contain the variant, output this string instead of ignoreing the sample. 

For example, functions 



    genotype()
    genotype('aff=1')
    genotype('BMI>20', 'field=DP_geno&missing=.')
    

returns genotypes of all samples, samples with `aff=1`, and depth of coverage of of all samples with `BMI > 20`, respectively. 

<details><summary> Examples: Display genotypes of multiple samples</summary> It is straightforward to list genotypes of all samples that contain the variant: 



    % vtools init genotype -f
    % vtools admin --load_snapshot vt_simple
    % vtools import CEU.vcf.gz --geno_info DP_geno --build hg18
    % vtools remove genotypes 'GT=0'
    % vtools output variant chr pos ref alt "genotype()"  -l 10
    

    1	533  	G	C	1,1,1,1,1,1
    1	41342	T	A	1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,1
    1	41791	G	A	1,1,1,1,1
    1	44449	T	C	1,1
    1	44539	C	T	1,1
    1	44571	G	C	1,1,1,1,1,1,1
    1	45162	C	T	1,2,1,1,1,1,2,1,1,1,1,2,1,1,1,2
    1	52066	T	C	1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1
    1	53534	G	A	1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    1	75891	T	C	2,1,2,1,1,1,2,1
    

If you would like to limit the samples, you can pass a condition (c.f. `vtools show samples`) 



    % vtools phenotype --from_file phenotype.txt
    % vtools output variant chr pos ref alt "genotype('BMI>24')"  -l 10
    

    1	533  	G	C	.
    1	41342	T	A	1,1
    1	41791	G	A	1
    1	44449	T	C	.
    1	44539	C	T	.
    1	44571	G	C	1,1,1
    1	45162	C	T	1
    1	52066	T	C	1,1
    1	53534	G	A	1
    1	75891	T	C	2
    

If you need to know which samples have these genotypes, you can use function `samples()` with the same condition. 

    % vtools output variant chr pos ref alt "samples('BMI>24')"  -l 10
    

    1	533  	G	C	.
    1	41342	T	A	NA11918,NA12814
    1	41791	G	A	NA11918
    1	44449	T	C	.
    1	44539	C	T	.
    1	44571	G	C	NA12003,NA12287,NA12751
    1	45162	C	T	NA12814
    1	52066	T	C	NA12003,NA12751
    1	53534	G	A	NA12287
    1	75891	T	C	NA12814
    

Using strings inside the condition is bit tricky because you need to use backslash to pass condition `sex='F'` to the `genotype` function in the following example: 



    % vtools output variant chr pos ref alt "genotype('sex=\'F\'')"  -l 10
    

    1	533  	G	C	1,1,1,1
    1	41342	T	A	1,1,1,1,1,1,1,1,2,1,1,1,1,1
    1	41791	G	A	1,1,1
    1	44449	T	C	1,1
    1	44539	C	T	1,1
    1	44571	G	C	1,1,1,1,1
    1	45162	C	T	1,2,1,1,2,1,1,1,1,1
    1	52066	T	C	1,1,1,1,1,1,1,1,1
    1	53534	G	A	1,1,1,1,1,1,1,1,1,1,1,1,1,1
    1	75891	T	C	2,1,2,1,2
    

Finally, if you would like to view values of other genotype info fields (c.f. `vtools show genotypes`), or using alternative delimiters, you can 



    % vtools output variant chr pos ref alt "genotype('BMI>23', 'field=DP_geno&d=\t&missing=.')"  -l 10
    

    1	533  	G	C	.	.	.	.	.	.	.	.	.	.
    1	41342	T	A	.	1	4	3	.	.	.	.	0	9
    1	41791	G	A	.	2	.	.	.	.	.	.	.	.
    1	44449	T	C	.	.	.	.	.	.	.	.	.	.
    1	44539	C	T	.	.	.	.	.	.	.	.	.	.
    1	44571	G	C	.	.	.	.	1	1	4	1	.	.
    1	45162	C	T	4	.	.	.	.	.	.	.	.	7
    1	52066	T	C	.	.	3	.	1	.	.	1	.	.
    1	53534	G	A	5	.	.	.	.	.	5	.	.	.
    1	75891	T	C	.	.	.	.	.	.	.	.	.	6
    

</details>


{{% notice tip %}}
Whereas the return value of `genotype(sample_name)` is an integer, the return value of `genotype(sample_cond)` is always a string, evern if only one sample is selected by the condition. 
{{% /notice %}}

{{% notice tip %}}
You could match returned genotypes with samples by comparing the output of `genotype(sample_cond)` with the output of `samples(sample_cond)`.
{{% /notice %}}