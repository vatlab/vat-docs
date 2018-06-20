+++
title = "admin"
description = ""
weight = 16
+++



## Miscellaneous administrative procedures 




### 1. Usage

    % vtools admin -h
    
    usage: vtools admin [-h] [--update_resource [TYPE]] [--mirror_repository dest]
                        [--merge_samples] [--rename_samples COND [COND ...]]
                        [--rename_table NAME NEW_NAME]
                        [--describe_table TABLE NEW_DESCRIPTION]
                        [--validate_build] [--validate_sex]
                        [--save_snapshot NAME MESSAGE]
                        [--extra_files [FILE [FILE ...]]] [--load_snapshot NAME]
                        [--set_runtime_option OPTION [OPTION ...]]
                        [--reset_runtime_option OPT]
                        [--fasta2crr FASTA [FASTA ...]] [-v {0,1,2,3}]
    
    Optimize or modify projects. Currently supports merging and rename of samples
    
    optional arguments:
      -h, --help            show this help message and exit
      -v {0,1,2,3}, --verbosity {0,1,2,3}
                            Output error and warning (0), info (1), debug (2) and
                            trace (3) information to standard output (default to
                            1).
    
    Download or update resources:
      --update_resource [TYPE]
                            Download resources of specified type, which can be
                            'current' (latest version of all resources), 'all'
                            (all resources including obsolete databases),
                            'existing' (only update resources that exist locally),
                            'hg18' or 'hg19' (all resources for reference genome
                            hg18 or hg19), 'annotation' (all current annotation
                            databases), 'format' (all formats), and 'snapshot'
                            (all online snapshots). Identical resources that are
                            available locally (under ~/.variant_tools or runtime
                            option \\(local_resource) are ignored. Note that option
                            'all' will download all versions of annotation
                            databases which can be slow and take a lot of disk
                            spaces.
      --mirror_repository dest
                            Mirror the main variant tools repository to a local
                            directory. This command will check files under dest,
                            download all missing or outdated files. Existing files
                            that do not belong to the repository will not be
                            removed.
    
    Merge samples:
      --merge_samples       Merge samples with the same sample names by combining
                            genotypes belonging to these samples. Phenotypes
                            related to individual samples will be merged.
    
    Rename samples:
      --rename_samples COND [COND ...]
                            This argument takes a condition by which samples are
                            selected, followed by either a new sample name (assign
                            a new name to selected samples) or an OLDNAME NEWNAME
                            pair of patterns for which the first instance of
                            OLDNAME in sample names will be replaced by NEWNAME.
    
    Rename/describe tables:
      --rename_table NAME NEW_NAME
                            Change table NAME to a NEW_NAME.
      --describe_table TABLE NEW_DESCRIPTION
                            Update description for TABLE with a NEW_DESCRIPTION.
    
    Validate reference genome:
      --validate_build      Validate the build of project's reference genome by
                            checking if the reference alleles of variants agree
                            with the reference genome sequence. A reference genome
                            will be automatically downloaded if it does not exist
                            in the local resource directory.
    
    Validate reported sex:
      --validate_sex        Validate the sex of samples by checking the genotypes
                            of samples on sex chromosomes (excluding pseudo-
                            autosomal regions). Sex of samples are determined by a
                            phenotype named sex or gender with values 1/2, M/F or
                            Male/Female. Inconsistency will be reported if, for
                            example, a female sample has genotypes on chromosome
                            Y.
    
    Save and load snapshots:
      --save_snapshot NAME MESSAGE
                            Create a snapshot of the current project with NAME,
                            which could be re-loaded using command 'vtools admin
                            --load_snapshot'. A filename with extension .tar, .tgz
                            or .tar.gz can be used to save the snapshot to a
                            specific directory with compression but such snapshots
                            are not listed by command 'vtools show snapshots'.
      --extra_files [FILE [FILE ...]]
                            Additional files that will be saved along with the
                            project and genotype databases. This could include
                            customized format files, project-specific annotations,
                            and results. Files outside of the current project
                            directory are not allowed due to security
                            considerations.
      --load_snapshot NAME  Revert the current project to specified snapshot. All
                            changes since the that snapshot will be lost. The NAME
                            should be one of the project snapshots or online
                            snapshots listed by command 'vtools show snapshots',
                            or name of a local snapshot file (with extension .tar,
                            .tgz or .tar.gz).
    
    Set values for some various internal options.:
      --set_runtime_option OPTION [OPTION ...]
                            Set value to internal options such as the batch size
                            for database options. The default values of these
                            options were chosen to fit most usage patterns but
                            tweaking them might provide better performance under
                            certain circumstances. Please use command "vtools show
                            runtime_options" to list all currently supported
                            runtime options.
      --reset_runtime_option OPT
                            Reset value to a runtime option to its default value.
    
    Misc utilities:
      --fasta2crr FASTA [FASTA ...]
                            Convert fasta files to a crr file (a binary format for
                            faster access) that can be used by variant tools. This
                            is only needed if you are working with a reference
                            genome that is not supported by variant tools. This
                            parameter accepts a list of fastq files (URLs and .gz
                            format are acceptable) followed by the name of the
                            .crr file. The .crr file should be put under the
                            project directory or the local resource directory
                            (under directory reference) to be usable by variant
                            tools.
    



### 2. Details

The `vtools admin` command performs various adminstrative functions for a variant tools project. 



#### 2.1 Download or update local resources (`--update_resource`)

Resources, such as annotation databases, format specification, and reference genomes are downloaded automatically when they are used. However, if you prefer having all resources downloaded before using variant tools (so that you do not have to wait each time when a source is needed), you can use option `--update_resource` to download them in batch. The resources will be saved to your home directory under `~/.variant_tools` unless you change this location using runtime option `@local_resource`. 

This command by default download all current resources (e.g. most recent versions of annotation databases for latest version of reference genome). You can however using option `hg18` to download resources for another reference genome, or option `existing` to update only resources that exists locally. 

<details><summary> Examples: Download resources</summary> The following command checks files under the local resource directory, ignored 112 existing files and downloaded a new version of EVS annotation database. 



    % vtools init temp   # needed if there is no project in the current directory
    % vtools admin --update_resource
    
    Scanning 112 local files: 100% [========================] 18,537,133,615 407.1M/s in 00:00:45
    INFO: 2 files need to be downloaded or updated
    1/2 annoDB/evs-6500.DB.gz: 100% [==========================] 109,502,699.0 1.4M/s in 00:01:17
    2/2 annoDB/evs-6500.ann: 100% [=================================] 7,984.0 40.2K/s in 00:00:00
    

</details>



#### 2.2 Rename samples (`--rename_samples`)

Although samples in *variant tools* can be identified by items other than sample names (e.g. filename such as `filename = "V1.vcf"`), or any of the phenotypes such as `aff=1`), sample name is the important identifier for samples and are used ubiquitously for reports. Sample names are assigned during `vtools import`, using either names specified in input files, or names specified by parameter `--sample_names`. If a sample name is missing or mis-specified, you can use the `vtools admin --rename_samples` to rename samples. 

