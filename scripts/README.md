# Scripts de la Fantasía del 7

Este directorio contiene los scripts de Python para el estudio de "La Fantasía del 7", una construcción matemática diseñada como contraejemplo para refutar las bases de la numerología.

El propósito de estos scripts es demostrar empíricamente cómo se puede construir un sistema matemático con rigor para forzar la convergencia a un número arbitrario (en este caso, el 7), mostrando que dicho número no posee ninguna cualidad mística o especial.

## Estructura de Archivos

```
scripts/
├── conjetura_7_basic.py      # Funciones básicas y fundamentales
├── conjetura_7_analysis.py   # Análisis estadístico y visualización
├── conjetura_7_interactive.py # Herramienta interactiva completa
├── requirements.txt          # Dependencias de Python
└── README.md                # Esta documentación
```

## Instalación de Dependencias

Antes de ejecutar los scripts, instale las dependencias necesarias:

```bash
pip install -r requirements.txt
```

O instale manualmente:
```bash
pip install numpy matplotlib
```

## Descripción de los Módulos

### 1. `conjetura_7_basic.py`

**Propósito:** Contiene las funciones fundamentales para trabajar con la Fantasía del 7.

**Funciones principales:**
- `F7(n)`: Implementación de la función F₇ según la definición matemática
- `compute_orbit(n0, max_iterations=1000)`: Calcula la órbita completa de un número
- `prove_convergence(n0)`: Demostración constructiva de convergencia (para n₀ > 100)

**Uso básico:**
```python
from conjetura_7_basic import F7, compute_orbit, prove_convergence

# Calcular F7 de un número
result = F7(153)
print(f"F7(153) = {result}")

# Obtener la órbita completa
orbit, time = compute_orbit(153)
print(f"153 converge en {time} pasos: {orbit}")

# Demostración constructiva
steps, trajectory = prove_convergence(153)
print(f"Demostración: {steps} pasos, trayectoria: {trajectory}")
```

**Ejecución directa:**
```bash
python conjetura_7_basic.py
```

### 2. `conjetura_7_analysis.py`

**Propósito:** Herramientas avanzadas para análisis estadístico y visualización.

**Funciones principales:**
- `evaluate_single_number(n0, ...)`: Análisis detallado de un número individual
- `evaluate_series(start, end, ...)`: Análisis estadístico de rangos de números
- `create_visualization(results, ...)`: Generación de gráficos y visualizaciones

**Uso básico:**
```python
from conjetura_7_analysis import evaluate_single_number, evaluate_series, create_visualization

# Análisis detallado de un número
result = evaluate_single_number(153)

# Análisis de una serie
results = evaluate_series(101, 200)

# Crear visualización
create_visualization(results, "Análisis [101, 200]")
```

**Características del análisis:**
- Verificación de cotas teóricas
- Estadísticas de convergencia
- Análisis de trayectorias
- Medición de tiempos de ejecución
- Distribuciones de tiempo de convergencia

**Ejecución directa:**
```bash
python conjetura_7_analysis.py
```

### 3. `conjetura_7_interactive.py`

**Propósito:** Herramienta interactiva completa para explorar la Fantasía del 7.

**Funciones principales:**
- `main_interactive()`: Interfaz de usuario interactiva
- `run_predefined_tests()`: Ejecuta pruebas predefinidas del documento
- `quick_test()`: Prueba rápida de funcionamiento

**Opciones del menú interactivo:**
1. **Evaluar un número único**: Análisis detallado de un valor específico
2. **Evaluar una serie de números**: Análisis estadístico de rangos
3. **Ejecutar pruebas predefinidas**: Casos de prueba del documento original
4. **Análisis completo con visualización**: Análisis + gráficos automáticos
5. **Demostración constructiva**: Verificación formal de convergencia

**Ejecución:**
```bash
python conjetura_7_interactive.py
```

## Ejemplos de Uso

### Ejemplo 1: Verificación Rápida

```python
# Verificar que un número converge
from conjetura_7_basic import compute_orbit

orbit, time = compute_orbit(247)
print(f"247 → {' → '.join(map(str, orbit))}")
print(f"Converge en {time} pasos")
```

### Ejemplo 2: Análisis Estadístico

```python
# Analizar un rango de números
from conjetura_7_analysis import evaluate_series

results = evaluate_series(101, 150, show_summary=True)
# Mostrará estadísticas completas automáticamente
```

### Ejemplo 3: Verificación de Casos del Documento

```python
# Ejecutar los casos específicos mencionados en el estudio
from conjetura_7_interactive import run_predefined_tests

run_predefined_tests()
```

### Ejemplo 4: Análisis Completo con Visualización

```python
from conjetura_7_analysis import evaluate_series, create_visualization

# Analizar serie y crear gráficos
results = evaluate_series(101, 300)
create_visualization(results, "Análisis Completo [101, 300]")
# Generará archivo 'conjetura_7_resultados.png'
```

## Casos de Prueba Predefinidos

Los scripts incluyen varios casos de prueba que replican exactamente los resultados del documento:

### Casos Específicos
- **153**: [153, 76, 38, 19, 9, 4, 5, 6, 7] (8 pasos)
- **247**: [247, 123, 61, 30, 15, 7] (5 pasos)
- **384, 519, 672**: Casos adicionales verificados
- **Potencias de 2**: 128, 256, 512, 1024

### Series Estadísticas
- **[101, 150]**: Análisis detallado de 50 números
- **[101, 200]**: Verificación de rango pequeño
- **[501, 1000]**: Análisis de escalabilidad

## Interpretación de Resultados

### Métricas Mostradas
- **Tiempo de convergencia**: Número de pasos hasta llegar a 7
- **Trayectoria**: Secuencia completa de valores
- **Cotas teóricas**: Verificación de límites superior e inferior
- **Estadísticas**: Promedio, mediana, desviación estándar
- **Eficiencia**: Ratio entre tiempo real y cota teórica

### Visualizaciones Generadas
1. **Histograma**: Distribución de tiempos de convergencia
2. **Scatter plot**: Tiempo vs valor inicial con cotas teóricas
3. **Trayectorias**: Ejemplos de convergencia
4. **Eficiencia**: Distribución de ratios de eficiencia

## Verificación de Resultados

Todos los scripts están diseñados para replicar exactamente los resultados presentados en el documento `Estudio.md`. Los casos de prueba predefinidos verifican:

- ✅ Convergencia universal en rangos testados
- ✅ Satisfacción de cotas teóricas
- ✅ Consistencia de trayectorias específicas
- ✅ Estadísticas de distribución de tiempos
- ✅ Comportamiento de casos especiales (potencias de 2)

## Solución de Problemas

### Error de Importación
```
ModuleNotFoundError: No module named 'numpy'
```
**Solución**: Instalar dependencias con `pip install -r requirements.txt`

### Error de Visualización
```
No module named 'matplotlib.pyplot'
```
**Solución**: Instalar matplotlib con `pip install matplotlib`

### Error en Demostración Constructiva
```
ValueError: n0 must be > 100
```
**Solución**: La demostración constructiva solo funciona para números > 100 según el teorema

## Extensiones Posibles

Los scripts pueden ser extendidos para:
- Análisis de la familia de funciones F_k
- Verificación de rangos más grandes
- Optimizaciones de rendimiento
- Análisis de patrones específicos
- Exportación de datos en diferentes formatos

## Contacto y Contribuciones

Estos scripts fueron extraídos automáticamente del documento académico `Estudio.md`. Para modificaciones o extensiones, consulte el documento original que contiene la fundamentación teórica completa.
