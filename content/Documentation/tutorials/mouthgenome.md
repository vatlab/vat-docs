+++
title = "Non-human genomes"
weight = 12
hidden = true
+++


## Working with mouse and other non-human reference genomes 

Variant Tools supports build `hg18` and `hg19` of the human reference genome natively. If your data uses a different reference genome, you will need to provide your own fasta files, which can usually be downloaded from resources such as [Illumina iGenomes][1]. The reference genome needs to be converted to a binary format (crr) before it can be used, and need to be stored under the project directory, or under `$local_resource/reference` (usually `~/.variant_tools/reference`). This tutorial shows you how to use the mm10 mouse genome for variant tools. 



### 1. Getting the reference genome and create a `.crr` file.

The first step is to build a `.crr` file from fasta files of the reference genome using command `vtools admin --fasta2crr`. This command accepts either local fasta files or URLs to one or more fasta files. For example, you can use the following command to create a `.crr` file for build `mm10` of the mouse reference genome. 



    % vtools admin --fasta2crr \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr1.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr2.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr3.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr4.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr5.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr6.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr7.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr8.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr9.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr10.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr11.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr12.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr13.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr14.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr15.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr16.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr17.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr18.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chr19.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chrX.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chrY.fa.gz \
    	 ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/chromosomes/chrM.fa.gz \
    	 mm10.crr
    

After you have successfully created this file, you can put it in the project directory, or under `$local_resource/reference` so that it can be shared by multiple projects. After this step is done, you can specify the reference genome to parameter `--build` of commands such as `vtools init` and `vtools import`. 



### 2. Annotation databases

Annotation databases for non-human reference genomes are currently scarce so you will most likely need to build your own annotation databases. Fortunately, most of the time you only need to modify the corresponding annotation database of the human genome. For example, you can create a ref seq annotation database by changing the header of `refGene-hg19_xxx.ann` from 



    [linked fields]
    hg19=chr, txStart, txEnd
    
    [data sources]
    anno_type=range
    description=Known human protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq).
    version=hg19_20130904
    source_url=ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz
    direct_url=annoDB/refGene-hg19_20130904.DB.gz   f3ae8c8baf11b1e32344ee3c7b64edb6
    source_type=txt
    

to 



    [linked fields]
    mm10=chr, txStart, txEnd
    
    [data sources]
    anno_type=range
    description=Known mouse protein-coding and non-protein-coding genes taken from the NCBI RNA reference sequences collection (RefSeq).
    version=mm10_20141201
    source_url=ftp://hgdownload.cse.ucsc.edu/goldenPath/mm10/database/refGene.txt.gz
    direct_url=annoDB/refGene-mm10_20141201.DB.gz
    source_type=txt
    

Note that the ref seq annotation database for mm10 `refGene-mm10_20141201` is already available from the variant tools repository.

 [1]: http://support.illumina.com/sequencing/sequencing_software/igenome.html
