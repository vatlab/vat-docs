+++
title = "rsname"
weight = 4
+++

## Importing variants from a list of dbSNP iDs (rsnames)


### 1. Format description

    % vtools show format rsname
    
    Import variants (chr, pos, ref, alt) that are queried from dbSNP database
    using provided rsnames
    
    Columns:
      None defined, cannot export to this format
    
    variant:
      chr                   Obtain chromosome from dbSNP by rsname
      pos                   Obtain position from dbSNP by rsname
      ref                   Obtain reference allele from dbSNP by rsname
      alt                   Obtain alternative allele from dbSNP by rsname
    
    Format parameters:
      sep                   delimiter used to separate input fields (default: ',')
      rsname_col            Index for the column with rsname (default: 1)
      dbfile                Name of an attached dbSNP database or path to the
                            dbSNP database in sqlite format (default: dbSNP-
                            hg19_138.DB)
    



### 2. Details

This format retrieves variant information from `dbSNP`. To use this format, you should first download and decompress the dbSNP database 



    % vtools init format rsname
    % vtools use dbSNP-hg19_138
    

You can then use the database to import variants from a list of rsnames: 



    % vtools import variants.txt --format rsname --build hg19
    
    INFO: Importing variants from variants.txt (1/1)
    variants.txt: 100% [==================================] 25,462 9.6K/s in 00:00:02
    INFO: 25,944 new variants (25,885 SNVs, 50 insertions, 11 deletions) from 25,462 lines are imported.
    WARNING: Sample information is not recorded for a file without genotype and sample name.
    Importing genotypes: 0 0.0/s in 00:00:00
    Copying samples: 0 0.0/s in 00:00:00
    



If a rsname corrsponds to multiple variants, all of them will be imported. For example, `rs111688037` can import variants `NM_004638.3:c.5085T>A` and `NM_004638.3:c.5085T>C` (chr6:31602679). 



#### 2.1 Use a different version of dbSNP

If you are interested in using a different version of dbSNP, you will need to 



1.  Use command `vtools use dbSNP-VER` to download and decompress another version of dbSNP 
2.  Use option `--dbfile dbSNP-VER.DB` to use an alternative db file. 

If your database file has different fields, please edit `rsname.fmt` to use the correct field names.
