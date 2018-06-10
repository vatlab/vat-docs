+++
title = "cumtomized"
weight = 5
+++

## Specification of external file formats 

### 1. Roles of format specification in variant tools:

Variant tools can import and export text files (or gzipped text files) in **delimiter-separated format**, namely records that are separated into columns by delimiters such as tab, space or comma. The file format must be **variant-oriented** (storing one or more variants by line), with the exception of sample-based PLINK format which is preprocessed internally into variant-oriented form for import. We use terms 

*   **column** for columns (text) in a delimiter-separated file, and 
*   **field** for fields (with types) in tables in a database, with 
    *   **variant** fields for fields that define variants (`chr`, `pos`, `ref`, `alt`), 
    *   **variant info** for fields that annotate variants (e.g. membership to dbSNP), 
    *   **genotype** fields for fields to store genotypes of samples, and 
    *   **genotype info** for fields that annotate genotypes (e.g. quality score of each genotype) 

A format specification defines how to extract fields from columns and how to write columns from fields, to 



*   **Insert new variants to the project using command `vtools import`**. The text file should provide at least four *fields* for chromosome, position, reference and alternative alleles. In addition to variant and variant info, an input file can contain genotype and genotype info for one or more samples. 



The four *fields* could, but not necessarily have to, be in four *columns* because a field could be synthesized from multiple columns, even not from any existing column. For example, if all variants are from dbSNP, `ref` and `alt` fields could be looked up from a dbSNP annotation database. 



*   **Update existing variants with additional info using command `vtools update`**. The text files can have 
    
    *   full variant information (`chr`, `pos`, `ref` and `alt`) to update matching variants and related genotypes and their info, or 
    
    *   chromosomal positions (`chr` and `pos`) to update all variants at specified locations, or 
    
    *   range (`chr`, `start`, `end`) to update variants in specified regions 
    

*   **Export samples and their variants using command `vtools export`**. The file format should be organized by variant (not by sample). Although each line of the output file usually present a variant (`chr`, `pos`, `ref`, `alt`), it can contain multiple variants at a locus (`chr`, `pos`, `ref`, mutliple alternative alleles), or only locus-specific information (`chr`, `pos`). 



### 2. The format specification file (`.fmt` file)

A `.fmt` file describes the format of an external file so that it can be handled by variant tools. An format specification file follows an extended `.ini` format with section and key/value pairs. Details of this format can be found at [this link][1] because it is parsed by a Python ConfigParser object. This file should have at least a `[format description]` section and a few `field` sections. A format specification could be used to import and export files but you can ignore import or export specifications if you are only interested in exporting or importing. 



#### 2.1 Section `[format description]`

This section should have keys 



*   `description`: a description of the format, with preferably a URL to the documentation of the format. 

*   `encoding` (optional): encoding of the input file. If you see errors such as `"codec can't decode byte 0xe7 in position 21480"`, you should perhaps add `encoding=ISO-8859-1` to your `.fmt` file. 

*   `delimiter` (optional): delimiter to define columns in the input file. Default to tab (`delimiter='\t'`). If your input can be either tab or space delimited, use `delimiter=None` if your input does not have any missing field because `'\t\t'` or `'  '` will be treated as a single delimiter. Quotations around other delimiters can be ignored (e.g. `,` instead of `','`). 

*   `header` (optional): variant tools by default treats lines with a leading `#` as header and skip them during data importing. The header will also be used to probe sample names for some formats (e.g. .vcf). If your input file does not use such a header, you can override this behavior by specifying the number of lines to skip (`header=1`), or a pattern by which headers are matched (e.g. use `header=^%.*` for header lines starting with `%`, see [documents of the Python re package][2] for details). 

*   `preprocessor` (optional): a functor to pre-process input data into some intermediate format that can be readily imported by variant tools (e.g., `PlinkConverter()`) 

*   `export_by` (optional, for export only): How variants at the same locus are exported. By default, variant tools exports one line for each variant. If fields specified by `export_by` (e.g. `chr`, `pos`) cannot uniquely identify variants so multiple variants will be outputted in one line, values at extra records will be ignored, or be collapsed to the first record if supported by column specification. 

*   `sort_output_by` (optional, for export only): How variants are ordered. This option is ignored if `export_by` is defined. 

THIS OPTION IS CURRENTLY NOT USED 



*   `merge_by` (optional, for import only): If genotype at different homozygous copies (ploidy) is recorded in separate lines, this option has to be used to specify the columns to uniquely identify a variant. These columns will be passed to the processor without modification, values at all other columns are merged (separated by ','). 

*   One of 
    
    *   `variant`: fields for `chr`, `pos`, `ref`, and `alt`. Such input files have complete variant information and can be used to add new variants or add or update info of existing variants. 
    
    *   `position`: fields for `chr` and `pos` for chromosomal positions. 
    
    *   `range`: fields for `chr`, `start` and `end` positions of regions. 



