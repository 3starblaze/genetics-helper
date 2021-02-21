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


def test_2_genotype_breeding_1():
    mg1 = MultiGenotype(G('Aa'), G('Bb'))
    mg2 = MultiGenotype(G('Aa'), G('Bb'))
    assert mg1.breed(mg2) == [
        'AABB', 'AABb', 'AAbB', 'AAbb',
        'AaBB', 'AaBb', 'AabB', 'Aabb',
        'aABB', 'aABb', 'aAbB', 'aAbb',
        'aaBB', 'aaBb', 'aabB', 'aabb',
    ]

def test_2_genotype_breeding_2():
    mg1 = MultiGenotype(G('ff'), G('cC'))
    mg2 = MultiGenotype(G('fF'), G('cc'))
    assert mg1.breed(mg2) == [
        'ffcc', 'ffcc', 'ffCc', 'ffCc',
        'fFcc', 'fFcc', 'fFCc', 'fFCc',
        'ffcc', 'ffcc', 'ffCc', 'ffCc',
        'fFcc', 'fFcc', 'fFCc', 'fFCc',
    ]
