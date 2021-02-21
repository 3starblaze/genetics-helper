#!/usr/bin/env python3

import pytest
from gene import gender_breed, Genotype, GeneAllele, XXGenotype, XYGenotype


def test_sample_gender_breeding():
    XX = ["Z", "z"]
    XY = ("Z")
    breeding_results = (gender_breed(XXGenotype(XX) ,XYGenotype(XY)))
    assert breeding_results == ["XZXZ","XZY","XzXZ","XzY"]
