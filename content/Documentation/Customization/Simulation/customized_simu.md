
+++
title = "Customized"
weight = 2
+++

## Define your own simulations 



### 1. Introduction

A simulation specification file is essentially a pipeline specification file defined [here][1]. The `vtools simulate` command executes the pipeline 

*   without `--input` file. It instead creates a simulation config file for each simulation and passes it to the pipeline. 
*   with `seed` as one of the pipeline variables so that it can be used in the pipeline. 
*   with pipeline actions designed for genetic simulations 

Core simulation actions are defined in variant tools module `simulation`. You can see a list of pipeline actions defined in this file by running command 



    % vtools show actions
    

    ... ignored ...
    Module:
            simulation
    Description:
            This module defines functions and actions for Variant Simulation Tools.
    Pipeline actions:
            CreatePopulation
            DrawCaseControlSample
            DrawQuanTraitSample
            DrawRandomSample
            EvolvePopulation
            ExportPopulation
            ExtractVCF
            OutputPopulationStatistics
    
    ... ignored ...
    

You can then learn the details of an action using command 



    % vtools show action CreatePopulation
    

    Help on class CreatePopulation in module variant_tools.simulation:
    
    class CreatePopulation(variant_tools.pipeline.PipelineAction)
     |  Create a simuPOP population from specified regions and
     |  number of individuals.
     |
     |  Methods defined here:
     |
     |  __init__(self, regions, size=None, importGenotypeFrom=None, infoFields=[], build=None, output=[], **kwargs)
     |      Parameters:
     |          regions: (string):
     |              One or more chromosome regions in the format of chr:start-end
     |              (e.g. chr21:33,031,597-33,041,570), Field:Value from a region-based
     |              annotation database (e.g. refGene.name2:TRIM2 or refGene_exon.name:NM_000947),
     |              or set options of several regions (&, |, -, and ^ for intersection,
     |              union, difference, and symmetric difference).
     |
     |          size (None, integer, list of integers):
     |              Size of the population. This parameter can be ignored (``None``) if
     |              parameter ``importGenotypeFrom`` is specified to import genotypes from
     |              external files.
     |
     |          importGenotypeFrom (None or string):
     |              A file from which genotypes are imported. Currently a file with extension
     |              ``.vcf`` or ``.vcf.gz`` (VCF format) or ``.ms`` (MS format) is supported.
     |              Because the ms format does not have explicit location of loci, the loci are
     |              spread over the specified regions according to their relative locations.
     |
     |          infoFields (string or list of strings):
     |              information fields of the population, if needed by particular operators
     |              during evolution.
     |
     |          build (string):
     |              build of the reference genome. Default to hg19.
     |
     |          output (string):
     |              Name of the created population in simuPOP's binary format.
     |
     |          kwargs (arbitrary keyword parameters):
     |              Additional parameters that will be passed to the constructor of
     |              population (e.g. ``ploidy=1`` for haploid population). Please refer
     |              to the ``Population()`` function of simuPOP for details.
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from variant_tools.pipeline.PipelineAction:
     |
     |  __call__(self, ifiles, pipeline=None)
     |      Execute action with input files ``ifiles`` with runtime information
     |      stored in ``pipeline``. This function is called by the pipeline and calls
     |      user-defined ``execute`` function.
     |
     |      Parameters:
     |
     |          ifiles (string or list of strings):
     |              input file names
     |
     |          pipeline (an pipeline object):
    



### 2. VST defined operators

VST is built on top of [simuPOP][2] and uses its forward-time simulation engine to perform forward and resampling-based simulations. It defines a number of customized simuPOP operators for that performs fine-scale recombination, reference-genome aware mutation, and protein based selection and quantitative trait models. These operators can be used in the `EvolvePopulation` action to perform realistic simulations of the human and other genomes. 



#### 2.1 `FineScaleRecombinator`

A fine-scale recombination operator for the human genome. 



    FineScaleRecombiantor(regions=None, scale=1, defaultRate=1e-8, output=None)
    

For specified regions of the chromosome, find genetic locations of all loci using a genetic map downloaded from HapMap. If no genetic map is used, a default recombination rate (per bp) is used. If a output file is specified, the physical/genetic map will be written to the file. If each element in regions has only length two, it is assumed to be a single-locus region. Finally, if a population object is specified, the regions will be obtained automatically from all loci of the population object. 



#### 2.2 `RefGenomeMutator`



    RefGenomeMutator(regions, model, rate)
    

This operator uses allele 0 as the reference allele at different loci and applies different `ActgMutator` according to the actual nuclotides on the reference genome. For example, if the reference genome is `ACCCCTTAGG`, it is represented by haplotype `0000000000`, and `1000000000` and `0200000000` represents `CCCCCTTAGG` and `ATCCCTTAGG` respectively (A->C->G->T). If you apply a Kimura's 2-parameter (K80) model ( [AcgtMutator][3]) to the reference genome, it will act differently at different location of the genome. 



#### 2.3 `ProteinSelector`

    ProteinSelector(regions, s_missense=0.001, s_stoploss=0.002, s_stopgain=0.01)
    

A protein selection operator that, for specified regions 

    1. find coding regions and pass them to PySelector
        2. find amino acid change of each individual
        3. return fitness caused by change of amino acid
    

s\_missense: selection coefficient for missense (nonsynonymous mutations) s\_stoploss: selection coefficient for stoploss muation (elongate protein) s_stopgain: selection coefficient for stopgan muation (premature coding of protein) 

Selection coefficient should be a single number (fixed s, with fitness 1-s). The fitness of multiple amino acid change will be Prod(1-si) even if two changes are at the same location (that is to say, a homozygote change will have fitness 1-2\*s-s\*2, which is close to an additive model for small s. 



#### 2.4 `ProteinPenetrance`



    ProteinPenetrance(regions, s_sporadic=0.0001, s_missense=0.001, s_stoploss=0.002, s_stopgain=0.01)
    

A protein penetrance model that is identical to ProteinSelector, but use 1 minus calculated fitness value as pentrance probability.

 [1]: http://varianttools.sourceforge.net/Calling/New
 [2]: http://simupop.sourceforge.net
 [3]: http://simupop.sourceforge.net/manual_svn/build/userGuide_ch5_sec6.html#nucleotide-mutation-models-acgtmutator
