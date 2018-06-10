
+++
title = "running R programs"
weight = 1
+++



## A General Framework for Association Analysis Using R Programs 



### 1. Introduction

A number of rare variant association methods as well as the flexible *VAT ensemble* algorithm makes it possible to conveniently evaluate variant associations via different statistical options. In addition to the existing association testing framework, `variant association tools` can talk to [R][1] via customized R programs prepared by users. Under this mechanism, users write up an R function that analyzes data of an association testing unit (e.g., gene) and specify the output statistic that passes into VAT to create formatted text file or annotation databases. Input association data comes directly from the project database, cleaned and annotated. Users can thus focus on customizing the association analysis without having to worry about file format conversions, quality control and annotations. Multiprocessing and auto results annotation features are also supported to guarantee efficient computation and neat output. This general R interface is not only suitable for evaluating novel statistical tests for method development projects, but also good for highly customized analysis of real world data with simple R scripts. 

The mechanism is implemented as `RTest` method which is available from `vtools associate` command interface. Please read below for instructions on preparing and executing R programs via `RTest`. 



### 2. Details

#### 2.1 Interface

    vtools show test RTest
    
    Name:          RTest
    Description:   A general framework for association analysis using R programs
    usage: vtools associate --method RTest [-h] [--name NAME] [--data_cache N]
                                           script
    
    R test
    
    positional arguments:
      script          R program to be loaded. The R script format has to follow
                      the convention documented at
                      http://varianttools.sf.net/Association/RTest
    
    optional arguments:
      -h, --help      show this help message and exit
      --name NAME     Name of the test that will be appended to names of output
                      fields.
      --data_cache N  Name of R data sets to be written into cache folder, for
                      debug purpose.
    

A trivial example of the R script looks like the following 


    1.  BEGINCONF 
    2.  [sample.size] 
    3.  [result] 
    4.  n=2 
    5.  columns=2 
    6.  name=beta0, beta1 
    7.  column_name=estimate, p.value 
    8.  ENDCONF 

    regression = function (dat, phenotype.name, family = "gaussian") { 
        y = dat@Y[, phenotype.name]
          x = apply(dat@X, 1, function(i) sum(i, na.rm=T))
          m = glm(y~x,family=family)
          return (list(sample.size=length(y), result=summary(m)$coef[,c(1,4)]))
    } 

To use this program for data analysis, 



    vtools associate variant stroke \
    -m 'RTest /path/to/regression.R --name demo --phenotype.name "stroke" --family "binomial"' \
    \
    -g refGene.name2 -j8 --to_db demo > demo.txt
    



#### 2.2 Format

You should have one main function in the R program named the same as the R script file name. This is the interface function that interacts with the `RTest` command, taking input parameters from command line and return output in specified format (see below for details) that can be recognized by `RTest` and be stored in databases. This main function can call any other R objects as long as they are available from R or implemented elsewhere in your R program. 



##### Input parameters

The main function should be defined in the following format 

