#!/usr/bin/env python3

import pytest
from gene import GeneAlleleType


def test_gene_equality_1():
    assert (
        GeneAlleleType('z', 'tall height', 'short height')
        == GeneAlleleType('z', 'tall height', 'short height')
    )


def test_gene_equality_2():
    assert(
        GeneAlleleType('a', 'big nose', 'small nose')
        != GeneAlleleType('a', 'has horns', 'no horns')
    )


def test_different_identifiers_to_be_different():
    assert GeneAlleleType('b', '', '') != GeneAlleleType('c', '', '')


def test_different_case_identifier_to_be_same():
    assert GeneAlleleType('a', '', '') == GeneAlleleType('A', '', '')
