
+++
title = "import_vcf"
description = ""
weight = 1
+++


# Import all variant and genotype fields from vcf files


## Usage

    % vtools show pipeline import_vcf
    

    This pipeline creates a customized .fmt file to import all variant and
    genotype info fields of input vcf files.
    
    Available pipelines: import_vcf
    
    Pipeline "import_vcf":  This pipeline creates a customized .fmt file by
    scanning the header of input vcf files and imports all variant and genotype
    info fields of the input files in VCF format. If an output file is specified
    (--output), it will be used to save the customized .fmt file.
      import_vcf_0:       Check the version of variant tools (version 2.1.1 and
                          above is required to execute this pipeline)
      import_vcf_10:      Create a feild description file from input text file.
      import_vcf_20:      Import input files using customized .fmt file. Please
                          check the .fmt file if the import process fails due to
                          incorrect field information.
    
    Pipeline parameters:
      build               Build of reference genome, which will be guessed
                          from the input vcf file (if it contains a
                          comment line with reference genome information).
    



## Details

*variant tools* provides a general `vcf.fmt` that contains the definition of many commonly used variant and genotype info fields, but the command `vtools import` by default does not import any of them. The reasons behind this include 



1.  A vcf file can contain many info fields, including novel ones that are not defined in `vcf.fmt` 
2.  Importing all info into a project is not always a good idea (increase the size of project etc). Even if you lave them out during the import stage, you can add them later using command `vtools update --from_file`, access them using the `track` function, or move them into an annotation database (see pipeline `annFileFromVcf` in `anno_utils.pipeline`. 
3.  It is not always clear how to import certain variant or genotype fields. For example, a variant info field `DP` might better be imported as genotype field if the samples are called one by one and `DP` describes per-sample read depth. 

Anyway, if you would like to import all information from an input vcf file, you can 

1.  Create a customized `.fmt` file that contains all variant and genotype info fields from the input vcf file 
2.  Import data using this customized `.fmt` file, 

This pipeline assists this process by automating the creation of the `.fmt` file. 



*   This pipeline outputs a `.fmt` file if you specify a output file using command line option `--output`. You can modify this file and use command `vtools import` to import data if the pipeline fails to execute (e.g. when an invalid field name is used). 
*   Although you can specify multiple vcf files in the command line (parameter --input), the format will be generated from the first vcf file. These vcf files therefore must have the same variant and genotype fields. 

<details><summary> Import all fields from vcf files</summary> 

    % vtools init test -f
    % vtools execute import_vcf --input V*.vcf
    

    INFO: Executing import_vcf.import_vcf_0: Check the version of variant tools (version 2.1.1 and above is required to execute this pipeline)
    INFO: Executing import_vcf.import_vcf_10: Create a feild description file from input text file.
    INFO: Executing import_vcf.import_vcf_20: Import input files using customized .fmt file. Please check the .fmt file if the import process fails due to incorrect field information.
    INFO: Running vtools import V1.vcf V2.vcf V3.vcf --build hg19 --format cache/V1.vcf.fmt
    INFO: Importing variants from V1.vcf (1/3)
    V1.vcf: 100% [================================================] 1,000 17.2K/s in 00:00:00
    INFO: 985 new variants (985 SNVs, 2 unsupported) from 1,000 lines are imported.
    INFO: Importing variants from V2.vcf (2/3)
    V2.vcf: 100% [================================================] 1,000 15.1K/s in 00:00:00
    INFO: 348 new variants (984 SNVs, 3 unsupported) from 1,000 lines are imported.
    INFO: Importing variants from V3.vcf (3/3)
    V3.vcf: 100% [================================================] 1,000 14.8K/s in 00:00:00
    INFO: 270 new variants (986 SNVs, 1 unsupported) from 1,000 lines are imported.
    Importing genotypes: 100% [====================================] 4,818 2.4K/s in 00:00:02
    Copying samples: 100% [===========================================] 6 48.0K/s in 00:00:00
    INFO: 1,603 new variants (2,955 SNVs, 6 unsupported) from 3,000 lines (3 samples) are imported.
    INFO: Command "vtools import V1.vcf V2.vcf V3.vcf --build hg19 --format cache/V1.vcf.fmt" completed successfully in 00:00:12
    

(:exampleend</summary>