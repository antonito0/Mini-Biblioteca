import json
import os
from libros import libro

ARCHIVO = 'libros.txt'


def guardar_libros(biblioteca):
    datos = [{'titulo': l.titulo, 'autor': l.autor, 'isbn': l.isbn} for l in biblioteca]
    with open(ARCHIVO, 'w', encoding='utf-8') as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


def cargar_libros():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            return [libro(d['titulo'], d['autor'], d['isbn']) for d in json.load(f)]
    return []
