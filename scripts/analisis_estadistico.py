#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANÁLISIS ESTADÍSTICO Y DE PATRONES - FANTASÍA DEL 7
Análisis detallado de patrones en trayectorias y propiedades estadísticas

Autor: R. Benítez
Fecha: Julio 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from collections import Counter
import json

from fantasia7_base import F7, compute_orbit
from verificacion_completa import compute_convergence_data, batch_analysis

def classify_trajectories(results):
    """
    Clasifica trayectorias según patrones característicos
    """
    patterns = {
        'direct_to_7': [],           # Alcanzan 7 sin pasar por < 7
        'undershoot': [],            # Pasan por debajo de 7
        'long_decreasing': [],       # > 15 pasos decrecientes
        'minimal_steps': [],         # Tiempo óptimo teórico
        'power_of_2_like': [],       # Siguen patrón similar a potencias de 2
        'one_step': []               # Alcanzan 7 en un solo paso
    }
    
    for result in results:
        trajectory = result['trajectory']
        n0 = result['initial']
        
        # Direct to 7
        if all(x >= 7 for x in trajectory[:-1]) and trajectory[-1] == 7:
            patterns['direct_to_7'].append(result)
        
        # Undershoot
        if any(x < 7 for x in trajectory[:-1]):
            patterns['undershoot'].append(result)
        
        # Long decreasing phase
        if result['decreasing_steps'] > 15:
            patterns['long_decreasing'].append(result)
        
        # Minimal steps (within 1 of theoretical minimum)
        theoretical_min = max(1, int(np.log2(n0)) - 2)
        if result['convergence_time'] <= theoretical_min + 1:
            patterns['minimal_steps'].append(result)
        
        # One step convergence
        if result['convergence_time'] == 1:
            patterns['one_step'].append(result)
        
        # Power of 2 like behavior
        if is_power_of_2_like(trajectory):
            patterns['power_of_2_like'].append(result)
    
    return patterns

def is_power_of_2_like(trajectory):
    """Detecta si la trayectoria sigue patrón de potencia de 2"""
    decreasing_part = []
    for i in range(len(trajectory)-1):
        if trajectory[i] > 7:
            decreasing_part.append(trajectory[i])
        else:
            break
    
    if len(decreasing_part) < 3:
        return False
    
    # Verifica si cada paso es aproximadamente la mitad del anterior
    ratios = [decreasing_part[i+1] / decreasing_part[i] 
              for i in range(len(decreasing_part)-1)]
    avg_ratio = np.mean(ratios)
    
    return 0.45 <= avg_ratio <= 0.55  # Cerca de 0.5

def analyze_correlations(results):
    """
    Analiza correlaciones entre propiedades de n₀ y tiempo de convergencia
    """
    data = []
    for result in results:
        n0 = result['initial']
        data.append({
            'n0': n0,
            'log_n0': np.log2(n0),
            'convergence_time': result['convergence_time'],
            'binary_weight': bin(n0).count('1'),  # Número de 1s en binario
            'trailing_zeros': (n0 & -n0).bit_length() - 1,  # Ceros al final
            'is_power_of_2': (n0 & (n0 - 1)) == 0,
            'mod_7': n0 % 7,
            'mod_8': n0 % 8,
            'first_digit': int(str(n0)[0]),
            'num_digits': len(str(n0))
        })
    
    df = pd.DataFrame(data)
    
    # Correlaciones
    correlations = df[['log_n0', 'convergence_time', 'binary_weight', 
                      'trailing_zeros', 'mod_7', 'mod_8']].corr()
    
    return df, correlations

def analyze_extreme_cases(results):
    """
    Analiza casos con comportamiento extremo
    """
    # Tiempos de convergencia más largos
    longest_times = sorted(results, key=lambda x: x['convergence_time'], 
                          reverse=True)[:10]
    
    # Tiempos más cortos para n0 > 1000
    large_fast = sorted([r for r in results if r['initial'] > 1000], 
                       key=lambda x: x['convergence_time'])[:10]
    
    # Valores que alcanzan mínimos más bajos
    with_undershoot = [r for r in results if r['min_before_seven'] is not None]
    if with_undershoot:
        lowest_mins = sorted(with_undershoot, 
                           key=lambda x: x['min_before_seven'])[:10]
    else:
        lowest_mins = []
    
    # Mayor eficiencia (tiempo real / cota teórica)
    most_efficient = sorted(results, key=lambda x: x['efficiency'])[:10]
    
    return {
        'longest_times': longest_times,
        'large_fast': large_fast,
        'lowest_mins': lowest_mins,
        'most_efficient': most_efficient
    }

