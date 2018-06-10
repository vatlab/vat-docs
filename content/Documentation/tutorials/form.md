+++
title = "Format"
weight = 10
hidden = true
+++


## Import a list of variants in an unsupported format 

### 1. Data

Your collaborator send you a list of variants of interest and you would like to annotate these variants with properties like SIFT and PolyPhen2 scores. However, the list of variants were dumped from an excel file and were saved in a format that cannot be directly imported by variant tools. 



    head -20 myVars.csv
    

    ADARB2,chr10,1224091,-/C
    ADARB2,chr10,1224097,-/A
    ADARB2,chr10,1225078,-/TACTC
    ADARB2,chr10,1226607,-/CCCTCTG
    ADARB2,chr10,1227210,-/T
    ADARB2,chr10,1231436,-/AAAAC
    ADARB2,chr10,1234557,-/T
    ADARB2,chr10,1240467,-/ATCT
    ADARB2,chr10,1245155,-/CC
    ADARB2,chr10,1245562,CAGGTGGG/-
    ADARB2,chr10,1248053,-/T
    ADARB2,chr10,1251205,TTTTAGGGCCACC/-
    ADARB2,chr10,1255256,CCCACCATGCCATCA/-
    ADARB2,chr10,1255475,TCGCCCACACCCATGCCA/-
    ADARB2,chr10,1257255,-/ATCT
    ADARB2,chr10,1259938,-/CTG
    ADARB2,chr10,1260318,CCTGGACCT/-
    ADARB2,chr10,1262873,G/-
    ADARB2,chr10,1265793,TGATGA/-
    ADARB2,chr10,1267343,T/-
    



### 2. Use shell commands to process data

The standard format that variant tools support is a text file that is 



*   tab delimited 
*   has columns chromosome, position, reference allele and alternative allele 
*   no "chr" before chromosome name 
*   use `-` for missing allele for insertions 

A recent version of `csv` format can handle the first and third problem but still cannot get reference and alternative alleles from the last column. 

Our data does not follow this format in that 

*   is comma delimited 
*   first column is gene name 
*   chromosome names are prefixed with `chr` 
*   reference and alternative alleles are in one column separated by `/` 

If you are familiar with shell commands, you can convert the files using the following commands 



    # remove first column
    cut -d, -f2,3,4 myVars.csv > f1
    # change , to tab (use Ctrl-V, tab to enter tab)
    sed 's/,/    /g' f1 > f2
    # remove leading chr
    sed 's/chr//' f2 > f3
    # split ref and alt alleles
    sed 's/\//    /g' f3 > output.lst
    

or connect the commands using Unix pipes: 



    cut -d, -f2,3,4 myVars.csv | sed 's/,/    /g' | \
        sed 's/chr//' | sed 's/\//    /g' > output.lst
    

The resulting file could then be imported to variant tools using command 



    vtools import output.lst --format basic
    



### 3. Use customized `.fmt` file

With some effort, these text-processing tools could be used to manipulate input files so that they could be imported by variant tools. However, when there are a large number of such files (in the same format), it might be easier to describe this format so that variant tools can import the files directly. To do this, let us get hold of the format description file of the basic format: 



    vtools show format basic
    cp cache/basic.fmt myformat.fmt
    

The first command downloads (and shows) the basic format from the variant tools website (`vtools.houstonbioinformatics.org`). It is saved in a `cache` directory so you can copy it to your project directory and rename it. 

The file looks like this: 



    cat cache/basic.fmt
    

    # Copyright (C) 2011 Bo Peng (bpeng@mdanderson.org)
    # Distributed under GPL. see <http://www.gnu.org/licenses/>
    #
    # Please refer to http://varianttools.sourceforge.net/Format/New for
    # a description of the format of this file.
    
    [format description]
    description=A basic variant input format with four columns: chr, pos, ref, alt.
    variant=chr,pos,ref,alt
    
    [chr]
    index=1
    type=VARCHAR(20)
    adj=RemoveLeading('chr')
    comment=Chromosome
    
    [pos]
    index=2
    type=INTEGER NOT NULL
    comment=1-based position
    
    [ref]
    index=3
    type=VARCHAR(255)
    comment=Reference allele, '-' for insertion.
    
    [alt]
    index=4
    type=VARCHAR(255)
    comment=Alternative allele, '-' for deletion.
    
    

