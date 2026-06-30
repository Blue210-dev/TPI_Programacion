import csv

# ==========================================
# 1. FUNCIONES DE CARGA Y CONTROL DE ERRORES
# ==========================================

def es_texto_valido(texto):
    # Reemplazamos los espacios vacíos para que .isalpha() no falle con nombres compuestos
    # y comprobamos que no esté vacío
    return texto.replace(" ", "").isalpha()

def cargar_datos_paises(ruta_archivo):
    #Lee el archivo CSV y carga los datos en memoria en una lista de diccionarios
    lista_paises = []
    try:
        with open(ruta_archivo, mode="r") as archivo:
            # Quitamos espacios en blanco accidentales de los encabezados
            lector_csv = csv.DictReader(archivo, skipinitialspace=True)
            
            for fila in lector_csv:
                # Controlar errores de formato en las columnas numéricas del CSV [cite: 84]
                try:
                    pais_procesado = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    }
                    lista_paises.append(pais_procesado)
                except (ValueError, KeyError):
                    print(f"⚠️ Saltando fila con formato inválido en el CSV: {dict(fila)}")
                    
        print(f"\n✅ Datos iniciales cargados con éxito. Total: {len(lista_paises)} países.")
        return lista_paises
    except FileNotFoundError:
        print(f"⚠️ Archivo '{ruta_archivo}' no encontrado. Se iniciará con una lista vacía.")
        return []

# ==========================================
# 2. FUNCIONALIDADES MÍNIMAS DEL SISTEMA [cite: 55]
# ==========================================

