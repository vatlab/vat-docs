+++
title = "dbNSFP"
description = ""
weight = 2
+++



# dbNSFP

(:skin vtools-annotation</summary> 

(:toc</summary> 

dbNSFP is an annotation database for non-synonymous SNPs assembled by Xiaoming Liu from the University of Texas School of Public Health (see citation below). With variant tools you can use the **dbNSFP** database or **dbNSFP-light** (a version with fewer features) - see which features are offered for each database version below. 



## dbNSFP

There can be frequent changes of name and their meanings of the fields across versions. Please pay close attention to the comments of fields before you use them. 



For the latest version dbNSFP 2.4 

*   For `SIFT_score`, lower score means more damaging. 
*   For Polyphen2 scores, higher score means more damaging. 
*   There are multiple scores in fields `SIFT_score_all`, `SIFT_pred_all`, `Polyphen2_HDIV_score_all`, `Polyphen2_HVAR_score_all`, `Polyphen2_HDIV_pred_all` and `Polyphen2_HVAR_pred_all`. If you need a score for selecting most damaging variants, use fields such as `SIFT_score`, `SIFT_pred`, `Polyphen2_HDIV_score`, `Polyphen2_HVAR_score` and `Polyphen2_HVAR_pred`. 
*   There can be multiple records for a variant so output of `vtools output` might be surprising (e.g. output score 0.4 with criterion 'score > 0.9'). Use option `--all` if you would like to see scores for all records. 



    % vtools show annotation dbNSFP -v2
    

    Annotation database dbNSFP (version hg18_hg19_2_1)
    Description:            dbNSFP version 2.1, maintained by Xiaoming Liu from
      UTSPH. Please cite "Liu X, Jian X, and Boerwinkle E. 2011. dbNSFP: a
      lightweight database of human non-synonymous SNPs and their functional
      predictions. Human Mutation. 32:894-899" and "Liu X, Jian X, and Boerwinkle
      E. 2013. dbNSFP v2.0: A Database of Human Nonsynonymous SNVs and Their
      Functional Predictions and Annotations. Human Mutation. 34:E2393-E2402." if
      you find this database useful.
    Database type:          variant
    Number of records:      89,617,785
    Distinct variants:      84,484,850
    Reference genome hg18:  chr, hg18_pos, ref, alt
    Reference genome hg19:  chr, pos, ref, alt
    
    Field:                  chr
    Type:                   string
    Comment:                Chromosome number
    Missing entries:        0 
    Unique Entries:         24
    
    Field:                  pos
    Type:                   integer
    Comment:                physical position on the chromosome as to hg19
                            (1-based coordinate)
    Missing entries:        0 
    Unique Entries:         28,060,014
    Range:                  6007 - 249212562
    
    Field:                  ref
    Type:                   string
    Comment:                Reference nucleotide allele (as on the + strand)
    Missing entries:        0 
    Unique Entries:         4
    
    Field:                  alt
    Type:                   string
    Comment:                Alternative nucleotide allele (as on the + strand)
    Missing entries:        0 
    Unique Entries:         4
    
    Field:                  aaref
    Type:                   string
    Comment:                reference amino acid
    Missing entries:        0 
    Unique Entries:         22
    
    Field:                  aaalt
    Type:                   string
    Comment:                alternative amino acid
    Missing entries:        0 
    Unique Entries:         22
    
    Field:                  hg18_pos
    Type:                   integer
    Comment:                physical position on the chromosome as to hg19
                            (1-based coordinate)
    Missing entries:        44,904 (0.1% of 89,617,785 records)
    Unique Entries:         28,043,425
    Range:                  4381 - 247179185
    
    Field:                  genename
    Type:                   string
    Comment:                common gene name
    Missing entries:        0 
    Unique Entries:         20,264
    
    Field:                  Uniprot_acc
    Type:                   string
    Comment:                Uniprot accession number. Multiple entries separated
                            by ";".
    Missing entries:        17,068,597 (19.0% of 89,617,785 records)
    Unique Entries:         55,816
    
    Field:                  Uniprot_id
    Type:                   string
    Comment:                Uniprot ID number. Multiple entries separated by ";".
    Missing entries:        20,254,026 (22.6% of 89,617,785 records)
    Unique Entries:         37,250
    
    Field:                  Uniprot_aapos
    Type:                   integer
    Comment:                amino acid position as to Uniprot. Multiple entries
                            separated by ";".
    Missing entries:        17,068,597 (19.0% of 89,617,785 records)
    Unique Entries:         2,687,476
    Range:                  1 - 9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9
    
    Field:                  Interpro_domain
    Type:                   string
    Comment:                Interpro_domain: domain or conserved site on which the
                            variant locates. Domain annotations come from Interpro
                            database. The number in the brackets following a
                            specific domain is the count of times Interpro assigns
                            the variant position to that domain, typically coming
                            from different predicting databases. Multiple entries
                            separated by ";".
    Missing entries:        60,454,832 (67.5% of 89,617,785 records)
    Unique Entries:         9,922
    
    Field:                  cds_strand
    Type:                   string
    Comment:                coding sequence (CDS) strand (+ or -)
    Missing entries:        0 
    Unique Entries:         5
    
    Field:                  refcodon
    Type:                   string
    Comment:                reference codon
    Missing entries:        2,270,742 (2.5% of 89,617,785 records)
    Unique Entries:         1,754
    
    Field:                  SLR_test_statistic
    Type:                   float
    Comment:                SLR test statistic for testing natural selection on
                            codons. A negative value indicates negative selection,
                            and a positive value indicates positive selection.
                            Larger magnitude of the value suggests stronger
                            evidence.
    Missing entries:        46,683,780 (52.1% of 89,617,785 records)
    Unique Entries:         511,811
    Range:                  -188.177 - 108.85
    
    Field:                  codonpos
    Type:                   integer
    Comment:                position on the codon (1, 2 or 3)
    Missing entries:        2,270,742 (2.5% of 89,617,785 records)
    Unique Entries:         4
    Range:                  1 - 3;2;3
    
    Field:                  fold_degenerate
    Type:                   integer
    Comment:                degenerate type (0, 2 or 3)
    Missing entries:        2,270,742 (2.5% of 89,617,785 records)
    Unique Entries:         79
    Range:                  0 - 2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;2;0
    
    Field:                  Ancestral_allele
    Type:                   string
    Comment:                Ancestral allele (based on 1000 genomes reference
                            data). The following comes from its original README
                            file: ACTG - high-confidence call, ancestral state
                            supproted by the other two sequences actg - low-
                            confindence call, ancestral state supported by one
                            sequence only N    - failure, the ancestral state is
                            not supported by any other sequence -    - the extant
                            species contains an insertion at this postion .    -
                            no coverage in the alignment
    Missing entries:        2,488,820 (2.8% of 89,617,785 records)
    Unique Entries:         10
    
    Field:                  Ensembl_geneid
    Type:                   string
    Comment:                Ensembl gene id
    Missing entries:        0 
    Unique Entries:         20,839
    
    Field:                  Ensembl_transcriptid
    Type:                   string
    Comment:                Ensembl transcript ids (separated by ";")
    Missing entries:        0 
    Unique Entries:         112,159
    
    Field:                  aapos
    Type:                   integer
    Comment:                : amino acid position as to the protein "-1" if the
                            variant is a splicing site SNP (2bp on each end of an
                            intron)
    Missing entries:        0 
    Unique Entries:         4,315,466
    Range:                  -1 - 9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;9;27;9;9;9;9;35;9;9;9
    
    Field:                  SIFT_score
    Type:                   float
    Comment:                SIFT score, If a score is smaller than 0.05 the
                            corresponding NS is predicted as "D(amaging)";
                            otherwise it is predicted as "T(olerated)".
    Missing entries:        12,024,501 (13.4% of 89,617,785 records)
    Unique Entries:         101
    Range:                  0 - 1
    
    Field:                  SIFT_score_converted
    Type:                   float
    Comment:                SIFTnew=1-SIFTori. The larger the more damaging.
    Missing entries:        12,024,501 (13.4% of 89,617,785 records)
    Unique Entries:         101
    Range:                  0 - 1
    
    Field:                  SIFT_pred
    Type:                   string
    Comment:                If SIFTori is smaller than 0.05 (SIFTnew>0.95) the
                            corresponding NS is predicted as "D(amaging)";
                            otherwise it is predicted as "T(olerated)".
    Missing entries:        12,024,501 (13.4% of 89,617,785 records)
    Unique Entries:         2
    
    Field:                  Polyphen2_HDIV_score_max
    Type:                   float
    Comment:                The maximum (most damaging) value of Polyphen2 score
                            based on HumDiv, i.e. hdiv_prob. Use
                            Polyphen2_HDIV_score to get a list of all scores.
    Missing entries:        17,086,068 (19.1% of 89,617,785 records)
    Unique Entries:         1,001
    Range:                  0 - 1
    
    Field:                  Polyphen2_HDIV_score
    Type:                   string
    Comment:                Polyphen2 score based on HumDiv, i.e. hdiv_prob. The
                            score ranges from 0 to 1, and the corresponding
                            prediction is "probably damaging" if it is in
                            [0.957,1]; "possibly damaging" if it is in
                            [0.453,0.956]; "benign" if it is in [0,0.452]. Score
                            cutoff for binary classification is 0.5, i.e. the
                            prediction is "neutral" if the score is smaller than
                            0.5 and "deleterious" if the score is larger than 0.5.
                            Multiple entries separated by ";".
    Missing entries:        17,084,053 (19.1% of 89,617,785 records)
    Unique Entries:         8,590,602
    
    Field:                  Polyphen2_HDIV_pred
    Type:                   string
    Comment:                Polyphen2 prediction based on HumDiv, "D" ("probably
                            damaging"), "P" ("possibly damaging") and "B"
                            ("benign"). Multiple entries separated by ";". Because
                            the availability of multiple values, use expression
                            such as 'D' in Polyphen2_HDIV_pred instead of 'D' =
                            Polyphen2_HDIV_pred to filter variants that are
                            probably damaging.
    Missing entries:        17,084,053 (19.1% of 89,617,785 records)
    Unique Entries:         83,942
    
    Field:                  Polyphen2_HVAR_score_max
    Type:                   float
    Comment:                The maximum (most damaging) value of all Polyphen2
                            score based on HumVar, i.e. hvar_prob. Use
                            Polyphen2_HVAR_score_all to get a list of all scores.
    Missing entries:        17,086,068 (19.1% of 89,617,785 records)
    Unique Entries:         1,001
    Range:                  0 - 1
    
    Field:                  Polyphen2_HVAR_score
    Type:                   string
    Comment:                Polyphen2 score based on HumVar, i.e. hvar_prob. The
                            score ranges from 0 to 1, and the corresponding
                            prediction is "probably damaging" if it is in
                            [0.909,1]; "possibly damaging" if it is in
                            [0.447,0.908]; "benign" if it is in [0,0.446]. Score
                            cutoff for binary classification is 0.5, i.e. the
                            prediction is "neutral" if the score is smaller than
                            0.5 and "deleterious" if the score is larger than 0.5.
                            Multiple entries separated by ";".
    Missing entries:        17,084,053 (19.1% of 89,617,785 records)
    Unique Entries:         10,999,020
    
    Field:                  Polyphen2_HVAR_pred
    Type:                   string
    Comment:                Polyphen2 prediction based on HumVar, "D" ("porobably
                            damaging"), "P" ("possibly damaging") and "B"
                            ("benign"). Multiple entries separated by ";". Because
                            the availability of multiple values, use expression
                            such as 'D' in Polyphen2_HVAR_pred instead of 'D' =
                            Polyphen2_HVAR_pred to filter variants that are
                            probably damaging.
    Missing entries:        17,084,053 (19.1% of 89,617,785 records)
    Unique Entries:         83,681
    
    Field:                  LRT_score
    Type:                   float
    Comment:                The original LRT two-sided p-value (LRTori).
    Missing entries:        21,548,464 (24.0% of 89,617,785 records)
    Unique Entries:         826,817
    Range:                  0 - 1
    
    Field:                  LRT_score_converted
    Type:                   float
    Comment:                Converted LRT original p-value (LRTnew). We converted
                            the LRTori to a score suggested by our Human Muation
                            (2011) paper: LRTnew=1-LRTori*0.5 if Omega<1, or
                            LRTnew=LRTori*0.5 if Omega>=1.
    Missing entries:        21,548,464 (24.0% of 89,617,785 records)
    Unique Entries:         1,168,826
    Range:                  0 - 1
    
    Field:                  LRT_pred
    Type:                   string
    Comment:                LRT prediction, D(eleterious), N(eutral) or U(nknown)
    Missing entries:        21,548,464 (24.0% of 89,617,785 records)
    Unique Entries:         3
    
    Field:                  MutationTaster_score
    Type:                   float
    Comment:                MutationTaster score
    Missing entries:        1,143,911 (1.3% of 89,617,785 records)
    Unique Entries:         598,533
    Range:                  0 - 1
    
    Field:                  MutationTaster_score_converted
    Type:                   float
    Comment:                The converted score suggested by our Human Mutation
                            (2011) paper: if the prediction is "A" or "D"
                            MTnew=MTori; if the prediction is "N" or "P",
                            MTnew=1-MTori.
    Missing entries:        4,373,664 (4.9% of 89,617,785 records)
    Unique Entries:         999,050
    Range:                  0 - 1
    
    Field:                  MutationTaster_pred
    Type:                   string
    Comment:                MutationTaster prediction, "A"
                            ("disease_causing_automatic"), "D"
                            ("disease_causing"), "N" ("polymorphism") or "P"
                            ("polymorphism_automatic")
    Missing entries:        1,143,911 (1.3% of 89,617,785 records)
    Unique Entries:         4
    
    Field:                  MutationAssessor_score
    Type:                   float
    Comment:                MutationAssessor functional impact combined score
                            (MAori)
    Missing entries:        14,986,410 (16.7% of 89,617,785 records)
    Unique Entries:         2,145
    Range:                  -5.545 - 5.975
    
    Field:                  MutationAssessor_score_converted
    Type:                   float
    Comment:                Scaled to 0-1: MAnew=(MAori-(-5.545))/(5.975-(-5.545))
    Missing entries:        14,986,410 (16.7% of 89,617,785 records)
    Unique Entries:         2,139
    Range:                  0 - 1
    
    Field:                  MutationAssessor_pred
    Type:                   string
    Comment:                MutationAssessor's functional impact of a variant :
                            predicted functional (high, medium), predicted non-
                            functional (low, neutral)" Please refer to Reva et al.
                            Nucl. Acids Res. (2011) 39(17):e118 for details
    Missing entries:        14,986,410 (16.7% of 89,617,785 records)
    Unique Entries:         4
    
    Field:                  FATHMM_score
    Type:                   float
    Comment:                FATHMM default score (weighted for human inherited-
                            disease mutations with Disease Ontology); If a score
                            is smaller than -1.5 the corresponding NS is predicted
                            as "D(AMAGING)"; otherwise it is predicted as
                            "T(OLERATED)". If there's more than one scores
                            associated with the same NS due to isoforms, the
                            smallest score (most damaging) was used. Please refer
                            to Shihab et al Hum. Mut. (2013) 34(1):57-65 for
                            details
    Missing entries:        19,342,889 (21.6% of 89,617,785 records)
    Unique Entries:         2,135
    Range:                  -16.13 - 10.64
    
    Field:                  FATHMM_score_converted
    Type:                   float
    Comment:                Scaled to 0-1 and reverse direction (the larger the
                            more damaging):
                            FATHMMnew=1-(FATHMMori-(-16.13))/(10.64-(-16.13))
    Missing entries:        19,342,889 (21.6% of 89,617,785 records)
    Unique Entries:         2,135
    Range:                  0 - 1
    
    Field:                  FATHMM_pred
    Type:                   string
    Comment:                If a FATHMM_score is <=-1.5 the corresponding NS is
                            predicted as "D(AMAGING)"; otherwise it is predicted
                            as "T(OLERATED)".
    Missing entries:        19,342,889 (21.6% of 89,617,785 records)
    Unique Entries:         2
    
    Field:                  GERP_NR
    Type:                   float
    Comment:                GERP++ neutral rate
    Missing entries:        541,067 (0.6% of 89,617,785 records)
    Unique Entries:         1,258
    Range:                  0.0465 - 6.17
    
    Field:                  GERP_RS
    Type:                   float
    Comment:                GERP++ RS score, the larger the score, the more
                            conserved the site.
    Missing entries:        541,067 (0.6% of 89,617,785 records)
    Unique Entries:         8,412
    Range:                  -12.3 - 6.17
    
    Field:                  PhyloP_score
    Type:                   float
    Comment:                PhyloP score, the larger the score, the more conserved
                            the site.
    Missing entries:        64,695 (0.1% of 89,617,785 records)
    Unique Entries:         10,245
    Range:                  -11.958 - 2.941
    
    Field:                  mg29way_pi
    Type:                   string
    Comment:                The estimated stationary distribution of A, C, G and T
                            at the site, using SiPhy algorithm based on 29 mammals
                            genomes.
    Missing entries:        0 
    Unique Entries:         7,239,991
    
    Field:                  mg29way_logOdds
    Type:                   float
    Comment:                SiPhy score based on 29 mammals genomes. The larger
                            the score, the more conserved the site.
    Missing entries:        1,348,155 (1.5% of 89,617,785 records)
    Unique Entries:         223,955
    Range:                  0.0003 - 37.9718
    
    Field:                  LRT_Omega
    Type:                   float
    Comment:                estimated nonsynonymous-to-synonymous-rate ratio
                            (reported by LRT)
    Missing entries:        21,548,464 (24.0% of 89,617,785 records)
    Unique Entries:         842,708
    Range:                  0 - 7780.54
    
    Field:                  UniSNP_ids
    Type:                   string
    Comment:                "rs numbers from UniSNP, which is a cleaned version of
                            dbSNP build 129, in format: rs number1;rs number2;..."
    Missing entries:        89,510,596 (99.9% of 89,617,785 records)
    Unique Entries:         100,701
    
    Field:                  KGp1_AC
    Type:                   integer
    Comment:                Alternative allele count in the whole 1000Gp1 data.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         2,172
    Range:                  0 - 2184
    
    Field:                  KGp1_AF
    Type:                   float
    Comment:                Alternative allele frequency in the whole 1000Gp1
                            data.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         2,571
    Range:                  0 - 1
    
    Field:                  KGp1_AFR_AC
    Type:                   integer
    Comment:                Alternative allele counts in the 1000Gp1 African
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         493
    Range:                  0 - 492
    
    Field:                  KGp1_AFR_AF
    Type:                   float
    Comment:                Alternative allele frequency in the 1000Gp1 African
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         1,062
    Range:                  0 - 1
    
    Field:                  KGp1_EUR_AC
    Type:                   integer
    Comment:                Alternative allele counts in the 1000Gp1 European
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         759
    Range:                  0 - 758
    
    Field:                  KGp1_EUR_AF
    Type:                   float
    Comment:                Alternative allele frequency in the 1000Gp1 European
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         1,185
    Range:                  0 - 1
    
    Field:                  KGp1_AMR_AC
    Type:                   integer
    Comment:                Alternative allele counts in the 1000Gp1 American
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         363
    Range:                  0 - 362
    
    Field:                  KGp1_AMR_AF
    Type:                   float
    Comment:                Alternative allele frequency in the 1000Gp1 American
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         735
    Range:                  0 - 1
    
    Field:                  KGp1_ASN_AC
    Type:                   integer
    Comment:                Alternative allele counts in the 1000Gp1 Asian
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         573
    Range:                  0 - 572
    
    Field:                  KGp1_ASN_AF
    Type:                   float
    Comment:                Alternative allele frequency in the 1000Gp1 Asian
                            descendent samples.
    Missing entries:        89,278,976 (99.6% of 89,617,785 records)
    Unique Entries:         939
    Range:                  0 - 1
    
    Field:                  ESP6500_AA_AF
    Type:                   float
    Comment:                Alternative allele frequency in the Afrian American
                            samples of the NHLBI GO Exome Sequencing Project
                            (ESP6500 data set).
    Missing entries:        88,817,528 (99.1% of 89,617,785 records)
    Unique Entries:         27,424
    Range:                  0 - 1
    
    Field:                  ESP6500_EA_AF
    Type:                   float
    Comment:                Alternative allele frequency in the European American
                            samples of the NHLBI GO Exome Sequencing Project
                            (ESP6500 data set).
    Missing entries:        88,817,528 (99.1% of 89,617,785 records)
    Unique Entries:         22,975
    Range:                  0 - 1
    
    

As a quick example, one can use dbNSFP to annotate all of the "damaging" non-synonymous variants from a list of variants. In this example, we find all of the variants predicted to be damaging by SIFT and PolyPhen2 from the master variant table, and we record these variants into a new table called "damaging\_ns\_snps". 



    vtools select variant "SIFT_pred = 'D' OR PolyPhen2_HDIV_pred like '%D%'" -t damaging_ns_snps
    



## dbNSFP_gene

    % vtools use dbNSFP_gene --linked_by refGene.name2
    % vtools show annotation dbNSFP_gene -v2
    

    Annotation database dbNSFP_gene (version 2_1)
    Description:            dbNSFP_gene version 2.1, maintained by Dr. Xiaoming
      Liu from UTSPH. Please cite "Liu X, Jian X, and Boerwinkle E. 2011. dbNSFP:
      a lightweight database of human non-synonymous SNPs and their functional
      predictions. Human Mutation. 32:894-899" and "Liu X, Jian X, and Boerwinkle
      E. 2013. dbNSFP v2.0: A Database of Human Nonsynonymous SNVs and Their
      Functional Predictions and Annotations. Human Mutation. 34:E2393-E2402." if
      you find this database useful.
    Database type:          field
    Reference genome *:     Gene_name
      Gene_name             Gene symbol from HGNC
      Ensembl_gene          Ensembl gene id (from HGNC)
      chr                   Chromosome number (from HGNC)
      Gene_old_names        Old gene sybmol (from HGNC)
      Gene_other_names      Other gene names (from HGNC)
      Uniprot_acc           Uniprot acc number (from HGNC and Uniprot)
      Uniprot_id            Uniprot id (from HGNC and Uniprot)
      Entrez_gene_id        Entrez gene id (from HGNC)
      CCDS_id               CCDS id (from HGNC)
      Refseq_id             Refseq gene id (from HGNC)
      ucsc_id               UCSC gene id (from HGNC)
      MIM_id                MIM gene id (from HGNC)
      Gene_full_name        Gene full name (from HGNC)
      Pathway_Uniprot       Pathway(s) the gene belongs to (from Uniprot)
      Pathway_ConsensusPathDB Pathway(s) the gene belongs to (from
                            ConsensusPathDB)
      Function_description  Function description of the gene (from Uniprot)
      Disease_description   Disease(s) the gene caused or associated with (from
                            Uniprot)
      MIM_phenotype_id      MIM id(s) of the phenotype the gene caused or
                            associated with (from Uniprot)
      MIM_disease           MIM disease name(s) with MIM id(s) in "[]" (from
                            Uniprot)
      Trait_association_GWAS Trait(s) the gene associated with (from GWAS catalog)
      GO_Slim_biological_process GO Slim terms for biological process
      GO_Slim_cellular_component GO Slim terms for cellular component
      GO_Slim_molecular_function GO Slim terms for molecular function
      Expression_egenetics  Tissues/organs the gene expressed in (egenetics data
                            from BioMart)
      Expression_GNF_Atlas  Tissues/organs the gene expressed in (GNF/Atlas data
                            from BioMart)
      Interactions_IntAct   Other genes the gene interacted with (from IntAct)
                            gene name followed by Pubmed id in "[]"
      Interactions_BioGRID  Other genes the gene interacted with (from BioGRID)
                            gene name followed by Pubmed id in "[]"
      Interactions_ConsensusPathDB Other genes the gene interacted with (from
                            ConsensusPathDB) gene name followed by interaction
                            confidence in "[]"
      P_HI                  Estimated probability of haploinsufficiency of the
                            gene from doi:10.1371/journal.pgen.1001154)
      P_rec                 Estimated probability that gene is a recessive disease
                            gene from doi:10.1126/science.1215040)
      Known_rec_info        Known recessive status of the gene (from DOI]
                            10.1126/science.1215040) "lof-tolerant = seen in
                            homozygous state in at least one 1000G individual"
                            "recessive = known OMIM recessive disease" original
                            annotations from DOI:10.1126/science.1215040)
      Essential_gene        Essential ("E") or Non-essential phenotype-changing
                            ("N") based on Mouse Genome Informatics database. from
                            doi:10.1371/journal.pgen.1003484
    



