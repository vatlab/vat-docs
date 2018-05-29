+++
title = "Illumina"
weight = 4
hidden = true
+++

## Analyze five samples from Illumina, a tutorial 



### 1. Data source

Whole genome-sequencing data for 4 cases and 1 control. Raw data and called variants are provided by Illumina. The SNV and Indel variants are called using CASAVA v18 and are stored separately for each chromosome. 


### 2. Import data



Create a project 


    # Performance data is collected on a Mac Workstation with 2x2.26G Quad-Core Xeon processor with 8G RAM. 
    % vtools init ILLUMINA --force
    

Import data that are outputted from CASAVA v18. The data are organized by sample. Indels and SNPs are stored in different folders and in different formats. Because these are text files, we need to specify sample names to them. 



    # It takes about 1 hour to import a total of 7.1 million variants. A maximum of 1G RAM is used. 
    % for dir in Data/SS*
    % do
    	name=${dir##*/}
    	echo "Processing", $name
    	vtools import --format CASAVA18_indels $dir/Variations/indels/*.txt --sample $name --build hg19
    	vtools import --format CASAVA18_snps $dir/Variations/snps/*.txt --sample $name --build hg19
    % done
    


{{% notice tip %}}
You can use command "`vtools show samples`" to show a list of samples. You will notice that genotypes for each patient are spread to 24 *samples* in variant tools term. 
{{% /notice %}}


Our data consists of four cases and one control, we can add an `aff` table to the sample table to differentiate them: 



    vtools phenotype --set aff=1 --samples "sample_name='SS113'"
    vtools phenotype --set aff=2 --samples "sample_name!='SS113'"
    

The first command sets 48 samples (24 indel files and 24 SNP files) for one patient as control (`aff=1`). The second command sets the rest of the samples as cases (`aff=2`). 



### 3. Find variants that only occur in cases

In order to find variants that are in cases but not in controls, we use command `sample_stat` to count the number of variants: 



    #These commands take about 15min, and use 1.55G of RAM. 
    % vtools update variant --from_stat 'case_num=#(alt)' 'case_hom=#(hom)' 'case_het=#(het)' --samples 'aff=2'
    % vtools update variant --from_stat 'ctrl_num=#(alt)' 'ctrl_hom=#(hom)' 'ctrl_het=#(het)' --samples 'aff=1'
    

When can then find all variants that 

*   All heterozygous in cases, none in control 
*   All homozygous in cases, none in control 
*   Homozygous or heterozygous in cases, none in control 



    # These are done in seconds. 
    % vtools select variant 'case_het=4' 'ctrl_num=0' -t case_het4_ctrl_0
    % vtools select variant 'case_hom=4' 'ctrl_num=0' -t case_hom4_ctrl_0
    % vtools select variant 'case_hom + case_het =4' 'ctrl_num=0' -t case_4_ctrl_0
    


{{% notice tip %}}
You can check the number of variants in these tables using command "`vtools show tables`". 
{{% /notice %}}


### 4. Narrowing down to a region of interest

See available annotation databases, and use the refGene database 

    % vtools show annotations
    % vtools use refGene-hg19_20110909
    

Display the variants in refGene NM_006805. 



    # This command takes about 1min 
    % vtools select variant 'refGene.name = "NM_007505"' --output chr pos ref alt 
    

We can select a wilder region around this gene using ranges: 



    # This command returns in 1 second 
    % vtools select case_4_ctrl_0 'chr="5"' 'pos < 117300000' 'pos > 117000000' \
        --output chr pos ref alt refGene.name case_het case_hom  
    


{{% notice tip %}}
To see a list of fields that could be outputted, use command "`vtools show fields`". 
{{% /notice %}}


### 5. Use ANNOVAR to annotate variants in `case_4_ctrl_0`.

    # It takes 8s to export 300K variants and 54s to import results. 
    %vtools export case_4_ctrl_0 ann_input --format ANNOVAR 
    %../annovar/annotate_variation.pl ann_input ../annovar/humandb --build hg19
    %vtools update --from_file variant ann_input.exonic_variant_function --format ANNOVAR_output\
        --var_info mut_type genename function
    


{{% notice tip %}}
`vtools import --format ANNOVAR_output` by default only import info `mut_type`. You can use command `vtools show format ANNOVAR_output` to see available fields and use parameter `-var_info` to import them. 
{{% /notice %}}

Now, we can select variants according to their function. 



    # Query finishes in 5s 
    % vtools select variant 'function is not NULL' -t exonic
    



### 6. Filter by dbSNP and 1000 genomes membership

We would like to remove variants that belong to dbSNP and 1000 genomes because they are unlikely to be causal. We first need to use the relevant databases 



    % vtools use dbSNP
    % vtools use /path/to/thousandGenomes-hg19_20110909.DB
    

and exclude variants by 



    # Two queries take less than 1s. 
    % vtools exclude exonic "dbSNP.chr is not NULL" -t nonDBSNP
    % vtools exclude nonDBSNP 'thousandGenome.chr is not NULL' -t nonDBSNP_1000g
    



### 7. Filter by quality score

The CASAVA import format imports one quality score during importing, that is the phred scaled quality score for indels and snps. The name of these geno fields are `Q_indel` and `Q_max_gt` (Use command `vtools show genotypes` to see these fields). To get the mean quality score for each variant, we use commands 



    # This command uses 7.5min and 2.5G of RAM because it involves multiple genotype tables 
    % vtools update variant --from_stat 'mean_Q_indel=avg(Q_indel)' \
        'mean_Q_max_gt=avg(Q_max_gt)'
    

To see if a variant has 'above average' quality, you can calculate the average quality score of all variants, using command 



    % vtools output variant 'avg(mean_Q_indel)' 'avg(mean_Q_max_gt)'
    

If we determine that any variants that have Q\_indel < 300 and Q\_max_gt < 100 are of low quality, you can exclude them as follows 



    # This command takes 15s to execute 
    % vtools exclude nonDBSNP_1000g 'mean_Q_max_gt < 400 OR mean_Q_indel < 100' -t result
    



### 8. Output selected variants

Finally, we can output selected variants with their annotations using command 



{{% notice tip %}}
dbNSFP is large and might take several hours to download 
{{% /notice %}}


    % vtools use dbNSFP
    % vtools output result chr pos ref alt case_het case_hom genename mut_type SIFT_score PolyPhen2_score
    

We use dbNSFP here because this database contains SIFT and PolyPhen2 score for some of the variants.
