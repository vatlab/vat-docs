+++
title = "Help"
weight = 3
+++


## Usage of variant tools commands


### 1. Structure of commands

`vtools` uses a subcommand system that is similar to `svn`. For example, command 



    % vtools select variant 'sift_score < 0.05' -t table
    

consists of: 



1.  command `vtools` 
2.  subcommand `select` that specify *operation*, 
3.  positional arguments `variant` that specifies a *variant table* and `'sift_score < 0.05'` that specify *operant*, which in this case are the variant table to select from, and condition by which the variants are selected. 
4.  optional argument `-t table`. In contrast to positional arguments, optional arguments are used for options that may be optional or have common default values. 



### 2. Available subcommands 

`vtools` has a growing number of subcommands. To check the available subcommands, please use command `vtools -h`. 



    % vtools -h
    

    usage: vtools [-h] [--version]
    
                  {init,import,phenotype,show,liftover,use,update,select,exclude,compare,output,export,remove,associate,admin,execute}
                  ...
    
    A variant calling, processing, annotation and analysis tool for next-
    generation sequencing studies.
    
    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
    
    subcommands:
      {init,import,phenotype,show,liftover,use,update,select,exclude,compare,output,export,remove,associate,admin,execute}
        init                Create a new project, or a subproject from an existing
                            parent project, or merge several existing projects
                            into one
        import              Import variants and related sample genotype from files
                            in specified formats
        phenotype           Manage sample phenotypes
        show                Display content of a project
        liftover            Set alternative reference genome and update
                            alternative coordinates of all variant tables
        use                 Prepare (download or import if necessary) and use an
                            annotation database
        update              Add or update fields of existing variants and genotype
                            using information from specified existing fields,
                            sample genotype, or external files
        select              Output or save select variants that match specified
                            conditions
        exclude             Output or save variants after excluding variants that
                            match specified conditions
        compare             Compare two variant tables, count or output intersect
                            and difference to other tables
        output              Output variants in tab or comma separated format
        export              Export samples (variants and genotypes) in specified
                            format
        remove              Remove project or its contents such as variant tables,
                            fields, and annotation databases.
        associate           Test association between variants and phenotypes
        admin               Perform various administrative tasks including merge
                            and rename samples.
        execute             Execute a pipeline or a SQL query
    
    Use 'vtools cmd -h' for details about each command. Please contact Bo Peng
    (bpeng at mdanderson.org) if you have any question.
    



### 3. Logging and option `--verbosity` (`-v`)

variant tools, by default, outputs information lines (starts with INFO and WARNING) and progress bars during the execution of commands. Additionally the information lines and detailed debug information (starts with DEBUG) are written to a project log file ($name.log). If something goes wrong, you can check this file for details. One particular feature of this file is that it **saves date and time of each log message** so that you can measure the performance of operations if needed. 

The verbosity level of command line output can be controlled by option `--verbosity LEVEL`, where `LEVEL` can be 

*   ``: suppress all output except for warning and errors (no INFO or DEBUG) 
*   `1`: display/log progress information, including progress bars on screen output (no DEBUG) 
*   `2`: display/log progress and debug information. 

<details><summary>Examples:</summary> 



    % vtools init test -v2
    
    DEBUG: 
    DEBUG: init test -v2
    DEBUG: Using temporary directory /tmp/tmpg9b5gqd1/_tmp_525486
    INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    INFO: Please visit http://varianttools.sourceforge.net for more information.
    INFO: Creating a new project test
    



    % less test.log
    
    2018-06-07 17:54:27,174: DEBUG: 
    2018-06-07 17:54:27,174: DEBUG: init test -v2
    2018-06-07 17:54:27,175: DEBUG: Using temporary directory /tmp/tmpg9b5gqd1/_tmp_525486
    2018-06-07 17:54:27,175: INFO: variant tools 3.0.0dev : Copyright (c) 2011 - 2016 Bo Peng
    2018-06-07 17:54:27,175: INFO: Please visit http://varianttools.sourceforge.net for more information.
    2018-06-07 17:54:27,175: INFO: Creating a new project test
    

If, for example for a production pipeline you do not want any debug information in the log file, you can set a runtime option `logfile_verbosity` to control the level of verbosity in the log file. For example, 



    % vtools admin --set_runtime_option logfile_verbosity=0
    

