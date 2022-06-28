auto1 = float(input("Ingresar la velocidad en M/S del auto 1:"))
auto2 = float(input("Ingresar la velocidad en M/S del auto 2:"))
distanciaI = float(input("Ingrese la distancia inicial en metros: "))

if auto1>0 and auto2 >0:
    suma = auto1 + auto2 
    tiempo = distanciaI/suma
    print("Tiempo de encuentro entre los vehiculos:" + str(tiempo) + " segundo") 
else: 
    print("Error")
