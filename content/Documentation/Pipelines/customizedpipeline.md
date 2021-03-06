
+++
title = "Customized"
weight = 1
+++



## Specification of a variant tools pipeline


<font color = "red">
This page describes the new pipeline format (version 1.1 and later). Please refer to [Format1_0][1] if you are editing a pipeline specification file for variant tools 2.7 and earlier.. 
</font>


### 1. Introduction

*Variant Tools* uses pipeline specification files to define pipelines. A pipeline specification file can define multiple pipelines. It can be stored locally or online in the variant tools repository (or a local repository maintained by your system adminstrator). You can use command 



    % vtools show pipelines
    

to get a list of all publicly available pipelines, and 



    % vtools show pipeline SPECFILE
    

to get the details of pipelines defined in `SPECFILE`. The output of this command consists of description of the `SPECFILE`, all pipelines in it, steps of each pipeline, and options of the pipelines. 

A pipeline can be executed by command 



    % vtools execute SPECFILE PIPELINE [--input XXX] [--output XXX] [OPTIONS]
    

where `SPECFILE` can be a local `.pipeline` file, or name of an online pipeline specification file, `PIPELINE` is the name of the pipeline defined in SPECFILE. The command line can be simplified to 



    % vtools execute SPECFILE [-i XXX] [-o XXX] [OPTIONS]
    

if the spec file only defines one pipeline. 

The format of pipeline spec files is similar to the `.ini` files of the good old days. It is not as fashionable as `XML` based configuration files but it is easier to read and write. The most simple pipeline specification file is a collection of commands and scripts as follows 



    ###fileformat=PIPELINE1.1
    # Copyright, change log etc
    
    # This is a description of all pipelines defined in this spec file
    
    [1]
    RunCommand(cmd='a shell command')
    
    [2]
    ExecuteRScript(script='''
    library(mylib)
    a <- read.table("${var2}.txt")
    
    ''')
    
    

although a spec file that defines multiple pipelines, accepts multiple command line parameters and makes uses of pipeline variables looks as follows: 