Given a condition (`COND`) that selects one or more samples, this command accepts two types of inputs: 



    % vtools admin --rename_samples COND name
    

and 



    % vtools admin --rename_samples COND name1 name2
    

In the first option, all selected samples are renamed to `name`. In the second option, the first instance of `name1` in sample names will be replaced by `name2`. The former is similar to linux command `move src dest` and the latter is similar to command `rename pat1 pat2 files`. 

<details><summary> Examples: Rename samples</summary> Let us first get some data and a few samples 



    % vtools init admin -f
    % vtools admin --load_snapshot vt_testData
    % vtools import V*_hg38.vcf --build hg38
   
    

There are four samples 



    % vtools show samples
    
    sample_name	filename
    SAMP1       V1_hg38.vcf
    SAMP2       V2_hg38.vcf
    SAMP3       V3_hg38.vcf
 
    

The first three samples share the same name, which can lead to erroneous results during analysis (e.g. `vtools associate` will treat them as genotypes from the same sample). We can rename them using commands 

    % vtools admin --rename_samples 'filename="V1_hg38.vcf"' V1
    % vtools admin --rename_samples 'filename="V2_hg38.vcf"' V2
    % vtools admin --rename_samples 'filename="V3_hg38.vcf"' V3
    
    INFO: 1 samples with names SAMP1 are renamed to V1
    INFO: 1 samples with names SAMP1 are renamed to V2
    INFO: 1 samples with names SAMP1 are renamed to V3
    

