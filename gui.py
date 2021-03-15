#!/usr/bin/env python3

import PySimpleGUI as sg
from pathlib import Path

sg.theme('Dark')
layout = [
    [sg.Text('Genotype A'), sg.InputText(key='genotype_a')],
    [sg.Text('Genotype B'), sg.InputText(key='genotype_b')],
    [sg.Text('Save location:'), sg.Input(), sg.FolderBrowse(key='save_folder')],
    [sg.Submit()],
]

window = sg.Window('Genotype maker', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        if not values['save_folder'] or values['save_folder'] == ' ':
            sg.popup_error('Value must be specified!')
        else:
            try:
                save_location = Path(values['save_folder']) / 'foo'
                save_location.touch(exist_ok=False)
            except Exception as e:
                sg.popup_error(e)

window.close()
