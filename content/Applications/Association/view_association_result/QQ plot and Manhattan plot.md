
+++
title = "QQ plot and Manhattan plot"
description = ""
weight = 1
+++



## Graphic Summary of Association Analysis 



### Introduction

`vtools_report plot_association` generates QQ plot and Manhattan plot of p-values from output of `vtools associate` command. The graphics are powered by the `R` package `ggplot2`. Fonts, color, page layout etc can be specified from the command interface, generating high quality and customized graphs. 



#### Input data format

`vtools associate` command typically generates two types of output: output of gene based association tests and single variant analysis. 



#### Gene-based test input

    #refGene_name2	sample_size_SBurdenTest	statistic_SBurdenTest	pvalue_SBurdenTest
    AAGAB	1246	14	0.709392
    ABHD2	1246	1	0.423756
    ACAN	1246	107	0.0235792
    ACSBG1	1246	23	0.887873
    ACTC1	1246	0	1
    ADAL	1246	2	1
    ADAMTS17	1246	19	0.875558
    ADAM10	1246	0	0.0766778
    AGBL1	1246	120	0.119562
    ...
    



#### Single variant test input

    #chr    pos     sample_size_SNV beta_x_SNV      pvalue_SNV
    1       802398  120     0.164128        0.205794
    1       861292  316     -0.0339594      0.556444
    1       865580  252     0.448666        0.271728
    1       866422  316     -0.106212       0.734266
    1       865584  268     0.0681559       0.267732
    1       865625  303     -0.54794        0.837163
    1       866517  311     0.154219        0.17982
    1       865662  303     -0.571153       0.881119
    1       871129  315     0.0691795       0.476523
    

Note that 



*   The program will read the header and only handle the columns prefixed by `pvalue_` and suffixed by some non-empty character string which will be used as legend names 
*   Multiple columns of p-values are allowed (see examples below) 



### Sample output graphs

#### QQ Plot samples

Attach:qqplots.zip 



#### Manhattan Plot samples

Attach:manhattanplots.zip 



## Details