The samples now have different names: 

    % vtools show samples
    
    sample_name	filename
    V1          V1_hg38.vcf
    V2          V2_hg38.vcf
    V3          V3_hg38.vcf
    
    

If you would like to change names of multiple samples according to a pattern, you can use the second form of the command. For example, the following command changes samples `V1`, `V2`, and `V3` to `SAMP1`, `SAMP2`, and `SAMP3`: 


    % vtools admin --rename_samples 1 V SAMP

    INFO: Rename 1 sample with name V1 to SAMP1
    INFO: Rename 1 sample with name V2 to SAMP2
    INFO: Rename 1 sample with name V3 to SAMP3
    



    % vtools show samples
    
    sample_name	filename
    SAMP1       V1_hg38.vcf
    SAMP2       V2_hg38.vcf
    SAMP3       V3_hg38.vcf
    

The command might look strange to you, but the first `1` is a condition to select all samples (`true`), the second and third parameter changes the first incidence of `V` to `SAMP` for all matched sample names. 

</details>



If you would like to prefix sample names by a string (e.g. `V1` -> `SAMP_V1`), you can use commands such as `vtools admin --rename_samples 1 '' SAMP_`, because an empty string matches an empty string before the fist character of the sample name. 



#### 2.3 (This function is only supported when STOREMODE is set to sqlite.) Merge samples by sample's name (`--merge_samples`)


Command `vtools admin --merge_samples` merges samples with the same names to a single sample. This command is used when genotypes of a sample are stored in several files (e.g. chromosome by chromosome, or seprate files for SNPs and Indels resulting from the Illumina pipeline) and are imported as separate samples. These samples should be merged together because otherwise number of samples in the variant tools project will not match number of physical samples, and lead to erronous results during analysis. Because this command merge samples by names, samples to be merged should be renamed to have the same names if needed. 

<details><summary> Examples: Merge samples with same names</summary> All our samples have different names now so we have to rename one of them in order to merge it with another sample, 

    % vtools init admin -f
    % vtools admin --load_snapshot vt_testData
    % vtools import V1.vcf --build hg18
    % vtools import V2.vcf 
    % vtools import V3.vcf 
    % vtools import CASAVA18_SNP.txt --format CASAVA18_snps 
    % vtools admin --rename_samples 'sample_name = "max_gt"' SAMP3
    
    INFO: 1 samples with names max_gt are renamed to SAMP3
    

Now we have four samples with the last two sharing the same name 

    % vtools show genotypes
    
    sample_name	filename	num_genotypes	sample_genotype_fields
    SAMP1	V1.vcf	989	GT
    SAMP2	V2.vcf	990	GT
    SAMP3	V3.vcf	988	GT
    SAMP3	CASAVA18_SNP.txt	21	GT,Q_max_gt
    

We can then merge the last two samples, 



    % vtools admin --merge_samples
    
    INFO: 2 samples that share identical names will be merged to 1 samples
    Merging samples: 100% [=========================================] 2 235.8/s in 00:00:00
    

The genotypes are 

    % vtools show genotypes
    
    sample_name	filename	num_genotypes	sample_genotype_fields
    SAMP1	V1.vcf	989	GT
    SAMP2	V2.vcf	990	GT
    SAMP3	CASAVA18_SNP.txt,V3.vcf	1009	GT,Q_max_gt
    

Note the change of filename field of the last sample. In addition, the orignal SAMP3 sample does not have genotype info field `Q_max_gt`. The new `SAMP3` has this field but the 988 genotypes from the orignal sample have `NULL` values for this field. </details>

Samples to be merged should not share any genotype (variant) because it is otherwise difficult to determine what genotypes to use for the merged sample. 

