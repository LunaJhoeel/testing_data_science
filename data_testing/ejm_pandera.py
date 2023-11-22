import pandera as pa
from pandera import Column, DataFrameSchema, Check
import pandas as pd

# Cargar datos
df = pd.read_csv('/home/jhoeel/testing_data_science/datos.csv')

# Convertir la columna fecha a datetime
df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])

# Esquema de validación con Pandera
schema = DataFrameSchema({
    "producto": Column(str, checks=Check.str_length(min_value=1)),
    "cantidad_vendida": Column(int, checks=Check.ge(0), nullable=True),
    "precio_unitario": Column(float, checks=Check.ge(0)),
    "fecha_venta": Column(pd.Timestamp)
})

try:
    # Validar datos
    validated_df = schema(df)

    # Si la validación es exitosa, imprimir mensaje personalizado
    print("Está bien, el formato es válido")
except pa.errors.SchemaError as e:
    # Manejar el error de validación
    print(f"Error de validación: {e}")
