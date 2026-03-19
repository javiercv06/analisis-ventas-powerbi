import pandas as pd

pd.options.display.float_format = '{:.0f}'.format

# Cargar archivo Excel
df = pd.read_excel("ventas.xlsx")

print("=== DATOS ORIGINALES ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

# Limpiar datos
df = df.dropna()

# Crear columnas nuevas
df["Ventas"] = df["Precio"] * df["Cantidad"]
df["Costo Total"] = df["Costo"] * df["Cantidad"]
df["Ganancia"] = df["Ventas"] - df["Costo Total"]

df = df.sort_values(by="Ventas", ascending=False)

print("\n=== DATOS LIMPIOS ===")
print(df.head())

# Guardar archivo limpio
df.to_csv("ventas_limpio.csv", index=False)

print("\n✅ Archivo creado: ventas_limpio.csv")

# =========================
# 🔍 ANÁLISIS DE DATOS
# =========================

print("\n=== ESTADÍSTICAS ===")
print(df.describe())

print("\n=== PRODUCTOS ===")
print(df["Producto"].unique())

print("\n=== REGIONES ===")
print(df["Región"].unique())

print("\n=== TOTAL VENTAS ===")
print(df["Ventas"].sum())

print("\n=== TOTAL GANANCIA ===")
print(df["Ganancia"].sum())

print("\n=== VENTAS POR PRODUCTO ===")
print(df.groupby("Producto")["Ventas"].sum())

print("\n=== GANANCIA POR PRODUCTO ===")
print(df.groupby("Producto")["Ganancia"].sum())