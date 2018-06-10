
+++
title = "bwa_gatk33_hg19"
weight = 1
+++



## Variant calling using BWA and GATK best practice pipeline 



### 1. Usage

    % vtools show pipeline bwa_gatk33_hg19
    
    A pipeline to align raw reads from fastq or BAM/SAM files using BWA and GATK best practice. It uses hg19 of human reference genome and assumes
    paired-end reads in plain text and compressed formats.
    
    Available pipelines: align
    
    Pipeline "align":  Align raw reads from input files using bwa, gatk, and picard. This pipeline accepts raw input files in plain text format, SAM/BAM
    format, and their compressed versions (.zip, .tar.gz, .tgz, .bz2, .tbz2 etc). All input files are assumed to be raw reads from the same sample. This
    pipeline generates a calibrated bam file (--output), and its reduced version if an additional output file is specified.
      align_0:            Check the version of variant tools (version 2.1.1 and above is required to execute this pipeline)
      align_1:            Check if a name has been asigned to the job
      align_2:            Check path to GATK jar file
      align_3:            Check path to Picard jar file
      align_10:           Check existence of commands bwa, samtools and java
      align_11:           Check the version of bwa. Version is 0.7.4 is recommended
      align_12:           Check the version of picard. Version is 1.82 is recommended.
      align_13:           Check the version of GATK. Version 3.3 is recommended.
      align_20:           Check existence of class files for Picard and GATK
      align_50:           Download the GATK resource bundle to resource directory
      align_60:           Build bwa index for build hg19 of reference genome
      align_100:          Convert bam files to paired fastq files if the input is in bam/sam format. Other input files are returned untouched.
      align_101:          Decompress all input files (.tgz2, .tar, .tar.gz, .gz, .tgz, .zip etc) to a cache directory. Uncompressed files are hard-
                          linked to the cache directory.
      align_200:          Check the format of the input fastq file and write an option file with option -I if the sequences are in Illumina 1.3+ format.
      align_201:          Call bwa aln to produce .sai files
      align_300:          Running bwa sampe for paired end reads, using read group tag saved in a .RG file
      align_302:          Check the proportion of aligned reads and exit if there are less than 80% of aligned reads.
      align_303:          If in production mode, remove fastq files dumped from bam files
      align_400:          Merge per-lane sam files into a single bam file. This step is skipped if there is only one input file.
      align_500:          Sort merged bam file using picard SortSam
      align_501:          If in production mode, remove decompressed fastq and individual bam files after a single bam file has been produced.
      align_600:          Mark duplicates using picard MarkDuplicates command
      align_601:          Remove _sorted.bam file after deduplication is completed.
      align_610:          Index dedupped bam file using samtools
      align_700:          Realign indels create indel realigner target
      align_710:          Apply indel realigner target to bam file
      align_711:          If in production mode, remove bam files before realignment steps
      align_800:          Create base recalibrator target
      align_810:          Apply base recalibrator target
      align_811:          If in production mode, remove bam files before realignment steps
      align_900:          Generated bam file with reduced reads if more than one output file is specified
      align_1000:         Send a warning message if default read group is used.
      align_1001:         Send a warning message if default read group is used.
    
    Pipeline parameters:
      name                Name of the job to be executed. All intermediate files generated from this pipeline will be saved to $CACHE_DIR/$NAME where
                          $CACHE_DIR is the cache directory of the project.
      strict_prog_version Whether or not use other version of programs if the exact version does not exist. Setting it to False allows variant tools to
                          use other versions of the programs. (default: False)
      production          If set to True or 1, all intermediate files will be removed. The whole pipeline would need to be rerun if a different
                          parameter or different version of external program is used. (default: False)
      picard_path         Path to picard jar files
      gatk_path           Path to GATK jar file GenomeAnalysisTK.jar
      rgid                Read group ID (default: 1)
      rglb                Read group Library. (default: LIB)
      rgpl                Read group Platform (default: Illumina)
      rgsm                Read group sample name. Value of parameter --name will be used if this parameter is left unspecified.
      rgpu                Read group platform unit (e.g. flowcall-barcode.lane). (default: FC.1)
      opt_java            Option to java program. -Djava.io.tmpdir is frequently used to set java temporary directory if system temporary partition is
                          not big enough. (default: -Xmx4g -XX:-UseGCOverheadLimit -Djava.io.tmpdir=${TEMP_DIR}/tmp)
      opt_bwa_index       Option to command 'bwa index'
      opt_bwa_aln         Option to command 'bwa aln'
      opt_bwa_sampe       Option to command 'bwa sampe'
      opt_samtools_faidx  Option to command 'samtools faidx'
      opt_samtools_index  Option to command 'samtools index'
      opt_picard_sortsam  Option to picard SortSam.jar (default: VALIDATION_STRINGENCY=LENIENT)
      opt_picard_mergesamfiles Option to picard MergeSamFiles.jar (default: MAX_RECORDS_IN_RAM=5000000)
      opt_picard_samtofastq Option to picard SamToFastq.jar (default: VALIDATION_STRINGENCY=LENIENT NON_PF=true)
      opt_picard_markduplicates Option to picard MarkDuplicates.jar
      opt_gatk_realignertargetcreator Option to command gatk RealignerTargetCreator
      opt_gatk_indelrealigner Option to command gatk IndelRealigner (default: --filter_mismatching_base_and_quals)
      opt_gatk_baserecalibrator Option to command gatk BaseRecalibrator (default: -rf BadCigar)
      opt_gatk_printreads Option to command gatk PrintReads
      opt_gatk_reducereads Option to command gatk ReduceReads
    


{{% notice warning%}}
Please specify correct readgroup information using parameters `--RGID`, `--RGLB`, `--RGPL`, `--RGPU` and `--RGSM` if you plan to analyze the generated bam file with other files (e.g. joint variant calling). 
{{% /notice %}}


### 2. Details

#### 2.1 Set up environment

This pipeline uses the following external commands: 



*   [bwa][1] 
*   [samtools][2] 
*   [Picard][3] 
*   [GATK][4] 

You should add path to bwa and samtools to `$PATH` so that the pipeline can find these tools. The pipeline expects to use certain versions of the tools. You can pass --strict_version no to use newer tools but the pipeline might not work as expected. Paths to `Picard` and `GATK` should be passed using options `gatk_path` and `picard_path`. 



#### 2.2 Test the environment

After you installed the programs, you should running the following commands to test if everything works ok: 



    # create a new project and download test data (an online snapshot)
    % vtools init test --parent vt_illuminaTestData
    % vtools execute bwa_gatk33_hg19 align --input illumina_test_seq.tar.gz --output test.bam \
        --gatk_path /path/to/gatk --picard_path /path/to/picard --name test
    

This command will not only test the availability of tools, but also download all required resource files and build necessary indexes. 



#### 2.3 Executing the pipeline in production mode

The pipeline will by default keep all intermediate files. If you restart the pipeline with different parameter or a different version of an external file, only the affected steps will be repeated. Intermediate files will be reused if available. This allows you to examine and fine-tune the pipeline to make sure it works as expected. 

Because intermediate files can be large, an option `--production true` is provided to execute the pipeline in production mode. In this mode, most intermediate files will be removed after the completion of the steps that make use of them. The pipeline can resume from the right step if it is interrupted, but has to be re-executed from the beginning if a result file is removed.

 [1]: http://bio-bwa.sourceforge.net/
 [2]: http://samtools.sourceforge.net/
 [3]: http://picard.sourceforge.net/
 [4]: http://www.broadinstitute.org/gatk/