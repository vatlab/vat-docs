+++
title = "Pipelines"
weight = 8
+++

## Documenting and Executing Bioinformatics Pipelines using Variant Pipeline Tools (Under development)



<figure>
  <p><a href="VariantPipelineTools.pdf"><img src="documents.jpg"></a>
  <figcaption> A presentation about Variant Pipeline Tools (Jan, 12th, 2015)  </figcaption>
</figure>





### 1. Introduction

<font color = red>
 Variant Pipeline Tools has been reborn as [Script of Scripts (SoS)][3] so all VPT pipelines will be rewritten in SoS once SoS is ready for prime time. We apologize for this inconvenience but you will not regret switching to SoS because it is more flexible and powerful, yet more intuitive to use. 
 </font>

The development of Variant Pipeline Tools (VPT) was motivated by the facts that 

*   **bioinformatics analyses often involve multiple command-line tools and scripts written in different languages that are difficult to decipher**. Although it is possible and often advantageous to rely on one single language and/or platform (e.g. R/Bioconductor), a large workflow can inevitably involve multiple scripts. 

*   **Difference in processing steps, choice of tools and parameters can lead to large difference in results**. 

*   **Bioinformatics tools are updated quickly and require frequent update to pipelines**. 

Although there has been [dozens of bioinformatics workflow management systems][4], they generally require users to learn a new system and it is relatively difficult for end users to read and modify a pipeline. The lack of readability makes it difficult 



*   to understand what exactly these pipelines do. Because minor differences in parameters can cause large differences in pipeline output, it can be dangerous to rely on these blackbox pipelines. 

*   to adapt a pipeline to their own running environment or update it to newer versions of tools and annotation sources. 

*   to share pipelines with your collaborators 

Variant Pipeline Tools (VPT) is **a light-weight pipeline recording and execution tool that emphasizes on readability**. VPT is designed to 



*   **Record your bioinformatics pipelines for reproducible analysis**. After you complete a project using tools such as shell commands, Python, R, or Perl scripts, you can document what you have done as a VPT pipeline by inserting commands and scripts to a pipeline file using actions such as `ExecuteRScript` and `ExecutePythonScript`. With added description, you can document the pipeline for yourself and execute all the steps instead of invoking different tools and commands separately. 

*   **Generalize the pipeline to make it applicable to other data**. Although a pipeline can be simply a collection of documented commands and scripts, VPT allows you to use pipeline variables to replace fixed filenames or options and apply the pipeline to other data by passing different command line options. 

*   **Share your pipelines with others**. 



### 2. Features

Compared to other GUI or script based pipeline implementations, Variant Pipeline Tools 



*   **uses pipeline specifiction files to describe pipelines**. Pipelines are hosted online so adding a pipeline to the server will make it instantly available to all users of *variant tools*. It is easy to check the availability of pipelines and details of each pipeline using commands such as `vtools show pipelines` and `vtools show pipeline bwa_gatk_hg19`. The `.ini`-style description file is easy to read and write so it is relatively easy to create your own pipeline by following the [pipeline specification][5][?][5] and examples under `~/.variant_tools/pipeline`. 

*   **can execute arbitrary commands, and variant tools, third-party, or user-defined functions**. The pipeline specification also allows you to pass parameters, skip certain steps, and run certain steps in parallel. This makes Variant Pipeline Tools a powerful tool for the implementation of complex pipelines. 

*   **provides features to ensure proper execution of the pipelines**. *variant tools* automatically check the existence of external commands, download, manage required resources (e.g. reference genome, known variant sites), and record signatures of all executed steps. It is safe to resume a pipeline even with different parameter settings because *variant tools* skips steps only if their signatures match a previous run. 

Variant Pipeline Tools has been used to implement all variant tools annotation and data processing pipelines, all simulations in [Variant Simulation Tools][6][?][6], and a number of variant calling and RNA Seq data analysis pipelines. This tool, however, does not provide features such as MapReduce to handle extremely large amount of data on the cloud. Please refer to other dedicated tools such as [SeqWare][7] if you are looking for a tool for these applications. 



### 3. Usage

After [installing and configuring variant tools][8][?][8], using variant pipeline tools is as easy as 



    % vtools show pipelines
    % vtools show pipeline SPECFILE
    

to figure out what pipelines are available and details of particular pipelines. After you set up the environment for a particular environment, prepare input data, you can then execute a pipeline using command 



    % vtools execute SPECFILE [PIPELINE] [OPTIONS]
    

If you are reading a pipeline and would like to know exactly what an action does, you can run commands 

    % vtools show actions
    % vtools show action ACTION
    

to get details of all pipeline actions defined by variant tools, variant simulation tools, and customized actions for existing pipelines. 



### 4. Pros and Cons, and comparison to other pipeline tools

#### 4.1 [Snakemake][9]

Snakemake has somewhat similar design with VPT. It is based on Python, integrate well with R and other languages, has report capacity, extensible. The major differences between VPT and snakemake is snakemake are rule based and VPT is step based. 



*   The rule-based design makes snakemake very appealing to Makefile users and make it easy to optimize execution of steps. A more complex pipeline can sometimes be written by integrating some sub-rules that are already available for smaller tasks. However, at least in bioinformatics world, there are many ways to perform a task and the choice of tools and parameters can make a huge difference. VPT chooses a design that shows all the steps and parameter up front instead of hiding rules in other files.

 
 [3]: https://github.com/bpeng2000/SOS
 [4]: http://en.wikipedia.org/wiki/Bioinformatics_workflow_management_system
 [5]: /vat-docs/documentation/pipelines/customizedpipeline/
 [6]: /vat-docs/documentation/customization/simulation/
 [7]: http://seqware.github.io/docs/1-introduction/
 [8]: /vat-docs/installation/
 [9]: https://bitbucket.org/johanneskoester/snakemake/wiki/Home
