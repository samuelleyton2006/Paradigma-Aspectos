# Taller Aspectos 

## Samuel Leyton Muñoz - Taller Paradigma Aspectos


### 1. En pocas palabras, el objetivo principal de la POA es:

 Opcion :
 
 c.	Separar conceptos y minimizar las dependencias entre ellos
 
 Justificacion : 
 

### 2. ¿Cuál es el inconveniente que se presenta al usar las metodologías iterativas y POO?

   Opcion : 
   b.	No se considera el tratamiento de aspectos como seguridad y gestión de
memoria

   Justificacion : 
   

### 3. ¿Cuál de las siguientes opciones no es uno de los inconvenientes que se presentan al implementar la POA?

  Opcion : 
  d.	Posibles choques entre los aspectos

  Justificacion : 

### 4. ¿En qué consiste el código mezclado (Code Tangling)?

   Opcion : 
   a.	Varios requerimientos pueden estar dentro de un mismo módulo.

   Justificacion : 
   


### 5. ¿Cuáles de los siguientes elementos son propios de la POA?

   Opcion : 
   b.	Puntos de corte, tejedores, puntos de enlace.

   Justificacion :



### 6. Una incumbencia transversal o ‘crosscutting concern’ es:

   Opcion : 
   c.	La conceptualización de responsabilidades de uso común en un sistema

   Justificacion : 

### 7. En un banco se desea aplicar el concepto de la programación orientada a aspectos, un aspecto que se podría abstraer sería:
 
   Opcion : 
   b.	La validación de una transacción de un cliente o empleado del banco.

   Justificacion : 

### 8. ¿Qué se define en un consejo?

   Opcion : 
   b.	El código que debe ser ejecutado en los puntos de unión

   Justificacion : 

   Los consejos se aplican en los puntos de union , las uniones son : 

   - Cuando se llama un metodo
   - Momento de ejecucion de algun metodo
   - El momento de crear objetos

   Se aplican en estos puntos ya que estos arreglos o consejos se deben ejecutar en un momento preciso . Funcional principalmente para generar funciones transversales (que no son dependientes en la mayoria de casos , de las funciones ).
   Como ejemplo de esto les puedo dar : 
   - La gestion de transacciones
   - cuestiones de creacion de usuarios y contraseñas

 Esto se hace para que estas creaciones o modificaciones dentro del sistema no afecten directamente a el codigo fuente o base . Evitan vulnerabilidades comunes o sencillas  .

   

### 9. La Programación Orientada a Aspectos (POA) es un paradigma cuya intención es permitir una adecuada _____________ de las aplicaciones, posibilitando mejor separación de incumbencias.

   Opcion : 
   b.	Modularización

   Justificacion : 

   La programacion orientada a aspectos esta especificamente diseñada para desarrollarse de manera modular o una manera en la cual los diferentes problemas que afectan al sistema .

   Como ejemplo de esto podria ser : 
   
   - En sistemas de seguridad principalmente basados en usuarios individuales que confian su seguridad en el prestador de servicio el cual le confian su informacion , lo que las empresas hacen es fraccionar el problema y las diferentes gestiones en el Logging de manera no centrica.
   - La programacion orientada a aspectos lo que busca es dividir los problemas de seguridad para que el manejo de errores sea mayor y sencillo .
   - La programacion orientada a aspectos es sencilla en cuestion visual y algo compleja en cuestion de conexion con los diferentes aspectos en que se puede basar un programa o sistema . Aunque al ser modular su mantenimiento y resolucion de bugs o errores se soluciona de manera mas directa y los errores son faciles de encontrar.

### 10.De los siguientes términos, ¿cuál está relacionado con la POA?

   Opcion : 
   d.	Tejedor

   Justificacion : 

   - El tejedor se basa de manera concisa en el procedimiento que se utiliza el codigo fuente o codigo base del programa con los diferentes aspectos que se creen . Crea puntos de interes o tambien llamadas preocupaciones en problemas transversales los cuales buscan otra solucion .
   

 

     
   En un servidor web que maneja un alto volumen de solicitudes de usuarios, el balanceo de carga es esencial para distribuir las solicitudes entre múltiples procesadores o servidores. Si una parte del sistema se sobrecarga mientras otras están inactivas, el tiempo de respuesta aumentará y los usuarios experimentarán retrasos. El balanceo de carga garantiza que todas las solicitudes se distribuyan de manera equitativa, optimizando los tiempos de respuesta y utilizando los recursos de manera eficiente.



   - Latencia: es el tiempo que tarda en iniciarse una comunicación entre hilos o procesos. Alta latencia puede afectar negativamente al rendimiento en sistemas paralelos, especialmente en aplicaciones que requieren comunicación frecuente.
   - Ancho de banda: es la cantidad de datos que pueden transferirse en un periodo determinado. Un bajo ancho de banda limita la cantidad de información que puede compartirse rápidamente, afectando el rendimiento en aplicaciones que requieren grandes volúmenes de datos entre hilos o nodos de procesamiento.


   - Sincronización y condiciones de carrera: los accesos concurrentes a datos compartidos pueden causar errores. Para mitigarlo, se utilizan técnicas de sincronización como bloqueos y semáforos.
   - Overhead de comunicación: el tiempo y recursos necesarios para coordinar hilos o procesos pueden reducir el rendimiento. Para reducir el overhead, se puede optimizar la comunicación y limitar la creación y sincronización de hilos.
   - Balanceo de carga: es difícil distribuir equitativamente las tareas en todos los núcleos. Algoritmos de balanceo de carga dinámico ayudan a mantener una distribución equitativa.
   - Escalabilidad: asegurar que el sistema pueda manejar el incremento de tareas y procesadores. Se puede mitigar utilizando arquitecturas de sistema escalables y protocolos de comunicación eficientes.
   - Deadlocks y bloqueos: para evitarlos, se utilizan técnicas de prevención y resolución de deadlocks, como los time-outs y el orden en la asignación de recursos.

