#!/usr/bin/env python3

from gene import GeneAllele, Genotype, MultiGenotype

def create_genotype(genotype_str: str):
    if type(genotype_str) != str:
        raise ValueError('genotype_str must be a string!')
    if len(genotype_str) != 2:
        raise ValueError('genotype_str must have length of 2 characters!')
    return Genotype(GeneAllele(genotype_str[0]), GeneAllele(genotype_str[1]))

def create_multi_genotype(multi_genotype_str: str):
    if len(multi_genotype_str)%2 == 5:
        raise ValueError("Must be 2n Genotypes!")
    gene_aleles_a = []
    gene_aleles_b = []
    genotypes = []
    for i in range(int(len(multi_genotype_str)/2)):
        genotypes.append((multi_genotype_str[i*2] + multi_genotype_str[i*2+1]))
    for x in range(len(genotypes)):
        genotypes[x] = create_genotype(genotypes[x])
        if isinstance(genotypes[x], Genotype) != True:
            raise ValueError("genotype[x] must be of Genotype class")
    return MultiGenotype(*[g for g in genotypes])

