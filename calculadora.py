print("===== CALCULADORA =====")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1-4): ")
s
numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))

if opcion == "1":
    print("Resultado:", numero1 + numero2)

elif opcion == "2":
    print("Resultado:", numero1 - numero2)

elif opcion == "3":
    print("Resultado:", numero1 * numero2)

elif opcion == "4":
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("Error: No se puede dividir entre cero.")

else:
    print("Opción no válida.")