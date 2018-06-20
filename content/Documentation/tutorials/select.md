+++
title = "Select"
weight = 6
hidden = true
+++

## Selecting variants belong to specified genes 

### 1. Data

We have whole genome sequencing data for more than 18M variants. After some initial analysis, three genes `geneA`, `geneB`, and `geneC` caught our eyes and we would like to further investigate these genes. We assume that we already have a project with all the variants imported 



### 2. Find variants that belong to the genes

We first need to get a list of genes 



    % vtools use refGene
    

From the output 



    % vtools show annotation refGene
    

we can see that it has locations of each gene, gene ID (`NM_XXX`) and a more common name `name2`. To select variants that belong to these genes, we can do 



    % vtools select variant 'refGene.name2 in ("geneA", "geneB", "geneC")' -t gene_ABC
    

Or, if you prefer separating the tables, you can use commands 



    % for gene in geneA geneB geneC
    % do
        vtools select variant "refGene.name2='$gene'" -t \\(gene
    % done
    

to create three tables. To create another table with variants in these three tables, you could do 



    % vtools compare geneA geneB --A_or_B gene_AB
    % vtools compare gene_AB geneC --A_or_B gene_ABC
    % vtools remove tables gene_AB
    

The last command remove the intermediate table `gene_AB`. 



### 3. Find variants that belong to a long list of genes

To subset a dataset to variants within a group of hundreds of genes, you need to create a small annotation database to link the gene list to the project, via, e.g., the refGene database. Suppose your list of genes are formatted like: 



    % NEBL	NM_213569
    % NEBL	NM_213569
    % NEBL	NM_213569
    % NEBL	NM_213569
    % LINC00167	NR_024233
    % PGAP2	NR_027016
    % PGAP2	NR_027016
    ...
    

where the columns are gene name and (or) transcript name. You can create an annotation file for the gene list, e.g., 



    [linked fields]
    *=gene_name
    
    [data sources]
    description=My gene selection for xxx project
    version=20130419
    anno_type=field
    source_type=txt
    
    [gene_name]
    index=1
    type=VARCHAR(255)
    comment=Gene name
    
    [transcript_name]
    index=2
    type=VARCHAR(255)
    comment=Transcript name
    

and the annotation database 



    % vtools use MyGenes.ann -f my_gene_list.txt --linked_by refGene.name2 
    

Note that the default linked field is "gene_name", the gene names. Alternatively you can choose to link by transcript name, e.g. 



    % vtools use MyGenes.ann -f my_gene_list.txt --linked_by refGene.name --linked_fields transcript_name
    

Finally select the variants belonging to this list of gene 



    % vtools select some_table "MyGenes.gene_name is not NULL" -t my_genes
    



### 4. Find variants that belong to exonic regions of the genes

Annotation database `refGene_exon` lists all exonic regions of each gene. To use this annotation database, you can download and use the latest version of this database using command 



    % vtools use refGene_exon
    

Then select variants that belong to the exonic regions of the genes using command 



    % vtools select variant 'refGene_exon.name2 in ("geneA", "geneB", "geneC")' -t gene_ABC
    

Or separately for each gene: 



    % for gene in geneA geneB geneC
    % do
        vtools select variant "refGene_exon.name2='$gene'" -t \\({gene}_exon
    % done
    



#### 4.1 Finding variants around a gene (e.g. promotor regions)

If you would like to find all variants that are in vicinity of genes (e.g. 2k basepair in the upstream and downstream of the gene), you will have to know the position of the genes. You could get such information from UCSC database, or from the refGene database using commands such as 



    % vtools execute 'SELECT chr, txStart, txEnd FROM refGene.refGene WHERE refGene.name2="geneA"'
    


{{% notice tip %}}
This query is database dependent. You could use command `sqlite3 annotation.DB .schame` to get the structure of database if you would like to know the structure of another annotation database and submit a similar query. 
{{% /notice %}}


After you get the starting and ending locations of the genes, you could select a variants using commands such as 



    % vtools select variant 'chr="5"' 'pos>=7152445' 'pos<=7158882' -t geneA_ext
