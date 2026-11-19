def buscar_libro(biblioteca):
    pedido = input().lower()
    for libro in biblioteca:
        if pedido in libro.titulo.lower() or pedido in libro.autor.lower():
            print(libro)