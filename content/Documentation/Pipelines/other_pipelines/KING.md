
+++
title = "KING"
weight = 7
+++





## Global ancestry and kinship inference



### 1. Usage

    % vtools show pipeline KING 

    Pipeline to call KING to perform global ancestry and kinship inference, and import ancestry analysis results as
    phenotypes into sample table.
    
    Available pipelines: king
    
    Pipeline "king":  This pipeline exports genotypes in specified variant table (parameter --var_table, default to
    variant) for specified samples (parameter --samples, default to all samples), executes PLINK's LD pruning, (R^2<0.5)
    and analysis selected variants using KING's population ancestry and kingship analysis. Specified number of MDS
    components for global ancestry analysis will be imported to sample table (parameter --num_comp, default to 5). A
    report of relatedness between pairs of samples will be written to file <jobname>.relatedness.txt (parameter --jobname,
    default to "KING"). No input or output file is required for this pipeline, but a snapshot could be specified, in which
    case the snapshot will be loaded (and overwrite the present project).
      king_0:             Load specified snapshot if a snapshot is specified. Otherwise use the existing project.
      king_10:            Check the existence of KING and PLINK command.
      king_20:            Write selected variant and samples in tped format
      king_21:            Rename tfam file to match tped file
      king_30:            Calculate LD pruning candidate list with a cutoff of R^2=0.5
      king_31:            LD pruning from pre-calculated list
      king_41:            Global ancestry inference
      king_42:            Kinship inference
      king_51:            Extract MDS result for vtools phenotype import
      king_52:            Import phenotype from global ancestry analysis
      king_61:            Save global ancestry inference result to plot
      king_62:            Save kinship analysis result to text file
    
    Pipeline parameters:
      var_table           Variant table for the variants to be analyzed. (default: variant)
      samples             Samples to be analyzed. (default: 1)
      reported_ancestry   Field name for self-reported ancestry. This is the name of the column of population group
                          information in "vtools show samples" command. If specified, the global ancestry inference will
                          be reported on a graph with colored dots indicating sample's self-reported ancestry group.
      king_path           Path to a directory that contains the "king" program, if it is not in the default \\(PATH.
      plink_path          Path to a directory that contains the "plink" program, if it is not in the default \\(PATH.
      num_comp            number of MDS components in global ancestry analysis that will be imported to sample table.
                          (default: 5)
      maf                 Minor Allele Frequency cutoff. Variants having MAF smaller than this value will be dropped from
                          analysis. (default: 0.01)
      jobname             A jobname, an identifier that will be part of filenames and field names generated during the
                          execution of this pipeline. Please ONLY use combination of letters and underscore ("_") for job
                          name. (default: KING)
    
    



### 2. Details

This pipeline integrates global ancestry analysis (MDS method) and kinship analysis. It updates sample phenotypes with calculated MDS components and generate graphic report for ancestry analysis, and text report for kinship analysis. project with the outputs. To use this pipeline, you should first download and install [KING][1] and [PLINK][2] to your \\(PATH or somewhere, then execute a command similar to 



    % vtools execute KING --jobname kin --var_table kin --reported_ancestry Population
    

After the execution of the pipeline, MDS analysis results are updated to phenotype fields 



    % vtools phenotype --output sample_name Population kin_mds1 kin_mds2 -l 10  

    HG00096	GBR	-0.0372	0.0185
    HG00097	GBR	-0.0369	-0.0768
    HG00099	GBR	-0.0338	-0.0608
    HG00100	GBR	-0.0361	0.0284
    HG00101	GBR	-0.0336	0.0254
    HG00102	GBR	-0.0332	0.02
    HG00103	GBR	-0.0334	0.0241
    HG00104	GBR	-0.0337	-0.0572
    HG00106	GBR	-0.0347	-0.0794
    HG00108	GBR	-0.035	0.0431
    

and a graph `kin.mds.pdf` is generated for the same information. Additionally a summary of kinship analysis is available to identify related individuals 

    % cat kin.RelatedIndividuals.txt 

    ID1 ID2 HetHet IBS0 Kinship Relationship
    HG00116 HG00120 0.116 0.0358 0.0781 3rd-degree
    HG00119 HG00124 0.131 0.0201 0.1558 2nd-degree
    HG00134 HG00142 0.122 0.0346 0.0849 3rd-degree
    HG00238 HG00240 0.125 0.0372 0.0868 3rd-degree
    NA11931 NA11933 0.119 0.0422 0.0540 3rd-degree
    NA11932 NA12383 0.118 0.0430 0.0530 3rd-degree

 [1]: http://people.virginia.edu/~wc9c/KING/Download.htm
 [2]: http://pngu.mgh.harvard.edu/~purcell/plink/download.shtml