+++
title = "export"
description = ""
weight = 13
+++



## Export variants and samples to external files


### 1. Usage

    % vtools export -h

    usage: vtools export [-h] [-o [OUTPUT]] [-s [COND [COND ...]]]
                         [--format FORMAT] [--build BUILD]
                         [--header [HEADER [HEADER ...]]] [-j JOBS] [-v {0,1,2}]
                         table

    Export variants and genotypes in text, vcf and other formats.

    positional arguments:
      table                 A variant table whose variants will be exported. If
                            parameter --samples is specified, only variants belong
                            to one or more of the samples will be exported.

    optional arguments:
      -h, --help            show this help message and exit
      -o [OUTPUT], --output [OUTPUT]
                            Name of output file. Output will be written to the
                            standard output if this parameter is left unspecified.
      -s [COND [COND ...]], --samples [COND [COND ...]]
                            Samples that will be exported, specified by conditions
                            such as 'aff=1' and 'filename like "MG%"'. Multiple
                            samples could be exported to a file if the output
                            format allows. No sample will be outputted if this
                            parameter is ignored.
      --format FORMAT       Format of the exported file. It can be one of the
                            variant tools supported file types such as VCF (cf.
                            'vtools show formats') or a local format specification
                            file (with extension .fmt). Some formats accept
                            additional parameters (cf. 'vtools show format FMT')
                            and allows you to export additional or alternative
                            fields.
      --build BUILD         Build version of the reference genome (e.g. hg18) of
                            the exported data. It can only be one of the primary
                            (default) of alternative (if exists) reference genome
                            of the project.
      --header [HEADER [HEADER ...]]
                            A complete header or a list of names that will be
                            joined by a delimiter specified by the file format to
                            form a header. If a special name - is specified, the
                            header will be read from the standard input, which is
                            the preferred way to specify large multi-line headers
                            (e.g. cat myheader | vtools export --header -).
                            Strings in the form of %(VAR)s will be interpolated to
                            values of variable VAR, which can be "sample_names"
                            for list of sample names, "datetime" for current date
                            and time, and "command" for the command used to create
                            output.
      -j JOBS, --jobs JOBS  Number of processes to export data. Multiple threads
                            will be automatically used if there are a large number
                            of samples.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).




### 2. Details

`vtools export` and `vtools output` perform similar functions but with different emphasis. `vtools output` output variants and variant info fields (and their summary statistics) in a tabular format, but it does not output genotype or genotype info fields. In comparison, `vtools export` exports variant, variant info fields, genotype and genotype info in pre-specified formats.



#### 2.1 Supported file formats

Command `vtools show formats` lists all formats that are supported by *variant tools* but some file formats can only be used to import or update variants. To check whether or not you can export data in a particular format, you can run command `vtools show format FMT` and check if it defines one or more `Columns`.

<details><summary> Check details of file formats</summary>

    % vtools show format ANNOVAR

    Format:      ANNOVAR
    Description: Input format of ANNOVAR. No genotype is defined.

    Columns:
      1            chromosome
      2            position (1-based)
      3            end position
      4            reference allele
      5            alternative allele
      6            optional column

    variant:
      chr          Chromosome
      pos          1-based position
      ref          Reference allele, '-' for insertion.
      alt          Alternative allele, '-' for deletion.

    Format parameters:
      comment_string Output one or more fields to the optional comment column of this
                   format. (default: )


Note the `Columns` section in the above configuration file. Columns in this section will be the output columns as a result of output. `vtools export` does not (yet) support as many formats as `vtools import` does, for example



    % vtools show format pileup_indel

    Format:      pileup_indel
    Description: Input format for samtools pileup indel caller. This format imports
      chr, pos, ref, alt and genotype.

    Columns:
      None defined, cannot export to this format

    variant:
      chr          Chromosome name
      pos          Start position of the indel event.
      ref          reference allele, '-' for insertion
      alt          alternative allele, '-' for deletion

    Genotype:
      GT           type of indel (homozygote or heterozygote)

    Other fields (usable through parameters):
      type         String summarizing the indel type, one of Dn (deletion of length n)
                   and In (insertion of length n)

    Format parameters:
      geno          (default: GT)


