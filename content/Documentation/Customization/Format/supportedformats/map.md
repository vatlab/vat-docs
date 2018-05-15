+++
title = "map"
weight = 4
+++

## Import variants from file without ref and alt alleles 

## Introduction

From time to time, you might get a list of variants in map format, or as a list with only chromosome and position information. Reference and alternative alleles are not specified because the variants are from GWA studies with well-defined reference and alternative alleles. In this case, you can use format `map`, which automatically retrieve reference and alternative alleles from a specified dbSNP database. 



## Format specification

    vtools show format format/map.fmt
    

    Format:      map
    Description: This input format imports variants from files in MAP format (with
      columns chr, name gen_dist, pos), or any delimiter-separated format
      with columns chr and pos. Because these input files do not contain
      reference and alternative alleles of variants, this format queries
      such information from the dbSNP database using chr and pos. Records
      that does not exist in dbSNP will be discarded. Records with
      multiple alternative alleles will lead to multiple records.
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr          Chromosome
      pos          1-based position
      ref          Reference allele, '-' for insertion.
      alt          Alternative allele obtained from another database
    
    Format parameters:
      db_file       (default: dbSNP.DB)
      pos_idx      Index of column for pyhysical location in the map file, should be 4
                   for a standard map file with chr, pos, gen_dist, pos.
                   (default: 4)
      ref_field    Name of ref field from the annotation database, used to retrieve
                   reference allele at specified location. (default:
                   refNCBI)
      alt_field    Name of alt field from the annotation database, used to retrieve
                   alternative allele at specified location. (default:
                   alt)
      chr_field    Name of chr field from the annotation database, used to locate
                   variants from the dbSNP database. (default: chr)
      pos_field    Name of pos field from the annotation database, used to locate
                   variants from the dbSNP database. (default: start)
      separator    Separator of the input file, default to space or tab. (default: None)
    
    



## Examples

You are given a list of variants with chromosome as the first column, and physical position as the third column: 



    CHR	SNP	BP	A1
    12	rs11054701	12180423	C
    12	rs2075241	12182746	C
    12	rs2160521	12184905	T
    12	rs10590349	12223570	G
    12	rs10492120	12224619	C
    12	rs3825258	12170662	C
    12	rs11054697	12163740	C
    12	rs16907786	12205869	A
    12	rs11054665	12113442	G
    



### Download `dbSNP`

The first step is to get the right version of dbSNP. Because the variants are in hg18, you cannot use the default version of dbSNP, which uses hg19. Instead, you should run 



    vtools show annotations
    vtools use dbSNP-hg18_130
    

The first command lists all available annotation databases, and the second command will download dbSNP and put a database such as `dbSNP-hg18_130.DB` under your project directory. 



### Import and filter variants

The default column for the position column is 4, but the input file has it at the third column, so you will need to use parameter `--pos_idx 3`. You do not have to set other parameters (fields) if you are using dbSNP database provided by variant tools. 

To import the data, you can run command 



    vtools import gwas_result.txt --format map --db_file dbSNP-hg18_130.DB \
      --pos_idx 3 --build hg18
    

This format will import multiple variants if there are multiple variants (usually SNV and indels) at the same location at dbSNP. For example, you can get one SNV and two deletions at position 12223570 of chromosome 12 in the following example. 



    vtools output variant chr pos dbSNP.name ref alt 
    

    12	12180423	rs11054701	T	C
    12	12182746	rs2075241	G	C
    12	12184905	rs2160521	C	T
    12	12223570	rs7974059	G	T
    12	12223570	rs10590349	GATA	-
    12	12223570	rs56097732	GA	-
    12	12224619	rs10492120	C	T
    12	12170662	rs3825258	T	C
    12	12163740	rs11054697	T	C
    12	12205869	rs16907786	G	A
    12	12113442	rs11054665	T	G
    

If you believe that all your variants are SNVs, you can run 



    vtools select variant 'ref != "-"' 'alt != "-"' -t SNV
    

to put all SNVs into a separate table, or run 



    vtools select variant 'ref = "-" OR alt = "-"' -t indels
    vtools remove variants indels
    

to remove all indels. 



This format will ignore all variants that are not in dbSNP. If you would like to keep them, you can modify `map.fmt`, and add parameter `default='-'` to `DatabaseQuerier`.
