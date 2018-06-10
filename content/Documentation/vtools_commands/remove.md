+++
title = "remove"
description = ""
weight = 14
+++





## Remove project, variant table, fields and others



### 1. Usage

    % vtools remove -h
    
    usage: vtools remove [-h] [-v STD[LOG]]
    
                         {project,tables,samples,fields,geno_fields,annotations,variants,genotypes,phenotypes}
                         [items [items ...]]
    
    Remove from the current project various items such as variants genotypes, and
    annotation fields.
    
    positional arguments:
      {project,tables,samples,fields,geno_fields,annotations,variants,genotypes,phenotypes}
                            Type of items to be removed.
      items                 Items to be removed, which should be, for 'project'
                            the name of project to be removed (optional), for
                            'tables' names of one or more variant tables, for
                            'samples' patterns using which matching samples are
                            removed, for 'fields' name of fields to be removed,
                            for 'geno_fields' name of genotype fields to be
                            removed (cf. 'vtools show genotypes'), for
                            'annotations' names of annotation databases, for
                            'variants' variant tables whose variants will be
                            removed from all variant tables and genotypes, for
                            'genotypes' conditions using which matching genotypes
                            are removed, and for 'phenotypes' columns in the
                            output of 'vtools show samples'. Note that removal of
                            samples will only remove sample name, filename (if all
                            related samples are removed), and related genotypes,
                            but not variants themselves; removal of annotation
                            databases will stop using these databases in the
                            project, but will not delete them from disk.
    
    optional arguments:
      -h, --help            show this help message and exit
      -v STD[LOG], --verbosity STD[LOG]
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1), and to
                            a logfile (default to 2).
    


{{% notice tip %}}
Fields from annotation databases cannot be removed. 
{{% /notice %}}

{{% notice tip %}}
Removing samples will only remove information for specified samples from existing variants. Variants themselves will not be removed. 
{{% /notice %}}

{{% notice tip %}}
Removing annotation databases only remove the database from the project (stop using it), not from the disk.
{{% /notice %}}

{{% notice tip %}}
Removing an annotation database might make other databases unusable if they are linked through one of the fields in the removed database. 
{{% /notice %}}



### 2. Details

#### 2.1 Remove variant table

To remove a variant table, 



    % vtools remove tables CEU
    % vtools show tables
    

This command accept the use of wildcard characters `?` and `*` so it is possible to easily remove a large number of tables. For example, the following command removes all temporary tables that were created when tables with the same names were created: 



    % vtools remove tables '*_Dec*'
    

The parameter should be quoted to avoid early interpretation of wildcard characters from the command line. 



{{% notice warning %}}
Wildcard characters should be used with caution. 
{{% /notice %}}


#### 2.2 Remove variant info fields

To remove a field, 



    % vtools remove field CEU_ctrls_freq CEU_ctrls_het
    % vtools show fields
    



#### 2.3 Remove genotype info fields from genotype tables

    % vtools remove geno_fields DP_geno
    % vtools show genotypes
    



#### 2.4 Remove project

The following command will remove an existing project. 



    % vtools remove project
    



#### 2.5 Remove samples

Show existing samples 



    % vtools show samples
    
    filename	sample_name	aff	sex	BMI
    SAMP1.vcf	SAMP1	        1	M	22.78
    SAMP2.vcf	SAMP1	        2	F	24.43
    var_format.vcf	SRR028913.aln.sorted.bam    None	None	 None
    

Remove one sample with an affection status of 1 



    % vtools remove samples 'aff = 1' -v2

    INFO: Removing sample SAMP1 from file SAMP1.vcf
    

Show samples again 



    % show samples
    
    INFO: Opening project sample.proj
    filename	sample_name	aff	sex	BMI
    SAMP2.vcf	SAMP1	        2	F	24.43
    var_format.vcf	SRR028913.aln.sorted.bam	None	None	None
    



#### 2.6 Remove annotation databases

A project uses three databases, `dbNSFP`, `keggPathway`, and `dbSNP131`, 



    % vtools show 

    Project name:                RA
    Primary reference genome:    hg18
    Secondary reference genome:  hg19
    Database engine:             sqlite3
    Variant tables:              variant, NS, NS_damaging, NS_sp_damaging, NS_pp, NS1_Aug16_012302, NS1, NS2
    Annotation databases:        dbNSFP (1.1_0), keggPathway, dbSNP131 (0)
    

You can remove `dbNSFP` from the project using command 



    % vtools remove annotations dbNSFP   

    INFO: Removing annotation database dbNSFP from the project
    

`dbNSFP` is no longer available, so `keggPathway` cannot be be loaded either, because it is linked by `dbNSFP.genename`. 



    % vtools show
    
    WARNING: Failed to locate field genename
    WARNING: Cannot open annotation database keggPathway
    Project name:                RA
    Primary reference genome:    hg18
    Secondary reference genome:  hg19
    Database engine:             sqlite3
    Variant tables:              variant, NS, NS_damaging, NS_sp_damaging, NS_pp, NS1_Aug16_012302, NS1, NS2
    Annotation databases:        dbSNP131 (0)
    



#### 2.7 Remove variants from specified variant tables

For example, we can remove all variants having low quality by: 



    % vtools select variant "DP<10" -t lowDP
    % vtools remove variants lowDP
    

If you would like to remove all but variants in a specified table, you will have to create a table with all variants to be removed using command `vtools compare`. 



    % vtools compare variant to_be_kept --difference to_be_removed
    

before you remove the table `to_be_removed` 



    % vtools remove variants to_be_removed
    


{{% notice tip %}}
Removing a large number of variants will be slow. In this case, it is usually much more efficient to create a subproject using the variants to be kept. (`vtools init name --parent /path/to/parent --variants to_be_kept`) 
{{% /notice %}}


#### 2.8 Remove genotypes

For example, we can remove all variants having low quality by: 



    % vtools remove genotypes "DP_geno<10"
    



#### 2.9 Remove phenotype from sample table

    % vtools remove phenotypes BMI