You see that the `Columns` section is not defined. </details>



#### 2.2 Export variants and variant info fields

The motivation of this export format is to prepare input files for annotating variants using `ANNOVAR`

<details><summary> Examples: Export in ANNOVAR format</summary>


    % vtools init import --parent vt_testData_v3
    % vtools import CEU_hg38.vcf --var_info AA AC AN DP --geno_info DP --build hg38
    % vtools export variant -o ANNOVAR.input --format ANNOVAR
    % head ANNOVAR.input

    1   10533   10533   G   C
    1   51479   51479   T   A
    1   51928   51928   G   A
    1   54586   54586   T   C
    1   54676   54676   C   T
    1   54708   54708   G   C
    1   55299   55299   C   T
    1   62203   62203   T   C
    1   63671   63671   G   A
    1   86028   86028   T   C


This optional comment field comes from the available fields in the variant table to be outputted. They should have been created using `vtools import` or `vtools update`



    % vtools export variant -o ANNOVAR.input --format ANNOVAR --comment_string DP
    % head ANNOVAR.input

    1   10533   10533   G   C   423
    1   51479   51479   T   A   188
    1   51928   51928   G   A   192
    1   54586   54586   T   C   166
    1   54676   54676   C   T   131
    1   54708   54708   G   C   135
    1   55299   55299   C   T   166
    1   62203   62203   T   C   159
    1   63671   63671   G   A   243
    1   86028   86028   T   C   182



</details>



#### 2.3 Output in PLINK TPED format

Please refer to the [TPED format][1] page.



#### 2.4 Export in vcf format

VCF is a flexible format that can store almost arbitrary information for variant, variant info, genotype and genotype info fields. All these information needs to be specified through command line options of the `vcf` format. To learn what options are available, you can use command



    % vtools show format vcf


Section `Other fields` lists the fields that can be imported (if they exist in the input file), and section `Format parameters` lists the parameters that can be specified from command line.



##### Export variants in VCF format

The basic command to export variants in vcf format is `vtools export TABLE --format vcf`. In this case, the variants are exported in vcf format, without header and with default (missing) name, `INFO`, and `FILTER` fields. `--format vcf` can be ignored if a `.vcf` file is specified in option `--output`.

<details><summary> Examples: export variants in vcf format</summary> Let us first get some data,



    % vtools init test -f
    % vtools import CEU_hg38.vcf --var_info AA AC AN DP --geno_info DP --build hg38



When we export variants in vcf format,

    % vtools export variant -o my.vcf

    INFO: Using 2 processes to handle 0 samples
    Selecting genotypes: 100% [===================================] 5 4.9/s in 00:00:01
    my.vcf: 100% [============================================] 292 15.6K/s in 00:00:00
    INFO: 290 lines are exported from variant table variant


The outputted file looks like

    % head my.vcf

    1   10533   .   G   C   .   PASS    .
    1   51479   .   T   A   .   PASS    .
    1   51928   .   G   A   .   PASS    .
    1   54586   .   T   C   .   PASS    .
    1   54676   .   C   T   .   PASS    .
    1   54708   .   G   C   .   PASS    .
    1   55299   .   C   T   .   PASS    .
    1   62203   .   T   C   .   PASS    .
    1   63671   .   G   A   .   PASS    .
    1   86028   .   T   C   .   PASS    .


</details>

Indel variants are outputted in VCF format. That is to say, instead of using `-` to represent missing alleles, indels such as `- => A` are outputted with padding alleles (e.g. `G => GA` if the reference allele before the variant is `G`). The positions of the variants are automatically adjusted.

<details><summary> Examples: export indel variants in vcf format</summary>

    % vtools init test -f
    % vtools admin --load_snapshot vt_testData
    % vtools import indels.vcf --build hg19

    INFO: Importing variants from indels.vcf (1/1)
    indels.vcf: 100% [==============================================] 184 21.5K/s in 00:00:00
    INFO: 137 new variants (1 SNVs, 77 insertions, 58 deletions, 7 complex variants) from 184 lines are imported.
    Importing genotypes: 0 0.0/s in 00:00:00
    Copying samples: 0 0.0/s in 00:00:00


