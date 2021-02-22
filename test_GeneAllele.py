#!/usr/bin/env python3

import pytest
from gene import GeneAllele


def test_equality():
    assert GeneAllele('J') == GeneAllele('J')


def test_different_value_case_are_not_same():
    assert GeneAllele('F') != GeneAllele('f')
