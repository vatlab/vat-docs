+++
title = "Formats"
weight = 2
hidden = "true"
+++

## Supported import/update/export file formats

*variant tools* uses file format specification files (`.fmt`) files to describe file formats so that commands such as `vtools import`, `vtools update` and `vtools export` know how to import data from and export data to files in such formats. 

*   *variant tools* can **import** variants, variant info fields, genotypes, and genotype info fields from a file. The file must contain information about *variants* (chr, pos, ref, alt), although *variant tools* is able to obtain information from other sources if some of the variant info fields are missing. (For example, variant tools can retrieve reference alleles from a reference genome). 
*   *variant tools* can **update** variant info fields and genotype info fields for existing variants and genotypes. The file can be variant-based (contains chr, pos, ref and alt), position-based (contains chra and pos), and range-based (contains chr, starting and ending positions). In the latter cases, a record in the input file can update multiple variants at the specified location or range. 
*   *variant tools* can **export** variants, variant info fields, genotypes, and genotype info fields to a file. The format description file must define `columns`, which specify what and in which format to export to each column of the output file. 

*variant tools* can import and export data in the following formats. We try to update descriptions of these formats as soon as possible but please use commands such as 



    % vtools show formats
    % vtools show format basic


to get the most updated information about these formats. 





| **Name** | **Import** | **Update** | **Export** | **Comment**  |            
|---------------|----------------|-------------------|-----------------------|-----------------------|    
| [basic][1] | Y  |  a  | Y | Import variants in tab-delimited format, export variants and optional variant info fields and genotypes| 
| VCF   | Y   | Y  | Y | [Variant Call Format][2] (VCF version 4.0 and 4.1) |
| [CSV][3]           | Y   |       | Y   | csv format    |                                
| [ANNOVAR][4]     |         |         | Y     | Format of ANNOVAR input file.  |
| [ANNOVAR\_variant\_function][5]  | Y     |     |   | used to imported annotations from ANNOVAR.variant\_function files. |
| [ANNOVAR\_exonic\_variant\_function][5] | Y|    |  | imports annotations from files generated from ANNOVAR of the form.exonic\_variant\_function. |
| [CASAVA18\_snps][6]   | Y   |     |     | Illumina snps.txt format|
| [CASAVA18\_indels][7] | Y   |    |  | indels.txt from Illumina    |
| [CGA][8]  | Y  |    |   | Complete Genomics CGA `masterVarBeta$ID.tsv.bz2` file  |
| [Pileup\_indel][9]   | Y   |  |     | Pileup Indel format |
| [MAP][10]  | Y    |   |  | Import variants from files with only chr and pos information. reference and alternative alleles are retrieved from dbSNP. |
| [PLINK][11] | Y | Y|  | Import variants and sample genotypes from PLINK file format. Currently only [PLINK binary file input][12] is supported.   |
| Polyphen2 | Y | | Y |Export data in Polyphen2 batch query, import information from results returned by the [polyphen2 batch query server][14]. |
| [TPED][15]    |    |    | Y   |                               |
| twoalleles  | Y  |     |  | Import alleles as allele 1 and 2, use a reference genome to determine which one is reference|
| [rsname][17]    | Y    |    |       | Import variants from rsnames, using the dbSNP database to query variants    |


Customize import/export format: 



*   Using [customized format specification][18] file (`.fmt`) to import/export arbitrary text format.

[1]: /  /documentation/customization/format/formats/txt/
[2]:  http://www.1000genomes.org/node/101
[3]: /  /documentation/customization/format/formats/csv/
[4]: /  /documentation/customization/format/formats/annovar/
[5]: /  /documentation/customization/format/formats/annovav/
[6]: /  /documentation/customization/format/formats/casava18snps/
[7]: /  /documentation/customization/format/formats/casava18indels/
[8]: /  /documentation/customization/format/formats/cga/
[9]: /  /documentation/customization/format/formats/cga/pileup/
[10]: /  /documentation/customization/format/formats/map/
[11]: /  /documentation/customization/format/formats/plink/
[12]: http://pngu.mgh.harvard.edu/~purcell/plink/binary.shtml
[14]: http://genetics.bwh.harvard.edu/pph2/bgi.shtml
[15]: /  /documentation/customization/format/formats/tped
[17]: /  /documentation/customization/format/formats/rsname/
[18]:/  /documentation/customization/format/formats/new/
