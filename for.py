
#Quiz
#Usando un for y una lista con los promedios, calcule su nota definitiva a la fecha

lista_nota=[5.0,5.0,4.5,4.5,0,3.0]
lista_porcentajes=[5,10,20,6,3,3]

promedio=0

for i in range(len(lista_nota)):
    promedio += lista_nota[i]*lista_porcentajes[i]

print(promedio)

