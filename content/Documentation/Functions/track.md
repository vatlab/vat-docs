+++
title = "track"
weight = 3
+++


## Extract annotation from external files


### 1. Usage

Function `track(filename, field)` returns annotation information at column `col` (optional) in file `filename`, at position (`chr`, `pos` at primary or alternative reference genome) of each variant. For example, function 



    % vtools output variant chr pos ref alt "track('1000g.vcf.gz', 'info')"
    


{{% notice tip %}}
single quote (`'`) should be used for string literals in SQL functions. Double quote (`"`) should be avoided although it sometimes works. 
{{% /notice%}}

output the "info" column of file `1000g.vcf.gz`, for variants at location `chr` and `pos`. 

This function currently accepts four types of track files: 



1.  Local or online `bgzipped` and `tabix`-indexed vcf files with extension `.vcf.gz`. 
2.  [`bigWig`][1] files that provides dense and continuous data for a region. 
3.  [`bigBed`][2] files with 3 required columns and 9 optional columns. Annotation tracks in BED format can be converted to this format using program `bedToBigBed`. 
4.  Local or online indexed BAM files with extension `.bam`. This format does not contain 'columns' as other formats do but it provides alignment information for the variants. 

The allowed and default values of the second option `field` vary for different file formats. Generally speaking, numeric values such as `1`, `2`, ... returns the `col`-th column of the input data file, with the exception that `` returns `1` (match or not) for all matched records. String values such as `"chrom"`, `"chromStart"`, `"info"` return values at specified column as strings. 



### 2. Details

#### 2.1 Display information about tracks

Before you use each track, it is important to run command 



    % vtools show track FilenameOrURL
    

to get the detailed information about the track file, and the available fields and their types. 


{{% notice tip%}}
As a shortcut to enter `track` function for multiple files, you can use wildcast characters in the first parameter (`filename`) of the `track` function. This will result in multiple `track()` function calls for each matching filename. For example, if you have `A01.BAM` and `A02.BAM` in the current directory, function `track('A*.BAM', 'calls')` is equivalent to `track('A01.BAM', 'calls') track('A02.BAM', 'calls')`. 
{{% /notice%}}

{{% notice tip%}}
The return values of the returned field will be numeric if the column contains numeric data (e.g. flag, score, position). **Only the first record will be returned if a variant matches multiple records in the track file**. If an option `all=1` is passed to field (e.g. `track('my.bam', 'info?all=1')`), the `track` function will output all matching records as string, separated by a delimiter `|`. 
{{% /notice%}}

{{% notice tip%}}
This function automatically chooses correct chromosome name (adding `chr` to chromosome name if needed), and position (adjust to 0-based position if needed) to match records in the track file.
{{% /notice%}}

{{% notice tip%}}
The return values are not adjusted. That is to say, columns such as `pos` will be 0-based for 0-based track files (e.g. bigBed files), and 1-based for 1-based track files (e.g. vcf). 
{{% /notice%}}

Please refer to [here][3] for more details of command vtools show, especially a brief description of the BAM header. 

 

#### 2.2 Tabixed vcf tracks

VCF files that can be used as tracks must be bgzipped and tabix-indexed. Regular vcf files can be converted to this format using commands `bgzip my.vcf` and `tabix -p vcf my.vcf.gz`. Parameter `col` for this format can be `1` (chrom), `2` (start, 1-based), `3` (name), `4` (ref), `5` (alt alleles), `6` (qual), `7` (filter), `8` (info), `9` (format string), `10` and more (for genotype columns for sample `col-9`); names of the columns `"chrom"`, `"pos"`, `"name"`, `"ref"`, `"alt"`, `"qual"`, `"filter"`, `"info"`, `"format"`; name of information fields available in the vcf file in the format of `info.FIELD`; name of samples for genotype columns, and name of genotype info fields in the format of `SAMPLE.FIELD`. If no `col` is specified, a default value `8` is passed to display the full `INFO` column of the vcf file. 

<details><summary> Examples: Annotate variants using vcf tracks</summary> Let us get some test data, and index the vcf file using the `tabix` program 

    % vtools init track
    % tabix -p vcf CEU_hg38.vcf.gz
    % vtools import CEU_hg38.vcf.gz --build hg38
    
    INFO: Importing variants from CEU_hg38.vcf.gz (1/1)
    CEU_hg38.vcf.gz: 100% [===================================] 306 10.4K/s in 00:00:00
    INFO: 292 new variants (292 SNVs) from 306 lines are imported.
    Importing genotypes: 100% [================================] 292 2.7K/s in 00:00:00

    

