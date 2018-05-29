+++
title = "Detailed analysis"
weight = 7
hidden = true
+++


## Analysis of one genetic variant



### 1. Data

After some preliminary analysis, we find one particular variant (`179248034` on chromosome 5) in gene `SQSTM1` that is likely to be associated with a phenotype. Let us try to find more information about this variant, which is in a variant table named `MyVar` in our project. 



### 2. Gene and mRNA

We first would like to download and use the ref gene database to our project. To learn what fields are available in this annotation database, we can use command `vtools show annotation` to print the details of it. 



    % vtools use refGene
    % vtools show annotation refGene
    

The following command output the corresponding records in refGene database for this variant: 



    % vtools output myVar chr pos ref alt refGene.name txStart txEnd cdsStart cdsEnd exonCount name2
    

    5       179248034       C       T       NM_001142298    179233388       179265077       179250005       179263593       9       SQSTM1
    5       179248034       C       T       NM_001142299    179234003       179265077       179250005       179263593       9       SQSTM1
    5       179248034       C       T       NM_003900       179247842       179265077       179247937       179263593       8       SQSTM1
    

If we use the `ccdsGene` database, we would get: 



    % vtools use ccdsGene
    % vtools output myVar chr pos ref alt ccdsGene.name ccdsGene.txStart ccdsGene.txEnd ccdsGene.cdsStart ccdsGene.cdsEnd ccdsGene.exonCount ccdsGene.name2
    

    5       179248034       C       T       CCDS34317.1     179247937       179263593       179247937       179263593       8
    

We had to use full name `ccdsGene.txStart` etc to avoid ambiguity because these fields also exist in the `refGene` database. 

The results show that 



*   This variant locates in consensus CDS gene CCDS34317.1, with common name `SQSTM1`. 

*This gene encodes a multifunctional protein that binds ubiquitin and regulates activation of the nuclear factor kappa-B (NF-kB) signaling pathway. The protein functions as a scaffolding/adaptor protein in concert with TNF receptor-associated factor 6 to mediate activation of NF-kB in response to upstream signals. Alternatively spliced transcript variants encoding either the same or different isoforms have been identified for this gene. Mutations in this gene result in sporadic and familial Paget disease of bone.* 



*   This gene can transcribed two three mRNAs `NM_001142298`, `NM_00142299` and `NM_003900`, which corresponds to CCDS id `CCDS4735.1` (first two), and `CCDS34317.1`. Searching in CCDS gene only displays `CCDS34317.1` because this variant falls out of the coding region of `CCDS4735.1`. 



### 3. Which exon?

Now we know that this variant is within the coding region of `CCDS34317.1`, is it in one of the exon region? We can use the `ccdsGene_exon` database to find this out. 



    % vtools use ccdsGene_exon
    % vtools output MyVar chr pos ref alt ccdsGene_exon.exon_start ccdsGene_exon.exon_end                        
    

    5       179248034       C       T       179247937       179248141
    

So we know this variant stays in an exon starting from `179247937`, according to [here][1], this is the first exon of this gene. 



### 4. Potential of damaging?

Because this variant belongs to one of the CCDS genes, we can find the SIFT score and PolyPhen2 (and other scores) of this variant from the dbNSFP database. 



    % vtools use dbNSFP
    % vtools output MyVar chr pos ref alt SIFT_score polyphen2_score
    

    5       179248034       C       T       0.49    0.893
    

This database also tells you how this mutation changes the aminoacid: 



    % vtools output MyVar chr pos ref alt aaref aaalt refcodon codonpos aapos
    

    5       179248034       C       T       A       V       GCG     2       33
    

So this variant mutates `C` in `GCG` to `T`, and changes aminoacid `A` (`GCG`) to `V` (`GTG`). 

Now, let us get the aminoacid sequence from the [CCDS gene page][1], and send it to the [PolyPhen 2 website][2], we need to fill in 

*   Protein identifier: leave blank or use name NP_003891.1 
*   Protein sequence: copy and paste with leading line `>NP_003891.1` or leave blank 
*   Position: 33 
*   From A -> V 

Note that we can use either protein name or sequence, but not both. 

The results show that 



    RecName: Full=Sequestosome-1; AltName: Full=EBI3-associated protein of 60 kDa; Short=EBIAP; Short=p60; AltName: Full=Phosphotyrosine-independent ligand for the Lck SH2 domain of 62 kDa; AltName: Full=Ubiquitin-binding protein p62; LENGTH: 440 AA
    
    HumDiv: (preferred model of evaluating rare alleles, dense mapping and analysis of natural selection)
    This mutation is predicted to be POSSIBLY DAMAGING with a score of 0.915 (sensitivity: 0.81; specificity: 0.94)
    
    HumVar: (preferred model for diagnostics of Mendelian disease)
    This mutation is predicted to be BENIGN with a score of 0.399 (sensitivity: 0.84; specificity: 0.78)
    
    


{{% notice tip %}}
The PolyPhen2 score obtained from PolyPhen2 website differs from what is reported by dbNSFP, which used a previous version of PolyPhen2 to generate scores for these variants.
{{% /notice %}}

 [1]: http://www.ncbi.nlm.nih.gov/CCDS/CcdsBrowse.cgi?REQUEST=CCDS&ORGANISM=0&BUILDS=CURRENTBUILDS&DATA=CCDS34317.1
 [2]: http://genetics.bwh.harvard.edu/pph2/
