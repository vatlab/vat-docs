
+++
title = "Customized"
weight = 2
+++


## Specification of a variant tools pipeline


This page describes the original pipeline format (version 1.0). Please refer to [New][1][?][1] if you are editing a new pipeline specification file for variant tools 2.7 and later. 



### 1. Introduction

*Variant Tools* uses pipeline specification files to define pipelines. A pipeline specification file can define multiple pipelines. It can be stored locally or online in the variant tools repository (or a local repository maintained by your system adminstrator). You can use command 



    % vtools show pipelines
    

to get a list of all publicly available pipelines, and 



    % vtools show pipeline SPECFILE
    

to get the details of pipelines defined in `SPECFILE`. This output consists of description of the `SPECFILE`, all pipelines in it, steps of each pipeline, and options of the pipelines. 

A pipeline can be executed by command 



    % vtools execute SPECFILE PIPELINE --input XXX --output XXX [OPTIONS]
    

where `SPECFILE` can be a local `.pipeline` file, or name of an online pipeline specification file, `PIPELINE` is the name of the pipeline defined in SPECFILE. The command line can be simplied to 



    % vtools execute SPECFILE -i XXX -o XXX [OPTIONS]
    

if the spec file only defines one pipeline. 

The format of pipeline spec files follows the `.ini` files of the good old days. It is not as fashionable as `XML` based configuration files but it is easier to read and write, and provides advanced features such as automatic parameter processing. 



The `.ini` format is simple to read and write but please note that 



*   Values of an item can be expanded into multiple lines, e.g. 



    name=this is a long text
      that continues to the second line
      or the third
    



Consequently, **you can expand your comments or commands into several lines as long as you do not start from the first column**. 



*   `"%"` is used for variable substitution (`%(VAR)s`) so **`%``%` should be used in place of `%`**. 

*   ";" prefixed by a whitespace is recognized as inline comment, so you should **leave no space before `;` if it is part of the value of an item**. 

A pipeline spec file should have a `pipleine description` section and multiple pipeline step sections. 



### 2. Section `[pipeline description]`

A pipeline specification file should start with a "pipeline description" section. This section should have the following keys: 



*   `description`: Summary of pipelines defined in this SPECFILE, which should include format and type of input data (raw reads? bam file? paired end?), external commands that are used, a short description of steps involved, and reference to external documentation if available. 

*   `PIPELINE_description`: Description of pipeline `PIPELINE`. `PIPELINE` has to be a valid pipeline defined in this file (with sections `PIPELINE_XX`). 



If you have long descriptions (highly recommended!), you can break it into several paragraphs by adding HTML tags `<p>` or `<br>`. Tag `<p>` starts a new paragraph (two newlines) and tag `<br>` starts a new line (one newline). You can also use tags <ul> and <li> to generate itemized lists. For example, 



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



*   `NAME=VAL` (optional): Pipeline variables. This is usually a good place to define constant values that will be used by pipeline steps. For example: 
    
        RESOURCE_DIR=${LOCAL_RESOURCE}/pipeline_resource/name_of_pipeline
        



where ${LOCAL_RESOURCE} is another pipeline variable that has value of project runtime option `$local_resource`. We will talk about pipeline variables in details later. 



## Section `[DEFAULT]` (command line options)

The `DEFAULT` section defines parameters that can be changed using command line arguments. For example, in the following `.pipeline` file (partial) 



    [DEFAULT]
    opt_java=-Xmx4g
    opt_java_comment=parameter passed to the java command, default to -Xmx4g to use a maximum of 4g heap space.
    
    [align_5]
    action=RunCommand(cmd="java %(opt_java)s SortSam ...")
    

The value of `opt_java` will be used to replace all instances of `%(opt_java)s` in the pipeline configuration file. The key `opt_java` has a help message defined by item `opt_java_comment`, and a default value `-Xmx4g`. If you query the details of this pipeline using command 



    % vtools show pipeline my_pipeline
    

