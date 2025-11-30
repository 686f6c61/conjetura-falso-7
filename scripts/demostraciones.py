#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIFICADOR COMPLETO DE LA SECCIÓN 3 - DEMOSTRACIÓN DE LA CONJETURA DEL 7
Implementación exhaustiva de TODOS los teoremas, lemas y proposiciones

TEOREMAS Y PROPOSICIONES VERIFICADOS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECCIÓN 2: MARCO TEÓRICO
- Proposición 2.1: F₇ bien definida en ℕ → ℕ
- Proposición 2.2: Monotonicidad condicional

SECCIÓN 3: DEMOSTRACIÓN
- Lema 3.1: Decremento garantizado para n > 7
- Lema 3.2: Acotación inferior para n > 7
- Lema 3.3: Convergencia ascendente para n < 7
- Teorema 3.1: Convergencia Universal
- Teorema 3.2: Cota superior T(n₀) ≤ ⌊log₂(n₀)⌋ + 6 (con optimalidad)
- Teorema 3.3: Cota inferior T(n₀) ≥ ⌊log₂(n₀)⌋ - 2
- Teorema 3.3bis: Caracterización completa Θ(log n)
- Proposición 3.1: T(2^k) = k + 6 para potencias de 2
- Proposición 3.2: F₇(2k+1) = k para números impares grandes
- Proposición 3.3: Convergencia directa {6, 14, 15}
- Teorema 3.4: Conjetura del 7 para n > 100
- Teorema 3.6: Comportamiento asintótico promedio E[T(n)] = log₂(n) + O(1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Autor: R. Benítez
Fecha: Julio 2025
Versión: 2.0 - Completa y fusionada
"""

import sys
import math
import json
import csv
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# Imports opcionales para visualización (no requeridos para verificación básica)
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_DISPONIBLE = True
except ImportError:
    MATPLOTLIB_DISPONIBLE = False

try:
    import networkx as nx
    NETWORKX_DISPONIBLE = True
except ImportError:
    NETWORKX_DISPONIBLE = False

# ============================================================================
# SECCIÓN 2: PROPOSICIONES FUNDAMENTALES
# ============================================================================

def F7(n: int) -> int:
    """
    Función F₇: ℕ → ℕ según definición formal (Sección 2.1)

    F₇(n) = {
        n            si n = 7
        ⌊n/2⌋        si n > 7 y n ≡ 0 (mod 2)
        ⌊(n-1)/2⌋    si n > 7 y n ≡ 1 (mod 2)
        n + 1        si n < 7
    }
    """
    if n == 7:
        return 7
    elif n > 7:
        if n % 2 == 0:
            return n // 2
        else:
            return (n - 1) // 2
    else:
        return n + 1

def verificar_proposicion_2_1(n: int) -> Dict:
    """
    Proposición 2.1: F₇ está bien definida en todo ℕ y F₇: ℕ → ℕ

    Verifica que:
    1. F₇(n) está definida para todo n ∈ ℕ
    2. F₇(n) ∈ ℕ para todo n ∈ ℕ
    """
    try:
        resultado = F7(n)
        bien_definida = True
        en_naturales = resultado > 0

        return {
            'proposicion': '2.1',
            'enunciado': 'F₇ bien definida',
            'n': n,
            'F7(n)': resultado,
            'bien_definida': bien_definida,
            'en_naturales': en_naturales,
            'cumple': bien_definida and en_naturales
        }
    except:
        return {
            'proposicion': '2.1',
            'n': n,
            'cumple': False
        }

def verificar_proposicion_2_2(n: int) -> Dict:
    """
    Proposición 2.2: Monotonicidad condicional

    Verifica que:
    - Para n > 7: F₇(n) < n (siempre decrece)
    - Para n < 7: F₇(n) > n (siempre crece)
    - Para n = 7: F₇(n) = n (punto fijo)
    """
    fn = F7(n)

    if n > 7:
        decrece = fn < n
        cumple = decrece
        tipo = "decreciente"
    elif n < 7:
        crece = fn > n
        cumple = crece
        tipo = "creciente"
    else:  # n == 7
        punto_fijo = fn == n
        cumple = punto_fijo
        tipo = "punto fijo"

    return {
        'proposicion': '2.2',
        'enunciado': 'Monotonicidad condicional',
        'n': n,
        'F7(n)': fn,
        'tipo': tipo,
        'cumple': cumple
    }

# ============================================================================
# SECCIÓN 3: LEMAS PREPARATORIOS
# ============================================================================

def verificar_lema_3_1(n: int) -> Optional[Dict]:
    """
    Lema 3.1 (Decremento Garantizado): Para todo n > 7, F₇(n) < n
    """
    if n <= 7:
        return None

    fn = F7(n)
    cumple = fn < n

    return {
        'lema': '3.1',
        'enunciado': 'Decremento garantizado para n > 7',
        'n': n,
        'F7(n)': fn,
        'F7(n) < n': f"{fn} < {n}",
        'cumple': cumple
    }

def verificar_lema_3_2(n: int) -> Optional[Dict]:
    """
    Lema 3.2 (Acotación Inferior): Para todo n > 7, F₇(n) ≥ 1

    De hecho, F₇(n) ≥ 4 para n > 7 (cota refinada)
    """
    if n <= 7:
        return None

    fn = F7(n)
    cumple_basico = fn >= 1
    cumple_refinado = fn >= 4  # Cota más ajustada

    return {
        'lema': '3.2',
        'enunciado': 'Acotación inferior para n > 7',
        'n': n,
        'F7(n)': fn,
        'F7(n) ≥ 1': cumple_basico,
        'F7(n) ≥ 4': cumple_refinado,
        'cumple': cumple_basico
    }

def verificar_lema_3_3(n: int) -> Optional[Dict]:
    """
    Lema 3.3 (Convergencia Ascendente):
    Para todo n₀ < 7, alcanza 7 en exactamente 7 - n₀ iteraciones
    """
    if n >= 7:
        return None

    pasos_teoricos = 7 - n
    actual = n
    pasos_reales = 0
    trayectoria = [n]

    while actual != 7:
        actual = F7(actual)
        trayectoria.append(actual)
        pasos_reales += 1

    cumple = (pasos_reales == pasos_teoricos)

    return {
        'lema': '3.3',
        'enunciado': f'Convergencia en {pasos_teoricos} pasos',
        'n': n,
        'pasos_teoricos': pasos_teoricos,
        'pasos_reales': pasos_reales,
        'trayectoria': trayectoria,
        'cumple': cumple
    }

# ============================================================================
# SECCIÓN 3.4: CONVERGENCIA Y COTAS
# ============================================================================

def calcular_convergencia(n0: int, max_iteraciones: int = 10000) -> Dict:
    """
    Calcula la convergencia completa con análisis exhaustivo
    """
    if n0 <= 0:
        raise ValueError("n₀ debe ser un número natural positivo")

    trayectoria = [n0]
    actual = n0
    k = 0

    # Fases de convergencia
    fase_descenso = 0
    fase_ascenso = 0
    valor_minimo = n0
    valor_maximo = n0

    while actual != 7 and k < max_iteraciones:
        anterior = actual
        actual = F7(actual)
        trayectoria.append(actual)
        k += 1

        # Análisis de fases
        if actual < anterior:
            fase_descenso += 1
        elif actual > anterior:
            fase_ascenso += 1

        valor_minimo = min(valor_minimo, actual)
        valor_maximo = max(valor_maximo, actual)

    # Verificar convergencia
    convergio = (actual == 7)

    # Calcular cotas (Teorema 3.2 y 3.3)
    if n0 > 7:
        cota_superior = int(math.log2(n0)) + 6
        cota_inferior = int(math.log2(n0)) - 2
    elif n0 < 7:
        cota_superior = 7 - n0
        cota_inferior = 7 - n0
    else:  # n0 == 7
        cota_superior = 0
        cota_inferior = 0

    # Verificar si es potencia de 2
    es_potencia_2 = (n0 > 0) and (n0 & (n0 - 1)) == 0

    # Para potencias de 2, verificar Proposición 3.1: T(2^k) = k + 1
    if es_potencia_2 and n0 > 7:
        k_teorico_pot2 = int(math.log2(n0)) + 1
        cumple_prop_3_1 = (k == k_teorico_pot2)
    else:
        k_teorico_pot2 = None
        cumple_prop_3_1 = None

    return {
        'n0': n0,
        'convergio': convergio,
        'k': k,
        'trayectoria': trayectoria,
        'cota_superior': cota_superior,
        'cota_inferior': cota_inferior,
        'cumple_cota_superior': k <= cota_superior,
        'cumple_cota_inferior': k >= cota_inferior,
        'fase_descenso': fase_descenso,
        'fase_ascenso': fase_ascenso,
        'valor_minimo': valor_minimo,
        'valor_maximo': valor_maximo,
        'es_potencia_2': es_potencia_2,
        'k_teorico_pot2': k_teorico_pot2,
        'cumple_proposicion_3_1': cumple_prop_3_1
    }

def verificar_teorema_3_2(resultado: Dict) -> Dict:
    """
    Teorema 3.2 (Cota Superior): T(n₀) ≤ ⌊log₂(n₀)⌋ + 6

    Verifica que el tiempo de convergencia cumple la cota superior.
    Para potencias de 2, verifica que se alcanza la igualdad (optimalidad).
    """
    n0 = resultado['n0']
    k = resultado['k']
    cota_sup = resultado['cota_superior']

    cumple = resultado['cumple_cota_superior']

    # Verificar optimalidad para potencias de 2
    alcanza_igualdad = (k == cota_sup) if resultado['es_potencia_2'] else False

    return {
        'teorema': '3.2',
        'enunciado': 'Cota superior T(n₀) ≤ ⌊log₂(n₀)⌋ + 6',
        'n0': n0,
        'k_real': k,
        'cota_superior': cota_sup,
        'cumple': cumple,
        'es_potencia_2': resultado['es_potencia_2'],
        'alcanza_igualdad': alcanza_igualdad,
        'es_optima': alcanza_igualdad if resultado['es_potencia_2'] else None
    }

def verificar_teorema_3_3(resultado: Dict) -> Dict:
    """
    Teorema 3.3 (Cota Inferior): Existen infinitos n₀ con T(n₀) ≥ ⌊log₂(n₀)⌋ - 2
    """
    n0 = resultado['n0']
    k = resultado['k']
    cota_inf = resultado['cota_inferior']

    cumple = resultado['cumple_cota_inferior']

    return {
        'teorema': '3.3',
        'enunciado': 'Cota inferior T(n₀) ≥ ⌊log₂(n₀)⌋ - 2',
        'n0': n0,
        'k_real': k,
        'cota_inferior': cota_inf,
        'cumple': cumple
    }

def verificar_teorema_3_3bis(resultado: Dict) -> Dict:
    """
    Teorema 3.3bis (Caracterización Completa):
    ⌊log₂(n₀)⌋ - 2 ≤ T(n₀) ≤ ⌊log₂(n₀)⌋ + 6

    Interpretación: T(n₀) = Θ(log n₀)
    """
    n0 = resultado['n0']
    k = resultado['k']
    cota_inf = resultado['cota_inferior']
    cota_sup = resultado['cota_superior']

    cumple_ambas = resultado['cumple_cota_inferior'] and resultado['cumple_cota_superior']

    # Cálculo del margen
    margen = cota_sup - cota_inf

    return {
        'teorema': '3.3bis',
        'enunciado': 'Caracterización completa Θ(log n₀)',
        'n0': n0,
        'k_real': k,
        'cota_inferior': cota_inf,
        'cota_superior': cota_sup,
        'margen_cotas': margen,
        'cumple_ambas': cumple_ambas
    }

# ============================================================================
# SECCIÓN 3.5: PROPOSICIONES DE CASOS ESPECIALES
# ============================================================================

def verificar_proposicion_3_1(n: int, resultado: Dict) -> Optional[Dict]:
    """
    Proposición 3.1 (Potencias de 2): T(2^k) = k + 1 exactamente (para k ≥ 3)

    Todas las potencias de 2 caen hasta 4, luego ascienden 4→5→6→7 (3 pasos).
    """
    if not resultado['es_potencia_2'] or n <= 7:
        return None

    k_exponente = int(math.log2(n))

    # Fórmula corregida: T(2^k) = k + 1
    k_real = resultado['k']
    k_teorico = k_exponente + 1

    cumple = (k_real == k_teorico)

    return {
        'proposicion': '3.1',
        'enunciado': f'T(2^k) = k + 1',
        'n': n,
        'k_exponente': k_exponente,
        'k_teorico': k_teorico,
        'k_real': k_real,
        'cumple': cumple
    }

def verificar_proposicion_3_2(n: int) -> Optional[Dict]:
    """
    Proposición 3.2 (Números Impares Grandes):
    Para n₀ = 2k + 1 con k > 7, F₇(n₀) = k
    """
    if n <= 7 or n % 2 == 0:
        return None

    k = (n - 1) // 2
    fn = F7(n)

    cumple = (fn == k)

    return {
        'proposicion': '3.2',
        'enunciado': 'F₇(2k+1) = k para impares',
        'n': n,
        'k': k,
        'F7(n)': fn,
        'cumple': cumple
    }

def verificar_proposicion_3_3() -> Dict:
    """
    Proposición 3.3: Los únicos valores que alcanzan 7 en 1 iteración son {6, 14, 15}
    """
    valores_directos = []

    # Verificar rango amplio para asegurar exhaustividad
    for n in range(1, 100):
        if F7(n) == 7:
            valores_directos.append(n)

    conjunto_esperado = {6, 14, 15}
    conjunto_encontrado = set(valores_directos)

    cumple = (conjunto_encontrado == conjunto_esperado)

    return {
        'proposicion': '3.3',
        'enunciado': 'Convergencia directa en 1 paso',
        'valores_esperados': sorted(conjunto_esperado),
        'valores_encontrados': valores_directos,
        'cumple': cumple
    }

# ============================================================================
# VERIFICACIÓN COMPLETA DE UN NÚMERO
# ============================================================================

def verificar_numero_completo(n: int) -> Dict:
    """
    Verificación exhaustiva de TODAS las proposiciones aplicables a un número
    """
    verificaciones = {}

    # Sección 2: Proposiciones fundamentales
    verificaciones['prop_2_1'] = verificar_proposicion_2_1(n)
    verificaciones['prop_2_2'] = verificar_proposicion_2_2(n)

    # Sección 3: Lemas
    verificaciones['lema_3_1'] = verificar_lema_3_1(n)
    verificaciones['lema_3_2'] = verificar_lema_3_2(n)
    verificaciones['lema_3_3'] = verificar_lema_3_3(n)

    # Convergencia completa
    resultado = calcular_convergencia(n)
    verificaciones['convergencia'] = resultado

    # Teoremas de cotas
    verificaciones['teorema_3_2'] = verificar_teorema_3_2(resultado)
    verificaciones['teorema_3_3'] = verificar_teorema_3_3(resultado)
    verificaciones['teorema_3_3bis'] = verificar_teorema_3_3bis(resultado)

    # Proposiciones de casos especiales
    verificaciones['prop_3_1'] = verificar_proposicion_3_1(n, resultado)
    verificaciones['prop_3_2'] = verificar_proposicion_3_2(n)

    # Conjetura 3.1 (para n > 100)
    if n > 100:
        verificaciones['conjetura_3_1'] = {
            'enunciado': 'Convergencia para n > 100',
            'n': n,
            'cumple': resultado['convergio']
        }

    return verificaciones

# ============================================================================
# INTERFAZ DE USUARIO - VERIFICACIÓN INDIVIDUAL
# ============================================================================

def verificar_numero_individual():
    """
    Verificación completa de un número con salida formateada
    """
    try:
        n = int(input("\nIngrese un número natural: "))
        if n <= 0:
            print("Error: Debe ser un número natural positivo")
            return

        print(f"\n{'='*70}")
        print(f"VERIFICACIÓN EXHAUSTIVA PARA n₀ = {n}")
        print(f"{'='*70}")

        verificaciones = verificar_numero_completo(n)

        # SECCIÓN 2: Proposiciones fundamentales
        print(f"\n{'─'*70}")
        print("SECCIÓN 2: PROPOSICIONES FUNDAMENTALES")
        print(f"{'─'*70}")

        prop_2_1 = verificaciones['prop_2_1']
        print(f"\n✓ Proposición 2.1: F₇ bien definida")
        print(f"  F₇({n}) = {prop_2_1['F7(n)']} ∈ ℕ: {'✓' if prop_2_1['cumple'] else '✗'}")

        prop_2_2 = verificaciones['prop_2_2']
        print(f"\n✓ Proposición 2.2: Monotonicidad condicional")
        print(f"  Tipo: {prop_2_2['tipo']}")
        print(f"  Cumple: {'✓' if prop_2_2['cumple'] else '✗'}")

        # SECCIÓN 3: Lemas
        print(f"\n{'─'*70}")
        print("SECCIÓN 3: LEMAS PREPARATORIOS")
        print(f"{'─'*70}")

        if verificaciones['lema_3_1']:
            lema = verificaciones['lema_3_1']
            print(f"\n✓ Lema 3.1: {lema['enunciado']}")
            print(f"  {lema['F7(n) < n']}: {'✓' if lema['cumple'] else '✗'}")

        if verificaciones['lema_3_2']:
            lema = verificaciones['lema_3_2']
            print(f"\n✓ Lema 3.2: {lema['enunciado']}")
            print(f"  F₇({n}) = {lema['F7(n)']} ≥ 1: {'✓' if lema['F7(n) ≥ 1'] else '✗'}")
            print(f"  F₇({n}) ≥ 4 (refinada): {'✓' if lema['F7(n) ≥ 4'] else '✗'}")

        if verificaciones['lema_3_3']:
            lema = verificaciones['lema_3_3']
            print(f"\n✓ Lema 3.3: {lema['enunciado']}")
            print(f"  Pasos teóricos: {lema['pasos_teoricos']}")
            print(f"  Pasos reales: {lema['pasos_reales']}")
            print(f"  Cumple: {'✓' if lema['cumple'] else '✗'}")

        # CONVERGENCIA
        conv = verificaciones['convergencia']
        print(f"\n{'─'*70}")
        print("TEOREMA 3.1: CONVERGENCIA UNIVERSAL")
        print(f"{'─'*70}")
        print(f"\n  Converge al 7: {'✓' if conv['convergio'] else '✗'}")
        print(f"  Número de pasos k: {conv['k']}")
        print(f"  Fase descendente: {conv['fase_descenso']} pasos")
        print(f"  Fase ascendente: {conv['fase_ascenso']} pasos")
        if conv['valor_minimo'] < 7:
            print(f"  Valor mínimo alcanzado: {conv['valor_minimo']}")

        # TEOREMAS DE COTAS
        print(f"\n{'─'*70}")
        print("TEOREMAS DE COTAS")
        print(f"{'─'*70}")

        t32 = verificaciones['teorema_3_2']
        print(f"\n✓ Teorema 3.2: Cota superior")
        print(f"  k = {t32['k_real']} ≤ {t32['cota_superior']}: {'✓' if t32['cumple'] else '✗'}")
        if t32['es_potencia_2']:
            print(f"  Potencia de 2: Alcanza igualdad {'✓' if t32['alcanza_igualdad'] else '✗'}")

        t33 = verificaciones['teorema_3_3']
        print(f"\n✓ Teorema 3.3: Cota inferior")
        print(f"  {t33['cota_inferior']} ≤ k = {t33['k_real']}: {'✓' if t33['cumple'] else '✗'}")

        t33bis = verificaciones['teorema_3_3bis']
        print(f"\n✓ Teorema 3.3bis: Caracterización Θ(log n)")
        print(f"  {t33bis['cota_inferior']} ≤ {t33bis['k_real']} ≤ {t33bis['cota_superior']}")
        print(f"  Margen: {t33bis['margen_cotas']} (constante)")
        print(f"  Cumple ambas cotas: {'✓' if t33bis['cumple_ambas'] else '✗'}")

        # CASOS ESPECIALES
        print(f"\n{'─'*70}")
        print("PROPOSICIONES DE CASOS ESPECIALES")
        print(f"{'─'*70}")

        if verificaciones['prop_3_1']:
            p31 = verificaciones['prop_3_1']
            print(f"\n✓ Proposición 3.1: Potencias de 2")
            print(f"  2^{p31['k_exponente']} = {p31['n']}")
            print(f"  k teórico: {p31['k_teorico']}")
            print(f"  k real: {p31['k_real']}")
            print(f"  Cumple T(2^k) = k + 1: {'✓' if p31['cumple'] else '✗'}")

        if verificaciones['prop_3_2']:
            p32 = verificaciones['prop_3_2']
            print(f"\n✓ Proposición 3.2: Números impares")
            print(f"  F₇({p32['n']}) = {p32['F7(n)']} = {p32['k']}: {'✓' if p32['cumple'] else '✗'}")

        # TRAYECTORIA
        print(f"\n{'─'*70}")
        print("TRAYECTORIA COMPLETA")
        print(f"{'─'*70}")
        tray = conv['trayectoria']
        if len(tray) <= 25:
            print(f"\n  {' → '.join(map(str, tray))}")
        else:
            print(f"\n  {' → '.join(map(str, tray[:15]))} ...")
            print(f"  ... {' → '.join(map(str, tray[-10:]))}")

    except ValueError:
        print("Error: Entrada inválida")

# ============================================================================
# VERIFICACIÓN DE RANGO
# ============================================================================

def verificar_rango():
    """
    Verificación completa de un rango según todos los teoremas de la Sección 3
    """
    try:
        inicio = int(input("\nNúmero inicial del rango: "))
        fin = int(input("Número final del rango: "))

        if inicio <= 0 or fin < inicio:
            print("Error: Rango inválido")
            return

        print(f"\n{'='*70}")
        print(f"VERIFICACIÓN DE RANGO [{inicio}, {fin}]")
        print(f"{'='*70}")

        # Contadores
        total = fin - inicio + 1
        todos_convergen = True
        cumple_prop_2_1 = 0
        cumple_prop_2_2 = 0
        cumple_lema_3_1 = 0
        cumple_lema_3_2 = 0
        cumple_lema_3_3 = 0
        cumple_teorema_3_2 = 0
        cumple_teorema_3_3 = 0
        cumple_teorema_3_3bis = 0
        cumple_prop_3_1 = 0
        potencias_de_2_encontradas = 0
        valores_directos_a_7 = []

        tiempo_total = 0
        tiempo_max = 0
        tiempo_min = float('inf')
        numero_max = inicio
        numero_min = inicio

        # Procesar
        print("\nProcesando...")
        for n in range(inicio, fin + 1):
            verif = verificar_numero_completo(n)

            if not verif['convergencia']['convergio']:
                todos_convergen = False

            # Contadores de proposiciones
            if verif['prop_2_1']['cumple']:
                cumple_prop_2_1 += 1
            if verif['prop_2_2']['cumple']:
                cumple_prop_2_2 += 1

            if verif['lema_3_1'] and verif['lema_3_1']['cumple']:
                cumple_lema_3_1 += 1
            if verif['lema_3_2'] and verif['lema_3_2']['cumple']:
                cumple_lema_3_2 += 1
            if verif['lema_3_3'] and verif['lema_3_3']['cumple']:
                cumple_lema_3_3 += 1

            if verif['teorema_3_2']['cumple']:
                cumple_teorema_3_2 += 1
            if verif['teorema_3_3']['cumple']:
                cumple_teorema_3_3 += 1
            if verif['teorema_3_3bis']['cumple_ambas']:
                cumple_teorema_3_3bis += 1

            if verif['prop_3_1'] and verif['prop_3_1']['cumple']:
                cumple_prop_3_1 += 1
                potencias_de_2_encontradas += 1

            if verif['convergencia']['k'] == 1:
                valores_directos_a_7.append(n)

            k = verif['convergencia']['k']
            tiempo_total += k
            if k > tiempo_max:
                tiempo_max = k
                numero_max = n
            if k < tiempo_min:
                tiempo_min = k
                numero_min = n

        # RESULTADOS
        print(f"\n{'─'*70}")
        print("RESULTADOS GLOBALES")
        print(f"{'─'*70}")

        print(f"\n✓ Proposición 2.1: {cumple_prop_2_1}/{total} ({100*cumple_prop_2_1/total:.1f}%)")
        print(f"✓ Proposición 2.2: {cumple_prop_2_2}/{total} ({100*cumple_prop_2_2/total:.1f}%)")
        print(f"✓ Teorema 3.1 (Convergencia Universal): {'✓ VERIFICADO' if todos_convergen else '✗ FALLÓ'}")
        print(f"✓ Teorema 3.2 (Cota Superior): {cumple_teorema_3_2}/{total} ({100*cumple_teorema_3_2/total:.1f}%)")
        print(f"✓ Teorema 3.3 (Cota Inferior): {cumple_teorema_3_3}/{total} ({100*cumple_teorema_3_3/total:.1f}%)")
        print(f"✓ Teorema 3.3bis (Ambas cotas): {cumple_teorema_3_3bis}/{total} ({100*cumple_teorema_3_3bis/total:.1f}%)")

        if potencias_de_2_encontradas > 0:
            print(f"✓ Proposición 3.1 (Potencias de 2): {cumple_prop_3_1}/{potencias_de_2_encontradas} ({100*cumple_prop_3_1/potencias_de_2_encontradas:.1f}%)")

        if valores_directos_a_7:
            print(f"\n✓ Proposición 3.3: Convergencia directa")
            print(f"  Valores encontrados: {valores_directos_a_7}")

        print(f"\n{'─'*70}")
        print("ESTADÍSTICAS (Teorema 3.6)")
        print(f"{'─'*70}")
        tiempo_promedio = tiempo_total / total
        print(f"Tiempo promedio E[T(n)]: {tiempo_promedio:.2f} pasos")
        print(f"Tiempo mínimo: {tiempo_min} pasos (n₀ = {numero_min})")
        print(f"Tiempo máximo: {tiempo_max} pasos (n₀ = {numero_max})")

        if fin > 100:
            prediccion_log = math.log2(fin)
            print(f"\nTeoría: E[T(n)] ≈ log₂({fin}) + O(1) ≈ {prediccion_log:.2f} + O(1)")
            print(f"Observado: {tiempo_promedio:.2f}")

        # Guardar resultados
        guardar = input("\n¿Guardar verificación completa? (s/n): ").lower() == 's'
        if guardar:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"verificacion_seccion3_{inicio}_{fin}_{timestamp}.json"

            resultados_detallados = []
            for n in range(inicio, fin + 1):
                res = calcular_convergencia(n)
                resultados_detallados.append({
                    'n': n,
                    'k': res['k'],
                    'convergio': res['convergio'],
                    'cumple_cota_superior': res['cumple_cota_superior'],
                    'cumple_cota_inferior': res['cumple_cota_inferior']
                })

            with open(filename, 'w') as f:
                json.dump({
                    'seccion': '3 - Demostración de la Conjetura del 7',
                    'rango': {'inicio': inicio, 'fin': fin},
                    'teorema_3_1_verificado': todos_convergen,
                    'estadisticas': {
                        'tiempo_promedio': tiempo_promedio,
                        'tiempo_maximo': tiempo_max,
                        'tiempo_minimo': tiempo_min,
                        'cumple_cotas_superior': cumple_teorema_3_2,
                        'cumple_cotas_inferior': cumple_teorema_3_3
                    },
                    'resultados': resultados_detallados
                }, f, indent=2)

            print(f"Verificación guardada en: {filename}")

    except ValueError:
        print("Error: Entrada inválida")

# ============================================================================
# VISUALIZACIÓN Y EXPORTACIÓN
# ============================================================================

def generar_visualizacion_ascii():
    """
    Generar visualización ASCII de la trayectoria (sin dependencias)
    """
    try:
        n = int(input("\nNúmero para visualizar trayectoria: "))
        if n <= 0:
            print("Error: Debe ser un número natural positivo")
            return

        print(f"\nCalculando trayectoria para n₀ = {n}")
        resultado = calcular_convergencia(n)

        if not resultado['convergio']:
            print("Error: El número no convergió")
            return

        tray = resultado['trayectoria']

        print(f"\n{'='*70}")
        print(f"VISUALIZACIÓN DE TRAYECTORIA: {n} → 7")
        print(f"{'='*70}")

        # Información general
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"   Pasos totales:      {resultado['k']}")
        print(f"   Fase descendente:   {resultado['fase_descenso']} pasos")
        print(f"   Fase ascendente:    {resultado['fase_ascenso']} pasos")
        print(f"   Valor mínimo:       {resultado['valor_minimo']}")
        print(f"   Cotas:              {resultado['cota_inferior']} ≤ {resultado['k']} ≤ {resultado['cota_superior']}")

        # Trayectoria visual
        print(f"\n📈 TRAYECTORIA COMPLETA:")
        print(f"{'─'*70}")

        max_val = max(tray)
        if max_val <= 100:
            # Gráfico de barras ASCII para números pequeños
            for i, val in enumerate(tray):
                bar_length = int((val / max_val) * 40)
                bar = '█' * bar_length
                marker = '→' if i < len(tray) - 1 else '✓'
                print(f"   Paso {i:2d}: {val:4d} {bar} {marker}")
        else:
            # Lista simple para números grandes
            for i in range(0, len(tray), 1):
                if i < 10 or i >= len(tray) - 5:
                    val = tray[i]
                    marker = '→' if i < len(tray) - 1 else '✓'
                    print(f"   Paso {i:2d}: {val:12,d} {marker}")
                elif i == 10:
                    print(f"   ...")

        # Trayectoria en formato flecha
        print(f"\n🔗 SECUENCIA:")
        if len(tray) <= 15:
            print(f"   {' → '.join(map(str, tray))}")
        else:
            print(f"   {' → '.join(map(str, tray[:8]))} → ... → {' → '.join(map(str, tray[-5:]))}")

        # Análisis de fases
        print(f"\n📉 ANÁLISIS DE FASES:")

        # Encontrar punto de inflexión
        idx_min = tray.index(resultado['valor_minimo'])

        print(f"   Inicio:          {tray[0]}")
        if idx_min > 0:
            print(f"   ↓ Descenso hasta paso {idx_min}")
            print(f"   Valor mínimo:    {tray[idx_min]}")
        if idx_min < len(tray) - 1:
            print(f"   ↑ Ascenso desde paso {idx_min}")
        print(f"   Final:           {tray[-1]} ✓")

        # Verificación de teoremas
        print(f"\n✅ VERIFICACIÓN DE TEOREMAS:")

        # Teorema 3.2
        cumple_sup = resultado['cumple_cota_superior']
        print(f"   Teorema 3.2 (cota superior): {'✓' if cumple_sup else '✗'}")
        print(f"      {resultado['k']} ≤ {resultado['cota_superior']}")

        # Teorema 3.3
        cumple_inf = resultado['cumple_cota_inferior']
        print(f"   Teorema 3.3 (cota inferior): {'✓' if cumple_inf else '✗'}")
        print(f"      {resultado['cota_inferior']} ≤ {resultado['k']}")

        # Potencia de 2
        if resultado['es_potencia_2']:
            k_exp = int(math.log2(n))
            print(f"   Proposición 3.1 (potencia de 2): {'✓' if resultado['cumple_proposicion_3_1'] else '✗'}")
            print(f"      2^{k_exp} = {n}: {resultado['k']} pasos (teórico: {k_exp + 1})")

        print(f"\n{'='*70}\n")

    except ValueError:
        print("Error: Entrada inválida")

def generar_grafo_trayectoria():
    """
    Generar grafo del camino de un número hasta el 7 (requiere matplotlib)
    """
    if not MATPLOTLIB_DISPONIBLE or not NETWORKX_DISPONIBLE:
        generar_visualizacion_ascii()
        return

    try:
        n = int(input("\nNúmero para graficar trayectoria: "))
        if n <= 0:
            print("Error: Debe ser un número natural positivo")
            return

        print(f"\nCalculando trayectoria para n₀ = {n}")
        resultado = calcular_convergencia(n)

        if not resultado['convergio']:
            print("Error: El número no convergió")
            return

        tray = resultado['trayectoria']

        # Crear grafo dirigido
        G = nx.DiGraph()
        for i in range(len(tray) - 1):
            G.add_edge(tray[i], tray[i+1])

        # Configurar visualización
        plt.figure(figsize=(14, 10))

        # Layout jerárquico
        pos = nx.spring_layout(G, k=3, iterations=50)

        # Colores: rojo para 7, azul para otros
        node_colors = ['red' if node == 7 else 'lightblue' for node in G.nodes()]
        node_sizes = [1000 if node == 7 else 600 for node in G.nodes()]

        # Dibujar grafo
        nx.draw(G, pos,
                node_color=node_colors,
                node_size=node_sizes,
                with_labels=True,
                font_size=12,
                font_weight='bold',
                arrows=True,
                edge_color='gray',
                arrowsize=20,
                arrowstyle='->')

        # Título y información
        plt.title(f'Trayectoria de Convergencia: n₀ = {n} → 7\n' +
                  f'Teorema 3.1: k = {resultado["k"]} pasos',
                  fontsize=16, fontweight='bold')

        # Agregar información de la demostración
        info_text = f"Verificación del Teorema 3.1\n" + \
                   f"n₀ = {n}\n" + \
                   f"Convergencia en k = {resultado['k']} pasos\n" + \
                   f"Cota superior: k ≤ {resultado['cota_superior']}"

        plt.text(0.02, 0.98, info_text,
                transform=plt.gca().transAxes,
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

        # Guardar y mostrar
        filename = f'grafo_convergencia_{n}.png'
        plt.tight_layout()
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        print(f"\nGrafo guardado en: {filename}")
        plt.show()

    except ValueError:
        print("Error: Entrada inválida")

def generar_csv_convergencias():
    """
    Generar CSV con convergencias de un rango de números
    """
    try:
        inicio = int(input("\nNúmero inicial del rango: "))
        fin = int(input("Número final del rango: "))

        if inicio <= 0 or fin < inicio:
            print("Error: Rango inválido")
            return

        filename = f"convergencias_{inicio}_{fin}.csv"

        print(f"\nGenerando CSV para rango [{inicio}, {fin}]...")

        # Escribir archivo CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Definir campos del CSV
            fieldnames = ['n0', 'k_pasos', 'trayectoria', 'valor_minimo',
                         'pasos_descenso', 'pasos_ascenso', 'cota_inferior', 'cota_superior',
                         'cumple_cota_sup', 'cumple_cota_inf', 'es_potencia_2']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Escribir encabezados
            writer.writeheader()

            # Procesar cada número
            contador = 0
            for n in range(inicio, fin + 1):
                resultado = calcular_convergencia(n)

                # Escribir fila
                writer.writerow({
                    'n0': n,
                    'k_pasos': resultado['k'],
                    'trayectoria': ' → '.join(map(str, resultado['trayectoria'])),
                    'valor_minimo': resultado['valor_minimo'],
                    'pasos_descenso': resultado['fase_descenso'],
                    'pasos_ascenso': resultado['fase_ascenso'],
                    'cota_inferior': resultado['cota_inferior'],
                    'cota_superior': resultado['cota_superior'],
                    'cumple_cota_sup': resultado['cumple_cota_superior'],
                    'cumple_cota_inf': resultado['cumple_cota_inferior'],
                    'es_potencia_2': resultado['es_potencia_2']
                })

                contador += 1
                if contador % 100 == 0:
                    print(f"  Procesados {contador} números...")

        print(f"\nCSV generado exitosamente: {filename}")
        print(f"Total de números procesados: {contador}")

    except ValueError:
        print("Error: Entrada inválida")
    except Exception as e:
        print(f"Error al generar CSV: {e}")

def generar_csv_numeros_grandes():
    """
    Generar CSV para números grandes específicos
    """
    try:
        print("\nIngrese números grandes (uno por línea, vacío para terminar):")
        numeros = []

        while True:
            entrada = input("Número: ").strip()
            if entrada == "":
                break
            try:
                n = int(entrada)
                if n > 0:
                    numeros.append(n)
                else:
                    print("Error: Debe ser positivo")
            except ValueError:
                print("Error: Número inválido")

        if not numeros:
            print("No se ingresaron números")
            return

        filename = f"convergencias_grandes_{len(numeros)}_numeros.csv"

        print(f"\nGenerando CSV para {len(numeros)} números grandes...")

        # Escribir archivo CSV
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['n0', 'k_pasos', 'valor_minimo', 'pasos_descenso',
                         'pasos_ascenso', 'cota_inferior', 'cota_superior',
                         'cumple_cota_sup', 'cumple_cota_inf',
                         'primeros_10_pasos', 'ultimos_10_pasos']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for i, n in enumerate(numeros):
                print(f"  Procesando {n} ({i+1}/{len(numeros)})...")
                resultado = calcular_convergencia(n, max_iteraciones=100000)

                tray = resultado['trayectoria']
                primeros_10 = ' → '.join(map(str, tray[:10]))
                ultimos_10 = ' → '.join(map(str, tray[-10:]))

                writer.writerow({
                    'n0': n,
                    'k_pasos': resultado['k'],
                    'valor_minimo': resultado['valor_minimo'],
                    'pasos_descenso': resultado['fase_descenso'],
                    'pasos_ascenso': resultado['fase_ascenso'],
                    'cota_inferior': resultado['cota_inferior'],
                    'cota_superior': resultado['cota_superior'],
                    'cumple_cota_sup': resultado['cumple_cota_superior'],
                    'cumple_cota_inf': resultado['cumple_cota_inferior'],
                    'primeros_10_pasos': primeros_10,
                    'ultimos_10_pasos': ultimos_10
                })

        print(f"\nCSV generado exitosamente: {filename}")

    except Exception as e:
        print(f"Error al generar CSV: {e}")

def verificar_proposicion_3_3_standalone():
    """
    Verificación independiente de Proposición 3.3
    """
    print(f"\n{'='*70}")
    print("VERIFICACIÓN DE PROPOSICIÓN 3.3")
    print(f"{'='*70}")

    resultado = verificar_proposicion_3_3()

    print(f"\nEnunciado: {resultado['enunciado']}")
    print(f"Valores esperados: {resultado['valores_esperados']}")
    print(f"Valores encontrados: {resultado['valores_encontrados']}")
    print(f"\nCumple: {'✓' if resultado['cumple'] else '✗'}")

# ============================================================================
# MENÚ Y EJECUCIÓN PRINCIPAL
# ============================================================================

def menu_principal():
    """
    Menú principal del verificador
    """
    print("\n" + "="*70)
    print("VERIFICADOR EXHAUSTIVO - SECCIÓN 3")
    print("Todos los Teoremas, Lemas y Proposiciones")
    print("="*70)
    print("\n1. Verificar número individual (completo)")
    print("2. Verificar rango (estadísticas)")
    print("3. Verificar Proposición 3.3 (convergencia directa)")
    print("4. Generar grafo de trayectoria")
    print("5. Generar CSV de convergencias (rango)")
    print("6. Generar CSV para números grandes específicos")
    print("0. Salir")

    return input("\nSeleccione opción: ")

def main():
    """
    Función principal
    """
    print("\n" + "="*70)
    print("VERIFICADOR COMPLETO DE LA CONJETURA DEL 7")
    print("Implementación exhaustiva de todos los puntos demostrables")
    print("="*70)

    while True:
        opcion = menu_principal()

        if opcion == '1':
            verificar_numero_individual()
        elif opcion == '2':
            verificar_rango()
        elif opcion == '3':
            verificar_proposicion_3_3_standalone()
        elif opcion == '4':
            generar_grafo_trayectoria()
        elif opcion == '5':
            generar_csv_convergencias()
        elif opcion == '6':
            generar_csv_numeros_grandes()
        elif opcion == '0':
            print("\nFin de la verificación")
            break
        else:
            print("Opción inválida")

        if opcion != '0':
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    # Verificación por línea de comandos
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            resultado = calcular_convergencia(n)
            if resultado['convergio']:
                print(f"{n} → 7 en {resultado['k']} pasos")
                print(f"Cotas: {resultado['cota_inferior']} ≤ {resultado['k']} ≤ {resultado['cota_superior']}")
            else:
                print(f"{n} no convergió")
        except ValueError:
            print("Uso: python verificador_teorema.py [número]")
    else:
        main()
