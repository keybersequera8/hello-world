'''
sorts.py

Implementación de los algoritmos de ordenamiento para el curso CI2692, SD 2019

Autores: Alexis Infante 17-10284
		 Keyber Sequera 16-11120
'''

from copy import deepcopy

import random, time

# Insertion Sort---------------------------------------------------------------------------------------------------------

def InsertionSort(A):
	'''
	Parametros:
	-----------
		A: Arreglo. Elemento que sera ordenado

	Returns:
	--------
		Nada

	Efecto:
	-------
		Ordena los elementos del arreglo dado de manera creciente
	'''

	for j in range(1,len(A)):    # Creamos un ciclo que recorra el arreglo, comenzando desde el segundo elemento

		key = A[j]				 # Tomamos cada elemento del ciclo como un pivote
		i = j-1					 # Creamos una variable que contenga los elementos anteriores al pivote

		while i >= 0 and A[i]>key :  # Creamos un nuevo ciclo que compare los valores anteriores al pivote con este mismo

			A[i+1] = A[i]	     # Si el valor es mayor que el pivote lo movemos a la derecha
			i = i-1				 # Nos movemos a la izquierda y comparamos con el pivote hasta salirnos del arreglo

		A[i+1] = key			 # Una vez se comparan todos los elementos con el pivote se procede a ubicar al pivote
								 # en el lugar que le corresponde
	return

# Merge Sort--------------------------------------------------------------------------------------------------------------

# Para poder implementar MergeSort es necesario crear 2 procedimientos, Merge y MergeSort

# Creamos el procedimiento Merge

def Merge(A,p,q,r):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que sera ordenado
		p: Entero. Posicion inicial del bloque que se esta trabajando
		q: Entero. Mitad del bloque que se esta trabajando
		r: Entero. Posicion final del bloque que se esta trabajando
	Returns:
	--------
		Nada

	Efecto:
	-------
		Ordena en un solo arreglo, los elementos de dos arreglos ordenados ascendentemente, de manera ascendente
	'''

	infinito = float('inf')			# Creamos el valor infinito que sera usado como sentinela para ordenar los elementos
	N_1 = q-p+1						# Almacenamos en una variable el valor de la mitad izquierda del bloque a trabajar
	N_2 = r-q						# Almacenamos en una variable el valor de la mitad derecha del bloque a trabajar
	L = [0]*(N_1)					
	R = [0]*(N_2)					# Creamos dos variables L y R 

	for i in range(0,N_1):
		
		L[i] = A[p+i]				# Guardamos en la variable L los elementos de la parte izquierda del bloque a ordenar 

	for j in range(0,N_2):
		
		R[j] = A[j+q+1]				# Guardamos en la variable R los elementos de la parte derecha del bloque a ordenar

	L = L + [infinito]				# Agregamos sentinelas en L y R, que haran que una vez alcanzada la posicion final en alguno
	R = R + [infinito]				# de los arreglos L o R, el arreglo sea llenado con los elementos restantes del otro
	i, j = 0, 0

	for k in range(p,r+1):
		
		if L[i]<=R[j]:				# Si el elemento de L es menor que el que esta en R
			
			A[k] = L[i]				# Se añade en el bloque a ordenar el elemento de L
			i = i+1					# Se analiza el proximo elemento de L con el elemento de R
		
		else:						# Si el elemento de R es menor que el que esta en L 
			
			A[k] = R[j]				# Se añade en el bloque a ordenar el elemento de R
			j = j+1					# Se analiza el proximo elemento de R con el elemento de L

	return

# Se crea el procedimiento MergeSort

def MergeSort(A,p,r):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que sera ordenado
		p: Entero. Posicion inicial del bloque que se esta trabajando
		r: Entero. Posicion final del bloque que se esta trabajando
	Returns:
	--------
		Nada

	Efecto:
	-------
		Ordena el arreglo de manera ascendente
	'''
	if r>p:
		
		q = (p+r)//2				# Calculamos la mitad del arreglo a ordenar
		MergeSort(A,p,q)			# Aplicamos MergeSort a la parte izquierda del arreglo, hasta tener solo arreglos de un elemento
		MergeSort(A,q+1,r)			# Aplicamos MergeSort a la parte izquierda del arreglo, hasta tener solo arreglos de un elemento
		Merge(A,p,q,r)				# Aplicamos Merge a cada bloque hasta ordenar el arreglo original

	return

