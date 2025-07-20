#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FANTASÍA DEL 7 - FUNCIONES BASE
Implementación de las funciones fundamentales de la Fantasía del 7

Autor: R. Benítez
Fecha: Julio 2025
"""

def F7(n):
    """
    Función central F₇: ℕ → ℕ
    
    Reglas:
    - Si n = 7: devuelve 7 (punto fijo)
    - Si n > 7: devuelve ⌊n/2⌋ si n es par, ⌊(n-1)/2⌋ si n es impar
    - Si n < 7: devuelve n + 1
    
    Args:
        n (int): Número natural de entrada
        
    Returns:
        int: F₇(n)
    """
    if n == 7:
        return n
    elif n > 7:
        if n % 2 == 0:
            return n // 2
        else:
            return (n - 1) // 2
    else:  # n < 7
        return n + 1

def compute_orbit(n0, max_iterations=1000):
    """
    Calcula la órbita completa de n₀ bajo iteración de F₇
    
    Args:
        n0 (int): Valor inicial
        max_iterations (int): Número máximo de iteraciones
        
    Returns:
        tuple: (órbita, tiempo_de_convergencia)
    """
    orbit = [n0]
    current = n0
    
    for i in range(max_iterations):
        if current == 7:
            break
        current = F7(current)
        orbit.append(current)
    
    return orbit, len(orbit) - 1  # orbit, convergence_time

def verify_convergence(n0, verbose=False):
    """
    Verifica que n₀ converge a 7 y proporciona información detallada
    
    Args:
        n0 (int): Valor inicial
        verbose (bool): Si mostrar información detallada
        
    Returns:
        dict: Información de convergencia
    """
    orbit, convergence_time = compute_orbit(n0)
    converged = orbit[-1] == 7
    
    result = {
        'initial': n0,
        'converged': converged,
        'convergence_time': convergence_time,
        'orbit_length': len(orbit),
        'final_value': orbit[-1]
    }
    
    if verbose:
        print(f"n₀ = {n0}")
        print(f"Órbita: {' → '.join(map(str, orbit))}")
        print(f"Convergió: {'Sí' if converged else 'No'}")
        print(f"Tiempo de convergencia: {convergence_time}")
        print()
    
    return result

if __name__ == "__main__":
    # Ejemplos de uso
    print("=== FANTASÍA DEL 7 - EJEMPLOS ===\n")
    
    # Ejemplo 1: Números pequeños
    print("Ejemplos con números pequeños:")
    for n in [1, 5, 7, 10, 15]:
        verify_convergence(n, verbose=True)
    
    # Ejemplo 2: Potencias de 2
    print("\nEjemplos con potencias de 2:")
    for k in [3, 4, 5]:
        verify_convergence(2**k, verbose=True)
    
    # Ejemplo 3: Números grandes
    print("\nEjemplos con números grandes:")
    for n in [100, 1000, 10000]:
        result = verify_convergence(n)
        print(f"n₀ = {n}: Tiempo de convergencia = {result['convergence_time']}")