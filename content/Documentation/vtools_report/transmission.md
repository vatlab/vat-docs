
+++
title = "transmission"
weight = 8
+++


## Locate de novo, recessive and other variants that are transmitted from parents to offspring 

<font color=#FF0000>
 The `inconsistent` option of this command is not completed yet.  
</font>


### 1. Usage

    % vtools_report transmission -h
    

    usage: vtools_report transmission [-h] [--parents PARENTS PARENTS]
                                      [--offspring OFFSPRING [OFFSPRING ...]]
                                      [--denovo [DENOVO [DENOVO ...]]]
                                      [--recessive [RECESSIVE [RECESSIVE ...]]]
                                      [--inconsistent [INCONSISTENT [INCONSISTENT ...]]]
                                      [-v {0,1,2}]
    
    optional arguments:
      -h, --help            show this help message and exit
      --parents PARENTS PARENTS
                            Names of parents, which should uniquely identify two
                            samples.
      --offspring OFFSPRING [OFFSPRING ...]
                            Names of one or more offspring samples.
      --denovo [DENOVO [DENOVO ...]]
                            A list of tables to store denovo variants for each
                            offspring. DeNovo variants are defined as offspring
                            variants that do not exist in any of the parents,
                            including the cases when the offspring have different
                            variants from what parents have at the same genomic
                            locations.
      --recessive [RECESSIVE [RECESSIVE ...]]
                            A list of tables to store recessive variants for each
                            offspring. Recessive variants are defined as variants
                            that are homozygous in offspring, and heterozygous in
                            both parents.
      --inconsistent [INCONSISTENT [INCONSISTENT ...]]
                            A list of tables to store variants for each offspring
                            that demonstrate mendelian inconsistencies, namely
                            variants that are not passed from parents to offspring
                            in a Mendelian fashion. Examples of inconsistent
                            variants include de novo variants, homozygous variants
                            in offspring with only one parental carrier, wildtype
                            offspring variants with a homozygous parent,
                            heterozygous offspring variants with two homozygous
                            parents, and more complicated cases when multiple
                            variants appear at the same sites.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information to standard output (default to 1).