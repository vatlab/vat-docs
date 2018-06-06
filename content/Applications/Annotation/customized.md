
+++
title = "Customized"
weight = 2
+++





## Create annotation database 



{{%notice tip%}}
Because you write your own .ann file, please consider using pipelines in `anno_utils`, which can usually create `.ann` file from some data sources with pre-defined formats. 
{{%/notice%}}


### 1. Define a new annotation database

If you would like to use an annotation source that is not currently supported by variant tools, you could [send us and email][1] if the data source is publicly available, or write an annotation specification file to create your own annotation database. This file describes various aspects of an annotation database such as 

*   Type of annotation (variant, positional, range and field) 
*   The reference genome(s) it uses, 
*   Description of the database, including license and citation, 
*   Where to get the database and/or its source, and 
*   Fields that the annotation database will provide 

An annotation file follows a windows `.ini` format. It is divided into several sections, each with several `key=entry` lines. Lines that start with a `#` or `;` are comments and are ignored. Inline comments starts with `;`. An annotation file should always starts with line 



    #Variant tools schema version 1.0
    

An annotation file should have sections `linked fields` and `data sources`, followed by sections that describe each field. 



#### 1.1 Section `[linked fields]`

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



#### 1.2 Section `[data sources]`

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



#### 1.3 Field sections 

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
        
{{%notice tip%}}     
Multiple functors/functions can be used sequentially. For example, `ExtractValue('CEU:'), ExtractField(1, '/')` extracts value `12` from `YRI:20/222;CEU:12/45` (the first extractor gets `12/45`, the second extractor gets `12`), and `ExtractValue('CEU:'), SplitField('/')` extracts values `12` and `45` from `YRI:20/222;CEU:12/45`. 
{{%/notice%}}

{{%notice tip%}}
If none of the provided extractors can be used, you can define your own function. For example, `lambda x: x[6:].replace(",", "")` extracts `24000` from `COUNT=24,000`. You can also mix function with variant tools provided extractor `ExtractValue("COUNT="), lambda x: x.replace(",", "")])` to extract `24000` from values such as `ASD;COUNT=24,000;MAF=0.5`. 
{{%/notice%}}

{{%notice tip%}}
If the return value of at least one of the fields is a tuple of more than one values (e.g. result from functor `SplitField`), multiple records will be generated from this line. Non-tuple values of other fields will be copied automatically. For example, if three fields have values `A1`, `(B1,)`, `(C1, C2)`, they will produce two records of `A1, B1, C1` and `A1, None, C2`. 
{{%/notice%}}
 
{{%notice tip%}}
If you would like to exclude certain records, you can use `adj` to produce invalid records that will be excluded during importing. For example, a record with `None` alternative allele, or a field with `NOT NULL` type will be ignored, or a genotype with `None` mutation type will be ignored. 
{{%/notice%}}       
        
        
## 2. Import and test
        
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



### 3. Examples

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


### 4. Import/Export adjustment functors

The following are all the adjustment functions that are provided by variant tools. The export functors are of course only used for exporting variants using `.fmt` files, and are not used in `.ann` files. 



#### 4.1 Adjust input

*   **`IncreaseBy(inc=1)`**, converting `5` -> `6` 



Increase input integer value by `inc`. This is usually used to adjust 0-based position to 1-based position that is used by *variant tools*. 



*   `MapValue(map)`''', converting `A/A` -> `2` 



Map value to another. This function is used to map input value to another one, for example, `MapValue({'het': '1', 'hom': '2'})` maps value 'het' to '1' and 'hom' to '2'. The mapped values should be strings or `None`. The item itself will be returned if it cannot be mapped. 



*   `Nullify(val)`''', converting `NA` -> `None` 



