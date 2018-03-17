
+++
title = "Customized annotation databases"
description = ""
weight = 3
+++





# Create annotation database 




Because you write your own .ann file, please consider using pipelines in `anno_utils`, which can usually create `.ann` file from some data sources with pre-defined formats. 



## Define a new annotation database

If you would like to use an annotation source that is not currently supported by variant tools, you could [send us and email][1] if the data source is publicly available, or write an annotation specification file to create your own annotation database. This file describes various aspects of an annotation database such as 

*   Type of annotation (variant, positional, range and field) 
*   The reference genome(s) it uses, 
*   Description of the database, including license and citation, 
*   Where to get the database and/or its source, and 
*   Fields that the annotation database will provide 

An annotation file follows a windows `.ini` format. It is divided into several sections, each with several `key=entry` lines. Lines that start with a `#` or `;` are comments and are ignored. Inline comments starts with `;`. An annotation file should always starts with line 



    #Variant tools schema version 1.0
    

An annotation file should have sections `linked fields` and `data sources`, followed by sections that describe each field. 



### Section `[linked fields]`

A database can provide one or more sets of linked fields by which it is linked to the master variant table of the project. Each line should have format 

    build=field1,field2,...
    

where build is the build of a reference genome, or '*' if this annotation database can be linked to project with any referenge genome. 

One or more fields can be specified as 'linked fields': 

*   for **variant** annotation database, they should be names of chr, pos, ref, and alt fields. 
*   for **position** annotation database, they should be names of chr and pos fields. 
*   for **range** annotation database, they should be names of chr, start pos and ending pos fields. 
*   for **field** annotation database, they should be names of fields that link to the master variant table. 

For example, it a variant-based database provides coordinates for both hg18 and hg19, the build lines will be similar to 



    hg18=chr,hg18_pos,ref,alt
                  hg19=chr,hg19_pos,ref,alt
    

where `chr`, `hg18_pos`, `hg19_pos`, `ref`, `alt` are fields defined below. 



### Section `[data sources]`

This section can have keys 

*   `description`: description of the database 
*   `encoding` (optional): encoding of the input file. If you see errors such as `"codec can't decode byte 0xe7 in position 21480"`, you should perhaps add `encoding=ISO-8859-1` to your `.ann` file. 
*   `preprocessor` (optional): A preprocessor to pre-process files before it can be imported. A common preprocessor is `Dos2Unix()` which converts files with `\r` as newline character to unix format (with `\n` as newline character. 
*   `header` (optional): variant tools by default treats lines with a leading `#` as header and skip them during data importing. The header will also be used to probe sample names for some formats (e.g. .vcf). If your input file does not use such a header, you can override this behavior by specifying the number of lines to skip (`header=1`), or a pattern by which headers are matched (e.g. use `header=^%.*` for header lines starting with `%`, see [documents of the Python re package][2] for details). 
*   `anno_type`: can be one of 'variant', 'position', 'range' or 'field' 
*   `direct_url`: URL to download annotation database directly. If no URL is given, variant tools will always build the database from source. 
*   `delimiter`: delimiter to define columns in the input file. Default to tab (`delimiter='\t'`). If your input can be either tab or space delimited, use `delimiter=None`. 
*   `source_type`: type of source files, we currently supported tab based text file (txt) and vcf file. 
*   `source_url`: How to obtain source file to be imported. If *variant tools* fail to download the database directly, it will get the source file and try to import data from it. The source url can be 
    *   A local file. This is rarely used because a user who builds annotation from a local file usually specify it using option `--files` of the `vtools use` command. 
    *   A `<a class='urllink' href='ftp://' rel='nofollow'>ftp://</a>` or `<a class='urllink' href='http://' rel='nofollow'>http://</a>` (or other) URLs (white space delimited). *variant tools* will try to download the file using a http client. 
    *   A sql in the format of `sql://user@password:select something from a database`. *variant tools* will try to connect to a sql server using specified username and password, run the query and use the result as input source file. Only a mysql server is supported at this time. 
*   `source_pattern`: pattern of source files (used to exclude README etc) 
*   `version`: version of the database, which is not necessarily version of the data source. The convension is sourceVersion\_dbVersion. If unspecified, vtools will try to get it from filename. For example, dbNSFP-1.1\_0.db will have version number 1.1_0. 



### Field sections 

Fields sections describe the fields that will be imported. Each of them can have 



*   `index`: index(es) of field, which can be 
    
    *   A 1-based index of the column in the database. The value at this column of the input file will be used for this field. 
    
    *   A tuple syntax with multiple indexes separated by `','`, for example `5,7`). A list of values at specified columns will be passed to an adjust function to produce values of the field. 
    

