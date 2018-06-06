
+++
title = "discordance_rate"
weight = 2
+++



### Usage

    % vtools_report discordance_rate -h
    

    usage: vtools_report discordance_rate [-h] [-s [SAMPLES [SAMPLES ...]]]
                                          [--genotypes [GENOTYPES [GENOTYPES ...]]]
                                          [-v {0,1,2}]
    
    Report discordance rate, namely the number of genotype calls that differ
    between a pair of samples divided by the total number of SNPs for which both
    calls are non-missing, between pairs of samples. The statistics can be
    calculated for all samples or selected samples specified by parameter
    --samples. This command output a n by n matrix with sample names in the
    header. Items (i,j) in this matrix is numbers in the format of diff/all for i
    >= j, and the actual ratio for i < j. This rate is affected by runtime option
    treat_missing_as_wildtype which assumes that variants that do not appear in a
    sample (or filtered by quality score etc) are wildtype alleles.
    
    optional arguments:
      -h, --help            show this help message and exit
      -s [SAMPLES [SAMPLES ...]], --samples [SAMPLES [SAMPLES ...]]
                            Limiting variants from samples that match conditions
                            that use columns shown in command 'vtools show sample'
                            (e.g. 'aff=1', 'filename like "MG%"').
      --genotypes [GENOTYPES [GENOTYPES ...]]
                            Limiting genotypes from samples that match conditions
                            that involves genotype fields (e.g. filter by quality
                            score, with fields shown in command 'vtools show
                            genotypes'). If a variant is filtered for one sample
                            but not another, it will be included if runtime option
                            $treat_missing_as_wildtype is set to True, and
                            discarded otherwise.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.