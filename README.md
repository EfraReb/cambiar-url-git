# Acerca de este script

Está pensado para automatizar el cambio de la url de origen de varios repositorios git.

Lo que hace este script es primero, dado un archivo excel, filtrar la data para obtener una lista de los repositorios que quieres cambiar la url de origen más su url que quieres cambiar en cada uno, luego busca en una ruta dada o en todo tu computadora cada repositorio que obtuvo en la lista filtrada, ingresa a la ruta del repositorio, primeramente se cambia a la rama master, después hace un pull y finalmente cambia la url de origen. 

# Instrucciones de Instalación y Uso

## Instalación de Paquetes

Para instalar los paquetes necesarios, ejecuta el siguiente comando:

```python
    pip3 install -r requirements.txt
```

## Uso del Script

### Argumentos:

- `-r` (string): Ruta. Ejemplos de valores: `/Users/myUser/Documents/`, `/Users/myUser/Descarga/`.
- `-c` (string): Current_dir. Valores permitidos: `n`, `y`.
- `-e` (string): Equipo. Nombre del equipo al que perteneces (Importante: Si el nombre de tu equipo es compuesto, debes escribirlo con somillas simples, ejemplo: 'Mi Equipo')

### Opciones de Ejecución:

#### Opción 1: Búsqueda en una Ruta Específica

Si deseas buscar los repositorios en una rut determinada, ejecuta:

```python
    python3 main.py -r [Ruta] -c n -e 'Mi equipo'
```

Por ejemplo, para buscar en "Documents":

```python
    python3 main.py -r /Users/myUser/Documents/ -c n -e 'Mi equipo'
```

Alternativamente, puedes omitir `-c`:

```python
    python3 main.py -r /Users/myUser/Documents/ -e 'Mi equipo'
```

#### Opción 2: Búsqueda en el Directorio Actual

Para buscar en el directorio actual donde vas a ejecutar tu script, utiliza:

```python
    python3 main.py -c y -e 'Mi equipo'
```

#### Opción 3: Búsqueda en el Directorio de Usuario Local

Para buscar en el directorio de tu usuario en tu sistema local, simplemente ejecuta:

```python
    python3 main.py -e 'Mi equipo'
```
Salida de éxito:
![Ejemplo de éxito](/images/ejemplo-cambio-url.png)
