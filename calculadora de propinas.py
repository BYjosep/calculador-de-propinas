#inputs
importe = int(input("¿Cuál es la factura total de hoy, por favor? "))
porcentaje_propina = int(input("indique el porcentaje de la propina "))
#calculos
propina= (importe * porcentaje_propina)/100
importe_t= propina+importe
#prints
print("su importe es de ")
print (importe)
print ("su importe de la propina es de ")
print (propina)
print ("su importe mas la propina es de ")
print (importe_t)