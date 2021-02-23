#!/usr/bin/env python3

from docx import Document
from gene import Genotype, GeneAllele, breed, MultiGenotype
from typing import Sequence
from gene_convenience import create_genotype as g


def create_table(genotype_a: Genotype, genotype_b: Genotype):
    document = Document()
    table = document.add_table(rows = 3, cols = 3)

    def set_cell(row, col, val):
        table.rows[row].cells[col].text = val

    set_cell(0, 0, "♀ \ ♂")

    set_cell(0, 1, genotype_b.gene_allele_a.value)
    set_cell(0, 2, genotype_b.gene_allele_b.value)
    set_cell(1, 0, genotype_a.gene_allele_a.value)
    set_cell(2, 0, genotype_a.gene_allele_b.value)

    breeding_results = [str(g) for g in breed(genotype_a, genotype_b)]

    set_cell(1, 1, breeding_results[0])
    set_cell(1, 2, breeding_results[1])
    set_cell(2, 1, breeding_results[2])
    set_cell(2, 2, breeding_results[3])

    document.save('sample.docx')

def create_multi_gene_table(MultiGenotype_a: MultiGenotype, MultiGenotype_b: MultiGenotype):
    document = Document()
    rows_cols_amount = len(MultiGenotype_a.genotypes) * len(MultiGenotype_b.genotypes)

    table = document.add_table(rows = (rows_cols_amount + 1), cols = (rows_cols_amount + 1))

    def set_cell(row, col, val):
        table.rows[row].cells[col].text = val



    multi_genotype_breeding_results = MultiGenotype_a.breed(MultiGenotype_b)
    element_counter = 0

    set_cell(0, 0, "♀ \ ♂")

    # fill left colum
    for i in range(rows_cols_amount):
        set_cell(i + 1, 0, multi_genotype_breeding_results[1 + i * rows_cols_amount][:2])

    # fill top row
    for i in range(rows_cols_amount):
        set_cell(0, i + 1, multi_genotype_breeding_results[i][2:])

    # fill table elements
    for rows in range(rows_cols_amount):
        for colums in range(rows_cols_amount):
            set_cell(rows + 1, colums + 1, multi_genotype_breeding_results[element_counter])
            element_counter += 1

    document.save('mgene_sample.docx')

