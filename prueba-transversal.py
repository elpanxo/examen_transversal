import random
import csv 

# Datos iniciales
trabajadores = [
    "Juan Pérez","Maria Garcia","Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández","Miguel Sánchez",
    "Isabel Gómez","Francisco Díaz","Elena Fernández"
]

sueldos = []

# Funcion para asignar sueldos aleatorios 
def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos aleatorios asignados.")

# Funcion para clasificar sueldos y mostrar reporte
def clasificar_y_mostrar_reporte():
    if not sueldos:
        print("Aun no se han asignado los sueldos.")
        return
    
    # Clasificacion de sueldos
    sueldo_menor_800000 = []
    sueldo_entre_800000_y_2000000 = []
    sueldo_mayor_2000000 = []

    for i in range(10):
        if sueldos[i] < 800000:
            sueldo_menor_800000.append((trabajadores[i], sueldos[i]))
        elif sueldos[i] >= 800000 and sueldos[i] <= 2000000:
            sueldo_entre_800000_y_2000000.append((trabajadores[i], sueldos[i]))
        elif sueldos[i] > 2000000:
            sueldo_mayor_2000000.append((trabajadores[i], sueldos[i]))

    # Mostrar clasificación
    print("Sueldos menores a $800.000 TOTAL: ", len(sueldo_menor_800000))
    mostrar_sueldo_empleados(sueldo_menor_800000)
    print("Sueldos entre $800.000 y $2.000.000: ", len(sueldo_entre_800000_y_2000000))
    mostrar_sueldo_empleados(sueldo_entre_800000_y_2000000)
    print("Sueldos superiores a $2.000.000: ", len(sueldo_mayor_2000000))
    mostrar_sueldo_empleados(sueldo_mayor_2000000)

    # Total de sueldos
    total_sueldos = sum(sueldos)
    print(f"TOTAL SUELDOS: ${total_sueldos}")

# Funcion para mostrar el sueldo de cada empleado
def mostrar_sueldo_empleados(lista):
    for empleado, sueldo in lista:
        print(f"{empleado}")
        print(f"Sueldo: ${sueldo}")
        print(" ")

def ver_estadisticas():
    if not sueldos:
        print("Aun no se han asignado los sueldos.")
        return
    
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    media_geometrica = 1
    for sueldo in sueldos:
        media_geometrica *= sueldo
    media_geometrica **= (1 / len(sueldos))

    print(f"Sueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldo: ${promedio_sueldos}:.2f")
    print(f"Media gemetrica de sueldos: ${media_geometrica:.2f}")

# Funcion para generar reporte de sueldo con descuento
def generar_reporte_csv():
    if not sueldos:
        print("Aun no se han asignado los sueldos.")
        return
    
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Nombre empleado', 'Sueldo base', 'Descuento salud', 'Descuento AFP', 'Sueldo líquido'])

    for i in range(10):
        sueldo_base = sueldos[i]
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp

        writer.writerow([trabajadores[i], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])

        print("Reporte de sueldos generado y guardado en 'reporte_sueldos.csv'." )

# Menu principal de opciones
while True:
    print("--- Menu principal ---")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldo")
    print("5. Salir del programa")

    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
        asignar_sueldos_aleatorios()
    elif opcion == '2':
        clasificar_y_mostrar_reporte
    elif opcion == '3':
        ver_estadisticas
    elif opcion == '4':
        generar_reporte_csv
    elif opcion == '5':
        print("Saliendo del programa...")
        print("Desarrollado por Francisco Agüero")
        print("21.062.893-2")
        break
    else:
        print("Opción no valida. Intente de nuevo")