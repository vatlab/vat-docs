+++
title = "ESP"
weight = 6
+++


## Variants from the Exome Sequencing Project (ESP)


The EVS annotation source contains exome sequencing variants retrieved from the **Exome Variant Server (EVS)** for the NHLBI Exome Sequencing Project (ESP). The `evs` annotation data was generated from approximately 2500 exomes and `evs_5400` from approximately 5400 exomes. (7500 exomes are the next milestone for this project in the next couple of months - see their website for project details: <http://evs.gs.washington.edu/EVS/>). Currently minor allele frequencies are given for European American and African American populations - see below for additional fields that you can use for variant selection and annotation. 

The data in `evs` annotation source was retrieved from the project website on November 7, 2011, and `evs_5400` was retrieved on December 15, 2011. If you find this data useful please cite their project: 

*Exome Variant Server, NHLBI Exome Sequencing Project (ESP), Seattle, WA (URL: **<http://evs.gs.washington.edu/EVS/>**) \[December 15, 2011\] (or [November 7, 2011] for the 2500 exome version)* 



### Available databases

You should run the following command to see the availability of most recent version of the evs database: 



    % vtools show annotations evs ESP
    
    ESP-6500SI-V2-SSA137    NHLBI GO Exome Sequencing Project (Exome Variant
                            Server, NHLBI Exome Sequencing Project (ESP), Seattle,
                            WA (URL: http://evs.gs.washington.edu/EVS/) [6500
                            samples, February, 2013].)
    ESP                     NHLBI GO Exome Sequencing Project (Exome Variant
                            Server, NHLBI Exome Sequencing Project (ESP), Seattle,
                            WA (URL: http://evs.gs.washington.edu/EVS/) [6500
                            samples, February, 2013].)
    evs-6500                NHLBI GO Exome Sequencing Project (Exome Variant
                            Server, NHLBI Exome Sequencing Project (ESP), Seattle,
                            WA (URL: http://evs.gs.washington.edu/EVS/) [6500
                            samples, February, 2013].)
    evs-hg19_20111107       NHLBI GO Exome Sequencing Project (Exome Variant
                            Server,  NHLBI Exome Sequencing Project (ESP),
                            Seattle, WA (URL: http://evs.gs.washington.edu/EVS/)
                            [November, 2011].)
    evs                     NHLBI GO Exome Sequencing Project (Exome Variant
                            Server, NHLBI Exome Sequencing Project (ESP), Seattle,
                            WA (URL: http://evs.gs.washington.edu/EVS/) [6500
                            samples, February, 2013].)
    evs_5400                NHLBI GO Exome Sequencing Project (Exome Variant
                            Server,  NHLBI Exome Sequencing Project (ESP),
                            Seattle, WA (URL: http://evs.gs.washington.edu/EVS/)
                            [5400 samples, December, 2011].)


    % vtools show annotation ESP
    
    Description:            NHLBI GO Exome Sequencing Project (Exome Variant
      Server, NHLBI Exome Sequencing Project (ESP), Seattle, WA (URL:
      http://evs.gs.washington.edu/EVS/) [6500 samples, February, 2013].)
    Database type:          variant
    Number of records:      1,998,204
    Distinct variants:      1,998,173
    Reference genome hg19:  chr, pos, ref, alt
    
    Field:                  chr
    Type:                   string
    Comment:                Chromosome that the variant was found in.
    Missing entries:        0
    Unique Entries:         24
    
    Field:                  pos
    Type:                   integer
    Comment:                Location on the chromosome (NCBI 37 or hg19), 1-based.
    Missing entries:        0
    Unique Entries:         1,979,319
    Range:                  5994 - 249212579
    
    Field:                  rs_id
    Type:                   string
    Comment:                dbSNP reference SNP identifier (if available)
    Missing entries:        1,068,352 (53.5% of 1,998,204 records)
    Unique Entries:         921,262
    
    Field:                  ref
    Type:                   string
    Comment:                Variant alternate allele.
    Missing entries:        0
    Unique Entries:         8,026
    
    Field:                  alt
    Type:                   string
    Comment:                Reference allele.
    Missing entries:        0
    Unique Entries:         2,084
    
    Field:                  dbSNPVersion
    Type:                   string
    Comment:                dbSNP version which established the rs_id
    Missing entries:        0
    Unique Entries:         57
    
    Field:                  EuropeanAmericanAltCount
    Type:                   integer
    Comment:                The observed ref allele counts for the European
                            American population. Allele counts only include
                            genotypes with quality >= 30 and read depth >= 10.
    Missing entries:        0
    Unique Entries:         8,517
    Range:                  0 - 8600
    
    Field:                  EuropeanAmericanRefCount
    Type:                   integer
    Comment:                The observed ref allele counts for the European
                            American population. Allele counts only include
                            genotypes with quality >= 30 and read depth >= 10.
    Missing entries:        0
    Unique Entries:         8,599
    Range:                  0 - 8600
    
    Field:                  AfricanAmericanAltCount
    Type:                   integer
    Comment:                The observed alt allele counts for the African
                            American population. Allele counts only include
                            genotypes with quality >= 30 and read depth >= 10.
    Missing entries:        0
    Unique Entries:         4,406
    Range:                  0 - 4406
    
    Field:                  AfricanAmericanRefCount
    Type:                   integer
    Comment:                The observed ref allele counts for the African
                            American population. Allele counts only include
                            genotypes with quality >= 30 and read depth >= 10.
    Missing entries:        0
    Unique Entries:         4,407
    Range:                  0 - 4406
    
    Field:                  AllAltCount
    Type:                   integer
    Comment:                The observed alt allele counts for all populations.
                            Allele counts only include genotypes with quality >=
                            30 and read depth >= 10.
    Missing entries:        0
    Unique Entries:         12,543
    Range:                  0 - 13005
    
    Field:                  AllRefCount
    Type:                   integer
    Comment:                The observed ref allele counts for all populations.
                            Allele counts only include genotypes with quality >=
                            30 and read depth >= 10.
    Missing entries:        0
    Unique Entries:         12,971
    Range:                  0 - 13005
    
    Field:                  EuropeanAmericanMaf
    Type:                   float
    Comment:                The European American minor-allele frequency in
                            percent.
    Missing entries:        0
    Unique Entries:         67,810
    Range:                  0 - 0.650641
    
    Field:                  AfricanAmericanMaf
    Type:                   float
    Comment:                The African American minor-allele frequency in
                            percent.
    Missing entries:        0
    Unique Entries:         75,477
    Range:                  0 - 0.652047
    
    Field:                  AllMaf
    Type:                   float
    Comment:                The minor-allele frequency in percent for all
                            populations.
    Missing entries:        0
    Unique Entries:         85,231
    Range:                  7.7e-05 - 0.652174
    
    Field:                  AvgSampleReadDepth
    Type:                   integer
    Comment:                The average sample read depth.
    Missing entries:        0
    Unique Entries:         795
    Range:                  1 - 2855
    
    Field:                  Genes
    Type:                   string
    Comment:                One or more genes for which the SNP is in the coding
                            region (CCDS).
    Missing entries:        0
    Unique Entries:         19,395
    
    Field:                  GeneAccession
    Type:                   string
    Comment:                NCBI mRNA transcripts accession number.
    Missing entries:        1,998,204 (100.0% of 1,998,204 records)
    
    Field:                  FunctionGvs
    Type:                   string
    Comment:                The GVS functions are calculated by the Exome Variant
                            Server; they are based on the alleles for all
                            populations and individuals; the bases in the coding
                            region are divided into codons (if a multiple of 3),
                            and the resulting amino acids are examined.
    Missing entries:        0
    Unique Entries:         157,919
    
    Field:                  AminoAcidChange
    Type:                   string
    Comment:                The corresponding amino acid change for a SNP.
    Missing entries:        1,998,204 (100.0% of 1,998,204 records)
    
    Field:                  ProteinPos
    Type:                   string
    Comment:                The coresponding amino acid postion in a protein
                            relative to the whole protein length.
    Missing entries:        1,998,204 (100.0% of 1,998,204 records)
    
    Field:                  cDNAPos
    Type:                   integer
    Comment:                The coresponding cDNA postion for a SNP.
    Missing entries:        1,998,204 (100.0% of 1,998,204 records)
    
    Field:                  ConservationScorePhastCons
    Type:                   float
    Comment:                A number between 0 and 1 that describes the degree of
                            sequence conservation among 17 vertebrate species;
                            these numbers are downloaded from the UCSC Genome site
                            and are defined as the "posterior probability that the
                            corresponding alignment column was generated by the
                            conserved state of the phylo-HMM, given the model
                            parameters and the multiple alignment" (see UCSC
                            description).
    Missing entries:        0
    Unique Entries:         12
    Range:                  0 - .
    
    Field:                  ConservationScoreGERP
    Type:                   float
    Comment:                The rejected-substitution score from the program GERP,
                            a number between -11.6 and 5.82 that describes the
                            degree of sequence conservation among 34 mammalian
                            species, with 5.82 being the most conserved; these
                            scores were provided by Gregory M. Cooper of the
                            University of Washington Department of Genome Sciences
                            to the EVS project.
    Missing entries:        0
    Unique Entries:         187
    Range:                  -12.3 - .
    
    Field:                  GranthamScore
    Type:                   integer
    Comment:                Grantham Scores categorize codon replacements into
                            classes of increasing chemical dissimilarity based on
                            the publication by Granthan R.in 1974, Amino acid
                            difference formula to help explain protein evolution.
                            Science 1974 185:862-864.
    Missing entries:        0
    Unique Entries:         9,363
    Range:                  5 - 99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99
    
    Field:                  PolyPhenPrediction
    Type:                   string
    Comment:                Prediction of possible impact of an amino acid
                            substitution on protein structure and function based
                            on Polymorphism Phenotyping (PolyPhen) program.
    Missing entries:        0
    Unique Entries:         23,374
    
    Field:                  ChimpAllele
    Type:                   string
    Comment:                Chimp alleles are acquired from UCSC human/chimp
                            alignment files. If the variation does not fall within
                            an alignment block, or if it is an indel, the chimp
                            allele is listed as "unknown". If the variation falls
                            within a gap in the alignment, it is listed as "-".
    Missing entries:        0
    Unique Entries:         6
    
    Field:                  ClinicalLink
    Type:                   string
    Comment:                The potential clinical implications associated with a
                            SNP (limited).
    Missing entries:        0
    Unique Entries:         5,918
    
    Field:                  ExomeChip
    Type:                   string
    Comment:                Whether a SNP is on the Illumina HumanExome Chip
    Missing entries:        0
    Unique Entries:         2
    
    Field:                  FilterStatus
    Type:                   string
    Comment:                A machine-learning technique called support vector
                            machine (SVM) classification was applied for variant
                            filtering. After the initial SNP calls were generated,
                            we re-examined the BAM files to collect additional
                            information about each variant site. Based on the
                            information, variants are initially filtered by
                            individual thresholds. For example, variants with
                            posterior probability <99% (glfMultiples SNP quality
                            <20), were <5bp away from an indel detected in the
                            1000 Genomes Pilot Project, had total depth across
                            samples of <5,379 or >5,379,000 reads (~1-1000 reads
                            per sample), having >65% of reads as heterozygotes
                            carrying the variant allele or where the absolute
                            squared correlation between allele (variant or
                            reference) and strand (forward or reverse) was >0.15
                            were marked as problematic SNPs. Sites failed 3 or
                            more criteria are used as negative examples to train
                            SVM classifier. HapMap3 and OMNI polymorphic sites
                            were used as positive examples. The SVM classifier
                            produces scores for each site, and we marked ~8.5% of
                            sites at threshold 0.3 as SVM filter-failed. The
                            unfiltered set had Ti/Tv = 2.63, and the filtered set
                            had Ti/Tv =2.78.
    Missing entries:        0
    Unique Entries:         1