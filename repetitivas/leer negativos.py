#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos numeros
suma_positivos = 0 
for i in range(10):
    numero = int(input("ingrese un numero negativo."))
    if numero < 0:
      numero *= -1
      suma_positivos += numero
print("la suma de los numeros enteros positivos es:", suma_positivos)
  