The track information can be displayed using command 



    % vtools show track CEU.vcf.gz | head -30   

    Version                 VCF v4.0
    Number of fields:       69
    
    Header: (exclude INFO and FORMAT lines)
                            ##reference=human_b36_both.fasta
                            ##rsIDs=dbSNP b129 mapped to NCBI 36.3, August 10, 2009
    
    Available columns (with type VARCHAR if unspecified or all=1):
    0 (INTEGER)             1 if matched
    chr (1, chrom)          chromosome
    pos (2, INTEGER)        position (1-based)
    name (3)                name of variant
    ref (4)                 reference allele
    alt (5)                 alternative alleles
    qual (6)                qual
    filter (7)              filter
    info (8, default)       variant info fields
    info.DP (INTEGER)       Total Depth
    info.HM2 (INTEGER, flag) HapMap2 membership
    info.HM3 (INTEGER, flag) HapMap3 membership
    info.AA                 Ancestral Allele, ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/pilot_data/technical/reference/ancestral_alignments/README
    info.AC (INTEGER)       Allele count in genotypes
    info.AN (INTEGER)       Total number of alleles in called genotypes
    format (9)              genotype format
    NA06985 (10)            genotype for sample NA06985
    NA06985.GT              Genotype for sample NA06985
    NA06985.DP (INTEGER)    Read Depth for sample NA06985
    NA06985.CB              Called by S(Sanger), M(UMich), B(BI) for sample NA06985
    NA06986 (11)            genotype for sample NA06986
    NA06986.GT              Genotype for sample NA06986

We can use the `track` function to display the info column in the original vcf file, 



    % vtools output variant chr pos "track('CEU_hg38.vcf.gz')" -l 5
    
    1   10533   AA=.;AC=6;AN=120;DP=423
    1   51479   AA=.;AC=29;AN=120;DP=188
    1   51928   AA=.;AC=5;AN=120;DP=192
    1   54586   AA=C;AC=2;AN=120;DP=166
    1   54676   AA=T;AC=2;AN=120;DP=131
    

The default parameter `col=8` is used to extract the info column of the info file. You can display other tracks such as name 



    % vtools output variant chr pos "track('CEU_hg38.vcf.gz', 'name')" -l 5   

    1   10533   .
    1   51479   .
    1   51928   .
    1   54586   .
    1   54676   rs2462492
    

Values of individual info fields could be specified by `info.FIELD` where `FIELD` is the name of info field. 



    % vtools output variant chr pos "track('CEU_hg38.vcf.gz', 'info.DP')" -l 5
    
    1   10533   423
    1   51479   188
    1   51928   192
    1   54586   166
    1   54676   131
    

If you know the name of the sample (in the vcf file, this example happens to has samples from this file), 

    % vtools show samples -l 5
    
    sample_name filename
    NA06985     CEU_hg38.vcf.gz
    NA06986     CEU_hg38.vcf.gz
    NA06994     CEU_hg38.vcf.gz
    NA07000     CEU_hg38.vcf.gz
    NA07037     CEU_hg38.vcf.gz
    (55 records omitted)

    

you can get the genotype columns using sample name 



    % vtools output variant chr pos "track('CEU_hg38.vcf.gz', 'NA06986')" -l 5  

    1   10533   0|0:14:SMB
    1   51479   0|1:16:SMB
    1   51928   0|0:7:SM
    1   54586   0|0:6:SM
    1   54676   0|0:12:SM
    

With the format information abtained from 



    % vtools output variant chr pos "track('CEU.vcf.gz', 'format')" -l 5
    
    1   10533   GT:DP:CB
    1   51479   GT:DP:CB
    1   51928   GT:DP:CB
    1   54586   GT:DP:CB
    1   54676   GT:DP:CB
    

we can list fields of the genotype columns, 

    % vtools output variant chr pos "track('CEU.vcf.gz', 'NA06986.GT')" -l 5
    
    1   10533   0|0
    1   51479   0|1
    1   51928   0|0
    1   54586   0|0
    1   54676   0|0
    

</details>

A very useful feature of the vcf track is that **you can use vcf files from online** by specifying a URL instead of a local filename. 

<details><summary> Examples: Annotate variants using online vcf files</summary> We would like to annotate our variants using VCF files from the hg19 version of 1000 genomes project. To make use of data from the 1000 genomes project, we need to first lift over our project: 



    % vtools liftover hg19
    
    INFO: Exporting variants in BED format
    Exporting variants: 100% [==========================] 288 67.3K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating table variant: 100% [======================] 288 21.8K/s in 00:00:00
    

To pass the correct coordinates, option `--build hg19` is needed: 



    % vtools output variant chr pos "track('http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20110521/ALL.chr1.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz', 'info')" \
    %     -l 5 --build hg19  

    1	10533	.
    1	51479	RSQ=0.7414;AVGPOST=0.9085;AA=T;AN=2184;THETA=0.0131;AC=235;VT=SNP;LDAF=0.1404;SNPSOURCE=LOWCOV;ERATE=0.0012;AF=0.11;ASN_AF=0.0035;AMR_AF=0.16;AFR_AF=0.03;EUR_AF=0.22
    1	51928	.
    1	54586	.
    1	54676	LDAF=0.1528;RSQ=0.6989;AA=T;AN=2184;AC=267;VT=SNP;AVGPOST=0.8998;SNPSOURCE=LOWCOV;THETA=0.0110;ERATE=0.0037;AF=0.12;ASN_AF=0.02;AMR_AF=0.20;AFR_AF=0.09;EUR_AF=0.18
    

</details>


{{% notice tip %}}
Available variant and genotype info fields are determined from the header of input vcf file. Columns such as `info.AA` is unacceptable if `AA` is not defined in the header. 
{{% /notice %}}
 

#### 2.3 bigWig tracks 

The bigWig tracks contains numeric values for locations (ranges). The default `col` value for this format is `4` (the value column), but you can specify `1` (chrom), `2` (start, 0-based), `3` (end, 1-based), `4` (value), and `"chrom"`, `"chromStart"`, `"chromEnd"`, and `"value"`. 