When we export variants in vcf format,

    % vtools export variant -o my_indel.vcf

    Writing: 100% [=================================================] 137 22.5K/s in 00:00:00
    INFO: 129 lines are exported from variant table variant


The outputted file looks like



    % head my_indel.vcf

    1   10433   .   A   AC  .   PASS    .
    1   10439   .   AC  A   .   PASS    .
    1   54787   .   TC  T   .   PASS    .
    1   54789   .   C   CT  .   PASS    .
    1   63735   .   CCTA    C   .   PASS    .
    1   63738   .   ACT CTA .   PASS    .
    1   81962   .   T   TAA .   PASS    .
    1   82133   .   CA  C   .   PASS    .
    1   82133   .   C   CAAAAAAAAAAAAAA .   PASS    .
    1   83118   .   CA  C   .   PASS    .


The difference is clear if you compare the output with what outputted from command `vtools output`:

    % vtools output variant chr pos ref alt -l 10

    1   10434   -   C
    1   10440   C   -
    1   54788   C   -
    1   54790   -   T
    1   63736   CTA -
    1   63738   ACT CTA
    1   81963   -   AA
    1   82134   A   -
    1   82134   -   AAAAAAAAAAAAAA
    1   83119   A   -



</details>

You can export one or more variant info fields using parameter `--var_info`, depending on how the field is defined in `vcf.fmt`, the field will be outputted as a flag (show field name if its value if True), a name value pair (show `name=val`), or a value. Outputting values of a field is usually not recommended unless the values already conform to vcf standard.

{{% notice tip %}}
You can specify fields that are not defined in `vcf.fmt`. However, because *variant tools* does not know how to output it (as value or flag etc), it will output its value directly without a field name. Such fields do not conform to the vcf format standard. To output fields that are not defined in `vcf.fmt`, it is recommended that you add the field to a local copy of `vcf.fmt` and use the modified format file to export data.
{{% /notice %}}

<details><summary> Examples: export variant info fields</summary>


    % vtools init test -f
    % vtools import CEU_hg38.vcf --var_info AA AC AN DP --geno_info DP --build hg38
    % vtools export variant --var_info AA -o my.vcf
    % head my.vcf

    1   10533   .   G   C   .   PASS    AA=.
    1   51479   .   T   A   .   PASS    AA=.
    1   51928   .   G   A   .   PASS    AA=.
    1   54586   .   T   C   .   PASS    AA=C
    1   54676   .   C   T   .   PASS    AA=T
    1   54708   .   G   C   .   PASS    AA=g
    1   55299   .   C   T   .   PASS    AA=c
    1   62203   .   T   C   .   PASS    AA=C
    1   63671   .   G   A   .   PASS    AA=G
    1   86028   .   T   C   .   PASS    AA=.


Anyway, if you have imported the whole `INFO` column of the input file, you can export it as it is for each variant



    % vtools init test -f
    % vtools import CEU_hg38.vcf --var_info AA info --geno_info DP --build hg38
    % vtools output variant chr pos ref alt info -l 5

    1   10533   G   C   AA=.;AC=6;AN=120;DP=423
    1   51479   T   A   AA=.;AC=29;AN=120;DP=188
    1   51928   G   A   AA=.;AC=5;AN=120;DP=192
    1   54586   T   C   AA=C;AC=2;AN=120;DP=166
    1   54676   C   T   AA=T;AC=2;AN=120;DP=131




    % vtools export variant --var_info info -o my.vcf
    % head my.vcf

    1   10533   .   G   C   .   PASS    AA=.;AC=6;AN=120;DP=423
    1   51479   .   T   A   .   PASS    AA=.;AC=29;AN=120;DP=188
    1   51928   .   G   A   .   PASS    AA=.;AC=5;AN=120;DP=192
    1   54586   .   T   C   .   PASS    AA=C;AC=2;AN=120;DP=166
    1   54676   .   C   T   .   PASS    AA=T;AC=2;AN=120;DP=131
    1   54708   .   G   C   .   PASS    AA=g;AC=7;AN=120;DP=135
    1   55299   .   C   T   .   PASS    AA=c;AC=20;AN=120;DP=166;HM2
    1   62203   .   T   C   .   PASS    AA=C;AC=18;AN=120;DP=159
    1   63671   .   G   A   .   PASS    AA=G;AC=18;AN=120;DP=243
    1   86028   .   T   C   .   PASS    AA=.;AC=11;AN=120;DP=182