### Command interface

    % vtools_report plot_association -h
    



    usage: vtools_report plot_association [-h] [-v {0,1,2}]
                                          {qq,manhattan,manhattan_plain} ...
    
    positional arguments:
      {qq,manhattan,manhattan_plain}
        qq                  QQ plot via ggplot2
        manhattan           Manhattan plot via ggplot2
        manhattan_plain     Manhattan plot implementation not using ggplot2
    
    optional arguments:
      -h, --help            show this help message and exit
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.
    



    % vtools_report plot_association qq -h
    



    usage: vtools_report plot_association qq [-h] [--shape INTEGER]
                                             [--fixed_shape] [--no_slope]
                                             [-t TITLE]
                                             [--color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}]
                                             [--width_height INCHES INCHES] [-s]
                                             [-o FILE] [-b]
                                             [-l POSITION [POSITION ...]]
                                             [--label_top INTEGER]
                                             [--label_these NAME [NAME ...]]
                                             [-f SIZE]
    
    optional arguments:
      -h, --help            show this help message and exit
      --shape INTEGER       Choose a shape theme (integer 1 to 16) for dots on QQ
                            plot. Default set to 1.
      --fixed_shape         Use the same dot-shape theme for all plots
      --no_slope            Do not plot the diagonal line
    
    graph properties:
      -t TITLE, --title TITLE
                            Title of plot.
      --color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}
                            Choose a color theme from the list above to apply to
                            the plot. (via the 'RColorBrewer' package:
                            cran.r-project.org/web/packages/RColorBrewer)
      --width_height INCHES INCHES
                            The width and height of the graphics region in inches
      -s, --same_page       Plot multiple groups of p-values on the same graph
      -o FILE, --output FILE
                            Specify output graph filename. Output is in pdf
                            format. It can be converted to jpg format via the
                            'convert' command in Linux (e.g., convert -density 180
                            p.pdf p.jpg)
    
    variants/genes highlighting:
      -b, --bonferroni      Plot the horizontal line at 0.05/N on Y-axis
                            (significance level after Bonferroni correction)
      -l POSITION [POSITION ...], --hlines POSITION [POSITION ...]
                            Additional horizontal line(s) to be drawn on the
                            Y-axis.
      --label_top INTEGER   Specify how many top hits (smallest p-values by rank)
                            you want to highlight with their identifiers in text.
      --label_these NAME [NAME ...]
                            Specify the names of variants (chr:pos, e.g., 1:87463)
                            or genes (genename, e.g., IKBKB) you want to highlight
                            with their identifiers in text.
      -f SIZE, --font_size SIZE
                            Font size of text labels. Default set to '2.5'.
    



    % vtools_report plot_association manhattan -h
    



    usage: vtools_report plot_association manhattan [-h]
                                                    [--chrom CHROMOSOME [CHROMOSOME ...]]
                                                    [--chrom_prefix PREFIX]
                                                    [--gene_map FILE] [-t TITLE]
                                                    [--color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}]
                                                    [--width_height INCHES INCHES]
                                                    [-s] [-o FILE] [-b]
                                                    [-l POSITION [POSITION ...]]
                                                    [--label_top INTEGER]
                                                    [--label_these NAME [NAME ...]]
                                                    [-f SIZE]
    
    optional arguments:
      -h, --help            show this help message and exit
      --chrom CHROMOSOME [CHROMOSOME ...]
                            Specify the particular chromosome(s) to display. Can
                            be one or multiple in this list: "1 2 3 4 5 6 7 8 9 10
                            11 12 13 14 15 16 17 18 19 20 21 22 X Y Un ?:?".
                            Slicing syntax "?:?" is supported. For example "1:22"
                            is equivalent to displaying all autosomes; "1:Y" is
                            equivalent to displaying all mapped chromosomes.
                            Default set to all including unmapped chromosomes.
      --chrom_prefix PREFIX
                            Prefix chromosome ID with a string. Default is set to
                            "chr" (X-axis will be displayed as "chr1", "chr2",
                            etc). Use "None" for no prefix.
      --gene_map FILE       If the plot units are genes and the program fails to
                            map certain genes to chromosomes, you can fix it by
                            providing a text file of genomic coordinate
                            information of these genes. Each gene in the file is a
                            line of 3 columns specifying "GENENAME CHROM
                            MIDPOINT_POSITION", e.g., "IKBKB 8 42128820".
    
    graph properties:
      -t TITLE, --title TITLE
                            Title of plot.
      --color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}
                            Choose a color theme from the list above to apply to
                            the plot. (via the 'RColorBrewer' package:
                            cran.r-project.org/web/packages/RColorBrewer)
      --width_height INCHES INCHES
                            The width and height of the graphics region in inches
      -s, --same_page       Plot multiple groups of p-values on the same graph
      -o FILE, --output FILE
                            Specify output graph filename. Output is in pdf
                            format. It can be converted to jpg format via the
                            'convert' command in Linux (e.g., convert -density 180
                            p.pdf p.jpg)
    
    variants/genes highlighting:
      -b, --bonferroni      Plot the horizontal line at 0.05/N on Y-axis
                            (significance level after Bonferroni correction)
      -l POSITION [POSITION ...], --hlines POSITION [POSITION ...]
                            Additional horizontal line(s) to be drawn on the
                            Y-axis.
      --label_top INTEGER   Specify how many top hits (smallest p-values by rank)
                            you want to highlight with their identifiers in text.
      --label_these NAME [NAME ...]
                            Specify the names of variants (chr:pos, e.g., 1:87463)
                            or genes (genename, e.g., IKBKB) you want to highlight
                            with their identifiers in text.
      -f SIZE, --font_size SIZE
                            Font size of text labels. Default set to '2.5'.
    



    % vtools_report plot_association manhattan_plain -h
    



    usage: vtools_report plot_association manhattan_plain [-h]
                                                          [--chrom CHROMOSOME [CHROMOSOME ...]]
                                                          [--chrom_prefix PREFIX]
                                                          [--gene_map FILE]
                                                          [-t TITLE]
                                                          [--color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}]
                                                          [--width_height INCHES INCHES]
                                                          [-s] [-o FILE] [-b]
                                                          [-l POSITION [POSITION ...]]
                                                          [--label_top INTEGER]
                                                          [--label_these NAME [NAME ...]]
                                                          [-f SIZE]
    
    optional arguments:
      -h, --help            show this help message and exit
      --chrom CHROMOSOME [CHROMOSOME ...]
                            Specify the particular chromosome(s) to display. Can
                            be one or multiple in this list: "1 2 3 4 5 6 7 8 9 10
                            11 12 13 14 15 16 17 18 19 20 21 22 X Y Un ?:?".
                            Slicing syntax "?:?" is supported. For example "1:22"
                            is equivalent to displaying all autosomes; "1:Y" is
                            equivalent to displaying all mapped chromosomes.
                            Default set to all including unmapped chromosomes.
      --chrom_prefix PREFIX
                            Prefix chromosome ID with a string. Default is set to
                            "chr" (X-axis will be displayed as "chr1", "chr2",
                            etc). Use "None" for no prefix.
      --gene_map FILE       If the plot units are genes and the program fails to
                            map certain genes to chromosomes, you can fix it by
                            providing a text file of genomic coordinate
                            information of these genes. Each gene in the file is a
                            line of 3 columns specifying "GENENAME CHROM
                            MIDPOINT_POSITION", e.g., "IKBKB 8 42128820".
    
    graph properties:
      -t TITLE, --title TITLE
                            Title of plot.
      --color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}
                            Choose a color theme from the list above to apply to
                            the plot. (via the 'RColorBrewer' package:
                            cran.r-project.org/web/packages/RColorBrewer)
      --width_height INCHES INCHES
                            The width and height of the graphics region in inches
      -s, --same_page       Plot multiple groups of p-values on the same graph
      -o FILE, --output FILE
                            Specify output graph filename. Output is in pdf
                            format. It can be converted to jpg format via the
                            'convert' command in Linux (e.g., convert -density 180
                            p.pdf p.jpg)
    
    variants/genes highlighting:
      -b, --bonferroni      Plot the horizontal line at 0.05/N on Y-axis
                            (significance level after Bonferroni correction)
      -l POSITION [POSITION ...], --hlines POSITION [POSITION ...]
                            Additional horizontal line(s) to be drawn on the
                            Y-axis.
      --label_top INTEGER   Specify how many top hits (smallest p-values by rank)
                            you want to highlight with their identifiers in text.
      --label_these NAME [NAME ...]
                            Specify the names of variants (chr:pos, e.g., 1:87463)
                            or genes (genename, e.g., IKBKB) you want to highlight
                            with their identifiers in text.
      -f SIZE, --font_size SIZE
                            Font size of text labels. Default set to '2.5'.
    



