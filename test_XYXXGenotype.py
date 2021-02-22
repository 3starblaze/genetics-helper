#!/usr/bin/env python3

import pytest
from gene import GeneAllele, XYGenotype, XXGenotype


def test_xy_genotype():
    m = XYGenotype(GeneAllele('H'))
    assert m.gene_allele.value == 'H'


def test_xy_genotype_wrong_arg_type():
    with pytest.raises(ValueError):
        XYGenotype(42)

def test_xx_genotype():
    f = XXGenotype(GeneAllele('L'), GeneAllele('l'))
    assert f.gene_allele_a.value == 'L' and f.gene_allele_b.value == 'l'


def test_xx_genotype_wrong_arg_type():
    with pytest.raises(ValueError):
        XXGenotype(GeneAllele('c'), 39)
