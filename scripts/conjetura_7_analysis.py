"""
Análisis Comprehensivo de la Fantasía del 7
===========================================

Este módulo contiene herramientas avanzadas para el análisis estadístico,
visualización y verificación empírica de la Fantasía del 7.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from conjetura_7_basic import F7

def evaluate_single_number(n0, max_iterations=1000, show_trajectory=True):
    """
    Evalúa un número único y muestra resultados detallados
    
    Args:
        n0: Número inicial
        max_iterations: Máximo número de iteraciones
        show_trajectory: Si mostrar la trayectoria completa
    
    Returns:
        dict: Resultados del análisis
    """
    print(f"\n=== EVALUACIÓN DE n₀ = {n0} ===")
    
    trajectory = [n0]
    current = n0
    steps = 0
    start_time = time.time()
    
    # Seguir la trayectoria
    while current != 7 and steps < max_iterations:
        current = F7(current)
        trajectory.append(current)
        steps += 1
    
    execution_time = time.time() - start_time
    converged = current == 7
    
    # Análisis de la trayectoria
    max_value = max(trajectory)
    min_value = min(trajectory)
    decreasing_steps = sum(1 for i in range(len(trajectory)-1) 
                          if trajectory[i] > trajectory[i+1])
    increasing_steps = sum(1 for i in range(len(trajectory)-1) 
                          if trajectory[i] < trajectory[i+1])
    
    # Mostrar resultados
    print(f"Convergencia: {'✓ SÍ' if converged else '✗ NO'}")
    print(f"Tiempo de convergencia: {steps} pasos")
    print(f"Tiempo de ejecución: {execution_time*1000:.3f} ms")
    print(f"Valor máximo alcanzado: {max_value}")
    print(f"Valor mínimo alcanzado: {min_value}")
    print(f"Pasos decrecientes: {decreasing_steps}")
    print(f"Pasos crecientes: {increasing_steps}")
    
    # Verificar cotas teóricas
    theoretical_upper = int(np.log2(n0)) + 6 if n0 > 0 else 10
    theoretical_lower = max(1, int(np.log2(n0)) - 2) if n0 > 0 else 1
    
    print(f"\nVerificación de cotas teóricas:")
    print(f"Cota superior teórica: T(n₀) ≤ ⌊log₂({n0})⌋ + 6 = {theoretical_upper}")
    print(f"Cota inferior teórica: T(n₀) ≥ ⌊log₂({n0})⌋ - 2 = {theoretical_lower}")
    print(f"Satisface cota superior: {'✓' if steps <= theoretical_upper else '✗'}")
    print(f"Satisface cota inferior: {'✓' if steps >= theoretical_lower else '✗'}")
    
    if show_trajectory:
        print(f"\nTrayectoria completa:")
        trajectory_str = " → ".join(map(str, trajectory))
        if len(trajectory_str) > 100:
            # Mostrar inicio y final si es muy larga
            start_part = " → ".join(map(str, trajectory[:5]))
            end_part = " → ".join(map(str, trajectory[-5:]))
            print(f"{start_part} → ... → {end_part}")
        else:
            print(trajectory_str)
    
    return {
        'initial': n0,
        'converged': converged,
        'steps': steps,
        'trajectory': trajectory,
        'execution_time': execution_time,
        'max_value': max_value,
        'min_value': min_value,
        'decreasing_steps': decreasing_steps,
        'increasing_steps': increasing_steps,
        'theoretical_upper': theoretical_upper,
        'theoretical_lower': theoretical_lower,
        'satisfies_upper': steps <= theoretical_upper,
        'satisfies_lower': steps >= theoretical_lower
    }

def evaluate_series(start, end, show_summary=True, show_details=False):
    """
    Evalúa una serie de números del start al end
    
    Args:
        start: Número inicial de la serie
        end: Número final de la serie
        show_summary: Si mostrar resumen estadístico
        show_details: Si mostrar detalles de cada número
    
    Returns:
        list: Lista de resultados para cada número
    """
    print(f"\n=== EVALUACIÓN DE SERIE [{start}, {end}] ===")
    print(f"Evaluando {end - start + 1} números...")
    
    results = []
    start_time = time.time()
    
    for n0 in range(start, end + 1):
        result = evaluate_single_number(n0, show_trajectory=False)
        results.append(result)
        
        if show_details:
            print(f"n₀={n0}: {result['steps']} pasos, "
                  f"converge={'✓' if result['converged'] else '✗'}")
        elif len(results) % 1000 == 0:
            print(f"Procesados {len(results)}/{end - start + 1}...")
    
    total_time = time.time() - start_time
    
    if show_summary:
        print(f"\n=== RESUMEN ESTADÍSTICO ===")
        
        # Estadísticas básicas
        convergence_times = [r['steps'] for r in results if r['converged']]
        success_rate = len(convergence_times) / len(results)
        
        print(f"Números evaluados: {len(results)}")
        print(f"Convergencia exitosa: {len(convergence_times)} ({success_rate:.1%})")
        print(f"Tiempo total de ejecución: {total_time:.2f} segundos")
        
        if convergence_times:
            print(f"\nTiempos de convergencia:")
            print(f"  Promedio: {np.mean(convergence_times):.2f}")
            print(f"  Mediana: {np.median(convergence_times):.1f}")
            print(f"  Mínimo: {min(convergence_times)}")
            print(f"  Máximo: {max(convergence_times)}")
            print(f"  Desviación estándar: {np.std(convergence_times):.2f}")
            
            # Verificación de cotas
            upper_violations = sum(1 for r in results if not r['satisfies_upper'])
            lower_violations = sum(1 for r in results if not r['satisfies_lower'])
            
            print(f"\nVerificación de cotas teóricas:")
            print(f"  Violaciones cota superior: {upper_violations}/{len(results)}")
            print(f"  Violaciones cota inferior: {lower_violations}/{len(results)}")
            
            # Distribución por rangos de tiempo
            print(f"\nDistribución de tiempos:")
            time_distribution = defaultdict(int)
            for ct in convergence_times:
                range_key = f"{(ct//5)*5}-{(ct//5)*5+4}"
                time_distribution[range_key] += 1
            
            for time_range in sorted(time_distribution.keys()):
                count = time_distribution[time_range]
                percentage = count / len(convergence_times) * 100
                print(f"  {time_range} pasos: {count} ({percentage:.1f}%)")
    
    return results

def create_visualization(results, title="Análisis de la Fantasía del 7"):
    """Crea visualizaciones de los resultados"""
    
    convergence_times = [r['steps'] for r in results if r['converged']]
    initial_values = [r['initial'] for r in results if r['converged']]
    
    if not convergence_times:
        print("No hay datos suficientes para visualización")
        return
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(title, fontsize=16)
    
    # 1. Histograma de tiempos de convergencia
    axes[0,0].hist(convergence_times, bins=min(30, max(convergence_times)-min(convergence_times)+1), 
                   alpha=0.7, color='skyblue', edgecolor='black')
    axes[0,0].set_title('Distribución de Tiempos de Convergencia')
    axes[0,0].set_xlabel('Tiempo de Convergencia (pasos)')
    axes[0,0].set_ylabel('Frecuencia')
    axes[0,0].grid(True, alpha=0.3)
    
    # 2. Tiempo vs valor inicial
    axes[0,1].scatter(initial_values, convergence_times, alpha=0.6, s=20)
    axes[0,1].set_title('Tiempo de Convergencia vs Valor Inicial')
    axes[0,1].set_xlabel('Valor Inicial (n₀)')
    axes[0,1].set_ylabel('Tiempo de Convergencia')
    axes[0,1].grid(True, alpha=0.3)
    
    # Añadir líneas de cotas teóricas si hay suficientes datos
    if len(initial_values) > 10:
        log_values = [np.log2(n) for n in initial_values if n > 0]
        upper_bounds = [int(log_n) + 6 for log_n in log_values]
        lower_bounds = [max(1, int(log_n) - 2) for log_n in log_values]
        
        sorted_indices = np.argsort([n for n in initial_values if n > 0])
        sorted_initials = np.array([n for n in initial_values if n > 0])[sorted_indices]
        sorted_upper = np.array(upper_bounds)[sorted_indices]
        sorted_lower = np.array(lower_bounds)[sorted_indices]
        
        axes[0,1].plot(sorted_initials, sorted_upper, 'r--', 
                      label='Cota Superior', linewidth=2)
        axes[0,1].plot(sorted_initials, sorted_lower, 'g--', 
                      label='Cota Inferior', linewidth=2)
        axes[0,1].legend()
    
    # 3. Trayectorias ejemplo (primeras 5 que sean cortas)
    example_results = [r for r in results[:20] if r['converged'] and len(r['trajectory']) <= 15][:5]
    
    for i, result in enumerate(example_results):
        trajectory = result['trajectory']
        axes[1,0].plot(range(len(trajectory)), trajectory, 
                      marker='o', label=f"n₀={result['initial']}", linewidth=2)
    
    axes[1,0].axhline(y=7, color='red', linestyle='--', linewidth=3, label='Objetivo (7)')
    axes[1,0].set_title('Ejemplos de Trayectorias de Convergencia')
    axes[1,0].set_xlabel('Iteración')
    axes[1,0].set_ylabel('Valor')
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # 4. Eficiencia vs cota teórica
    efficiency_ratios = []
    for r in results:
        if r['converged'] and r['initial'] > 0:
            theoretical = r['theoretical_upper']
            actual = r['steps']
            efficiency_ratios.append(actual / theoretical)
    
    if efficiency_ratios:
        axes[1,1].hist(efficiency_ratios, bins=20, alpha=0.7, 
                      color='lightgreen', edgecolor='black')
        axes[1,1].axvline(x=np.mean(efficiency_ratios), color='red', linestyle='--', 
                         linewidth=2, label=f'Promedio: {np.mean(efficiency_ratios):.3f}')
        axes[1,1].set_title('Eficiencia: Tiempo Real / Cota Teórica')
        axes[1,1].set_xlabel('Ratio (Tiempo Real / Cota Superior)')
        axes[1,1].set_ylabel('Frecuencia')
        axes[1,1].legend()
        axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('conjetura_7_resultados.png', dpi=150, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Ejemplo de uso
    print("=== ANÁLISIS DE EJEMPLO DE LA FANTASÍA DEL 7 ===")
    
    # Evaluar algunos números específicos
    specific_numbers = [153, 247, 384]
    for n in specific_numbers:
        evaluate_single_number(n)
    
    # Evaluar una serie pequeña
    results = evaluate_series(101, 120)
    
    # Crear visualización
    create_visualization(results, "Análisis de Ejemplo [101, 120]")
