+++
title = "ANNNOVAR variants"
weight = 13
+++


## Generating and importing ANNOVAR annotations for variants in vtools

`vtools` supports the generation of an ANNOVAR input file through the `ANNOVAR.fmt` format. In addition, there are two ANNOVAR format files (`ANNOVAR_variant_function.fmt` and `ANNOVAR_exonic_variant_function.fmt`) that support the import of ANNOVAR generated annotations. 



### 1. Example of running annovar on variants in vtools and importing the resulting annotations

    # export all variants in the variant table to an annovar file (an input file for annovar)
    vtools export variant ANNOVAR.input --format ANNOVAR
    
    # run annovar to generate annotation files
    # see http://www.openbioinformatics.org/annovar/ for help
    perl annotate_variation.pl -geneanno ANNOVAR.input -buildver hg19 humandb/
    
    # import annovar annotations using a separate format for each of the two annovar annotation files
    vtools update variant --format ANNOVAR_exonic_variant_function --from_file ANNOVAR.input.exonic_variant_function --var_info mut_type function genename
    vtools update variant --format ANNOVAR_variant_function --from_file ANNOVAR.input.variant_function --var_info region_type region_name
    

You now have the following fields: `region_type, region_name, genename, mut_type, and function` added as annotations to your variants in vtools. 

A description of the used annotation files are below. 



### 2. ANNOVAR.fmt

    vtools show format ANNOVAR   

    Format:      ANNOVAR
    Description: Input format of ANNOVAR. No genotype is defined.
    
    Columns:
      1            chromosome
      2            position (1-based)
      3            end position
      4            reference allele
      5            alternative allele
      6            optional column
    
    variant:
      chr          Chromosome
      pos          1-based position
      ref          Reference allele, '-' for insertion.
      alt          Alternative allele, '-' for deletion.
    
    Format parameters:
      comment_string Output one or more fields to the optional comment column of this
                   format. (default: )
    



### 3. ANNOVAR\_variant\_function.fmt

    vtools show format ANNOVAR_variant_function   

    Format:      ANNOVAR_variant_function
    Description: Output from ANNOVAR for files of type "*.variant_function", generated
      from command "path/to/annovar/annotate_variation.pl annovar.txt
      path/to/annovar/humandb/". This format imports chr, pos, ref, alt
      and ANNOVAR annotations. For details please refer to
      http://www.openbioinformatics.org/annovar/annovar_gene.html
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr          Chromosome
      pos          1-based position
      ref          Reference allele, '-' for insertion.
      alt          Alternative allele, '-' for deletion.
    
    Variant info:
      region_type  The genomic region type (i.e., intergenic, ncRNA_intronic, etc) where
                   this variant lies.
    
    Other fields (usable through parameters):
      region_name  Genomic region name that corresponds to the region_type.  If the
                   variant lies in an intergenic region, this field will
                   specify the closest known regions upstream and
                   downstream of this variant.
    
    Format parameters:
      var_info     Fields to be outputted, can be one or both of region_type and
                   region_name. (default: region_type)
    



### 4. ANNOVAR\_exonic\_variant_function.fmt

    vtools show format ANNOVAR_exonic_variant_function
    
    Format:      ANNOVAR_exonic_variant_function
    Description: Output from ANNOVAR, generated from command
      "path/to/annovar/annotate_variation.pl annovar.txt
      path/to/annovar/humandb/". This format imports chr, pos, ref, alt
      and ANNOVAR annotations. For details please refer to
      http://www.openbioinformatics.org/annovar/annovar_gene.html
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr          Chromosome
      pos          1-based position
      ref          Reference allele, '-' for insertion.
      alt          Alternative allele, '-' for deletion.
    
    Variant info:
      mut_type     the functional consequences of the variant.
    
    Other fields (usable through parameters):
      genename     Gene name (for the first exon if the variant is in more than one
                   exons, but usually the names for all exons are the
                   same).
      function     the gene name, the transcript identifier and the sequence change in
                   the corresponding transcript
    
    Format parameters:
      var_info     Fields to be outputted, can be one or both of mut_type and function.
                   (default: mut_type)