## dbNSFP_light

This light version of dbNSFP is only available for dbNSFP 1.0. 



    vtools show annotation dbNSFP_light -v2
    

    Annotation database dbNSFP_light (version hg18_hg19_1.3)
    Description: dbNSFP_light version 1.0, maintained by Xiaoming Liu from UTSPH.
        Please cite "Liu X, Jian X, and Boerwinkle E. 2011. dbNSFP: a
        lightweight database of human non-synonymous SNPs and their
        functional predictions. Human Mutation. 32:894-899" if you find
        this database useful.
    Database type: variant
    Number of records: 73,968,886
    Number of distinct variants: 73,754,006
    Reference genome hg18: ['chr', 'pos', 'ref', 'alt']
    Reference genome hg19: ['chr', 'pos', 'ref', 'alt']
    
    Field:           chr
    Type:            string
    Missing entries: 0 
    Unique Entries:  24
    
    Field:           pos
    Type:            integer
    Missing entries: 0 
    Unique Entries:  24,918,243
    Range:           4381 - 247179185
    
    Field:           ref
    Type:            string
    Comment:         Reference nucleotide allele (as on the + strand)
    Missing entries: 0 
    Unique Entries:  4
    
    Field:           alt
    Type:            string
    Comment:         Alternative nucleotide allele (as on the + strand)
    Missing entries: 0 
    Unique Entries:  4
    
    Field:           aaref
    Type:            string
    Comment:         reference amino acid
    Missing entries: 0 
    Unique Entries:  21
    
    Field:           aaalt
    Type:            string
    Comment:         alternative amino acid
    Missing entries: 0 
    Unique Entries:  21
    
    Field:           hg19pos
    Type:            integer
    Comment:         physical position on the chromosome as to hg19 (1-based
                     coordinate)
    Missing entries: 33 (0.0% of 73,968,886 records)
    Unique Entries:  24,900,697
    Range:           15925 - 249212562
    
    Field:           PhyloP_score
    Type:            float
    Comment:         PhyloP score, phyloPnew=1-0.5x10^phyloPori if phyloPori>0 or
                     phyloPnew=0.5x10^phyloPori if phyloPori<0
    Missing entries: 21,677 (0.0% of 73,968,886 records)
    Unique Entries:  6,237
    Range:           0 - 0.995645X
    
    Field:           SIFT_score
    Type:            float
    Comment:         SIFT score, SIFTnew=1-SIFTori
    Missing entries: 570,924 (0.8% of 73,968,886 records)
    Unique Entries:  167
    Range:           0 - 195561991
    
    Field:           Polyphen2_score
    Type:            float
    Comment:         Polyphen2 score, i.e. pph2_prob
    Missing entries: 10,400,231 (14.1% of 73,968,886 records)
    Unique Entries:  1,005
    Range:           0 - T
    
    Field:           LRT_score
    Type:            float
    Comment:         LRT score, LRTnew=1-LRTorix0.5 if <1, or LRTnew=LRTorix0.5 if
                     >=1
    Missing entries: 7,795,201 (10.5% of 73,968,886 records)
    Unique Entries:  780,594
    Range:           0 - T
    
    Field:           LRT_pred
    Type:            string
    Comment:         LRT prediction, D(eleterious), N(eutral) or U(nknown)
    Missing entries: 7,795,201 (10.5% of 73,968,886 records)
    Unique Entries:  17
    
    Field:           MutationTaster_score
    Type:            float
    Comment:         MutationTaster score
    Missing entries: 5,514,812 (7.5% of 73,968,886 records)
    Unique Entries:  999,920
    Range:           0 - W
    
    Field:           MutationTaster_pred
    Type:            string
    Comment:         MutationTaster prediction, "A" ("disease_causing_automatic"),
                     "D" ("disease_causing"), "N" ("polymorphism") or "P"
                     ("polymorphism_automatic")
    Missing entries: 5,514,843 (7.5% of 73,968,886 records)
    Unique Entries:  6
    
    Field:           LRT_Omega
    Type:            float
    Comment:         estimated nonsynonymous-to-synonymous-rate ratio (reported by
                     LRT)
    Missing entries: 7,795,201 (10.5% of 73,968,886 records)
    Unique Entries:  837,566
    Range:           0 - 0.995645X
    
    Field:           GERP_NR
    Type:            float
    Comment:         GERP++ netral rate
    Missing entries: 0 
    Unique Entries:  1,218
    Range:           0 - 195561992
    
    Field:           GERP_RS
    Type:            float
    Comment:         GERP++ RS score
    Missing entries: 0 
    Unique Entries:  8,344
    Range:           -11.6 - T
    
    Field:           uniprot_acc
    Type:            string
    Comment:         Uniprot accession number
    Missing entries: 0 
    Unique Entries:  18,766
    
    Field:           uniprot_id
    Type:            string
    Comment:         Uniprot ID number
    Missing entries: 0 
    Unique Entries:  17,552
    
    Field:           uniprot_aapos
    Type:            integer
    Comment:         amino acid position as to Uniprot
    Missing entries: 0 
    Unique Entries:  8,815
    Range:           0.53741 - Y