Treat value as `NULL`'''. This is usually used to adjust input `NA` values to `NULL` in the database. Multiple NULL values are allowed (e.g. `Nullify(['NA', '.'])`). 



*   **`DiscardRecord(val, keepMatched=False)`**, discard records with (or without) val at specified field 



Discard the whole record if the file has `val`, or is one of `val` if `val` is a list at the specified column, or if val is evaluated to be True if `val` is a lambda function. If `keepMatched` is true, non-matching records will be discarded. For example, `DiscardRecord(lambda x: x.startswith('NC_'))` will discard all records with passed value starts with `NC_`. 



*   **`RemoveLeading(val)`**, converting `chr10` -> `10` 



Remove leading characters `val`. This is usually used to remove leading `chr` from inputs with chromosomes such as `chr1`, `chr2`, because *variant tools* only stores `1`, `2`, etc. 



#### 4.2 Encode genotype

Variant tools ignores phase of genotype and stores `1` for heterozygote (alt/ref), `2` for homozygote (alt/alt), and `-1` for both variants (ref/alt1, ref/alt2) for genotype alt1/alt2. 



*   **`EncodeGenotype(default=None)`**, converting `1/1` -> `2` 



Convert genotype formats such as `0/1`, `0|1` etc in vcf format to mutation type. 



*   **`VcfGenotype(default=None)`**, converting `A/A;50` -> `2` 



Extract genotype as the first item of a field and return mutation type. This is a shortcut to `ExtractField(1, ';'), EncodeGenotype(default=None)`. For a .vcf file with multiple genotype columns, the index should be specified as `index=10:`. 



*   **`VcfGenoFromFormat(default=None)`**, converting `GT;DP, A/A;50` -> `2` 



Extract genotype field according to format specification and return mutation type. This is a shortcut to `FieldFromFormat('GT', ';'), EncodeGenotype(default=None)`. There should be two inputting columns, the first for FORMAT, the second for value. Fields defined by this functor is used to extract genotype from a .vcf file that does not put genotype as the first field. 


{{%notice warning%}}
This field requires two input columns, the first one for format, and the second one for genotype field. For a typical .vcf file with multiple samples, this field should have `index=9,10:` in order to get format string from column 9, and values from columns 10, 11, .... s
{{%/notice%}}

#### 4.3 Extract values from a field

*   **`ExtractFlag(name, sep=';')`**, converting `SD:SF1:NS=1` -> `1` 



Split the value by `sep`, return `1` if it contains `name` and `` otherwise. 



*   **`ExtractField(index, sep=';', default=None)`**, converting `10;20:30` -> `20` 



Split the value by `sep` and return the `index`-th field (1-based). Return `default` if there are less than `index` fields. For example, `ExtractField(2, ':')` extracts `20` from `10:20:30`. 



*   **`ExtractValue(name, sep=';', default=None)`**, converting `AS;MAF=0.4;dbSNP` -> `0.4` 



Split the value by `sep`, return the rest of an item if it starts with `name`. For example, functor `ExtractValue('MAF=')` extracts `0.4` from `AS;MAF=0.4;dbSNP`. 



*   **`FieldFromFormat(name, sep=';', default=None)`,** converting `GT;DP, A/A;50` -> `50` 



Get the format from the first column and extract the corresponding field from the second column. This is used to extract genotype info according to FORMAT column of a vcf file. There should be two input columns, the first for FORMAT, the second for value. 


{{%notice warning%}}
This field requires two input columns, the first one for format, and the second one for genotype field. For a typical .vcf file with multiple samples, this field should have `index=9,10:` in order to get format from column 9, and values from columns 10, 11, .... 
{{%/notice%}}


#### 4.4 Produce multiple records

*   **`SplitField(sep=',')`**, converting `0.4,0.6` -> `(0.4, 0.6)` 



This functor split value at a column to a tuple of multiple items, which will lead to multiple records if there are more than one items. 



*   **`CheckSplit(sep=',')`**, converting `A`->`A`, `A,T`->`(A, T)` 



This functor returns a tuple if there are multiple fields (the same as `SplitField`), and the item itself if it contains only one field (different from `SplitField`). This functor is used when you would like to copy an value to multiple records if there is a single item, and spread the items to multiple records if there are more than one item. 



#### 4.5 Retrieve information from annotation database.

*   **`FieldFromDB(dbfile, res_field, cond_fields, default=None)`**, obtaining reference allele from chromosome and position. 



This functor accepts an annotation database, and returns value of a field by querying the database with inputted values. For example `FieldFromDB("dbSNP.DB", "refNCBI", "chr,start")` with `index=1,2` will feed the functor with chromosome and start position from columns 1 and 2 of the input file. The querier will run a query similar to `SELECT refNCBI FROM dbSNP WHERE chr=? AND start=?` for each input value of chromosome and position, and use the result as the value of this field. A default value will be returned if no record is found, which will most likely invalidate the whole record (because of no reference allele in this case). 



#### 4.6 Connecting multiple functors and lambda functions

*   **`func1, func2`**, converting `AS=2/3;BD=5` to `3` 



When multiple functors (or lambda functions) are provided, the output of the first functor will be sent to the second, and so on. If a tuple is returned by one of the functors, the following functors will be applied to items in the tuple one by one. For example, `SplitField(','), IncreaseBy(1)` will convert `2,3,4` to `(2, 3, 4)`, and then `(3, 4, 5)`. Output values of other types (including list) are passed directly to the next functor/function, although there is no guarantee that the latter functor/function can handle such an input value. 



#### 4.7 Adjust output

*   **`JoinFields(sep=',')`**, converting `field1` `field2` -> `field1,field2` 



This functor joins multiple items in different fields into one field. The items are separated by specified delimiter. 



*   **`IfMulti(ifFunc=None, elseFunc=None)`** 

*   **`ValueOfNull(val)`**, converting `NULL`->`val` 



Treat NULL values as specified value. This is usually used to adjust output NULL values to some symbols that the file format conventionally use. For example `ValueOfNull('PASS')` is applied to output filters for qualified variants, and `ValueOfNull('.')` for missing genotypes. 



*   **`Constant(val=CONSTANT_VAL)`**, converting `field_val`->`CONSTANT_VAL` 



Set a constant value to a field. 



*   **`SequentialCollector([..extractors..])`** 



Define an extractor that calls a list of extractors. The string extracted from the first extractor will be passed to the second, and so on. 



*   **`CSVFormatter()`** 



Format any input as a field in a csv file. It will quote strings with `"`, `,` or newline. In the first case, it will also replace all instances of `"` to `""`. 



*   **`InfoFormatter(name, ignore='')`** 

Output value `val` in the format of `name=val`. Nothing will be outputted if item matches `ignore`. 



*   **`FlagFormatter(name)`** 

Output `name` if value is True, and `''` otherwise. 



*   **`GenoFormatter(style='genotype', **kwargs)`** 



This formatter determines how genotypes are outputted. 

*   `style='genotype'`: Output actual genotype. This style accepts paramters `sep` and `null` to specify how to join two genotypes, and what to use for null genotype for indels. For example, if `ref=A`, `alt=T`, `sep=','` (default is tab), this formatter returns `A,A`, `A,T`, `T,T`, and `T,-` for homozygous reference alleles, heterozygote, homozygous alternative alleles, and one of double alternative alleles, respectively. Missing data are represented by '`.`'. 

*   `style='numeric'`: Output number of alternative alleles. This style accepts parameter `base=0` and outputs ``, `1`, `2` (if `base=0` for homozygous reference alleles, heterozygote, homozygous alternative alleles. Genotypes with two different alternative alleles are also outputted as 2. Missing data are represented by '`NA`'. 

*   `style='vcf'`: output genotype in vcf format. For example `0/0` for homozygous reference alleles, `1/1` for homozygous alternative alleles, and `1/2` for two different alternative alleles. Missing data are represented by '`.`'. 

*   `style='plink'`: The same as style genotype but treat half-missing genotype (./A) as missing, and ignore all multi-allele variants. Missing data are represented by '``'.


 [1]: mailto:varianttools-user@lists.sourceforge.net
 [2]: http://docs.python.org/2/library/re.html#re.match
 [3]: http://vtools.houstonbioinformatics.org/annoDB/dbNSFP.ann
 [4]: http://vtools.houstonbioinformatics.org/annoDB/thousandGenomes.ann
 [5]: http://vtools.houstonbioinformatics.org/annoDB/keggPathway.ann