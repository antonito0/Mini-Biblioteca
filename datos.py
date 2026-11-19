def guardar_libros(biblioteca):
    with open("libros.txt", "w", encoding="utf-8") as f:
        for bib in biblioteca:
            for clave, valor in biblioteca.items():
                biblioteca_en_texto = ";".join(str(n) for n in notas)
                f.write(f"{nombre};{notas_en_texto}\n")