<details><summary> Examples: Fail to merge samples with shared genotypes</summary> If we rename sample `SAMP2` to `SAMP1`, 

    % vtools admin --rename_samples 1 SAMP2 SAMP1
    
     INFO: Rename 1 sample with name SAMP2 to SAMP1
    

and try to merge `SAMP2` to `SAMP1`, we will get an error message because `SAMP1` and `SAMP2` share many of the variants. 

    % vtools admin --merge_samples
    
    INFO: 2 samples that share identical names will be merged to 1 samples
    Merging samples: 100% [=========================================] 2 197.5/s in 00:00:00
    ERROR: Failed to merge samples with name SAMP1 because there are 1979 genotypes for 1341 unique variants.
    

Note that we use `vtools admin --rename_samples 1 SAMP2 SAMP1` to rename sample using the second option of the `vtools admin --rename_samples` command. It is easier to use than `vtools admin --rename_samples 'sample_name = "SAMP2"' SAMP1`, but has the risk of renaming other tables containing `SAMP2` (e.g. `SAMP21`) and should be used with caution. </details>



#### 2.4 Rename and modify descriptions of variant tables (`--rename_table` and `--describe_table`)

A lot of variant tables can be generated during the analysis and it can be difficult to remember what types of variants are stored in each table. *variant tools* allows you to use arbitrary characters in table names and describe tables with messages when they are created, rename tables and modify their descriptions after they are created. The latter two operations are performed using commands `vtools admin --rename-table OLDNAME NEWNAME` and `vtools admin --describe_table NAME NEW_DESCRIPTION`. The usages of these two commands are straightforward. 

<details><summary> Examples: Change name and comment of variant tables</summary> Let us get a sample project and create a few variant tables 

    vtools init testProj
    vtools import V*_hg38.vcf --build hg38
    vtools select variant -t 'all variant'
    vtools select variant --samples 'filename = "V1_hg38.vcf"' -t fromV1 'variants from v1'
    

The project has three tables, 



    % vtools show tables
    
    table          #variants     date message
    all variant        2,051    May29
    fromV1             1,269    May29 variants from v1
    variant            2,051    May29 Master variant table
    

You can rename the `all variant` to `all_variant` 

    % vtools admin --rename_table 'all variant' all_variant
    
    INFO: Table all variant is renamed to all_variant
    

and give it a short description, 

    % vtools admin --describe_table 'all_variant' 'A replicate of the master variant table'

    INFO: Description of table all_variant is updated
    

The table now has a new name and a description, but its creation date and command are not changed. 

    % vtools show table all_variant  

    Name:                   all_variant
    Description:            A replicate of the master variant table
    Creation date:          May29
    Command:                select variant -t "all variant"
    Fields:                 variant_id, chr
    Number of variants:     2051
    

</details>

 

#### 2.5 Validate build of project's reference genome (`--validate_build`)

Sometimes when you get a bunch of data, look everywhere in the folder and emails, and cannot find any information regarding the reference genome used to call the variants. In this case, you can import your data using the most likely build of reference genome (`hg19`), and use command `vtools admin --validate_build` to check if you have made the correct assumption. 

<details><summary> Examples: Validate the reference genome used in a project</summary> Let us create a project and get some test data 

    % vtools init test
    % vtools admin --load_snapshot vt_testData
    
    Downloading snapshot vt_testData.tar.gz from online
    INFO: Snapshot vt_testData has been loaded
    

We would like to import data from `V1.vcf`, `V2.vcf`, and `V3.vcf` but do not know the correct reference genome to use, so we use `hg19` 

    % vtools import V*.vcf --build hg19
    
    INFO: Importing variants from V1.vcf (1/3)
    V1.vcf: 100% [======================================] 1,000 19.3K/s in 00:00:00
    INFO: 989 new variants (989 SNVs) from 1,000 lines are imported.
    INFO: Importing variants from V2.vcf (2/3)
    V2.vcf: 100% [======================================] 1,000 27.6K/s in 00:00:00
    INFO: 352 new variants (352 SNVs) from 995 lines are imported.
    INFO: Importing variants from V3.vcf (3/3)
    V3.vcf: 100% [======================================] 1,000 27.8K/s in 00:00:00
    INFO: 270 new variants (270 SNVs) from 1,000 lines are imported.
    Importing genotypes: 100% [==========================] 2,995 1.5K/s in 00:00:02
    Copying genotype: 100% [=================================] 3 8.1K/s in 00:00:00
    INFO: 1,611 new variants (1,611 SNVs) from 2,995 lines (3 samples) are imported.
    

