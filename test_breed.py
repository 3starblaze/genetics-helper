#!/usr/bin/env python3

import pytest
from gene import breed, Genotype, GeneAllele


def test_sample_breeding_a():
    a = Genotype(GeneAllele('Z'), GeneAllele('z'))
    b = Genotype(GeneAllele('Z'), GeneAllele('z'))

    breeding_results = [str(genotype) for genotype in breed(a,b)]
    assert breeding_results == ['ZZ', 'Zz', 'zZ', 'zz']