you will see at the end of the output the following description: 



    Pipeline parameters:
      opt_java     parameter passed to the java command, default to -Xmx4g to use a maximum of 4g heap space.
                   (default: -Xmx4g)
    

That is to say, you can pass an alternative value of `opt_java` to this format using command-line options such as `--opt_java -Xmx32g` to change the value of this option. 



If you have a large number of parameters, you can save them to an external file, one item per line, and load them by prefixing filename with a `"@"` symbol. For example, if you have a file `param.cfg` with content 



    --bwa
    /path/to/bwa
    --samtools
    /path/to/samtools
    

you can load parameters `--bwa /path/to/bwa --samtools /path/to/samtools` using `"@param.cfg"` from command line. 



### 3. Pipeline variables



#### 3.1 Definition of pipeline variables

Two different types of variables can be used in a spec file: command line options and pipeline variables. Command line options are defined in the `[DEFAULT]` section and are used in the spec file with syntax `%(NAME)s`. These variables are replaced right after a spec file is loaded and cannot be changed. 

Pipeline variables are variables associated with the execution of pipeline. They are added with the progression of the pipeline and provides runtime information for each step. 

All pipelines starts with the following variables: 



*   `${CMD_INPUT}`: Pipeline input from command line option `--input`. For example, `${CMD_INPUT}` will be `['data.tgz']` for command `vtools execute bwa_gatk28_hg19 align --input data.tgz --output data.bam`. 



*   `${CMD_INPUT}` will always be a list even if only one input file is passed. 
*   `${CMD_INPUT}` does not have to be a list of files but it must be translated to a list of filenames in the `input` section of the first step because each steps expects a list of files. 



*   `${CMD_OUTPUT}`: Pipeline output from command line option `--output`, which will be `['data.bam']` for the above mentioned example. It does not have to a list of files. For example, it can be used to specify output directory or prefix of output files. 

*   `${VTOOLS_VERSION}`: Version of variant tools (e.g. `2.0.2`) used to execute the pipeline. 

*   `${SPEC_FILE}`: Full path of the specfile in which the pipeline is defined. 

*   `${PIPELINE_NAME}` and `${MODEL_NAME}`: Name of the pipeline. The name `MODEL_NAME` is preferred when the pipeline is used in variant simulation tools. 

*   `${PIPELINE_STEP}`: Current step in the pipeline (as a string). 

*   `${REF_GENOME_BUILD}`: Primary build of the reference genome of the project (e.g. `hg19`). 

*   `${LOCAL_RESOURCE}`: Project resource directory (runtime variable `$local_resource`). 

*   `${CACHE_DIR}`: Project cache directory, which is usually used to store all intermediate files of a pipeline. 

*   `${TEMP_DIR}`: Project temporary directory (`$temp_dir`), which can be used to store, for example, java temp directories. This directory can be set by runtime option `$temp_dir`. A system temp directory will be used if the pipeline is executed without a variant tools project. 

*   `{MODEL_NAME}` and `SEED`: Name of the simulation model (pipeline) and seed. Used by [Variant Simulation Tools][2][?][2]. 

Varialbes defined in the `[Pipeline Description]` section are added before the execution of the pipeline. Then, for each step, variant tools defines 



*   `${INPUT1}`, `${INPUT2}`, ... 

as input files of the step, and 



*   `${OUTPUT1}`, `${OUTPUT2}`, ... 

as output files of the step after the completion of each step. Variables can be defined and added to the pipeline **after the completion of each step**. Because these files are dynamically determined, '''you can not refer to input and output files of a later step of a pipeline'''. Because input files will be selected and passed to pipeline actions in groups, a temporary variable 



*   `${INPUT}` 

is used to store each group of input files. For example, if the input fastq files are emitted in groups (more about this later), `${INPUT}` will be paired filenames. **This variable should only be used in the `action` item of a step**. 



### Use of Pipline variables

It is important to remember that 