Let us see if these 1,611 variants have the correct reference alleles at the specified locations of the reference genome, 



    % vtools admin --validate_build

    Validate reference alleles: 100% [=============] 1,611/1,238 14.8K/s in 00:00:00
    INFO: 1611 non-insertion variants are checked. 1238 mismatch variants found.
    

As you can see, most of the variants do not have correct reference genomes. Now if we import the data using `hg18`, the validation process completes successfully and we are confident that we are using the correct reference genome this time. 



    % vtools init test -f
    % vtools import V*.vcf --build hg18
    % vtools admin --validate_build 

    Validate reference alleles: 100% [==================] 1,611 60.1K/s in 00:00:00
    INFO: 1611 non-insertion variants are checked. 0 mismatch variants found.
    

</details>



#### 2.6 Validate sex of samples (`--validate_sex`)

If your data contain genotypes on sex chromosomes and have sex information, you can use command `vtools admin --validate_sex` to check if the reported sex information match sample genotypes. To use this command, your project should have a phenotype with name `sex` or `gender` that contains sex of samples (coded in `1/2`, `M/F`, or `Male/Female`, missing values are not allowed). This command goes through all samples, and identify inconsistencies by 



*   For males, check if there are homozygote alternative alleles on non-pseudo-autosomal regions of chromosome X, 
*   For females, check if there are any genotype on chromosome Y. 


{{% notice warning %}}
Variant calling pipelines are unlikely to call variants on sex chromosomes correctly if the variants are called blindly (without knowing chromosome name and sex of samples), so it is common that your data appear to have genotypes that are inconsistent with the sex of samples. 
{{% /notice %}}
 

#### 2.7 Save and load snapshots of a project (`--save_snapshot` and `--load_snapshot`)

You can save snapshots of the current project and revert to them later. This allows you to recover a project when it is damaged by incorrect operations or system failure, and more importantly, allows you to explore different processing pipelines with saved baseline stages. A snapshot is also a good way to carry a project around. 

There are several types of snapshots: 



*   Online snapshots that can be downloaded automatically using command `vtools admin --load_snapshot`. The names of these snapshots starts with `vt_`. 
*   Project-specific snapshots that are saved in the project's cache directory. These snapshots are saved and loaded by snapshot name and are listed by command `vtools show snapshots`. 
*   Local snapshots that are saved in arbitrarily specified directory, with extension `.tar` or `.tar.gz` (compressed). These snapshots are not listed by command `vtools show snapshots`. 

You should in general use project-specific snapshots, unless you plan to carry the snapshots around. In that case you should use the compressed snapshots although it can take some time to compress a large project. 


{{% notice warning %}}
All changes to the current project will be lost if you revert to a previous snapshot. 
{{% /notice %}}

<details><summary> Examples: Save snapshots of a project </summary> By default, a snapshot can be created with a name, and saved without compression in the cache directory of the current project: 



    % vtools admin --save_snapshot stage1 "after importing date"

    INFO: Snapshot stage1 has been saved
    

A message is required to describe each snapshot so that you can know later on what this snapshot is about: 



    % vtools show snapshots 

    stage1                  after importing date  (122.0KB, created: Jul15
                            14:35:14)
    vt_qc                   snapshot for QC tutorial, exome data of 1000 genomes
                            project with simulated GD and GQ scores (2.0GB, online
                            snapshot)
    vt_ExomeAssociation     Data with ~26k variants from chr1 and 2, ~3k samples,
                            3 phenotypes, ready for association testing. (446.0MB,
                            online snapshot)
    vt_quickStartGuide      A simple project with variants from the CEU and JPT
                            pilot data of the 1000 genome project (148.0KB, online
                            snapshot)
    vt_illuminaTestData     Test data with 1M paired reads (49.0MB, online
                            snapshot)
    vt_simple               A simple project with variants imported from three vcf
                            files (41.0KB, online snapshot)
    vt_testData             An empty project with some test datasets (63.0KB,
                            online snapshot)

