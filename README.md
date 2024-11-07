markdown
# Laboratorio N°1 - ALGORITMOS GENÉTICOS

## Universidad Nacional Mayor de San Marcos  
**Facultad de Ingeniería de Sistemas e Informática**  
**Curso:** Automatización y Control de Software

### Descripción del Proyecto

Este proyecto tiene como objetivo la implementación de un **algoritmo genético** para la resolución de problemas de optimización en un entorno de simulación. El problema planteado consiste en encontrar la mejor ruta para un robot en un laberinto, donde el robot debe tomar decisiones sobre los movimientos a seguir basándose en una población de cromosomas generados aleatoriamente.

### Funcionamiento del Algoritmo Genético

1. **Inicialización de Cromosomas**: Se generan una población inicial de cromosomas, los cuales representan diferentes rutas posibles que el robot puede seguir en el laberinto.
2. **Evaluación de la Población**: Cada cromosoma es evaluado en función de su "fitness" (aptitud), que se calcula considerando factores como la distancia recorrida, colisiones, y la cantidad de giros.
3. **Selección, Cruce y Mutación**: Los cromosomas con mejor desempeño son seleccionados para cruzarse y generar nuevos cromosomas mediante mutaciones aleatorias.
4. **Evolución**: El proceso de selección, cruce y mutación se repite durante un número determinado de generaciones, hasta que se encuentra la ruta óptima o se alcanza el número máximo de generaciones.

El algoritmo se ejecuta en una interfaz gráfica en la que se visualiza el laberinto, el robot y las rutas que toma en cada generación, permitiendo observar la evolución de las soluciones encontradas.

### Integrantes del Proyecto

- **Chuquispuma Merino, Fabricio Vidal**
- **Felix Huayhua, Axel Patrick**
- **Fernandez Camacho Geomar Willy**
- **Saavedra Monterrey, Max Bruno**
- **Sanchez Saldaña, Sergio Antonio**

### Requisitos de Configuración

Este proyecto fue desarrollado en Python y requiere las siguientes bibliotecas para su ejecución:

- `tkinter`: Para la interfaz gráfica de usuario.
- `random`: Para la generación de cromosomas aleatorios.
- `matplotlib`: Para la visualización de los resultados.
- `numpy`: Para operaciones matemáticas.

#### Instalación de Dependencias

Para instalar las dependencias necesarias, puedes utilizar `pip`:

bash
pip install -r requirements.txt


El archivo `requirements.txt` debe contener las siguientes líneas:


tkinter
numpy
matplotlib


### Instrucciones para Ejecutar el Proyecto

1. **Clona el repositorio**:

   bash
   git clone <URL_DEL_REPOSITORIO>
   cd <directorio_del_repositorio>
   

2. **Ejecuta el script principal**:

   bash
   python main.py
   

3. **Interfaz gráfica**: Al ejecutar el proyecto, se abrirá una ventana con la interfaz gráfica en la que podrás ingresar las posiciones del robot y el objetivo. Luego, el algoritmo genético se ejecutará mostrando el progreso y la mejor ruta encontrada.

### Estructura del Proyecto

- `main.py`: Script principal para ejecutar el algoritmo genético y la interfaz gráfica.
- `algoritmo.py`: Contiene la implementación del algoritmo genético.
- `robot.py`: Implementación de la clase `Robot`, que representa al robot y sus movimientos.
- `laberinto.py`: Define la estructura del laberinto.
- `generaciones_log.txt`: Archivo de log que guarda el progreso de cada generación del algoritmo.

### Aportaciones y Resultados

El proyecto ha sido desarrollado por un grupo de estudiantes de la Facultad de Ingeniería de Sistemas e Informática de la **Universidad Nacional Mayor de San Marcos**, y tiene como objetivo demostrar el uso de algoritmos genéticos para resolver problemas de optimización. La solución encontrada representa una ruta óptima para el robot dentro del laberinto, teniendo en cuenta las restricciones del entorno.

### Licencia

Este proyecto es de uso académico y se encuentra bajo la **Licencia MIT**. Esta licencia permite a los usuarios utilizar, modificar y distribuir el software de forma gratuita, siempre que se incluya el aviso de copyright y la renuncia de responsabilidad. Se ofrece "tal cual", sin ninguna garantía expresa o implícita, incluyendo, pero no limitándose a, garantías de comerciabilidad o adecuación para un propósito particular.

