#TPI - Gestión de Datos de Países en Python
Este proyecto es el Trabajo Práctico Integrador desarrollado para la materia Programación 1 de la Tecnicatura Universitaria en Programación a Distancia de la Universidad Tecnológica Nacional (UTN).

Consiste en una aplicación de consola desarrollada en Python que permite administrar y analizar un dataset de países almacenado en un archivo CSV. El sistema implementa la carga dinámica de datos en memoria (utilizando listas y diccionarios), validación de entradas, control de errores, modularización, filtros avanzados, algoritmos de ordenamiento e indicadores estadísticos básicos.

## 👥 Integrantes del Equipo y Participación
[Rey Martin Nicolas] 

Tareas: Desarrollo del módulo de carga de CSV, funciones de ordenamiento y validación de entradas de texto.

## 🛠️ Requerimientos del Sistema e Instalación
Requisitos previos
Tener instalado Python 3.x en tu sistema.

Estructura de Archivos Necesaria
Para que el sistema funcione correctamente, los siguientes archivos deben estar ubicados en el mismo directorio:

main.py (Código fuente principal)

paises.csv (Base de datos de países)

README.md (Este archivo de documentación)

## Ejecución
Para iniciar el programa, abrí la terminal de comandos dentro de la carpeta del proyecto y ejecutá:

```Bash
python main.py
```

## 📖 Instrucciones de Uso y Funcionalidades
Al iniciar, el sistema cargará automáticamente los registros del archivo paises.csv a la memoria RAM. El usuario interactúa mediante un menú numérico interactivo en consola con las siguientes opciones:

Mostrar todos los países: Lista el contenido actual cargado en memoria en formato de tabla simple.

Agregar un nuevo país: Solicita el ingreso de un nuevo registro. Cuenta con validación estricta para evitar campos de texto vacíos o números negativos en los registros de población y superficie.

Actualizar datos de un país: Permite buscar un país por su nombre exacto y actualizar sus valores actuales de población y superficie.

Buscar país por nombre: Permite buscar países utilizando coincidencia parcial o exacta (insensible a mayúsculas y minúsculas).

Filtrar países: Ofrece un submenú para aislar datos mediante tres criterios independientes: por Continente, por Rango de Población o por Rango de Superficie.

Ordenar países: Permite reordenar el dataset en base al Nombre, la Población o la Superficie, seleccionando si se desea un orden Ascendente o Descendente.

Ver indicadores estadísticos: Calcula y despliega en tiempo real 5 métricas clave: País con mayor población, País con menor población, Promedio global de población, Promedio global de superficie y la Cantidad de países distribuidos por continente.

Salir del programa: Finaliza la ejecución del script de manera limpia.

## 💻 Ejemplos de Entradas y Salidas en Consola
Ejemplo 1: Carga Inicial de Datos (Éxito)
Plaintext
✅ Datos iniciales cargados con éxito. Total: 9 países.

##⚙️  SISTEMA DE GESTIÓN DE PAÍSES (TPI)
1. Mostrar todos los países en memoria
2. Agregar un nuevo país
3. Actualizar datos de un país
...
Ejemplo 2: Uso del Filtro por Rango de Población (Opción 5)
Entrada de usuario:

Opción elegida: 5

Criterio: 2 (Por Rango de Población)

Valor mínimo: 40000000

Valor máximo: 100000000

Salida del sistema:

## Plaintext
📋 Resultados del Filtro (4 encontrados):
• Argentina (América) - Pob: 45376763 - Sup: 2780400 km²
• Alemania (Europa) - Pob: 83149300 - Sup: 357022 km²
• Francia (Europa) - Pob: 68000000 - Sup: 551695 km²
• Italia (Europa) - Pob: 59000000 - Sup: 301340 km²
Ejemplo 3: Validación ante una Entrada Inválida
Entrada de usuario:

Opción de menú seleccionada: cinco

Salida del sistema:

Plaintext
⚠️ Opción inválida. Por favor, ingresá un número del 1 al 8.
