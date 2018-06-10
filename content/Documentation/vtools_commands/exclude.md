+++
title = "exclude"
description = ""
weight = 9
+++


## Exclude variants that match certain criteria


### 1. Usage

    % vtools exclude -h
    
    usage: vtools exclude [-h] [-s [COND [COND ...]]] [-t [TABLE [DESC ...]]]
                          [-c | -o [FIELDS [FIELDS ...]]]
                          [--header [HEADER [HEADER ...]]] [-d DELIMITER]
                          [--na NA] [-l N] [--build BUILD]
                          [-g [FIELD [FIELD ...]]]
                          [--order_by [FIELD [FIELD ...]]] [-u] [-v {0,1,2}]
                          from_table [condition [condition ...]]
    
    Exclude variants according to properties (variant and annotation fields) and
    membership (samples) of variant. The result can be counted, outputted, or
    saved to a variant table.
    
    positional arguments:
      from_table            Source variant table.
      condition             Conditions by which variants are excluded. Multiple
                            arguments are automatically joined by 'AND' so 'OR'
                            conditions should be provided by a single argument
                            with conditions joined by 'OR'. If unspecified, all
                            variants (except those excluded by parameter
                            --samples) will be excluded.
    
    optional arguments:
      -h, --help            show this help message and exit
      -s [COND [COND ...]], --samples [COND [COND ...]]
                            Limiting variants from samples that match conditions
                            that use columns shown in command 'vtools show sample'
                            (e.g. 'aff=1', 'filename like "MG%"').
      -t [TABLE [DESC ...]], --to_table [TABLE [DESC ...]]
                            Destination variant table.
      -c, --count           Output number of variant, which is a shortcut to '--
                            output count(1)'.
      -o [FIELDS [FIELDS ...]], --output [FIELDS [FIELDS ...]]
                            A list of fields that will be outputted. SQL-
                            compatible expressions or functions such as "pos-1",
                            "count(1)" or "sum(num)" are also allowed.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).
    
    Output options:
      --header [HEADER [HEADER ...]]
                            A complete header or a list of names that will be
                            joined by a delimiter (parameter --delimiter). If a
                            special name - is specified, the header will be read
                            from the standard input, which is the preferred way to
                            specify large multi-line headers (e.g. cat myheader |
                            vtools export --header -). If this parameter is given
                            without parameter, a default header will be derived
                            from field names.
      -d DELIMITER, --delimiter DELIMITER
                            Delimiter, default to tab, a popular alternative is
                            ',' for csv output
      --na NA               Output string for missing value
      -l N, --limit N       Limit output to the first N records.
      --build BUILD         Output reference genome. If set to alternative build,
                            chr and pos in the fields will be replaced by alt_chr
                            and alt_pos
      -g [FIELD [FIELD ...]], --group_by [FIELD [FIELD ...]]
                            Group output by fields. This option is useful for
                            aggregation output where summary statistics are
                            grouped by one or more fields.
      --order_by [FIELD [FIELD ...]]
                            Order output by specified fields in ascending order.
      -u, --unique          Remove duplicated records while keeping the order of
                            output. This option can be time- and RAM-consuming
                            because it keeps all outputted records in RAM to
                            identify duplicated records. You should pipe output to
                            command 'uniq' if you only need to remove adjacent
                            duplicated lines.
    



### 2. Details

This command differs from `vtools select` only in that it **excludes** (rather than selects) from a variant table a subset of variants satisfying given condition(s), count, output or save the remaining variants. 

However, command `vtools exclude` is not simply a `vtools select` command with a reversed condtion. As we will show in the examples, command "`` `vtools select table cond ``" (e.g. `sift_score > 0.95`) and "`vtools exclude table reverse-cond `" (e.g. `sift_score <= 0.95`) might select different sets of variants. This happens when 



*   **If field values for some variants are missing (`NULL`)**, they will not be selected by commands such as  `vtools select table "sift_score > 0.95" ` and `vtools select table "sift_score <= 0.95" `. Variants without a score and with score > 0.95 can be selected by command `vtools exclude table "sift_score <= 0.95"`. Alternatively, you can use command `vtools select table "sift_score > 0.95 OR sift_score is NULL" ` to explicitly specify the NULL case. 

*   **If there are multiple entries for a variant in the annotation database**, these variants might match both conditions. This is, for example, the case for some variants in dbNSFP when these variants are included in different genes and have different damaging scores. These variants will only be selected by  `vtools select`. 

<details><summary> Examples: </summary> 

For example, 



    % vtools select ns 'sift_score > 0.95' -t ns_damaging
    
    Running: 0 0.0/s in 00:00:00
    INFO: 10 variants selected.
    

selects 10 variants. If we remove non-synonymous variants with sift_score <= 0.95, we will get 9 variants. 



    % vtools exclude ns 'sift_score <= 0.95' -t ns_excl_benign   

     Running: 0 0.0/s in 00:00:00
     INFO: 9 variants selected.
    

We track this difference using `vtools compare` 



    % vtools compare ns_damaging ns_excl_benign --difference diff -v0
    

and output the information for this variant 



    % vtools output diff variant_id chr pos ref alt sift_score genename --build hg18
    
    1036	5	139908704	C	A	1	        ANKHD1-EIF4EBP3
    1036	5	139908704	C	A	0.942108	EIF4EBP3
    

if we use the complete `dbNSFP` annotation database we can show more fields 



    % vtools output diff variant_id chr pos ref alt CCDSid sift_score genename Descriptive_gene_name --build hg18
    
    #id     chr  pos        ref  alt CCDSid         sift_score      genename            Descriptive_gene_name
    1036	5    139908704	C    A	 CCDS4224.1	1.0	        ANKHD1-EIF4EBP3	    ANKHD1-EIF4EBP3 readthrough
    1036	5    139908704	C    A	 CCDS4226.1	0.942108	EIF4EBP3	    eukaryotic translation initiation factor 4E binding protein 3
    

It turns out that this variant has two entries in dbNSFP for different genes. In this case the variant matches both conditions "sift\_score>0.95" and "sift\_score<=0.95". As a result this variant will be selected by `vtools select "sift_score>0.95"` but not `vtools exclude "sift_score<=0.95"` 



</details>