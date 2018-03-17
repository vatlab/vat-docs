+++
title = "FAQ"
description = ""
+++


### Import data

#### Some of my samples occur in multiple vcf files but their genotype calls may be different. How can I identify them after they are imported?

Because a file might contain genotype for multiple samples (.vcf), and genotype for a sample can be spread into several files (your case), **a sample in variant tools is uniquely identified by `filename` and `sample_name`** in the output of "`vtools show sample`". However 



*   Samples usually come with pre-specified names (the header line of vcf or other text files). But you may customize sample names by option `--sample_name` in `vtools import` for different data sources when you import data. The customized names will overwrite the original names. Then your sample can be identified by option `--samples 'sample_name = "name"'` in `vtools select` command. 

*   If there are too many to customize, you could still identify your sample by `filename + sample_name` (e.g. `--samples 'filename like "FILE_1%"' 'sample_name = "NA07000"'`). 

*   You can also add a column of customized sample names to the sample table using command `vtools phenotype`. You can then refer to the samples using the new names. For example you append an additional column `sampleID` to the sample table, where you customize sample names from different sources, then use `--samples 'sampleID="name"'` to identify samples. 



### My filtering commands are running slowly

With SQLite and MySQL, you can "analyze" tables or create indexes on table columns to help speed up queries. Creating indexes though does increase the size of the database and can slow down import speeds. Indexes based on genomic positions are automatically created by vtools. 



#### Can I rename sample's name

#### Is there a way to merge a sample from the different sources

#### How to update the sample information, inclusing geno, and phenotype information

#### What kind formats can be imported using vtools

#### What kind of formats of the results can be outputed using vtools

#### Can I use the different versions of human genome assembled

#### How to create sub-project

#### Can I exclude some specific samples

#### How to remove the tables I created 

#### how to create connection between my samples and the annotation database

#### Can I use more than 1 annotation databases

#### 

`vtools execute 'analyze variant'` 

`vtools execute 'create index my_index on variant(some_field)'` 

For more help see: 

*   <http://www.sqlite.org/lang_analyze.html> 
*   <http://www.sqlite.org/lang_createindex.html>