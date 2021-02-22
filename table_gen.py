#!/usr/bin/env python3

from docx import Document
from gene import Genotype, GeneAllele, breed, MultiGenotype


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

    table = document.add_table(rows = (len(MultiGenotype_a.genotypes) + 1), cols = (len(MultiGenotype_b.genotypes) + 1))

    def set_cell(row, col, val):
        table.rows[row].cells[col].text = val

    set_cell(0, 0, "♀ \ ♂")

    for i in range(len(MultiGenotype_a.genotypes)):
        set_cell(i + 1, 0, MultiGenotype_a.genotypes[i])
    for i in range(len(MultiGenotype_b.genotypes)):
        set_cell(0, i + 1, MultiGenotype_b.genotypes[i])

    multi_genotype_breeding_results = [MultiGenotype_a.breed(MultiGenotype_b)]
    element_counter = 0

    for rows in range(len(MultiGenotype_a.genotypes)):
        for colums in range(len(MultiGenotype_b.genotypes)):
            set_cell(rows + 1, colums + 1, multi_genotype_breeding_results[element_counter])
            element_counter += 1

    document.save('mgene_sample.docx')

