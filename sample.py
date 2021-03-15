#!/usr/bin/env python3

from gene_convenience import create_genotype as G
from gene import XYGenotype, XXGenotype, GeneAllele, MultiGenotype
from table_gen import Document

(Document()
 .create_table(G('Aa'), G('Aa'))
 .create_gender_table(
     XXGenotype(GeneAllele('A'), GeneAllele('a')),
     XYGenotype(GeneAllele('a')))
 .create_multi_gene_table(
     MultiGenotype(G('Aa'), G('Bb')),
     MultiGenotype(G('Aa'), G('Bb')))
 .save('better-example.docx'))
