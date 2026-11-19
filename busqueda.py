def buscar_libro(biblioteca):
    print("Introduce el titulo o el autor del cual buscar los libros")
    pedido = input().lower()
    for libro in biblioteca:
        if pedido in libro.titulo.lower() or pedido in libro.autor.lower():
            print(libro)