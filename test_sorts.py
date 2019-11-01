'''
test_sorts.py

Programa que contiene la prueba de todos los algoritmos de ordenamiento, con el calculo del tiempo promedio
de ejecucion de cada uno, junto con la desviacion estandar.

Estudiantes: Alexis Infante 17-10284 
			 Keyber Sequera 16-11120
'''

import random, time, math, sys, sorts

from copy import deepcopy

numero_de_pruebas = int(format(sys.argv[1]))

numero_de_elementos = int(format(sys.argv[2]))

# Definimos la funcion Arreglo que devolvera un arreglo con elementos random.

def Arreglo(A):
	'''
	Parametros:
	-----------
		A: Arreglo. Arreglo que se llenara con elementos random
	Returns:
	--------
		A: Arreglo. Arreglo A con elementos random
	Efecto:
	-------
		Toma un arreglo cualquiera y cada una de sus componentes las cambia por numeros enteros random
	'''
	
	for i in range(0,len(A)):							# Recorremos cada elemento del arreglo a modificar
		numero = random.randint(0,numero_de_elementos)  # Guardamos un numero random en la variable numero 
		A[i] = numero 									# Asignamos el numero random a la posicion en la que se este 											
	
	return A

def T_promedio(tiempos):
	'''
	Parametros:
	-----------
		tiempos: Arreglo. Arreglo que contiene los tiempos de ejecucion del algoritmo que se este implementando
	Returns:
	--------
		media: Float. Valor del tiempo promedio
	Efecto:
	-------
		Calcula el tiempo promedio de un arreglo con n tiempos.
	'''

	suma_tiempos = 0

	for i in range(0,len(tiempos)):

 		suma_tiempos = suma_tiempos+tiempos[i]		# Sumamos cada uno de los tiempos y los guardamos en la variable suma_tiempos

	media = (suma_tiempos)/len(tiempos)				# Calculamos la media, haciendo uso de la suma de los tiempos dividida entre
													# n ( que son los tiempos considerados)

	return media

def D_estandar(tiempos,media):
	'''
	Parametros:
	-----------
		tiempos: Arreglo. Arreglo que contiene los tiempos de ejecucion del algoritmo que se desea analizar
		media: Float. Valor que tiene el valor promedio de los tiempos
	Returns:
	--------
		d_estandar: Float. Desviacion estandar de los tiempos.
	Efecto:
	-------
		Calcula la desviacion estandar de un grupo de tiempos
	'''

	varianza = 0 

	for j in range(0,len(tiempos)):

		varianza = varianza+(tiempos[j]-media)**2    # Calculamos la varianza la cual es necesaria para calcular la 
													 # desviacion estandar        

	varianza = varianza/(len(tiempos)-1)
	d_estandar = math.sqrt(varianza)				# Calculamos la desviacion estandar que sera igual a la raiz cuadrada de la varianza

	return d_estandar

def Calculo_Promedio_y_Desviacion_Estandar(tiempos):
	'''
	Parametros:
	-----------
		tiempos: Arreglo. Arreglo que contiene los tiempos del algoritmo que se quiere analizar
	Returns:
	--------
		T_prom: Float. Valor del tiempo promedio
		des_estandar: Float. Valor de la desviacion estandar de los tiempos dados
	Efecto:
	-------
		Calculamos el vaor del tiempo promedio y de la desviacion estandar de los tiempos dados
	'''

	T_prom = T_promedio(tiempos)
	des_estandar = D_estandar(tiempos,T_prom)

	return T_prom, des_estandar

# Calculo de tiempo promedio y desviacion estandar de Insertion Sort-------------------------------------

tiempos_insertion_sort = [0]*(numero_de_pruebas)
tiempos_merge_sort = [0]*(numero_de_pruebas)
tiempos_heap_sort = [0]*(numero_de_pruebas)
tiempos_quick_sort = [0]*(numero_de_pruebas)			# Guardamos los datos de los tiempos en distintos arreglos
tiempos_random_quick_sort = [0]*(numero_de_pruebas)
tiempos_counting_sort = [0]*(numero_de_pruebas)
tiempos_radix_sort = [0]*(numero_de_pruebas)

