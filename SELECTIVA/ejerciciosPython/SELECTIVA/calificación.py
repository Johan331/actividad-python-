calificacion_1 = int(input("ingrese la calificacion del estudiante 1:"))
calificacion_2 = int(input("ingrese la calificacion del estudiante 2:"))
calificacion_3 = int(input("ingrese la calificacion del estudiante 3:"))
calificacion_4 = int(input("ingrese la calificacion del estudiante 4:"))
calificacion_5 = int(input("ingrese la calificacion del estudiante 5:"))
calificacion_6 = int(input("ingrese la calificacion del estudiante 6:"))
calificacion_7 = int(input("ingrese la calificacion del estudiante 7:"))
calificacion_8 = int(input("ingrese la calificacion del estudiante 8:"))
calificacion_9 = int(input("ingrese la calificacion del estudiante 9:"))
calificacion_10 = int(input("ingrese la calificacion del estudiante 10:"))

menor_50=0
entre_50_y_70=0
entre_70_y_80=0
mayor_80=0

if calificacion_1>=1 and calificacion_1<=49:
    menor_50 +=1
elif calificacion_1>=50 and calificacion_1<=69:
    entre_50_y_70 +=1
elif calificacion_1 >= 70 and calificacion_1 < 79:
    entre_70_y_80 += 1
elif calificacion_1>=80 and calificacion_1<=100:
    mayor_80 +=1

if calificacion_2>=1 and calificacion_2<=49:
    menor_50 +=1
elif calificacion_2>=50 and calificacion_2<=69:
    entre_50_y_70 +=1
elif calificacion_2 >= 70 and calificacion_2 < 79:
    entre_70_y_80 += 1
elif calificacion_2>=80 and calificacion_2<=100:
    mayor_80 +=1

if calificacion_3>=1 and calificacion_3<=49:
    menor_50 +=1
elif calificacion_3>=50 and calificacion_3<=69:
    entre_50_y_70 +=1
elif calificacion_3 >= 70 and calificacion_3 < 79:
    entre_70_y_80 += 1
elif calificacion_3>=80 and calificacion_3<=100:
    mayor_80 +=1

if calificacion_4>=1 and calificacion_4<=49:
    menor_50 +=1
elif calificacion_4>=50 and calificacion_4<=69:
    entre_50_y_70 +=1
elif calificacion_4 >= 70 and calificacion_4 < 79:
    entre_70_y_80 += 1
elif calificacion_4>=80 and calificacion_4<=100:
    mayor_80 +=1

if calificacion_5>=1 and calificacion_5<=49:
    menor_50 +=1
elif calificacion_5>=50 and calificacion_5<=69:
    entre_50_y_70 +=1
elif calificacion_5 >= 70 and calificacion_5 < 79:
    entre_70_y_80 += 1
elif calificacion_5>=80 and calificacion_5<=100:
    mayor_80 +=1

if calificacion_6>=1 and calificacion_6<=49:
    menor_50 +=1
elif calificacion_6>=50 and calificacion_6<=69:
    entre_50_y_70 +=1
elif calificacion_6 >= 70 and calificacion_6 < 79:
    entre_70_y_80 += 1
elif calificacion_6>=80 and calificacion_6<=100:
    mayor_80 +=1

if calificacion_7>=1 and calificacion_7<=49:
    menor_50 +=1
elif calificacion_7>=50 and calificacion_7<=69:
    entre_50_y_70 +=1
elif calificacion_7 >= 70 and calificacion_7 < 79:
    entre_70_y_80 += 1
elif calificacion_7>=80 and calificacion_7<=100:
    mayor_80 +=1

if calificacion_8>=1 and calificacion_8<=49:
    menor_50 +=1
elif calificacion_8>=50 and calificacion_8<=69:
    entre_50_y_70 +=1
elif calificacion_8 >= 70 and calificacion_8 < 79:
    entre_70_y_80 += 1
elif calificacion_8>=80 and calificacion_8<=100:
    mayor_80 +=1

if calificacion_9>=1 and calificacion_9<=49:
    menor_50 +=1
elif calificacion_9>=50 and calificacion_9<=69:
    entre_50_y_70 +=1
elif calificacion_9 >= 70 and calificacion_9 < 79:
    entre_70_y_80 += 1
elif calificacion_9>=80 and calificacion_9<=100:
    mayor_80 +=1

if calificacion_10>=1 and calificacion_10<=49:
    menor_50 +=1
elif calificacion_10>=50 and calificacion_10<=69:
    entre_50_y_70 +=1
elif calificacion_10 >= 70 and calificacion_10 < 79:
    entre_70_y_80 += 1
elif calificacion_10>=80 and calificacion_10<=100:
    mayor_80 +=1
    
print("la cantidad de estudiantes que obtuvieron calificacion menor a 50 es:", menor_50)
print("la cantidad de estudiantes que obtuvieron calificacion entre 50 y 69 es:", entre_50_y_70)
print("la cantidad de estudiantes que obtuvieron calificacion entre 70 y 79 es:", entre_70_y_80)
print("la cantidad de estudiantes que obtuvieron calificacion mayor a 80 es:", mayor_80)