def agregar_pais(lista_paises):
    """Permite añadir un nuevo país validando que no haya campos vacíos."""
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    nombre = input("Nombre del país: ").strip()
    # Validamos que no esté vacío y que contenga solo letras/espacios
    if not nombre or not es_texto_valido(nombre):
        print("⚠️ Error: El nombre debe contener únicamente letras y no puede estar vacío.")
        return
        
    continente = input("Continente: ").strip()
    if not continente or not es_texto_valido(continente):
        print("⚠️ Error: El continente debe contener únicamente letras y no puede estar vacío.")
        return

    try:
        poblacion = int(input("Población (entero): "))
        superficie = int(input("Superficie en km² (entero): "))
        if poblacion < 0 or superficie < 0:
            print("⚠️ Error: Los valores numéricos no pueden ser negativos.")
            return
    except ValueError:
        print("⚠️ Error: Entrada inválida. Población y superficie deben ser números enteros.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    print(f"✅ ¡{nombre} se ha registrado correctamente en la memoria!")


def actualizar_pais(lista_paises):
    """Actualiza la Población y Superficie de un país buscando por nombre exacto."""
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    nombre_buscar = input("Ingresá el nombre exacto del país a modificar: ").strip().lower()
    
    encontrado = False
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar:
            encontrado = True
            print(f"Datos actuales -> Población: {pais['poblacion']} | Superficie: {pais['superficie']} km²")
            try:
                nueva_pob = int(input("Nueva Población: "))
                nueva_sup = int(input("Nueva Superficie en km²: "))
                if nueva_pob < 0 or nueva_sup < 0:
                    print("⚠️ Error: No se admiten valores negativos.")
                    return
                
                pais["poblacion"] = nueva_pob
                pais["superficie"] = nueva_sup
                print(f"✅ Datos de {pais['nombre']} actualizados con éxito.")
            except ValueError:
                print("⚠️ Error: Los valores deben ser números enteros.")
            break
            
    if not encontrado:
        print("⚠️ No se encontró ningún país con ese nombre exacto.")


def buscar_pais_nombre(lista_paises):
    """Busca países por coincidencia parcial o exacta en el nombre."""
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    busqueda = input("Ingresá las letras o el nombre a buscar: ").strip().lower()
    if not busqueda or not es_texto_valido(busqueda):
        print("⚠️ Error: El nombre debe contener únicamente letras y no puede estar vacío.")
        return
    
    resultados = [p for p in lista_paises if busqueda in p["nombre"].lower()]
    
    if resultados:
        print(f"\n🔍 Se encontraron {len(resultados)} resultados:")
        for p in resultados:
            print(f"• {p['nombre']} | Continente: {p['continente']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
    else:
        print("⚠️ No se encontraron países que coincidan con la búsqueda.")


def filtrar_paises(lista_paises):
    """Submenú para aplicar filtros por continente, rango de población o superficie."""
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opc = input("Elegí una opción de filtrado: ").strip()
    
    if opc == "1":
        continente = input("Ingresá el continente: ").strip().lower()
        filtrados = [p for p in lista_paises if p["continente"].lower() == continente]
    elif opc == "2" or opc == "3":
        try:
            minimo = int(input("Valor mínimo: "))
            maximo = int(input("Valor máximo: "))
            campo = "poblacion" if opc == "2" else "superficie"
            filtrados = [p for p in lista_paises if minimo <= p[campo] <= maximo]
        except ValueError:
            print("⚠️ Filtro inválido. Debés ingresar números válidos.")
            return
    else:
        print("⚠️ Opción de filtrado no válida.")
        return

    if filtrados:
        print(f"\n📋 Resultados del Filtro ({len(filtrados)} encontrados):")
        for p in filtrados:
            print(f"• {p['nombre']} ({p['continente']}) - Pob: {p['poblacion']} - Sup: {p['superficie']} km²")
    else:
        print("⚠️ No hay países que cumplan con los criterios especificados.")


def ordenar_paises(lista_paises):
    """Ordena la lista de países por Nombre, Población o Superficie (Asc / Desc)."""
    if not lista_paises:
        print("⚠️ La lista está vacía.")
        return

    print("\n--- ORDENAR PAÍSES ---")
    print("Criterio: 1. Nombre | 2. Población | 3. Superficie")
    criterio = input("Elegí el criterio (1-3): ").strip()
    
    mapa_campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if criterio not in mapa_campos:
        print("⚠️ Criterio inválido.")
        return
        
    sentido = input("¿Sentido? (1. Ascendente / 2. Descendente): ").strip()
    descendente = True if sentido == "2" else False
    
    campo_clave = mapa_campos[criterio]
    
    # Aplicamos algoritmo de ordenamiento dinámico mediante llaves [cite: 49]
    # En caso de ordenar strings (nombre), pasamos a minúsculas para evitar problemas de orden ASCII
    if campo_clave == "nombre":
        paises_ordenados = sorted(lista_paises, key=lambda x: x["nombre"].lower(), reverse=descendente)
    else:
        paises_ordenados = sorted(lista_paises, key=lambda x: x[campo_clave], reverse=descendente)
        
    print("\n📊 Lista Ordenada:")
    for p in paises_ordenados:
        print(f"• {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")


def mostrar_estadisticas(lista_paises):
    """Calcula y muestra en consola todos los indicadores estadísticos solicitados."""
    if not lista_paises:
        print("⚠️ No hay datos cargados para calcular estadísticas[cite: 85].")
        return
        
    print("\n=========================================")
    print("       ESTADÍSTICAS DEL DATASET          ")
    print("=========================================")

    # 1. País con mayor y menor población [cite: 73]
    pais_max_pob = max(lista_paises, key=lambda x: x["poblacion"])
    print(f"• Mayor Población: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']} hab.)")
    
    pais_min_pob = min(lista_paises, key=lambda x: x["poblacion"])
    print(f"• Menor Población: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']} hab.)")

    # 2. Promedios de población y superficie [cite: 75, 82]
    total_pob = sum(p["poblacion"] for p in lista_paises)
    total_sup = sum(p["superficie"] for p in lista_paises)
    cant = len(lista_paises)
    
    print(f"• Promedio de población global: {total_pob / cant:.2f} habitantes")
    print(f"• Promedio de superficie global: {total_sup / cant:.2f} km²")

    # 3. Cantidad de países por continente [cite: 83]
    frecuencia_continentes = {}
    for p in lista_paises:
        cont = p["continente"]
        frecuencia_continentes[cont] = frecuencia_continentes.get(cont, 0) + 1
        
    print("\n• Cantidad de países por continente:")
    for cont, canti in frecuencia_continentes.items():
        print(f"  - {cont}: {canti}")
    print("=========================================")


# ==========================================
# 3. CONTROLADOR / INTERFAZ DE USUARIO [cite: 56]
# ==========================================

def menu_principal():
    # Cargamos el archivo al iniciar la ejecución [cite: 12]
    dataset_paises = cargar_datos_paises(r"C:\Users\Blue\Desktop\UTN\Programacion\Integrador\paises.csv")
    
    while True:
        print("\n⚙️  SISTEMA DE GESTIÓN DE PAÍSES")
        print("1. Mostrar todos los países en memoria")
        print("2. Agregar un nuevo país ")
        print("3. Actualizar datos de un país ")
        print("4. Buscar país por nombre ")
        print("5. Filtrar países (Continente / Rangos)")
        print("6. Ordenar países (Ascendente / Descendente)")
        print("7. Ver indicadores estadísticos generales")
        print("8. Salir del programa")
        
        opcion = input("Seleccioná una opción (1-8): ").strip()
        
        if opcion == "1":
            if dataset_paises:
                print(f"\n📋 Registros actuales ({len(dataset_paises)}):")
                for p in dataset_paises:
                    print(f"• {p['nombre']} | Continente: {p['continente']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km²")
            else:
                print("La lista está vacía.")
        elif opcion == "2":
            agregar_pais(dataset_paises)
        elif opcion == "3":
            actualizar_pais(dataset_paises)
        elif opcion == "4":
            buscar_pais_nombre(dataset_paises)
        elif opcion == "5":
            filtrar_paises(dataset_paises)
        elif opcion == "6":
            ordenar_paises(dataset_paises)
        elif opcion == "7":
            mostrar_estadisticas(dataset_paises)
        elif opcion == "8":
            print("\n👋 ¡Muchas gracias por utilizar el sistema de gestión!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, ingresá un número del 1 al 8.")

if __name__ == "__main__":
    menu_principal()