# Heap Sort ------------------------------------------------------------------------------------------------------------------

# Para hacer uso del algoritmo de ordenamiento Heap Sort es necesario crear varias funciones con anterioridad

# Primero definimos que valores representaran las ramas izquierdas de nuestro arbol binario

def Left(i):
	'''
	Parametros:
	----------
		i: Entero. Valor del nodo padre
	Returns:
	--------
		2*i: Entero. Valor de la rama izquierda de nuestro nodo padre
	Efecto:
	-------
		Clasifica a los numeros pares, como la ramas izquierdas de nuestro arbol binario
	'''

	return 2*i

# Tambien debemos definir que valores representaran las ramas derechas de nuestro arbol binario

def Right(i):
	'''
	Parametros:
	----------
		i: Entero. Valor del nodo padre
	Returns:
	--------
		(2*i)+1: Entero. Valor de la rama derecha de nuestro nodo padre
	Efecto:
	-------
		Clasifica a los numeros impares, como las ramas derechas de nuestro arbol binario
	'''
	
	return (2*i)+1

# Luego creamos una funcion que compare el valor del nodo padre con su dos ramas hijas

def MaxHeapify(A,i,n):
	'''
	Parametros:
	----------
		A: Arreglo. Arreglo que queremos ordenar
		i: Entero. Valor del nodo padre
		n: Entero. Cantidad de nodos que hay en A
	Returns:
	--------
		Nada
	Efecto:
	-------
		Compara al nodo padre con sus nodos hijos y si alguno de estos es mayor, cambia la posicion del nodo padre
		con el nodo hijo respectivo y repite el proceso hasta que el arreglo este ordenado decrecientemente.
	'''

	l = Left(i)									# Se almacena la rama izquierda en la variable l
	r = Right(i)								# Se almacena la rama derecha en la variable r
	largest = 0									# Se declara la variable que almacenara al valor mas grande
	
	if l < n and A[l] > A[i]:					# Siempre que l sea un nodo dentro del arreglo y se cumpla que A[l]>A[i]
		largest = l 							# El numero valor mas grande sera el que esta en l
	
	else:										
		largest = i 							# De lo contrario, el mas grande sera el nodo padre i

	if r < n and A[r] >= A[largest]: 			# Verificamos si el lado derecho contiene al elemento mas grande
		largest = r 							# En caso de contenerlo, el elemento mas grande sera el que esta en r

	if largest != i:
		
		(A[i],A[largest]) = (A[largest], A[i]) 	# Si el elemento mas grande no esta en i, intercambiamos las posiciones de i
												# con la del elemento mas grande
		MaxHeapify(A,largest,n)					# Vemos si el anterior nodo padre, es el nodo padre de las ramas de abajo

	return

# Creamos una funcion que ordene todo el arreglo de manera decreciente

def BuildMaxHeap(A):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que queremos ordenar
	Returns:
	--------
		Nada
	Efecto:
	-------
		Ordena el arreglo A de manera decreciente
	'''

	A_heapsize = len(A)						# La cantidad de nodos que tiene el arbol binario es igual a la longitud del arreglo A

	for i in range(len(A)//2, -1, -1):		# Ordenamos los elementos decrecientemente

		MaxHeapify(A,i,A_heapsize)			# Verificamos que los nodos esten ordenados decrecientemente usando MaxHeapify 

	return

# Finalmente, definimos Heap Sort.

def HeapSort(A):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que queremos ordenar
	Returns:
	--------
		Nada
	Efecto:
	--------
		Ordena el arreglo de manera creciente
	'''

	A_heapsize = len(A)					# La cantidad de nodos del arreglo binario es igual al tamaño del arreglo A
	BuildMaxHeap(A)						# Ordenamos el arreglo de manera decreciente

	for i in range(len(A)-1, 0, -1):	# Recorremos el arreglo desde el ultimo termino hasta el segundo elemento de A 
		
		(A[0],A[i]) = (A[i],A[0])		# Cambiamos los valores finales con el primero, de manera que el mas pequeño siempre quede
										# de primero y los demas en la posicion que les corresponde
		A_heapsize = A_heapsize-1		# Se reduce la cantidad de nodos, con el fin de no volver a considerar al termino mas grande
		MaxHeapify(A,0,A_heapsize) 		# Se ordena el arreglo decrecientemente, para seguir ordenando

	return 

# Quick Sort -------------------------------------------------------------------------------------------------------------------

# Primero determinamos cual sera el pivote que consideraremos

