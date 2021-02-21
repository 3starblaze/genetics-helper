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


def test_equality_1():
    assert MultiGenotype(G('ll'), G('Aa')) == MultiGenotype(G('ll'), G('Aa'))


def test_equality_2():
    assert MultiGenotype(G('bb'), G('cc')) != MultiGenotype(G('BB'), G('CC'))
