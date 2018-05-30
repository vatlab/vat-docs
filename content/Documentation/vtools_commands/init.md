+++
title = "init"
weight = 1
+++

## Create a new project 

### 1. Usage

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


### 2. Details

Command `vtools init` creates a new project in the current directory. The project will be empty unless it is a child project from a parent project (with a subset of samples, variants etc), or a parent project of several children projects (with merged variants and samples). 

**A directory can only have one project**. After a project is created, subsequent `vtools` calls will automatically load the project in the current directory. Working from outside of a project directory is not allowed. 

A variant tools project `$name` consists of a project file `$name.proj`, a genotype database `$name_genotype.DB`, and a log file `$name.log`. In addition to the project databases under the project directory, variant tools will store 

*   annotation databases, format specification etc in a **local resource** directory, which is by default `~/.variant_tools`. You can use command "`vtools admin --set_runtime_option local_resource`" to relocate this directory if your home directory does not have enough free space. 
*   temporary files stored in a system **temporary directory**, which is usually under `/tmp`. If your temp partition is not large enough, you can set runtime option `temp_dir` to another directory. This directory will be cleared automatically after a project is closed, so do not point it to a directory with existing files. 



#### 2.1 Create a new project

Command `` `vtools init NAME `` creates a new project `NAME` under the current directory. It will fail if there is already a project in the current directory, unless option `--force` is used to remove any existing project. 

<details><summary> Examples: create a new project</summary> The following commands create a directory `myproj` and create a variant tools project in this directory: 

    % mkdir myproj
    % cd myproj
    % vtools init myproj
    
    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project myproj
    

If you attempt to create another project in the same directory, command `` `vtools init `` will fail with an error message: 

    % vtools init myproj
    
    ERROR: A project can only be created in a directory without another project.

Using the `--force` option will remove the existing project and create a new one: 

    % vtools init test --force
    
    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project test
    
</details>


{{% notice tip %}}
If you are worried about losing your work by accidentally calling `vtools init` with option `--force`, you could save copies of your project using command `` `vtools admin --save_snapshot `` from time to time, and load a saved snapshot using command `` `vtools admin --load_snapshot `` when needed.
{{% /notice %}}



#### 2.2 Create a project from a parent project

A project could be created from a **parent project** with a subset of its variants and samples. For example, a child project with variants from a small chromosomal region could be created from a parent project to test a pipeline before it is applied to the whole project. This also allows differential analysis of subsets of variants (e.g. SNVs and indels) and samples. 

The following filters could be applied to the parent project 

*   `--variants` Only variants from the specified variant table of the parent project will be copied. Genotypes of samples will be affected because only genotypes related to these variants will be copied. 
*   `--samples` Only samples matching specified conditions (e.g. sample names) will be copied. 
*   `--genotypes` Only genotypes matching specified conditions (e.g. with quality score above certain threshold) will be copied. 

<details><summary> Examples: create a parent project</summary> Let us start from a snapshot project `quickStartGuide`: 

    % vtools admin --load_snapshot vt_quickStartGuide_v3
    
    Downloading snapshot vt_quickStartGuide_v3.tar.gz from online repository
    Extracting vt_quickStartGuide_v3: 100% [===================================] 148,585 20.1M/s in 00:00:00
    INFO: Snapshot vt_quickStartGuide_v3 has been loaded

    
This project has variants from two samples and a single master variant table with 4,858 variants: 

    % vtools show samples

    sample_name filename
    CEU         CEU_hg38_all.vcf
    JPT         JPT_hg38_all.vcf
    
    % vtools show tables
    
    table      #variants     date message
    variant        4,839    May30 Master variant table
    
Variants from the HG00096 and HG00479 samples could be selected to separate variant tables using commands 

    % vtools select variant --samples "sample_name=='CEU'" -t CEU
                                 
    INFO: 3470 variants selected.
    
    % vtools select variant --samples "sample_name=='JPT'" -t JPT
    
    INFO: 2878 variants selected.

The project now has three variant tables 

    % vtools show tables
    
    table      #variants     date message
    CEU            3,470    May30
    JPT            2,878    May30
    variant        4,839    May30 Master variant table
    

</details>

<details><summary> Examples: create subprojects from the parent project (The "--variants" option is only supported when STOREMODE is set to sqlite )</summary> You can create a subproject with variants from the CEU: 


    % mkdir myproj
    % cd myproj
    % vtools admin --load_snapshot vt_quickStartGuide
    % export STOREMODE="sqlite"
    % vtools select variant --samples 'sample_name == "CEU"' -t CEU 'Variants from CEU population'
    % vtools select variant --samples 'sample_name == "JPT"' -t JPT 'Variants from JPT population'
    % mkdir ../CEU
    % cd ../CEU
    % vtools init CEU --parent ../myproj --variants CEU
    
    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project CEU
    Copying variant tables ../myproj/test.proj: 100% [============================] 6 251.6/s in 00:00:00
    Copying samples: 100% [=======================================================] 2 211.4/s in 00:00:00
    INFO: 3489 variants and 2 samples are copied
    

The new project has a master variant table with 3,489 variants: 



    % vtools show tables
    
    table      #variants     date message
    CEU            3,489    May14 Variants from CEU population
    JPT            1,531    May14 Variants from JPT population
    variant        3,489
    

