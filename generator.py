import csv
from typing import List, Dict

# Crear datos de ejemplo para 25 filas (reciclando los datos)
data_dict: Dict[str, List] = {
    "producto": ["A", "B", "C", "D"] * 6,
    "cantidad_vendida": [100, 50, 200, "trescientos"] * 6,
    "precio_unitario": [10.5, 15.2, 9.8, 12.0] * 6,
    "fecha_venta": ["2022-01-15", "2022-02-20", "2022-03-25", "2022-04-30"] * 6
}

# Crear un archivo CSV
with open('datos.csv', 'w', newline='') as csvfile:
    fieldnames = data_dict.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    # Escribir 25 filas de datos reciclando los datos
    for i in range(25):
        row_data = {key: data_dict[key][i % 4] for key in fieldnames}
        writer.writerow(row_data)

print("Archivo CSV creado exitosamente.")