</details>


{{% notice warning %}}
If you compare the outputted vcf file with the original vcf file, you can notice a few differences. More specifically,

1. *variant tools* removes duplicate variants from input file when it imports data. If your data has multiple lines for a variant (e.g. the same variant with multiple rsnames), you will only be able to export one of them.
2. *variant tools* split variants from an input file if there are multiple alternative alleles. It exports variants one by one so such variants will not be combined into records that define multiple variants.
3.  Variant tools does not import phase information of genotypes and it always output variants in the format of `A/B`.

{{% /notice %}}


##### Specify a header

The `--header` option can be used to add a header to outputs. Although it is possible to specify a minimal header using option ` --header CHROM POS ID REF ALT QUAL FILTER INFO FORMAT`, it is useful to create a header file and send it to `vtools export` command through standard input (option `--header -`). The latter is preferred because vcf files usually has long headers.

<details><summary> Examples: export in vcf format with header</summary>

    % vtools init test -f
    % vtools import indels.vcf --build hg19
    % vtools export variant --header CHROM POS ID REF ALT QUAL FILTER INFO FORMAT -o my_indel.vcf
    % head -5 my_indel.vcf

    CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT
    1	10433	.	A	AC	.	PASS	.
    1	10439	.	AC	A	.	PASS	.
    1	54788	.	CC	C	.	PASS	.
    1	54789	.	C	CT	.	PASS	.




You can add `'%(sample_names)s'` to the header to add a list of sample names to the header if you are exporting sample genotypes (see examples below).

Alternatively you can create a text file with a tab delimited and use `--header -`. For example, we can use the header of an existing vcf file, and export variants with command



    % head -200 indels.vcf | grep '#' | vtools export variant --format ~/vtools/format/vcf --header - > my_indels.vcf

    INFO: Reading header from standard input
    Writing: 100% [=====================================================================] 137 13.8K/s in 00:00:00
    INFO: 129 lines are exported from variant table variant


</details>



##### Output genotype

Genotypes of selected samples can be outputted if you use use parameter `--samples` to specify samples to output. `--samples 1` will output genotypes of all samples.

<details><summary> Examples: export genotypes of selected samples</summary>

    % vtools init test -f
    % vtools import CEU_hg38.vcf --geno_info DP --var_info AA --build hg38
    % vtools export variant  --samples 'sample_name like "NA128%"' --format_string "GT" -o my.vcf

    INFO: Genotypes of 8 samples are exported.
    Writing: 100% [==============================================] 288 10.6K/s in 00:00:00
    INFO: 286 lines are exported from variant table variant with 1 failed records


    % head -10 my.vcf

    1   10533   .   G   C   .   PASS    .   GT  0/0 0/0 0/0 0/1 0/0 0/0 0/1 0/1
    1   51479   .   T   A   .   PASS    .   GT  0/0 0/0 0/1 0/1 0/0 0/0 0/0 0/0
    1   51928   .   G   A   .   PASS    .   GT  0/0 0/0 0/0 0/0 0/0 0/0 0/0 0/0
    1   54586   .   T   C   .   PASS    .   GT  0/1 0/0 0/0 0/0 0/0 0/0 0/0 0/0
    1   54676   .   C   T   .   PASS    .   GT  0/1 0/0 0/0 0/0 0/0 0/0 0/0 0/0
    1   54708   .   G   C   .   PASS    .   GT  0/1 0/0 0/0 0/0 0/0 0/0 0/0 0/0
    1   55299   .   C   T   .   PASS    .   GT  0/0 0/0 0/1 0/0 1/1 0/0 0/0 0/0
    1   62203   .   T   C   .   PASS    .   GT  0/1 0/0 0/0 0/0 0/0 0/0 0/0 0/1
    1   63671   .   G   A   .   PASS    .   GT  0/1 0/1 0/0 0/0 0/0 0/0 0/0 0/0
    1   86028   .   T   C   .   PASS    .   GT  0/0 0/0 1/1 0/0 0/1 0/0 0/0 0/0


