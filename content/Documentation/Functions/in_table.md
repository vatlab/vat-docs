+++
title = "in_table"
weight = 6
+++



## Test membership of variants in variant tables 




### 1. Usage

The `in_table` function is a simple function used to test is a variant is in a specified variant table. It accepts the name of a variant table and returns 1 if the variant belong to this table, and 0 otherwise. 



    in_table('table_name')
    



### 2. Details

For example, command 



    % vtools admin --load_snapshot vt_simple
    % vtools show tables