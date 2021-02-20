#!/usr/bin/env python3

from typing import Optional


def legal_gene_identifier(gene):
    return (
        type(gene is str)
        and len(gene) == 1
        and gene.lower() != gene.upper() # Check gene can be capitalized
    )


class Gene:
    def __init__(
            self,
            identifier: str,
            dominant_property: str,
            recessive_property: str,
            codominant_property: Optional[str] = None
    ):
        if not legal_gene_identifier(identifier):
            raise "Not a legal identifier"
        self.identifier = identifier
        self.dominant_property = dominant_property
        self.recessive_property = recessive_property
        self.codominant_property = codominant_property


    def __eq__(self, other):
        if not isinstance(other, Gene):
            return NotImplemented
        return (
            self.identifier == other.identifier
            and self.dominant_property == other.dominant_property
            and self.recessive_property == other.recessive_property
            and self.codominant_property == other.codominant_property
        )
