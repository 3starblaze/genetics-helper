#!/usr/bin/env python3

import pytest
from gene import is_legal_gene_allele


def test_correct_gene_allele():
    assert is_legal_gene_allele('F') and is_legal_gene_allele('k')


def test_correct_unicode_gene_allele():
    assert is_legal_gene_allele('ķ')


def test_incorrect_as_gene_allele_number():
    assert not is_legal_gene_allele(4)


def test_incorrect_as_gene_allele_string_list():
    assert not is_legal_gene_allele(['h'])


def test_incorrect_gene_allele_length():
    assert not is_legal_gene_allele('ok')


def test_incorrect_gene_allele_uncapitalizable():
    assert not is_legal_gene_allele('@')
