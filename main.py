import sh
import sys, os
from getopt import getopt
import utils_shared as utils

ruta = ''
current_dir = ''
equipo = ''
opts, args = getopt(sys.argv[1:],'r:c:e:',['ruta=', 'current_dir=', 'equipo='])

for option, argument in opts:
    if option == '-r':
        ruta = argument
    if option == '-c':
        current_dir = argument
        if current_dir != 'n' and current_dir != 'y':
            raise ValueError('El argumento debe ser y o n')
    if option == '-e':
        equipo = argument

if equipo == '':
    input_user = input('Si no ingresas un equipo, se buscarán todos los repositorios del excel en tu local\n ¿estás seguro que quieres continuar sin ingresar un equipo?\n\n 1)Sí\n 2)No\n\n Ingresa 1 ó 2: ')
    if input_user == '2':
        equipo = input("Por favor ingresa el nombre de tu equipo: ")

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

dir_base = '/' + CURR_DIR.split('/')[1] + '/'

if ruta != '' and (current_dir.lower() == '' or current_dir.lower() == 'n'):
    dir_base = ruta
if ruta == '' and current_dir.lower() == 'y':
    dir_base = CURR_DIR

if equipo  != '':
    print(f"Se buscarán repos del equipo: {equipo}")

print(f"Ruta base donde se buscarán los repos: {dir_base}")

data_repos = utils.get_data_excel().to_numpy().transpose().tolist()

data_filtrada = utils.filter_data(data_repos, equipo)

col_repo = data_filtrada[0]
col_set_url = data_filtrada[1]

for idx in range(len(col_repo)):
    print(f"Buscando el repo {col_repo[idx]}")
    remote_url = ''
    dir_repo = utils.buscar_repo(col_repo[idx], dir_base)
    if dir_repo != '':
        os.chdir(dir_repo)
        sh_cmd = sh.Command('git')
        remote_url = sh_cmd('remote', '-v')
        branchs = sh_cmd('branch')
        print(f"Url actual del repo\n {remote_url}")
        if col_set_url[idx] not in remote_url:
            print(f"Cambiando url al repo {col_repo[idx]}")
            try:
                if 'master' in branchs:
                    sh_cmd('checkout', 'master')
                if 'main' in branchs:
                    sh_cmd('checkout', 'main')
                sh_cmd('pull')
                sh_cmd('remote', 'set-url', 'origin', col_set_url[idx])
                remote_url = sh_cmd('remote', '-v')
                if col_set_url[idx] in remote_url:
                    print(f"Cambio exitoso de url en el repo: {col_repo[idx]}!!!!")
            except Exception as e:
                print(f"Ha ocurrido un error al intentar cambiar la url del repo {col_repo[idx]}: {e}")
        elif col_set_url[idx] in remote_url:
            print(f"La url origin ya es {col_set_url[idx]}")
    else:
        print(f"Repo {col_repo[idx]} no encontrado en tu local")