If for some reason you would like to revert to a particular snapshot, you can do 



    % vtools admin --load_snapshot stage1

    INFO: Snapshot stage1 has been loaded
    

If the disk that holds your project does not have enough free diskspace to hold these snapshots, you can save snapshots to another disk using filenames with extension `.tar`, `.tgz`, or `.tar.gz`. In the latter two cases, the snapshot will be compressed. 



    % vtools admin --save_snapshot stage1.tgz "after importing phenotypes"
    
    INFO: Snapshot stage1.tgz has been saved
    

This snapshot will not be displayed by command `vtools show snapshots` because it is managed by the current project 



    % vtools show snapshots -l 2
    
    stage1                  after importing date  (122.0KB, created: Jul15
                            14:35:14)
    vt_qc                   snapshot for QC tutorial, exome data of 1000 genomes
                            project with simulated GD and GQ scores (2.0GB, online
                            snapshot)
    

but it can be viewed using command `vtools show snapshot` 



    % vtools show snapshot stage1.tgz  

    Name:                   stage1.tgz
    Source:                 local
    Size:                   40273 (40.0KB)
    Creation date:          Jul15 14:36:37
    Description:            after importing phenotypes
    

You can revert to this snapshot using command 



    % vtools admin --load_snapshot stage1.tgz   

    INFO: Snapshot stage1.tgz has been loaded
    

