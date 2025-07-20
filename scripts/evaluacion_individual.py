#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA DE EVALUACIÓN INDIVIDUAL - FANTASÍA DEL 7
Herramienta para evaluar números individuales con métricas detalladas

Autor: R. Benítez
Fecha: Julio 2025
"""

import time
import math
import statistics
import argparse
import json

def F7(n):
    """
    Implementación de la función F₇ según la Fantasía del 7.
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

def evaluate_number(n0, max_iterations=1000, track_metrics=True, verbose=False):
    """
    Evalúa la convergencia de un número específico con métricas detalladas.
    
    Args:
        n0 (int): Número inicial a evaluar
        max_iterations (int): Máximo de iteraciones permitidas
        track_metrics (bool): Si calcular métricas adicionales
        verbose (bool): Si mostrar información detallada durante la evaluación
    
    Returns:
        dict: Diccionario con todos los resultados y métricas
    """
    if n0 <= 0:
        raise ValueError("n0 debe ser un número natural positivo")
    
    trajectory = [n0]
    current = n0
    steps = 0
    start_time = time.time()

    # Seguimiento de métricas adicionales
    max_value = n0
    min_value = n0
    decreasing_steps = 0
    increasing_steps = 0
    previous_value = n0
    
    # Fases de convergencia
    phase_changes = 0
    current_phase = None  # 'decreasing', 'increasing', or None

    while current != 7 and steps < max_iterations:
        current = F7(current)
        trajectory.append(current)
        steps += 1

        if track_metrics:
            max_value = max(max_value, current)
            min_value = min(min_value, current)
            
            # Determinar dirección
            if current < previous_value:
                decreasing_steps += 1
                new_phase = 'decreasing'
            elif current > previous_value:
                increasing_steps += 1
                new_phase = 'increasing'
            else:
                new_phase = current_phase
            
            # Detectar cambios de fase
            if new_phase != current_phase and current_phase is not None:
                phase_changes += 1
            current_phase = new_phase
            
            previous_value = current
            
        if verbose and steps % 10 == 0:
            print(f"  Paso {steps}: {current}")

    execution_time = (time.time() - start_time) * 1000  # en ms
    converged = current == 7

    # Cálculo de cotas teóricas
    theoretical_upper = math.floor(math.log2(n0)) + 6 if n0 > 0 else 10
    theoretical_lower = max(1, math.floor(math.log2(n0)) - 2) if n0 > 0 else 1

    efficiency = steps / theoretical_upper if theoretical_upper > 0 else 0
    slack = theoretical_upper - steps

    # Análisis adicional
    has_undershoot = min_value < 7
    direct_to_seven = all(val >= 7 for val in trajectory[:-1]) and converged
    
    # Propiedades binarias
    binary_rep = bin(n0)[2:]
    binary_length = len(binary_rep)
    binary_weight = binary_rep.count('1')
    
    # Detectar patrones especiales
    is_power_of_2 = (n0 & (n0 - 1)) == 0 and n0 != 0
    is_mersenne = all(c == '1' for c in binary_rep)  # Todos 1s en binario
    
    result = {
        # Información básica
        "initial": n0,
        "converged": converged,
        "steps": steps,
        "trajectory": trajectory,
        "executionTime": execution_time,
        
        # Métricas de trayectoria
        "trajectoryLength": len(trajectory),
        "maxValue": max_value,
        "minValue": min_value,
        "decreasingSteps": decreasing_steps,
        "increasingSteps": increasing_steps,
        "phaseChanges": phase_changes,
        
        # Cotas teóricas
        "theoreticalUpper": theoretical_upper,
        "theoreticalLower": theoretical_lower,
        "satisfiesUpper": steps <= theoretical_upper,
        "satisfiesLower": steps >= theoretical_lower,
        "efficiency": efficiency,
        "slack": slack,
        
        # Características especiales
        "hasUndershoot": has_undershoot,
        "directToSeven": direct_to_seven,
        
        # Propiedades binarias
        "binaryLength": binary_length,
        "binaryWeight": binary_weight,
        "binaryDensity": binary_weight / binary_length,
        
        # Patrones especiales
        "isPowerOf2": is_power_of_2,
        "isMersenne": is_mersenne,
        "mod7": n0 % 7,
        "mod8": n0 % 8
    }
    
    # Análisis estadístico de la trayectoria
    if len(trajectory) > 1:
        differences = [trajectory[i+1] - trajectory[i] 
                      for i in range(len(trajectory)-1)]
        result["avgStepSize"] = sum(abs(d) for d in differences) / len(differences)
        result["maxStepSize"] = max(abs(d) for d in differences)
    
    return result

def format_trajectory(trajectory, max_display=20):
    """
    Formatea la trayectoria para mostrar de manera legible
    """
    if len(trajectory) <= max_display:
        return ' → '.join(map(str, trajectory))
    else:
        first_part = ' → '.join(map(str, trajectory[:10]))
        last_part = ' → '.join(map(str, trajectory[-5:]))
        return f"{first_part} → ... → {last_part}"

