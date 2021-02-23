from table_gen import create_multi_gene_table
from gene_convenience import create_genotype as g
from gene import MultiGenotype

MGenotype1 = MultiGenotype(g("Aa"), g("Bb"))
MGenotype2 = MultiGenotype(g("Aa"), g("Bb"))

create_multi_gene_table(MGenotype1, MGenotype2)