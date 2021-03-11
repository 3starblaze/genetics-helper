#!/usr/bin/env python3

from gene_convenience import create_genotype as G
from gene import XYGenotype, XXGenotype, GeneAllele
from table_gen import Document

(Document()
 .create_table(G('Aa'), G('Aa'))
 .create_gender_table(
     XXGenotype(GeneAllele('A'), GeneAllele('a')),
     XYGenotype(GeneAllele('a')))
 .save('better-example.docx'))