A snapshot only contains the project, and the genotype database. It does not save log file, annotation databases, and various output and results (e.g. database created by command `vtools associate`. You should use `--extra_files` option to include other files in a snapshot. 



    % vtools admin --save_snapshot stage1.tgz 'a snapshot with extra files' \
         --extra_files test.log cache/*
    



Directories cannot be directly added to snapshots, since recursively adding files under a directory may lead to unwanted behaviors (e.g., when symbolic links are involved). However you may use wildcard names (`cache/*`) to include files in a directory. 

</details>



#### 2.8 Set and reset runtime options (`--set_runtime_option` and `--reset_runtime_option`)

Setting runtime options, for example, 

    % vtools admin --set_runtime_option 'logfile_verbosity=0'
    

can stop the project from writing debug information to a file. 

A list of runtime options and their descriptions could be obtained by 



    % vtools show runtime_options
    
    associate_num_of_readers None (default)
                            Use specified number of processes to read genotype
                            data for association tests. The default value is the
                            minimum of value of option --jobs and 8. Note that a
                            large number of reading processes might lead to
                            degraded performance or errors due to disk access
                            limits.
    association_timeout     None (default)
                            Cancel associate test and return special values when a
                            test lasts more than specified time (in seconds). The
                            default value of this option is None, which stands for
                            no time limit.
    check_update            True (default)
                            Automatically check update of variant tools and
                            resources.
    import_num_of_readers   2 (default)
                            variant tools by default uses two processes to read
                            from input files during multi-process importing
                            (--jobs > 0). You can want to set it to zero if a
                            single process provides better performance or reduces
                            disk traffic.
    local_resource          ~/.variant_tools (default)
                            A directory to store variant tools related resources
                            such as reference genomes and annotation database.
                            Files under this directory is usually downloaded
                            automatically upon use, but can also be synchronized
                            directly from
                            http://vtools.houstonbioinformatics.org/.
    logfile_verbosity       2 (default)
                            Verbosity level of the log file, can be 0 for warning
                            and error only, 1 for general information, or 2 for
                            general and debug information.
    search_path             .;http://vtools.houstonbioinformatics.org/ (default)
                            A ;-separated list of directories and URLs that are
                            used to locate annotation database (.ann, .DB), file
                            format (.fmt) and other files. Reset this option
                            allows alternative local or online storage of such
                            files. variant tools will append trailing directories
                            such as annoDB for certain types of data so only root
                            directories should be listed in this search path.
    sqlite_pragma            (default)
                            pragmas for sqlite database that can be used to
                            optimize the performance of database operations.
    temp_dir                None (default)
                            Use the specified temporary directory to store
                            temporary files to improve performance (use separate
                            disks for project and temp files), or avoid problems
                            due to insufficient disk space.
    treat_missing_as_wildtype False (default)
                            Treat missing values as wildtype alleles for
                            association tests. This option is used when samples
                            are called individuals or in batch so genotypes for
                            some samples are ignored and treated as missing if
                            they consist of all wildtype alleles. This option
                            should be used with caution because it convert real
                            missing genotypes and genotypes removed due to, for
                            example low quality score, to wildtype genotypes.
    verbosity               1 (default)
                            Default verbosity level (to the standard output) of
                            the project. This option can be set during vtools init
                            where the verbosity level set by option --verbosity
                            will be set as the project default.
    

In particular, 



*   **`temp_dir`**: Project temporary directory. By default a random temporary directory will be created each time when a project is opened. If 
    *   the partition that hosts the temporary directory is not large enough, 
    *   the partition is slow, 
    *   or if you would like to move the temporary directory to a separate physical disk to improve I/O performance, 

you can set a different location for this directory. Note that this directory will be removed after the project is closed. 



*   **`sqlite_pragma`**: Sqlite pragma can have a significant impact on the performance of sqlite database operations. Variant tools strives to provide optimal pragma to achieve good performance (for example, `synchronous=OFF` to disable disk write check), but you can define your own set of pragmas that fit your environment. For example, if your system has plenty of RAM, you can use 



    % vtools admin --set_runtime_option 'sqlite_pragma=synchronous=OFF,journal_mode=MEMORY'
    



to use in-memory journal. 


{{% notice warning %}}
The MEMORY journaling mode saves disk I/O but at the expense of database safety and integrity. If the application using SQLite crashes in the middle of a transaction when the MEMORY journaling mode is set, then the database file will very likely go corrupt [*][1].* You can enable it for data import operations such as `vtools import` and `vtools update --from_file` and set it to default (journal\_mode=DELETE) afterwards. 
{{% /notice %}}


The pragmas are usually applied to all databases (e.g. project, genotype and annotation databases) but you can limit the pragma to certain databases if you prefix it with database name (e.g. `_geno.snchronous=OFF`). This, however, needs an understanding of the databases involved in a command, and is generally not recommended. Please read about supported pragma statements [here][2]. 



*   **`treat_missing_as_wildtype`**: If your sample variants are called sample by sample or in batch, some variants might exists for certain samples but not for others, because they have all wildtype alleles for some samples and are not recorded. For example, if you are analyzing your samples with affected individuals, and use the 1000 genomes data as controls, novel variants in your data might not have corresponding genotypes in the 1000 genomes data, leading to complete missing genotypes for controls. The variants will likely to be discarded due to excessive missing data and will not be selected. 



In this case, it is advised that you set runtime option `treat_missing_as_wildtype` to 1 before association analysis so that all missing and not-imported gentoypes are considered as wildtype alleles. This is dangerous because it might introduce a large number of non-existing (wildtype) alleles, and effectively change all NA genotypes to wildtype alleles from your input data. The results from such analysis should therefore be compared with results with this optoin turned off, and be examined closely for validity. If you would like to reset a runtime option, simply run 



    % vtools admin --reset_runtime_option sqlite_pragma
    



to reset an option to its default values. 



#### 2.9 Convert fasta files of non-human reference genomes to `.crr` files

Variant tools supports human reference genomes natively. It can also work with other reference genomes in `.crr` format, which is a binary format that allows efficient random access to the reference genome. If you have a reference genome in fasta format, you will need to convert it to `.crr` format using command `vtools admin --fasta2crr`. 

<details><summary> Examples: Create a .crr file for a mouse genome</summary> 



    % vtools admin --fasta2crr \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr1.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr2.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr3.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr4.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr5.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr6.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr7.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr8.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr9.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr10.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr11.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr12.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr13.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr14.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr15.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr16.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr17.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr18.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chrX.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chrY.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chrM.fa.gz \
    	 mm10.crr
    

</details>

 [1]: http://www.sqlite.org/pragma.html#pragma_journal_mode
 [2]: http://www.sqlite.org/pragma.html