def print_evaluation_report(result):
    """
    Imprime un informe detallado de la evaluación
    """
    print("\n" + "="*60)
    print(f"EVALUACIÓN DE n₀ = {result['initial']}")
    print("="*60)
    
    print(f"\n✓ CONVERGENCIA: {'SÍ' if result['converged'] else 'NO'}")
    print(f"  Pasos totales: {result['steps']}")
    print(f"  Tiempo de ejecución: {result['executionTime']:.2f} ms")
    
    print(f"\n📊 MÉTRICAS DE TRAYECTORIA:")
    print(f"  Longitud: {result['trajectoryLength']}")
    print(f"  Valor máximo alcanzado: {result['maxValue']}")
    print(f"  Valor mínimo alcanzado: {result['minValue']}")
    print(f"  Pasos decrecientes: {result['decreasingSteps']}")
    print(f"  Pasos crecientes: {result['increasingSteps']}")
    print(f"  Cambios de fase: {result['phaseChanges']}")
    
    print(f"\n📏 ANÁLISIS DE COTAS:")
    print(f"  Cota superior teórica: {result['theoreticalUpper']}")
    print(f"  Cota inferior teórica: {result['theoreticalLower']}")
    print(f"  Satisface cota superior: {'SÍ' if result['satisfiesUpper'] else 'NO'}")
    print(f"  Satisface cota inferior: {'SÍ' if result['satisfiesLower'] else 'NO'}")
    print(f"  Eficiencia: {result['efficiency']:.1%}")
    print(f"  Holgura: {result['slack']}")
    
    print(f"\n🔍 CARACTERÍSTICAS ESPECIALES:")
    print(f"  Pasa por debajo de 7: {'SÍ' if result['hasUndershoot'] else 'NO'}")
    print(f"  Directo a 7: {'SÍ' if result['directToSeven'] else 'NO'}")
    print(f"  Es potencia de 2: {'SÍ' if result['isPowerOf2'] else 'NO'}")
    print(f"  Es número de Mersenne: {'SÍ' if result['isMersenne'] else 'NO'}")
    
    print(f"\n💻 PROPIEDADES BINARIAS:")
    print(f"  Longitud binaria: {result['binaryLength']} bits")
    print(f"  Peso binario (1s): {result['binaryWeight']}")
    print(f"  Densidad binaria: {result['binaryDensity']:.1%}")
    print(f"  Módulo 7: {result['mod7']}")
    print(f"  Módulo 8: {result['mod8']}")
    
    print(f"\n🛤️ TRAYECTORIA:")
    print(f"  {format_trajectory(result['trajectory'])}")
    
    print("\n" + "="*60)

def evaluate_range(start, end, step=1):
    """
    Evalúa un rango de números y encuentra casos interesantes
    """
    interesting_cases = {
        'one_step': [],
        'very_efficient': [],
        'very_inefficient': [],
        'with_undershoot': [],
        'direct_to_seven': [],
        'power_of_2': []
    }
    
    for n in range(start, end + 1, step):
        result = evaluate_number(n, track_metrics=True, verbose=False)
        
        # Clasificar casos interesantes
        if result['steps'] == 1:
            interesting_cases['one_step'].append(n)
        if result['efficiency'] < 0.5:
            interesting_cases['very_efficient'].append(n)
        if result['efficiency'] > 0.9:
            interesting_cases['very_inefficient'].append(n)
        if result['hasUndershoot']:
            interesting_cases['with_undershoot'].append(n)
        if result['directToSeven']:
            interesting_cases['direct_to_seven'].append(n)
        if result['isPowerOf2']:
            interesting_cases['power_of_2'].append(n)
    
    return interesting_cases

def main():
    parser = argparse.ArgumentParser(
        description='Evaluar números individuales en la Fantasía del 7'
    )
    parser.add_argument('number', type=int, nargs='?', 
                       help='Número a evaluar (si no se especifica, modo interactivo)')
    parser.add_argument('--range', nargs=2, type=int, metavar=('START', 'END'),
                       help='Evaluar un rango de números')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Mostrar información detallada')
    parser.add_argument('--json', '-j', action='store_true',
                       help='Salida en formato JSON')
    parser.add_argument('--find-special', action='store_true',
                       help='Buscar casos especiales en el rango')
    
    args = parser.parse_args()
    
    if args.range:
        # Modo rango
        start, end = args.range
        if args.find_special:
            print(f"Buscando casos especiales en [{start}, {end}]...")
            cases = evaluate_range(start, end)
            print("\nCASOS ESPECIALES ENCONTRADOS:")
            for case_type, numbers in cases.items():
                if numbers:
                    print(f"\n{case_type}: {numbers[:10]}{'...' if len(numbers) > 10 else ''}")
        else:
            for n in range(start, end + 1):
                result = evaluate_number(n, verbose=args.verbose)
                if args.json:
                    print(json.dumps(result))
                else:
                    print(f"n₀={n}: {result['steps']} pasos, eficiencia={result['efficiency']:.1%}")
    
    elif args.number:
        # Evaluar número específico
        result = evaluate_number(args.number, verbose=args.verbose)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_evaluation_report(result)
    
    else:
        # Modo interactivo
        print("=== EVALUADOR INTERACTIVO DE LA FANTASÍA DEL 7 ===")
        print("Ingrese números para evaluar (0 para salir)")
        
        while True:
            try:
                n = int(input("\nn₀ = "))
                if n == 0:
                    break
                if n < 0:
                    print("Por favor ingrese un número natural positivo")
                    continue
                    
                result = evaluate_number(n, verbose=args.verbose)
                print_evaluation_report(result)
                
            except ValueError:
                print("Por favor ingrese un número válido")
            except KeyboardInterrupt:
                print("\n\nSaliendo...")
                break

if __name__ == "__main__":
    main()