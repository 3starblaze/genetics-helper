from table_gen import create_multi_gene_table
from gene_convenience import create_genotype as g
from gene_convenience import  create_multi_genotype as m
from gene import MultiGenotype

MGenotype1 = m("AaBb")
MGenotype2 = m("AaBb")

create_multi_gene_table(MGenotype1, MGenotype2)