def Partition(A,p,r):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que se quiere ordenar
		p: Entero. Elemento inicial del arreglo A
		r: Entero. Elemento final del arreglo A
	Returns:
	--------
		i+1: Entero. Localizacion del pivote
	Efecto:
	-------
		Este procedimiento selecciona un pivote y de acuerdo a este modifica el arreglo A. Compara los elementos del
		arreglo con el pivote y ubica a este mismo en la posicion que le corresponde en el arreglo A, ademas, ubica
		del lado izquierdo, los elementos menores que el pivote y del lado derecho los mayores. 
	'''

	x = A[r-1]						# Tomamos como pivote el ultimo valor del arreglo
	i = p-1							# Declaramos la variable i que nos ayudara a ubicar a el pivote en la posicion adecuada

	for j in range(p,r-1):			# Recorremos el arreglo desde el valor inicial p, hasta un elemento anterior al pivote

		if A[j]<=x:					# Si el pivote es mayor o igual al valor de la posicion que se esta considerando

			i = i+1					# Aumentamos en 1 la variable que nos ayudara a ubicar la posicion del pivote
			A[i],A[j] = A[j],A[i]	# Cambiamos las posiciones de A[i] con A[j], con el fin de ubicar del lado izquierdo los
									# elementos menores que el pivote y del derecho los mayores 

	A[i+1],A[r-1] = A[r-1],A[i+1]	# Ubicamos al pivote despues del ultimo elemento menor a este

	return i+1						# Devolvemos la localizacion del pivote

# Definimos el procedimiento Quick Sort:

def QuickSort(A,p,r):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que se ordernara
		p: Entero. Valor inicial del arreglo A
		r: Entero. Valor final del arreglo A
	Returns:
	--------
		Nada
	Efecto:
	-------
		Ordena el arreglo A de forma creciente
	'''

	if p<r:						

		q = Partition(A,p,r)	# Seleccionamos el pivote usando la funcion Partition
		QuickSort(A,p,q)		# Aplicamos Quick Sort a la parte izquierda del pivote, sin tocar al pivote
		QuickSort(A,q+1,r)		# Aplicamos Quick Sort a la parte derecha del pivote, sin tocar al pivote

	return

# Randomized Quick Sort ------------------------------------------------------------------------------------------

# Primero determinamos cual sera el pivote que consideraremos

def Partition(A,p,r):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que se quiere ordenar
		p: Entero. Elemento inicial del arreglo A
		r: Entero. Elemento final del arreglo A
	Returns:
	--------
		i+1: Entero. Localizacion del pivote
	Efecto:
	-------
		Este procedimiento selecciona un pivote y de acuerdo a este modifica el arreglo A. Compara los elementos del
		arreglo con el pivote y ubica a este mismo en la posicion que le corresponde en el arreglo A, ademas, ubica
		del lado izquierdo, los elementos menores que el pivote y del lado derecho los mayores. 
	'''

	x = A[r-1]						# Tomamos como pivote el ultimo valor del arreglo
	i = p-1							# Declaramos la variable i que nos ayudara a ubicar a el pivote en la posicion adecuada

	for j in range(p,r-1):			# Recorremos el arreglo desde el valor inicial p, hasta un elemento anterior al pivote

		if A[j] <= x:				# Si el pivote es mayor o igual al valor de la posicion que se esta considerando

			i = i+1					# Aumentamos en 1 la variable que nos ayudara a ubicar la posicion del pivote
			A[j],A[i] = A[i],A[j]	# Cambiamos las posiciones de A[i] con A[j], con el fin de ubicar del lado izquierdo los
									# elementos menores que el pivote y del derecho los mayores

	A[i+1],A[r-1] = A[r-1],A[i+1]	# Ubicamos al pivote despues del ultimo elemento menor a este

	return i+1						# Devolvemos la localizacion del pivote

# Definimos la funcion Randomized Partition, la cual ubicara a un valor aleatorio del arreglo en la posicion final

def RandomPartition(A,p,r):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que se quiere ordenar
		p: Entero. Valor inicial que se esta considerando
		r: Etero. Valor final que se esta considerando
	Returns:
	--------
		Partition(A,p,r): Entero. Retorma el valor del pivote
	Efecto:
	-------
		Selecciona un pivote aleatorio, con el fin de hacer menos probable que ocurra el peor caso de Quick Sort
	'''
	
	i = random.randint(p,r)				# Almacenamos alguna de las posiciones en una variable
	
	if i != r:						
		
		A[i],A[r-1] = A[r-1],A[i]		# Cambiamos el valor final por el elemento ubicado en la posicion elegida al azar

	return Partition(A,p,r)				# Aplicamos la funcion partition para ubicar al pivote en la posicion que le,
										# corresponde y a los numeros menores a el a la izquierda y a los mayores a la derecha

