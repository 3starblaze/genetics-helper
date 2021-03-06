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


def test_no_duplicate_genotype_classes():
    with pytest.raises(ValueError):
        MultiGenotype(G('Zz'), G('ZZ'))


def test_2_genotype_breeding_1():
    mg1 = MultiGenotype(G('Aa'), G('Bb'))
    mg2 = MultiGenotype(G('Aa'), G('Bb'))
    assert mg1.breed(mg2) == [
        'AABB', 'AABb', 'AaBB', 'AaBb',
        'AAbB', 'AAbb', 'AabB', 'Aabb',
        'aABB', 'aABb', 'aaBB', 'aaBb',
        'aAbB', 'aAbb', 'aabB', 'aabb'
    ]

def test_2_genotype_breeding_2():
    mg1 = MultiGenotype(G('ff'), G('cC'))
    mg2 = MultiGenotype(G('fF'), G('cc'))
    assert mg1.breed(mg2) == [
        'ffcc', 'ffcc', 'fFcc', 'fFcc',
        'ffCc', 'ffCc', 'fFCc', 'fFCc',
        'ffcc', 'ffcc', 'fFcc', 'fFcc',
        'ffCc', 'ffCc', 'fFCc', 'fFCc',
    ]


def test_incompatible_multi_genotypes():
    mg1 = MultiGenotype(G('kK'), G('yY'))
    mg2 = MultiGenotype(G('kk'), G('sS'))
    with pytest.raises(ValueError):
        mg1.breed(mg2)


def test_misshapen_multi_genotypes():
    mg1 = MultiGenotype(G('kK'), G('Ll'))
    mg2 = MultiGenotype(G('kk'), G('ll'), G('cC'))
    with pytest.raises(ValueError):
        mg1.breed(mg2)
