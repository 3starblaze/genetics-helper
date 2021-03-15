#!/usr/bin/env python3

import PySimpleGUI as sg
from pathlib import Path
from table_gen import Document
from gene_convenience import create_genotype as G

sg.theme('Dark')
layout = [
    [sg.Text('Genotype A'), sg.InputText(key='genotype_a')],
    [sg.Text('Genotype B'), sg.InputText(key='genotype_b')],
    [sg.Text('Save location:'), sg.Input(), sg.FolderBrowse(key='save_folder')],
    [sg.Submit()],
]

window = sg.Window('Genotype maker', layout)

d = Document()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        try:
            genotype_a = G(values['genotype_a'])
            genotype_b = G(values['genotype_b'])
            d.create_table(genotype_a, genotype_b)

            if not values['save_folder'] or values['save_folder'] == ' ':
                raise ValueError('Save location must be specified!')

            full_filename = Path(values['save_folder']) / 'genetics-helper.docx'
            d.save(Path(values['save_folder']) / 'genetics-helper.docx')
            sg.popup(f'File has been saved in { full_filename }', title='Success!')
        except Exception as e:
            sg.popup_error(e)

window.close()