input files of the latter two types can only be used to update matching variants with additional `variant_info`. 



*   `variant_info` (optional): Additional fields that will be inserted to specified variant table. 

*   `genotype` (optional): name of a field that will be imported into the sample variant table. Using a slice-index syntax, this field can process genotypes for multiple samples (e.g. `index=8:` will produce genotypes from columns 8, 9, ...). The return value of this field must be value `1` for heterozygote, `2` for homozygote, and `-1` for double heterozygote (alt1, alt2). 

*   `genotype_info` (optional): Fields such as quality score that will be appended to genotype of each sample. They should either generate a single value for all samples (regular index), or a different value for each sample (slice-index). 

General speaking, genotype info fields are sample specific so different samples can have different values for the same variant. Variant info fields are supposed to be properties of variants and are shared by all (or part of the) samples. It is up to the user (and file format) to decide how to handle particular fields from input files. 



#### 2.2 Section `[DEFAULT]` (define parameters of a format)

The default section defines values that exist, conceptually, in all sections. It is used to define parameters used for import or export. These parameters could be overriden using corresponding command line option. For example, in the following .fmt file (partial) 



    [format description]
    description=Output from ANNOVAR, generated from command "path/to/annovar/annotate_variation.pl annovar.txt path/to/annovar/humandb/". This format imports chr, pos, ref, alt and ANNOVAR annotations. For details please refer to http://www.openbioinformatics.org/annovar/annovar_gene.html
    variant=chr, pos, ref, alt
    variant_info=%(var_info)s
    
    [DEFAULT]
    var_info=mut_type
    var_info_comment=Fields to be outputted, can be one or both of mut_type and function
    

The key `var_info` has a help message defined by parameter `var_info_comment`, and a default value `mut_type`. If you query the details of this format using command 



    % vtools show format ANNOVAR_output
    

you will see at the end of the output the following description: 



    Other fields (usable through parameters):
      function     the gene name, the transcript identifier and the sequence change in
                   the corresponding transcript
    
    Format parameters:
      var_info     Fields to be outputted, can be one or both of mut_type and function.
                   (default: mut_type)
    

This means you can pass an alternative value of `var_info` to this format using parameters such as `--var_info function` to change the variant information field to be imported or updated. For example, you can use command 



    % vtools update variant input_file --format ANNOVAR_output --var_info mut_type function 
    

to update two fields `mut_type` and `function` instead of the default one (`mut_type`). 



Name of a variable cannot be any keyword (e.g. `field`, `comment`, `adj`, `type`) or start with `fmt_`. 



#### 2.3 Field sections (import: how to extract fields from input file)

Import fields sections describe the fields that can be imported if they appear in one of `variant`, `position`, `range`, `variant_info`, `genotype` and `genotype_info`. Because the value of these fields could be overridden using corresponding parameters of command `vtools import`, a `.fmt` file might define additional or alternative fields to provide alternative ways to import data in this format. 

Each field section can have the following keys: 



*   `index`: index(es) of field, which can be 
    
    *   A 1-based index of the column in the input file. The value at this column will be used for this field. 
    
    *   A tuple syntax with multiple indexes separated by `','`, for example `5,7`. A list of values at specified columns will be passed to an adjust function to produce values of the field. 
    
    *   A 'slice' syntax to specify multiple fields. This syntax will only be used for genotype and genotype information fields. For example, `index=8:` will produce multiple fields from columns `8, 9, ...` till end of the columns. Other examples include `index=8::2` for `8, 10, 12, ...`, `index=5,8:` for `(5,8)`, `(5,9)`, ..., and `index=8::2,9::2` for `(8,9)`, `(10,11)`, etc 
    

*   `type`: can be any SQL allowed types such as "INTEGER", "FLOAT", "INTEGER NOT NULL", or "DECIMAL(7,6) NOT NULL" 

*   `comment` (optional) a description of the field 

*   `adj` (optional): Functions or functors to extract or modify one or more values from the field value. *variant tools* provides a number of functors to help the processing of different fields. For example, 
    
    *   **`IncreaseBy(inc=1)`** (increase value by `inc`). This is usually used to adjust 0-based position to 1-based position that is used by *variant tools*. 
    
    *   **`MapValue(map)`** (map value to another). This function is used to map input value to another one, for example, `MapValue({'het': '1', 'hom': '2'})` maps value 'het' to '1' and 'hom' to '2'. Note that the mapped values should be strings or `None`. 
    
    *   **`Nullify(val)`** (treat value as NULL). This is usually used to adjust input `NA` values to `NULL` in the database. 
    
    *   **`RemoveLeading(val)`** (remove leading characters). This is usually used to remove leading `chr` from inputs with chromosomes such as `chr1`, `chr2`, because *variant tools* only stores `1`, `2`, etc. 
    
    *   **`ExtractField(index, sep=';', default=None)`** (field of a column): Split the item by `sep` and return the `index`-th field (1-based). Return `default` if there are less than `index` fields. For example, `ExtractField(2, ':')` extracts `20` from `10:20:30`. 