*   Pipeline variables are case-insensitive, read only, and can be only string or list of strings. List of strings are joined by space when they are outputted. 
*   All file-list variables such as `CMD_INPUT`, `CMD_OUTPUT`, `INPUT`, `INPUTXXX`, `OUTPUTXXX` (where `XXX` is step of pipeline) are list of strings, even if there is only one file in the list. 

For example, if the value of variable `CMD_INPUT` is `['file1.txt', 'file2.txt']`, they will appear as `file1.txt file2.txt` when `${CMD_INPUT}` is used in a command line. 

If you need to output pipeline variables in any other format, you can use a function form of the variable `${VAR: lambda_func}` using Python lambda function. For example, 



    ${CMD_OUTPUT: os.path.basename(CMD_OUTPUT[0])}
    

passes value of `CMD_OUTPUT` to a Python lambda function `lambda x: os.path.basename(x[0])`, which will be `"output.bam"` if `${CMD_OUTPUT}` equals to `"/path/to/output.bam"`. 



    ${INPUT: ','.join(sorted([x for x in INPUT if '_R1_' in x]))}
    

takes a list of input files, select files with `_R1_` in filename, sort them, and output them as comma-separated list. 

This mechanism is very powerful in that the lambda function can take zero or more than one pipeline variables. For example 



    ${: "-f" if "%(force)s" == "Yes" else ""}
    

returns `-f` if a command line parameter `force` is set to "Yes". 



    ${INPUT,CMD_OUTPUT: os.path.join(CMD_OUTPUT[0], INPUT[0])}
    



Use of shell variables (e.g. use a for loop in action `RunCommand`) is possible but can be tricky because pipeline and shell variables can take the same form. Whereas simple form of shell variables (`$VAR` instead of `${VAR}`) can be used without problem, the brace form `${VAR}` will trigger a warning message if `VAR` is a not valid pipeline variable, and return unexpected results otherwise. 



## Pipeline action sections `[PIPELINE_XX]`, or `[PIPELINE_XX,PIPELINE1_XX]`, or `[*_XX]`

A pipeline is, roughly speaking, a *pipe* that connects the input (e.g. raw reads in fastq format) to the output (e.g. aligned reads in bam format), going through a few steps (actions) along the way. A pipeline specification file can define multiple pipelines with different `PIPELINE`. Steps in a pipeline are numbered and will be executed in such order. 



*   The same action can be used for multiple pipelines in the same spec file or be called at different steps of the same pipeline. You can even use pipeline variable `{pipeline_name}` and `${pipeline_step}` to allow slightly different actions for different steps. 
*   The indexes of actions do not have to be consecutive so `align_10`, `align_20`, and `align_30` are acceptable. They do not even have to be defined in the order they are be executed. 

For each step of a pipeline, we need to know 

*   What are the input files 
*   How to process input files? One by one or altogether? 
*   What actions should be applied to the input files? 
*   What are the outputs? 

Answers of these questions should be specified using the following keys: 



*   **`input`** (optional). List of input files for a step. The default value of the `input` is the output of the previous step (or the command input for the first step). One or more files could be specified explicitly (separated by space, space in filenames should be escaped by a back slash). For example, 



    # output of step 400, not from previous step
    input=${OUTPUT400}
    
    # output from multiple steps
    input=${OUTPUT400} ${OUTPUT500}
    
    # all files in a directory
    input=${:glob.glob('*.gz')}
    
    # If your pipeline does not need any input file, you can use the SPECFILE
    # itself as a placeholder.  
    input=${SPECFILE}
    



*   A pipeline will be terminated if there is no input file or if any of the specified input files does not exist. 



