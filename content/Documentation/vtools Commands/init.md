
+++
title = "Init"
description = ""
weight = 1
+++

# Create a new project 


## Usage

    % vtools init -h
    

    usage: vtools init [-h] [-f] [--parent DIR_or_SNAPSHOT] [--variants [TABLE]]
                       [--samples [COND [COND ...]]]
                       [--genotypes [COND [COND ...]]]
                       [--children DIR_OR_SNAPSHOT [DIR_OR_SNAPSHOT ...]]
                       [-v {0,1,2}]
                       project
    
    Create a new project in the current directory. This command will fail if
    another project already exists in this directory, unless option '--force' is
    used to remove the existing project.
    
    positional arguments:
      project               Name of a new project. This will create a new .proj
                            file under the current directory. Only one project is
                            allowed in a directory.
    
    optional arguments:
      -h, --help            show this help message and exit
      -f, --force           Remove a project if it already exists.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).
    
    Derive from a parent project:
      --parent DIR_or_SNAPSHOT
                            Directory or snapshot file of a parent project (e.g.
                            --parent ../main) from which all or part of variants
                            (--variants), samples (--samples) and genotypes
                            (--genotypes) will be copied to the newly created
                            project.
      --variants [TABLE]    A variant table of the parental project whose variants
                            will be copied to the new project. Default to variant
                            (all variants).
      --samples [COND [COND ...]]
                            Copy only samples of the parental project that match
                            specified conditions.
      --genotypes [COND [COND ...]]
                            Copy only genotypes that match specified conditions.
    
    Merge from children projects:
      --children DIR_OR_SNAPSHOT [DIR_OR_SNAPSHOT ...]
                            A list of a subprojects (directories or snapshot files
                            of projects) that will be merged to create this new
                            project. The subprojects must have the same primary
                            and alternative reference genome. Variant tables with
                            the same names from multiple samples will be merged.
                            Samples from the children projects will be copied even
                            if they were identical samples imported from the same
                            source files.
    
    
    



## Details

Command `` `vtools init `` creates a new project in the current directory. The project will be empty unless it is a child project from a parent project (with a subset of samples, variants etc), or a parent project of several children projects (with merged variants and samples). 

**A directory can only have one project**. After a project is created, subsequent `vtools` calls will automatically load the project in the current directory. Working from outside of a project directory is not allowed. 

A variant tools project `$name` consists of a project file `$name.proj`, a genotype database `$name_genotype.DB`, and a log file `$name.log`. In addition to the project databases under the project directory, variant tools will store 

*   annotation databases, format specification etc in a **local resource** directory, which is by default `~/.variant_tools`. You can use command "`vtools admin --set_runtime_option local_resource`" to relocate this directory if your home directory does not have enough free space. 
*   temporary files stored in a system **temporary directory**, which is usually under `/tmp`. If your temp partition is not large enough, you can set runtime option `temp_dir` to another directory. This directory will be cleared automatically after a project is closed, so do not point it to a directory with existing files. 



### Create a new project

Command `` `vtools init NAME `` creates a new project `NAME` under the current directory. It will fail if there is already a project in the current directory, unless option `--force` is used to remove any existing project. 

(:toggleexample Examples: create a new project:) The following commands create a directory `myproj` and create a variant tools project in this directory: 



    % mkdir myproj
    % cd myproj
    % vtools init myproj
    

    INFO: variant tools 1.0.4svn : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project myproj
    

