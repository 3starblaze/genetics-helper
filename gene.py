#!/usr/bin/env python3

from typing import Optional


def is_legal_gene_allele(gene):
    return (
        type(gene) is str
        and len(gene) == 1
        and gene.lower() != gene.upper() # Check gene can be capitalized
    )


class GeneAlleleType:
    def __init__(
            self,
            identifier: str,
            dominant_property: str,
            recessive_property: str,
            codominant_property: Optional[str] = None
    ):
        if not is_legal_gene_allele(identifier):
            raise "Not a legal identifier"
        self.identifier = identifier.upper()
        self.dominant_property = dominant_property
        self.recessive_property = recessive_property
        self.codominant_property = codominant_property


    def __eq__(self, other):
        if not isinstance(other, GeneAlleleType):
            return NotImplemented
        return (
            self.identifier == other.identifier
            and self.dominant_property == other.dominant_property
            and self.recessive_property == other.recessive_property
            and self.codominant_property == other.codominant_property
        )


class GeneAllele:
    def __init__(
            self,
            value: str,
            dominant_property: str,
            recessive_property: str,
            codominant_property: Optional[str] = None
    ):
        self.value = value
        self.gene_allele_type = GeneAlleleType(
            value, dominant_property, recessive_property, codominant_property
        )
        self.is_dominant = value == value.upper()


    def __eq__(self, other):
        if not isinstance(other, GeneAllele):
            return NotImplemented
        return (
            self.gene_allele_type == other.gene_allele_type
            and self.is_dominant == other.is_dominant
        )


class Genotype:
    def __init__(self, gene_allele_a: GeneAllele, gene_allele_b: GeneAllele):
        if (
            not isinstance(gene_allele_a, GeneAllele)
            or not isinstance(gene_allele_b, GeneAllele)
        ):
            raise ValueError('Arguments must be objects of GeneAllele class!')

        if gene_allele_a.gene_allele_type != gene_allele_b.gene_allele_type:
            raise ValueError('Gene alleles must have same type!')

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
#XY breeding thingie
class XYGenotype:
    def __init__(self,gene_allele_a):
        self.chromosome_a = ["X", str(gene_allele_a)]
        self.chromosome_b = ["Y", ""]

class XXGenotype:
    def __init__(self,gene_allele_ab):
        self.chromosome_a = ["X", str(gene_allele_ab[0])]
        self.chromosome_b = ["X", str(gene_allele_ab[1])]

def gender_breed(female: XXGenotype, male: XYGenotype):
    results = []
    for Chromosome_A in [female.chromosome_a,female.chromosome_b]:
        for Chromosome_B in [male.chromosome_a, male.chromosome_b]:
            results.append(Chromosome_A[0]+Chromosome_A[1] + Chromosome_B[0]+Chromosome_B[1])
    return results
