# HomePage

## Import/Export adjustment functors

The following are all the adjustment functions that are provided by variant tools. The export functors are of course only used for exporting variants using `.fmt` files, and are not used in `.ann` files. 



### Adjust input

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



### Encode genotype

Variant tools ignores phase of genotype and stores `1` for heterozygote (alt/ref), `2` for homozygote (alt/alt), and `-1` for both variants (ref/alt1, ref/alt2) for genotype alt1/alt2. 



*   **`EncodeGenotype(default=None)`**, converting `1/1` -> `2` 



Convert genotype formats such as `0/1`, `0|1` etc in vcf format to mutation type. 



*   **`VcfGenotype(default=None)`**, converting `A/A;50` -> `2` 



Extract genotype as the first item of a field and return mutation type. This is a shortcut to `ExtractField(1, ';'), EncodeGenotype(default=None)`. For a .vcf file with multiple genotype columns, the index should be specified as `index=10:`. 



*   **`VcfGenoFromFormat(default=None)`**, converting `GT;DP, A/A;50` -> `2` 



Extract genotype field according to format specification and return mutation type. This is a shortcut to `FieldFromFormat('GT', ';'), EncodeGenotype(default=None)`. There should be two inputting columns, the first for FORMAT, the second for value. Fields defined by this functor is used to extract genotype from a .vcf file that does not put genotype as the first field. 



This field requires two input columns, the first one for format, and the second one for genotype field. For a typical .vcf file with multiple samples, this field should have `index=9,10:` in order to get format string from column 9, and values from columns 10, 11, .... 



### Extract values from a field

*   **`ExtractFlag(name, sep=';')`**, converting `SD:SF1:NS=1` -> `1` 



Split the value by `sep`, return `1` if it contains `name` and `` otherwise. 



*   **`ExtractField(index, sep=';', default=None)`**, converting `10;20:30` -> `20` 



Split the value by `sep` and return the `index`-th field (1-based). Return `default` if there are less than `index` fields. For example, `ExtractField(2, ':')` extracts `20` from `10:20:30`. 



*   **`ExtractValue(name, sep=';', default=None)`**, converting `AS;MAF=0.4;dbSNP` -> `0.4` 



Split the value by `sep`, return the rest of an item if it starts with `name`. For example, functor `ExtractValue('MAF=')` extracts `0.4` from `AS;MAF=0.4;dbSNP`. 



*   **`FieldFromFormat(name, sep=';', default=None)`,** converting `GT;DP, A/A;50` -> `50` 



Get the format from the first column and extract the corresponding field from the second column. This is used to extract genotype info according to FORMAT column of a vcf file. There should be two input columns, the first for FORMAT, the second for value. 



This field requires two input columns, the first one for format, and the second one for genotype field. For a typical .vcf file with multiple samples, this field should have `index=9,10:` in order to get format from column 9, and values from columns 10, 11, .... 



### Produce multiple records

*   **`SplitField(sep=',')`**, converting `0.4,0.6` -> `(0.4, 0.6)` 



This functor split value at a column to a tuple of multiple items, which will lead to multiple records if there are more than one items. 



*   **`CheckSplit(sep=',')`**, converting `A`->`A`, `A,T`->`(A, T)` 



This functor returns a tuple if there are multiple fields (the same as `SplitField`), and the item itself if it contains only one field (different from `SplitField`). This functor is used when you would like to copy an value to multiple records if there is a single item, and spread the items to multiple records if there are more than one item. 



### Retrieve information from annotation database.

*   **`FieldFromDB(dbfile, res_field, cond_fields, default=None)`**, obtaining reference allele from chromosome and position. 



This functor accepts an annotation database, and returns value of a field by querying the database with inputted values. For example `FieldFromDB("dbSNP.DB", "refNCBI", "chr,start")` with `index=1,2` will feed the functor with chromosome and start position from columns 1 and 2 of the input file. The querier will run a query similar to `SELECT refNCBI FROM dbSNP WHERE chr=? AND start=?` for each input value of chromosome and position, and use the result as the value of this field. A default value will be returned if no record is found, which will most likely invalidate the whole record (because of no reference allele in this case). 



### Connecting multiple functors and lambda functions

*   **`func1, func2`**, converting `AS=2/3;BD=5` to `3` 



When multiple functors (or lambda functions) are provided, the output of the first functor will be sent to the second, and so on. If a tuple is returned by one of the functors, the following functors will be applied to items in the tuple one by one. For example, `SplitField(','), IncreaseBy(1)` will convert `2,3,4` to `(2, 3, 4)`, and then `(3, 4, 5)`. Output values of other types (including list) are passed directly to the next functor/function, although there is no guarantee that the latter functor/function can handle such an input value. 



### Adjust output

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
