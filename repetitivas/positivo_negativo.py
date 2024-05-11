#Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos 

positivos = 0
negativos = 0
neutros = 0
for i in range(20):
  numero= int(input("ingrese un numero:"))
  if numero > 0:
      positivos += 1
  elif numero < 0:
      negativos += 1
  else:
      neutros += 1
      
print("cantidad de numeros positivos:", positivos)
print("cantidad de numeros negativos:", negativos)
print("cantidad de numeros neutros:", neutros)