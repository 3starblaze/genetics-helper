#!/usr/bin/env python3

from typing import Optional


def is_legal_gene_allele(gene):
    return (
        type(gene) is str
        and len(gene) == 1
        and gene.lower() != gene.upper() # Check gene can be capitalized
    )


class GeneAllele:
    def __init__(self, value: str):
        self.value = value


    def __eq__(self, other):
        if not isinstance(other, GeneAllele):
            return NotImplemented
        return self.value == other.value


def is_same_gene_allele_type(gene_a: GeneAllele, gene_b: GeneAllele):
    return gene_a.value.lower() == gene_b.value.lower()


class Genotype:
    def __init__(self, gene_allele_a: GeneAllele, gene_allele_b: GeneAllele):
        if (
            not isinstance(gene_allele_a, GeneAllele)
            or not isinstance(gene_allele_b, GeneAllele)
        ):
            raise ValueError('Arguments must be objects of GeneAllele class!')

        if not is_same_gene_allele_type(gene_allele_a, gene_allele_b):
            raise ValueError('Gene alleles must be of same type!')

        self.gene_allele_a = gene_allele_a
        self.gene_allele_b = gene_allele_b


    def __eq__(self, other):
        return (
            self.gene_allele_a == other.gene_allele_a
            and self.gene_allele_b == other.gene_allele_b
        )


    def __str__(self):
        return self.gene_allele_a.value + self.gene_allele_b.value


def breed (genotype_a: Genotype, genotype_b: Genotype):
    if (
        not isinstance(genotype_a, Genotype)
        or not isinstance(genotype_a, Genotype)
    ):
        raise ValueError("Arguments must be objects of class Genotype!")

    results = []
    for allele_a in [genotype_a.gene_allele_a, genotype_a.gene_allele_b]:
        for allele_b in [genotype_b.gene_allele_a, genotype_b.gene_allele_b]:
            results.append(Genotype(allele_a, allele_b))

    return results


class XYGenotype:
    def __init__(self, gene_allele_a: GeneAllele):
        self.gene_allele_a = gene_allele_a
        self.gene_allele_b = None
    def __str__(self):
        return f"X^{self.gene_allele_a}Y"

class XXGenotype:
    def __init__(self, gene_allele_a: GeneAllele, gene_allele_b:GeneAllele):
        self.gene_allele_a = gene_allele_a
        self.gene_allele_b = gene_allele_b
    def __str__(self):
        return f"X^{self.gene_allele_a}X^{self.gene_allele_b}"

def gender_breed(female: XXGenotype, male: XYGenotype):
    breeding_results = []
    for allele_a in [female.gene_allele_a, female.gene_allele_b]:
        for allele_b in [male.gene_allele_a, male.gene_allele_b]:
            if allele_b != None:
                breeding_results.append(XXGenotype(allele_a,allele_b))
            else:
                breeding_results.append(XYGenotype(allele_a))
    return breeding_results
