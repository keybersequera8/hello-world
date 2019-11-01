#### CI2692
#### SD 2019
#### Estudiantes: Alexis Infante 17-10284 y Keyber Sequera 16-11120

# Proyecto 1
## Comparacion de algoritmos de aprendizaje

### Resumen

El proyecto aborda los distintos tipos de algoritmos de ordenamiento y las estructuras que estos poseen, dicha estructura es unica y tal cualidad hace que algunos sean mas rapidos y eficientes que otros, por ejemplo se puede apreciar el comportamiento del algoritmo de ordenamiento por insercion, que hace lo que requiere un algoritmo de ordenamiento, sin embargo, el tiempo de corrida de este es mucho mayor que otros algoritmos cuya estructura es un poco mas compleja, pero que a su favor cuentan con la cualidad de que ordenan los arreglos desordenados en menos tiempo. Lo cual nos enseña que existen diversas formas de resolver un problema y algunas son mas eficientes que otras.

#### Breve descripcion de la implementacion

Los algoritmos de ordenamiento estudiados cuentan con la caracteristica de que algunos resuelven el problema de ordenamiento de manera lineal y otros usando el metodo (Divide and Conquer), que consiste en dividir el problema original en varios subproblemas los cuales ayudaran a resolver el problema original. Los algoritmos de ordenamiento lineal estudiados fueron: Insertion Sort, Counting Sort y Radix Sort.

- Insertion Sort: cuenta con la cualidad de que en el peor caso, resuelve el problema de ordenamiento de un arreglo de n elementos en tiempo de O(n^2)^, y aborda este problema comparando cada uno de los elementos del arreglo.

- Counting Sort: cuenta con la cualidad de que en el peor caso resuelve el problema de ordenamiento de un arreglo de n elementos en un tiempo de O(n+k), donde k sera el mayor de los elementos del arreglo estudiado, este algoritmo resuelve el problema de ordenamiento de una manera mas sofisticada, haciendo uso de dos arreglos auxiliares donde en uno se guardaron las ocurrencias de cada elemento y en otro se guardara el arreglo original ordenado.

- Radix Sort: cuenta con la cualidad de que en el peor caso resuelve el problema de ordenamiento de un arreglo de n elementos en un tiempo de O(n.k), donde k es la cantidad de digitos del mayor elemento, este algoritmo resuelve el problema de ordenamiento haciendo uso de un arreglo (B) auxiliar, que se usara para almacenar la ocurrencia de cada digito de los distintos elementos del arreglo a ordenar, y los guardara en cada uno de las posiciones de B (como si fuera un pote donde se arrojan los elementos), luego los devolvera al arreglo original en el orden en que se encuentran en el arreglo B, asi hasta recorrer cada digito de cada elemento de A y devolver finalmente el arreglo ordenado.

Por otra parte, los algoritmos que usan la estrategia de Divide and Conque, fueron:

- Merge Sort: cuenta con la cualidad de que en el peor caso resuelve el problema de ordenamiento de un arreglo de n elementos en un tiempo de O(n.log(n)), ese parte el arreglo original en bloques y luego ordena estos de manera recursiva hasta ordenar el arreglo original.

- Heap Sort: cuenta con la cualidad de que en el peor caso resuelve el problema de ordenamiento de un arreglo de n elementos en un tiempo de O(n.log(n)), este algoritmo considera al arreglo a ordenar como un arbol binario, que ordenara de manera descendente, luego a traves de la implementacion del algoritmo Heap Sort, ordenara el arreglo, intercambiando el valor de la ultima rama del arbol binario con la primera, lo que hace que el menor elemento este de primero y ubique los demas elementos de tal forma que el arreglo queda ordenado de manera ascendente.

- Quick Sort: cuenta con la cualidad de que en el peor caso resuelve el problema de ordenamiento de un arreglo de n elementos en un tiempo de O(n^2), sin embargo, su caso promedio resuelve el problema de ordenamiento en un tiempo de O(n.log(n)), lo cual lo hace bastante efectivo, este algoritmo funciona tomando pivotes y comparandolos con cada elemento anterior a ellos, de manera que pone al pivote en la posicion que le corresponde y a su lado izquierdo a los elementos menores a el y a la derecha a los elementos mayores a el, luego, creara un pivote para estos dos lados (izquierdo y derecho) y ubicara en la posicion adecuada al nuevo pivote, y llamara recursivamente al proceso hasta ordenar al arreglo original

- Randomized Quick Sort: cuenta con la cualidad de que en el peor caso resuelve el problema de ordenamiento de un arreglo de n elementos en un tiempo de O(n^2), sin embargo, su caso promedio resuelve el problema de ordenamiento en un tiempo de O(n.log(n)), y al seleccionar al pivote de manera aleatorio hace menos probable la aparicion del peor caso, lo que lo hace una mejor opcion que quick sort a pesar de que su tiempo de ejecucion en el caso promedio se tarde un poco mas que el anterior.

### Tabla que contiene los datos obtenidos de la corrida de los algoritmos de ordenamiento.

