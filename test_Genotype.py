#!/usr/bin/env python3

import pytest
from gene import Genotype, GeneAllele


def test_genotype_identity():
    a = GeneAllele('h', '', '')
    b = GeneAllele('H', '', '')

    assert Genotype(a, b) == Genotype(a, b)

def test_incorrect_genotype_identity():
    a = GeneAllele('l', '', '')
    b = GeneAllele('L', '', '')

    assert Genotype(a, b) != Genotype(b, a)


def test_incorrect_different_gene_allele_types():
    a = GeneAllele('z', '', '')
    b = GeneAllele('c', '', '')

    with pytest.raises(ValueError):
        Genotype(a, b)


def test_incorrect_non_gene_allele_arguments():
    a = GeneAllele('k', '', '')
    b = 42
    with pytest.raises(ValueError):
        Genotype(a, b)


def test_to_str():
    a = GeneAllele('C', '', '')
    b = GeneAllele('c', '', '')
    g = Genotype(a, b)
    assert str(g) == 'Cc'
