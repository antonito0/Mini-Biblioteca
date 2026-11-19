# --- Aquí cada persona añade el import de su módulo ---
import busqueda

def mostrar_menu():
    print("\n=== MINI BIBLIOTECA ===")
    # --- Aquí cada persona añade su opción del menú ---
    print("0. Salir")
   

def añadir_libro(biblioteca):
    titulo = input("Indique el título: ")
    autor = input("Indique el autor: ")
    isbn = input("Indique el ISBN: ")
    libro = {"titulo": titulo,"autor": autor,"isbn": isbn}
    biblioteca.append(libro)
    print("el libro", titulo, "añadido correctamente")

def listar_libros(biblioteca):
    for libro in biblioteca:
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("ISBN:", libro["isbn"])
        print("--------------------")
    
def main():
    biblioteca = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "0":
            print("¡Hasta pronto!")
            break
        elif opcion == "3":
            busqueda.buscar_libro
        # --- Aquí cada persona añade su elif ---
        else:
            print("Opción no válida")
    
if __name__ == "__main__":
    main()