
+++
title = "HugoGene"
description = ""
weight = 2
+++


# HUGO Gene Nomenclature Committee (HGNC) approved gene names


The HUGO Gene Nomenclature Committee (HGNC) has assigned unique gene symbols and names to almost 38,000 human loci, of which around 19,000 are protein coding. genenames.org is a curated online repository of HGNC-approved gene nomenclature and associated resources including links to genomic, proteomic and phenotypic information, as well as dedicated gene family pages. 



## HGNC

The HGNC annotation database is a field database that, by default, annotates another gene name field such as `refGene.name2`, through its `All_Symbols` column, which contains all current and previously used gene names. For example, for gene `TMEM261` with a previously used name `C9orf123`, it has two entries in the database, 



    name       All_Symbols
    TMEM261    TMEM261
    TMEM261    C9orf123
    

so that the `name` field will have its HGNC approved name `TMEM261`. To link to this database, you should do, for example, 



    % vtools use HGNC --linked_by refGene.name2
    

    INFO: Downloading annotation database from annoDB/HGNC.ann
    INFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/HGNC-20131029.DB.gz
    INFO: Using annotation DB HGNC in project test.
    INFO: The HUGO Gene Nomenclature Committee (HGNC) has assigned unique gene symbols
    and names to almost 38,000 human loci, of which around 19,000 are protein coding.
    genenames.org is a curated online repository of HGNC-approved gene nomenclature and
    associated resources including links to genomic, proteomic and phenotypic information,
    as well as dedicated gene family pages
    INFO: 22889 out of 23953 refgene.name2 are annotated through annotation database HGNC
    WARNING: 30614 out of 53503 values in annotation database HGNC are not linked to the project.
    

Note that not all names in `refGene` have an entry in `HGNC`. Genes that are not in `HGNC` are mostly `LOC?????` genes. Then, instead of output `refGene.name2`, you can output HGNC approved name 



    % vtools output variant chr pos HGNC.name
    

You can, if you are interested, check the change of names using commands 



    % vtools select variant 'refGene.name2 != HGNC.name' --output chr pos refGene.name2 HGNC.name --all
    