and two samples (with subsets of variants): 



    % vtools show genotypes
    
    sample_name	filename	num_genotypes	sample_genotype_fields
    CEU	CEU.exon.2010_03.sites.vcf.gz	3489	
    JPT	JPT.exon.2010_03.sites.vcf.gz	1531
    

You can create another project with variants in the JPT population, and only the JPT sample: 



    % mkdir ../JPT
    % cd ../JPT
    % vtools init JPT  --parent ../myproj --variants JPT --samples 'sample_name == "JPT"'
    
    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project JPT
    Copying variant tables ../myproj/test.proj: 100% [==================================] 6 214.4/s in 00:00:00
    Copying samples: 100% [=============================================================] 1 111.3/s in 00:00:00
    INFO: 4858 variants and 1 samples are copied
    

The new JPT project has a master variant table with 2,900 variants, 

    % vtools show tables
    
    table      #variants     date message
    CEU            1,531    May14 Variants from CEU population
    JPT            2,900    May14 Variants from JPT population
    variant        2,900    
    

and a single sample JPT: 



    % vtools show samples
    
    sample_name	filename
    JPT        	JPT.exon...3.sites.vcf.gz




if you use `–-samples` (or `–-genotypes`) options without `–-variants` option to create a subproject, all of the variant tables in the parent project will be copied into your subproject, and the specified samples or genotypes will be copied to your subproject. 

</details>

The parent project does not have to be a directory. It can also be a local or online snapshot. For example, command 


    % mkdir ../test
    % cd ..test
    % vtools init test --parent vt_simple
    
    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project test
    INFO: Extracting snapshot vt_simple to .
    Downloading snapshot vt_simple.tar.gz from online repository
    Extracting vt_simple: 100% [====================================================] 41,325 5.4M/s in 00:00:00
    

will download snapshot `vt_simple` from online and become the present project. In addition, if you have a snapshot file, you can use command 



    % vtools init test --parent my_snapshot.tar.gz
    

which is a shortcut to commands 



    % vtools init test 
    % vtools admin --load_snapshot my_snapshot.tar.gz
    



#### 2.3 Create a project from several subprojects


##### This function is only supported when STOREMODE is set to sqlite. 

A project could also be created from one or more **children projects**. This allows flexible handling of batches of data (e.g. analyze data separately or jointly), and parallel processing of large datasets (e.g. split a project by chromosomes, analyze them separately, and combine the results). 

Merging two or more variant tools projects will merge variants and samples from these projects. More specifically, 

*   variant tables with the same names are merged with duplicate variants removed 
*   variant info fields are merged. Projects that do not have certain fields will have `NULL` values for these fields. 
*   samples from the children projects are copied to the merged project even if they are identical. 

Because subprojects might have overlapping variants, variant tables, and samples, merging subproject might lead to unexpected results. 



{{% notice tip %}}
Variant tables from children projects will be copied to `$name (from $proj)` before they are merged. This allows you to keep track of information from the original projects, or compare tables from children projects.
{{% /notice %}}

<details><summary> Examples: merge subprojects</summary> Continue from the previous example, if we just merge the CEU and JPT projects we created, 

    % mkdir ../merged
    % cd ../merged
    % vtools init merged --children ../CEU ../JPT 
    
    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project merged
    Loading ../CEU/CEU (1/2): 0 0.0/s in 00:00:00                                                              
    Loading ../JPT/JPT (2/2): 0 0.0/s in 00:00:00                                                              
    Merging all projects: 100% [========================================================] 22 21.9/s in 00:00:01

    

we will see that variants from these two projects are corrected merged 



    % vtools show tables
    
    table                 #variants     date message
    CEU                       3,489    May14 Variants from CEU population (merged)
    CEU (from CEU)            3,489    May14 Variants from CEU population (from CEU)
    CEU (from JPT)            1,531    May14 Variants from CEU population (from JPT)
    JPT                       2,900    May14 Variants from JPT population (merged)
    JPT (from CEU)            1,531    May14 Variants from JPT population (from CEU)
    JPT (from JPT)            2,900    May14 Variants from JPT population (from JPT)
    variant                   4,858    May14  (merged)
    variant (from CEU)        3,489           (from CEU)
    variant (from JPT)        1,369           (from JPT)        
    

but we have three samples with different number of variants 

    % vtools show genotypes
    
    sample_name	filename                 	num_genotypes	sample_genotype_fields
    CEU        	CEU.exon...3.sites.vcf.gz	3489         	
    JPT        	JPT.exon...3.sites.vcf.gz	1531         	
    JPT        	JPT.exon...3.sites.vcf.gz	2900   
    

Because the latter two samples have the same name, it is even difficult to remove one of them using command `vtools remove samples`. If you have to merge samples with the same names from different projects, it is recommended that you use command `vtools admin --rename_samples` to change names of samples before merging, and remove duplicated samples afterwards. 



If you have a large number of samples from different sources, it is a good idea to create subprojects for groups of samples. Merging subprojects will be faster than reading from source files again. However, due to the overhead of re-mapping all variants, pre-processing each sample by creating its own project usually does not help much. 

</details>

The children projects can also be snapshots, so if you have snapshots of a number of children projects, you can create a merged project using command 



    % vtools init test --children max_gt_data.tar poly_data.tar
    

The snapshots can also be an online snapshot so you can use an online snapshot to start your new project: 



    % vtools init test --children vt_simple