</details>

You could export one or more genotype info fields using option `--geno_info` (Hint: use command `vtools show genotypes` to show available genotype fields). However, because the format string cannot be automatically determined, you will have to specify the `FORMAT` string manually using option `--format_string`,

<details><summary> Examples: export genotype info fields</summary>

    % vtools export variant --samples 'sample_name like "NA128%"' --geno_info DP_geno --format_string 'GT:DP' -o my.vcf

    INFO: Genotypes of 8 samples are exported.
    INFO: Using 2 processes to handle 8 samples
    Selecting genotypes: 100% [===================================] 5 4.9/s in 00:00:01
    my.vcf: 100% [=============================================] 292 5.1K/s in 00:00:00
    INFO: 288 lines are exported from variant table variant with 2 failed records


    % head -10 my.vcf

    1       10533   .       G       C       .       PASS    .       GT:DP   0/0:7   0/0:0   0/0:6   0/1:5   0/0:4   0/0:5   0/1:5   0/1:9
    1       51479   .       T       A       .       PASS    .       GT:DP   0/0:1   0/0:1   0/1:9   0/1:2   0/0:3   0/0:5   0/0:2   0/0:3
    1       51928   .       G       A       .       PASS    .       GT:DP   0/0:6   0/0:1   0/0:5   0/0:6   0/0:0   0/0:6   0/0:0   0/0:2
    1       54586   .       T       C       .       PASS    .       GT:DP   0/1:3   0/0:0   0/0:6   0/0:0   0/0:3   0/0:1   0/0:1   0/0:0
    1       54676   .       C       T       .       PASS    .       GT:DP   0/1:2   0/0:0   0/0:4   0/0:1   0/0:2   0/0:3   0/0:1   0/0:0
    1       54708   .       G       C       .       PASS    .       GT:DP   0/1:2   0/0:0   0/0:2   0/0:1   0/0:3   0/0:2   0/0:1   0/0:0
    1       55299   .       C       T       .       PASS    .       GT:DP   0/0:4   0/0:0   0/1:7   0/0:5   1/1:3   0/0:0   0/0:4   0/0:1
    1       62203   .       T       C       .       PASS    .       GT:DP   0/1:3   0/0:1   0/0:6   0/0:0   0/0:2   0/0:2   0/0:2   0/1:3
    1       63671   .       G       A       .       PASS    .       GT:DP   0/1:3   0/1:1   0/0:3   0/0:0   0/0:3   0/0:0   0/0:1   0/0:0
    1       86028   .       T       C       .       PASS    .       GT:DP   0/0:7   0/0:0   1/1:6   0/0:2   0/1:2   0/0:6   0/0:5   0/0:0


</details>



##### Export `ID`, `QUAL`, and `FILTER` columns

You can specify arbitrary fields (or constant values) to the `ID` (name), `QUAL`, and `FILTER` columns of the vcf output, using parameters `--id`, `--qual` and `--filter`. The `ID` column is supposed to list `rsnames` of variants, you can specify a field in your project (e.g. if you import the `id` field from the original vcf file), or `dbSNP.name`.

<details><summary> Examples: export id, qual and filter columns</summary> Suppose we have imported everything from the original vcf file,



    % export STOREMODE="sqlite"
    % vtools init test -f
    % vtools admin --load_snapshot vt_testData
    % vtools import CEU_hg38.vcf --var_info id qual filter info AA  --build hg38




