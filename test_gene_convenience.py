#!/usr/bin/env python3

import pytest
from gene import Genotype, GeneAllele
from gene_convenience import create_genotype

def test_sample_genotype_1():
    verbose_genotype = Genotype(GeneAllele('C'), GeneAllele('c'))
    convenient_genotype = create_genotype('Cc')
    assert convenient_genotype == verbose_genotype


def test_sample_genotype_2():
    verbose_genotype = Genotype(GeneAllele('ž'), GeneAllele('ž'))
    convenient_genotype = create_genotype('žž')
    assert convenient_genotype == verbose_genotype


def test_invalid_genotype_str_length_1():
    with pytest.raises(ValueError):
        create_genotype('m')


def test_invalid_genotype_str_length_3():
    with pytest.raises(ValueError):
        create_genotype('HhH')


def test_invalid_genotype_str_type():
    with pytest.raises(ValueError):
        create_genotype(777)
