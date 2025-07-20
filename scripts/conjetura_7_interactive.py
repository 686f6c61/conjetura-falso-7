"""
Herramienta Interactiva para la Fantasía del 7
==============================================

Este módulo proporciona una interfaz interactiva para probar y verificar
la Fantasía del 7, una construcción matemática para refutar la numerología.
"""

import numpy as np
from conjetura_7_basic import F7, compute_orbit, prove_convergence
from conjetura_7_analysis import evaluate_single_number, evaluate_series, create_visualization

def run_predefined_tests():
    """Ejecuta pruebas predefinidas para verificación"""
    
    print("\n=== EJECUTANDO PRUEBAS PREDEFINIDAS ===")
    
    # Prueba 1: Casos específicos mencionados en el paper
    print("\n1. Casos específicos:")
    specific_cases = [153, 247, 384, 519, 672, 135, 298, 444, 789, 1001]
    specific_results = []
    
    for n0 in specific_cases:
        result = evaluate_single_number(n0, show_trajectory=False)
        specific_results.append(result)
        print(f"n₀={n0}: {result['steps']} pasos")
    
    # Verificar que coincidan con predicciones
    expected_patterns = {
        153: [153, 76, 38, 19, 9, 4, 5, 6, 7],
        247: [247, 123, 61, 30, 15, 7],
        384: [384, 192, 96, 48, 24, 12, 6, 7],
        519: [519, 259, 129, 64, 32, 16, 8, 4, 5, 6, 7],
        672: [672, 336, 168, 84, 42, 21, 10, 5, 6, 7],
        135: [135, 67, 33, 16, 8, 4, 5, 6, 7],
        298: [298, 149, 74, 37, 18, 9, 4, 5, 6, 7],
        444: [444, 222, 111, 55, 27, 13, 6, 7],
        789: [789, 394, 197, 98, 49, 24, 12, 6, 7],
        1001: [1001, 500, 250, 125, 62, 31, 15, 7]
    }
    
    print("\n2. Verificación de trayectorias específicas:")
    for n0, expected in expected_patterns.items():
        result = next(r for r in specific_results if r['initial'] == n0)
        actual = result['trajectory']
        match = actual == expected
        print(f"n₀={n0}: {'✓ COINCIDE' if match else '✗ DIFIERE'}")
        if not match:
            print(f"  Esperado: {expected}")
            print(f"  Actual:   {actual}")
    
    # Prueba 2: Verificación de rango pequeño
    print("\n3. Verificación rango [101, 200]:")
    small_range_results = evaluate_series(101, 200, show_details=False)
    
    # Prueba 3: Casos de potencias de 2
    print("\n4. Casos especiales - Potencias de 2:")
    powers_of_2 = [128, 256, 512, 1024]
    for n0 in powers_of_2:
        result = evaluate_single_number(n0, show_trajectory=False)
        expected_time = int(np.log2(n0)) + 6
        print(f"2^{int(np.log2(n0))} = {n0}: {result['steps']} pasos "
              f"(teórico: {expected_time})")
    
    # Resumen de todas las pruebas
    all_results = specific_results + small_range_results
    success_rate = sum(1 for r in all_results if r['converged']) / len(all_results)
    print(f"\n=== RESUMEN DE PRUEBAS PREDEFINIDAS ===")
    print(f"Total de números evaluados: {len(all_results)}")
    print(f"Tasa de convergencia: {success_rate:.1%}")
    print(f"Tiempo promedio: {np.mean([r['steps'] for r in all_results if r['converged']]):.2f}")

def main_interactive():
    """Función principal interactiva para pruebas"""
    
    print("=== HERRAMIENTA DE EVALUACIÓN: LA FANTASÍA DEL 7 ===")
    print("Opciones disponibles:")
    print("1. Evaluar un número único")
    print("2. Evaluar una serie de números")
    print("3. Ejecutar pruebas predefinidas")
    print("4. Análisis completo con visualización")
    print("5. Demostración constructiva")
    
    while True:
        try:
            choice = input("\nSeleccione una opción (1-5, o 'q' para salir): ").strip()
            
            if choice.lower() == 'q':
                break
            elif choice == '1':
                n0 = int(input("Ingrese el número a evaluar: "))
                evaluate_single_number(n0)
                
            elif choice == '2':
                start = int(input("Número inicial de la serie: "))
                end = int(input("Número final de la serie: "))
                results = evaluate_series(start, end)
                
                visualize = input("¿Crear visualización? (y/n): ").strip().lower()
                if visualize == 'y':
                    create_visualization(results, f"Serie [{start}, {end}]")
                    
            elif choice == '3':
                run_predefined_tests()
                
            elif choice == '4':
                start = int(input("Rango inicial: "))
                end = int(input("Rango final: "))
                if end - start > 1000:
                    confirm = input(f"Evaluar {end-start+1} números tomará tiempo. ¿Continuar? (y/n): ")
                    if confirm.lower() != 'y':
                        continue
                
                results = evaluate_series(start, end)
                create_visualization(results, f"Análisis Completo [{start}, {end}]")
                
            elif choice == '5':
                n0 = int(input("Número para demostración constructiva (>100): "))
                try:
                    steps, trajectory = prove_convergence(n0)
                    print(f"\n=== DEMOSTRACIÓN CONSTRUCTIVA EXITOSA ===")
                    print(f"n₀ = {n0} converge a 7 en {steps} pasos")
                    print(f"Trayectoria: {' → '.join(map(str, trajectory))}")
                except ValueError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error inesperado: {e}")
                
            else:
                print("Opción no válida. Intente de nuevo.")
                
        except ValueError:
            print("Error: Ingrese números válidos.")
        except Exception as e:
            print(f"Error: {e}")

def quick_test():
    """Ejecuta una prueba rápida para verificar que todo funciona"""
    print("=== PRUEBA RÁPIDA ===")
    
    # Probar función básica
    test_n = 153
    orbit, time = compute_orbit(test_n)
    print(f"F7({test_n}) converge en {time} pasos: {' → '.join(map(str, orbit))}")
    
    # Probar análisis detallado
    result = evaluate_single_number(test_n, show_trajectory=False)
    print(f"Análisis detallado: {result['steps']} pasos, satisface cotas: {result['satisfies_upper']}")
    
    print("✓ Prueba rápida completada exitosamente")

if __name__ == "__main__":
    # Ejecutar prueba rápida primero
    quick_test()
    
    # Ejecutar algunas pruebas automáticamente para mostrar resultados
    print("\nEjecutando pruebas automáticas para verificación...")
    run_predefined_tests()
    
    # Ofrecer modo interactivo
    interactive = input("\n¿Ejecutar modo interactivo? (y/n): ").strip().lower()
    if interactive == 'y':
        main_interactive()
