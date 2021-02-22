from table_gen import create_multi_gene_table
from gene_convenience import create_genotype as G
from gene import MultiGenotype

MGenotype1 = MultiGenotype(G("Aa"), G("Bb"))
MGenotype2 = MultiGenotype(G("Aa"), G("Bb"))

create_multi_gene_table(MGenotype1, MGenotype2)