import os
import pandas as pd

def get_data_excel():
    data = []
    path_excel = 'repos.xlsx'
    try:
        data = pd.read_excel(path_excel, sheet_name='Hoja1', usecols=['nombre-repo', 'url-actual', 'set-url', 'equipo'])
    except Exception as error:
        print(f"No se pudo leer el excel: {error}")
    return data

def filter_data(array_excel, equipo):
    array_repos = []
    array_urls = []
    data_excel_filtrada = []
    for idx in range(len(array_excel[0])):
        if equipo != '' and array_excel[3][idx].lower() == equipo.lower():
            repo = array_excel[0][idx]
            set_url = array_excel[2][idx]
            if repo not in array_repos:
                array_repos.append(repo)
            if set_url not in array_urls:
                array_urls.append(set_url)
        if equipo == '':
            repo = array_excel[0][idx]
            set_url = array_excel[2][idx]
            if repo not in array_repos:
                array_repos.append(repo)
            if set_url not in array_urls:
                array_urls.append(set_url)

    data_excel_filtrada.append(array_repos)
    data_excel_filtrada.append(array_urls)
            
    return data_excel_filtrada

def buscar_repo(repo, dir_base):
    dir_repo = ''
    for root, folders, files in os.walk(dir_base):
        for folder in folders:
            if folder == repo:
                dir_repo = os.path.join(root, folder)
                break
    return dir_repo