### QQ Plot Examples

#### Gene base tests

    zcat genetest.result.gz | vtools_report plot_association qq -o genes_qq1
    zcat genetest.result.gz | vtools_report plot_association qq -s --color Dark2 -b -o genes_qq\
    2
    zcat genetest.result.gz | vtools_report plot_association qq -t "Demo QQ plot" -b -o genes_q\
    q3
    zcat genetest.result.gz | vtools_report plot_association qq -t "Demo otherwise shaped QQ pl\
    ot" -s -b --shape 12 -o genes_qq4
    



#### Single variant tests

    zcat varianttest.result.gz | vtools_report plot_association qq -o variants_qq1
    zcat varianttest.result.gz | vtools_report plot_association qq -s --color Dark2 -b -o varia\
    nts_qq2
    zcat varianttest.result.gz | vtools_report plot_association qq -t "Demo QQ plot" -b -o vari\
    ants_qq3
    zcat varianttest.result.gz | vtools_report plot_association qq -t "Demo otherwise shaped QQ\
     plot" -s -b --shape 12 -o variants_qq4
    



### Manhattan Plot Examples

#### Gene base tests

    zcat genetest.result.gz | vtools_report plot_association manhattan -t "Demo Manhattan plot"\
     --color Dark2 --s -b -o genes_man1
    zcat genetest.result.gz | vtools_report plot_association manhattan -t "Demo Manhattan plot"\
     --chrom 1:22 --chrom_prefix None --same_page -o genes_man2
    zcat genetest.result.gz | vtools_report plot_association manhattan_plain -t "Demo Manhattan\
     plain plot" --color Dark2 --s -b -o genes_man3
    zcat genetest.result.gz | vtools_report plot_association manhattan_plain -t "Demo Manhattan\
     plain plot" --chrom 1:22 --chrom_prefix None --same_page -o genes_man4
    



#### Single variant tests

    zcat varianttest.result.gz | vtools_report plot_association manhattan -t "Demo Manhattan pl\
    ot" --color Dark2 --s -b -o variants_man1
    zcat varianttest.result.gz | vtools_report plot_association manhattan -t "Demo Manhattan pl\
    ot" --chrom 1:22 --chrom_prefix None --same_page -o variants_man2
    zcat varianttest.result.gz | vtools_report plot_association manhattan_plain -t "Demo Manhat\
    tan plain plot" --color Dark2 --s -b -o variants_man3
    zcat varianttest.result.gz | vtools_report plot_association manhattan_plain -t "Demo Manhat\
    tan plain plot" --chrom 1:22 --chrom_prefix None --same_page -o variants_man4