# Definimos el procedimiento Quick Sort:

def RandomQuickSort(A,p,r):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que se ordernara
		p: Entero. Valor inicial del arreglo A
		r: Entero. Valor final del arreglo A
	Returns:
	--------
		Nada
	Efecto:
	-------
		Ordena el arreglo A de forma creciente
	'''

	if p<r:						

		q = RandomPartition(A,p,r)		# Seleccionamos el pivote usando la funcion RandomizedPartition
		RandomQuickSort(A,p,q)			# Aplicamos Randomized Quick Sort a la parte izquierda del pivote, sin tocar al pivote
		RandomQuickSort(A,q+1,r)		# Aplicamos Randomized Quick Sort a la parte derecha del pivote, sin tocar al pivote

	return 

# Counting Sort --------------------------------------------------------------------------------------------------------------

def CountingSort(A,B,k):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que se quiere ordenar
		B: Arreglo. Arreglo auxiliar en donde se alamacenara el arreglo A ordenado
		k: Entero. Valor maximo del arreglo A
	Returns:
	--------
		Nada
	Efecto:
	-------
		Ordena el arreglo A en el arreglo B
	'''

	C = [0]*(k+1)					# Creamos un arreglo C que sea de longitud igual al valor maximo de A

	for j in range(0,len(A)):		

		C[A[j]] = C[A[j]]+1			# El arreglo C almacenara la cantidad que hay de cada elemento de A

	for i in range(1,k+1):

		C[i] = C[i] + C[i-1]		# Sumamos el valor de la cuenta de cada elemento con la del anterior, obteniendo un valor
									# por debajo de la longitud de A 

	for j in range(len(A)-1,-1,-1):

		B[(C[A[j]]-1)] = A[j]		# Ordenamos de manera creciente los elementos en B, haciendo uso de los arreglos A y C
		C[A[j]] = C[A[j]] - 1		# Restamos 1 a la casilla anterior del valor de C que se uso para ordenar el elemento en B

	return B

# Radix Sort -----------------------------------------------------------------------------------------------------------------

def RadixSort(A,d):
	'''
	Parametros:
	-----------
		A: Arreglo. Elemento que se quiere ordenar
		d: Entero. Cantidad de digitos que tiene el valor mas grande de A
	Returns:
	--------
		A: Arreglo. Arreglo A ordenado
	Efecto:
	-------
		Ordena el arreglo de manera creciente haciendo uso de un nuevo arreglo auxiliar
	'''

	division = 1            # Almacenamos un multiplo de 10 en esta variable, la cual usaremos para desplazarnos 
							# entre cada digito de los elementos del arreglo
	modulo = 10				# Usamos esta variable para considerar al primer digito del elemento, luego los
							# dos primeros digitos de cada elemento... hasta llegar a los primeros d digitos de cada elemento

	while d>0:

		B = [ [], [], [], [], [], [], [], [], [], [] ]	# Creamos un valor auxiliar B que contendra 10 arreglos vacios, cada
														# casilla almacenara cada uno de los elementos cuyo digito sea igual a la 
														# posicion de la casilla
		
		for numeros in A:	# Recorremos cada elemento de A								

			posicion = (numeros % modulo)//division		# la posicion del elemento de A en B, sera dada por el valor del digito
														# que se esta estudiando 
			B[posicion] = B[posicion] + [numeros]		# Guardamos el numero en la posicion obtenida

		A = []									# Hacemos el arreglo A vacio para poder concatenarlo con los elementos de B
		
		for arreglos in B:						# Recorremos los elementos de B

			for elementos in arreglos:			# Recorremos cada elemento de los arreglos de B

				A = A + [elementos]				# Concatenamos cada elemento en los arreglos de B con A

		modulo = modulo * 10	# Aumentamos esta variable para considerar 1 digito mas hasta llegar a considerar los d digitos

		division = division * 10 # Aumentamos la variable division con el fin de poder aislar los digitos  

		d = d-1     # Restamos el digito considerado con el fin de salir del ciclo inicial 

	return A