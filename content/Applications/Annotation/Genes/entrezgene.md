
+++
title = "EntrezGene"
description = ""
weight = 3
+++


### EntrezGene

    % vtools show annotation EntrezGene.DB
    

    Annotation database EntrezGene (version 20131028)
    Description:            Entrez Gene
      (www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=gene) is NCBI's database for
      gene-specific information. It does not include all known or predicted genes;
      instead Entrez Gene focuses on the genomes that have been completely
      sequenced, that have an active research community to contribute gene-
      specific information, or that are scheduled for intense sequence analysis.
      This database contains Entrez gene info database for Homo Sapiens,
      downloaded from ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sap
      iens.gene_info.gz.
    Database type:          range
    Reference genome hg19:  chr, start, end
      chr                   chromosome name, the same as field chromosome
      start                 Start location of the gene, retrieved from
                            EntrezGene2RefSeq.
      end                   End location of the gene, retrieved from
                            EntrezGene2RefSeq.
      tax_id                the unique identifier provided by NCBI Taxonomy for
                            the species or strain/isolate
      GeneID                the unique identifier for a gene (ASN1: geneid)
      Symbol                the default symbol for the gene (ASN1: gene->locus)
      LocusTag              the LocusTag value (ASN1:  gene->locus-tag)
      Synonyms              bar-delimited set of unofficial symbols for the gene
      dbXrefs               bar-delimited set of identifiers in other databases
                            for this gene.  The unit of the set is database:value.
      chromosome            the chromosome on which this gene is placed. for
                            mitochondrial genomes, the value 'MT' is used.
      map_location          the map location for this gene
      description           a descriptive name for this gene
      type_of_gene          the type assigned to the gene according to the list of
                            options. provided in http://www.ncbi.nlm.nih.gov/IEB/T
                            oolBox/CPP_DOC/lxr/source/src/objects/entrezgene/entre
                            zgene.asn
      Symbol_from_nomenclature_authority If exists (not NULL), indicates that this
                            symbol is from a nomenclature authority
      Full_name_from_nomenclature_authority If exists (not NULL), indicates that
                            this full name is from a nomenclature authority
      Nomenclature_status   If exists (not NULL), indicates the status of the name
                            from the nomenclature authority (O for official, I for
                            interim)
      Other_designations    pipe-delimited set of some alternate descriptions that
                            have been assigned to a GeneID '-' indicates none is
                            being reported.
      Modification_date     the last date a gene record was updated, in YYYYMMDD
                            format
    



### EntrezGene2RefSeq

This is a field database that links `gene_id` to information to `refGene`. 



    % vtools show annotation EntrezGene2RefSeq
    

    Annotation database EntrezGene2RefSeq (version 20131028)
    Description:            This database is a comprehensive report of the
      accessions that are related to a Entrez GeneID.  It includes sequences from
      the international sequence collaboration, Swiss-Prot, and RefSeq. This
      database only keeps record for human genome with reference genome Reference
      GRCh37.p13 Primary Assembly, and it also only keeps sequence on reference
      assembly (ref seq with assession type NC_).
    Database type:          field
    Reference genome *:     GeneID
      tax_id                the unique identifier provided by NCBI Taxonomy for
                            the species or strain/isolate
      GeneID                the unique identifier for a gene
      status                status of the RefSeq values are: INFERRED, MODEL, NA,
                            PREDICTED, PROVISIONAL, REVIEWED, SUPPRESSED,
                            VALIDATED
      RNA_nucleotide_accession_version may be null (-) for some genomes
      RNA_nucleotide_gi     the gi for an RNA nucleotide accession (e.g.
                            NP_047184.1, NC_004871.1)
      protein_accession_version will be null (-) for RNA-coding genes
      protein_gi            the gi for a protein accession, '-' if not applicable
      genomic_nucleotide_accession_version may be null (-) if a RefSeq was
                            provided after the genomic accession was submitted
      genomic_nucleotide_gi the gi for a genomic nucleotide accession, '-' if not
                            applicable
      start_position_on_the_genomic_accession position of the gene feature on the
                            genomic accession, adjusted to be 1-based
      end_position_on_the_genomic_accession position of the gene feature on the
                            genomic accession, adjusted to be 1-based
      orientation           orientation of the gene feature on the genomic
                            accession, '?' if not applicable
      assembly              the name of the assembly '-' if not applicable
      mature_peptide_accession_version will be null (-) if absent
      mature_peptide_gi     the gi for a mature peptide accession, '-' if not
                            applicable
      Symbol                the default symbol for the gene