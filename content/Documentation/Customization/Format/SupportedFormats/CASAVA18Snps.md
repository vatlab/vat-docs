+++
title = "CASAVA18Snps"
weight = 10
+++

## CASAVA18Snps

### Sample data

    #	**	CASAVA	depth-filtered	snp	calls	**
    #$	CMDLINE	/CASAVA-1.8.0a19/filterSmallVariants.pl	--chrom=chr1
    #$	SEQ_MAX_DEPTH	chr1	142.345267150165
    #
    #$	COLUMNS	seq_name	pos	bcalls_used	bcalls_filt	ref	Q(snp)	max_gt	Q(max_gt)	max_gt|poly_site	Q(max_gt|poly_site)	A_used	C_used	G_used	T_used
    chr1	10231	5	9	C	28	AC	28	AC	59	3	2	0	0
    chr1	10255	14	29	A	1	AA	9	AT	25	12	0	0	2
    chr1	10264	15	19	C	18	AC	18	AC	51	4	11	0	0
    chr1	10291	2	16	C	1	CC	10	CT	21	0	1	0	1
    chr1	10330	3	14	C	2	CC	5	AC	28	2	1	0	0
    chr1	13273	9	0	G	58	CG	54	CG	57	0	6	3	0
    chr1	14464	18	0	A	60	AT	60	AT	93	12	0	0	6
    chr1	14673	19	0	G	63	CG	63	CG	96	0	8	11	0
    chr1	14699	23	0	C	72	CG	72	CG	105	0	14	9	0
    chr1	14907	13	0	A	118	AG	65	AG	65	4	0	9	0
    chr1	14930	14	2	A	119	AG	68	AG	68	5	0	9	0
    chr1	14933	14	2	G	78	AG	78	AG	110	6	0	8	0
    chr1	14976	4	0	G	18	AG	18	AG	47	2	0	2	0
    chr1	15211	2	0	T	37	GG	5	GG	5	0	0	2	0
    chr1	15817	1	0	G	11	GT	3	GT	3	0	0	0	1
    chr1	15820	1	0	G	11	GT	3	GT	3	0	0	0	1
    chr1	16487	12	0	T	62	CT	62	CT	94	0	6	0	6
    chr1	17538	64	0	C	88	AC	88	AC	121	18	46	0	0
    chr1	17746	53	1	A	22	AG	22	AG	55	39	0	14	0
    chr1	17765	47	1	G	26	AG	26	AG	59	13	0	34	0
    chr1	20131	1	0	G	8	CG	2	CG	3	0	1	0	0
    chr1	20144	1	0	G	9	AG	2	AG	3	1	0	0	0
    chr1	20206	2	0	C	4	CT	4	CT	30	0	1	0	1
    chr1	20245	3	0	G	4	AG	4	AG	34	1	0	2	0
    chr1	20304	2	0	G	2	GG	5	CG	27	0	1	1	0
    



## Example

    vtools import --format Illumina_SNP Illumina_SNP.txt --build hg18
    
    INFO: Opening project f.proj
    INFO: Additional genotype fields: Q_max_gt
    INFO: Importing genotype from Illumina_SNP.txt (1/1)
    Illumina_SNP.txt: 30
    

The variants are 



    vtools show table variant -l -1
    
    INFO: Opening project f.proj
    variant_id, bin, chr, pos, ref, alt
    1, 585, 1, 10231, C, A
    2, 585, 1, 10264, C, A
    3, 585, 1, 13273, G, C
    4, 585, 1, 14464, A, T
    5, 585, 1, 14673, G, C
    6, 585, 1, 14699, C, G
    7, 585, 1, 14907, A, G
    8, 585, 1, 14930, A, G
    9, 585, 1, 14933, G, A
    10, 585, 1, 14976, G, A
    11, 585, 1, 15817, G, T
    12, 585, 1, 15820, G, T
    13, 585, 1, 16487, T, C
    14, 585, 1, 17538, C, A
    15, 585, 1, 17746, A, G
    16, 585, 1, 17765, G, A
    17, 585, 1, 20131, G, C
    18, 585, 1, 20144, G, A
    19, 585, 1, 20206, C, T
    20, 585, 1, 20245, G, A
