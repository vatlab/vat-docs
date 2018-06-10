
+++
title = "report progress"
weight = 1
+++


## Report the progress of the execution of pipelines 




### 1. ChangeLog

*   Dec 30, 2013: Initial release 



### 2. Download

Download [report_progress][1], use 



`% python report_progress` 

or execute 



`% report_progress` 

directly after `chmod +x report_progress`. 

Note:  Python module [matplotlib][2] is required to execute this script. 



### 3. Introduction

*variant tools* records the progress of the execution of pipelines in log files. This script parses the log files, extract the starting end ending time of the execution of each step of the pipeline, and plots them in a resulting pdf file. 



    % report_progress -h
    
    usage: report_progress [-h] [--output OUTPUT] logfiles [logfiles ...]
    
    This script reads one or more local or remote log files produces by variant
    tools, extract starting times of steps of pipelines, and generate graphical
    reports
    
    positional arguments:
      logfiles         One or more log files. If address:path is specified, log
                       files will be copied to a temporary directory using command
                       scp. No password can be specified so public key
                       authentication is needed if a password is needed.
    
    optional arguments:
      -h, --help       show this help message and exit
      --output OUTPUT  Name of the output file (in pdf format). progress.pdf will
                       be used if no file is specified.
    



This command accept a list of log files, which can be local or remote. In the latter case, command `scp` will be used to copy the files to a local temporary directory. 



    % python report_progress /path/to/*.log
    % python report_progress 'username@server:path/to/*bam.log'
    

Without specifying the `--output` parameter, the figures will be saved in a PDF file named `progress.pdf`, with figures similar to 

 Attach:progress\_Page\_01.png  

Note that 

*   Green lines represent running times of successful steps. 
*   Red lines represent running times of failed steps. 
*   Purple lines represent on-going steps, which is the last started job in the log file. Because a job might be killed during the last step, the running time might not be accurate. 
*   Duration for the execution of successful steps are reported (for non-trivial steps that lasts more than 2 minutes).

 [1]: http://sourceforge.net/p/varianttools/code/HEAD/tree/trunk/utility/report_progress?format=raw
 [2]: http://matplotlib.org/