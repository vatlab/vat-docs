+++
title = "anno_utils"
weight = 2
+++

## Annotation utility pipelines 



### 1. Usage

    % vtools show pipeline anno_utils

    This file defines a number of pipelines to manipulate variant tools annotation
    databases.
    
    Available pipelines: annFileFromText, annFileFromVcf, annoDB2proj, proj2annoDB
    
    Pipeline "annFileFromText":  This pipeline reads a tab, comma or space
    delimited file, take its header as name of fields, guess the type of each
    column, and output an .ann file with these fields. The annotation database is
    assumed to be of type "field" and use the first column as the linked field.
    The input file of this pipeline should be the text file, and the ouput file
    should be an .ann file. If the .ann file is created correctly, it can be used
    to create an annotation database from the input text file.
      annFileFromText_10: Create a feild description file from input text file.
      annFileFromText_20: Create an annotation file from fields guessed from input
                          file
    
    Pipeline "annFileFromVcf":  This pipeline reads the header of a vcf file and
    creates an .ann file with chr, pos, ref, alt, and fields from all INFO fields.
    The input file can be a file (.vcf or .vcf.gz) or a URL (.vcf.gz only). The
    file must be tabix-indexed if it is bgzipped. The output file is an .ann file,
    which can be used to create an annotation database for the vcf file. This
    pipeline tries to guess the reference genome used from the VCF file but you
    should always check if the correct reference genome is generated.
      annFileFromVcf_10:  Create a feild description file from input text file.
      annFileFromVcf_20:  Create an annotation file from fields guessed from input
                          vcf file
    
    Pipeline "annoDB2proj":  This pipeline creates a variant tools project from a
    variant-based annotation database. The input of this pipeline should be the
    .DB or .DB.gz file of an annotation database. The output should be name of a
    directory within which the project will be created. The output directory will
    be created if it does not exist. Any existing project in that directory will
    be removed.
      annoDB2proj_0:      Check the existence of command sqlite3, which is
                          required for this pipeline
      annoDB2proj_10:     Decompress .DB.gz file if needed
      annoDB2proj_20:     Dump the structure of the the variant table to
                          cache/$PROJ.schema.
      annoDB2proj_25:     Determine build information for the annotation database
      annoDB2proj_30:     Create a .fmt file for variants in annotation database
      annoDB2proj_40:     Create an input format definition file .fmt
      annoDB2proj_50:     Dump the annotation database to a text file
      annoDB2proj_60:     Create a project if it does not exist
      annoDB2proj_70:     Create a project and import data
    
    Pipeline "proj2annoDB":  This pipeline creates an annotation database using
    variants and variant info fields of a variant tools project. The database can
    then be used, for example, to filter variants from another project. The input
    of this pipeline should be a vtools project database ($name.proj), the output
    is a .ann file ($name.ann). $name.ann, $name.DB and $name.DB.gz will be
    created. If a variant table is specified through parameter -export, only
    variants in specified variant table will be dumped.
      proj2annoDB_0:      Check the existence of command sqlite3, which is
                          required for this pipeline
      proj2annoDB_10:     Dump the structure of the the variant table to
                          cache/$PROJ.schema.
      proj2annoDB_11:     Convert .schema to .ann definitions
      proj2annoDB_20:     Create an annotation definition file (.ann)
      proj2annoDB_30:     Dump the variant table to a text file
      proj2annoDB_40:     Create annotation database from dumped text file
    
    Pipeline parameters:
      export              A variant table to create annotation database
                          from for pipeline proj2annoDB (default: variant)
    



### 2. Details

 

#### 2.1 Converting a project to an annotation database (pipeline `proj2annoDB`)

You might have several projects and would like to use them to analyze a new project. For example, you might want to exclude from a project all variants that exist in a few control project (or projects with normal unaffected samples). You could achieve this by merging all these projects and analyze all variants together, but a more convenient way is to build annotation databases from these project and use them in the new project. 

