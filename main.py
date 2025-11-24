import Operaciones

def menu():
    while(True):

        print("\nCALCULADORA EN PYTHON\n")
        print("MENÚ")
        print("1. SUMA")
        print("2. RESTA")
        print("3. MULTIPLICACIÓN")
        print("4. DIVISIÓN")
        print("5. SALIR\n")


        try:
         opcion = int(input("Ingresa una opción: "))
        except ValueError:
            print("Ingrese la opción correcta.")
            continue

        match(opcion):
            case 1:
                numA = float(input("Ingrese el primer número: "))
                numB = float(input("Ingrese el segundo número: "))
                resultado = Operaciones.suma(numA,numB)
                print(f"Resultado: {resultado} ")
                input("Presione ENTER para salir...")
            case 2:
                numA = float(input("Ingrese el primer número: "))
                numB = float(input("Ingrese el segundo número: "))
                resultado = Operaciones.resta(numA,numB)
                print(f"Resultado: {resultado} ")
                input("Presione ENTER para salir...")
                
            case 3:
                numA = float(input("Ingrese un número: "))
                numB = float(input("Ingrese el multiplicador: "))
                resultado = Operaciones.multiplicacion(numA,numB)
                print(f"Resultado: {resultado} ")
                input("Presione ENTER para salir...")
            case 4:
                numA = float(input("Ingrese el número dividendo: "))

                while(True):
                    numB = float(input("Ingrese el divisor: "))

                    try:
                     resultado = Operaciones.division(numA, numB)
                     print("Resultado:", resultado)
                     break  
                    except ValueError as e:
                        print("Error:", e)
                        print("Inténtelo nuevamente.\n")  

                input("Presione ENTER para continuar...")
            case 5:
                print("Saliendo de la calculadora...")
                break
            case _:
                print("Inserte una opción correcta.")


menu()
