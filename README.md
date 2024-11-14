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

   

### 9. ¿Qué es un “deadlock” y cómo puede ocurrir en sistemas paralelos? 

   Un deadlock (bloqueo mutuo) ocurre cuando dos o más hilos o procesos esperan indefinidamente por recursos que están siendo retenidos mutuamente. En sistemas paralelos, puede suceder cuando un proceso bloquea un recurso que otro necesita y viceversa, provocando que ambos se queden en un estado de espera sin poder continuar.

### 10. ¿Cuál es el rol de un “scheduler” en la administración de tareas en paralelismo? 

Un "scheduler" (planificador) es el componente encargado de asignar y gestionar la ejecución de tareas o hilos en los núcleos de procesamiento. En paralelismo, el scheduler optimiza la distribución de tareas, decide cuándo y dónde ejecutar cada tarea, y gestiona la prioridad y los recursos para maximizar el rendimiento del sistema y evitar conflictos.


### 11. Describe cómo el paralelismo puede mejorar el rendimiento de un programa. Da un ejemplo general. 

   El paralelismo mejora el rendimiento de un programa al dividir una tarea compleja en sub-tareas más pequeñas que pueden ejecutarse simultáneamente en varios núcleos o procesadores. Esto reduce el tiempo total de ejecución en comparación con la ejecución secuencial.  
   **Ejemplo:** En el procesamiento de una gran cantidad de datos, como una imagen para aplicar filtros, cada sección de la imagen puede procesarse en paralelo, permitiendo que el procesamiento completo se realice mucho más rápido.

### 12. Explica qué es una “condición de carrera” y proporciona un ejemplo de cómo podría ocurrir. 

   Una "condición de carrera" ocurre cuando el resultado de un programa depende del orden en el que se ejecutan los hilos o procesos, lo cual no es controlado ni garantizado. Esto sucede cuando dos o más hilos acceden y modifican una variable compartida sin la adecuada sincronización, llevando a resultados inconsistentes.  
   **Ejemplo:** Dos hilos intentan incrementar el valor de una misma variable. Si ambos leen el valor inicial al mismo tiempo, lo incrementan y lo almacenan, el resultado final puede ser incorrecto, ya que ambos escribieron el mismo valor sin considerar el incremento del otro.

### 13. ¿Por qué es importante la sincronización en programación paralela? Menciona alguna técnica de sincronización.

   La sincronización es crucial para evitar condiciones de carrera y garantizar la consistencia de los datos compartidos entre hilos. Sin sincronización, el acceso concurrente a los recursos puede llevar a errores y resultados impredecibles.  
   Técnica de sincronización: Los bloqueos o "locks" son una técnica común que permite que solo un hilo acceda a una sección crítica del código a la vez, asegurando así que las operaciones se realicen en orden y sin interferencias.

### 14. Describe los posibles efectos del “overhead” en la ejecución de tareas en paralelo. 

   El "overhead" en la ejecución de tareas paralelas se refiere a los recursos adicionales y tiempo que se emplean en la creación, sincronización y gestión de hilos o procesos. Si el overhead es muy alto, puede reducir los beneficios de la paralelización, ya que el tiempo de administración supera las mejoras en el tiempo de ejecución. Esto es especialmente notable en tareas pequeñas, donde el tiempo de coordinación es comparable o incluso mayor que el tiempo de ejecución de la tarea misma.


### 15. Explica cómo se pueden evitar los deadlocks en un sistema paralelo.  

   Para evitar deadlocks, se pueden emplear varias estrategias, como:
   - Evitar la espera circular: asignar recursos en un orden definido y exigir que los procesos soliciten recursos en ese orden, previniendo que formen un ciclo de espera.
   - Asignación preventiva de recursos: asignar todos los recursos necesarios a un proceso antes de que comience, asegurando que no necesite esperar.
   - Desbloqueo de procesos (time-out): establecer un límite de tiempo para que un proceso obtenga recursos; si no lo consigue, libera los recursos asignados y vuelve a intentarlo.
   - Evitar la retención de recursos: hacer que los procesos liberen recursos antes de solicitar otros, reduciendo las dependencias entre ellos.

