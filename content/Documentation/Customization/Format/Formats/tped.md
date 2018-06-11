+++
title = "tped"
weight = 6
+++

## PLINK/TPED format 



### 1. About TPED format

Many software applications for linkage and association studies (e.g. [plink][1], [merlin][2]) accept PED/MAP format. The map file records basic information about markers, the Ped file contains sample genotype. Whereas variant tools can easily export in MAP format, it is difficult to export in PED format because this format is not variant oriented (output by variant). 

Fortunately, PLINK accepts a transposed PED format (TPED) that is variant oriented. variant tools can export variants in this format using format `tped`. 



Format `tped` cannot import from TPED files because this format does not specify reference and alternative alleles. To import PLINK TPED data please use [format `plink`][3] 



#### 1.1 The TPED/TFAM bundle

To make the exported TPED file compatible with other software applications that handles PLINK input, a TFAM file containing individual names is generated. Unlike a standard TFAM file which is the first six columns of a PED file, i.e., Family ID, Individual ID, Paternal ID, Maternal ID, Sex and Phenotype, the TFAM file exported here only has valid individual ID, with other columns being placeholders. However it is straightforward to create a TFAM file with information for other columns using `vtools phenotype --output` command. 



### 2. Format specification

    vtools show format tped
    
    Format:      tped
    Description: Output to TPED format with the first four columns chr name gen_pos
      pos, and the rest for genotypes. Variant tools cannot import from
      this format because it does not contain information about reference
      genome.
    
    Columns:
      1            chromosome (without leading chr)
      2            Locus name
      3            Genetic distance, left empty
      4            Physical position
      5            genotype
    Formatters are provided for fields: gt
    
    variant:
      chr          Chromosome
      pos          1-based position
      ref          
      alt          
    
    Format parameters:
      name         (export) Field for name of variants, can be dbSNP.name if dbSNP is
                   available (default: )
      style        (export) Style of genotype format, can be 'genotype' for genotype
                   separated by tab (e.g. A C), or 'numeric' for 0, 1, or
                   2 for number of alternative alleles. (default:
                   genotype)
      tfamfile     (export) Name of the tfam file to be outputed. Filename that does not
                   ends with .tfam will be ignored. (default: $table.tfam)
    

By default, the corresponding TFAM file is named after the variant table from which variants/samples are exported. You can specify the TFAM file name by passing an additional parameter with specified filename: `--tfamfile FILENAME.tfam`. Note that the extension `.tfam` is required. 



### Example

Output some variants. The genotypes for selected samples are ordered alphabetically by sample name (and the selected samples are recorded in the log file). 



    vtools export variant --format tped --samples 'sample_name like "NA069%"' -v0
    

    1	.	.	10533	G	G	G	G	G	G
    1	.	.	51479	T	T	T	A	T	A
    1	.	.	51928	G	G	G	G	G	G
    1	.	.	54586	T	T	T	T	T	T
    1	.	.	54676	C	C	C	C	C	C
    1	.	.	54708	G	G	G	G	G	G
    1	.	.	55299	C	C	C	C	C	C
    1	.	.	62203	T	T	T	T	T	T
    1	.	.	63671	G	G	G	A	G	A
    1	.	.	86028	T	T	T	T	T	T
    1	.	.	86065	G	G	G	G	G	G
    1	.	.	86331	A	A	A	A	A	A
    1	.	.	87190	G	G	G	A	G	G
    1	.	.	88316	G	G	G	G	G	G
    1	.	.	88338	G	G	G	A	G	G
    1	.	.	91536	G	G	T	T	G	G
    1	.	.	108310	C	C	T	C	T	C
    1	.	.	233473	C	C	C	C	C	G
    1	.	.	234760	A	A	A	A	A	A
    

Export in numeric style. This will recode the tped file to a numeric format using additive coding, equivalent to applying the PLINK [`--recodeA`][4] command to the data: 



    vtools export variant --format tped --samples 'sample_name like "NA069%"' --style numeric -v0
    

    1	.	.	10533	0	0	0
    1	.	.	51479	0	1	1
    1	.	.	51928	0	0	0
    1	.	.	54586	0	0	0
    1	.	.	54676	0	0	0
    1	.	.	54708	0	0	0
    1	.	.	55299	0	0	0
    1	.	.	62203	0	0	0
    1	.	.	63671	0	1	1
    1	.	.	86028	0	0	0
    1	.	.	86065	0	0	0
    1	.	.	86331	0	0	0
    1	.	.	87190	0	1	0
    1	.	.	88316	0	0	0
    1	.	.	88338	0	1	0
    1	.	.	91536	0	2	0
    1	.	.	108310	2	1	1
    1	.	.	233473	0	0	1
    1	.	.	234760	0	0	0
    

The name field of the output is empty. If you would like to use an annotation database to assign variants a name, you can do 



    vtools use dbSNP
    vtools export variant --format tped --samples 'sample_name like "NA069%"' --name dbSNP.name  -v0
    

    1	rs114315702	.	10533	G	G	G	G	G	G
    1	rs116400033	.	51479	T	T	T	A	T	A
    1	rs78732933	.	51928	G	G	G	G	G	G
    1	rs79600414	.	54586	T	T	T	T	T	T
    1	rs2462492	.	54676	C	C	C	C	C	C
    1	rs115797567	.	54708	G	G	G	G	G	G
    1	rs10399749	.	55299	C	C	C	C	C	C
    1	rs28402963	.	62203	T	T	T	T	T	T
    1	rs80011619	.	63671	G	G	G	A	G	A
    1	rs114608975	.	86028	T	T	T	T	T	T
    1	rs116504101	.	86065	G	G	G	G	G	G
    1	rs115209712	.	86331	A	A	A	A	A	A
    1	rs1524602	.	87190	G	G	G	A	G	G
    1	rs113759966	.	88316	G	G	G	G	G	G
    1	rs55700207	.	88338	G	G	G	A	G	G
    1	rs6702460	.	91536	G	G	T	T	G	G
    1	rs74747225	.	108310	C	C	T	C	T	C
    1	rs112455420	.	233473	C	C	C	C	C	G
    1	rs7548182	.	234760	A	A	A	A	A	A
    



In case there are multiple entries for a variant in the dbSNP database, only the first name will be used, which does not have to be the most commonly used name for the variant. 

A TFAM file is also generated, 



    0	NA06985	0	0	0	-9
    1	NA06986	0	0	0	-9
    2	NA06994	0	0	0	-9
    3	NA06985	0	0	0	-9
    4	NA06986	0	0	0	-9
    5	NA06994	0	0	0	-9
    6	NA06985	0	0	0	-9
    7	NA06986	0	0	0	-9
    8	NA06994	0	0	0	-9

 [1]: http://pngu.mgh.harvard.edu/~purcell/plink/
 [2]: http://www.sph.umich.edu/csg/abecasis/Merlin/
 [3]: /  /documentation/customization/format/Formats/tped/plink/
 [4]: http://pngu.mgh.harvard.edu/~purcell/plink/dataman.shtml
