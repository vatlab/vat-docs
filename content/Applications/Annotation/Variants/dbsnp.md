
+++
title = "dbSNP"
description = ""
weight = 3
+++


# dbSNP annotation databases


The default version of our **dbSNP** annotation is currently referring to dbSNP143 (using hg38 coordinates) as shown below. However, users can also retrieve older versions of dbSNP: dbSNP141, dbSNP138, dbSNP137, dbSNP135, dbSNP132, dbSNP131, dbSNP130, dbSNP129. The 129 and 130 versions use hg18 as a reference genome, 131, 132, 135, 137, 138 and 141 use hg19 and 143 uses hg38. The archived versions can be used by a variant tools project by referring to their specific names - for example: **dbSNP-hg18_129**. 



1.  dbSNP143 has many more flags and fields than previous versions. It also does not contain all variants that are defined in dbSNP141 and earlier. 
2.  A dbSNP entry might match multiple variants. For example, `rs111688037` matches variants `T->A` and `T->C` at `chr6:31602679`. 



### version 

    % vtools show annotation dbSNP -v1
    

    Annotation database dbSNP (version hg38_143)
    Description:            dbSNP version 143, created using vcf file downloaded from NCBI
    Database type:          variant
    Reference genome hg38:  chr, pos, ref, alt
      chr (char)
      pos (int)
      name (char)           DB SNP ID (rsname)
      ref (char)            Reference allele (as on the + strand)
      alt (char)            Alternative allele (as on the + strand)
      FILTER (char)         Inconsistent Genotype Submission For At Least One Sample
      RS (int)              dbSNP ID (i.e. rs number)
      RSPOS (int)           Chr position reported in dbSNP
      RV (int)              RS orientation is reversed
      VP (char)             Variation Property. Documentation 
                            is at ftp://ftp.ncbi.nlm.nih.gov/snp/specs/dbSNP_BitField_latest.pdf
      GENEINFO (char)       Pairs each of gene symbol:gene id.  
                            The gene symbol and id are delimited by a colon (:)
                            and each pair is delimited by a vertical bar (|)
      dbSNPBuildID (int)    First dbSNP Build for RS
      SAO (int)             Variant Allele Origin: 0 - unspecified, 1 - Germline, 2 - Somatic,
                            3 - Both
      SSR (int)             Variant Suspect Reason Codes (may be more than one value
                            added together)
                            0 - unspecified, 1 - Paralog, 2 - byEST, 4 - oldAlign, 8 - Para_EST, 
                            16 - 1kg_failed, 1024 - other
      WGT (int)             Weight, 00 - unmapped, 1 - weight 1, 2 - weight 2, 3 - weight 3 or 
                            more
      VC (char)             Variation Class
      PM_flag (int)         Variant is Precious(Clinical,Pubmed Cited)
      TPA_flag (int)        Provisional Third Party Annotation(TPA)
                            (currently rs from PHARMGKB who will give phenotype data)
      PMC_flag (int)        Links exist to PubMed Central article
      S3D_flag (int)        Has 3D structure - SNP3D table
      SLO_flag (int)        Has SubmitterLinkOut - From SNP->SubSNP->Batch.link_out
      NSF_flag (int)        Has non-synonymous frameshift A coding region variation where one 
                            allele in the set changes all downstream amino acids. 
                            FxnClass = 44
      NSM_flag (int)        Has non-synonymous missense A coding region variation where one 
                            allele in the set changes protein peptide. FxnClass = 42
      NSN_flag (int)        Has non-synonymous nonsense A coding region variation where one 
                            allele in the set changes to STOP codon (TER). FxnClass = 41
      REF_flag_flag (int)   Has reference A coding region variation where one allele in the 
                            set is identical to the reference sequence. FxnCode = 8
      SYN_flag (int)        Has synonymous A coding region variation where one allele in the 
                            set does not change the encoded amino acid. FxnCode = 3
      U3_flag (int)         In 3' UTR Location is in an untranslated region (UTR). 
                            FxnCode = 53
      U5_flag (int)         In 5' UTR Location is in an untranslated region (UTR). 
                            FxnCode = 55
      ASS_flag (int)        In acceptor splice site FxnCode = 73
      DSS_flag (int)        In donor splice-site FxnCode = 75
      INT_flag (int)        In Intron FxnCode = 6
      R3_flag (int)         In 3' gene region FxnCode = 13
      R5_flag (int)         In 5' gene region FxnCode = 15
      OTH_flag (int)        Has other variant with exactly the same set of mapped positions on 
                            NCBI refernce assembly.
      CFL_flag (int)        Has Assembly conflict. This is for weight 1 and 2 variant that maps to
                            different chromosomes on different assemblies.
      ASP_flag (int)        Is Assembly specific. This is set if the variant only maps to one 
                            assembly
      MUT_flag (int)        Is mutation (journal citation, explicit fact): a low frequency 
                            variation that is cited in journal and other reputable sources
      VLD_flag (int)        Is Validated.  This bit is set if the variant has 2+ minor 
                            allele count based on frequency or genotype data.
      G5A_flag (int)        >5% minor allele frequency in each and all populations
      G5_flag (int)         >5% minor allele frequency in 1+ populations
      HD_flag (int)         Marker is on high density genotyping kit (50K density or greater).
                            The variant may have phenotype associations present in dbGaP.
      GNO_flag (int)        Genotypes available. The variant has individual genotype 
                            (in SubInd table).
      KGValidated_flag (int)
                            1000 Genome validated
      KGPhase1_flag (int)   1000 Genome phase 1 (incl. June Interim phase 1)
      KGPilot123_flag (int) 1000 Genome discovery all pilots 2010(1,2,3)
      KGPROD_flag (int)     Has 1000 Genome submission
      OTHERKG_flag (int)    non-1000 Genome submission
      PH3_flag (int)        HAP_MAP Phase 3 genotyped: filtered, non-redundant
      CDA_flag (int)        Variation is interrogated in a clinical diagnostic assay
      LSD_flag (int)        Submitted from a locus-specific database
      MTP_flag (int)        Microattribution/third-party annotation(TPA:GWAS,PAGE)
      OM_flag (int)         Has OMIM/OMIA
      NOC_flag (int)        Contig allele not present in variant allele list.
                            The reference sequence allele at the mapped position is not 
                            present in the variant allele list, adjusted for orientation.
      WTD_flag (int)        Is Withdrawn by submitter If one member ss is withdrawn by submitter,
                            then this bit is set.  If all member ss' are withdrawn,
                            then the rs is deleted to SNPHistory
      NOV_flag (int)        Rs cluster has non-overlapping allele sets.
                            True when rs set has more than 2 alleles from different submissions
                            and these sets share no alleles in common.
      CAF (char)            An ordered, comma delimited list of allele frequencies based on
                            1000Genomes, starting with the reference allele
                            followed by alternate alleles as ordered in the ALT column.
                            Where a 1000Genomes alternate allele is not in the dbSNPs alternate
                            allele set, the allele is added to the ALT column.
                            The minor allele is the second largest value in the list, and
                            was previuosly reported in VCF as the GMAF.
                            This is the GMAF reported on the RefSNP and EntrezSNP pages 
                            and VariationReporter
      COMMON (int)          RS is a common SNP.  A common SNP is one that has at least one 
                            1000Genomes population with a minor allele of frequency >= 1% 
                            and for which 2 or more founders contribute to that
                            minor allele frequency.
    