will suppress any logfile output (except for warnings). </details>


{{% notice tip %}}
The verbosity level when the project is created is the default verbosity level of the project. That is to say, if you create the project using `` `vtools init test -v0 ``, the subsequent `vtools` command will have a default verbosity level of 0. 
{{%/notice%}}


### 4. Save output to files

Output from `vtools` can be saved to files via *standard output redirection*. The progress/warning/errors information will be displayed on screen while only the standard output will be written to files. 

<details><summary> Examples: direct output to files</summary> If you load a project from online and output its variants as follows: 



    % vtools init simple
    % vtools admin --load_snapshot vt_simple
    % vtools output variant chr pos ref alt -v2 > output.txt
    
    DEBUG: 
    DEBUG: output variant chr pos ref alt -v2
    DEBUG: Using temporary directory /tmp/tmpy265fgcj/_tmp_104712
    INFO: Upgrading variant tools project to version 2.7.20
    hg18.crr: 100% [==================================================] 770,113,155.0 15.5M/s in 00:00:49
    Verifying variants: 100% [=================================================] 1,611 32.4/s in 00:00:49
    INFO: 0 variants are updated

    

the output is written to file `output.txt` while debug information continues to be displayed and written to log file. 



    % head -n 5 output.txt
    

    1	4540	G	A
    1	5683	G	T
    1	5966	T	G
    1	6241	T	C
    1	9992	C	T
    

</details>



### 5. Conditions used in variant tools commands

One of the key features of the command line interface of variant tools is that its use of *conditions*. For example, `vtools select variant COND` finds variants in table `variant` that match specified `COND`, `vtools select --samples COND` finds variants that belong to samples that match certain `COND`, and `vtools init --parent DIR --genotypes COND` copies genotypes that match specific conditions from parent project `DIR` to a new project. 

Generally speaking, conditions are arbitrary SQL expressions that involves fields in the project. The syntax is described in [here][1], but generally speaking, you need to first determine *the fields that can be used*, *the type of fields*. Generally speaking, 



*   `vtools show fields` lists all variant info and annotation fields that can be used for selecting variants. 
*   `vtools show genotypes` lists all fields in the genotype tables that can be used to select genotypes. 
*   `vtools show samples` lists all fields in the sample table that can be used to select samples. 

You can then select records using expressions, 



*   For numeric fields (e.g. `pos`), you can use expressions such as `pos > 1000`, `pos = 12345`, and `pos BETWEEN 2000 AND 3000`. 
*   For character strings (e.g. `chr`, `ref`, and `alt`), you can use expressions such as `chr = '13'`, `length(ref) = 1`, `filename like 'INT%'`. Here `length` is a function to get the length of field `chr`. A complete list of usable functions is available [here][2]. 
*   Operator `IN` is sometimes very useful. E.g. `ref IN ('A', 'C')`. 
*   To test if there is a value at a field, use expression such as `chr IS NULL` or `chr IS NOT NULL`. 

Multiple conditions are allowed. For example `"ref='A'" "alt='C'"` means `"ref='A" AND alt='c'"`. If you need `OR` condition, you can write that explicitly, e.g. `"ref='A" OR alt='c'"`. 

For example, 



*   Condition `dbSNP.chr IS NOT NULLL` selects variants that are in dbSNP database. This is because all records in `dbSNP` has value at field `chr`. 
*   `vtools select variant --samples "filename LIKE 'CEU%'"` get variants that belong to all samples with filename starting at `CEU`. 
*   Condition `"((ref='A' AND alt='G') OR (ref='G' AND alt='A') OR (ref='C' AND alt='T') OR (ref='T' AND alt='C'))"` matches all transition mutations. 
*   Condition `"ref=<small>'"` select all insertions, and `"alt='</small>"` select all deletions, and `"ref != <small>'" "alt != '</small>" "length(ref)=1" "length(alt)=1"` selects all SNVs. 
*   `vtools remove genotypes "DP < 10"` removes all genotypes with depth less than 10. 
*   `vtools export ... --samples 1` export genotypes at all samples because condition `1` means `TRUE` for all samples.

 [1]: http://www.sqlite.org/lang_expr.html
 [2]: http://www.sqlite.org/lang_corefunc.html