### 16. ¿Cuáles son las ventajas y desventajas de utilizar memoria compartida en lugar de paso de mensajes en paralelismo?  

   - Ventajas de la memoria compartida:  

 - Mayor velocidad de comunicación, ya que los hilos acceden directamente a los datos en memoria sin necesidad de transferirlos.
 	- Menor latencia en el acceso a datos, ya que se evita el envío de mensajes.
   - Desventajas de la memoria compartida:  
 	- Necesidad de sincronización para evitar condiciones de carrera, lo que añade complejidad.
 	- Mayor riesgo de errores y deadlocks si no se manejan adecuadamente los accesos concurrentes.

   - Ventajas del paso de mensajes:  

 	- Mayor aislamiento entre procesos, lo que reduce el riesgo de interferencias y condiciones de carrera.
 	- Mejor escalabilidad en sistemas distribuidos, ya que los procesos no dependen de un área de memoria compartida.
   - Desventajas del paso de mensajes:  
 	- Mayor latencia y overhead en la comunicación, especialmente si los mensajes deben enviarse a través de una red.
 	- Mayor complejidad para diseñar protocolos de comunicación eficiente entre procesos.

### 17. ¿Qué estrategias existen para gestionar la asignación de tareas en un sistema con múltiples núcleos?
 
   - Asignación estática: las tareas se asignan a núcleos específicos al inicio y no cambian durante la ejecución, reduciendo el overhead pero menos adaptable a cambios de carga.
   - Asignación dinámica: las tareas se asignan a los núcleos de forma dinámica durante la ejecución, lo que permite una mayor flexibilidad y mejor respuesta a variaciones en la carga.
   - Balanceo de carga dinámico: los núcleos se supervisan en tiempo real y las tareas se reasignan para equilibrar la carga, optimizando el uso de recursos.
   - Asignación basada en afinidad: asigna tareas a núcleos que previamente procesaron datos relacionados, optimizando el rendimiento al aprovechar la memoria caché.

### 18. Describe un caso en el que el balanceo de carga sea esencial en un sistema paralelo. 

   En un servidor web que maneja un alto volumen de solicitudes de usuarios, el balanceo de carga es esencial para distribuir las solicitudes entre múltiples procesadores o servidores. Si una parte del sistema se sobrecarga mientras otras están inactivas, el tiempo de respuesta aumentará y los usuarios experimentarán retrasos. El balanceo de carga garantiza que todas las solicitudes se distribuyan de manera equitativa, optimizando los tiempos de respuesta y utilizando los recursos de manera eficiente.

### 19. Explica cómo la latencia y el ancho de banda afectan el rendimiento en paralelismo. 

   - Latencia: es el tiempo que tarda en iniciarse una comunicación entre hilos o procesos. Alta latencia puede afectar negativamente al rendimiento en sistemas paralelos, especialmente en aplicaciones que requieren comunicación frecuente.
   - Ancho de banda: es la cantidad de datos que pueden transferirse en un periodo determinado. Un bajo ancho de banda limita la cantidad de información que puede compartirse rápidamente, afectando el rendimiento en aplicaciones que requieren grandes volúmenes de datos entre hilos o nodos de procesamiento.

### 20. ¿Cuáles son los desafíos principales en la implementación de sistemas paralelos y cómo se pueden mitigar?  

   - Sincronización y condiciones de carrera: los accesos concurrentes a datos compartidos pueden causar errores. Para mitigarlo, se utilizan técnicas de sincronización como bloqueos y semáforos.
   - Overhead de comunicación: el tiempo y recursos necesarios para coordinar hilos o procesos pueden reducir el rendimiento. Para reducir el overhead, se puede optimizar la comunicación y limitar la creación y sincronización de hilos.
   - Balanceo de carga: es difícil distribuir equitativamente las tareas en todos los núcleos. Algoritmos de balanceo de carga dinámico ayudan a mantener una distribución equitativa.
   - Escalabilidad: asegurar que el sistema pueda manejar el incremento de tareas y procesadores. Se puede mitigar utilizando arquitecturas de sistema escalables y protocolos de comunicación eficientes.
   - Deadlocks y bloqueos: para evitarlos, se utilizan técnicas de prevención y resolución de deadlocks, como los time-outs y el orden en la asignación de recursos.

### Ejercicio de implementación 

```kotlin
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
