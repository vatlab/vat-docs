
+++
title = "keggPathway"
weight = 2
+++

## Kegg Pathway

### 1. About `keggPathway`

This database provides KEGG pathway IDs and a pathway description for genes with CCDS IDs. If you would like to annotate variants to these KEGG pathways, you first need to annotate your variants with CCDS IDs. Variant tools databases such as **ccdsGene** annotates variants with CCDS IDs (see example below). 



### 2. Fields

*   **ccdsId** CCDS gene ID 
*   **KgID** Kegg pathway ID 
*   **KgDesc** Description of pathway 



### 3. keggPathway

    vtools show annotation keggPathway -v2
    
    Annotation database keggPathway (version 20110823)
    Description: kegg pathway for CCDS genes
    Database type: attribute
    Number of records: 19,584
    Reference genome *: ['ccdsId']
    
    Field:           ccdsId
    Type:            string
    Comment:         CCDS gene ID
    Missing entries: 0
    Unique entries:  6,949
    
    Field:           KgID
    Type:            string
    Comment:         Kegg pathway ID
    Missing entries: 0
    Unique entries:  209
    
    Field:           KgDesc
    Type:            string
    Comment:         Description of pathway
    Missing entries: 0
    Unique entries:  209
    



### 4. Examples

First we need to use `dbNSFP` in our project to annotate our variants with CCDS IDs: 

    vtools use ccdsGene
    

We then load the keggPathway database linked by `ccdsGene.name` 

    % vtools use keggPathway --linked_by ccdsGene.name
    
    INFO: Opening project RA.proj
    WARNING: Cannot locate annotation database /Users/bpeng/vtools/ccdsKeggPathway
    WARNING: Cannot open annotation database /Users/bpeng/vtools/ccdsKeggPathway
    INFO: Downloading annotation database from https://cge.mdanderson.org/~bpeng1/User/annoDB/keggPathway.DB
    keggPathway.DB: 100.0% [=====================================>] 252 0.3/s in 00:00:00
    INFO: Failed to download database or downloaded database unusable.
    INFO: Downloading keggPathway.txt.gz
    keggPathway.txt.gz: 100.0% [=====================================>] 107,677 103.0K/s in 00:00:01
    INFO: Importing database keggPathway from sourece files ['/var/folders/7O/7OzyfGRoH+i7iQCDzTkba++++TQ/-Tmp-/tmpKqPYoN/keggPathway.txt.gz']
    INFO: Importing annotation data from /var/folders/7O/7OzyfGRoH+i7iQCDzTkba++++TQ/-Tmp-/tmpKqPYoN/keggPathway.txt.gz
    keggPathway.txt.gz: 100.0% [=====================================>] 11,719 26.8K/s in 00:00:00
    INFO: 19584 records handled, 0 ignored.
    INFO: Creating indexes (this can take quite a while)
    INFO: Using annotation DB keggPathway in project RA.
    

At the end of `vtools show fields` output, we can see 

    keggPathway.ccdsId           CCDS gene ID
    keggPathway.KgID             Kegg pathway ID
    keggPathway.KgDesc           Description of pathway
    

Now, we can see which pathways our variants belong to: 

    vtools output NS_SNV chr pos ref alt genename kgID kgDesc  -l 10
    
    INFO: Opening project RA.proj
    INFO: Writing output
    1	878522	T	C	NOC2L	NA	NA
    1	899101	G	C	PLEKHN1	NA	NA
    1	939471	G	A	ISG15	hsa04622	RIG-I-like receptor signaling pathway
    1	1190055	C	G	UBE2J2	hsa04120	Ubiquitin mediated proteolysis
    1	1190055	C	G	UBE2J2	hsa05012	Parkinson's disease
    1	1216741	C	T	SCNN1D	NA	NA
    1	1541790	T	C	MIB2	NA	NA
    1	1656111	G	A	SLC35E2	NA	NA
    1	1675900	G	T	NADK	hsa00760	Nicotinate and nicotinamide metabolism
    1	1675900	G	T	NADK	hsa01100	Metabolic pathways
    

