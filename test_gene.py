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
