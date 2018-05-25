+++
title = "basic"
weight = 1
+++

## Importing variants from tab-delimited files

### Format description

    % vtools show format basic
    

    A basic variant import/export format that import variants with four tab-
    delimited columns (chr, pos, ref, alt), and export variants, optional variant
    info fields and genotypes.
    
    Columns:
      1                     Output variant info fields as one column
      2                     variant position, set --pos_adj to -1 to export
                            variants in 0-based positions.
      3                     reference allele
      4                     alternative allele
      5                     genotype in numeric style
    Formatters are provided for fields: gt
    
    variant:
      chr                   Chromosome
      pos                   1-based position, set --pos_adj to 1 if input position
                            is 0 based.
      ref                   Reference allele, '-' for insertion.
      alt                   Alternative allele, '-' for deletion.
    
    Format parameters:
      chr_col               Column index for the chromosome field (default: 1)
      pos_col               Column index for the position field (default: 2)
      ref_col               Column index for the reference field (default: 3)
      alt_col               Column index for the alternative field (default: 4)
      pos_adj               Set to 1 to import variants with 0-based positions, or
                            to -1 to export variants in 0-based positions.
                            (default: 0)
      fields                Fields to output, simple arithmetics are allowed (e.g.
                            pos+1) but aggregation functions are not supported.
                            (default: chr,pos,ref,alt)
    



## Examples

### Import variants with columns chr, pos, ref, and alt

(:toggleexample Examples: create a sample project:) Let us load a project with a few test datasets 

    % vtools init basic 
    % vtools admin --load_snapshot vt_testData
    

    Downloading snapshot vt_testData.tar.gz from online
    INFO: Snapshot vt_testData has been loaded
    

(:exampleend:) 

This format can be used to import variants that are provided as four columns in the input file, 

(:toggleexample Examples: Import variants using format `basic`:) File `variants.txt` has a list of variants as follows 

    % head variants.txt 
    

    1	203148112	T	-
    1	203148168	G	A
    1	203148202	G	C
    1	203148224	G	A
    1	203148265	GG	T
    1	203148284	T	C
    1	203148294	G	T
    1	203148359	C	A
    1	203148360	G	A
    1	203148360	G	C
    

You can import variants using format `basic` as follows: 



    % vtools import variants.txt --format basic --build hg19
    

    INFO: Importing variants from variants.txt (1/1)
    variants.txt: 100% [===============================================] 20 9.9K/s in 00:00:00
    INFO: 20 new variants (17 SNVs, 1 insertions, 1 deletions, 1 complex variants) from 20 lines are imported.
    WARNING: Sample information is not recorded for a file without genotype and sample name.
    Importing genotypes: 0 0.0/s in 00:00:00                                                                                                        
    Copying genotype: 0 0.0/s in 00:00:00 
    

The variants can be displayed using command `vtools output`, 

    % vtools output variant chr pos ref alt -l 10
    

    1	203148112	T	-
    1	203148168	G	A
    1	203148202	G	C
    1	203148224	G	A
    1	203148265	GG	T
    1	203148284	T	C
    1	203148294	G	T
    1	203148359	C	A
    1	203148360	G	A
    1	203148360	G	C
    

(:exampleend:) 

If the chr, pos, ref, alt columns are not columns 1 through 4 in the input file, you can use parameters `chr_col`, `pos_col`, `ref_col`, and `alt_col` to specify the columns of these fields. If the input data uses 0-based position, parameter `pos_adj` can be used to adjust input. 

(:toggleexample Examples: Use parameters --pos_adj to import data in 0-based coordinates:) If the position used in `variants.txt` is zero-based (like all data downloaded from UCSC), you can use format parameter `--pos_adj 1` to add `1` to import positions: 



    % vtools init import -f
    % vtools import variants.txt --format basic --pos_adj 1 --build hg19 
    

    vtools import variants.txt --format basic --pos_adj 1 --build hg19
    INFO: Importing variants from variants.txt (1/1)
    variants.txt: 100% [========================================] 20 758.8/s in 00:00:00
    INFO: 20 new variants (17 SNVs, 1 insertions, 1 deletions, 1 complex variants) from 20 lines are imported.
    WARNING: Sample information is not recorded for a file without genotype and sample name.
    Importing genotypes: 0 0.0/s in 00:00:00
    Copying genotype: 0 0.0/s in 00:00:00
    



    % vtools output variant chr pos ref alt -l 10
    

    1	203148113	T	-
    1	203148169	G	A
    1	203148203	G	C
    1	203148225	G	A
    1	203148266	GG	T
    1	203148285	T	C
    1	203148295	G	T
    1	203148360	C	A
    1	203148361	G	A
    1	203148361	G	C
    

