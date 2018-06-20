
+++
title = "CancerGeneCensus"
weight = 6
+++

## Cancer Genome Census

### 1. Data source

This database contains variants from the Cancer Genome Project. It is "an ongoing effort to catalogue those genes for which mutations have been causally implicated in cancer. The original census and analysis was published in Nature Reviews Cancer and supplemental analysis information related to the paper is also available. Currently, more than 1% of all human genes are implicated via mutation in cancer. Of these, approximately 90% have somatic mutations in cancer, 20% bear germline mutations that predispose to cancer and 10% show both somatic and germline mutations." [{1}][1] 


{{% notice warning%}}
Not all genes are available in the knownGene or refGene database so you will lose a few genes if you try to find all variants within these cancer genes through location information of knownGene or refGene. The latest version of Cancer Gene Census lists the following genes that are not available in refGene.name2: `AMER1, C12orf9, CDKN2a, FAM22B, H3F3AP4, IGH, IGK@, IGL@, KMT2A, KMT2B, KMT2C, NUTM1, NUTM2A, TCRB, TRA, TRD`. 
{{%/notice%}}


### 2. Usage

This database should be linked to a field of common gene name, e.g. `refGene.name2`. You can use load it by 



    vtools use refGene
    vtools use CancerGeneCensus --linked_by refGene.name2
    

    NFO: Downloading annotation database from http://vtools.houstonbioinformatics.org/annoDB/CancerGeneCensus-20130711.DB.gz
    INFO: Using annotation DB CancerGeneCensus in project ra.
    INFO: This database contains variants from the Cancer Genome Project. It is
    an ongoing effort to catalogue those genes for which mutations have been causally
    implicated in cancer. The original census and analysis was published in Nature
    Reviews Cancer and supplemental analysis information related to the paper is also
    available. Currently, more than 1% of all human genes are implicated via mutation
    in cancer. Of these, approximately 90% have somatic mutations in cancer, 20% bear
    germline mutations that predispose to cancer and 10% show both somatic and
    germline mutations.
    INFO: 471 out of 23242 refgene.name2 are annotated through annotation database CancerGeneCensus
    WARNING: 16 out of 487 values in annotation database CancerGeneCensus are not linked to the project.
    

If you would like to use the knownGene database, you will have to link through `knownGene.name`. The command to use would be 



    vtools use knownGene
    vtools use CancerGeneCensus --linked_by knownGene.name --linked_field kgID
    

    INFO: Using annotation DB CancerGeneCensus in project ra.
    INFO: This database contains variants from the Cancer Genome Project. It is
    an ongoing effort to catalogue those genes for which mutations have been causally
    implicated in cancer. The original census and analysis was published in Nature
    Reviews Cancer and supplemental analysis information related to the paper is also
    available. Currently, more than 1% of all human genes are implicated via mutation
    in cancer. Of these, approximately 90% have somatic mutations in cancer, 20% bear
    germline mutations that predispose to cancer and 10% show both somatic and
    germline mutations.
    INFO: 433 out of 80922 knowngene.name are annotated through annotation database CancerGeneCensus
    WARNING: 54 out of 487 values in annotation database CancerGeneCensus are not linked to the project.
    



### 3. Fields

    Description: Cancer Genome Project
    Database type: field
    Number of records: 487
    Number of distinct entries: 485
    Reference genome *: ['kgID']
    
    Field:           GeneSymbol
    Type:            string
    Missing entries: 0
    Unique Entries:  484
    
    Field:           kgID
    Type:            string
    Missing entries: 0
    Unique Entries:  485
    
    Field:           Name
    Type:            string
    Missing entries: 0
    Unique Entries:  487
    
    Field:           GeneID
    Type:            string
    Missing entries: 0
    Unique Entries:  485
    
    Field:           Chr
    Type:            string
    Missing entries: 0
    Unique Entries:  24
    
    Field:           ChrBand
    Type:            string
    Missing entries: 0
    Unique Entries:  343
    
    Field:           CancerSomaticMut
    Type:            string
    Missing entries: 0
    Unique Entries:  2
    
    Field:           CancerGermlineMut
    Type:            string
    Missing entries: 0
    Unique Entries:  3
    
    Field:           TumourTypesSomatic
    Type:            string
    Missing entries: 0
    Unique Entries:  230
    
    Field:           TumourTypesGermline
    Type:            string
    Missing entries: 0
    Unique Entries:  59
    
    Field:           CancerSyndrome
    Type:            string
    Missing entries: 0
    Unique Entries:  66
    
    Field:           TissueType
    Type:            string
    Missing entries: 0
    Unique Entries:  26
    
    Field:           CancerMolecularGenetics
    Type:            string
    Missing entries: 0
    Unique Entries:  9
    
    Field:           MutationType
    Type:            string
    Missing entries: 0
    Unique Entries:  77
    
    Field:           TranslocationPartner
    Type:            string
    Missing entries: 0
    Unique Entries:  159
    
    Field:           OtherGermlineMut
    Type:            string
    Missing entries: 0
    Unique Entries:  3
    
    Field:           OtherSyndromeOrDisease
    Type:            string
    Missing entries: 0
    Unique Entries:  33
    



