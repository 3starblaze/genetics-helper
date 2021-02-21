#!/usr/bin/env python3

from gene import GeneAllele, Genotype

def create_genotype(genotype_str: str):
    if type(genotype_str) != str:
        raise ValueError('genotype_str must be a string!')
    if len(genotype_str) != 2:
        raise ValueError('genotype_str must have length of 2 characters!')
    return Genotype(GeneAllele(genotype_str[0]), GeneAllele(genotype_str[1]))