def plot_convergence_distribution(results, save_path='convergence_distribution.png'):
    """
    Genera visualizaciones de la distribución de tiempos de convergencia
    """
    convergence_times = [r['convergence_time'] for r in results]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Histograma
    ax1 = axes[0, 0]
    ax1.hist(convergence_times, bins=30, edgecolor='black', alpha=0.7)
    ax1.set_xlabel('Tiempo de Convergencia')
    ax1.set_ylabel('Frecuencia')
    ax1.set_title('Distribución de Tiempos de Convergencia')
    
    # Box plot
    ax2 = axes[0, 1]
    ax2.boxplot(convergence_times)
    ax2.set_ylabel('Tiempo de Convergencia')
    ax2.set_title('Box Plot de Tiempos')
    
    # Scatter plot: n0 vs tiempo
    ax3 = axes[1, 0]
    n0_values = [r['initial'] for r in results[:1000]]  # Muestra
    times_sample = convergence_times[:1000]
    ax3.scatter(n0_values, times_sample, alpha=0.5)
    ax3.set_xlabel('Valor Inicial (n₀)')
    ax3.set_ylabel('Tiempo de Convergencia')
    ax3.set_title('n₀ vs Tiempo de Convergencia')
    
    # Comparación con cotas teóricas
    ax4 = axes[1, 1]
    theoretical_upper = [r['theoretical_upper'] for r in results[:1000]]
    ax4.scatter(times_sample, theoretical_upper, alpha=0.5)
    ax4.plot([0, max(times_sample)], [0, max(times_sample)], 'r--', label='y=x')
    ax4.set_xlabel('Tiempo Real')
    ax4.set_ylabel('Cota Superior Teórica')
    ax4.set_title('Tiempo Real vs Cota Teórica')
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def generate_pattern_report(results):
    """
    Genera un informe detallado de patrones encontrados
    """
    patterns = classify_trajectories(results)
    
    report = {
        'total_analyzed': len(results),
        'pattern_frequencies': {},
        'pattern_percentages': {},
        'pattern_examples': {}
    }
    
    for pattern_name, pattern_results in patterns.items():
        count = len(pattern_results)
        percentage = count / len(results) * 100
        
        report['pattern_frequencies'][pattern_name] = count
        report['pattern_percentages'][pattern_name] = round(percentage, 2)
        
        # Ejemplos representativos
        if pattern_results:
            examples = sorted(pattern_results, 
                            key=lambda x: x['initial'])[:3]
            report['pattern_examples'][pattern_name] = [
                {
                    'n0': ex['initial'],
                    'trajectory': ex['trajectory'],
                    'time': ex['convergence_time']
                } for ex in examples
            ]
    
    return report

def analyze_binary_properties(results):
    """
    Analiza propiedades relacionadas con la representación binaria
    """
    binary_analysis = []
    
    for result in results:
        n0 = result['initial']
        binary_rep = bin(n0)[2:]  # Quitar '0b'
        
        binary_analysis.append({
            'n0': n0,
            'convergence_time': result['convergence_time'],
            'binary_length': len(binary_rep),
            'ones_count': binary_rep.count('1'),
            'zeros_count': binary_rep.count('0'),
            'ones_ratio': binary_rep.count('1') / len(binary_rep),
            'starts_with_1': binary_rep[0] == '1',
            'ends_with_1': binary_rep[-1] == '1',
            'consecutive_ones': max(len(s) for s in binary_rep.split('0') if s),
            'consecutive_zeros': max(len(s) for s in binary_rep.split('1') if s) if '0' in binary_rep else 0
        })
    
    df_binary = pd.DataFrame(binary_analysis)
    
    # Análisis de correlaciones
    binary_correlations = df_binary[['convergence_time', 'binary_length', 
                                     'ones_count', 'ones_ratio', 
                                     'consecutive_ones']].corr()
    
    return df_binary, binary_correlations

def run_complete_analysis(start=101, end=10000):
    """
    Ejecuta análisis estadístico completo
    """
    print("=== ANÁLISIS ESTADÍSTICO COMPLETO ===")
    print(f"Analizando rango [{start}, {end}]...")
    
    # Obtener datos
    results, execution_time = batch_analysis(start, end)
    print(f"Datos obtenidos en {execution_time:.2f} segundos")
    
    # 1. Análisis de patrones
    print("\n1. Análisis de Patrones:")
    pattern_report = generate_pattern_report(results)
    for pattern, percentage in pattern_report['pattern_percentages'].items():
        print(f"  {pattern}: {percentage}%")
    
    # 2. Correlaciones
    print("\n2. Análisis de Correlaciones:")
    df_corr, correlations = analyze_correlations(results)
    print("Correlaciones con tiempo de convergencia:")
    print(correlations['convergence_time'].sort_values(ascending=False))
    
    # 3. Casos extremos
    print("\n3. Casos Extremos:")
    extremes = analyze_extreme_cases(results)
    print(f"  Tiempo más largo: n₀={extremes['longest_times'][0]['initial']}, " +
          f"tiempo={extremes['longest_times'][0]['convergence_time']}")
    print(f"  Más eficiente: n₀={extremes['most_efficient'][0]['initial']}, " +
          f"eficiencia={extremes['most_efficient'][0]['efficiency']:.2%}")
    
    # 4. Propiedades binarias
    print("\n4. Análisis de Propiedades Binarias:")
    df_binary, binary_corr = analyze_binary_properties(results[:1000])
    print("Correlaciones binarias con tiempo de convergencia:")
    print(binary_corr['convergence_time'].sort_values(ascending=False))
    
    # 5. Generar visualizaciones
    print("\n5. Generando visualizaciones...")
    plot_convergence_distribution(results)
    print("Gráficos guardados en convergence_distribution.png")
    
    # Guardar informe completo
    report = {
        'range': {'start': start, 'end': end},
        'patterns': pattern_report,
        'correlations': correlations.to_dict(),
        'extreme_cases': {
            'longest_time': extremes['longest_times'][0]['initial'],
            'most_efficient': extremes['most_efficient'][0]['initial']
        }
    }
    
    with open('analisis_completo.json', 'w') as f:
        json.dump(report, f, indent=2)
    print("\nInforme completo guardado en analisis_completo.json")
    
    return results, report

if __name__ == "__main__":
    # Ejecutar análisis completo
    results, report = run_complete_analysis(101, 10000)
    
    # Análisis adicional: valores que convergen en 1 paso
    print("\n\n=== ANÁLISIS ESPECIAL: Convergencia en 1 paso ===")
    one_step = [r for r in results if r['convergence_time'] == 1]
    if one_step:
        print(f"Valores que convergen en 1 paso: {[r['initial'] for r in one_step]}")
        
        # Verificar patrón
        for r in one_step[:5]:
            n0 = r['initial']
            print(f"n₀ = {n0} → F₇({n0}) = {F7(n0)}")