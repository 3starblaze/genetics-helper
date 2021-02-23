#!/usr/bin/env python3

from typing import Optional, Sequence
from functools import reduce
from itertools import product, chain


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


class MultiGenotype:
    def __init__(self, *genotypes: Sequence[Genotype]):
        for genotype in genotypes:
            if not isinstance(genotype, Genotype):
                raise ValueError(f"{ genotype } is not an instance of Genotype!")

        # Genotype classes are obtained by forcing the same case
        genotype_classes = [str(g).lower() for g in genotypes]
        # set() never contains duplicates, if the new set has different length than
        # list, that means the list contains duplicates
        if len(genotype_classes) != len(set(genotype_classes)):
            raise ValueError("MultiGenotype can't contain duplicate Genotypes!")

        self.genotypes = genotypes

    def __str__(self):
        return reduce(lambda g1, g2: str(g1) + str(g2), self.genotypes)

    def __eq__(self, other):
        if not isinstance(other, MultiGenotype):
            return NotImplemented
        return str(self) == str(other)


    def breed(self, other):
        if not isinstance(other, MultiGenotype):
            raise ValueError(
                "MultiGenotype instance must be breeded with a MultiGenotype"
                + "instance!"
            )
        if (
            len(self.genotypes) != len(other.genotypes)
            # Quick way to check if there's same gene type
            or str(self).lower() != str(other).lower()
        ):
            raise ValueError("Genotype classes don't match!")

        basic_breeds = []

        f_half_genotype = [
            "".join(chars) for chars in product(*[str(g) for g in self.genotypes])
        ]
        m_half_genotype = [
            "".join(chars) for chars in product(*[str(g) for g in other.genotypes])
        ]

        return [
            "".join(chain.from_iterable(x)) for x in
            [list(zip(*x)) for x in product(f_half_genotype, m_half_genotype)]
        ]
