
+++
title = "inbreeding_coefficient"
weight = 7
+++


## Calculation inbreeding coefficient for individual samples

`vtools_report inbreeding_coefficient` calculates the \\(F\\)  statistic at **single individual sample level** from genotype data. It measures the reduction in heterozygosity for given genomic region of samples, compare to expected heterozygosity level under Hardy-Weinberg Equilibrium. For a two allelic locus, $$P(AA)=p^2(1-F)+pF$$$$P(aa)=q^2(1-F)+qF$$$$P(Aa)=2pq(1-F)$$We compute estimate for \\(F\\)  as \\(\hat{F}=1-\frac{\#observed(Aa)}{\#expected(Aa)}\\)  


{{% notice info %}}
Variants included for calculation of \\(F\\)  must be under HWE and be bi-allelic. Tri-allelic loci are automatically excluded from calculation. 
{{% /notice %}}

Estimate of MAF using given samples should be computed prior to calculation of \\(F$, via `vtools update TABLE --from_stat <em>maf=maf()</em>`. 



### 1. Details

#### 1.1 Interface

    vtools_report inbreeding_coefficient -h
    
    usage: vtools_report inbreeding_coefficient [-h]
                                                [--samples [SAMPLES [SAMPLES ...]]]
                                                --maf_field MAF_FIELD [-v {0,1,2}]
                                                table
    
    Report F statistic which describe the expected degree of a reduction in
    heterozygosity when compared to Hardy-Weinberg expectation. In simple two
    allele system with inbreeding, P(AA) = p^2(1-F)+pF, P(aa) = q^2(1-F)+qF and
    P(HET) = 2pq(1-F). For an individual F is estimated by F = 1 - #observed(HET)
    / #expected(HET). Tri-allelic loci, if identified, are excluded from
    calculation.
    
    positional arguments:
      table                 Variants based on which individual inbreeding
                            coefficients are evaluated.
    
    optional arguments:
      -h, --help            show this help message and exit
      --samples [SAMPLES [SAMPLES ...]]
                            Conditions based on which samples are selected to have
                            inbreeding coefficients calculated. Default to all
                            samples.
      --maf_field MAF_FIELD
                            Name of the field that holds minor allele frequency
                            for sample variants, which is the field name for
                            command 'vtools update table --from_stat
                            "maf_field=maf()" --samples ...'.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.
    



#### 1.2 Example

Compute MAF for given samples 



    vtools update variant --from_stat 'mafEUR=maf()' --samples "super_pop='EUR'" -j8
    

We evaluate heterozygosity level on chromosome 1 



    vtools select "chr='1'" -t chr1
    

Inbreeding coefficients are computed and saved to file `chr1.inbreeding.txt` 



    vtools_report inbreeding_coef chr1 --maf_field mafEUR --samples "super_pop='EUR'" > chr1.inbreeding.txt

    HG00118	0.00599944241381
    HG00119	0.00206096581669
    HG00120	0.0114070032711
    HG00121	0.0461496321201
    HG00122	0.0127749763012
    HG00123	0.00582167049467
    HG00124	0.0129693670104
    ...