--------------------------------------------------------------------------------------------------------------------
| Algoritmo             |  1.000  |  5.000 | 10.000 | 20.000 | 40.000  | 80.000   | 160.000  |                      |
|----------------------	|-------  |--------|--------|--------|-------- |----------|----------|----------------------|
| Insertion            	|143.74   |3934.10 |16380.12|60879.13|218773.51|1080815.38|4234563.75| Tiempo Promedio      |
|						|23.06    |172.39  |296.00	|5523.38 |11269.06 |112080.59 |320653.35 | Desviacion estandar  |
|                       |         |        |        |        |         |          |          |                      |
| Merge Sort           	|9.37     |82.81   |167.18  |356.23  |693.70   |1701.44   |4073.19   | Tiempo Promedio      |
|						|8.07	  |12.86   |16.55   |59.29   |33.10    |124.89    |398.53    | Desviacion estandar  | 
|                       |         |        |        |        |         |          |          |                      |
| Heap Sort            	|20.31    |129.68  |285.92  |595.27  |1168.67  |2900.56   |4681.58   | Tiempo Promedio      |
|						|7.55     |16.55   |32.98   |62.69   |40.88    |408.83    |390.86    | Desviacion estandar  |
|                       |         |        |        |        |         |          |          |                      |
| Quicksort            	|9.37     |46.87   |101.55  |209.36  |406.23   |1007.07   |2183.98   | Tiempo Promedio      |
|						|8.07     |10.42   |8.24    |16.79   |23.29    |134.86    |206.53    | Desviacion estandar  |
|                       |         |        |        |        |         |          |          |                      |
| Randomized Quicksort 	|10.94    |56.25   |132.80  |281.23  |523.40   |1297.81   |2438.78   | Tiempo Promedio      |
|						|7.55     |8.07    |18.41   |54.12   |30.59    |202.95    |385.97    | Desviacion estandar  |
|                       |         |        |        |        |         |          |          |                      |
| Counting sort        	|3.12     |12.50   |17.19   |35.94   |68.74    |171.73    |436.25    | Tiempo Promedio      |
|						|6.59     |6.59    |4.94    |7.55    |8.06     |28.37     |56.37	 | Desviacion estandar  |
|                       |         |        |        |        |         |          |          |                      |
| Radix sort           	|9.37     |315.60  |2010.80 |8230.68 |35021.03 |191334.98 |546737.64 | Tiempo Promedio      |
|						|8.07     |17.74   |47.19   |256.08  |326.58   |61733.62  |127839.83 | Desviacion estandar  |
---------------------------------------------------------------------------------------------------------------------

### Graficas


![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Insertion%20Sort.png)

![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Merge%20Sort.png)

![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Heap%20Sort.png)

![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Quicksort.png)

![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Randomized%20Quicksort.png)

![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Counting%20Sort.png)

![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Radix%20Sort.png)

![alt text](https://github.com/keybersequera8/hello-world/blob/master/Graficas/Average%20Running%20Times.png)


### Analisis de graficas

En las graficas se puede apreciar que la mayoria de los algoritmos de ordenamiento lineal tardan en ordenar un arreglo desordenado mas tiempo de lo que lo hacen los algoritmos que hacen multiples llamadas recursivas. Ademas, se puede observar que los algoritmos de
ordenamiento lineal, tienen un tiempo de corrida que siguen los valores teoricos expuestos en clases, sin embargo, el tiempo de corrida de ellos varia mucho de un algoritmo a otro, por ejemplo: el tiempo de corrida de Insertion Sort, es mucho mayor que el de Radix Sort y estos a su vez arrojan tiempos mayores que los de Counting Sort, en cambio, la diferencia de tiempos de los algoritmos que siguen el paradigma de Divide and Conquer, es mucho menor, ya que sus tiempos de corrida promedio son iguales O(n.log(n)).

### Conclusiones

Existen diversas maneras de resolver un mismo problema, algunas de ellas rápidas y efectivas, mientras que existen otras las cuales aunque resuelven el problema prsentado, son menos eficientes. Un ejemplo claro de esta situacion se presenta con los algoritmos de ordenamiento estudiados, pudimos observar que con algoritmos menos complejos tales como Inserion Sort, el problema de ordenar un arreglo es resuelto, pero el costo de tiempo requerido para obtener el objetivo es extremadamente alto para arreglos de gran tamaño.

A pesar de que observamos que Insertion Sort puede ser igual o mas efectivo que algunos de sus competidores para arreglos pequenos, al aumentar el tamano del arreglo a ordenar se pudo observar que su estructura lineal no era tan eficiente como algoritmos que siguen la estrategia Divide and Conquer, los cuales al dividir el problema original en subproblemas y resolverlos de manera recursiva, mostraron ser eficientes para cualquier tamano de arreglo. 

Se pudo comprobar el conocimiento teorico de que los tiempos de corrida de algoritmos lineales suelen ser mucho mayores que el de algoritmos Divide and Conquer. A pesar de que todos los metodos eventualmente resuelven el mismo problema, es necesario diferenciar en que situaciones algunos son mas eficientes que otros, y hacer la eleccion correcta para resolver el problema en cuestion de la mejor manera posible.