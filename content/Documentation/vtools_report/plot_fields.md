
+++
title = "plot_fields"
description = ""
weight = 10
+++





# Plot fields from variant tables



## Usage

    % vtools_report plot_fields -h
    

    usage: vtools_report plot_fields [-h] [--variants TABLE]
                                     [--save_data FILENAME]
                                     [--save_script FILENAME] [--width px]
                                     [--height px] [--hist name] [--norm_curve]
                                     [--dot name] [--dot_size pt]
                                     [--discrete_color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}]
                                     [--box name] [--stratify C [C ...]]
                                     [--outlier_size pt]
                                     [--color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}]
                                     [-v {0,1,2}]
                                     fields [fields ...]
    
    positional arguments:
      fields                A list of fields that will be outputted.
    
    optional arguments:
      -h, --help            show this help message and exit
      --variants TABLE      Limit value of fields to variant in specified variant
                            table. Default to all variants.
      --save_data FILENAME  Save data to file.
      --save_script FILENAME
                            Save R script to file.
      --width px            Width of plot. Default to 800.
      --height px           Height of plot. Default to 600.
      -v {0,1,2}, --verbosity {0,1,2}
                            Output error and warning (0), info (1) and debug (2)
                            information of vtools and vtools_report. Debug
                            information are always recorded in project and
                            vtools_report log files.
    
    Draw histogram:
      --hist name           File name of the outputted figure, which can have type
                            PDF, EPS, or JPG. Multiple files might be produced if
                            more than one figure is produced (e.g.
                            MyFig_$FIELD1.pdf, MyFig_$FILED2.pdf if MyFig.pdf is
                            specified)
      --norm_curve          Add a normal distribution N(mean, stdev) density curve
                            to the histogram.
    
    Draw dot plot. Allow up to 3 input fields: for single input
        field, the values will be plotted on y-axis with index being x-axis; for two input fields, the first
        field will be plotted on x-axis and the second field on y-axis; for three input fields, values of
        the third input field is represented by color of the dots.:
      --dot name            File name of the outputted figure, which can have type
                            PDF, EPS, or JPG.
      --dot_size pt         Size of dots. Default is 2.0
      --discrete_color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}
                            If specified, the third field of input will be treated
                            as "factor" data.
    
    Draw box plot. Allow one or more input fields and produce
        box plot for all fields in one graph. With --stratify option, box plot will be generated for field
        in different strata, if there is only one input field, or for the first field in different strata of
        the second field, if there are two input fields.:
      --box name            File name of the outputted figure, which can have type
                            PDF, EPS, or JPG.
      --stratify C [C ...]  Cutoff values to stratify data in the input field for
                            box plot. When this option is on, only one input field
                            is allowed.
      --outlier_size pt     Size of outlier dots. Default is 2.0
      --color {Dark2,grayscale,default,BrBG,PiYG,PRGn,PuOr,RdBu,RdGy,RdYlBu,RdYlGn,Spectral,Accent,Paired,Pastel1,Pastel2,Set1,Set2,Set3,Blues,BuGn,BuPu,GnBu,Greens,Greys,Oranges,OrRd,PuBu,PuBuGn,PuRd,Purples,RdPu,Reds,YlGn,YlGnBu,YlOrBr,YlOrRd}
                            Color theme for boxes.
    



## Example

Histograms, dot plots and box plots can be generated for variant info fields. The command interface is similar to `vtools_report plot_pheno_fields`.