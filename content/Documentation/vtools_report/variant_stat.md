
+++
title = "variant_stat"
weight = 6
+++



## Counting variants of different types, optionally by samples



### 1. Usage

    % vtools_report variant_stat -h
    
    usage: vtools_report variant_stat [-h] [-s [SAMPLES [SAMPLES ...]]]
                                      [-g [GROUP_BY [GROUP_BY ...]]] [-v {0,1,2}]
                                      table
    
    Command 'vtools variant_stat' calculates the number of snps, insertions,
    deletions and substitutions for groups of samples with some size metrics to
    characterize the indels. The statistics can be calculated for all samples
    (effectively for the master variant table when parameters --samples and
    --group_by are ignored), a subset of samples (e.g. --samples aff=1), grouped
    by samples (e.g. --group_by aff), or for each sample separately (e.g.
    --group_by filename sample_name, because those two fields in the sample table
    uniquely identify each sample.
    
    positional arguments:
      table                 Variant table for which variant metrics are
                            calculated.
    
    optional arguments:
      -h, --help            show this help message and exit
      -s [SAMPLES [SAMPLES ...]], --samples [SAMPLES [SAMPLES ...]]
                            Limiting variants from samples that match conditions
                            that use columns shown in command 'vtools show sample'
                            (e.g. 'aff=1', 'filename like "MG%"'). If this
                            parameter is specified without a value, variants
                            belonging to any of the samples will be counted. If
                            this parameter is left unspecified, all variants,
                            including those that do not belong to any samples will
                            be counted.
      -g [GROUP_BY [GROUP_BY ...]], --group_by [GROUP_BY [GROUP_BY ...]]
                            Group samples by certain conditions such as 'aff=1'. A
                            common usage is to group variants by 'filename' and
                            'sample_name' so that variant statistics are outputted
                            for each sample.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.
    



### 2. Details

This command calculates the number of snps, insertions, deletions and substitutions for groups of samples with some size metrics to characterize the indels. You can use parameters `--samples` to limit variants to specified samples, and `--group_by` to output statistics for each sample groups. For example, the statistics can be calculated 

*   all variants in the specified variant table (default if parameters `--samples` and `--group_by` are ignored), 
*   a subset of samples (e.g. `--samples aff=1`), 
*   grouped by samples (e.g. `--group_by aff`), or 
*   for each sample separately (e.g. `--group_by filename sample_name`, because those two fields in the sample table uniquely identify each sample. 

{{% notice warning%}}
Note that

    % vtools_report variant_stat VTABLE
    % vtools_report variant_stat VTABLE --samples 1
    % vtools_report variant_stat VTABLE --group_by aff   
might give different total variant count because the first command counts all variants in the `VTABLE`, the second and third commands count all variants in specified samples (all samples for condition `1`). Because some variants might not appear in any of the samples, the number of reported variants of the first command might be larger than the others. 

{{%/notice%}}

You would like to generate output for selected variants (e.g. variants on chromosome 1), you should use command `vtools select -t table` to generate a variant table and use this command to summarize them. 



    % vtools_report variant_stat variant --group_by filename
    
    filename	num_sample	num_snps	num_insertions	num_deletions	num_substitutions	min_insertion_size	avg_insertion_size	max_insertion_size	min_deletion_size	avg_deletion_size	max_deletion_size
    case1.vcf	1	21504	322	75	0	1	2.64906832298	23	1	1.28	11
    case10.vcf	1	21069	317	77	0	1	2.64353312303	21	1	1.25974025974	6
    case11.vcf	1	20995	315	70	0	1	2.65396825397	23	1	1.08571428571	3
    case12.vcf	1	22195	340	68	0	1	2.91176470588	26	1	1.23529411765	10
    
    ... ...