

+++
title = "snpEff"
description = ""
weight = 6
+++


# Variant effect provided by snpEFF 



## Usage

This pipeline exports variants in VCF format, call snpEff to predict its effect, and import the result as an variant info field EFF. 



    % vtools show pipeline snpEff
    

    A pipeline to call snpEff to annotate variants.
    
    Available pipelines: eff
    
    Pipeline "eff":  This pipeline export variants in VCF format, call snpEff to
    annotate it, and import the EFF info as an information field. This pipeline will
    automatically download appropriate snpEff database (e.g. hg19).
      eff_0:              Load specified snapshot if a snapshot is specified. Otherwise
                          use the existing project.
      eff_10:             Check the existence of command java
      eff_11:             Check if snpEff is installed and executable
      eff_12:             Check the data storage location in snpEff.config file.
      eff_14:             Download reference database for the project reference genome
      eff_20:             Export variants in VCF format
      eff_30:             Execute snpEff eff to annotate variants
      eff_40:             Importing results from snpEff
    
    Pipeline parameters:
      var_table           Variant table for the variants to be analyzed. (default:
                          variant)
      java                path to java. Default to 'java' (use $PATH to determine actual
                          path) (default: java)
      opt_java            Option to java program. -Djava.io.tmpdir is frequently used to
                          set java temporary directory if system temporary partition is
                          not big enough. (default: -Xmx4g -XX:-UseGCOverheadLimit)
      snpeff_path         Path to directory that contains snpEff.jar. (default: ./)
      eff_fields          Fields that will be imported to the project from the output of
                          snpEff. The default value is EFF, which is the whole EFF info.
                          You can also specify one or more off EFF_Type, EFF_Impact and
                          Eff_Functional_Class, which are from extracted from the
                          Effect(Effct_impact|Functional_Class... field. (default: EFF)
    



## Details

This pipeline calls `snpEff` to estimate the effect of variants so you first need to download and install `snpEff`. 



    % vtools execute snpEff eff --snpeff_path ~/bin/snpEff/
    

    INFO: Executing step eff_0 of pipeline snpEff: Load specified snapshot if a snapshot is specified. Otherwise use the existing project.
    INFO: Executing step eff_10 of pipeline snpEff: Check the existence of command java
    INFO: Command java is located.
    INFO: Executing step eff_11 of pipeline snpEff: Check if snpEff is installed and executable
    INFO: Executing step eff_12 of pipeline snpEff: Check the data storage location in snpEff.config file.
    INFO: Running cat /Users/bpeng/bin/snpEff//snpEff.config | grep "data_dir =" | cut -d= -f2 > cache/snpEff.data_dir
    INFO: Command "cat /Users/bpeng/bin/snpEff//snpEff.config | grep "data_dir =" | cut -d= -f2 > cache/snpEff.data_dir" completed successfully in 00:00:01
    INFO: Executing step eff_14 of pipeline snpEff: Download reference database for the project reference genome
    INFO: Reuse existing files /Users/bpeng/snpEff/data//hg19/snpEffectPredictor.bin
    INFO: Executing step eff_20 of pipeline snpEff: Export variants in VCF format
    INFO: Running vtools export variant --format vcf --output cache/snpEff_input.vcf
    INFO: Command "vtools export variant --format vcf --output cache/snpEff_input.vcf" completed successfully in 00:00:01
    INFO: Executing step eff_30 of pipeline snpEff: Execute snpEff eff to annotate variants
    INFO: Running java -jar /Users/bpeng/bin/snpEff//snpEff.jar -c /Users/bpeng/bin/snpEff//snpEff.config -v hg19 cache/snpEff_input.vcf > cache/snpEff_output.vcf
    INFO: Command "java -jar /Users/bpeng/bin/snpEff//snpEff.jar -c /Users/bpeng/bin/snpEff//snpEff.config -v hg19 cache/snpEff_input.vcf > cache/snpEff_output.vcf" completed successfully in 00:00:34
    INFO: Executing step eff_40 of pipeline snpEff: Importing results from snpEff
    INFO: Running vtools update variant --from_file cache/snpEff_output.vcf --var_info EFF
    INFO: Using primary reference genome hg19 of the project.
    Getting existing variants: 100% [===========================================] 1,611 181.8K/s in 00:00:00
    INFO: Updating variants from cache/snpEff_output.vcf (1/1)
    snpEff_output.vcf: 100% [====================================================] 1,610 12.3K/s in 00:00:00
    INFO: Field EFF of 1,611 variants are updated
    INFO: Command "vtools update variant --from_file cache/snpEff_output.vcf --var_info EFF" completed successfully in 00:00:01
    

The field `EFF` is added to (or updated if it already exists) the project, 



    % vtools output variant chr pos ref alt EFF -l 10
    

    6	32797167	A	G	INTRON(MODIFIER||||653|TAP2||CODING|NM_018833.2.8|11|1),INTRON(MODIFIER||||703|TAP2||CODING|NM_000544.3.8|11|1)
    6	32369594	A	G	INTRON(MODIFIER||||455|BTNL2||CODING|NM_019602.1.8|3|1)
    6	32797947	A	G	INTRON(MODIFIER||||653|TAP2||CODING|NM_018833.2.8|9|1),INTRON(MODIFIER||||703|TAP2||CODING|NM_000544.3.8|9|1)
    6	32797168	A	G	INTRON(MODIFIER||||653|TAP2||CODING|NM_018833.2.8|11|1),INTRON(MODIFIER||||703|TAP2||CODING|NM_000544.3.8|11|1)
    6	31380276	A	G	INTRON(MODIFIER||||332|MICA||CODING|NM_001177519.1.4|5|1),INTRON(MODIFIER||||383|MICA||CODING|NM_000247.1.5|6|1),INTRON(MODIFIER|||||MICA||CODING|NR_036523.1.5|5|1),INTRON(MODIFIER|||||MICA||CODING|NR_036524.1.4|5|1)
    6	32369554	A	G	INTRON(MODIFIER||||455|BTNL2||CODING|NM_019602.1.8|4|1)
    6	32369596	A	G	INTRON(MODIFIER||||455|BTNL2||CODING|NM_019602.1.8|3|1)
    6	32369597	A	G	INTRON(MODIFIER||||455|BTNL2||CODING|NM_019602.1.8|3|1)
    6	32369515	A	G	INTRON(MODIFIER||||455|BTNL2||CODING|NM_019602.1.8|4|1)
    6	31380278	A	G	INTRON(MODIFIER||||332|MICA||CODING|NM_001177519.1.4|5|1),INTRON(MODIFIER||||383|MICA||CODING|NM_000247.1.5|6|1),INTRON(MODIFIER|||||MICA||CODING|NR_036523.1.5|5|1),INTRON(MODIFIER|||||MICA||CODING|NR_036524.1.4|5|1)