for i in range(0,numero_de_pruebas):	

	A = [0]*numero_de_elementos 						# Creamos un arreglo random
	A = Arreglo(A)			
	B = deepcopy(A)					
	C = deepcopy(A)
	D = deepcopy(A)
	E = deepcopy(A)		# Guardamos el arreglo aleatorio A en varias variables con el fin de probar los distintos algoritmos
	F = deepcopy(A)		# de ordenamiento con el mismo algoritmo, y asi poder apreciar cual es mas eficiente
	G = deepcopy(A)

	# Tiempos de Insertion Sort----------------------------------------------------------------- 
	
	inicio = time.time()
	sorts.InsertionSort(A)
	fin = time.time()
	tiempos_insertion_sort[i] = (fin-inicio)*1000

	# Tiempos de Merge Sort -------------------------------------------------------------------
	
	inicio = time.time()
	sorts.MergeSort(B,0,len(B)-1)
	fin = time.time()
	tiempos_merge_sort[i] = (fin-inicio)*1000

	# Tiempos de Heap Sort --------------------------------------------------------------------

	inicio = time.time()
	sorts.HeapSort(C)
	fin = time.time()
	tiempos_heap_sort[i] = (fin-inicio)*1000

	# Tiempos Quick Sort ----------------------------------------------------------------------

	inicio = time.time()
	sorts.QuickSort(D,0,len(D))
	fin = time.time()
	tiempos_quick_sort[i] = (fin-inicio)*1000

	# Tiempos de Random Quick Sort ------------------------------------------------------------

	inicio = time.time()
	sorts.RandomQuickSort(E,0,len(E))
	fin = time.time()
	tiempos_random_quick_sort[i] = (fin-inicio)*1000

	# Tiempos de Counting Sort ----------------------------------------------------------------

	H = [0]*len(F)
	k = max(F)
	inicio = time.time()
	F = sorts.CountingSort(F,H,k)
	fin = time.time()
	tiempos_counting_sort[i] = (fin-inicio)*1000

	# Tiempos de Radix Sort ------------------------------------------------------------------

	digito_maximo = 0

	for l in range(0,len(G)):

		G[l] = str(G[l])

		if len(G[l]) >= digito_maximo:

			digito_maximo = len(G[l])

		G[l] = int(G[l])

	inicio = time.time()
	J = sorts.RadixSort(G,digito_maximo)
	fin = time.time()
	tiempos_radix_sort[i] = (fin-inicio)*1000

# Calculo de tiempo promedio y desviacion estandar de Insertion Sort:

tiempo_promedio_insertion ,desviacion_estandar_insertion = Calculo_Promedio_y_Desviacion_Estandar(tiempos_insertion_sort)

print("\nInsertion Sort {:.2f} {:.2f}".format(tiempo_promedio_insertion, desviacion_estandar_insertion))

# Calculo de tiempo promedio y desviacion estandar de Merge Sort:

tiempo_promedio_merge, desviacion_estandar_merge = Calculo_Promedio_y_Desviacion_Estandar(tiempos_merge_sort)  

print("\nMerge Sort {:.2f} {:.2f}".format(tiempo_promedio_merge, desviacion_estandar_merge))

# Calculo de tiempo promedio y desviacion estandar de Heap Sort:

tiempo_promedio_heap, desviacion_estandar_heap = Calculo_Promedio_y_Desviacion_Estandar(tiempos_heap_sort) 

print("\nHeap Sort {:.2f} {:.2f}".format(tiempo_promedio_heap, desviacion_estandar_heap))

# Calculo de tiempo promedio y desviacion estandar de Quick Sort:

tiempo_promedio_quick, desviacion_estandar_quick = Calculo_Promedio_y_Desviacion_Estandar(tiempos_quick_sort) 

print("\nQuick Sort {:.2f} {:.2f}".format(tiempo_promedio_quick, desviacion_estandar_quick))

# Calculo de tiempo promedio y desviacion estandar de Random Quick Sort:

tiempo_promedio_quick_r, desviacion_estandar_quick_r = Calculo_Promedio_y_Desviacion_Estandar(tiempos_random_quick_sort)  

print("\nRandom Quick Sort {:.2f} {:.2f}".format(tiempo_promedio_quick_r, desviacion_estandar_quick_r))

# Calculo de tiempo promedio y desviacion estandar de Counting Sort:

tiempo_promedio_counting, desviacion_estandar_counting = Calculo_Promedio_y_Desviacion_Estandar(tiempos_counting_sort)

print("\nCounting Sort {:.2f} {:.2f}".format(tiempo_promedio_counting, desviacion_estandar_counting))

# Calculo de tiempo promedio y desviacion estandar de radix Sort:

tiempo_promedio_radix, desviacion_estandar_radix = Calculo_Promedio_y_Desviacion_Estandar(tiempos_radix_sort)

print("\nRadix Sort {:.2f} {:.2f}".format(tiempo_promedio_radix, desviacion_estandar_radix))