<details><summary> Examples: Use bigWig tracks to annotate and select variants</summary> Let us create a project in hg19, import some data, and download a bigWig track from the UCSC ENCODE website: 



    % wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeOpenChromFaire/wgEncodeOpenChromFaireFrontalcortexocSig.bigWig
    % vtools init track -f
    % vtools import indels.vcf  --build hg19

    INFO: Importing variants from indels.vcf (1/1)
    indels.vcf: 100% [============================================] 184 12.3K/s in 00:00:00
    INFO: 137 new variants (1 SNVs, 77 insertions, 58 deletions, 7 complex variants) from 184 lines are imported.
    Importing genotypes: 0 0.0/s in 00:00:00
    Copying samples: 0 0.0/s in 00:00:00
    

The detailed information about this track can be obtained by 



    % vtools show track wgEncodeOpenChromFaireFrontalcortexocSig.bigWig
    
    Version:                4
    Primary data size       1320909131
    Zoom levels:            10
    Chrom count:            23
    Chrom size:
        chr1                249250621
        chr10               135534747
        chr11               135006516
        chr12               133851895
        chr13               115169878
        chr14               107349540
        chr15               102531392
        chr16               90354753
        chr17               81195210
        chr18               78077248
        chr19               59128983
        chr2                243199373
        chr20               63025520
        chr21               48129895
        chr22               51304566
        chr3                198022430
        chr4                191154276
        chr5                180915260
        chr6                171115067
        chr7                159138663
        chr8                146364022
        chr9                141213431
        chrX                155270560
    Bases covered:          2951253637
    Mean:                   0.004807
    Min:                    0.000000
    Max:                    0.592400
    std:                    0.004469
    Number of fields:       4
    
    Available columns (with type VARCHAR if unspecified or all=1):
    0 (INTEGER)             1 if matched
    chrom (1)               chromosome
    chromStart (2, INTEGER) start position (0-based)
    chromEnd (3, INTEGER)   end position (1-based)
    value (4, FLOAT)        value

and we can show the track values for each variant using command 



    % vtools output variant chr pos ref alt "track('wgEncodeOpenChromFaireFrontalcortexocSig.bigWig')" -l 5
    
    1	10434	-	C	0.00089999998454
    1	10440	C	-	0.00089999998454
    1	54789	C	-	0.00719999987632
    1	54790	-	T	0.00719999987632
    1	63738	ACT	-	0.00710000004619
    

In addition to output, the track can also be used to select variants, 



    % vtools select variant "track('wgEncodeOpenChromFaireFrontalcortexocSig.bigWig') > 0.001" \
         --output chr pos ref alt "track('wgEncodeOpenChromFaireFrontalcortexocSig.bigWig')" -l 5
    
    1	54789	C	-	0.00719999987632
    1	54790	-	T	0.00719999987632
    1	63738	ACT	-	0.00710000004619
    1	63738	ACT	CTA	0.00710000004619
    1	81963	-	AA	0.0120000001043
    

</details>

 

#### 2.4 bigBed tracks 

BigBed is a compressed indexed BED format that contains three mandatory columns and nine optional columns. The default `col` value for this format is `` (return 1 for matched records), but you can be specify items such as `1` (chrom) and `chromStart` (start, 0-based) according to output of command `vtools show track BIGBEDFILE`. 

<details><summary> Examples: Use bigBed tracks to annotate variants</summary> Let us create a project in hg19, import some data, and download a bigWig track from the UCSC ENCODE website: 

    % wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeDukeAffyExon/wgEncodeDukeAffyExonUrothelUt189SimpleSignalRep2.bigBed
    % vtools init track
    % vtools import indels.vcf  --build hg19
    
    INFO: Importing variants from indels.vcf (1/1)
    indels.vcf: 100% [============================================] 184 12.3K/s in 00:00:00
    INFO: 137 new variants (1 SNVs, 77 insertions, 58 deletions, 7 complex variants) from 184 lines are imported.
    Importing genotypes: 0 0.0/s in 00:00:00
    Copying samples: 0 0.0/s in 00:00:00
    

This tracks provides the following information: 



    % vtools show track wgEncodeDukeAffyExonUrothelUt189SimpleSignalRep2.bigBed

    Version:                4
    Item count:             38378
    Primary data size:      798350
    Zoom levels:            7
    Chrom count:            24
    Chrom size:
        chr1                249250621
        chr10               135534747
        chr11               135006516
        chr12               133851895
        chr13               115169878
        chr14               107349540
        chr15               102531392
        chr16               90354753
        chr17               81195210
        chr18               78077248
        chr19               59128983
        chr2                243199373
        chr20               63025520
        chr21               48129895
        chr22               51304566
        chr3                198022430
        chr4                191154276
        chr5                180915260
        chr6                171115067
        chr7                159138663
        chr8                146364022
        chr9                141213431
        chrX                155270560
        chrY                59373566
    Bases covered           1143378960
    Mean depth:             1.055693
    Min depth:              1.000000
    Max depth:              18.000000
    Std of depth:           0.310857
    Number of fields:       9
    
    Available columns (with type VARCHAR if unspecified or all=1):
    chrom (1)               Chromosome (or contig, scaffold, etc.)
    chromStart (2, INTEGER) Start position in chromosome
    chromEnd (3, INTEGER)   End position in chromosome
    name (4)                Name of item
    score (5, INTEGER)      Score from 0-1000. Capped number of reads
    strand (6)              + or -
    signalValue (7, FLOAT)  Measurement of expression value of the gene
    exonCount (8, INTEGER)  Number of exons used to estimate expression value
    constituitiveExons (9, INTEGER) Number of constituitive exons used to estimate the
                            expression value

