# Solicitud de datos del estudiante
print("--- REGISTRO DE ESTUDIANTE ---")
nombre = input("Ingrese el nombre completo del estudiante: ")
nie = input("Ingrese el NIE (Número de Identificación Estudiantil): ")
grado = input("Ingrese el grado (ej. 9no Grado, 1er Año): ")
seccion = input("Ingrese la sección (ej. A, B, C): ")

# Línea divisoria para ordenar la salida
print("-" * 30)

# Mostrar los datos registrados
print("\n=== DATOS REGISTRADOS ===")
print(f"Nombre:  {nombre}")
print(f"NIE:     {nie}")
print(f"Grado:   {grado}")
print(f"Sección: {seccion}")
print("=========================")