*   `type`: can be any SQL allowed types such as "INTEGER", "FLOAT", "INTEGER NOT NULL", or "DECIMAL(7,6) NOT NULL" 

*   `comment` (optional) a description of the field 

*   `adj` (optional): Functions or functors to extract or modify one or more values from the field value. *variant tools* provides a number of functors to help the processing of different fields. For example, 
    
    *   **`IncreaseBy(inc=1)`** (increase value by `inc`). This is usually used to adjust 0-based position to 1-based position that is used by *variant tools*. 
    
    *   **`MapValue(map)`** (map value to another). This function is used to map input value to another one, for example, `MapValue({'het': '1', 'hom': '2'})` maps value 'het' to '1' and 'hom' to '2'. Note that the mapped values should be strings or `None`. 
    
    *   **`Nullify(val)`** (treat value as NULL). This is usually used to adjust input `NA` values to `NULL` in the database. 
    
    *   **`RemoveLeading(val)</strong> (remove leading characters). This is usually used to remove leading `chr` from inputs with chromosomes such as `chr1`, `chr2`, because <em>variant tools</em> only stores `1`, `2@@, etc. </li>
        
        *   **`ExtractField(index, sep=';', default=None)`** (field of a column): Split the item by `sep` and return the `index`-th field (1-based). Return `default` is there are less than `index` fields. For example, `ExtractField(2, ':')` extracts `20` from `10:20:30`. </ul></li></ul>
        
        
        *   Multiple functors/functions can be used sequentially. For example, `ExtractValue('CEU:'), ExtractField(1, '/')` extracts value `12` from `YRI:20/222;CEU:12/45` (the first extractor gets `12/45`, the second extractor gets `12`), and `ExtractValue('CEU:'), SplitField('/')` extracts values `12` and `45` from `YRI:20/222;CEU:12/45`. 
        
        *   If none of the provided extractors can be used, you can define your own function. For example, `lambda x: x[6:].replace(",", "")` extracts `24000` from `COUNT=24,000`. You can also mix function with variant tools provided extractor `ExtractValue("COUNT="), lambda x: x.replace(",", "")])` to extract `24000` from values such as `ASD;COUNT=24,000;MAF=0.5`. 
        
        *   If the return value of at least one of the fields is a tuple of more than one values (e.g. result from functor `SplitField`), multiple records will be generated from this line. Non-tuple values of other fields will be copied automatically. For example, if three fields have values `A1`, `(B1,)`, `(C1, C2)`, they will produce two records of `A1, B1, C1` and `A1, None, C2`. 
        
        *   If you would like to exclude certain records, you can use `adj` to produce invalid records that will be excluded during importing. For example, a record with `None` alternative allele, or a field with `NOT NULL` type will be ignored, or a genotype with `None` mutation type will be ignored. 
        
        
        
        ## Import and test
        
        Once you have written a `.ann` file, you can create an annotation database using command 
        
        
        
            vtools use /path/to/file.ann
            
        
        or 
        
        
        
            vtools use /path/to/file.ann --files source_files
            
        
        if you have source files available. 
        
        Once the database is created and used correctly, you can have a look at it using command 
        
        
        
            vtools show annotation ANNODB -v2
            
        
        to get the basic information of the annotation database, or 
        
        
        
            vtools show table ANNODB
            
        
        to display the actual data. 
        
        Please pay attention to invalid records and statistics of each field (e.g. missing values) to make sure the database has been created correctly. 
        
        
        
        ## Examples
        
        For example 
        
            [SIFT_pred]
            index=20
            adj=Nullify('NA')
            type=VARCHAR(2) NULL
            comment=SIFT prediction, D(amaging) or T(olerated)
            
        
        specifies a field that predicts if a variant is damaging, with value D or T. 
        
        
        
            [HD_INFO]
            index=8
            adj=ExtractFlag('HD')
            type=INTEGER
            comment=Marker is on high density genotyping kit (50K density or greater).  The snp may have phenotype associations present in dbGaP.
            
        
        specifies a field that is imported from the `HD` flag of column 8 with delimiter `;`. This is a common format when the annotations are created from the info column of a vcf file. 
        
        
        
        *   Example for a variant annotation database with multiple reference genomes: [dbNSFP.ann][3] 
        *   Example for a variant annotation database created from a .vcf file [thousandGenomes.ann][4] 
        *   Example for a field annotation database [keggPathway.ann][5]

 [1]: mailto:varianttools-user@lists.sourceforge.net
 [2]: http://docs.python.org/2/library/re.html#re.match
 [3]: http://vtools.houstonbioinformatics.org/annoDB/dbNSFP.ann
 [4]: http://vtools.houstonbioinformatics.org/annoDB/thousandGenomes.ann
 [5]: http://vtools.houstonbioinformatics.org/annoDB/keggPathway.ann