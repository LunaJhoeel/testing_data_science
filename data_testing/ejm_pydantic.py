import pandas as pd
from datetime import datetime
from pydantic import BaseModel, ValidationError, field_validator
from typing import Optional, List

# Cargar datos
df = pd.read_csv('/home/jhoeel/testing_data_science/datos.csv')

class Venta(BaseModel):
    producto: str
    cantidad_vendida: Optional[int] = None
    precio_unitario: float
    fecha_venta: datetime

    @field_validator('producto')
    def validar_longitud_producto(cls, valor):
        if len(valor) < 1:
            raise ValueError("El nombre del producto debe tener al menos 1 carácter.")
        return valor

    @field_validator('cantidad_vendida')
    def validar_cantidad_vendida(cls, valor):
        if valor is not None and valor < 0:
            raise ValueError("La cantidad vendida no puede ser negativa.")
        return valor

    @field_validator('precio_unitario')
    def validar_precio_unitario(cls, valor):
        if valor < 0:
            raise ValueError("El precio unitario no puede ser negativo.")
        return valor

    # Custom validator for fecha_venta
    @field_validator('fecha_venta', mode='before')
    def parse_fecha_venta(cls, valor):
        if isinstance(valor, str):
            return datetime.strptime(valor, '%Y-%m-%d')
        return valor

# Función para validar toda la DataFrame
def validar_dataframe(dataframe):
    ventas_validadas = []
    for _, fila in dataframe.iterrows():
        venta = Venta(**fila.to_dict())
        ventas_validadas.append(venta)
    return ventas_validadas

try:
    # Validar datos
    ventas_validadas = validar_dataframe(df)
    print("el formato es válido")
except ValidationError as e:
    # Manejar el error de validación
    print(f"error de validación: {e}")
