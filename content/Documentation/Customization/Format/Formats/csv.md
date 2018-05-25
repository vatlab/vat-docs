+++
title = "csv"
weight = 2
+++

## Importing and exporting variants in .csv (comma-separated value) format
### Format description

When this format is used to import data, it is similar to the [basic][1][?][1] format except that it assumes the use of commas, instead of tabs, as delimiters of the input format. 

When this format is used to export variants, it can be used to export arbitrary fields. The command and the resulting ouput are similar to that of the command `vtools output --delimiter ,` (output fields with a delimiter of comma), except that the `vtools export --format csv` command will properly quote field values when it contains comma, quotation mark etc. 



### Fields

    Format:                 csv
    Description:            Import variants (chr, pos, ref, alt) in csv format, or
      output arbitrary specified fields in csv format
    
    Columns:
      1                     Output all fields as one column
      2                     genotype
    Formatters are provided for fields: gt, *
    
    variant:
      chr                   Chromosome
      pos                   1-based position
      ref                   Reference allele, '-' for insertion.
      alt                   Alternative allele, '-' for deletion.
    
    Format parameters:
      chr_col               Column index for the chromosome field (default: 1)
      pos_col               Column index for the position field (default: 2)
      ref_col               Column index for the reference field (default: 3)
      alt_col               Column index for the alternative field (default: 4)
      pos_adj               Set to 1 if the input position is zero-based.
                            (default: 0)
      fields                Fields to output, simple arithmetics are allowed (e.g.
                            pos+1) but aggregation functions are not supported.
                            (default: chr,pos,ref,alt)
      order_by              Fields used to order output in ascending order.
                            (default: )
    



### Examples

#### Import variants (similar to format `<a class='createlinktext' rel='nofollow'
    href='http://localhost/~iceli/wiki/pmwiki.php?n=Format.Basic?action=edit'>basic</a><a rel='nofollow' 
    class='createlink' href='http://localhost/~iceli/wiki/pmwiki.php?n=Format.Basic?action=edit'>?</a>`)

    vtools import inputfile.txt --format csv --build hg18
    

This format assumes 1-based position for input files. If your input file uses zero-based position, you can use paramter `--pos_adj 1` to let variant tools adjust the position by 1. 



    vtools import inputfile.txt --format csv --pos_adj 1 --build hg18
    

This format supports parameters 

*   `chr_col` 
*   `pos_col` 
*   `ref_col` 
*   `alt_col` 

If, for example, your input file has columns `chr, start, end, ref, alt`, you can import from this file using command 



    vtools import inputfile.txt --format csv --ref_col 4 --alt_col 5 --build hg18
    



####x Export arbitrary fields and genotypes

The following command demonstrate how to export variants and a large number of annotation fields from different annotation databases, with a more descriptive header added to the output file. To repeat this command, you will need to update a variant table with number of variants in cases and controls, mean quality scores (fields `case_num`, `ctrl_num`, `mean_Q_indel`, `mean_Q_gt`, obtained using command `vtools update --from_stat`), and use all relevant annotation databases (`refGene`, `thousandGenomes`, `dbSNP`, and `dbNSFP`). 



    vtools export selected_variants --format csv --fields chr pos ref alt refGene.name2 case_num ctrl_num \
            GMAF_INFO dbSNP.name dbSNP.func SIFT_score PolyPhen2_score mean_Q_indel mean_Q_gt \
        --order_by chr pos \
        --header chr pos ref alt 'gene name' '# in cases' '# in ctrl' \
            'allele freq in 1000 genomes' 'dbSNP ID' 'func (dbSNP)' 'SIFT score' \
            'PolyPhen2 score' 'mean Quality score (indel)' 'mean Quality score (SNV)' \
        > selected_variants.csv
    

If you also need to export genotype, you can use a command similar to 



    vtools export selected_variants --format csv --samples 1 --fields chr pos ref alt refGene.name2 case_num ctrl_num \
            GMAF_INFO dbSNP.name dbSNP.func SIFT_score PolyPhen2_score mean_Q_indel mean_Q_gt \
        --order_by chr pos \
        --header chr pos ref alt 'gene name' '# in cases' '# in ctrl' \
            'allele freq in 1000 genomes' 'dbSNP ID' 'func (dbSNP)' 'SIFT score' \
            'PolyPhen2 score' 'mean Quality score (indel)' 'mean Quality score (SNV)' \
            '%(sample_names)s' \
        > selected_variants.csv
    

Note here the use of `--samples 1` to select all samples by condition `1` (true),, and the use of `%(sample_names)s` in the header to list all sample names.

 [1]: http://localhost/~iceli/wiki/pmwiki.php?n=Format.Basic?action=edit