(:exampleend:) 



### Export variants, variants info and genotypes 

If we export data in `basic` format without any parameter, the output is similar to the output of command `vtools output variant chr pos ref alt`, 

(:toggleexample Examples: export variants:) Let us get more variants, 

    % vtools import CEU.vcf.gz --var_info DP
    

    INFO: Using primary reference genome hg18 of the project.
    Getting existing variants: 100% [=======================] 20 30.5K/s in 00:00:00
    INFO: Importing variants from CEU.vcf.gz (1/1)
    CEU.vcf.gz: 100% [=====================================] 300 16.8K/s in 00:00:00
    INFO: 288 new variants (288 SNVs) from 300 lines are imported.
    Importing genotypes: 100% [==========================] 18,000 9.0K/s in 00:00:02
    Removing duplicates: 100% [===========================] 120 445.8K/s in 00:00:00
    Copying samples: 100% [===============================] 120 558.0K/s in 00:00:00
    

Then export variants in `basic` format, 



    % vtools export variant --format basic > bb
    

    Writing: 100% [========================================] 308 32.4K/s in 00:00:00
    INFO: 308 lines are exported from variant table variant
    



    % head -5 bb
    

    1	203148112	T	-
    1	203148168	G	A
    1	203148202	G	C
    1	203148224	G	A
    1	203148265	GG	T
    

(:exampleend:) 

You can specify more fields, even annotation fields, through parameter `--fields` 

(:toggleexample Examples: export variant info fields:) 



    % vtools use dbSNP-hg18_130
    % vtools export variant --fields DP dbSNP.name --format ~/vtools/format/basic > bb
    

    Writing: 100% [========================================] 308 29.3K/s in 00:00:00
    INFO: 308 lines are exported from variant table variant
    

You can see the output has six columns, with depth (field `DP`) and rsname (field `dbSNP.name`) as the last two columns. Note that missing entries are displayed as empty string. 



    % head -30 bb
    

    1	203148112	T	-
    1	203148168	G	A
    1	203148202	G	C
    1	203148224	G	A
    1	203148265	GG	T
    1	203148284	T	C
    1	203148294	G	T
    1	203148359	C	A
    1	203148360	G	A
    1	203148360	G	C
    1	203148510	G	T
    1	203148513	A	T
    1	203148633	A	G
    1	203148677	T	C
    1	203148727	C	T
    1	203148868	T	C
    1	203148989	-	C
    10	58118181	A	C
    10	58118185	C	T
    10	58120990	C	T
    1	533	G	C	423
    1	41342	T	A	188
    1	41791	G	A	192
    1	44449	T	C	166
    1	44539	C	T	131	rs2462492
    1	44571	G	C	135
    1	45162	C	T	166	rs10399749
    1	52066	T	C	159	rs28402963
    1	53534	G	A	243
    1	75891	T	C	182
    

(:exampleend:) 

The `basic` format can also be used to export genotypes, 

(:toggleexample Examples: export genotypes :) This example select 8 samples using condition ` 'sample_name like "NA128%"'`, 



    % vtools select variant --samples 1 -t inSamples
    % vtools export inSamples --samples 'sample_name like "NA128%"'  --format ~/vtools/format/basic > bb
    

    INFO: Genotypes of 8 samples are exported.
    Writing: 100% [========================================] 288 10.6K/s in 00:00:00
    INFO: 288 lines are exported from variant table inSamples
    



    % head -5 bb
    

    1	533	G	C		0	0	0	1	0		1	1
    1	41342	T	A		0	0	1	1	0		0	0
    1	41791	G	A		0	0	0	0	0		0	0
    1	44449	T	C		1	0	0	0	0		0	0
    1	44539	C	T		1	0	0	0	0		0	0
    

(:exampleend:) 

The `--header` option can be used to specify a header, with `%(sample_names)s` being replaced by names of samples, 

(:toggleexample Examples: specify a header to exported file:) 

    % vtools export inSamples --samples 'sample_name like "NA128%"'  --format ~/vtools/format/basic --header chr pos ref alt "%(sample_names)s" > bb
    

    INFO: Genotypes of 8 samples are exported.
    Writing: 100% [========================================] 288 12.9K/s in 00:00:00
    INFO: 288 lines are exported from variant table inSamples
    



    % head -5 bb
    

    chr	pos	ref	alt	NA12812	NA12813	NA12814	NA12815	NA12828	NA12872	NA12873	NA12874
    1	533	G	C		0	0	0	1	0		1	1
    1	41342	T	A		0	0	1	1	0		0	0
    1	41791	G	A		0	0	0	0	0		0	0
    1	44449	T	C		1	0	0	0	0		0	0
    

(:exampleend:)