and we can select variants that belong to a pathway, for example, 



    vtools select NS_SNV 'kgID="hsa00760"' --output chr pos ref alt genename kgDesc 
    
    INFO: Opening project RA.proj
    INFO: Writing output
    1	1675900	G	T	NADK	Metabolic pathways
    1	1675900	G	T	NADK	Nicotinate and nicotinamide metabolism
    11	70847195	G	C	NADSYN1	Metabolic pathways
    11	70847195	G	C	NADSYN1	Nicotinate and nicotinamide metabolism
    11	70862326	A	C	NADSYN1	Metabolic pathways
    11	70862326	A	C	NADSYN1	Nicotinate and nicotinamide metabolism
    16	29615851	A	G	QPRT	Metabolic pathways
    16	29615851	A	G	QPRT	Nicotinate and nicotinamide metabolism
    2	18629604	C	T	NT5C1B	Metabolic pathways
    2	18629604	C	T	NT5C1B	Nicotinate and nicotinamide metabolism
    2	18629604	C	T	NT5C1B	Purine metabolism
    2	18629604	C	T	NT5C1B	Pyrimidine metabolism
    2	18629604	C	T	NT5C1B	Metabolic pathways
    2	18629604	C	T	NT5C1B	Nicotinate and nicotinamide metabolism
    2	18629604	C	T	NT5C1B	Purine metabolism
    2	18629604	C	T	NT5C1B	Pyrimidine metabolism
    2	201242634	A	G	AOX1	Drug metabolism - cytochrome P450
    2	201242634	A	G	AOX1	Metabolic pathways
    2	201242634	A	G	AOX1	Nicotinate and nicotinamide metabolism
    2	201242634	A	G	AOX1	Tryptophan metabolism
    2	201242634	A	G	AOX1	Tyrosine metabolism
    2	201242634	A	G	AOX1	Valine, leucine and isoleucine degradation
    2	201242634	A	G	AOX1	Vitamin B6 metabolism
    4	15318290	G	A	BST1	Calcium signaling pathway
    4	15318290	G	A	BST1	Metabolic pathways
    4	15318290	G	A	BST1	Nicotinate and nicotinamide metabolism
    6	86255952	A	G	NT5E	Metabolic pathways
    6	86255952	A	G	NT5E	Nicotinate and nicotinamide metabolism
    6	86255952	A	G	NT5E	Purine metabolism
    6	86255952	A	G	NT5E	Pyrimidine metabolism
    10	104924699	T	C	NT5C2	Metabolic pathways
    10	104924699	T	C	NT5C2	Nicotinate and nicotinamide metabolism
    10	104924699	T	C	NT5C2	Purine metabolism
    10	104924699	T	C	NT5C2	Pyrimidine metabolism
    16	29613945	C	T	QPRT	Metabolic pathways
    16	29613945	C	T	QPRT	Nicotinate and nicotinamide metabolism
    4	15318350	G	A	BST1	Calcium signaling pathway
    4	15318350	G	A	BST1	Metabolic pathways
    4	15318350	G	A	BST1	Nicotinate and nicotinamide metabolism
    6	132103113	G	A	ENPP3	Metabolic pathways
    6	132103113	G	A	ENPP3	Nicotinate and nicotinamide metabolism
    6	132103113	G	A	ENPP3	Pantothenate and CoA biosynthesis
    6	132103113	G	A	ENPP3	Purine metabolism
    6	132103113	G	A	ENPP3	Riboflavin metabolism
    6	132103113	G	A	ENPP3	Starch and sucrose metabolism
    2	201234575	A	G	AOX1	Drug metabolism - cytochrome P450
    2	201234575	A	G	AOX1	Metabolic pathways
    2	201234575	A	G	AOX1	Nicotinate and nicotinamide metabolism
    2	201234575	A	G	AOX1	Tryptophan metabolism
    2	201234575	A	G	AOX1	Tyrosine metabolism
    2	201234575	A	G	AOX1	Valine, leucine and isoleucine degradation
    2	201234575	A	G	AOX1	Vitamin B6 metabolism
    5	102922572	T	C	NUDT12	Nicotinate and nicotinamide metabolism
    5	102922572	T	C	NUDT12	Peroxisome
    14	20010446	G	A	PNP	Metabolic pathways
    14	20010446	G	A	PNP	Nicotinate and nicotinamide metabolism
    14	20010446	G	A	PNP	Purine metabolism
    14	20010446	G	A	PNP	Pyrimidine metabolism
    2	18629637	G	T	NT5C1B	Metabolic pathways
    2	18629637	G	T	NT5C1B	Nicotinate and nicotinamide metabolism
    2	18629637	G	T	NT5C1B	Purine metabolism
    2	18629637	G	T	NT5C1B	Pyrimidine metabolism
    2	18629637	G	T	NT5C1B	Metabolic pathways
    2	18629637	G	T	NT5C1B	Nicotinate and nicotinamide metabolism
    2	18629637	G	T	NT5C1B	Purine metabolism
    2	18629637	G	T	NT5C1B	Pyrimidine metabolism
    11	70869465	C	T	NADSYN1	Metabolic pathways
    11	70869465	C	T	NADSYN1	Nicotinate and nicotinamide metabolism
    5	43691831	C	T	NNT	Metabolic pathways
    5	43691831	C	T	NNT	Nicotinate and nicotinamide metabolism
    1	1675941	G	A	NADK	Metabolic pathways
    1	1675941	G	A	NADK	Nicotinate and nicotinamide metabolism
    6	86255962	T	C	NT5E	Metabolic pathways
    6	86255962	T	C	NT5E	Nicotinate and nicotinamide metabolism
    6	86255962	T	C	NT5E	Purine metabolism
    6	86255962	T	C	NT5E	Pyrimidine metabolism
    4	15389158	C	T	CD38	Calcium signaling pathway
    4	15389158	C	T	CD38	Hematopoietic cell lineage
    4	15389158	C	T	CD38	Metabolic pathways
    4	15389158	C	T	CD38	Nicotinate and nicotinamide metabolism
    11	70870707	G	A	NADSYN1	Metabolic pathways
    11	70870707	G	A	NADSYN1	Nicotinate and nicotinamide metabolism
    5	43736078	A	G	NNT	Metabolic pathways
    5	43736078	A	G	NNT	Nicotinate and nicotinamide metabolism
    11	70886273	G	A	NADSYN1	Metabolic pathways
    11	70886273	G	A	NADSYN1	Nicotinate and nicotinamide metabolism
    17	70638943	G	A	NT5C	Metabolic pathways
    17	70638943	G	A	NT5C	Nicotinate and nicotinamide metabolism
    17	70638943	G	A	NT5C	Purine metabolism
    17	70638943	G	A	NT5C	Pyrimidine metabolism
    9	76873744	T	G	C9orf95	Nicotinate and nicotinamide metabolism
    6	132086873	A	G	ENPP3	Metabolic pathways
    6	132086873	A	G	ENPP3	Nicotinate and nicotinamide metabolism
    6	132086873	A	G	ENPP3	Pantothenate and CoA biosynthesis
    6	132086873	A	G	ENPP3	Purine metabolism
    6	132086873	A	G	ENPP3	Riboflavin metabolism
    6	132086873	A	G	ENPP3	Starch and sucrose metabolism
    



The result of the above example can be confusing because the output displays multiple pathways, not only the one we specified. The reason is that this query is identifying variants in your specified pathway and then it generates a report of these variants with all the pathways that they might be in. Genes often belong to multiple pathways. You can filter the output again, or output only the variant information (chromosome, position) if you would like to get a list of unique variants.