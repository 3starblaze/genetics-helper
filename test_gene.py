#!/usr/bin/env python3

import pytest
from gene import Gene


def test_gene_equality_1():
    assert (
        Gene('z', 'tall height', 'short height')
        == Gene('z', 'tall height', 'short height')
    )


def test_gene_equality_2():
    assert(
        Gene('a', 'big nose', 'small nose')
        != Gene('a', 'has horns', 'no horns')
    )
