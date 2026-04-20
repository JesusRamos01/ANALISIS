# ANALISIS

Repositorio creado para la práctica de **análisis de datos**, uso personal.

## Descripción

Proyecto de práctica con Python para explorar, limpiar y visualizar datos usando bibliotecas estándar del ecosistema de ciencia de datos.

## Estructura del proyecto

```
ANALISIS/
├── data/               # Conjuntos de datos (CSV, etc.)
│   └── ventas.csv      # Datos de ejemplo: ventas por producto
├── src/                # Scripts de análisis
│   └── analisis.py     # Análisis exploratorio de datos
├── requirements.txt    # Dependencias de Python
└── README.md
```

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/JesusRamos01/ANALISIS.git
   cd ANALISIS
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta el script de análisis:

```bash
python src/analisis.py
```

El script carga `data/ventas.csv`, muestra estadísticas descriptivas y genera gráficas de ventas por producto y por mes.

## Tecnologías

- [Python 3](https://www.python.org/)
- [pandas](https://pandas.pydata.org/) – manipulación y análisis de datos
- [matplotlib](https://matplotlib.org/) – visualización de datos
- [seaborn](https://seaborn.pydata.org/) – gráficas estadísticas