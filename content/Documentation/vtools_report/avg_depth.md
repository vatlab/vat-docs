
+++
title = "avg_depth"
weight = 1
+++


## Average depth of coverage Ratio



### 1. About ``vtools_report avg_depth ``

This command report average depth of all variants, or variants divided by sample allele count. 



### 2. Usage

    % vtools_report avg_depth -h
    
    usage: vtools_report avg_depth [-h] -n NUM_FIELD -d DEPTH_FIELD
                                   [--group_by [GROUP_BY [GROUP_BY ...]]]
                                   [-v {0,1,2}]
                                   table
    
    Command 'vtools update table --from_stat "meanDP=avg(DP_geno)"' calculates the
    average depth of variants across sample (e.g. average depth of three variants
    if the variant appears three times in the sample). This command report average
    depth of all variants, or variants divided by sample allele count (output
    count, number of variant, and average depth for count from 1 to 2*#sample).
    This command requires a field that stores the sample count for each variant
    and a field to store average depth of each variant, which should be prepared
    using command 'vtools update table --from_stat "num=#(alt)"
    "meanDP=avg(DP_geno)"'.
    
    positional arguments:
      table                 Variant table for which average depth are calculated.
    
    optional arguments:
      -h, --help            show this help message and exit
      -n NUM_FIELD, --num_field NUM_FIELD
                            Name of the field that holds sample variant count,
                            which is the field name for command 'vtools update
                            table --from_stat "num=#(alt)"'.
      -d DEPTH_FIELD, --depth_field DEPTH_FIELD
                            Name of the field that holds average depth of each
                            variant, which is the field name for command 'vtools
                            update table --from_stat "meanDP=avg(DP_geno)"'.
      --group_by [GROUP_BY [GROUP_BY ...]]
                            Output average depth for each group, for example, '--
                            group_by NUM_FIELD to output depth for each sample
                            variant frequency (count).
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.
    



### 3. Example

    % vtools_report avg_depth variant -n num -d depth
    
    num_of_variant	average_depth
    905	6.86372641088
    



    % vtools_report avg_depth variant -n num -d depth --group_by num

    num	num_of_variant	average_depth
    1	410	7.18662601626
    2	163	32.3737218814
    3	28	6.8375
    4	72	35.1266203704
    5	19	4.93245614035
    6	14	4.93571428571
    7	23	4.10942028986
    ... ...