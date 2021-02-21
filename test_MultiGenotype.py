#!/usr/bin/env python3

import pytest
from gene import MultiGenotype
from gene_convenience import create_genotype as G


def test_2_genotypes():
    assert str(MultiGenotype(G('Aa'), G('cc'))) == 'Aacc'


def test_3_genotypes():
    assert str(MultiGenotype(G('kK'), G('FF'), G('Rr'))) == 'kKFFRr'


def test_wrong_args():
    with pytest.raises(ValueError):
        MultiGenotype(G('Cc'), 42)