*   **`input_emitter`** (optional). How to emit input files to `action`. By default, all input files are passed together to the action (so `${INPUT}` equals to `${INPUTXXX}` where `XXX` is number of pipeline step. An input emitter changes this behavior. Basically, an emitter select input files, divides them into groups and pass them one by one to the `action`. Unselected files can be discarded or passed directly as step output. 



*Variant Tools* currently provides two input emitters: 

**`EmitInput(group_by='all', select=True, pass_unselected=True)`**: Select input files of certain types, group them, and send input files to `action`. `select` can be `True` (all input file), `False` (no input file, the step will be skipped), `'fastq'` (ignore file extension and check content of files), or one or more file extensions (e.g. `['sam', 'bam']`). Eligible files are by default sent altogether (`group_by='all'`) to `action` (`group_by='all'`, `${INPUT}` equals to `${INPUT#}` where `#` is the index of step), but can also be sent individually (`group_by='single'`, `${INPUT}` is a list of a single file), or in pairs (`group_by='paired'`, e.g. `filename_1.txt` and `filename_2.txt`). Unselected files are by default passed directly as output of a step. 

**`SkipIf(cond, pass_unselected=True)`**: Skip an step if condition is `True`. All input files will be passed directly to output by default. This is equvalent to `EmitInput(select=not cond, pass_unselected)`. 



An input emitter does not substitute `${INPUT}` because it determines `${INPUT}`. They can however use other variables such as `${CMD_OUTPUT}`. For example, 

    SkipIf(${INPUT200:len(INPUT200)==1})
    
    

select files only if there are more than one input file. This is useful, for example, to merge bam files only if there are more than one input bam files. 



*   **`action`** (required): An action that will be executed by variant tools, sometimes repeatedly for different input files (e.g. for each or each pair of input files). Each action will return a list of output files, which will form the output files of the step. A list of actions can be specified in the format of `Action1, Action2, ...`. These actions will be executed sequentially and the output of a previous action will become the input of the following action. Please check the actions section for a list of available actions. 

*   **`comment`** (optional): description of this step of the pipeline. 

*   **`NAME=VALUE`** (optional): This allows the pipeline step to define some pipeline variable with results obtained by the step. For example, if this step writes an optional flag in file `file1.txt`, you can use 



    FLAG=${: open("file1.txt").read() }
    



to save its content to a pipeline variable. In addition, it is a good 

practice to rename `OUTPUTXXX` to a more meaningful name to make the pipeline more readable. For example 



    ACCEPTED_HITS=${OUTPUT440}
    

assigns the `OUTPUT440` to a variable `ACCEPTED_HITS` so that you can use `ACCEPTED_HITS` in later actions. Note that the usage of two variables are slightly different because `ACCEPTED_HITS` is a string where as `OUTPUT440` is a list of string. 



A section can define multiple pipeline steps if the same step can be used for multiple steps of a pipeline or for other pipelines in the same file. For example 



    [EU_100,EU_200,EU_300]
    

    [EU_100,AF_100,GT_100]
    

can be used to perform the same action for steps 100, 200, and 300 of pipeline `EU`, or the same step 100 for pipelines `EU`, `AF` and `GT`. In the latter case, you can even use wildcard character 

    [*_100]
    

to define a step that will be executed by all pipelines defined in this file. 

If an action differ only slightly across pipelines, you can use variable `${PIPELINE_NAME}` to perform different actions for different pipelines. For example, 



    [eu_100,af_100]
        action= ..... ${PIPELINE_NAME: '-g' if PIPELINE_NAME='eu' else ''}
    

uses passes an additional option `-g` to an action for pipeline `eu`. 





## Available actions

Actions are functions that are executed by *Variant Tools*. 



Technically speaking, pipeline actions are evaluated as a Python expression to obtain a `PipelineAction` object. That is to say, you can use arbitrary python expressions for this item. 

Given an action, variant tools 

1.  Replace `%(NAME)s` with corresponding command line argument `NAME`. 
2.  Replace `${NAME}` with corresponding pipeline variable `NAME`. Lambda functions such as `{:EXPR}`, `{NAME:EXPR}`, `{NAME1,NAME2:EXPR}` etc will be evaluated before they are substituted. 
3.  Evaluate the text as a Python expression to obtain an `PipelineAction` object that will be called by *Variant Tools*. Python functions and expressions will be evaluated during this step. 

For example, for the following action, 



    action=CheckDirs(["%(resource_dir)s", os.path.join('${CACHE_DIR}', '${PIPELINE_NAME}')])
    

will be processed as 



    action=CheckDirs(["/path/to/resource", os.path.join('${CACHE_DIR}', '${PIPELINE_NAME}')])
    

with command line option `--resource_dir /path/to/resource` (or use default value defined in section `DEFAULT`), and then to 

    action=CheckDirs(["/path/to/resource", os.path.join('cache', 'EUS')])
    

if the current pipeline is called `EUS`, and finally be evaluated to produce an object `CheckDirs` with parameters: 

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
     |      action=TerminateIf(not '${CMD_OUTPUT}', 'No --output is specified.')
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



### Brief description of built-in actions

The following is a partial list of built-in actions defined by variant tools. The descriptions are brief and might have been outdated so please use command above to check the latest documentation. 



*   **`CheckVariantToolsVersion(ver)`**: Check the version of variant tools. Stop the pipeline if it is not recent enough to execute the pipeline. 

*   **`CheckCommands(cmds)`**: Check the existence of command `cmds` and raise an error if the command does not exist. Input files of the step is passed directly as output files. 

*   **`CheckFiles(files, msg='')`**: Check the existence of specified files. This can be used to check, for example, the existence of the `.jar` file of `GATK`. An error message can be specified. 

*   **`CheckDirs(dirs, msg='')`**: Check the existence of specified directories. An error message can be specified. 

*   **`CheckOutput(cmd, patterns, failIfMismatch=True)`**: Check the output of a command and see if it matches one of the specified patterns (see the `search` function of [Python re package][3] for details). The pipeline will be terminated if `failIfMismatch` is set to `True` (default). This action is usually used to check the version of commands. 



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

*   **RemoveIntermediateFiles(files)**: This action replaces specified files with info files (adds extension `.file_info`) that records the size, MD5 signature and modification date of the original files, usually after the completion of steps that make use of these intermediate files. *variant tools* will not try to re-execute the step with the existence of such truncated output files, unless a real output file is need to re-execute a later step. **This action does not change input pipeline files. Files to be removed needs to be explicitly specified.** (e.g. Use `RemoveIntermediateFiles('${OUTPUT400}')` instead of specifying `input=${OUTPUT400}`) 

*   **`RunCommand(cmd, working_dir=None, output=[], submitter=None)`**: Execute `cmd` (one command or a list of commands) under working directory `working_dir` (default to current project directory). A list of output files specified by `output` will be returned. If `output` is specified, three additional files, `filename.out#`, `filename.err#`, `filename.exe_info` (where `filename` is the first file in `output`) will be produced with command output, command error output, and command execution information, respectively. Command execution information contains command executed, start and ending time, file size and md5 signature of input and output files. **If output files already exist, newer than input files, size and md5 checksum of input and output files and command used match what have been recorded in `filename.exe_info`, the command will not be executed**. Because valid `filename.exe_info` files are only created after commands are completed successfully (not interrupted), a pipeline can be safely resumed if it is terminated due to user or system errors. 



*   Multiple commands could be executed in a single `RunCommand` action. The pipeline will terminate if any of the commands returns non-zero code. 
*   Using option `output` to specify output files is highly recommended because otherwise the command will be re-executed if the pipeline is re-executed. If the command does not produce any new output (e.g. many vtools commands), you can generate a status output file and use it as output, as in 

    RunCommand(cmd=['vtools import ${INPUT: " ".join(INPUT)} --build hg19',
                   'vtools show genotypes > genotype.lst'],
                   output='genotype.lst')
    

*   If a valid `working_dir` is set, the child process in which the commands are executed will switch to this directory but the current directory of the master process will remain the same. That is to say, all input and output filenames etc are still relative to the project path, but `os.path.abspath` might be needed if these path are used in the `cmd`. 
*   If a `submitter` is defined, the submission command will be used to run the commands in background (e.g. `submitter='sh {} &'`) or as a separate job (e.g. @@submitter='qsub {}'). This allows parallel execution of pipeline steps. 
*   If no output is specified, input files are passed through as output files. 



Arbitrary command could be defined for this action, which in theory could destroy all your data or system. It is your responsibility to verify that a pipeline description file does not contain malicious piece of code and we (developers of variant tools) are not responsible for any damage that might have been caused. 



### Define your own pipeline actions

You can define your pipeline actions to perform steps that cannot be performed by an existing command. Generally speaking, you will need to 



*   Create a `.py` file such as `my_actions.py` with the actions. Taking an example from `RNASeq_tools.py`, the `@.py` file should look like: 



    from variant_tools.utils import env, calculateMD5
    from variant_tools.pipeline import PipelineAction
    
    class CreateRefGeneBed(PipelineAction):
        '''This pipeline step converts UCSC refGene.txt to BED format,
        to be used by tools such as RSeQC.'''
        def __init__(self, txt_file, output):
            # NOTE: incrase _v? after the change of this function that might affect output
            PipelineAction.__init__(self, 'CreateRefGeneBed_v1 --txt_file {} {} '
                .format(txt_file, calculateMD5(txt_file, partial=True)), output)
            self.txt_file = txt_file
    
        def _execute(self, ifiles, pipeline=None):
            with open(self.txt_file, 'rU') as ifile, open(self.output[0], 'w') as ofile:
                for line in ifile:
                    # 13      NM_020929       chr11   -       40135750        41481186        40135919        40137842        5
                    #           40135750,40162350,40341177,40669691,41480980,   40137884,40162403,40341271,40669828,41481186,   0
                    #           LRRC4C  cmpl    cmpl    0,-1,-1,-1,-1,
                    #
                    ls = line.strip().split('\t')
                    #
                    # ls[9]: exon start (0-based)
                    # ls[10]: exon end (1-based)
                    #
                    starts = [int(x) for x in ls[9].strip(',').split(',')]
                    stops = [int(x) for x in ls[10].strip(',').split(',')]
                    #
                    # length is the sum of exons
                    lengths = ','.join([str(y-x) for x,y in zip(starts, stops)])
                    #
                    # ls[4]: gene start 
                    #
                    # relative start positions
                    relstarts = ','.join([str(x-int(ls[4])) for x in starts])
                    #
                    # write each line in BED format
                    #
                    # chromosome
                    # chromStart
                    # chromEnd
                    # name
                    # score, ---unused--- 
                    # strand
                    # coding start
                    # coding end
                    # itemRgb ---unused---
                    # blockCount, namely number of exons
                    # blockStarts, namely relative starting position of the exons
                    #
                    # chr11    40135750    41481186    NM_020929    0    -    40135919    40137842    0    5
                    #       2134,53,94,137,206    0,26600,205427,533941,1345230
                    #
                    ofile.write("{0}\t{1}\t{2}\t{3}\t0\t{4}\t{5}\t{6}\t0\t{7}\t{8}\t{9}\n".format(
                        ls[2], ls[4], ls[5], ls[1], ls[3], ls[6], ls[7], ls[8], lengths, relstarts))
            return True
    



This function converts a UCSC refGene.txt to BEd format so that it can be used by tools such as RSeQC. Basically, 

* A class should be derived from `PipelineAction` defined in `variant_tools.pipeline` 

* It should call `PipelineAction.__init__(self, cmd, output)` with proper command line and expected output files so that the action will be skipped if it is called with identical signature. 

* Define function `_execute(self, ifiles, pipeline)` to perform needed action and return output files and returns `True` if everything is ok. This function can generate output files, and/or set pipeline variables using `pipeline.VARS[key]=value`. 



*   Import the module to your pipeline using `ImportModules('my_tools.py')`.

 [1]: http://localhost/~iceli/wiki/pmwiki.php?n=Pipeline.New?action=edit
 [2]: http://localhost/~iceli/wiki/pmwiki.php?n=Simulation.HomePage?action=edit
 [3]: http://docs.python.org/2/library/re.html