*   Multiple functors/functions can be used sequentially. For example, `ExtractValue('CEU:'), ExtractField(1, '/')` extracts value `12` from `YRI:20/222;CEU:12/45` (the first extractor gets `12/45`, the second extractor gets `12`), and `ExtractValue('CEU:'), SplitField('/')` extracts values `12` and `45` from `YRI:20/222;CEU:12/45`. 

*   If none of the provided extractors can be used, you can define your own function. For example, `lambda x: x[6:].replace(",", "")` extracts `24000` from `COUNT=24,000`. You can also mix function with variant tools provided extractor `ExtractValue("COUNT="), lambda x: x.replace(",", "")])` to extract `24000` from values such as `ASD;COUNT=24,000;MAF=0.5`. 

*   If the return value of at least one of the fields is a tuple of more than one values (e.g. result from functor `SplitField`), multiple records will be generated from this line. Non-tuple values of other fields will be copied automatically. For example, if three fields have values `A1`, `(B1,)`, `(C1, C2)`, they will produce two records of `A1, B1, C1` and `A1, None, C2`. 

*   If you would like to exclude certain records, you can use `adj` to produce invalid records that will be excluded during importing. For example, a record with `None` alternative allele, or a field with `NOT NULL` type will be ignored, or a genotype with `None` mutation type will be ignored. 



#### 2.4 Section `[Field formatter]` (export: how to format fields for output)

This section specifies how to format fields when they are outputted to a file. Fields that are not listed in this section will be converted to string directly, unless a special wildcast formatter `fmt_*` is specified. This section should look like 



    [Field formatter]
    fmt_chr=Prepend('chr')
    fmt_freq=Formatter('{.3f}')
    fmt_id=ValueOfNull('.')
    fmt_other=lambda x: something
    

The name of the formatter should be field name prepended by `fmt_`. Formatter for each field should be a functor or a function. Their return value must be a string. More interestingly, multiple fields could be formatted altogether so it is possible to specify 



    fmt_PL1,fmt_PL2,fmt_PL3=lambda x: x[0] + x[1] + x[2]
    

to create a single string from multiple fields. 



#### 2.5 Column sections (export: how to organize fields into columns of output file)

Export reverses the import process. Instead of extracting fields from one or more columns, it generates columns from one or more fields. Column sections have title `col_#` where `#` is the index of column. They are specified in a similar way to fields. File formats without column specification cannot be used to export variants and samples. 

Each column section can have the following keys: 



*   `field`: name of field or fields that will be used to create a column. The fields are usually defined in this .fmt file. If a field specifies genotype or genotype information of more than one sample using a slice syntax, multiple columns will be generated. If multiple records are collapsed into a single record(c.f. `export_by`), a tuple of values will be passed to the `adj` function/functor if it is defined. Otherwise, only the first record will be exported. 

*   `adj`: function or functor that accepts values at one or more fields and produce a single value at this column. 

*   `comment` (optional) a description of the column 



The basic steps of outputting a file is to collect values of all fields, apply formatters to each field (or groups of fields) if available, and collect results to columns. Note that 



*   Although fields of columns are usually the ones that are defined in a .fmt file, arbitrary fields could be outputted if fields of a column are configurable through parameters. 

*   A column is considered as a genotype column if it contains field `GT`. Multiple columns will be exported if genotypes of multiple samples are outputted. 

*   A field can generate multiple columns by using a formatter that returns, for example, '1,2' for a comma-separated format. 



### 3. Import and test

After a file is created, you can use command 



    vtools import --format /path/to/fmt_file input_file --build specified_build
    

to import your file, and use command 



    vtools show table variant -l -1
    

to check if variants are correctly imported. If you believe that your format is commonly used, please send the `.fmt` file to our [mailinglist][3]. We will post the file to the repository so that others can make use of it. 



### 4. Examples

You can learn from the system format files on how to define a format: 

*   A basic example of a format with variant fields: [ANNOVAR format][4]. 
*   An example of using lambda functions to extract information from multiple columns: [snps.txt created by CASAVA 1.8][5]. 

You can have a look at system format files using 



    vtools show formats
    vtools show format SOME_FORMAT
    more cache/SOME_FORMAT.fmt
    

The first command gets a list of supported formats. The second command gets details of a specific format, and the third command lets you view the format file because all used formats are stored in a temporary directory named `cache` under your project folder.

 [1]: http://docs.python.org/library/configparser.html
 [2]: http://docs.python.org/2/library/re.html#re.match
 [3]: mailto:varianttools-devel@lists.sourceforge.net
 [4]: http://vtools.houstonbioinformatics.org/format/ANNOVAR.fmt
 [5]: http://vtools.houstonbioinformatics.org/format/CASAVA18_snps.fmt
