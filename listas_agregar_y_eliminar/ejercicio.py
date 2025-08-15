# de acuerdo a la guia elabora un ejercicio donde solicites una lista de n numeros y 
# elabora un menu con la declaración match y aplica los metodos de listas para python, 
# por ejemplo ordenar la lista de numeros, eliminar un numero de la lista, 
# insertas mas numeros la lista, etc

lista = []

print("bienvenido a tu ordenador de numeros favoritos")


conte = int(input("ingresa tus numeros por ordenar: "))
print("\n")
for i in range(conte):
    numero = int(input(f"ingresa el {i+1} valor: "))
    lista.append(numero)

lista.sort()
print("\n")
print(lista)
while True:
    try:
     print("\nquieres remover  algun numero que colocaste o ingresar algun"
    "\nEscoge alguna opcion"
    "\n1.si"
    "\n2.ingresar"
    "\n3.no")
     remover =int(input())
     "\n"
     match remover:
        case 1:
            while True:
                quitar=int(input(f"cual deseas remover de la lista {lista}:"))
                if quitar in lista:
                    lista.remove(quitar)
                    print("Número removido.")
                    break
                else:
                    print("Ese número no está en la lista.")
                    print("Lista actual:", lista)
            # lista.remove(quitar)
            # print(lista)
        case 2:
            ingresar=int(input(f"cual deseas ingresar{lista}:"))
            lista.append(ingresar)
            lista.sort()
            print("numero ingresado")
            print(lista)
        case 3:
            print("Gracias por usar el ordenador. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Intenta de nuevo.")
    except ValueError:
        print("ingresa un valor numerico")
