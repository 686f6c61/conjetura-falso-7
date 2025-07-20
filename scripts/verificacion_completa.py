#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA DE VERIFICACIÓN COMPLETO - FANTASÍA DEL 7
Verificación exhaustiva de la convergencia universal

Autor: R. Benítez
Fecha: Julio 2025
"""

import time
import math
import numpy as np
from multiprocessing import Pool, cpu_count
from functools import lru_cache
import json
from datetime import datetime

@lru_cache(maxsize=10000)
def F7_cached(n):
    """Versión optimizada con caché para valores frecuentes"""
    if n == 7:
        return 7
    elif n > 7:
        return n // 2 if n % 2 == 0 else (n - 1) // 2
    else:
        return n + 1

def compute_convergence_data(n0, max_iterations=1000):
    """
    Computa datos completos de convergencia para n0
    
    Returns:
        dict: Datos completos de convergencia incluyendo métricas
    """
    trajectory = [n0]
    current = n0
    steps = 0
    decreasing_steps = 0
    increasing_steps = 0
    max_value = n0
    min_before_seven = n0 if n0 < 7 else float('inf')
    
    for i in range(max_iterations):
        if current == 7:
            break
            
        prev = current
        current = F7_cached(current)
        trajectory.append(current)
        steps += 1
        max_value = max(max_value, current)
        
        if current < prev:
            decreasing_steps += 1
        elif current > prev:
            increasing_steps += 1
            
        if current < 7:
            min_before_seven = min(min_before_seven, current)
    
    # Cálculo de cotas teóricas
    theoretical_upper = int(math.log2(n0)) + 6 if n0 > 0 else 10
    theoretical_lower = max(1, int(math.log2(n0)) - 2) if n0 > 0 else 1
    
    return {
        'initial': n0,
        'trajectory': trajectory,
        'convergence_time': steps,
        'converged': current == 7,
        'max_value': max_value,
        'min_before_seven': min_before_seven if min_before_seven != float('inf') else None,
        'decreasing_steps': decreasing_steps,
        'increasing_steps': increasing_steps,
        'trajectory_length': len(trajectory),
        'theoretical_upper': theoretical_upper,
        'theoretical_lower': theoretical_lower,
        'satisfies_upper': steps <= theoretical_upper,
        'satisfies_lower': steps >= theoretical_lower,
        'efficiency': steps / theoretical_upper if theoretical_upper > 0 else 0
    }

def analyze_chunk(chunk_data):
    """Analiza un chunk de datos (para paralelización)"""
    chunk_start, chunk_end = chunk_data
    return [compute_convergence_data(n) for n in range(chunk_start, chunk_end)]

def batch_analysis(start, end, chunk_size=1000, num_processes=None):
    """
    Análisis por lotes para rangos grandes con paralelización
    """
    if num_processes is None:
        num_processes = cpu_count()
    
    # Crear chunks
    chunks = []
    for i in range(start, end + 1, chunk_size):
        chunk_end = min(i + chunk_size, end + 1)
        chunks.append((i, chunk_end))
    
    print(f"Procesando {end - start + 1} valores en {len(chunks)} chunks...")
    print(f"Usando {num_processes} procesos paralelos")
    
    start_time = time.time()
    
    # Paralelización
    with Pool(processes=num_processes) as pool:
        results = pool.map(analyze_chunk, chunks)
    
    # Flatten results
    all_results = [item for sublist in results for item in sublist]
    
    execution_time = time.time() - start_time
    
    return all_results, execution_time

def verify_upper_bound(results):
    """Verifica la cota superior teórica"""
    violations = []
    
    for result in results:
        n0 = result['initial']
        actual_time = result['convergence_time']
        theoretical_upper = result['theoretical_upper']
        
        if actual_time > theoretical_upper:
            violations.append({
                'n0': n0,
                'actual': actual_time,
                'bound': theoretical_upper,
                'excess': actual_time - theoretical_upper
            })
    
    return violations

def generate_statistics(results):
    """Genera estadísticas completas del análisis"""
    convergence_times = [r['convergence_time'] for r in results]
    
    stats = {
        'total_tested': len(results),
        'successful_convergence': sum(1 for r in results if r['converged']),
        'success_rate': sum(1 for r in results if r['converged']) / len(results) * 100,
        'average_time': np.mean(convergence_times),
        'median_time': np.median(convergence_times),
        'std_dev': np.std(convergence_times),
        'min_time': min(convergence_times),
        'max_time': max(convergence_times),
        'q25': np.percentile(convergence_times, 25),
        'q75': np.percentile(convergence_times, 75),
        'upper_bound_violations': len(verify_upper_bound(results)),
        'lower_bound_satisfaction': sum(1 for r in results if r['satisfies_lower']) / len(results) * 100
    }
    
    return stats

def run_complete_verification(start=101, end=10000, save_results=True):
    """
    Ejecuta verificación completa y guarda resultados
    """
    print("=== VERIFICACIÓN COMPLETA DE LA FANTASÍA DEL 7 ===")
    print(f"Rango: [{start}, {end}]")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Análisis por lotes
    results, execution_time = batch_analysis(start, end)
    
    # Generar estadísticas
    stats = generate_statistics(results)
    stats['execution_time'] = execution_time
    stats['range'] = {'start': start, 'end': end}
    
    # Mostrar resultados
    print("\n=== RESULTADOS ===")
    print(f"Total de valores testados: {stats['total_tested']}")
    print(f"Convergencia exitosa: {stats['successful_convergence']} ({stats['success_rate']:.1f}%)")
    print(f"Tiempo de ejecución: {execution_time:.2f} segundos")
    print(f"\nEstadísticas de tiempo de convergencia:")
    print(f"  Media: {stats['average_time']:.2f}")
    print(f"  Mediana: {stats['median_time']:.2f}")
    print(f"  Desv. estándar: {stats['std_dev']:.2f}")
    print(f"  Mínimo: {stats['min_time']}")
    print(f"  Máximo: {stats['max_time']}")
    print(f"\nValidación de cotas:")
    print(f"  Violaciones de cota superior: {stats['upper_bound_violations']}")
    print(f"  Satisfacción de cota inferior: {stats['lower_bound_satisfaction']:.1f}%")
    
    if save_results:
        # Guardar resultados en JSON
        output_file = f"verificacion_{start}_{end}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w') as f:
            json.dump({
                'statistics': stats,
                'sample_results': results[:100]  # Guardar muestra
            }, f, indent=2)
        print(f"\nResultados guardados en: {output_file}")
    
    return results, stats

if __name__ == "__main__":
    # Ejecutar verificación estándar
    results, stats = run_complete_verification(101, 10000)
    
    # Verificación adicional con números grandes
    print("\n\n=== VERIFICACIÓN CON NÚMEROS GRANDES ===")
    large_sample = [1000, 10000, 100000, 1000000, 10000000]
    
    for n in large_sample:
        data = compute_convergence_data(n)
        print(f"n₀ = {n:,}: Tiempo = {data['convergence_time']}, " +
              f"Cota superior = {data['theoretical_upper']}, " +
              f"Eficiencia = {data['efficiency']:.2%}")