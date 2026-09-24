"""
Programa: Registro de Frutas sin Repetir
Descripción: Programa que utiliza un conjunto (set) para almacenar 
             frutas asegurando que no existan duplicados.
"""

def mostrar_menu():
    print("\n--- MENU DE GESTION DE FRUTAS ---")
    print("1. Agregar fruta")
    print("2. Mostrar todas las frutas")
    print("3. Buscar fruta")
    print("4. Eliminar fruta")
    print("5. Salir")

def programa_frutas():
    # Estructura principal: Conjunto (set) para evitar elementos duplicados
    frutas = set()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion (1-5): ").strip()

        if opcion == "1":
            # OPERACION: Insertar / Agregar datos
            nueva_fruta = input("Ingrese el nombre de la fruta: ").strip().capitalize()
            
            if nueva_fruta in frutas:
                print(f"Aviso: La fruta '{nueva_fruta}' ya esta en el conjunto (no se pueden repetir).")
            else:
                frutas.add(nueva_fruta)
                print(f"'{nueva_fruta}' agregada exitosamente.")

        elif opcion == "2":
            # OPERACION: Mostrar de forma clara la informacion
            if not frutas:
                print("El conjunto de frutas esta vacio.")
            else:
                print(f"\n--- FRUTAS REGISTRADAS (Total: {len(frutas)}) ---")
                # Recorremos el conjunto
                for idx, fruta in enumerate(frutas, 1):
                    print(f"{idx}. {fruta}")

        elif opcion == "3":
            # OPERACION ADICIONAL: Buscar elemento
            fruta_buscar = input("Ingrese la fruta a buscar: ").strip().capitalize()
            if fruta_buscar in frutas:
                print(f"Resultado: La fruta '{fruta_buscar}' SI se encuentra registrada.")
            else:
                print(f"Resultado: La fruta '{fruta_buscar}' NO esta en el conjunto.")

        elif opcion == "4":
            # OPERACION ADICIONAL: Eliminar elemento
            fruta_eliminar = input("Ingrese la fruta a eliminar: ").strip().capitalize()
            if fruta_eliminar in frutas:
                frutas.remove(fruta_eliminar)
                print(f"'{fruta_eliminar}' fue eliminada correctamente.")
            else:
                print(f"Error: La fruta '{fruta_eliminar}' no se encontro en el conjunto.")

        elif opcion == "5":
            print("Gracias por usar el programa.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")

if __name__ == "__main__":
    programa_frutas()