The track provides provides numeric annotation for each variant, 



    % vtools output variant chr pos ref alt "track('wgEncodeDukeAffyExonUrothelUt189SimpleSignalRep2.bigBed')" -l5s  

    1	10434	-	C	.
    1	10440	C	-	.
    1	54789	C	-	.
    1	54790	-	T	.
    1	63738	ACT	-	.
    

The first five variant does not overlap with any regions in the bigBed file, but we can select variants using track membership: 



    % vtools select variant "track('wgEncodeDukeAffyExonUrothelUt189SimpleSignalRep2.bigBed') = 1" -t encode
    
    Running: 0 0.0/s in 00:00:00
    INFO: 28 variants selected.
    

and lists fields from the bigBed file for these variants 



    % vtools output encode chr pos ref alt "track('wgEncodeDukeAffyExonUrothelUt189SimpleSignalRep2.bigBed', 4)" -l5  

    1	761958	-	    T    	LINC00115
    1	768117	GTTTT	-    	RP11-206L10.11
    1	768117	-    	GTTTT	RP11-206L10.11
    1	768118	-    	TT   	RP11-206L10.11
    1	768625	-    	A    	RP11-206L10.11
    

and 



    % vtools output encode chr pos ref alt "track('wgEncodeDukeAffyExonUrothelUt189SimpleSignalRep2.bigBed', 'score')" -l5

    1	761958	-    	T    	692
    1	768117	GTTTT	-    	659
    1	768117	-    	GTTTT	659
    1	768118	-    	TT  	659
    1	768625	-    	A    	659
    

</details>

 

#### 2.5 Indexed BAM tracks 

Tracks in BAM format provides information regarding aligments, namely the reads that cover the starting position of each variant. If the variant is called from the provided BAM file, the BAM track provides information regarding the reads from which variants are called. 


{{% notice tip%}}
*variant tools* currently only use the starting location of variants so it ignores reads that overlap but do not cover the starting position of a variant (e.g. an insertion). 
{{% /notice %}}

A BAM track accepts the following fields, 

1.  `coverage`: number of reads that cover the starting position of each variant. This is the default field. 
2.  `calls`: nucleotide of the reads at the variant location. This allows you to show the number of reference and alternative alleles for SNV variants, but not so informative for indels. 
3.  `reads`: display a small piece of nucleotide sequence around the variant location (default to 5, namely the variant location and 4 base after it), separated by `|`. `_` will be displayed if the position goes beyond the end of a read. A parameter can be specified in the form of `reads?start=-5&width=10` to change the starting point and width of displayed sequence. 
4.  `qual`: A list of phred base quality of reads at the location. 
5.  `avg_qual`: Average qual scores of all reads. 
6.  `mapq`: A list of phred-scaled quality of alignment at the location. 
7.  `avg_mapq`: Average map qual scores of all reads. 
8.  Any tag values listed at the end of command `vtools show track`. 

Parameters can be used to limit the reads to count or display, and change the way reads are displayed. The `bam` track currently supports the following options: 

