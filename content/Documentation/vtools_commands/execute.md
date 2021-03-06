+++
title = "execute"
description = ""
weight = 15
+++



## Execute variant tools pipelines



### 1. Usage

    % vtools execute -h

    usage: vtools execute [-h] [-i [INPUT_FILE [INPUT_FILE ...]]]
                          [-o [OUTPUT_FILE [OUTPUT_FILE ...]]] [-j JOBS]
                          [-d DELIMITER] [-v {0,1,2}]
                          PIPELINE/QUERY [PIPELINE/QUERY ...]

    Execute a pipeline that uses external commands to process input files, usually
    to align raw reads to a reference genome and call variants from aligned reads.
    The pipelines are controlled by pipeline description files. This command can
    also be used to execute arbitrary SQL query against the project database.
    Additional parameters will be passed to pipelines as pipeline parameters.

    positional arguments:
      PIPELINE/QUERY        Name of a pipeline configuration file with optional
                            names of pipelines to be executed if the configuration
                            file defines more than one pipelines. The
                            configuration file can be identified by path to a
                            .pipeline file (with or without extension), or one of
                            the online pipelines listed by command "vtools show
                            pipelines". If no input and output files are specified
                            (options --input and --output), values of this option
                            is treated as a SQL query that will be executed
                            against the project database, with project genotype
                            database attached as "genotype" and annotation
                            databases attached by their names.

    optional arguments:
      -h, --help            show this help message and exit
      -i [INPUT_FILE [INPUT_FILE ...]], --input [INPUT_FILE [INPUT_FILE ...]]
                            Input files to the pipeline, which will be passed to
                            the pipelines as pipeline variable \\({CMD_INPUT}.
      -o [OUTPUT_FILE [OUTPUT_FILE ...]], --output [OUTPUT_FILE [OUTPUT_FILE ...]]
                            Names of output files of the pipeline, which will be
                            passed to the pipelines as \\({CMD_OUTPUT}.
      -j JOBS, --jobs JOBS  Maximum number of concurrent jobs to execute.
      -d DELIMITER, --delimiter DELIMITER
                            Delimiter used to output results of a SQL query.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).




### 2. Details

#### 2.1 Execute variant tools pipelines

This command executes a pipeline that calls external commands to perform various operations. The general command line is



    % vtools execute pipeline_file [pipeline_name] [--input input_files] [--output output_files] [--options]


Here only the `pipeline_file` is required, which is a local or online pipeline file that defines one or more pipelines. `pipeline_name` can be ignored if only one pipeline is defined in this file. To get a list of available pipelines, you should run



    % vtools show pipelines


You can then use command



    % vtools show pipeline pipeline_file


to get details of the pipelines defined in this file.

Each pipeline accepts different `--input`, `--output` and optional parameters so please refer to the documentation for details of each pipeline.



#### 2.2 Execute SQL query

This command executes arbitrary SQL query and displays output to standard output or a file.

{{% notice warning %}}
Successful use of this command requires clear understanding of the structure of tables, which can be changed without notice from version to version.
{{% /notice%}}

Display name of samples



    % vtools execute select sample_name from sample -v2

    DEBUG: Loading annotation database testNSFP
    DEBUG: Executing SQL statement: "select sample_name from sample"
    NA06985
    NA06986
    NA06994
    NA07000
    ... ...


The following query needs to be quoted because of the existence of *



    % vtools execute 'SELECT * FROM sample' -v2

    DEBUG: Opening project esp.proj
    DEBUG: Loading annotation database refGene_exon
    DEBUG: Loading annotation database ../annoDB/dbSNP-hg19_132
    DEBUG: Analyze statement: "SELECT * FROM SAMPLE"
    DEBUG: 0	0	0	SCAN TABLE SAMPLE (~1000000 rows)
    1	1	NA06985
    2	1	NA06986
    3	1	NA06994
    4	1	NA07000
    5	1	NA07037
    6	1	NA07051
    7	1	NA07346
    8	1	NA07347

    ... ...