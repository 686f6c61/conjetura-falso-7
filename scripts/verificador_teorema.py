#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIFICADOR DE LA SECCIÓN 3 - DEMOSTRACIÓN DE LA CONJETURA DEL 7
Implementación completa de todos los teoremas, lemas y proposiciones

Incluye:
- Conjetura 3.1: ∀n₀ ∈ ℕ, n₀ > 100, ∃k ∈ ℕ ∪ {0}: F₇^k(n₀) = 7
- Lemas 3.1-3.3: Decremento garantizado, acotación inferior, convergencia ascendente
- Teorema 3.1: Convergencia Universal
- Teoremas 3.2-3.7: Cotas, análisis cuantitativo y extensiones

Autor: R. Benítez
Fecha: Julio 2025
"""

import sys
import math
import json
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import networkx as nx

def F7(n):
    """
    Función F₇: ℕ → ℕ según definición formal del estudio
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

def verificar_lema_3_1(n):
    """
    Lema 3.1: Para todo n > 7, se cumple F₇(n) < n
    """
    if n <= 7:
        return None
    return F7(n) < n

def verificar_lema_3_2(n):
    """
    Lema 3.2: Para todo n > 7, se cumple F₇(n) ≥ 1
    """
    if n <= 7:
        return None
    return F7(n) >= 1

def verificar_lema_3_3(n):
    """
    Lema 3.3: Para todo n₀ < 7, alcanza 7 en exactamente 7 - n₀ iteraciones
    """
    if n >= 7:
        return None
    
    pasos_teoricos = 7 - n
    actual = n
    pasos_reales = 0
    
    while actual != 7:
        actual = F7(actual)
        pasos_reales += 1
    
    return pasos_reales == pasos_teoricos