>>output< 

    ###fileformat=PIPELINE1.1
    # Copyright, change log etc
    
    # This is a description of all pipelines defined in this spec file
    #
    
    p1_description:
        The p1 pipeline performs ...
    
    p2_description:
        The p1 pipeline performs ...
    
    # pipeline variables
    VAR=VALUE
    VAR1=VALUE1
    
    [DEFAULT]
    arg1=
        This argument does this
    
    arg2=1.0
        This argument has a default value 1.0
    
    [*_10: passthrough]
    # Check the version of variant tools
    CheckVariantToolVersion('2.7')
    
    [p1_20]
    # Execute a single command
    input:
        \\({cmd_input}
    RunCommand(cmd='''
       a very long command > \\({var1} ''',
       output='${var1}')
    
    [p1_200]
    # Execute a R script
    ExecuteRScript(script='''
    library(mylib)
    a <- read.table("${var2}.txt"
    
    ''',
       output='${var2[:-3]}.pdf')
    
    [p2_20]
    # Execute a R script for pipeline p2
    ExecuteRScript(script='''
    library(mylib)
    a <- read.table("${var2}.txt"
    
    ''',
       output='${var2[:-3]}.pdf')
    
    

This small example demonstrates almost all the features of pipeline specification files. Before we go to the details of each section, here are some basic rules: 



{{% notice info %}}
A spec file should start with line 

    ##fileformat=PIPELINE1.1
{{% /notice %}}    


{{% notice info %}}
 Lines starts with `#` are comments. Some comments are significant and will be displayed in the output of `vtools show pipeline`. 
 {{% /notice %}}

{{% notice info %}}
A pipeline spec file consists of a starting description section with no header, an optional `[DEFAULT]` section, and multiple pipeline step sections.
{{% /notice %}}

{{% notice info %}}
Values of an item can be expanded into multiple lines, e.g. 

    name=this is a long text
      that continues to the second line
      or the third
{{% /notice %}}
    


{{% notice info%}}
Consequently, **you can expand your comments or commands into several lines as long as you do not start from the first column**. An exception to this rule is when a large piece of text is quoted in triple quotes such as 

    ExecuteRScript('''
    data <- read.table("${input}")
    data <- data[1,]
    ''')

Note that `''' ... '''` literals are automatically translated to `r''' ... '''` so escape characters are not translated. Use `""" ... """` string literals if you would like to allow escape characters. 
{{% /notice %}}   

{{% notice info%}}
You can use either `KEY = VALUE` or `KEY : VALUE`. The convention is to use `KEY = VALUE` for variable assignment and `KEY : VALUE` for all other. 
{{% /notice %}}  

{{% notice info%}}
Pattern `${ }` are specially handled as pipeline variables. `;` and `%` are not special characters as in the original specification format. 
{{% /notice %}}  




### 2. Top Section 

A pipeline specification file should start with a description section (no header is needed). This section should have the following keys: 



*   `description`: Summary of pipelines defined in this SPECFILE, which should include format and type of input data (raw reads? bam file? paired end?), external commands that are used, a short description of steps involved, and reference to external documentation if available. If no description is provided, the second block of comments will be treated as overall pipeline description in the output of `vtools show pipeline`. For example, 



    ##fileformat=PIPELINE1.1
    # Copyright line
    
    # This is the overall pipeline description
    


*   `PIPELINE_description`: (Optional) Description of pipeline `PIPELINE`. `PIPELINE` has to be a valid pipeline defined in this file (with sections `PIPELINE_XX`). 


{{% notice tip %}}
If you have long descriptions (highly recommended!), you can break it into several paragraphs by adding HTML tags `<p>` or `<br>`. Tag `<p>` starts a new paragraph (two newlines) and tag `<br>` starts a new line (one newline). You can also use tags `<ul>` and `<li>` to generate itemized lists. For example, 

    This pipeline uses <ul>
      <li>tophat 2.0.13 
      <li>bowtie 1.1.1
      <li>samtools 0.1.19
      <li>picard 1.82
      </ul>
    
will produce output 

    This pipeline uses
      * tophat 2.0.13
      * bowtie 1.1.1
      * samtools 0.1.19
      * picard 1.82
    
when the description is outputted using command `vtools show pipeline`. 
{{% /notice %}}


*   `NAME=VAL` (optional): Pipeline variables. This is usually a good place to define constant values that will be used by pipeline steps. For example: 
    
        RESOURCE_DIR=${local_resource}/pipeline_resource/name_of_pipeline
        



where \\({local_resource} is another pipeline variable that has value of project runtime option `$local_resource`. We will talk about pipeline variables in details later. 



### 3. Section `[DEFAULT]` (command line options)

The `DEFAULT` section defines parameters that can be changed using command line arguments. For example, in the following `.pipeline` file (partial) 



    [DEFAULT]
    opt_java=-Xmx4g
        Parameter passed to the java command, default to -Xmx4g to use a maximum of 4g heap space.
    
    [align_5]
    RunCommand(cmd="java \\({opt_java} SortSam ...")
    

The value of `opt_java` will be used to replace all instances of `${opt_java}` in the pipeline configuration file (or its derivatives, more on this later). The parameter has a default value `-Xmx4g` and a help message, which will be displayed when you view the details of this parameter. 



    % vtools show pipeline my_pipeline
    

you will see at the end of the output the following description: 



    Pipeline parameters:
      opt_java     Parameter passed to the java command, default to -Xmx4g to use a maximum of 4g heap space.
                   (default: -Xmx4g)
    

That is to say, you can pass an alternative value of `opt_java` to this format using command-line options such as `--opt_java -Xmx32g` to change the value of this option. 


{{% notice tip%}}
If you have a large number of parameters, you can save them to an external file, one item per line, and load them by prefixing filename with a `"@"` symbol. For example, if you have a file `param.cfg` with content 



    --bwa
    /path/to/bwa
    --samtools
    /path/to/samtools
    

you can load parameters `--bwa /path/to/bwa --samtools /path/to/samtools` using `"@param.cfg"` from command line. 
{{%/notice%}}

{{% notice tip %}}
You do not have to define parameter `--input` and `--output` but it is a good practice to define them in this section to provide description of the input and output of the pipeline. 
{{% /notice %}}


### 4. Pipeline variables

#### 4.1 Definition of pipeline variables

Pipeline variables are variables associated with the execution of pipeline. They are added with the progression of the pipeline and provides runtime information for each step. All pipelines starts with the following variables: 



*   **Command line options**: All command line options will be passed as pipeline variables as a list of strings, with the exceptions for 
    *   `${cmd_input}` for option `--input` 
    *   `${cmd_output}` for option `--output` Pipeline output , which will be `['data.bam']` for the above mentioned example. It does not have to a list of files. For example, it can be used to specify output directory or 



For example, `${cmd_input}` and \\({cmd_output} will be `['data.tgz']` and `['data.bam']` respectively for command `vtools execute bwa_gatk28_hg19 align --input data.tgz --output data.bam`. 


{{% notice tip %}}
A pipeline starts by default with `${cmd_input}` as input files but it can start without any input, or from another variable. 
{{% /notice %}}

{{% notice tip %}}
`${cmd_input}` and `${cmd_output}` will always be a list even if only one input or output file is passed. 
{{% /notice %}}

{{% notice tip %}}
`${cmd_input}` and @@${cmd_output} do not have to be a list of files. For example they can be used to specify input and output directories. 
{{% /notice %}}


*   **Execution environment** including 
    *   `${vtools_version}`: Version of variant tools (e.g. `2.0.2`) used to execute the pipeline. 
    *   `${spec_file}`: Full path of the specfile in which the pipeline is defined. 
    *   `${pipeline_name}` and `${model_name}`: Name of the pipeline. The name `MODEL_NAME` is preferred when the pipeline is used in variant simulation tools. 
    *   `${pipeline_step}`: Current step in the pipeline (as a string). 
    *   `${ref_genome_build}`: Primary build of the reference genome of the project (e.g. `hg19`). 
    *   `${local_resource}`: Project resource directory (runtime variable `$local_resource`). 
    *   `${cache_dir}`: Project cache directory, which is usually used to store all intermediate files of a pipeline. 
    *   `${temp_dir}`: Project temporary directory (`$temp_dir`), which can be used to store, for example, java temp directories. This directory can be set by runtime option `$temp_dir`. A system temp directory will be used if the pipeline is executed without a variant tools project. 
    *   `${model_name}` and `SEED`: Name of the simulation model (pipeline) and seed. Used by [Variant Simulation Tools][2][?][2]. 
    *   `${home}`: user's home directory. 
    *   `${working_dir}` Working directory, which is default to current directory. 
    

*   **User-defined variables** defined in the top section and pipeline sections. The top section usually defines constant that will be used later. The pipeline sections usually define variables as a result of certain action. 


{{% notice tip%}}
You can override some execution environment variables by re-defining it in the top section. In particular, if you define `${working_dir}` in the top section of the spec file, all jobs will be executed under this directory (although some actions can have their own working directories). 
{{% /notice %}}


*   **Runtime variables** including 
    
    *   `${input}` as input to actions because an action might be repeated for each input files. 



#### 4.2 Use of Pipline variables

It is important to remember that 


{{% notice info %}}
Pipeline variables are case-insensitive, read only, and can be only string or list of strings. List of strings are joined by space when they are outputted. 
{{% /notice %}}

{{% notice info %}}
All file-list variables such as `cmd_input`, `cmd_output`, `input`, `inputXXX`, `outputXXX` (where `XXX` is step of pipeline) and [their aliases][3] are list of strings, even if there is only one file in the list. 
{{% /notice %}}

{{% notice info %}}
All command line arguments are list of strings. 
{{% /notice %}}

{{% notice info %}}
All other variables such as user-defined variables can hold string only. 
{{% /notice %}}
For example, if the value of variable `cmd_input` is `['file1.txt', 'file2.txt']`, they will appear as `file1.txt file2.txt` when `${cmd_input}` is used in a command line (with proper quotation). 

If you need to access one or more elements of the list of strings, use variables such as `${input[0]}`, `${cmd_output[-1]}`, `${input[2:]}` and `${input[0][:-3]}`. 

If you need to output pipeline variables in any other format, you can use a function form of the variable `${var: lambda_func}` using Python lambda function. For example, 



    \\({cmd_output: os.path.basename(cmd_output[0])}
    

passes value of `cmd_output` to a Python lambda function `lambda x: os.path.basename(x[0])`, which will be `"output.bam"` if `${cmd_output}` equals to `"/path/to/output.bam"`. 



    \\({input: ','.join(sorted([x for x in input if '_R1_' in x]))}
    

takes a list of input files, select files with `_R1_` in filename, sort them, and output them as comma-separated list. 

This mechanism is very powerful in that the lambda function can take zero or more than one pipeline variables. For example 



    hostname=${: subprocess.check_output("hostname")}
    

returns the output of the `hostname` command 



    \\({input,cmd_output: OS.PATH.JOIN(cmd_output[0], input[0])}
    


{{% notice warning %}}
Use of shell variables (e.g. use a for loop in action `RunCommand`) is possible but can be tricky because pipeline and shell variables can take the same form. Whereas simple form of shell variables (`$VAR` instead of `${var}`) can be used without problem, the brace form `${var}` will trigger a warning message if `VAR` is a not valid pipeline variable, and return unexpected results otherwise. 
{{% /notice %}}

{{% notice warning%}}
Pipeline variables can use functions from common Python modules such as `os`, `sys`, `glob`, `subprocess`, and functions defined in modules imported using action `ImportModule`. If you need more modules, you can import them using inline script of action `ImportModule`. 
{{% /notice %}}


### 5. Step sections

#### 5.1 Name of step sections `[PIPELINE]`, `[XX]`, `[PIPELINE_XX]`, or `[PIPELINE_XX,PIPELINE1_XX]`, or `[*_XX]`

A pipeline is, roughly speaking, a *pipe* that connects the input (e.g. raw reads in fastq format) to the output (e.g. aligned reads in bam format), going through a few steps (actions) along the way. A pipeline specification file can define multiple pipelines with different `PIPELINE`. Steps in a pipeline are numbered and will be executed in such order. The indexes of actions do not have to be consecutive so `align_10`, `align_20`, and `align_30` are acceptable. They do not even have to be defined in the order they are be executed. 

If your pipeline contains only one step, you can just define a section as follows 



    [test_env]
    

If your spec file defines only one pipeline or if you would like to define a default pipeline that will be executed without specifying a name, you can specify this pipeline without name, e.g. 

    [100]
        [200]
    

Otherwise you can define multiple multi-step pipelines like 



    [EU_10]
        [EU_20]
        [AF_10]
        [AF_20]
    

A section can define multiple pipeline steps if the same step can be used for multiple steps of a pipeline or for other pipelines in the same file. For example 



    [EU_100,EU_200,EU_300]
    

    [100, EU_100,AF_100,GT_100]
    

can be used to perform the same action for steps 100, 200, and 300 of pipeline `EU`, or the same step 100 for pipelines `default`, `EU`, `AF` and `GT`. In the latter case, you can even use wildcard character 

    [*_100]
    

to define a step that will be executed by all pipelines defined in this file. 



#### 5.2 Content of pipeline step sections 

For each step of a pipeline, we need to know 

*   What are the input files 
*   How to process input files? One by one or altogether? 
*   What actions should be applied to the input files? 
*   What are the outputs? 

Answers of these questions should be specified using the following keys: 



*   **`input`** (optional). List of input files for a step. The default value of the `input` is the output of the previous step (or the command input for the first step). One or more files could be specified explicitly (separated by space). For example, 



    # output of step 400, not from previous step
    input: \\({output400}
    
    # output from multiple steps
    input: \\({output400} \\({output500}
    
    # all files in a directory
    input: \\({:glob.glob('*.gz')}
    


{{% notice tip %}}
A pipeline will be terminated if there is no input file or if any of the specified input files does not exist. 
{{% /notice %}}

*   **`input options`** (optional). By default, all input files are passed together to the action (so `${input}` equals to `${inputxxx}` where `XXX` is number of pipeline step. You can change this behavior by setting one or more input options, which are specified by one or more comma-separated `opt=val` options in the format of 



    input:  input_files : option1, option2, option3
    



For example, the following example select all fastq files from input files and send them to pipeline action in pairs: 



    input:  \\({cmd_input}
        : select='fastq', group='pair'
    



*Variant Tools* currently provides the following options: 

*   '''`group_by='all'` Eligible files are by default sent altogether (`group_by='all'`) to `action` (`group_by='all'`, `${input}` equals to `${input#}` where `#` is the index of step), but can also be sent individually (`group_by='single'`, `${input}` is a list of a single file), or in pairs (`group_by='paired'`, e.g. `filename_1.txt` and `filename_2.txt`). 

*   **`select=True/False/'fastq'/...`** `select` can be `True` (all input file), `False` (no input file, the step will be skipped), `'fastq'` (ignore file extension and check content of files), or one or more file extensions (e.g. `['sam', 'bam']`). 

*   **`pass_unselected=True`**: If files are not used (pass through), unselected files are by default passed directly as output of a step. 

*   **`skip=True/False`**: Skip an step if set to True (which is usually a variable. All input files will be passed directly to output by default. 


{{% notice tip%}}
An input option does not substitute `${input}` because it determines `${input}`. They can however use other variables such as `${cmd_output}`. For example, 

    \\({bam_files} : \\({input200:len(input200)==1})
    
    
select files only if there are more than one input file. This is useful, for example, to merge bam files only if there are more than one input bam files. 
{{% /notice %}}


*   **`action`** (required): An action that will be executed by variant tools, sometimes repeatedly for different input files (e.g. for each or each pair of input files). Each action will return a list of output files, which will form the output files of the step. A list of actions can be specified in the format of `Action1, Action2, ...`. These actions will be executed sequentially and the output of a previous action will become the input of the following action. Please check the actions section for a list of available actions. **The `action=` key can be ignored.**. 

*   **`NAME=VALUE`** (optional): This allows the pipeline step to define some pipeline variable with results obtained by the step. For example, if this step writes an optional flag in file `file1.txt`, you can use 



    flag=${: open("file1.txt").read() }
    



to save its content to a pipeline variable. 

If an action differ only slightly across pipelines, you can use variable `${pipeline_name}` to perform different actions for different pipelines. For example, 



    [eu_100,af_100]
        ..... \\({pipeline_name: '-g' if PIPELINE_NAME='eu' else ''}
    

uses passes an additional option `-g` to an action for pipeline `eu`. 


{{% notice tip%}}
Comments in pipeline steps will be displayed in the output of `vtools show pipeline`: 
{{%/notice%}}


    [hg19_100]
    # decompress input files only if they are compressed
    DecompressFiles(...)
    





#### 5.3 Section options (`[pipeline_100: output_alias=hits]`) 

Pipeline steps accept a few options that tells variant tools how to handle input and output files. These options are specified in section head after section names in the format of 



    [[p1_10, p2_20 : option1, option2]]
    

Variant Tools currently supports the following options 



*   `independent`. This option tells variant tools that a step does not belong to a pipeline and there is no need to track input and output of it. The variable `${input}` will be undefined for this step and its output will not be passed to the next step. This option should be used for steps such as `CheckVariantToolsVersion`, `DownloadResource` that are independent of input files. 

*   `no_input`: The step does not need any input file to generate output. Because variant tools terminates a pipeline if there is no input file, this option allows the starting or continuation of pipeline with no input file. 

*   `blocking`: The step is shared by multiple instance of the pipelines and can only be executed by one instance. If multiple instances are running, only the first one will execute it and the rest of them will wait for the output to be generated. This option should be used for steps to download data, to generate index et al. 

*   `input_alias=another_name` and `output_alias=another_name: Assign variable `another_name` to the input and output of the step, respectively. This option is very useful to give output of a step a meaningful name so that the subsequent steps can refer to them by this name. In the following example, pipeline variable `${accepted_hits}` becomes an alias to `${output200}` after the execution of `hg19_200@@, and can be used in later sections. 



    [hg19_200: output_alias=accepted_hits]
    RunCommand('tophat ....')
    
    [hg19_210]
    ...
    
    [hg19_200]
    input:  \\({accepted_hits}
    RunCommand('...')
    



### 6. Available actions

Actions are functions that are executed by *Variant Tools*. 


{{% notice info%}}
Technically speaking, pipeline actions are evaluated as a Python expression to obtain a `PipelineAction` object. That is to say, you can use arbitrary python expressions such as list comprehension for this item. 
{{% /notice %}}

Given an action, variant tools 

1.  Replace `${name}` with corresponding pipeline variable `NAME`. Lambda functions such as `{:EXPR}`, `{NAME:EXPR}`, `{NAME1,NAME2:EXPR}` etc will be evaluated before they are substituted. 
2.  Evaluate the text as a Python expression to obtain an `PipelineAction` object that will be called by *Variant Tools*. Python functions and expressions will be evaluated during this step. 

For example, for the following action, 



    CheckDirs(["${resource_dir}", os.path.join('${cache_dir}', '${pipeline_name}')])
    

will be processed as to 

    CheckDirs(["/path/to/resource", os.path.join('cache', 'EUS')])
    

with command line option `--resource_dir /path/to/resource` (or use default value defined in section `DEFAULT`), and values of pipeline variables `CACHE_DIR` and `PIPELINE_NAME`, and finally be evaluated to produce an object `CheckDirs` with parameters: 

    CheckDirs(["/path/to/resource", 'cache/EUS'])
    

There are two kinds of pipeline actions 



1.  Built-in actions: Actions that are defined by variant tools. 

2.  Pipeline-defined actions: Actions that are defined by users of variant tools pipeline. They are defined in `.py` files and need to be imported to a pipeline using action `ImportModules`. 

Because of the increasing number of pipeline actions, variant tools provides a command 



    % vtools show actions
    

to list all built-in action (for variant tools and variant simulation tools), and actions defined by pipelines in the variant tools repository. You can check the details of each action using command 



    % vtools show action ACTION
    

For example, you can use command 



    % vtools show action TerminateIf
    

    Help on class TerminateIf in module variant_tools.pipeline:
    
    class TerminateIf(PipelineAction)
     |  Terminate a pipeline if a condition is not met.
     |
     |  Examples:
     |      TerminateIf(not '${cmd_output}', 'No --output is specified.')
     |
     |  Methods defined here:
     |
     |  __call__(self, ifiles, pipeline=None)
     |      Terminate the pipeline if specified condition is met.
     |
     |      Parameters:
     |          ifiles: unused
     |          pipeline: unused
     |
     |      Results:
     |          Pass input to output. Does not change pipeline.
     |
     |      Raises:
     |          A RuntimeError will be raised to terminate the pipeline if
     |          the condition is met.
     |
     |  __init__(self, cond, message)
     |      Parameters:
     |          cond (boolean):
     |              True or False. In practice, ``cond`` is usually
     |              a lambda function that checks the existence of a file or value
     |              of a pipeline variable.
     |
     |          message (string):
     |              A message to be outputted when the condition is met.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from PipelineAction:
     |
     |  execute(self, ifiles, pipeline=None)
     |      Function called by __call__ for actual action performed on ifiles. A user-defined
     |      action should re-define __call__ or redefine this function and return ``True`` if the
     |      action is completed successfully.
    

to check the details of action `TerminateIf`. 



#### 6.1 Brief description of built-in actions

The following is a partial list of built-in actions defined by variant tools. The descriptions are brief and might have been outdated so please use command above to check the latest documentation. 



*   **`CheckVariantToolsVersion(ver)`**: Check the version of variant tools. Stop the pipeline if it is not recent enough to execute the pipeline. 

*   **`CheckCommands(cmds)`**: Check the existence of command `cmds` and raise an error if the command does not exist. Input files of the step is passed directly as output files. 

*   **`CheckFiles(files, msg='')`**: Check the existence of specified files. This can be used to check, for example, the existence of the `.jar` file of `GATK`. An error message can be specified. 

*   **`CheckDirs(dirs, msg='')`**: Check the existence of specified directories. An error message can be specified. 

*   **`CheckOutput(cmd, patterns, failIfMismatch=True)`**: Check the output of a command and see if it matches one of the specified patterns (see the `search` function of [Python re package][4] for details). The pipeline will be terminated if `failIfMismatch` is set to `True` (default). This action is usually used to check the version of commands. 



*   Check for a specific version of bwa 

    CheckOutput('bwa', 'Version: 0.7.4')
    



*   Check for multiple allowed versions of bwa 

    CheckOutput('bwa', 'Version: 0.7.*')
    



*   Check version of picard 

    CheckOutput('ls %(picard_path)s/picard*.jar', 'picard-1.82')
    



*   Check version of GATK 

    CheckOutput('java -jar %(gatk_path)/GenomeAnalysisTK.jar -version', '^2.4')
    



*   Check version of MosaikAligner 

    CheckOutput('MosaikAligner -version', '2.1')
    



*   **`DownloadResource(resource, dest_dir)`**: Download a list of resources (URLs) (a single string, URLs can be separated by spaces or newlines) to a pipeline resource directory `resource_dir`. **The resources will not be downloaded if the files already exist.** `.gz` files will be decompressed automatically. If both `filename` and `filename.md5` exist, the md5 signature of `filename` will be compared to `filename.md5`. `resource_dir` will be locked during downloading so only one process can execute this step at any time. 

*   **`RunCommand(cmd, working_dir=None, output=[], submitter=None)`**: Execute `cmd` (one command or a list of commands) under working directory `working_dir` (default to current project directory). A list of output files specified by `output` will be returned. If `output` is specified, three additional files, `filename.out#`, `filename.err#`, `filename.exe_info` (where `filename` is the first file in `output`) will be produced with command output, command error output, and command execution information, respectively. Command execution information contains command executed, start and ending time, file size and md5 signature of input and output files. **If output files already exist, newer than input files, size and md5 checksum of input and output files and command used match what have been recorded in `filename.exe_info`, the command will not be executed**. Because valid `filename.exe_info` files are only created after commands are completed successfully (not interrupted), a pipeline can be safely resumed if it is terminated due to user or system errors. 


{{% notice tip %}}
Multiple commands could be executed in a single `RunCommand` action. The pipeline will terminate if any of the commands returns non-zero code. 
{{%/notice%}}

{{% notice tip %}}
Using option `output` to specify output files is highly recommended because otherwise the command will be re-executed if the pipeline is re-executed. If the command does not produce any new output (e.g. many vtools commands), you can generate a status output file and use it as output, as in 
{{% /notice %}}
    RunCommand(cmd=['vtools import \\({input: " ".join(input)} --build hg19',
                   'vtools show genotypes > genotype.lst'],
                   output='genotype.lst')
    
{{% notice tip %}}
If a valid `working_dir` is set, the child process in which the commands are executed will switch to this directory but the current directory of the master process will remain the same. That is to say, all input and output filenames etc are still relative to the project path, but `os.path.abspath` might be needed if these path are used in the `cmd`. 
{{% /notice %}}

{{% notice tip%}}
If a `submitter` is defined, the submission command will be used to run the commands in background (e.g. `submitter='sh {} &'`) or as a separate job (e.g. @@submitter='qsub {}'). This allows parallel execution of pipeline steps. 
{{%/notice%}}

{{% notice tip%}}
If no output is specified, input files are passed through as output files. 
{{% /notice %}}

{{% notice warning%}}
Arbitrary command could be defined for this action, which in theory could destroy all your data or system. It is your responsibility to verify that a pipeline description file does not contain malicious piece of code and we (developers of variant tools) are not responsible for any damage that might have been caused. 
{{%/notice%}}


*   **`ExecuteRScript(script, working_dir=None, output=[], submitter=None)`**: Execute an in-line R script. 

*   **`ExecuteShellScript(script, working_dir=None, output=[], submitter=None)`**: Execute an in-line shell script. 

*   **`ExecutePythonScript(script, working_dir=None, output=[], submitter=None)`**: Execute an in-line Python script. 

*   **`ExecutePython3Script(script, working_dir=None, output=[], submitter=None)`**: Execute an in-line Python3 script. 

*   **`ExecutePerlScript(script, working_dir=None, output=[], submitter=None)`**: Execute an in-line Perl script. 

*   **`ExecuteRubyScript(script, working_dir=None, output=[], submitter=None)`**: Execute an in-line Ruby script. 



#### 6.2 Define your own pipeline actions

You can define your pipeline actions to perform steps that cannot be performed by an existing command. There are several ways to achieve this. 



*   For simple tasks that can be achieved using shell script, Python script, R script etc, use actions such as `ExecuteShellScript`. 

*   If the steps requires processing of a single file, you can define an in-line action using action `ExecutePythonCode`. This action looks like 



    ExecutePythonCode(='''
    with open("${input:input[0]}", 'r') as input:
        # process input files
        # generate output files
        # set variables to pipeline.VARS (e.g. pipeline.VARS['read_length'] = 100)
    ''')
    

The difference between `ExecutePythonCode` and `ExecutePythonScript` is that `ExcutePythonCode` will be execute in the current process, and the script passed to `ExecutePythonScript` will be written to a Python script and called using a separate processed with optional command line options. 



*   If you have a complex action that involves classes and/or multiple functions, you can define the action in a `.py` file and import it using action `ImportModule`. Taking an example from `RNASeq_tools.py`, the `@.py` file looks like: 



    from variant_tools.utils import env, calculateMD5
    from variant_tools.pipeline import PipelineAction
    
    class CreateRefGeneBed(PipelineAction):
        '''This pipeline step converts UCSC refGene.txt to BED format,
        to be used by tools such as RSeQC.'''
        def __init__(self, txt_file, output):
            PipelineAction.__init__(self, 'CreateRefGeneBed_v1 --txt_file {} {} '
                .format(txt_file, calculateMD5(txt_file, partial=True)), output)
            self.txt_file = txt_file
    
        def _execute(self, ifiles, pipeline=None):
            with open(self.txt_file, 'rU') as ifile, open(self.output[0], 'w') as ofile:
                for line in ifile:
                    ls = line.strip().split('\t')
                    starts = [int(x) for x in ls[9].strip(',').split(',')]
                    stops = [int(x) for x in ls[10].strip(',').split(',')]
                    lengths = ','.join([str(y-x) for x,y in zip(starts, stops)])
                    relstarts = ','.join([str(x-int(ls[4])) for x in starts])
                    ofile.write("{0}\t{1}\t{2}\t{3}\t0\t{4}\t{5}\t{6}\t0\t{7}\t{8}\t{9}\n".format(
                        ls[2], ls[4], ls[5], ls[1], ls[3], ls[6], ls[7], ls[8], lengths, relstarts))
            return True
    



This function converts a UCSC refGene.txt to BED format so that it can be used by tools such as RSeQC. Basically, 

* A class should be derived from `PipelineAction` defined in `variant_tools.pipeline` 

* It should call `PipelineAction.__init__(self, cmd, output)` with proper command line and expected output files so that the action will be skipped if it is called with identical signature. 

* Define function `_execute(self, ifiles, pipeline)` to perform needed action and return output files and returns `True` if everything is ok. This function can generate output files, and/or set pipeline variables using `pipeline.VARS[key]=value`. 



*   Import the module to your pipeline using `ImportModules('my_tools.py')`.

 [1]:    /documentation/pipelines/format10/
 [2]:    /documentation/customization/simulation/
 [3]: #alias
 [4]: http://docs.python.org/2/library/re.html