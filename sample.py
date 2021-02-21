#!/usr/bin/env python3

from gene import Genotype, GeneAllele
from table_gen import create_table

g1 = Genotype(GeneAllele('A'), GeneAllele('a'))
g2 = Genotype(GeneAllele('A'), GeneAllele('a'))

create_table(g1, g2)