(:codestart r</summary> ScriptName <- function(dataname, args, **kwargs) { ... } (:codeend</summary> 

where the first argument has to be the data object variable name (e.g. `dat` in the `regression.R` example, or any other valid names you specify), followed by a few required positional arguments (e.g. `phenotype.name` in `regression.R` example which has to be passed from commandline every time the program is executed), and other keyword arguments that have default values (e.g. `family` in the `regression.R` example. If not specified from the command line it will use default value "gaussian"). The required and optional arguments can be assigned from the commandline (e.g., the `--phenotype.name 'stroke'` argument of `vtools associate`). 



##### Output configuration

The return object of the main R function should be a list with the properties of each element in the list been pre-specified as comment strings at the beginning of the scripts taking the following format 



    # BEGINCONF
    # [attribute1]
    # name=
    # type=
    # comment=
    # [attribute2]
    # n=N
    # columns=
    # name=
    # column_name=
    # type=
    # comment=
    # ENDCONF
    

and the return R list object is 



    list(attribute1=..., attribute2=..., ...)
    



*   The configuration area are R comments, starts with **BEGINCONF** and ends with **ENDCONF**. 
*   Each section name corresponds to an attribute in the return R list of the main function. Values of these attributes can be R **numeric, string, vector, matrix or data.frame. Other R data type are not allowed**. 
*   For attributes that are single values, e.g., numeric or string, two properties can be specified: a **name** property (default to the same name as the R attribute's name), a**type** property (default to "float") and a **comment** property (default to empty string). You can set them to different values than default, or use the default value by leaving the attribute empty (e.g. the `[sample.size]` attribute in the `regression.R` example) 
*   For attributes that are R vectors or two dimensional (2D) data.frame or matrices, the property **n**, indicating the number of elements in the vector or number of rows in 2D objects, have to be specified. **If n is not specified the attribute will be treated as a single numeric value**, leading to truncated result output. Besides **n**, all other properties have default values same as with single value attributes which can be re-set by specifying them in the configuration. For vector objects the **name** property, if set, should be comma separated and have number of elements equals **n**. The **type** of all elements in a vector should be the same, so there is only one **type** value to be set (e.g. `type=float` for all the **n** elements). For 2D objects, an additional **required** property **p** has to be set to specify how many columns are there in the attribute. The **type** property now would have to have **p** elements separated by comma, specifying the type of each column (e.g., `type=float, string` for the 1st column being float and 2nd column being character string). The **name** property is now the name of the rows, and an additional optional **column_name** property can be specified for column names. The **comment** property, if set, should be a sentence that briefly describes the entire section, not specific to certain row or column. 

It is important that the return R object matches the descriptions in the configuration area. **If the configuration area is not found in the R script, no output will be written to result databases**. This is allowed because there are usage cases that does not need any output, e.g., you write an R program to plot some graphical summary of the association testing unit rather than performing association analysis and calculate p-values. 



##### Data structure

Data from `vtools associate` are passed into the main R function taking a variable name defined by the first argument of the function. For example if the first argument name is `dat` then you should manipulate the R variable `dat` in your R program. The `dat` object contains 3 default attributes and two optional attributes. 

Default attributes 



*   R variable `dat@name` is a **single character string** which is the association testing group name of the data set. For example if the command is `vtools associate ... -m ' ... ' --group_by refGene.name2`, then the group name will be refseq gene names. If no `--group_by` option is used the group name will be `chromosome:position` of a variant. 
*   R variable `dat@X` is a **data.frame** with rows being samples (row names are sample names) and columns being variants (column names are `chromosome:position` of variants). The samples match the `vtools associate ... --samples` specification, and the variants are the ones in the `variant_table` specified by the association command `vtools associate variant_table ...` 
*   R variable `dat` object, although you can also pass the names of these phenotype/covariates to the R function and refer to the columns by their names (e.g., the `phenotype.name` specification in the `regression.R` example) 

Optional attributes 



*   R variable `dat@V` is a **data.frame** of variant information corresponding to `--var_info` option in `vtools associate` command. The rows are variants (row names are `chromosome:position`) and columns are variant information / annotation field names. 
*   R variable `dat@G` is a **list of data.frame** of genotype information corresponding to `--geno_info` option in `vtools associate` command. Each attribute in the list is a data.frame with rows being samples and columns being the genotype information of each genotype call in a sample, e.g., the genotype quality, imputation scores, etc. 



#### 2.3 Cautions

This R interfacing mechanism is flexible, and fragile at the same time, because the `RTest` method of `vtools associate` will have no control over what are implemented inside the R program. It assumes the R program the users provide is flawless and can result in exactly the same output as specified in the configuration area. If any errors occurs in the program, `RTest` will not attempt to fix it. It instead will simply flag an association test as "failed". If you run an genome-wide association scan with your R program via `RTest` method and noticed all tests failed, its most likely your R program is problematic. 



##### Debug suggestions

*   All error messages will be written to the project log file for you to look into. Take a look at the log file to figure out why failures occur and fix your R code. 
*   A more advance option is to write out one or two groups of data with the R code to test interactively in R to see what's going wrong. The `--data_cache N` option will output N R scripts per thread with data-set coded in it, to `cache` folder. The file name will be `[Association Group Name].dat.R`. For debug purpose you can add `--data_cache 1` to the association command and run the command on a small variant table, find the R data file in `cache`, load it in R and play with the data-set to make sure your R function works, then remove the `--data_cache` option to actually perform association scans. 





### 3. Example

We provide some R interface examples for `RTest` method as extensions to the standard routines `vtools associate` provides. These examples are meant to be demonstrations for `RTest` method and are not thoroughly tested for use in a production environment. You are welcome to engineer them to better shape and use for your projects. We and other uses would appreciate it if you are willing to share your R program to the developers mailinglist (varianttools-devel@lists.sourceforge.net) and allow us to publish on this website for others to use. 



*   [`MetaSKAT` analysis][2], contributed by Gao Wang (varianttools-devel) and Raphael Mourad (University of Chicago) 
*   The `RAssociation` package

 [1]: http://cran.r-project.org/
 [2]:   /applications/association/create_your_test/rtest/