we can export them for selected variants,



    % vtools select variant 'AA="T"' -t 'AA=T'
    % vtools export 'AA=T' --id id --qual qual --var_info info --filter filter -o my.vcf
    % head my.vcf

    1   54676   rs2462492   C   T   .   PASS    AA=T;AC=2;AN=120;DP=131
    22  50719683    .   T   C   .   PASS    AA=T;AC=1;AN=120;DP=298
    22  50719873    .   T   C   .   PASS    AA=T;AC=7;AN=120;DP=169
    22  50724422    rs5770822   C   T   .   PASS    AA=T;AC=41;AN=120;DP=367
    22  50725687    rs5770996   C   T   .   PASS    AA=T;AC=52;AN=120;DP=357
    22  50725859    rs6009957   T   C   .   PASS    AA=T;AC=37;AN=120;DP=331
    22  50734032    rs5770824   T   C   .   PASS    AA=T;AC=3;AN=120;DP=274
    22  50736511    .   C   T   .   PASS    AA=T;AC=4;AN=120;DP=317
    22  50737736    .   T   C   .   PASS    AA=T;AC=3;AN=120;DP=380
    22  50747800    rs3865766   C   T   .   PASS    AA=T;AC=51;AN=120;DP=253;HM3


Actually, because we are using columns such as `qual` from a VCF file, we can export these columns using a vcf `track`. The input `CEU.vcf.gz` file must be indexed though:




    % vtools export 'AA=T' --id id --qual 'track("CEU_hg38.vcf", "qual")' --var_info 'track("CEU_hg38.vcf", "info")' --filter 'track("CEU_hg38.vcf", "filter")' -o my.vcf
    % head my.vcf

    1   54676   rs2462492   C   T   .   PASS    AA=T;AC=2;AN=120;DP=131
    22  50719683    .   T   C   .   PASS    AA=T;AC=1;AN=120;DP=298
    22  50719873    .   T   C   .   PASS    AA=T;AC=7;AN=120;DP=169
    22  50724422    rs5770822   C   T   .   PASS    AA=T;AC=41;AN=120;DP=367
    22  50725687    rs5770996   C   T   .   PASS    AA=T;AC=52;AN=120;DP=357
    22  50725859    rs6009957   T   C   .   PASS    AA=T;AC=37;AN=120;DP=331
    22  50734032    rs5770824   T   C   .   PASS    AA=T;AC=3;AN=120;DP=274
    22  50736511    .   C   T   .   PASS    AA=T;AC=4;AN=120;DP=317
    22  50737736    .   T   C   .   PASS    AA=T;AC=3;AN=120;DP=380
    22  50747800    rs3865766   C   T   .   PASS    AA=T;AC=51;AN=120;DP=253;HM3




Optionally, you can use rsnames in the `dbSNP` database



    % vtools use dbSNP
    % vtools export 'AA=T' --id dbSNP.name --qual qual --var_info info --filter dbSNP.filter -o my.vcf
    % head my.vcf

    1   54676   rs2462492   C   T   .   .   AA=T;AC=2;AN=120;DP=131
    22  50719683    rs73174428  T   C   .   .   AA=T;AC=1;AN=120;DP=298
    22  50719873    rs117910162 T   C   .   .   AA=T;AC=7;AN=120;DP=169
    22  50724422    rs5770822   C   T   .   .   AA=T;AC=41;AN=120;DP=367
    22  50725687    rs5770996   C   T   .   .   AA=T;AC=52;AN=120;DP=357
    22  50725859    rs6009957   T   C   .   .   AA=T;AC=37;AN=120;DP=331
    22  50734032    rs5770824   T   C   .   .   AA=T;AC=3;AN=120;DP=274
    22  50736511    rs73174435  C   T   .   .   AA=T;AC=4;AN=120;DP=317
    22  50737736    rs76593947  T   C   .   .   AA=T;AC=3;AN=120;DP=380
    22  50747800    rs3865766   C   T   .   .   AA=T;AC=51;AN=120;DP=253;HM3

    % export STOREMODE="hdf5"


</details>

 [1]:    /documentation/customization/format/supportedformats/tped/
