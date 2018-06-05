
+++
title = "lifttover"
description = ""
weight = 5
+++




## Adding coordinates from an alternative reference genome 

### 1. Usage

    % vtools liftover -h
    

    usage: vtools liftover [-h] [--flip] [-v STD[LOG]] build
    
    Convert coordinates of existing variants to alternative coordinates in an
    alternative reference genome. The UCSC liftover tool will be automatically
    downloaded if it is not available.
    
    positional arguments:
      build                 Name of the alternative reference genome
    
    optional arguments:
      -h, --help            show this help message and exit
      --flip                Flip primary and alternative reference genomes so that
                            the specified build will become the primary reference
                            genome of the project.
      -v STD[LOG], --verbosity STD[LOG]
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1), and to
                            a logfile (default to 2).
    



### 2. Details

Vtools provides a command which is based on the tool of USCS liftOver to map the variants from existing reference genome to an alternative build. After executing of this command, The fields of chromosome, position reference and alternative of the variant in current and previous reference genomes are all in the master variant table. 



An illustration of the liftover process 

<details><summary> An illustration of the liftover process </summary>
<!-- <img src= "/vat-docs/images/liftover.png" /> -->
![](/static/images/liftover.png)
</details>


*   This command adds `alt_chr` and `alt_pos` columns to the master variants table. 
*   Annotation databases that use the alternative reference genome can now be used. 
*   `vtools output` and `vtools export` can output alternative coordinates using parameter `--build`. 


1.  This feature is unavailable under windows because UCSC liftOver tool does not support windows. 
2.  Because the UCSC liftover tools does not guarantee complete translation, variants that failed to map will have missing alternative coordinates. 

<details><summary> Liftover from hg19 to hg38</summary> The following example demonstrates how to liftOver a project from hg18 to hg19. Note that the UCSC liftOver tool and needed chain files are automatically downloaded if they are not available. 


    % vtools init -f liftover
    % vtools import V1-3_hg19_combine.vcf --build hg19
    % vtools liftover hg38
    

    INFO: Downloading liftOver chain file from UCSC
    INFO: Exporting variants in BED format
    Exporting variants: 100% [===============================] 288 110.5K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    Updating table variant: 100% [============================] 288 780.0/s in 00:00:00

    

After the liftOver operation, three more fields are added to the master variant table (alt\_bin, alt\_chr, alt_pos) 



    % vtools show table variant

    Name:                   variant
    Description:            Master variant table
    Creation date:          May29
    Command:
    Fields:                 variant_id, bin, chr, pos, ref, alt, alt_bin, alt_chr, alt_pos
    Number of variants:     1611
    

    variant_id, bin, chr, pos, ref, alt, DP, alt_bin, alt_chr, alt_pos
    52,586,1,230047,A,T,586,1,260296
    53,586,1,230058,T,G,586,1,260307
    54,586,1,231480,G,C,586,1,261729
    55,586,1,231504,G,A,586,1,261753
    56,586,1,231526,C,T,586,1,261775
    57,586,1,232223,C,T,587,1,262472
    58,586,1,234301,T,C,587,1,264550
    59,586,1,234308,A,G,587,1,264557
    ... ...
    

</details>

<details><summary> Flipping primary and alternative reference genome</summary> 



    % vtools show
    

    Project name:                test
    Primary reference genome:    hg19
    Secondary reference genome:  hg38
    Storage method:              hdf5
    Variant tables:              variant
    Annotation databases:
    

    % vtools liftover hg38 --flip
    

    INFO: Downloading liftOver chain file from UCSC
    INFO: Exporting variants in BED format
    Exporting variants: 100% [===============================] 288 116.2K/s in 00:00:00
    INFO: Running UCSC liftOver tool
    INFO: Flipping primary and alternative reference genome
    Updating table variant: 100% [============================] 288 612.1/s in 00:00:00

    



Interruption of the flipping process will leave the project unusable because of mixed coordinates. 



    % vtools show
    

    Project name:                test
    Primary reference genome:    hg38
    Secondary reference genome:  hg19
    Storage method:              hdf5
    Variant tables:              variant
    Annotation databases: 
    

    % vtools show table variant
    

    variant_id, bin, chr, pos, ref, alt, DP, alt_bin, alt_chr, alt_pos
    52,586,1,260296,A,T,586,1,230047
    53,586,1,260307,T,G,586,1,230058
    54,586,1,261729,G,C,586,1,231480
    55,586,1,261753,G,A,586,1,231504
    56,586,1,261775,C,T,586,1,231526
    57,587,1,262472,C,T,586,1,232223
    58,587,1,264550,T,C,586,1,234301
    59,587,1,264557,A,G,586,1,234308
    ... ...
    

</details>