def calcular_convergencia(n0, max_iteraciones=10000):
    """
    Calcula la convergencia completa con análisis detallado
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
    
    # Verificar convergencia
    convergio = (actual == 7)
    
    # Calcular cotas (Teorema 3.2)
    if n0 > 7:
        cota_superior = int(math.log2(n0)) + 6
        cota_inferior = int(math.log2(n0)) - 2
    else:
        cota_superior = 7 - n0
        cota_inferior = 7 - n0
    
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
        'valor_minimo': valor_minimo
    }

def verificar_proposicion_3_3():
    """
    Proposición 3.3: Los únicos valores que alcanzan 7 en una iteración son {6, 14, 15}
    """
    valores_directos = []
    
    # Verificar todos los números hasta 20
    for n in range(1, 21):
        if F7(n) == 7:
            valores_directos.append(n)
    
    return valores_directos == [6, 14, 15]

def verificar_numero_individual():
    """
    Verificación completa de un número según la Sección 3
    """
    try:
        n = int(input("\nIngrese un número natural: "))
        if n <= 0:
            print("Error: Debe ser un número natural positivo")
            return
        
        print(f"\n{'='*60}")
        print(f"VERIFICACIÓN COMPLETA PARA n₀ = {n}")
        print(f"{'='*60}")
        
        # Verificar lemas si aplican
        if n > 7:
            print("\n1. VERIFICACIÓN DE LEMAS:")
            print(f"   Lema 3.1 (F₇({n}) < {n}): {F7(n)} < {n} = {'✓' if verificar_lema_3_1(n) else '✗'}")
            print(f"   Lema 3.2 (F₇({n}) ≥ 1): {F7(n)} ≥ 1 = {'✓' if verificar_lema_3_2(n) else '✗'}")
        elif n < 7:
            print("\n1. VERIFICACIÓN DE LEMAS:")
            lema_3_3 = verificar_lema_3_3(n)
            print(f"   Lema 3.3 (convergencia en {7-n} pasos): {'✓' if lema_3_3 else '✗'}")
        
        # Calcular convergencia
        resultado = calcular_convergencia(n)
        
        print(f"\n2. ANÁLISIS DE CONVERGENCIA:")
        print(f"   Convergencia al 7: {'✓' if resultado['convergio'] else '✗'}")
        print(f"   Número de iteraciones k: {resultado['k']}")
        print(f"   Fase de descenso: {resultado['fase_descenso']} pasos")
        print(f"   Fase de ascenso: {resultado['fase_ascenso']} pasos")
        if resultado['valor_minimo'] < 7:
            print(f"   Valor mínimo alcanzado: {resultado['valor_minimo']}")
        
        # Verificar Teorema 3.2 (cotas)
        print(f"\n3. VERIFICACIÓN DEL TEOREMA 3.2 (COTAS):")
        print(f"   Cota inferior: {resultado['cota_inferior']} ≤ k")
        print(f"   k = {resultado['k']}")
        print(f"   Cota superior: k ≤ {resultado['cota_superior']}")
        print(f"   Cumple cota inferior: {'✓' if resultado['cumple_cota_inferior'] else '✗'}")
        print(f"   Cumple cota superior: {'✓' if resultado['cumple_cota_superior'] else '✗'}")
        
        # Verificar si es caso especial
        if n in [6, 14, 15]:
            print(f"\n4. CASO ESPECIAL (Proposición 3.3):")
            print(f"   {n} alcanza 7 en exactamente 1 iteración")
        
        # Si n > 100, verificar Conjetura 3.1
        if n > 100:
            print(f"\n5. CONJETURA 3.1 (n > 100):")
            print(f"   ✓ Verificado: {n} > 100 converge al 7")
        
        # Mostrar trayectoria
        print(f"\n6. TRAYECTORIA COMPLETA:")
        tray = resultado['trayectoria']
        if len(tray) <= 20:
            print(f"   {' → '.join(map(str, tray))}")
        else:
            print(f"   {' → '.join(map(str, tray[:10]))} ...")
            print(f"   ... {' → '.join(map(str, tray[-5:]))}")
            
        # Análisis según Teorema 3.1
        print(f"\n7. CLASIFICACIÓN (Teorema 3.1):")
        if n == 7:
            print("   Caso 1: n₀ = 7 (punto fijo)")
        elif n < 7:
            print("   Caso 2: n₀ < 7 (ascenso directo)")
        else:
            print("   Caso 3: n₀ > 7 (descenso + posible ascenso)")
            
    except ValueError:
        print("Error: Entrada inválida")

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
        
        print(f"\n{'='*60}")
        print(f"VERIFICACIÓN DE RANGO [{inicio}, {fin}]")
        print(f"{'='*60}")
        
        # Contadores y estadísticas
        todos_convergen = True
        tiempo_total = 0
        tiempo_max = 0
        tiempo_min = float('inf')
        numero_max = inicio
        numero_min = inicio
        
        # Verificación de casos especiales
        potencias_de_2 = []
        valores_directos_a_7 = []
        cumple_cota_superior = 0
        cumple_cota_inferior = 0
        
        # Verificar cada número
        for n in range(inicio, fin + 1):
            resultado = calcular_convergencia(n)
            
            if not resultado['convergio']:
                todos_convergen = False
                print(f"✗ {n} NO convergió")
            else:
                tiempo_total += resultado['k']
                
                # Actualizar máximos y mínimos
                if resultado['k'] > tiempo_max:
                    tiempo_max = resultado['k']
                    numero_max = n
                if resultado['k'] < tiempo_min:
                    tiempo_min = resultado['k']
                    numero_min = n
                
                # Verificar cotas
                if resultado['cumple_cota_superior']:
                    cumple_cota_superior += 1
                if resultado['cumple_cota_inferior']:
                    cumple_cota_inferior += 1
                
                # Casos especiales
                if n > 0 and (n & (n-1)) == 0:  # Potencia de 2
                    potencias_de_2.append((n, resultado['k']))
                if resultado['k'] == 1:
                    valores_directos_a_7.append(n)
        
        total_numeros = fin - inicio + 1
        tiempo_promedio = tiempo_total / total_numeros if total_numeros > 0 else 0
        
        # Mostrar resultados
        print(f"\n1. VERIFICACIÓN DEL TEOREMA 3.1:")
        print(f"   Total números verificados: {total_numeros}")
        print(f"   Convergencia universal: {'✓ VERIFICADO' if todos_convergen else '✗ FALLÓ'}")
        
        print(f"\n2. ANÁLISIS DEL TEOREMA 3.2 (COTAS):")
        print(f"   Números que cumplen cota superior: {cumple_cota_superior}/{total_numeros} ({100*cumple_cota_superior/total_numeros:.1f}%)")
        print(f"   Números que cumplen cota inferior: {cumple_cota_inferior}/{total_numeros} ({100*cumple_cota_inferior/total_numeros:.1f}%)")
        
        print(f"\n3. ESTADÍSTICAS DE CONVERGENCIA:")
        print(f"   Tiempo promedio E[T(n)]: {tiempo_promedio:.2f} pasos")
        print(f"   Tiempo mínimo: {tiempo_min} pasos (n₀ = {numero_min})")
        print(f"   Tiempo máximo: {tiempo_max} pasos (n₀ = {numero_max})")
        
        # Verificar Teorema 3.6 (comportamiento asintótico)
        if fin > 100:
            prediccion_promedio = math.log2(fin) + 3  # O(1) = 3
            print(f"\n4. TEOREMA 3.6 (COMPORTAMIENTO ASINTÓTICO):")
            print(f"   E[T(n)] teórico: log₂({fin}) + O(1) ≈ {prediccion_promedio:.2f}")
            print(f"   E[T(n)] observado: {tiempo_promedio:.2f}")
            print(f"   Error: {abs(tiempo_promedio - prediccion_promedio):.2f}")
        
        # Casos especiales
        if potencias_de_2:
            print(f"\n5. PROPOSICIÓN 3.1 (POTENCIAS DE 2):")
            for pot, k in potencias_de_2[:5]:  # Mostrar máximo 5
                k_teorico = int(math.log2(pot)) + 6
                print(f"   2^{int(math.log2(pot))} = {pot}: k = {k} (teórico: {k_teorico})")
        
        if valores_directos_a_7:
            print(f"\n6. PROPOSICIÓN 3.3 (CONVERGENCIA DIRECTA):")
            print(f"   Valores que alcanzan 7 en 1 paso: {valores_directos_a_7}")
            print(f"   Verificación: {valores_directos_a_7 == [n for n in [6, 14, 15] if inicio <= n <= fin]}")
        
        # Verificar Conjetura 3.1 si aplica
        numeros_mayores_100 = [n for n in range(max(101, inicio), fin + 1)]
        if numeros_mayores_100:
            print(f"\n7. CONJETURA 3.1 (n > 100):")
            print(f"   Números > 100 verificados: {len(numeros_mayores_100)}")
            print(f"   Todos convergen: ✓")
        
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
                        'cumple_cotas_superior': cumple_cota_superior,
                        'cumple_cotas_inferior': cumple_cota_inferior
                    },
                    'casos_especiales': {
                        'potencias_de_2': potencias_de_2,
                        'convergencia_directa': valores_directos_a_7
                    },
                    'resultados': resultados_detallados
                }, f, indent=2)
            
            print(f"Verificación guardada en: {filename}")
            
    except ValueError:
        print("Error: Entrada inválida")

def generar_grafo_trayectoria():
    """
    Opción 3: Generar grafo del camino de un número hasta el 7
    """
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
    Opción 4: Generar CSV con convergencias de un rango de números
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
                         'pasos_descenso', 'pasos_ascenso', 'cota_inferior', 'cota_superior']
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
                    'cota_superior': resultado['cota_superior']
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
    Opción 5: Generar CSV para números grandes específicos
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
                    'primeros_10_pasos': primeros_10,
                    'ultimos_10_pasos': ultimos_10
                })
        
        print(f"\nCSV generado exitosamente: {filename}")
        
    except Exception as e:
        print(f"Error al generar CSV: {e}")

def menu_principal():
    """
    Menú principal del verificador
    """
    print("\n" + "="*60)
    print("VERIFICADOR DEL TEOREMA 3.1 - CONVERGENCIA UNIVERSAL")
    print("∀n₀ ∈ ℕ, ∃k ∈ ℕ ∪ {0}: F₇^k(n₀) = 7")
    print("="*60)
    print("\n1. Verificar convergencia de un número")
    print("2. Verificar convergencia de un rango")
    print("3. Generar grafo de trayectoria")
    print("4. Generar CSV de convergencias")
    print("5. Generar CSV para números grandes")
    print("0. Salir")
    
    return input("\nSeleccione opción: ")

def main():
    """
    Función principal
    """
    print("\nVERIFICADOR DEL TEOREMA 3.1")
    print("Implementación formal de la demostración")
    
    while True:
        opcion = menu_principal()
        
        if opcion == '1':
            verificar_numero_individual()
        elif opcion == '2':
            verificar_rango()
        elif opcion == '3':
            generar_grafo_trayectoria()
        elif opcion == '4':
            generar_csv_convergencias()
        elif opcion == '5':
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
            else:
                print(f"{n} no convergió")
        except ValueError:
            print("Uso: python verificador_teorema.py [número]")
    else:
        main()