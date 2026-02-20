"""
Análisis exploratorio de datos de ventas.

Carga el archivo data/ventas.csv, muestra estadísticas descriptivas
y genera gráficas de ventas por producto y por mes.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Configuración ──────────────────────────────────────────────────────────────
_BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(_BASE_DIR, "..", "data", "ventas.csv")
OUTPUT_DIR = os.path.join(_BASE_DIR, "..", "output")
sns.set_theme(style="whitegrid")


def cargar_datos(ruta: str) -> pd.DataFrame:
    """Carga el CSV y devuelve un DataFrame con columnas derivadas."""
    ruta = os.path.abspath(ruta)
    if not os.path.isfile(ruta):
        raise FileNotFoundError(
            f"No se encontró el archivo de datos: {ruta}\n"
            "Asegúrate de ejecutar el script desde la raíz del proyecto."
        )
    df = pd.read_csv(ruta, parse_dates=["fecha"])
    df["total"] = df["cantidad"] * df["precio_unitario"]
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)
    return df


def mostrar_resumen(df: pd.DataFrame) -> None:
    """Imprime un resumen estadístico del DataFrame."""
    print("=== Primeras filas ===")
    print(df.head(), "\n")
    print("=== Información general ===")
    print(df.info(), "\n")
    print("=== Estadísticas descriptivas ===")
    print(df.describe(), "\n")
    print("=== Ventas totales por categoría ===")
    print(df.groupby("categoria")["total"].sum(), "\n")


def grafica_ventas_por_producto(df: pd.DataFrame) -> None:
    """Genera un gráfico de barras con el total de ventas por producto."""
    ventas = df.groupby("producto")["total"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.barplot(x=ventas.index, y=ventas.values, hue=ventas.index,
                palette="Blues_d", legend=False, ax=ax)
    ax.set_title("Ventas totales por producto")
    ax.set_xlabel("Producto")
    ax.set_ylabel("Total ($)")
    plt.tight_layout()
    salida = os.path.join(OUTPUT_DIR, "ventas_por_producto.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.savefig(salida, dpi=150)
    print(f"Gráfica guardada: {salida}")
    plt.close(fig)


def grafica_ventas_por_mes(df: pd.DataFrame) -> None:
    """Genera una línea de tiempo con el total de ventas por mes."""
    ventas = df.groupby("mes")["total"].sum()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(ventas.index, ventas.values, marker="o", linewidth=2, color="steelblue")
    ax.set_title("Evolución de ventas por mes")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Total ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    salida = os.path.join(OUTPUT_DIR, "ventas_por_mes.png")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.savefig(salida, dpi=150)
    print(f"Gráfica guardada: {salida}")
    plt.close(fig)


def main() -> None:
    df = cargar_datos(DATA_PATH)
    mostrar_resumen(df)
    grafica_ventas_por_producto(df)
    grafica_ventas_por_mes(df)


if __name__ == "__main__":
    main()
