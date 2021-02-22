#!/usr/bin/env python3

import pytest
from gene import gender_breed, GeneAllele, XXGenotype, XYGenotype

def test_gender_breeding_with_XX_XY_chromosome():
    female = XXGenotype(GeneAllele("A"),GeneAllele("a"))
    male = XYGenotype(GeneAllele("A"))
    results = gender_breed(female,male)
    test_results = ["X^AX^A","X^AY","X^aX^A","X^aY"]
    for i in range(len(results)):
        assert str(results[i]) == test_results[i]