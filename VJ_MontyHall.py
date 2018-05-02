import numpy as np
from random import shuffle


# funcion que desordena aleatoriamente los elemtos de la lista declarada.

def sort_doors():

	lista = ['goat','goat','car']

	shuffle(lista)

	return lista

print sort_doors()

# funcion que elige un numero aleatorio de la lista 
# indica la poscion elegida

def choose_door():

	lista=np.random.choice(3,1)
	
	return lista


print choose_door()

# Esta funcion retorna una lista cambiando el valor de goat por GOAT_MONTY siempre i cuando la posicion sea diferente de choice 

def reveal_door(lista, choice):

	for i in range(len(lista)):

		if ( i !=choice and lista[i]== 'goat'):

			lista[i]= "GOAT_MONTY"
			return lista

a=reveal_door(sort_doors(), choose_door())
print a 

# esta funcion termina el juego, depende de si el jugador decide moverse o no 
# retorna el valor de la posicion que sea diferente a GOAT_MONTY y a choice 
# entra como parametro la lista que arroja la funcion anterior, un numero choice y un booleano True o False

def finish_game (lista, choice, change):

	if (change== False):
		return lista[choice]

	else:

		for i in range(len(lista)):

			if ( lista[i] != "GOAT_MONTY" and i!= choice):

				return lista[i]
			
print finish_game (a, choose_door(), False)


#  Cada vez que se simule el juego, se  debe  guardar  el  valor  del  resultado  en  una  lista, para 100 repeticiones

true=[]
false=[]

for i in range(100):

	l= sort_doors()
	n= choose_door()
	k= reveal_door(l, n)
	a= finish_game (k,n,False)
	false.append(a)

for i in range(100):

	l2= sort_doors()
	n2= choose_door()
	k2= reveal_door(l2, n2)
	a2= finish_game (k2,n2,True)
	true.append(a2)

print true


cont=0;
for i in range(len(true)):

	if (true[i]=="car"):

		cont += 1

cont1=0;
for i in range(len(false)):

	if (false[i]=="car"):

		cont1 += 1	
	
print "La posibilidad de ganar con cambio de puerta es de", cont, "/100. La probabilidad de ganar sin cambio de puerta es de", cont1, "/100."

	

	