### Ejercicio de implementación 

```python 
import kotlinx.coroutines.*
import java.util.concurrent.RecursiveTask
import java.util.concurrent.ForkJoinPool
import kotlin.system.measureTimeMillis

// Implementación secuencial
fun sumList(numbers: List<Int>): Int {
    var sum = 0
    for (number in numbers) {
        sum += number
    }
    return sum
}

// Implementación paralela usando corrutinas
fun sumListParallelCoroutine(numbers: List<Int>): Int = runBlocking {
    val chunkSize = numbers.size / 4  // Dividir la lista en 4 partes
    val deferredResults = (0 until 4).map { i ->
        async {
            numbers.subList(i * chunkSize, (i + 1) * chunkSize).sum()
        }
    }
    deferredResults.awaitAll().sum() // Esperar a todas las corrutinas y sumar los resultados
}

// Implementación paralela usando ForkJoinPool
class SumTask(private val numbers: List<Int>, private val start: Int, private val end: Int) : RecursiveTask<Int>() {
    override fun compute(): Int {
        return if (end - start <= 250_000) {  // Tamaño mínimo para dividir
            numbers.subList(start, end).sum()
        } else {
            val mid = (start + end) / 2
            val leftTask = SumTask(numbers, start, mid)
            val rightTask = SumTask(numbers, mid, end)
            leftTask.fork()  // Ejecutar la tarea izquierda en paralelo
            rightTask.compute() + leftTask.join()  // Combinar resultados
        }
    }
}

fun sumListParallelForkJoin(numbers: List<Int>): Int {
    val pool = ForkJoinPool()
    val task = SumTask(numbers, 0, numbers.size)
    return pool.invoke(task)
}

fun main() {
    val numbers = List(1_000_000) { (1..10).random() }

    // Ejecución secuencial
    val timeSequential = measureTimeMillis {
        println("Suma total secuencial: ${sumList(numbers)}")
    }
    println("Tiempo secuencial: $timeSequential ms")

    // Ejecución paralela con corrutinas
    val timeParallelCoroutine = measureTimeMillis {
        println("Suma total paralela (corrutinas): ${sumListParallelCoroutine(numbers)}")
    }
    println("Tiempo paralelo (corrutinas): $timeParallelCoroutine ms")

    // Ejecución paralela con ForkJoinPool
    val timeParallelForkJoin = measureTimeMillis {
        println("Suma total paralela (ForkJoin): ${sumListParallelForkJoin(numbers)}")
    }
    println("Tiempo paralelo (ForkJoin): $timeParallelForkJoin ms")
}
```
## Análisis de Comparación de Tiempos

### Implementación Secuencial:

Este método recorre toda la lista de números y suma cada elemento de manera secuencial.
Este método actúa como un punto de referencia. Como es secuencial, su tiempo de ejecución será el más alto en la mayoría de los casos, especialmente para listas grandes (1,000,000 de elementos en este caso).
Tiempo esperado: Mayor tiempo debido a la falta de paralelización.

### Implementación Paralela con Corrutinas:

Este método divide la lista en 4 partes iguales y usa una corrutina para calcular la suma de cada parte en paralelo.
Las corrutinas son ligeras y no crean hilos adicionales a menos que sea necesario, lo que reduce la sobrecarga de gestión de hilos.
Ventajas: Las corrutinas son adecuadas para procesamiento concurrente con poco overhead, siendo una buena opción en sistemas con pocos núcleos.
Desventajas: La paralelización se limita a 4 corrutinas, lo que podría no aprovechar al máximo los recursos en sistemas con muchos núcleos.
Tiempo esperado: Generalmente menor que la implementación secuencial, pero puede ser menos eficiente que ForkJoinPool en sistemas multicore.

### Implementación Paralela con ForkJoinPool:

Utiliza el patrón divide y vencerás para dividir la lista en partes cada vez más pequeñas hasta un tamaño mínimo (250,000 en este caso).
ForkJoinPool es altamente eficiente para tareas que pueden dividirse en subtareas recursivas, optimizando la gestión de hilos en sistemas multicore.
Ventajas: Ideal para listas grandes en sistemas con múltiples núcleos, debido a su paralelización profunda y administración eficiente de tareas.
Desventajas: Puede ser menos eficiente para listas pequeñas debido a la sobrecarga de gestionar la estructura de tareas.
Tiempo esperado: Generalmente el tiempo más bajo en sistemas multicore, aprovechando la paralelización y optimización de recursos.

## Ejemplo de resultados

```kotlin

Suma total secuencial: 5,000,000
Tiempo secuencial: 150 ms

Suma total paralela (corrutinas): 5,000,000
Tiempo paralelo (corrutinas): 80 ms

Suma total paralela (ForkJoin): 5,000,000
Tiempo paralelo (ForkJoin): 60 ms
```
- Secuencial: tomó 150 ms, el tiempo más alto debido a la falta de paralelización.
- Corrutinas: redujeron el tiempo a 80 ms, mostrando una mejora significativa en comparación con el método secuencial.
- ForkJoinPool: fue el método más rápido (60 ms), mostrando que aprovecha mejor los recursos del sistema para listas grandes.
### Conclusión

Secuencial: Suficiente para listas pequeñas. <br>
Corrutinas: Adecuado para tamaños de listas medianas o en sistemas con pocos núcleos. <br>
ForkJoinPool: Recomendado para listas grandes y sistemas multicore. <br>
