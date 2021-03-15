#!/usr/bin/env python3

import pytest
from gene import Genotype, GeneAllele, MultiGenotype
from gene_convenience import create_genotype
from gene_convenience import create_multi_genotype

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

def test_invalid_mgene_str_len_1():
    with pytest.raises(ValueError):
        create_multi_genotype("AAA")

def test_sample_mgene_1():
    verbose_mgene = MultiGenotype(create_genotype("Aa"), create_genotype("Bb"))
    convinient_mgene = create_multi_genotype("AaBb")
    assert verbose_mgene == convinient_mgene

def test_sample_mgene_2():
    verbose_mgene = MultiGenotype(create_genotype("ĢĢ"), create_genotype("Zz"))
    convinient_mgene = create_multi_genotype("ĢĢZz")
    assert verbose_mgene == convinient_mgene

def test_invalid_mgene_input_type():
    with pytest.raises(TypeError):
        create_multi_genotype(123)

def test_invalid_mgene_str_len_2():
    with pytest.raises(ValueError):
        create_multi_genotype("A")
