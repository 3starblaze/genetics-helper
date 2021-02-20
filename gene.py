#!/usr/bin/env python3

from typing import Optional


def legal_gene_identifier(gene):
    return (
        type(gene is str)
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
        if not legal_gene_identifier(identifier):
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