### version 141 and earlier

    % vtools show annotation dbSNP-hg19_141 -v2
    

    Annotation database dbSNP (version hg19_141)
    Description:            dbSNP version 141
    Database type:          variant
    Number of records:      58,691,269
    Distinct variants:      57,577,990
    Reference genome hg19:  chr, start, refNCBI, alt
    
    Field:                  chr
    Type:                   string
    Missing entries:        0 
    Unique Entries:         25
    
    Field:                  start
    Type:                   integer
    Comment:                start position in chrom (1-based)
    Missing entries:        0 
    Unique Entries:         48,758,859
    Range:                  56 - 249240605
    
    Field:                  end
    Type:                   integer
    Comment:                end position in chrom (1-based). start=end means zero-length feature
    Missing entries:        0 
    Unique Entries:         48,957,633
    Range:                  56 - 249240605
    
    Field:                  name
    Type:                   string
    Comment:                dbSNP reference SNP identifier
    Missing entries:        0 
    Unique Entries:         58,096,504
    
    Field:                  strand
    Type:                   string
    Comment:                which DNA strand contains the observed alleles
    Missing entries:        0 
    Unique Entries:         2
    
    Field:                  refNCBI
    Type:                   string
    Comment:                Reference genomic sequence from dbSNP
    Missing entries:        0 
    Unique Entries:         164,868
    
    Field:                  refUCSC
    Type:                   string
    Comment:                Reference genomic sequence from UCSC lookup of chrom,chromStart,
                            chromEnd
    Missing entries:        0 
    Unique Entries:         187,096
    
    Field:                  observed
    Type:                   string
    Comment:                Strand-specific observed alleles
    Missing entries:        0 
    Unique Entries:         205,862
    
    Field:                  alt
    Type:                   string
    Comment:                alternate allele on the '+' strand
    Missing entries:        0 
    Unique Entries:         30,716
    
    Field:                  molType
    Type:                   string
    Comment:                sample type, can be one of unknown, genomic or cDNA
    Missing entries:        0 
    Unique Entries:         3
    
    Field:                  class
    Type:                   string
    Comment:                Class of variant (single, in-del, het, named, mixed,
                            insertion, deletion etc
    Missing entries:        0 
    Unique Entries:         6
    
    Field:                  valid
    Type:                   string
    Comment:                validation status, can be unknown, by-cluster, by-frequency,
                            by-submitter, by-2hit-2allele, by-hapmap, and by-1000genomes
    Missing entries:        0 
    Unique Entries:         63
    
    Field:                  avHet
    Type:                   float
    Comment:                Average heterozygosity from all observations
    Missing entries:        0 
    Unique Entries:         39,766
    Range:                  0 - 0.999999
    
    Field:                  avHetSE
    Type:                   float
    Comment:                Standard error for the average heterozygosity
    Missing entries:        0 
    Unique Entries:         46,007
    Range:                  0 - 0.305748
    
    Field:                  func
    Type:                   string
    Comment:                Functional cetegory of the SNP (coding-synon, coding-nonsynon,
                            intron, etc.)
    Missing entries:        0 
    Unique Entries:         648
    
    Field:                  locType
    Type:                   string
    Comment:                Type of mapping inferred from size on reference.
    Missing entries:        0 
    Unique Entries:         6