The `proj2annoDB` pipeline defined in `anno_utils.pipeline` can be used for this purpose. It exports all variants and variant info fields of the master variant table, or a specified variant table (parameter `--export` to a file and create an annotation database using a generated `.ann` file. 

<details><summary> Create an annotation database from a project</summary> 

    % vtools init test
    % vtools admin --load_snapshot vt_quickStartGuide
    % vtools execute anno_utils proj2annoDB --input test.proj --output myanno.ann
    
    INFO: Executing step proj2annoDB_0 of pipeline anno_utils: Check the existence of command sqlite3, which is required for this pipeline
    INFO: Command sqlite3 is located.
    INFO: Executing step proj2annoDB_5 of pipeline anno_utils: Dump project build information
    INFO: Running "sqlite3 test.proj 'select value from project where name="build"' > cache/test.proj.build"
    INFO: Output redirected to cache/test.proj.build.out_10717 and cache/test.proj.build.err_10717 and will be saved to cache/test.proj.build.exe_info after completion of command.
    INFO: Command "sqlite3 test.proj 'select value from project where name="build"' > cache/test.proj.build" completed successfully in 00:00:11
    INFO: Executing step proj2annoDB_10 of pipeline anno_utils: Dump the structure of the the variant table to cache/$PROJ.schema.
    INFO: Running "sqlite3 test.proj ".schema variant" > cache/test.proj.schema"
    INFO: Output redirected to cache/test.proj.schema.out_10717 and cache/test.proj.schema.err_10717 and will be saved to cache/test.proj.schema.exe_info after completion of command.
    INFO: Command "sqlite3 test.proj ".schema variant" > cache/test.proj.schema" completed successfully in 00:00:11
    INFO: Executing step proj2annoDB_11 of pipeline anno_utils: Convert .schema to .ann definitions
    INFO: Running "echo "None command executed.""
    INFO: Output redirected to cache/test.proj.ann_tmp.out_10717 and cache/test.proj.ann_tmp.err_10717 and will be saved to cache/test.proj.ann_tmp.exe_info after completion of command.
    INFO: Command "echo "None command executed."" completed successfully in 00:00:00
    INFO: Executing step proj2annoDB_20 of pipeline anno_utils: Create an annotation definition file (.ann)
    INFO: Running "echo '[linked fields]' > myanno.ann; echo 'hg18=chr, pos, ref, alt' >> myanno.ann; echo '[data sources]' >> myanno.ann; echo 'description=Annotation database dumped from project test.proj' >> myanno.ann; echo 'delimiter="|"' >> myanno.ann; echo 'anno_type=variant' >> myanno.ann; echo 'source_type=txt' >> myanno.ann; cat cache/test.proj.ann_tmp >> myanno.ann"
    INFO: Output redirected to myanno.ann.out_10717 and myanno.ann.err_10717 and will be saved to myanno.ann.exe_info after completion of command.
    INFO: Command "echo '[linked fields]' > myanno.ann; echo 'hg18=chr, pos, ref, alt' >> myanno.ann; echo '[data sources]' >> myanno.ann; echo 'description=Annotation database dumped from project test.proj' >> myanno.ann; echo 'delimiter="|"' >> myanno.ann; echo 'anno_type=variant' >> myanno.ann; echo 'source_type=txt' >> myanno.ann; cat cache/test.proj.ann_tmp >> myanno.ann" completed successfully in 00:00:11
    INFO: Executing step proj2annoDB_30 of pipeline anno_utils: Dump the variant table to a text file
    INFO: Running "sqlite3 test.proj "select * from variant ;" > cache/test.proj.dump"
    INFO: Output redirected to cache/test.proj.dump.out_10717 and cache/test.proj.dump.err_10717 and will be saved to cache/test.proj.dump.exe_info after completion of command.
    INFO: Command "sqlite3 test.proj "select * from variant ;" > cache/test.proj.dump" completed successfully in 00:00:11
    INFO: Executing step proj2annoDB_40 of pipeline anno_utils: Create annotation database from dumped text file
    INFO: Running "vtools use myanno.ann --files cache/test.proj.dump --rebuild"
    INFO: Output redirected to myanno.DB.gz.out_10717 and myanno.DB.gz.err_10717 and will be saved to myanno.DB.gz.exe_info after completion of command.
    INFO: Command "vtools use myanno.ann --files cache/test.proj.dump --rebuild" completed successfully in 00:00:11
    



You can export variant from a selected variant table by passing the name of the variant table to parameter `--export`. 

You can then use this annotation database to annotation other projects 



    % vtools use /path/to/myanno
    % vtools select variant 'myanno.chr is not NULL' -o chr pos ref alt myanno.AA myanno.AN -l 10
    
    1	1105366	T	C	T	114
    1	1105411	G	A	G	106
    1	1108138	C	T	c	130
    1	1110240	T	A	T	178
    1	1110294	G	A	A	158
    1	3537996	T	C	C	156
    1	3538692	G	C	G	178
    1	3541597	C	T	C	178
    1	3541652	G	A	G	202
    1	3545211	G	A	G	178
    

</details>

 

#### 2.2 Converting a variant-based annotation database to a project (pipeline `annoDB2proj`)

If you would like to study a variant-based annotation database in details, for example, to annotate these variants using other annotation databases, you can convert it to a variant tools project using the `annoDB2proj` pipeline defined in `anno_utils.pipeline`. The resulting project has all the variants in the annotation database, but not the annotation fields, so you will have to `use` the original annotation database to get the annotations. 


{{% notice warning%}}
Annotation databases sometimes have multiple annotations for a variant (e.g. more than one dbSNP names for a variant). These variants will be imported only once in the resulting variant tools project. 
{{% /notice %}}

<details><summary> Convert database dbSNP to a project</summary> The input of this pipeline is the database DB file, which is usually under `~/.variant_tools/annoDB`. The output should be name of a directory that holds the created project. 



    % vtools init test_proj
    % vtools execute anno_utils annoDB2proj --input ~/.variant_tools/annoDB/dbSNP-hg19_137.DB.gz --output dbSNP
    
    INFO: Executing step annoDB2proj_0 of pipeline anno_utils: Check the existence of command sqlite3, which is required for this pipeline
    INFO: Command sqlite3 is located.
    INFO: Executing step annoDB2proj_10 of pipeline anno_utils: Decompress .DB.gz file if needed
    INFO: Decompressing /Users/bpeng/.variant_tools/annoDB/dbSNP-hg19_137.DB.gz to cache/dbSNP-hg19_137.DB
    INFO: Executing step annoDB2proj_20 of pipeline anno_utils: Dump the structure of the the variant table to cache/$PROJ.schema.
    INFO: Running "sqlite3 cache/dbSNP-hg19_137.DB ".schema dbSNP" > cache/dbSNP.schema"
    INFO: Output redirected to cache/dbSNP.schema.out_9315 and cache/dbSNP.schema.err_9315 and will be saved to cache/dbSNP.schema.exe_info after completion of command.
    INFO: Command "sqlite3 cache/dbSNP-hg19_137.DB ".schema dbSNP" > cache/dbSNP.schema" completed successfully in 00:00:11
    INFO: Executing step annoDB2proj_25 of pipeline anno_utils: Determine build information for the annotation database
    INFO: Running "sqlite3 cache/dbSNP-hg19_137.DB "select value from dbSNP_info WHERE name = 'build'" > cache/dbSNP.build"
    INFO: Output redirected to cache/dbSNP.build.out_9315 and cache/dbSNP.build.err_9315 and will be saved to cache/dbSNP.build.exe_info after completion of command.
    INFO: Command "sqlite3 cache/dbSNP-hg19_137.DB "select value from dbSNP_info WHERE name = 'build'" > cache/dbSNP.build" completed successfully in 00:00:00
    INFO: Executing step annoDB2proj_30 of pipeline anno_utils: Create a .fmt file for variants in annotation database
    INFO: Running "echo "None command executed.""
    INFO: Output redirected to cache/dbSNP.fmt_tmp.out_9315 and cache/dbSNP.fmt_tmp.err_9315 and will be saved to cache/dbSNP.fmt_tmp.exe_info after completion of command.
    INFO: Command "echo "None command executed."" completed successfully in 00:00:00
    INFO: Executing step annoDB2proj_40 of pipeline anno_utils: Create an input format definition file .fmt
    INFO: Running "echo '[format description]' > cache/dbSNP.fmt; echo 'description=Project created from annotation database /Users/bpeng/.variant_tools/annoDB/dbSNP-hg19_137.DB.gz' >> cache/dbSNP.fmt; echo 'variant=chr, start, refNCBI, alt' >> cache/dbSNP.fmt; echo 'delimiter="|"' >> cache/dbSNP.fmt; cat cache/dbSNP.fmt_tmp >> cache/dbSNP.fmt"
    INFO: Output redirected to cache/dbSNP.fmt.out_9315 and cache/dbSNP.fmt.err_9315 and will be saved to cache/dbSNP.fmt.exe_info after completion of command.
    INFO: Command "echo '[format description]' > cache/dbSNP.fmt; echo 'description=Project created from annotation database /Users/bpeng/.variant_tools/annoDB/dbSNP-hg19_137.DB.gz' >> cache/dbSNP.fmt; echo 'variant=chr, start, refNCBI, alt' >> cache/dbSNP.fmt; echo 'delimiter="|"' >> cache/dbSNP.fmt; cat cache/dbSNP.fmt_tmp >> cache/dbSNP.fmt" completed successfully in 00:00:11
    INFO: Executing step annoDB2proj_50 of pipeline anno_utils: Dump the annotation database to a text file
    INFO: Running "sqlite3 cache/dbSNP-hg19_137.DB "select * from dbSNP;" > cache/dbSNP.dump"
    INFO: Output redirected to cache/dbSNP.dump.out_9315 and cache/dbSNP.dump.err_9315 and will be saved to cache/dbSNP.dump.exe_info after completion of command.
    INFO: Command "sqlite3 cache/dbSNP-hg19_137.DB "select * from dbSNP;" > cache/dbSNP.dump" completed successfully in 00:06:58
    INFO: Executing step annoDB2proj_60 of pipeline anno_utils: Create a project if it does not exist
    INFO: Running "if [ ! -d dbSNP ]; then mkdir dbSNP; fi"
    INFO: Command "if [ ! -d dbSNP ]; then mkdir dbSNP; fi" completed successfully in 00:00:11
    INFO: Executing step annoDB2proj_70 of pipeline anno_utils: Create a project and import data
    INFO: Running "vtools init -v2 --force dbSNP"
    INFO: Output redirected to dbSNP/dbSNP.proj.out_9315 and dbSNP/dbSNP.proj.err_9315 and will be saved to dbSNP/dbSNP.proj.exe_info after completion of command.
    INFO: Command "vtools init -v2 --force dbSNP" completed successfully in 00:00:11
    INFO: Running "vtools import /Users/bpeng/Temp/cache/dbSNP.dump --format /Users/bpeng/Temp/cache/dbSNP.fmt --build hg19"
    

</details>

 

#### 2.3 Create an annotation specification file (.ann file) from a local or online VCF file (pipeline `annFileFromVcf`)

The default `vtools import` command by default imports variants but not related info fields from a vcf file. To access the info fields, you have the choices of 

*   Use option `--var_info` to import selected variant info to the project. 
*   Use command `vtools update` to import variant info later when you need them. 
*   Use the `track()` function to retrieve such information for a few variants, or 
*   Create an annotation database from the vcf file so that you can access variant info quickly without increasing the size of the project. 

The pipeline `annFileFromVcf` is designed to help you generate an annotation database from an input VCF file (but it also accepts a URL for an online vcf file) by extracting field information from the vcf file and creates an `.ann` file. 

<details><summary> Create an .ann file from the vcf file from the dbSNP vcf file </summary> The input of this pipeline is the database DB file, which is usually under `~/.variant_tools/annoDB`. The output should be name of a directory that holds the created project. 



    % vtools init test_proj
    % vtools execute anno_utils annFileFromVcf --input ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz --output dbSNP.ann
    
    INFO: Executing anno_utils.annFileFromVcf_10: Create a feild description file from input text file.
    [get_local_version] downloading the index file...
    INFO: Executing anno_utils.annFileFromVcf_20: Create an annotation file from fields guessed from input vcf file
    INFO: Running echo '# Please refer to http://varianttools.sourceforge.net/Annotation/New' > dbSNP.ann; echo '# for a description of the format of this file.' >> dbSNP.ann; echo '' >> dbSNP.ann; echo '[linked fields]' >> dbSNP.ann; echo 'hg19=chr,pos,ref,alt' >> dbSNP.ann; echo '' >> dbSNP.ann; echo '[data sources]' >> dbSNP.ann; echo 'description=An annotation database created from' ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz >> dbSNP.ann; echo 'version=' >> dbSNP.ann; echo 'anno_type=variant' >> dbSNP.ann; echo 'direct_url=' >> dbSNP.ann; echo 'source_url='ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz >> dbSNP.ann; echo 'source_type=txt' >> dbSNP.ann; echo 'source_pattern=' >> dbSNP.ann; echo '' >> dbSNP.ann; cat cache/00-All.vcf.gz.fields >> dbSNP.ann
    INFO: Command "echo '# Please refer to http://varianttools.sourceforge.net/Annotation/New' > dbSNP.ann; echo '# for a description of the format of this file.' >> dbSNP.ann; echo '' >> dbSNP.ann; echo '[linked fields]' >> dbSNP.ann; echo 'hg19=chr,pos,ref,alt' >> dbSNP.ann; echo '' >> dbSNP.ann; echo '[data sources]' >> dbSNP.ann; echo 'description=An annotation database created from' ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz >> dbSNP.ann; echo 'version=' >> dbSNP.ann; echo 'anno_type=variant' >> dbSNP.ann; echo 'direct_url=' >> dbSNP.ann; echo 'source_url='ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz >> dbSNP.ann; echo 'source_type=txt' >> dbSNP.ann; echo 'source_pattern=' >> dbSNP.ann; echo '' >> dbSNP.ann; cat cache/00-All.vcf.gz.fields >> dbSNP.ann" completed successfully in 00:00:01
    

</details>


{{% notice warning%}}
The created .ann file might not have the correct build information and might not be always usable due to, for example, unacceptable field name. Always check the .ann file before you create an annotation database from it. 
{{% /notice %}}
 

#### 2.4 Create an annotation specification file (.ann file) from a text file (pipeline `annFileFromText`)

During the analysis of dataset, you might have some summary report that can be used to direct further analysis, or you might have a text file that annotate some or all fields of your project. This pipeline help you convert these files to an annotation database so that you can use it in the project. 

<details><summary> Create an annotation database from summary statistics outputted from command `vtools output`</summary> For example, the following command counts the number of variants (in a variant table called `kg`, across all samples) and output know gene ID and the counts to a text file. 



    % vtools output kg knownGene.name 'sum(variant.num)' --group_by knownGene.name --header > kg.count
    

The text file looks like this 



    % head -5 kg.count
    
    knownGene name	sum variant num
    uc001abt.4	5
    uc001abv.1	18
    uc001abw.1	32
    uc001abx.1	16
    

If you have a project with all affected samples and would like to identify novel variants that are causing the disease, you might want to remove variants that are very rare in the sample. However, doing so might not be wise because different variants in a gene might have the same effect and each of them is rare. In this case, you might want to remove all variants that appear only once (or very few times) in a gene. The information you obtained in the output of the above command can be useful. 

However, you will need to import the genotype counts into the project before you can use it. Because the text file contains annotation information for field `knownGene.name`, it is best to create an field-based annotation database that annotate this field. Pipeline `annFileFromText` from `anno_utils` can help you during this process. For example 



    % vtools execute anno_utils annFileFromText -i kg.count  -o kg_sum_geno.ann   

    INFO: Executing step annFileFromText_10 of pipeline anno_utils: Create a feild description file from input text file.
    INFO: Executing step annFileFromText_20 of pipeline anno_utils: Create an annotation file from fields guessed from input file
    INFO: Running "echo '[linked fields]' > kg_sum_geno.ann; echo '*=knownGene_name' >> kg_sum_geno.ann; echo '' >> kg_sum_geno.ann; echo '[data sources]' >> kg_sum_geno.ann; echo 'description=Field annotation database created by pipeline annFileFromText (in anno_utils.pipeline) from text file kg.count' >> kg_sum_geno.ann; echo 'anno_type=field' >> kg_sum_geno.ann; echo 'header=1' >> kg_sum_geno.ann; echo 'source_url=kg.count' >> kg_sum_geno.ann; echo 'source_type=txt' >> kg_sum_geno.ann;"
    INFO: Output redirected to kg_sum_geno.ann.out_69301 and kg_sum_geno.ann.err_69301 and will be saved to kg_sum_geno.ann.exe_info after completion of command.
    INFO: Command "echo '[linked fields]' > kg_sum_geno.ann; echo '*=knownGene_name' >> kg_sum_geno.ann; echo '' >> kg_sum_geno.ann; echo '[data sources]' >> kg_sum_geno.ann; echo 'description=Field annotation database created by pipeline annFileFromText (in anno_utils.pipeline) from text file kg.count' >> kg_sum_geno.ann; echo 'anno_type=field' >> kg_sum_geno.ann; echo 'header=1' >> kg_sum_geno.ann; echo 'source_url=kg.count' >> kg_sum_geno.ann; echo 'source_type=txt' >> kg_sum_geno.ann;" completed successfully in 00:00:11
    INFO: Running "cat cache/kg.count.fields >> kg_sum_geno.ann"
    INFO: Command "cat cache/kg.count.fields >> kg_sum_geno.ann" completed successfully in 00:00:12
    

The .ann file created looks like 



    % cat kg_sum_geno.ann   

    [linked fields]
    *=knownGene_name
    
    [data sources]
    description=Field annotation database created by pipeline annFileFromText (in anno_utils.pipeline) from text file kg.count
    anno_type=field
    header=1
    source_url=kg.count
    source_type=txt
    delimiter="\t"
    
    [knownGene_name]
    index=1
    type=VARCHAR(10)
    
    [sum_variant_num]
    index=2
    type=INT
    

And you can use it to create an annotation database from `kg.count` and link it to the project 



    % vtools use kg_sum_geno.ann --linked_by knownGene.name  

    INFO: Importing database kg_sum_geno from source files ['kg.count']
    INFO: Importing annotation data from kg.count
    kg.count: 100% [========================================================] 61,214 32.3K/s in 00:00:01
    INFO: 61224 records are handled, 0 ignored.
    INFO: Using annotation DB kg_sum_geno in project Arun.
    INFO: Field annotation database created by pipeline annFileFromText (in anno_utils.pipeline) from text file kg.count
    INFO: 61223 out of 80922 knowngene.name are annotated through annotation database kg_sum_geno
    

You can then use the `sum_variant_num` field from the `kg_sum_geno` database to filter variants: 



    % vtools select kg 'kg_sum_geno.sum_variant_num = 1' -t rare_variants  

    Running: 10,468 696.0/s in 00:00:15
    INFO: 2717 variants selected.
    

Compared to the number of singletons in the project, the above command identified a lot less variants. 



    % vtools select kg 'variant.num=1' -c

    Counting variants: 973 346.9/s in 00:00:02
    627489
    



Using `vtools select` with condition `kg_sum_geno.sum_variant_num = 1` will include variants that appear in more than one gene but has count 1 in one of them. It is better to use `vtools exclude` and condition `kg_sum_geno.sum_variant_num > 1` to find out variants that appear in only one gene once. 

</details>