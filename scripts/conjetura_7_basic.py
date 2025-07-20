"""
Funciones básicas para la Fantasía del 7
=======================================

Este módulo contiene las funciones fundamentales para trabajar con la Fantasía del 7,
una construcción matemática diseñada para refutar la numerología.
"""

def F7(n):
    """
    Función F₇ según la definición de la Fantasía del 7
    
    Args:
        n (int): Número natural de entrada
        
    Returns:
        int: Resultado de aplicar F₇(n)
        
    Definición:
        F₇(n) = n           si n = 7
        F₇(n) = ⌊n/2⌋       si n > 7 y n es par
        F₇(n) = ⌊(n-1)/2⌋   si n > 7 y n es impar  
        F₇(n) = n + 1       si n < 7
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
    Computa la órbita completa de un número bajo la función F₇
    
    Args:
        n0 (int): Número inicial
        max_iterations (int): Máximo número de iteraciones para evitar bucles infinitos
        
    Returns:
        tuple: (orbit, convergence_time) donde:
            - orbit (list): Lista con todos los valores en la trayectoria
            - convergence_time (int): Número de pasos hasta convergencia
    """
    orbit = [n0]
    current = n0
    
    for i in range(max_iterations):
        if current == 7:
            break
        current = F7(current)
        orbit.append(current)
    
    return orbit, len(orbit) - 1  # orbit, convergence_time

def prove_convergence(n0):
    """
    Demostración constructiva de que n0 converge a 7
    
    Args:
        n0 (int): Número inicial (debe ser > 100)
        
    Returns:
        tuple: (steps, trajectory) donde:
            - steps (int): Número de pasos hasta convergencia
            - trajectory (list): Trayectoria completa
            
    Raises:
        ValueError: Si n0 <= 100
    """
    if n0 <= 100:
        raise ValueError("n0 must be > 100")
    
    current = n0
    steps = 0
    trajectory = [current]
    
    # Phase 1: Decrement until ≤ 7
    while current > 7:
        current = F7(current)
        steps += 1
        trajectory.append(current)
        assert current < trajectory[-2]  # Verify strict decrease
    
    # Phase 2: Increment until = 7 (if needed)
    while current < 7:
        current = F7(current)
        steps += 1
        trajectory.append(current)
        assert current == trajectory[-2] + 1  # Verify increment by 1
    
    assert current == 7
    return steps, trajectory

if __name__ == "__main__":
    # Pruebas básicas
    print("=== PRUEBAS BÁSICAS DE LA FANTASÍA DEL 7 ===")
    
    # Probar algunos valores específicos
    test_values = [153, 247, 384, 519, 672]
    
    for n in test_values:
        orbit, time = compute_orbit(n)
        print(f"n₀ = {n}: converge en {time} pasos")
        print(f"  Trayectoria: {' → '.join(map(str, orbit))}")
        print()
    
    # Probar demostración constructiva
    print("=== DEMOSTRACIÓN CONSTRUCTIVA ===")
    try:
        steps, trajectory = prove_convergence(153)
        print(f"Demostración exitosa para n₀=153: {steps} pasos")
        print(f"Trayectoria: {' → '.join(map(str, trajectory))}")
    except Exception as e:
        print(f"Error en demostración: {e}")
