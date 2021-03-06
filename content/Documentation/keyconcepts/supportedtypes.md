+++
title = "Variants"
weight = 1
+++

## Supported types of variants


### How variants are imported and stored in variant tools

**Variant tools** import different types of variants as follows: 



| **Type**  | **Reference** | **Alternative** | **Imported Variant(s)** | **Note**                       |
|-------------|------------|-----------------|-------------------------|----------------------------------|
| SNV       | `A`           | `G`             | `A`,`G`                 |                                |
|           | `TC`          | `TG`            | `C`,`G`                 | pos + 1                        |
| Deletion  | `TC`          | `T`             | `C,-`                   | pos + 1                        |
|           | `TCG`         | `TG`            | `C,-`                   | pos + 1                        |
|           | `TCGC`        | `TC`            | `GC,-`                  | pos + 2, *                     |
|           | `TC`          | `-` or `.`      | `TC,-`                  | Not VCF compatible             |
| Insertion | `TCG`         | `TCAG`          | `-,A`                   | pos + 2                        |
|           | `TC`          | `TCA`           | `-,A`                   | pos + 2                        |
|           | `-` or `.`    | `A`             | `-,A`                   | not VCF compatible             |
| MNP       | `AA`          | `ATAAC`         | `A,TAAC`                | pos + 1                        |
|           | `TACT`        | `TCTA`          | `ACT,CTA`               | pos + 1                        |
| Mixed     | `A`           | `C,G`           | `A,C` `A,G`             | Two single nucleotide variants |
|           | `TC`          | `TCGG,T`        | `-,GG` `C,-`            | A deletion and an insertion    |

Note that 

1.  `-` or `.` are treated as missing allele and can be used to import indels. 
2.  When reference and alternative variants have common leading alleles, variant positions are adjusted. For example, `10, ACG, A` will be imported as variant `CG,-` at position 11. The Common ending alleles are also removed. We remove common leading alleles greedily to avoid ambiguity. For example, deletion `TCGC`->`GC` (case * in the table) can be intepretted as a deletion of `GC` at pos + 2 and `CG` at pos + 1, *variant tools* uses the first interpretation. 
3.  When there are multiple alternative variants, they are treated as multiple variants. If a sample with two alternative variants are imported, the sample will have *other* type for this variant, in contrast to homozygote (two identical alternative variant) and heterozygote (one reference and one alternative variant. 
4.  Although indels could be imported, annotation database for these kinds of variants are, essentially, non-exist at this time. Using command `vtools import --format ANNOVAR` to import annotation for ANNOVAR might be a good choice.