If you attempt to create another project in the same directory, command `` `vtools init `` will fail with an error message: 



    % vtools init myproj
    

    Project myproj already exists. Please use option --force to remove it if you would like to start a new project.
    

Using the `--force` option will remove the existing project and create a new one: 



    % vtools init test --force
    

    INFO: variant tools 1.0.4svn : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project test
    

(:exampleend:) 



If you are worried about losing your work by accidentally calling `vtools init` with option `--force`, you could save copies of your project using command `` `vtools admin --save_snapshot `` from time to time, and load a saved snapshot using command `` `vtools admin --load_snapshot `` when needed. 



### Create a project from a parent project

A project could be created from a **parent project** with a subset of its variants and samples. For example, a child project with variants from a small chromosomal region could be created from a parent project to test a pipeline before it is applied to the whole project. This also allows differential analysis of subsets of variants (e.g. SNVs and indels) and samples. 

The following filters could be applied to the parent project 

*   `--variants` Only variants from the specified variant table of the parent project will be copied. Genotypes of samples will be affected because only genotypes related to these variants will be copied. 
*   `--samples` Only samples matching specified conditions (e.g. sample names) will be copied. 
*   `--genotypes` Only genotypes matching specified conditions (e.g. with quality score above certain threshold) will be copied. 

(:toggleexample Examples: create a parent project:) Let us start from a snapshot project `quickStartGuide`: 



    % vtools admin --load_snapshot vt_quickStartGuide
    

    Downloading snapshot vt_quickStartGuide.tar.gz from online
    --2012-11-13 10:19:30--  http://vtools.houstonbioinformatics.org//snapshot/vt_quickStartGuide.tar.gz
    Resolving vtools.houstonbioinformatics.org... 70.39.145.13
    Connecting to vtools.houstonbioinformatics.org|70.39.145.13|:80... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 112905 (110K) [application/x-gzip]
    Saving to: ‘/Volumes/Home/.variant_tools/snapshot/vt_quickStartGuide.tar.gz’
    
    100%[===================================================================================>] 112,905     --.-K/s   in 0.1s    
    
    2012-11-13 10:19:31 (859 KB/s) - ‘/Volumes/Home/.variant_tools/snapshot/vt_quickStartGuide.tar.gz’ saved [112905/112905]
    
    INFO: Snapshot vt_quickStartGuide has been loaded
    

This project has variants from two samples and a single master variant table with 4,858 variants: 



    % vtools show samples
    

    sample_name	filename
    CEU	CEU.exon...3.sites.vcf.gz
    JPT	JPT.exon...3.sites.vcf.gz
    



    % vtools show tables
    

    table                 #variants     date  message
    variant                   4,858 
    

Variants from the CEU and JPT samples could be selected to separate variant tables using commands 



    % vtools select variant --samples 'sample_name == "CEU"' -t CEU 'Variants from CEU population'
    

    INFO: 1 samples are selected by condition: sample_name == "CEU"
    Running: 8 923.8/s in 00:00:00                                                                                                                           
    INFO: 3489 variants selected.
    



    % vtools select variant --samples 'sample_name == "JPT"' -t JPT 'Variants from JPT population'
    

    INFO: 1 samples are selected by condition: sample_name == "JPT"
    Running: 6 729.5/s in 00:00:00                                                                                                                           
    INFO: 2900 variants selected.
    

The project now has three variant tables 



    % vtools show tables
    

    table                 #variants     date  message
    variant                   4,858           
    CEU                       3,489    Nov13  Variants from CEU population
    JPT                       2,900    Nov13  Variants from JPT population
    

(:exampleend:) 

(:toggleexample Examples: create subprojects from the parent project:) You can create a subproject with variants from the CEU: 



    % mkdir ../CEU
    % cd ../CEU
    % vtools init CEU --parent ../myproj --variants CEU
    

    Creating cache directory cache
    INFO: variant tools 1.0.4svn : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project CEU
    Copying variant tables ../myproj/test.proj: 100% [========================] 6 78.6/s in 00:00:00
    Copying samples: 100% [==================================================] 2 137.0/s in 00:00:00
    INFO: 3489 variants and 2 samples are copied
    

The new project has a master variant table with 3,489 variants: 



    % vtools show tables
    

    table                 #variants     date  message
    variant                   3,489           
    CEU                       3,489    Nov13  Variants from CEU population
    JPT                       1,531    Nov13  Variants from JPT population
    

and two samples (with subsets of variants): 



    % vtools show genotypes
    

    sample_name	filename	num_genotypes	sample_genotype_fields
    CEU	CEU.exon.2010_03.sites.vcf.gz	3489	
    JPT	JPT.exon.2010_03.sites.vcf.gz	1531
    

You can create another project with variants in the JPT population, and only the JPT sample: 



    % mkdir ../JPT
    % cd ../JPT
    % vtools init JPT  --parent ../myproj --variants JPT --samples 'sample_name == "JPT"'
    

    Creating cache directory cache
    INFO: variant tools 1.0.4svn : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project JPT
    Copying variant tables ../p1/test.proj: 100% [======================================] 6 33.6/s in 00:00:00
    Copying samples: 100% [============================================================] 1 161.0/s in 00:00:00
    INFO: 4858 variants and 1 samples are copied
    

The new JPT project has a master variant table with 2,900 variants, 

    % vtools show tables
    

    table                 #variants     date  message
    variant                   2,900           
    CEU                       1,531    Nov13  Variants from CEU population
    JPT                       2,900    Nov13  Variants from JPT population
    

and a single sample JPT: 



    % vtools show samples
    

    sample_name	filename
    JPT	JPT.exon...3.sites.vcf.gz
    



if you use `–-samples` (or `–-genotypes`) options without `–-variants` option to create a subproject, all of the variant tables in the parent project will be copied into your subproject, and the specified samples or genotypes will be copied to your subproject. 

(:exampleend:) 

The parent project does not have to be a directory. It can also be a local or online snapshot. For example, command 



    % vtools init test --parent vt_simple
    

    INFO: variant tools 2.3.0svn : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project test
    INFO: Extracting snapshot vt_simple to .
    Downloading snapshot vt_simple.tar.gz from online repository
    

will download snapshot `vt_simple` from online and become the present project. In addition, if you have a snapshot file, you can use command 



    % vtools init test --parent my_snapshot.tar.gz
    

which is a shortcut to commands 



    % vtools init test 
    % vtools admin --load_snapshot my_snapshot.tar.gz
    



### Create a project from several subprojects

A project could also be created from one or more **children projects**. This allows flexible handling of batches of data (e.g. analyze data separately or jointly), and parallel processing of large datasets (e.g. split a project by chromosomes, analyze them separately, and combine the results). 

Merging two or more variant tools projects will merge variants and samples from these projects. More specifically, 

*   variant tables with the same names are merged with duplicate variants removed 
*   variant info fields are merged. Projects that do not have certain fields will have `NULL` values for these fields. 
*   samples from the children projects are copied to the merged project even if they are identical. 

Because subprojects might have overlapping variants, variant tables, and samples, merging subproject might lead to unexpected results. 



Variant tables from children projects will be copied to `$name (from $proj)` before they are merged. This allows you to keep track of information from the original projects, or compare tables from children projects. 

(:toggleexample Examples: merge subprojects:) Continue from the previous example, if we just merge the CEU and JPT projects we created, 



    % mkdir ../merged
    % cd ../merged
    % vtools init merged --children ../CEU ../JPT 
    

    INFO: variant tools 1.0.4svn : Copyright (c) 2011 - 2012 Bo Peng
    INFO: San Lucas FA, Wang G, Scheet P, Peng B (2012) Bioinformatics 28(3):421-422
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project merged
    WARNING: 1 samples from the same source files have been copied, leading to potentially duplicated samples.
    Loading ../CEU/CEU (1/2): 0 0.0/s in 00:00:00                                                     
    Loading ../JPT/JPT (2/2): 0 0.0/s in 00:00:00                                                     
    Merging all projects: 100% [==============================================] 21 21.0/s in 00:00:01
    

we will see that variants from these two projects are corrected merged 



    % vtools show tables
    

    table                 #variants     date  message
    variant                   4,858           
    CEU                       3,489    Nov13  Variants from CEU population
    JPT                       2,900    Nov13  Variants from JPT population         
    

but we have three samples with different number of variants 

    % vtools show genotypes
    

    sample_name	filename	num_genotypes	sample_genotype_fields
    CEU	CEU.exon.2010_03.sites.vcf.gz	3489	
    JPT	JPT.exon.2010_03.sites.vcf.gz	1531	
    JPT	JPT.exon.2010_03.sites.vcf.gz	2900
    

Because the latter two samples have the same name, it is even difficult to remove one of them using command `vtools remove samples`. If you have to merge samples with the same names from different projects, it is recommended that you use command `vtools admin --rename_samples` to change names of samples before merging, and remove duplicated samples afterwards. 



If you have a large number of samples from different sources, it is a good idea to create subprojects for groups of samples. Merging subprojects will be faster than reading from source files again. However, due to the overhead of re-mapping all variants, pre-processing each sample by creating its own project usually does not help much. 

(:exampleend:) 

The children projects can also be snapshots, so if you have snapshots of a number of children projects, you can create a merged project using command 



    % vtools init test --children max_gt_data.tar poly_data.tar
    

The snapshots can also be an online snapshot so you can use an online snapshot to start your new project: 



    % vtools init test --children vt_simple