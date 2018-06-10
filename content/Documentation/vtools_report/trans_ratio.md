

+++
title = "trans_ratio"
weight = 5
+++



## Transition-transversion Ratio



### 1. About ``vtools_report trans_ratio ``

This command counts the number of transition and transversion variants and calculates its ratio. The expected ratio is 2 in human pseudo-genes (after the exclusion of transitions at CpG sites). 



### 2. Usage

    % vtools_report trans_ratio -h  

    usage: vtools_report trans_ratio [-h] -n NUM_FIELD
                                     [--group_by [GROUP_BY [GROUP_BY ...]]]
                                     [-v {0,1,2}]
                                     table
    
    This command counts the number of transition (A<->G and C<->T) and
    transversion variants (others) and calculate its ratio. A ratio of 2 is
    expected from a normal sample. If option '--by_count' is specified, it will
    calculate this ratio for variants with different sample allele frequency
    (count). This commands requires a field that stores the sample count for each
    variant, which should be prepared using command 'vtools update table
    --from_stat "num=#(alt)"'.
    
    positional arguments:
      table                 Variant table for which transversion/transversion
                            mutants are counted.
    
    optional arguments:
      -h, --help            show this help message and exit
      -n NUM_FIELD, --num_field NUM_FIELD
                            Name of the field that holds sample variant count,
                            which is the field name for command 'vtools update
                            table --from_stat "num=#(alt)"'.
      --group_by [GROUP_BY [GROUP_BY ...]]
                            Output transition/transversion rate for groups of
                            variants. e.g. --group_by num for each sample variant
                            frequency group.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.
    



### 3. Example

    % vtools_report trans_ratio variant -n num  

    num_of_transition	num_of_transversion	ratio
    4891	                2562	                1.909


    % vtools_report trans_ratio variant -n num --group_by num   

    sample_count    num_of_transition       num_of_transversion     ratio
    1               375                     170                     2.206
    2               105                     68                      1.544
    3               17                      8                       2.125
    4               44                      25                      1.760
    5               15                      3                       5.000
    6               10                      11                      0.909
    7               9                       6                       1.500
    8               12                      7                       1.714
    9               8                       7                       1.143
    10              4                       6                       0.667
    ... ...