although variants that belong to more than one gene will also be selected and outputted. 



    % vtools show annotation HGNC
    

    Annotation database HGNC (version 20131029)
    Description:            The HUGO Gene Nomenclature Committee (HGNC) has
      assigned unique gene symbols and names to almost 38,000 human loci, of which
      around 19,000 are protein coding. genenames.org is a curated online
      repository of HGNC-approved gene nomenclature and associated resources
      including links to genomic, proteomic and phenotypic information, as well as
      dedicated gene family pages
    Database type:          field
    Reference genome *:     All_Symbols
      name                  HGNC Approved Symbol
      All_Symbols           All symbols, including Approved and repvious symbols
      HGNC_ID               A unique ID provided by the HGNC. In the HTML results
                            page this ID links to the HGNC Symbol Report for that
                            gene.
      Approved_Symbol       The official gene symbol that has been approved by the
                            HGNC and is publicly available. Symbols are approved
                            based on specific HGNC nomenclature guidelines. In the
                            HTML results page this ID links to the HGNC Symbol
                            Report for that gene.
      Approved_Name         The official gene name that has been approved by the
                            HGNC and is publicly available. Names are approved
                            based on specific HGNC nomenclature guidelines.
      Status                Indicates whether the gene is classified as: Approved
                            - these genes have HGNC-approved gene symbols Entry
                            withdrawn - these previously approved genes are no
                            longer thought to exist Symbol withdrawn - a
                            previously approved record that has since been merged
                            into a another record
      Locus_Type            Specifies the type of locus described by the given
                            entry: gene with protein product, RNA, cluster, etc (h
                            ttp://www.genenames.org/data/gdlw_columndef.html#gd_ap
                            p_sym)
      Locus_Group           Groups locus types together into related sets. See
                            http://www.genenames.org/data/gdlw_columndef.html#gd_a
                            pp_sym for details.
      Previous_Symbols      Symbols previously approved by the HGNC for this gene
      Previous_Names        Gene names previously approved by the HGNC for this
                            gene
      Synonyms              Other symbols used to refer to this gene
      Name_Synonyms         Other names used to refer to this gene
      Chromosome            Indicates the location of the gene or region on the
                            chromosome
      Date_Approved         Date the gene symbol and name were approved by the
                            HGNC
      Date_Modified         If applicable, the date the entry was modified by the
                            HGNC
      Date_Symbol_Changed   If applicable, the date the gene symbol was last
                            changed by the HGNC from a previously approved symbol.
                            Many genes receive approved symbols and names which
                            are viewed as temporary (eg C2orf#) or are non-ideal
                            when considered in the light of subsequent
                            information. In the case of individual genes a change
                            to the name (and subsequently the symbol) is only made
                            if the original name is seriously misleading.
      Date_Name_Changed     If applicable, the date the gene name was last changed
                            by the HGNC from a previously approved name
      Accession_Numbers     Accession numbers for each entry selected by the HGNC
      Enzyme_IDs            Enzyme entries have Enzyme Commission (EC) numbers
                            associated with them that indicate the hierarchical
                            functional classes to which they belong
      Entrez_Gene_ID        Entrez Gene at the NCBI provide curated sequence and
                            descriptive information about genetic loci including
                            official nomenclature, synonyms, sequence accessions,
                            phenotypes, EC numbers, MIM numbers, UniGene clusters,
                            homology, map locations, and related web sites. In the
                            HTML results page this ID links to the Entrez Gene
                            page for that gene. Entrez Gene has replaced
                            LocusLink.
      Ensembl_Gene_ID       This column contains a manually curated Ensembl Gene
                            ID
      Mouse_Genome_Database_ID MGI identifier. In the HTML results page this ID
                            links to the MGI Report for that gene.
      Specialist_Database_Links This column contains links to specialist databases
                            with a particular interest in that symbol/gene (also
                            see Specialist Database IDs).
      Specialist_Database_IDs The Specialist Database Links column contains HTML
                            links to the database in question. This column
                            contains the database ID only.
      Pubmed_IDs            Identifier that links to published articles relevant
                            to the entry in the NCBI's PubMed database.
      RefSeq_IDs            The Reference Sequence (RefSeq) identifier for that
                            entry, provided by the NCBI. As we do not aim to
                            curate all variants of a gene only one selected RefSeq
                            is displayed per gene report. RefSeq aims to provide a
                            comprehensive, integrated, non-redundant set of
                            sequences, including genomic DNA, transcript (RNA),
                            and protein products. RefSeq identifiers are designed
                            to provide a stable reference for gene identification
                            and characterization, mutation analysis, expression
                            studies, polymorphism discovery, and comparative
                            analyses.
      Gene_Family_Tag       Tag used to designate a gene family or group the gene
                            has been assigned to, according to either sequence
                            similarity or information from publications,
                            specialist advisors for that family or other
                            databases. Families/groups may be either structural or
                            functional, therefore a gene may belong to more than
                            one family/group. These tags are used to generate gene
                            family or grouping specific pages at genenames.org and
                            do not necessarily reflect an official nomenclature.
                            Each gene family has an associated gene family tag and
                            gene family description. If a particular gene is a
                            member of more than one gene family, the tags and the
                            descriptions will be shown in the same order.
      Gene_family_description Name given to a particular gene family. The gene
                            family description has an associated gene family tag.
                            Gene families are used to group genes according to
                            either sequence similarity or information from
                            publications, specialist advisors for that family or
                            other databases. Families/groups may be either
                            structural or functional, therefore a gene may belong
                            to more than one family/group.
      Record_Type
      Primary_IDs
      Secondary_IDs
      CCDS_IDs              The Consensus CDS (CCDS) project is a collaborative
                            effort to identify a core set of human and mouse
                            protein coding regions that are consistently annotated
                            and of high quality. The long term goal is to support
                            convergence towards a standard set of gene
                            annotations.
      VEGA_IDs              This contains a curated VEGA gene ID
      Locus_Specific_Databases This contains a list of links to databases or
                            database entries pertinent to the gene
      Entrez_Gene_ID_NCBI   Entrez Gene at the NCBI provide curated sequence and
                            descriptive information about genetic loci including
                            official nomenclature, synonyms, sequence accessions,
                            phenotypes, EC numbers, MIM numbers, UniGene clusters,
                            homology, map locations, and related web sites. In the
                            HTML results page this ID links to the Entrez Gene
                            page for that gene. Entrez Gene has replaced
                            LocusLink.
      OMIM_ID_NCBI          Identifier provided by Online Mendelian Inheritance in
                            Man (OMIM) at the NCBI. This database is described as
                            a catalog of human genes and genetic disorders
                            containing textual information and links to MEDLINE
                            and sequence records in the Entrez system, and links
                            to additional related resources at NCBI and elsewhere.
                            In the HTML results page this ID links to the OMIM
                            page for that entry.
      RefSeq_NCBI           The Reference Sequence (RefSeq) identifier for that
                            entry, provided by the NCBI. As we do not aim to
                            curate all variants of a gene only one mapped RefSeq
                            is displayed per gene report. RefSeq aims to provide a
                            comprehensive, integrated, non-redundant set of
                            sequences, including genomic DNA, transcript (RNA),
                            and protein products. RefSeq identifiers are designed
                            to provide a stable reference for gene identification
                            and characterization, mutation analysis, expression
                            studies, polymorphism discovery, and comparative
                            analyses. In the HTML results page this ID links to
                            the RefSeq page for that entry.
      UniProt_ID            The UniProt identifier, provided by the EBI. The
                            UniProt Protein Knowledgebase is described as a
                            curated protein sequence database that provides a high
                            level of annotation, a minimal level of redundancy and
                            high level of integration with other databases. In the
                            HTML results page this ID links to the UniProt page
                            for that entry.
      Ensembl_ID_Ensembl    The Ensembl ID is derived from the current build of
                            the Ensembl database and provided by the Ensembl team.
      UCSC_ID               The UCSC ID is derived from the current build of the
                            UCSC database
      Mouse_Genome_Database_ID_MGI MGI identifier. In the HTML results page this
                            ID links to the MGI Report for that gene.
      Rat_Genome_Database_ID_RGD RGD identifier. In the HTML results page this ID
                            links to the RGD Report for that gene.