# La Fantasía del 7: Una Refutación Matemática de la Numerología

## 🎯 Propósito

Este proyecto es una demostración matemática diseñada para refutar las pretensiones de la numerología sobre el número 7. Construimos deliberadamente un sistema donde TODOS los números convergen al 7, no por alguna propiedad mística o especial de este número, sino por diseño matemático arbitrario.

**Mensaje clave:** Si podemos hacer que cualquier número sea "especial" mediante construcción matemática, entonces ningún número es verdaderamente especial en el sentido místico que propone la numerología.

## 🚀 Inicio Rápido

```bash
# 1. Clonar y entrar al directorio
git clone https://github.com/686f6c61/conjetura-falso-7.git
cd conjetura-falso-7

# 2. Instalar dependencias
pip install -r scripts/requirements.txt

# 3. Ejecutar verificador del teorema
python scripts/verificador_teorema.py

# 4. Verificar un número específico
python scripts/verificador_teorema.py 10000000
# Salida: 10000000 → 7 en 24 pasos
```

## 🔢 La Función F₇

La función central es devastadoramente simple:

```
F₇(n) = {
    n                    si n = 7
    ⌊n/2⌋               si n > 7 y n es par
    ⌊(n-1)/2⌋           si n > 7 y n es impar
    n + 1               si n < 7
}
```

### Ejemplo de Convergencia

```
20 → 10 → 5 → 2 → 3 → 4 → 5 → 6 → 7 → 7 → 7...
100 → 50 → 25 → 12 → 6 → 7 → 7 → 7...
10000000 → 5000000 → 2500000 → ... → 7 (en 24 pasos)
```

## 📁 Estructura del Proyecto

### Documento Principal
- **`Investigacion_Conjetura_7.md`** - Estudio completo que incluye:
  - Marco teórico anti-numerológico
  - Definiciones formales y demostraciones
  - Análisis matemático riguroso
  - Implicaciones filosóficas
  - Refutación sistemática de la numerología

### Script de Verificación

#### `scripts/verificador_teorema.py`
**Verificador completo de la Sección 3 del estudio**

**Funcionalidades principales:**
1. **Verificación individual**: Análisis completo de cualquier número con todos los teoremas
2. **Verificación de rangos**: Verificación masiva con estadísticas detalladas
3. **Generación de grafos**: Visualización de trayectorias de convergencia
4. **Exportación CSV**: Datos para análisis posterior
5. **Números grandes**: Procesamiento especializado para n > 1,000,000

**Lo que DEMUESTRA este script:**
- TODOS los números convergen al 7 por DISEÑO, no por propiedades místicas
- La convergencia es 100% predecible y FORZADA
- Verifica formalmente todos los teoremas, lemas y proposiciones de la Sección 3
- Genera visualizaciones que muestran la artificialidad del sistema

## 🚀 Instalación Completa

### Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación paso a paso

```bash
# 1. Clonar el repositorio
git clone https://github.com/686f6c61/conjetura-falso-7.git
cd conjetura-falso-7

# 2. Crear entorno virtual (recomendado)
python3 -m venv venv

# 3. Activar entorno virtual
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r scripts/requirements.txt
```

### Dependencias

El archivo `scripts/requirements.txt` incluye solo las librerías necesarias:

| Librería | Versión Mínima | Uso en el Proyecto |
|----------|----------------|-------------------|
| `matplotlib` | ≥3.3.0 | Generación de grafos de convergencia |
| `networkx` | ≥2.5 | Visualización de trayectorias como grafos dirigidos |

## 🔬 Uso del Script Verificador

### Modo Interactivo (Menú principal)

```bash
python scripts/verificador_teorema.py
```

**Opciones del menú:**
1. Verificar convergencia de un número
2. Verificar convergencia de un rango
3. Generar grafo de trayectoria
4. Generar CSV de convergencias (rangos ≥ 100)
5. Generar CSV para números grandes (≥ 1,000,000)
0. Salir

### Verificación por línea de comandos

```bash
# Verificar un número específico
python scripts/verificador_teorema.py 1500
# Salida: 1500 → 7 en 11 pasos

# Verificar un número grande
python scripts/verificador_teorema.py 10000000
# Salida: 10000000 → 7 en 24 pasos
```

## 📊 Archivos Generados

### Grafos de Convergencia (PNG)
- **Ejemplo**: `grafo_convergencia_1500.png`
- Visualiza la trayectoria completa de n₀ → 7
- Nodos en azul claro, excepto el 7 en rojo (punto fijo)
- Incluye información del Teorema 3.1 y cotas

### Archivos CSV
- **Rangos**: `convergencias_100_200.csv`
  - Columnas: n₀, k_pasos, trayectoria completa, valor_mínimo, fases, cotas
- **Números grandes**: `convergencias_grandes_3_numeros.csv`
  - Incluye primeros y últimos 10 pasos de trayectorias largas

### Archivos JSON (opcional)
- **Verificación completa**: `verificacion_seccion3_[rango]_[timestamp].json`
- Contiene validación de todos los teoremas y estadísticas agregadas

## 🎯 Ejemplos de Uso

### 1. Verificar que el 7 NO es especial

```bash
python scripts/verificador_teorema.py
# Opción 1: Ingrese cualquier número
# Verá que TODOS convergen al 7 por diseño artificial
```

### 2. Generar grafo de convergencia

```bash
python scripts/verificador_teorema.py
# Opción 3: Ingrese 1500
# Genera: grafo_convergencia_1500.png
```

### 3. Análisis de números grandes

```bash
python scripts/verificador_teorema.py
# Opción 5: Ingrese 10000000, 5000000, 1000000
# Genera CSV con análisis detallado
```

### 4. Verificación de rangos

```bash
python scripts/verificador_teorema.py
# Opción 2: Rango 100-200
# Verifica TODOS los números y genera estadísticas
```

## 🎓 Lección Anti-Numerológica

Este proyecto demuestra matemáticamente que:

1. **Cualquier número puede ser hecho "especial"** mediante construcción artificial
2. **La convergencia universal NO implica significado místico**
3. **La verificación formal NO otorga profundidad espiritual**
4. **El rigor matemático puede aplicarse a construcciones vacías**

## 📖 Resultados Clave

- **10,000,000** converge en 24 pasos (dentro de las cotas teóricas: 21 ≤ 24 ≤ 29)
- **100% de convergencia** para TODOS los números naturales
- **Tiempo promedio**: O(log n) pasos
- **NO hay excepciones** ni casos especiales genuinos

## 🔬 Para Escépticos y Educadores

Este material es ideal para:
- Enseñar la diferencia entre matemáticas genuinas y pseudociencia
- Demostrar cómo se puede "fabricar" significado matemático
- Ilustrar el pensamiento crítico aplicado a afirmaciones numerológicas
- Refutar con rigor matemático las pretensiones místicas sobre números

## 📖 Cita

Si usas este trabajo para educación o investigación:

```
Benítez, R. (2025). "La Fantasía del 7: Una Refutación Matemática de la Numerología". 
GitHub: https://github.com/686f6c61/conjetura-falso-7
```

## ⚖️ Licencia

MIT License - Úsalo libremente para combatir la pseudociencia.

---

**Nota final:** Este proyecto prueba que podemos hacer que CUALQUIER número parezca "especial" con las reglas adecuadas. La "magia" del 7 es tan real como decidamos fabricarla matemáticamente.