### 4. Abbreviations

    Abbreviation	Term
    A	 amplification
    AEL	 acute eosinophilic leukemia
    AL	 acute leukemia
    ALCL	 anaplastic large-cell lymphoma
    ALL	 acute lymphocytic leukemia
    AML	 acute myelogenous leukemia
    AML*	 acute myelogenous leukemia (primarily treatment associated)
    APL	 acute promyelocytic leukemia
    B-ALL	 B-cell acute lymphocytic leukaemia
    B-CLL	 B-cell Lymphocytic leukemia
    B-NHL	 B-cell Non-Hodgkin Lymphoma
    CLL	 chronic lymphatic leukemia
    CML	 chronic myeloid leukemia
    CMML	 chronic myelomonocytic leukemia
    CNS	 central nervous system
    D	 large deletion
    DFSP	 dermatofibrosarcoma protuberans
    DLBCL	 diffuse large B-cell lymphoma
    DLCL	 diffuse large-cell lymphoma
    Dom	 dominant
    E	 epithelial
    F	 frameshift
    GIST	 gastrointestinal stromal tumour
    JMML	 juvenile myelomonocytic leukemia
    L	 leukaemia/lymphoma
    M	 mesenchymal
    MALT	 mucosa-associated lymphoid tissue lymphoma
    MDS	 myelodysplastic syndrome
    Mis	 Missense
    MLCLS	 mediastinal large cell lymphoma with sclerosis
    MM	 multiple myeloma
    MPD	 Myeloproliferative disorder
    N	 nonsense
    NHL	 non-Hodgkin lymphoma
    NK/T	 natural killer T cell
    NSCLC	 non small cell lung cancer
    O	 other
    PMBL	 primary mediastinal B-cell lymphoma
    pre-B All	 pre-B-cell acute lymphoblastic leukaemia
    Rec	 reccesive
    S	 splice site
    T	 translocation
    T-ALL	 T-cell acute lymphoblastic leukemia
    T-CLL	 T-cell chronic lymphocytic leukaemia
    TGCT	 testicular germ cell tumour
    T-PLL	 T cell prolymphocytic leukaemia
    



### 5. Examples

#### 5.1 Find variants belong to one of the cancer genes

    vtools use CancerGeneCensus --linked_by refGene.name2
    vtools select variant 'GeneSymbol is not NULL' -t CancerVariants
    



#### 5.2 Find variants that are in 5kb up and downstream of some cancer genes.

If you are interested in only some of the cancer genes, but would like to get variants not only within the genes, but also up and downstream of these genes, you will first have to get a list of genes. 

For example, you can run 



    vtools execute select GeneSymbol from CancerGeneCensus
    

to get a list of cancer genes. 

Then, to locate variants in a different region as the default range of the `refGene` database (from `txStart` to `txEnd`), you will need to re-use the `refGene` database using command 



    vtools use refGene --linked_fields chr 'txStart-5000', 'txEnd+5000'
    

Then, you can use the following commands to create tables of variants for each gene: 



    for gene in GENE1 GENE2 GENE3
    do
        vtools select variant "refGene.name2='${gene}'" -t \\({gene}_ext
    done

 [1]: http://www.sanger.ac.uk/genetics/CGP/Census/