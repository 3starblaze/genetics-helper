from table_gen import create_multi_gene_table
from gene_convenience import create_genotype as g
from gene_convenience import  create_multi_genotype as m
from gene import MultiGenotype

MGenotype1 = m("ttdd")
MGenotype2 = m("ttDd")
#Can they be diferent grrr?
create_multi_gene_table(MGenotype1, MGenotype2)