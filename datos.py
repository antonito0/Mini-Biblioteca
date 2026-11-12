import ast
import os

ARCHIVO = 'libros.txt'


def guardar_libros(biblioteca):
    with open(ARCHIVO, 'w', encoding='utf-8') as f:
        f.write(str(biblioteca))

def cargar_libros():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            return ast.literal_eval(f.read())
    else:
        return []