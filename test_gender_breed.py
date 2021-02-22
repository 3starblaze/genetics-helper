#!/usr/bin/env python3

import pytest
from gene import gender_breed, GeneAllele, XXGenotype, XYGenotype

def test_gender_breeding_with_XX_XY_chromosome():
    f = XXGenotype(GeneAllele("A"),GeneAllele("a"))
    m = XYGenotype(GeneAllele("A"))
    results = [str(g) for g in gender_breed(f, m)]
    assert results == ["X^AX^A","X^AY","X^aX^A","X^aY"]