You can find detailed description of this file [here][1], but it is not too difficult to learn that 



1.  `variant=chr,pos,ref,alt` defines four fields for chromosome, position, reference and alternative alleles. 

2.  For each field, `index` specifies the index of the column, `type` specifies the type of field, `comment` gives a description of the field, and most importantly `adj` adjust the input to something variant tools can recognize. For example, `RemoveLeading('chr')` for the `chr` field remove leading `chr` from input if it exists. 

To adapt this format file to handle our format, we need to 



1.  Add `delimiter=","` in the `format description` section to indicate that our files are comma delimited. 

2.  change the indexes of the four fields to `2`, `3`, `4`, `4` because we will get the fields from these columns. 

These changes will correctly import fields `chr` and `pos`, but not `ref` and `alt`, because they will both get values such as `A/G` from the fourth column. To separate `A` and `G` from such inputs, you will need to use a `adj` function. If you look through functions listed in [here][2], you can find a function `ExtractField` that does exactly this. More specifically, `ExtractField(1, sep="/")` will split the input by separator `/`, and return the first item, and `ExtractField(2, sep="/")` will split the input and return the second item. So, to input `ref` and `alt` correctly, you can add lines 



*   `ExtractField(1, sep="/")` to field `ref`, and 
*   `ExtractField(2, sep="/")` to field `alt`. 

The format file now looks like this: 



    cat myformat.fmt
    

    # Copyright (C) 2011 Bo Peng (bpeng@mdanderson.org)
    # Distributed under GPL. see <http://www.gnu.org/licenses/>
    #
    # Please refer to http://varianttools.sourceforge.net/Format/New for
    # a description of the format of this file.
    
    [format description]
    description=A basic variant input format with four columns: chr, pos, ref, alt.
    variant=chr,pos,ref,alt
    delimiter=","
    
    [chr]
    index=2
    type=VARCHAR(20)
    adj=RemoveLeading('chr')
    comment=Chromosome
    
    [pos]
    index=3
    type=INTEGER NOT NULL
    comment=1-based position
    
    [ref]
    index=4
    type=VARCHAR(255)
    adj=ExtractField(1, sep='/')
    comment=Reference allele, '-' for insertion.
    
    [alt]
    index=4
    type=VARCHAR(255)
    adj=ExtractField(2, sep='/')
    comment=Alternative allele, '-' for deletion.
    

With this file, you can use 



    vtools import myVars.lst --format myformat.fmt --build hg18
    

to import the data. 



### 4. Import gene name as well

The input file has a column with gene names. We do not have to import this column because gene name could be retrieved and outputted using command 



    vtools use refGene
    vtools output variant chr pos ref alt refGene.name2
    

However, because one variant can belong to several genes, importing this column can help us focus on the gene we are interested in. To import this column, we need to 



1.  define a field `genename` with proper type 
2.  add this field to `variant_info` so that it will be imported automatically as a variant info field 

The modified format file should look like (with modified descriptions): 



    cat myformat.fmt
    

    [format description]
    description=A format file that import genename, chr, pos, ref and alt from a comma
        delimited file
    variant=chr,pos,ref,alt
    variant_info=genename
    delimiter=","
    
    [genename]
    index=1
    type=VARCHAR(255)
    comment=Gene name
    
    [chr]
    index=2
    type=VARCHAR(20)
    adj=RemoveLeading('chr')
    comment=Chromosome
    
    [pos]
    index=3
    type=INTEGER NOT NULL
    comment=1-based position
    
    [ref]
    index=4
    type=VARCHAR(255)
    adj=ExtractField(1, sep='/')
    comment=Reference allele, '-' for insertion.
    
    [alt]
    index=4
    type=VARCHAR(255)
    adj=ExtractField(2, sep='/')
    comment=Alternative allele, '-' for deletion.
    

The command to import data is the same 



    vtools import myVars.lst --format myformat.fmt --build hg18

 [1]:    /documentation/customization/format/formats/new/
 [2]:    /documentation/customization/format/formats/functor/
