
+++
title = "hapmap"
weight = 8
+++

## Hap Map


### 1. Usage

Population-specific databases from the HapMap project. They provide population-specific variant count and frequences. 



    % vtools show annotations hapmap -v0
    
    hapmap_ASW_freq-hg18_20100817
    hapmap_ASW_freq
    hapmap_CEU_freq-hg18_20100817
    hapmap_CEU_freq
    hapmap_CHB_freq-hg18_20100817
    hapmap_CHB_freq
    hapmap_CHD_freq-hg18_20100817
    hapmap_CHD_freq
    hapmap_GIH_freq-hg18_20100817
    hapmap_GIH_freq
    hapmap_JPT_freq-hg18_20100817
    hapmap_JPT_freq
    hapmap_LWK_freq-hg18_20100817
    hapmap_LWK_freq
    hapmap_MEX_freq-hg18_20100817
    hapmap_MEX_freq
    hapmap_MKK_freq-hg18_20100817
    hapmap_MKK_freq
    hapmap_TSI_freq-hg18_20100817
    hapmap_TSI_freq
    hapmap_YRI_freq-hg18_20100817
    hapmap_YRI_freq
    



### 2. Details

    % vtools show annotation hapmap_CEU_freq
    
    Annotation database hapmap_CEU_freq (version hg18_20100817)
    Description:            Allele frequency information of SNP markers of the CEU
      population of phase II and III of the HAPMAP project.
    Database type:          variant
    Reference genome hg18:  chrom, pos, refallele, otherallele
      rsname                rsname
      chrom                 chromosome
      pos                   1-based position
      strand                strand
      refallele             reference allele
      CEU_refallele_freq    frequency of reference allele
      CEU_refallele_count   Count of reference allele
      otherallele           Other allele
      CEU_otherallele_freq  frequency of other allele
      CEU_otherallele_count Count of other allele
      CEU_totalcount        Total allele count
    

For example, if you would like to know the allele count and frequencies in hapmap, ESP, and thousand genomes projects, you can 



    vtools init freq
    vtools import mydata.vcf --build hg19  # import data
    vtools liftover hg18                   # if your data is in hg19
    vtools use dbSNP
    vtools use hapmap_ASW_freq
    vtools use hapmap_CEU_freq
    vtools use hapmap_CHB_freq
    vtools use hapmap_CHD_freq
    vtools use hapmap_GIH_freq
    vtools use hapmap_JPT_freq
    vtools use hapmap_LWK_freq
    vtools use hapmap_MEX_freq
    vtools use hapmap_MKK_freq
    vtools use hapmap_TSI_freq
    vtools use hapmap_YRI_freq
    vtools use ESP
    vtools use thousandGenomes
    
    vtools export variant --format csv --header \
        chr pos ref alt rsname \
        ASW_refallele_freq ASW_total_count \
        CEU_refallele_freq CEU_totalcount \
        CHB_refallele_freq CHB_totalcount \
        CHD_refallele_freq CHD_totalcount \
        GIH_refallele_freq GIH_totalcount \
        JPT_refallele_freq JPT_totalcount \
        LWK_refallele_freq LWK_totalcount \
        MEX_refallele_freq MEX_totalcount \
        MKK_refallele_freq MKK_totalcount \
        TSI_refallele_freq TSI_totalcount \
        YRI_refallele_freq YRI_totalcount \
        ESP_all_ref_freq ESP_totalcount \
        ESP_AfricanAmerican_RefFreq ESP_AfricanAmerican_totalcount \
        ESP_EuropeanAmerican_RefFreq EuropeanAmerican_totalcount \
        1kg_REF_FREQ \
    --fields  chr pos ref alt dbSNP.name \
        ASW_refallele_freq ASW_totalcount \
        CEU_refallele_freq CEU_totalcount \
        CHB_refallele_freq CHB_totalcount \
        CHD_refallele_freq CHD_totalcount \
        GIH_refallele_freq GIH_totalcount \
        JPT_refallele_freq JPT_totalcount \
        LWK_refallele_freq LWK_totalcount \
        MEX_refallele_freq MEX_totalcount \
        MKK_refallele_freq MKK_totalcount \
        TSI_refallele_freq TSI_totalcount \
        YRI_refallele_freq YRI_totalcount \
        "ESP.AllRefCount * 1.0 / (ESP.AllRefCount + ESP.AllAltCount)" "ESP.AllRefCount + ESP.AllAltCount" \
        "ESP.AfricanAmericanRefCount * 1.0 / (ESP.AfricanAmericanRefCount + ESP.AfricanAmericanAltCount)" \
        "ESP.AfricanAmericanRefCount + ESP.AfricanAmericanAltCount" \
        "ESP.EuropeanAmericanRefCount * 1.0 / (ESP.EuropeanAmericanRefCount + ESP.EuropeanAmericanAltCount)" \
        "ESP.EuropeanAmericanRefCount + ESP.EuropeanAmericanAltCount" \
        thousandGenomes.REF_FREQ_INFO > freq.csv
    

Or, if you would like to get the frequency across all hapmap populations, you can do 



    vtools output variant chr pos ref alt dbSNP.name \
        ASW_refallele_freq ASW_totalcount \
        CEU_refallele_freq CEU_totalcount \
        CHB_refallele_freq CHB_totalcount \
        CHD_refallele_freq CHD_totalcount \
        GIH_refallele_freq GIH_totalcount \
        JPT_refallele_freq JPT_totalcount \
        LWK_refallele_freq LWK_totalcount \
        MEX_refallele_freq MEX_totalcount \
        MKK_refallele_freq MKK_totalcount \
        TSI_refallele_freq TSI_totalcount \
        YRI_refallele_freq YRI_totalcount \
    "(IFNULL(ASW_refallele_count, 0.) + \
        IFNULL(CEU_refallele_count, 0.) + \
        IFNULL(CHB_refallele_count, 0.) + \
        IFNULL(CHD_refallele_count, 0.) + \
        IFNULL(GIH_refallele_count, 0.) + \
        IFNULL(JPT_refallele_count, 0.) + \
        IFNULL(LWK_refallele_count, 0.) + \
        IFNULL(MEX_refallele_count, 0.) + \
        IFNULL(MKK_refallele_count, 0.) + \
        IFNULL(TSI_refallele_count, 0.) + \
        IFNULL(YRI_refallele_count, 0.)) * 1.0 / \
        (IFNULL(ASW_totalcount, 0) + \
        IFNULL(CEU_totalcount, 0) + \
        IFNULL(CHB_totalcount, 0) + \
        IFNULL(CHD_totalcount, 0) + \
        IFNULL(GIH_totalcount, 0) + \
        IFNULL(JPT_totalcount, 0) + \
        IFNULL(LWK_totalcount, 0) + \
        IFNULL(MEX_totalcount, 0) + \
        IFNULL(MKK_totalcount, 0) + \
        IFNULL(TSI_totalcount, 0) + \
        IFNULL(YRI_totalcount, 0))"  -l 10
    

Here `IFNULL` is used to convert missing values to ``, and the result will be `NULL` if total count is `` (which leads to `0./0`).