1.  `type`: If set to `` (matched to reference sequence), `1` (unmatched single nucleotide), `2` (insertion) and `3` (deletion), only reads that are matched, unmatched (single nucleotide), insertion or deletion at the variant location is counted or outputted. Note that nucleotide before the insertion will be matched to reference genome, but they are not counted as matched. 
2.  `min_mapq`: limits the reads to those with `mapq` scores that exceed the specified value. 
3.  `min_qual`: limits the reads to those with `qual` scores that execeed the specified value. 
4.  `color=[1|0]`: display variant location in blue, and insertions in green for `reads` field. 
5.  `limit`: limit the number of reads or calls to display if the depth of coverage is high. 
6.  `delimiter`: character (e.g. `\t` to separate reads in the `reads` output (`|` is used by default). 
7.  `show_seq=[1|0]`: A `.` is used by default when the nucleotide matches the reference genome at the location. The actual nucleotide sequence will be displayed if this option is set to `1`. 


{{% notice tip%}}
You can count the number of reads that match (or unmatch) the reference genome using parameter `coverage`type=0@@. 
{{% /notice %}}

<details><summary> Examples: Use BAM files to check the details of variant calls. </summary> Now suppose that we have a project with a list of variants (due to the size of BAM files, original data is not provided), we select the variants based on the sample from which they are called: 



    % vtools select variant --samples "sample_name = 'WGS4_9'" -t ex49
    
    INFO: 1 samples are selected by condition: sample_name = 'WGS4_9'
    Running: 3,959 164.5/s in 00:00:24
    INFO: 1191 variants selected.
    

We first need to check the available information that can be retrived 



    $ vtools show track LP6005253-DNA_A02.bam  

    Header:
    @HD	VN:1.0	SO:coordinate
    @PG	ID:CASAVA	VN:CASAVA-1.9.0a1_110909	CL:/illumina/ /development/casava/CASAVA-VariantCalling-2.12a_gVCF/bin/configureBuild.pl --targets all bam --inSampleDir=/illumina/build/services/Projects/MDAnderson_Thompson2/LP6005253-DNA_A02/Aligned/D1LTMACXX_Aligned_MDAnderson_Thompson2_LP6005253-DNA_A02_121222_SN1012_0268_BD1LTMACXX_CE_L5/Sample_LP6005253-DNA_A02 --inSampleDir=/illumina/build/services/Projects/MDAnderson_Thompson2/LP6005253-DNA_A02/Aligned/D1LTMACXX_Aligned_MDAnderson_Thompson2_LP6005253-DNA_A02_121222_SN1012_0268_BD1LTMACXX_CE_L6/Sample_LP6005253-DNA_A02 --inSampleDir=/illumina/build/services/Projects/MDAnderson_Thompson2/LP6005253-DNA_A02/Aligned/D1LTMACXX_Aligned_MDAnderson_Thompson2_LP6005253-DNA_A02_121222_SN1012_0268_BD1LTMACXX_CE_L7/Sample_LP6005253-DNA_A02 --outDir=/scratch/LP6005253-DNA_A02 --samtoolsRefFile=/illumina/scratch/services/Genomes/FASTA_UCSC/HumanNCBI37_UCSC/HumanNCBI37_UCSC_XX.fa --indelsSaveTempFiles --variantsConsensusVCF --jobsLimit=12 --variantsPrintUsedAlleleCounts --variantsWriteRealigned --sortKeepAllReads --bamChangeChromLabels=OFF --sgeQueue=prod-s.q
    @SQ	SN:chr1	LN:249250621
    @SQ	SN:chr2	LN:243199373
    @SQ	SN:chr3	LN:198022430
    @SQ	SN:chr4	LN:191154276
    @SQ	SN:chr5	LN:180915260
    @SQ	SN:chr6	LN:171115067
    @SQ	SN:chr7	LN:159138663
    @SQ	SN:chrX	LN:155270560
    @SQ	SN:chr8	LN:146364022
    @SQ	SN:chr9	LN:141213431
    @SQ	SN:chr10	LN:135534747
    @SQ	SN:chr11	LN:135006516
    @SQ	SN:chr12	LN:133851895
    @SQ	SN:chr13	LN:115169878
    @SQ	SN:chr14	LN:107349540
    @SQ	SN:chr15	LN:102531392
    @SQ	SN:chr16	LN:90354753
    @SQ	SN:chr17	LN:81195210
    @SQ	SN:chr18	LN:78077248
    @SQ	SN:chr20	LN:63025520
    @SQ	SN:chr19	LN:59128983
    @SQ	SN:chr22	LN:51304566
    @SQ	SN:chr21	LN:48129895
    @SQ	SN:chrM	LN:16571
    
    Chrom size:             24
        chr1                249250621
        chr2                243199373
        chr3                198022430
        chr4                191154276
        chr5                180915260
        chr6                171115067
        chr7                159138663
        chrX                155270560
        chr8                146364022
        chr9                141213431
        chr10               135534747
        chr11               135006516
        chr12               133851895
        chr13               115169878
        chr14               107349540
        chr15               102531392
        chr16               90354753
        chr17               81195210
        chr18               78077248
        chr20               63025520
        chr19               59128983
        chr22               51304566
        chr21               48129895
        chrM                16571
    
    Available fields (with type VARCHAR if unspecified or all=1):
    0 (INTEGER)             1 if depth is over 0, NULL otherwise
    coverage (INTEGER)      Number of reads that cover the starting position of the variant
    calls                   nucleotide of the reads at the variant location
    reads                   nucleotide sequence around the variant location
    qual                    A list of phred base quality of reads at the location
    avg_qual (FLOAT)        Average qual score of all reads
    mapq                    A list of phred base quality of alignment at the location
    avg_mapq (FLOAT)        Average mapq score of all reads
    
    Tags and flag that can be outputed or used in filters, with values from the 1st record:
    AM                      C (int)    : 0
    BC                      Z (string) : 0
    XD                      Z (string) : 49A12AC19C11C4
    SM                      i (int32)  : 0
    AS                      i (int32)  : 511
    flag                    int flag   : 0x63 (paired, unmapped according to bits 1 & 3)
    
    Parameters start (default to 0), width (default to 5) and color (default to 0) can be used with reads to adjust the window around variant, and use colors for insertions and variant allele, with syntax reads?start=-5&width=10&color=1. min_qual, min_mapq and TAG=VAL (or >, >=, <, <=, !=) can be used for all fields to limit the reads to the ones with mapq and qual scores that exceed the specified value, and tag satisfying specified conditions. Parameter limit limits the number of reads or calls to display if the depth of coverage is high.
    

The depth of coverage of these variants could be obtained using the BAM track, 



    % vtools output ex49 chr pos ref alt "track('LP6005253-DNA_A02.bam')" -l5
    
    1	1138963	C	T	26
    1	1470808	G	A	37
    1	6161109	C	T	27
    1	6314785	T	C	32
    1	9990112	A	G	43
    

The quality of reads and alignment can be displayed using fields `qual` and `mapq`, 



    % vtools output ex49 chr pos ref alt "track('LP6005253-DNA_A02.bam', 'qual')" -l5
    
    1	1138963	C	T	34,34,32,30,33,39,40,41,31,34,23,25,37,33,34,40,40,2,11,31,33,24,2,40,39,35
    1	1470808	G	A	31,2,37,35,35,33,33,35,33,29,41,35,35,33,33,2,35,5,35,35,36,40,31,40,31,26,23,38,33,39,31,41,40,30,35,34,34
    1	6161109	C	T	10,31,32,39,31,39,41,41,35,2,22,40,38,28,39,40,39,35,41,20,40,35,39,38,35,30,34
    1	6314785	T	C	2,34,37,2,33,2,31,27,37,10,24,39,33,36,31,35,35,36,33,33,38,41,41,29,38,38,39,23,35,35,31,35
    1	9990112	A	G	34,34,37,37,35,36,36,33,36,36,41,31,37,39,36,40,38,36,41,38,37,41,35,25,38,40,40,40,36,41,41,39,37,34,30,36,36,41,41,36,39,37,37
    



    % vtools output ex49 chr pos ref alt "track('LP6005253-DNA_A02.bam', 'mapq')" -l5   

    1	1138963	C	T	254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,241,254,254,254,254,254,254,254,254
    1	1470808	G	A	254,194,254,254,254,254,254,254,254,254,254,254,254,254,254,149,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254
    1	6161109	C	T	254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254
    1	6314785	T	C	254,254,254,254,254,254,254,254,254,231,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254
    1	9990112	A	G	254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254,254
    

We can exclude some reads depending on quality scores, using parameters `min_qual` or `min_mapq`, 



    % vtools output ex49 chr pos ref alt "track('LP6005253-DNA_A02.bam', 'coverage?min_qual=30')" -l5
    
    1	1138963	C	T	20
    1	1470808	G	A	31
    1	6161109	C	T	22
    1	6314785	T	C	24
    1	9990112	A	G	42
    

Read TAGs can also be outputed or used in filter conditions. For example, this bam file has tags `AM`, `BC`, `XD`, `SM` and `AS`, you can list the `AS` values of all reads using command 



    % vtools output ex49 chr pos ref alt 'ref_sequence(chr, pos-3, pos+3)' "track('LP6005253-DNA_A02.bam', 'AS?min_qual=35')" -l5
    
    1	1138963	C	T	AGCCTCC	1007|1001|1001|966|941|1006|816|946|1002
    1	1470808	G	A	GGCGGCC	1007|475|783|951|998|878|967|968|1004|967|967|962|962|935|1004|1008|963|998
    1	6161109	C	T	TACCGTG	897|922|927|830|967|965|936|997|997|832|774|961|966|922|937|949|964
    1	6314785	T	C	CGATGGG	939|517|0|925|968|965|962|912|968|967|855|0|924|962|923|919
    1	9990112	A	G	ATCATTA	964|966|968|1007|965|1003|1008|1008|991|963|989|963|906|872|1008|1007|965|962|968|1002|963|1007|963|966|1006|937|912|1008|966|1008|962|1008|1008|1005|1008|1008
    

or its values to filter reads: 



    % vtools output ex49 chr pos ref alt 'ref_sequence(chr, pos-3, pos+3)' "track('LP6005253-DNA_A02.bam', 'coverage?AS>1000')" -l5
    
    1	1138963	C	T	AGCCTCC	5
    1	1470808	G	A	GGCGGCC	7
    1	6161109	C	T	TACCGTG	0
    1	6314785	T	C	CGATGGG	1
    1	9990112	A	G	ATCATTA	18
    

</details>

<details><summary> Count and display calls and reads for reads of different types</summary> 

The `track` function can also be used to display calls (nucleotide at the variant site) and reads (nucleotide sequences around the variant site). To demonstrate the features more clearly, we will use a project with more types of variants. 

First, we can display the nucleotide at the variant site using the `calls` parameter, 



    % bam=/path/to/a/bam/file
    % vtools output exon1 chr pos ref alt "track('${bam}', 'calls?limit=20')"  

    1 	118420020	-           	T	IIIII.I.I.I..III.I.I
    1 	159023386	G           	A	.AAAAA..A.AA..A..A.A
    1 	160398161	G           	A	A.A.AA....A..AAA..A.
    1 	180772617	C           	T	.T..TTT..TT.T.TTTT.T
    3 	12581722 	T           	C	C.C.......C.C....CC.
    4 	1945715  	A           	T	.N..T..TTTTT.T..T.TT
    5 	137089865	C           	G	.G..G.G..GGGG...G...
    8 	42878531 	TCCT        	-	....................
    12	65449852 	C           	A	AA.A.A..AA.AAA..AAAA
    16	11929051 	T           	C	CC..CCC.........C...
    16	17197814 	G           	A	AA..A.AAAAA..AA.AAAA
    17	78938525 	G           	A	A......AAA....AAAAAA
    17	79525590 	C           	G	.GG.GGG..GG...G.G...
    17	79687655 	C           	T	....T.TTT.TTT..TTN.T
    19	34843754 	CCCCACCCCAGC	-	..........**.*......
    

The output shows 

1.  Nucleotides that match the reference sequence are displayed as `.`. 
2.  Deletions are displayed as `*`. 
3.  Insertions are displayed as `I`. 

You can display the reads around the variant site, using the `reads` parameter: 



    % vtools output exon1 chr pos ref alt "track('${bam}', 'reads?limit=5')"
    
    1 	118420020	-           	T	T.....|T.....|T.....|T.....|T.....
    1 	159023386	G           	A	..   |A... |A....|A....|A....
    1 	160398161	G           	A	A    |..   |A..  |...  |A....
    1 	180772617	C           	T	.    |T..  |.... |.....|T....
    3 	12581722 	T           	C	C    |..   |C..  |.... |.....
    4 	1945715  	A           	T	.... |N....|.....|.....|T....
    5 	137089865	C           	G	.....|G....|.....|.....|G....
    8 	42878531 	TCCT        	-	.    |.... |.... |.....|.....
    12	65449852 	C           	A	A    |A..  |.... |A....|.....
    16	11929051 	T           	C	C.   |C....|.....|.....|C....
    16	17197814 	G           	A	A.   |A..  |.... |.....|A....
    17	78938525 	G           	A	A..  |.... |.... |.....|.....
    17	79525590 	C           	G	..   |G... |G... |.....|G....
    17	79687655 	C           	T	.    |.....|.....|.....|T....
    19	34843754 	CCCCACCCCAGC	-	..   |..   |...  |.....|.....
    

Parameter `limit-5` is used to avoid lengthy output. 

Parameters `start` and `width` can be used to specify the window of sequences to display: 



    % vtools output exon1 chr pos ref alt "track('${bam}', 'reads?limit=5&start=-5&width=8&color=1&show_seq=1')"
    
    1 	118420020	-           	T	GTTACTTTT|GTTACTTTT|GTTACTTTT|GTTACTTTT|GTTACTTTT
    1 	159023386	G           	A	AAGTGGT |AAGTGATG|AAGTGATG|AAGTGATG|AAGTGATG
    1 	160398161	G           	A	CTTCCA  |CTTCCGT |CTTCCATG|CTTCCGTG|CTTCCATG
    1 	180772617	C           	T	TACTAC  |TACTATGC|TACTACGC|TACTACGC|TACTATGC
    3 	12581722 	T           	C	GGTTGC  |GGTTGTG |GGTTGCGC|GGTTGTGC|GGTTGTGC
    4 	1945715  	A           	T	AAATGACC|AAANNNCC|AAATGACC|AAATGACC|AAATGTCC
    5 	137089865	C           	G	TGGAGCCA|TGGAGGCA|TGGAGCCA|TGGAGCCA|TGGAGGCA
    8 	42878531 	TCCT        	-	CTTCCT  |CTTCCTCC|CTTCCTCC|CTTCCTCC|CTTCCTCC
    12	65449852 	C           	A	ACTTAA  |ACTTAAAT|ACTTACAT|ACTTAAAT|ACTTACAT
    16	11929051 	T           	C	TTTTTCT |TTTTTCTC|TTTTTTTC|TTTTTTTC|TTTTTCTC
    16	17197814 	G           	A	GAGAGAA |GAGAGAAA|GAGAGGAA|GAGAGGAA|GAGAGAAA
    17	78938525 	G           	A	CAGGCACT|CAGGCGCT|CAGGCGCT|CAGGCGCT|CAGGCGCT
    17	79525590 	C           	G	CTCCCCT |CTCCCGTT|CTCCCGTT|CTCCCCTT|CTCCCGTT
    17	79687655 	C           	T	CAGACC  |CAGACCAC|CAGACCAC|CAGACCAC|CAGACTAC
    19	34843754 	CCCCACCCCAGC	-	GCAGACC |GCAGACC |GCAGACCC|GCAGACCC|GCAGACCC
    

Parameter `color=1` will make the insertion displayed in green, and nucleotide at variant site displayed in blue on terminal. Parameter `show_seq` displays real sequence instead of `.` for matched nucleotides. 


You can also specify the types of reads so that you can count or display just a subsets of reads. For example, you can display all reads on the forward strand 



    % vtools output exon1 chr pos ref alt "track('${bam}', 'reads?limit=5&start=-5&width=8&color=1&show_seq=1&strand=+')"
    
    1 	118420020	-           	T	GTTACTTTT|GTTACTTTT|GTTACTTTT|GTTACTTTT|GTTACTTTT
    1 	159023386	G           	A	AAGTGATG|AAGTGATG|AAGTGATG|AAGTGATG|AAGTGGTG
    1 	160398161	G           	A	CTTCCATG|CTTCCATG|CTTCCATG|CTTCCATG|CTTCCATG
    1 	180772617	C           	T	TACTACGC|TACTACGC|TACTATGC|TACTATGC|TACTACGC
    3 	12581722 	T           	C	GGTTGTG |GGTTGCGC|GGTTGTGC|GGTTGTGC|GGTTGTGC
    4 	1945715  	A           	T	AAANNNCC|AAATGACC|AAATGACC|AAATGTCC|AAATGACC
    5 	137089865	C           	G	TGGAGCCA|TGGAGGCA|TGGAGCCA|TGGAGCCA|TGGAGGCA
    8 	42878531 	TCCT        	-	CTTCCTCC|CTTCCTCC|CTTCCTCC|CTTCCTCC|CTTCCTCC
    12	65449852 	C           	A	ACTTACAT|ACTTAAAT|ACTTAAAT|ACTTAAAT|ACTTAAAT
    16	11929051 	T           	C	TTTTTCTC|TTTTTTTC|TTTTTTTC|TTTTTTTC|TTTTTTTC
    16	17197814 	G           	A	GAGAGAA |GAGAGAAA|GAGAGGAA|GAGAGAAA|GAGAGAAA
    17	78938525 	G           	A	CAGGCACT|CAGGCGCT|CAGGCGCT|CAGGCGCT|CAGGCGCT
    17	79525590 	C           	G	CTCCCGTT|CTCCCGTT|CTCCCGTT|CTCCCCTT|CTCCCCTT
    17	79687655 	C           	T	CAGACCAC|CAGACCAC|CAGACCAC|CAGACCAC|CAGACTAC
    19	34843754 	CCCCACCCCAGC	-	GCAGACCC|GCAGACCC|GCAGACCC|GCAGACCC|GCAGACCC
    

Or display just the mismatch single-nucleotides 

    % vtools output exon1 chr pos ref alt "track('${bam}', 'reads?limit=5&start=-5&width=8&type=1')"
    
    1 	118420020	-           	T
    1 	159023386	G           	A	.....A..|.....A..|.....A..|.....A..|.....A..
    1 	160398161	G           	A	.....A  |.....A..|.....A..|.....A..|.....A..
    1 	180772617	C           	T	.....T..|.....T..|.....T..|.....T..|.....T..
    3 	12581722 	T           	C	.....C  |.....C..|.....C..|.....C..|.....C..
    4 	1945715  	A           	T	...NNN..|.....T..|.....T..|.....T..|.....T..
    5 	137089865	C           	G	.....G..|.....G..|.....G..|.....G..|.....G..
    8 	42878531 	TCCT        	-
    12	65449852 	C           	A	.....A  |.....A..|.....A..|G....A..|.....A..
    16	11929051 	T           	C	.....C. |.....C..|.....C..|.....C..|.....C..
    16	17197814 	G           	A	.....A. |.....A..|.....A..|.....A..|.....A..
    17	78938525 	G           	A	.....A..|.....A..|.....A..|.....A..|.....A..
    17	79525590 	C           	G	.....G..|.....G..|.....G..|.....G..|.....G..
    17	79687655 	C           	T	.....T..|.....T..|.....T..|.....T..|.....T..
    19	34843754 	CCCCACCCCAGC	-
    

For example, we can output the number of reads that match (type 0), mismatch (type 1), insert before (type 2), or delete (type 3) the nucleotide sequence at the variant site: 



    vtools output exon1 chr pos ref alt "track('${bam}')" \
    	"track('${bam}', 'coverage?type=0')" \
    	"track('${bam}', 'coverage?type=1')" \
    	"track('${bam}', 'coverage?type=2')" \
    	"track('${bam}', 'coverage?type=3')" \
    	"track('${bam}', 'coverage?type=3&strand=+')" \
    	"track('${bam}', 'coverage?type=3&strand=-')"
    
    1 	118420020	-           	T	25 	9 	0 	16	0 	0 	0
    1 	159023386	G           	A	43 	18	25	0 	0 	0 	0
    1 	160398161	G           	A	50 	23	27	0 	0 	0 	0
    1 	180772617	C           	T	40 	17	23	0 	0 	0 	0
    3 	12581722 	T           	C	107	63	44	0 	0 	0 	0
    4 	1945715  	A           	T	64 	29	35	0 	0 	0 	0
    5 	137089865	C           	G	81 	41	40	0 	0 	0 	0
    8 	42878531 	TCCT        	-	50 	27	0 	14	9 	3 	6
    12	65449852 	C           	A	65 	30	35	0 	0 	0 	0
    16	11929051 	T           	C	69 	37	32	0 	0 	0 	0
    16	17197814 	G           	A	57 	19	38	0 	0 	0 	0
    17	78938525 	G           	A	88 	47	41	0 	0 	0 	0
    17	79525590 	C           	G	58 	31	27	0 	0 	0 	0
    17	79687655 	C           	T	95 	54	41	0 	0 	0 	0
    19	34843754 	CCCCACCCCAGC	-	64 	30	0 	0 	34	16	18
    

The last two functions are interesting as it shows the number of reads on forward and reverse strands that shows the deletion. This information can be usful because the variant might not be real if it exists mostly on one of the strands. 

</details>


{{% notice tip%}}
An option `color=1` can be used with the `read` field to display insertions and variant allele in color (green and blue respectively). This is very helpful if you have long reads and reads that contain indels. 
{{% /notice %}}

Online BAM tracks can also be used so you do not have to download large BAM files in order to use them. 

<details><summary> Examples: obtain depth of coverage of variants using online BAM files</summary> 

    % vtools output variant chr pos "track('ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data/HG00096/alignment/HG00096.mapped.ILLUMINA.bwa.GBR.low_coverage.20120522.bam')" -l5
    
    [bam_index_load] attempting to download the remote index file.
    1	533	0
    1	41342	1
    1	41791	4
    1	44449	7
    1	44539	12
    

</details>

 [1]: http://genome.ucsc.edu/goldenPath/help/bigWig.html
 [2]: http://genome.ucsc.edu/goldenPath/help/bigBed.html
 [3]:    /documentation/vtools_commands/show/