
+++
title = "COSMIC"
weight = 1
+++



## Catalogue of Somatic Mutations in Cancer


COSMIC (Catalogue of Somatic Mutations in Cancer) is a data resource that is designed to store and display somatic mutation information and related details and contains information relating to human cancers. Data in COSMIC is curated from known Cancer Genes Literature and Systematic Screens. COSMIC data is freely downloadable in many formats on the project's FTP site: <ftp://ftp.sanger.ac.uk/pub/CGP/cosmic>. 

If you use COSMIC annotations, please credit the project with the following acknowledgement: 

*The mutation data was obtained from the Sanger Institute Catalogue Of Somatic Mutations In Cancer web site, <http://www.sanger.ac.uk/cosmic>. Bamford et al (2004). The COSMIC (Catalogue of Somatic Mutations in Cancer) database and website. Br J Cancer, 91,355-358.* 

There are 3 data sources that you can use to annotate vtools project variants with those from the COSMIC project. There are 2 higher-level databases that annotate variants with information such as how many cancer samples have been documented to contain the variant. These databases include a database that annotates coding mutations (**CosmicCodingMuts**) and a database that annotates noncoding variants (**CosmicNonCodingVariants**). 

There is also a more detailed database (**CosmicMutantExport**) that can be linked to these higher-level databases (e.g., `vtools use CosmicMutantExport --linkedby CosmicCodingMuts.COSMIC_ID` or `vtools use CosmicMutantExport --linked_by CosmicNonCodingVariants.COSMIC_ID`) to extract detailed information about the COSMIC variant (such as variant details and details of the samples the variant was detected in). See below for the available annotation fields from these databases. 



    % vtools use CosmicCodingMuts
    % vtools show annotation CosmicCodingMuts -v2
    
    Annotation database CosmicCodingMuts (version v61_260912)
    Description: Cosmic coding mutation database.  This data contains mutations 
    affecting 10 or less nucleotides in REF.  The mutation data was obtained 
    from the Sanger Institute Catalogue Of Somatic Mutations In Cancer web site, 
    http://www.sanger.ac.uk/cosmic.  Bamford et al (2004). The COSMIC (Catalogue 
    of Somatic Mutations in Cancer) database and website. Br J Cancer, 91,355-358.
    Database type: variant
    Number of records: 216,900
    Number of distinct variants: 198,331
    Reference genome hg19: ['chr', 'pos', 'ref', 'alt']
    
    Field:           chr
    Type:            string
    Comment:         Chromosome
    Missing entries: 0 
    Unique Entries:  25
    
    Field:           pos
    Type:            integer
    Comment:         1-based position
    Missing entries: 0 
    Unique Entries:  193,076
    Range:           8115 - 249212084
    
    Field:           COSMIC_ID
    Type:            string
    Comment:         cosmic id of mutation
    Missing entries: 0 
    Unique Entries:  216,900
    
    Field:           ref
    Type:            string
    Comment:         Reference allele, '-' for insertion.
    Missing entries: 0 
    Unique Entries:  1,241
    
    Field:           alt
    Type:            string
    Comment:         Alternative allele, '-' for deletion.
    Missing entries: 0 
    Unique Entries:  1,138
    
    Field:           gene
    Type:            string
    Comment:         genename
    Missing entries: 0 
    Unique Entries:  20,405
    
    Field:           strand
    Type:            string
    Comment:         strand
    Missing entries: 0 
    Unique Entries:  2
    
    Field:           CDS
    Type:            string
    Comment:         CDS annotation
    Missing entries: 0 
    Unique Entries:  65,794
    
    Field:           AA
    Type:            string
    Comment:         Peptide annotation
    Missing entries: 0 
    Unique Entries:  111,311
    
    Field:           CNT
    Type:            integer
    Comment:         Number of samples with this mutation
    Missing entries: 0 
    Unique Entries:  157
    Range:           1 - 29906
    

    % vtools use CosmicNonCodingVariants
    % vtools show annotation CosmicNonCodingVariants -v2 

    Annotation database CosmicNonCodingVariants (version v61_260912)
    Description: Cosmic non-coding mutation database.  This data contains 
    mutations affecting 10 or less nucleotides in REF.  The mutation data 
    was obtained from the Sanger Institute Catalogue Of Somatic Mutations 
    In Cancer web site, http://www.sanger.ac.uk/cosmic.  Bamford et al 
    (2004). The COSMIC (Catalogue of Somatic Mutations in Cancer) database 
    and website. Br J Cancer, 91,355-358.
    Database type: variant
    Number of records: 108,713
    Number of distinct variants: 104,410
    Reference genome hg19: ['chr', 'pos', 'ref', 'alt']
    
    Field:           chr
    Type:            string
    Comment:         Chromosome
    Missing entries: 0 
    Unique Entries:  24
    
    Field:           pos
    Type:            integer
    Comment:         1-based position
    Missing entries: 0 
    Unique Entries:  104,370
    Range:           13663 - 249204167
    
    Field:           COSMIC_ID
    Type:            string
    Comment:         cosmic id of mutation
    Missing entries: 0 
    Unique Entries:  108,713
    
    Field:           ref
    Type:            string
    Comment:         Reference allele, '-' for insertion.
    Missing entries: 0 
    Unique Entries:  1,251
    
    Field:           alt
    Type:            string
    Comment:         Alternative allele, '-' for deletion.
    Missing entries: 0 
    Unique Entries:  152
    
    Field:           gene
    Type:            string
    Comment:         genename
    Missing entries: 88,900 (81.8% of 108,713 records)
    Unique Entries:  7,501
    
    Field:           strand
    Type:            string
    Comment:         strand
    Missing entries: 88,900 (81.8% of 108,713 records)
    Unique Entries:  2
    

    % vtools use CosmicMutantExport --linked_by CosmicCodingMuts.COSMIC_ID
    % vtools show annotation CosmicMutantExport -v2
    
    Annotation database CosmicMutantExport (version v61_260912)
    Description: Cosmic mutant export.  This data contains all coding 
    point mutations.  The mutation data was obtained from the Sanger 
    Institute Catalogue Of Somatic Mutations In Cancer web site, 
    http://www.sanger.ac.uk/cosmic.  Bamford et al (2004). The 
    COSMIC (Catalogue of Somatic Mutations in Cancer) database and 
    website. Br J Cancer, 91,355-358.
    Database type: field
    Number of records: 404,865
    Number of distinct entries: 224,650
    Reference genome *: ['COSMIC_ID']
    
    Field:           COSMIC_ID
    Type:            string
    Missing entries: 0 
    Unique Entries:  224,650
    
    Field:           Gene_name
    Type:            string
    Missing entries: 0 
    Unique Entries:  20,451
    
    Field:           Accession_Number
    Type:            string
    Missing entries: 0 
    Unique Entries:  20,403
    
    Field:           Gene_CDS_length
    Type:            string
    Missing entries: 0 
    Unique Entries:  2,220
    
    Field:           HGNC_ID
    Type:            string
    Missing entries: 0 
    Unique Entries:  16,990
    
    Field:           Sample_name
    Type:            string
    Missing entries: 0 
    Unique Entries:  179,301
    
    Field:           ID_sample
    Type:            string
    Missing entries: 0 
    Unique Entries:  183,630
    
    Field:           ID_tumour
    Type:            string
    Missing entries: 0 
    Unique Entries:  181,851
    
    Field:           Primary_site
    Type:            string
    Missing entries: 0 
    Unique Entries:  44
    
    Field:           Site_subtype
    Type:            string
    Missing entries: 0 
    Unique Entries:  185
    
    Field:           Primary_histology
    Type:            string
    Missing entries: 0 
    Unique Entries:  91
    
    Field:           Histology_subtype
    Type:            string
    Missing entries: 0 
    Unique Entries:  417
    
    Field:           Genomewide_screen
    Type:            string
    Missing entries: 0 
    Unique Entries:  3
    
    Field:           Mutation_ID
    Type:            string
    Missing entries: 0 
    Unique Entries:  224,650
    
    Field:           Mutation_CDS
    Type:            string
    Missing entries: 0 
    Unique Entries:  69,434
    
    Field:           Mutation_AA
    Type:            string
    Missing entries: 0 
    Unique Entries:  115,530
    
    Field:           Mutation_Description
    Type:            string
    Missing entries: 0 
    Unique Entries:  17
    
    Field:           Mutation_zygosity
    Type:            string
    Missing entries: 0 
    Unique Entries:  4
    
    Field:           Mutation_NCBI36_genome_position
    Type:            string
    Missing entries: 0 
    Unique Entries:  35,240
    
    Field:           Mutation_NCBI36_strand
    Type:            string
    Missing entries: 0 
    Unique Entries:  4
    
    Field:           Mutation_GRCh37_genome_position
    Type:            string
    Missing entries: 0 
    Unique Entries:  198,031
    
    Field:           Mutation_GRCh37_strand
    Type:            string
    Missing entries: 0 
    Unique Entries:  4
    
    Field:           Mutation_somatic_status
    Type:            string
    Missing entries: 0 
    Unique Entries:  7
    
    Field:           Pubmed_PMID
    Type:            string
    Missing entries: 0 
    Unique Entries:  7,690
    
    Field:           Sample_source
    Type:            string
    Missing entries: 0 
    Unique Entries:  30
    
    Field:           Tumour_origin
    Type:            string
    Missing entries: 0 
    Unique Entries:  9
    
    Field:           Comments
    Type:            string
    Missing entries: 0 
    Unique Entries:  3,202