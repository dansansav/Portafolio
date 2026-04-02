# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 16:34:56 2026

@author: danie
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np

data = pd.read_excel("Taller 5 .xlsx",sheet_name="Paso 2 Limpiar los datos")

print(data.describe().round(2))

#Grafico del histograma del sexo
sns.histplot(data=data, x="EDAD")
plt.title("Histograma")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()
#sns.countplot(data=data, x="SEXO", palette=["steelblue", "hotpink"])
#Grafico de la frecuencia del sexo
# Grafico de barras con data labels
ax = sns.countplot(
    data=data,
    x="SEXO",
    hue="SEXO",
    legend=False,
    palette=["steelblue", "hotpink"]
)

# Agregar data labels con número y porcentaje
total = len(data)
for p in ax.patches:
    porcentaje = f'{int(p.get_height())} ({p.get_height()/total*100:.1f}%)'
    ax.annotate(
        porcentaje,
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight=False
    )

plt.title("Distribución por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Frecuencia")

plt.show()

#Grafica de si tienen tiempo o no

sns.countplot(data=data, x="TIEMPO", hue="TIEMPO", legend=False, palette=["#32CD32", "#20B2AA"])
plt.title("Distribución por Tiempo")
plt.xlabel("Tiempo")
plt.ylabel("Frecuencia")
plt.show()

# Histrograma de felicidad 
sns.histplot(data=data, x="TOTAL", bins=22, color="#9A21FD")
plt.title("Histograma de Felicidad")
plt.xlabel("Felicidad")
plt.ylabel("Frecuencia")
plt.show()

#Box plot de la felicidad
sns.boxplot(
    data=data,
    y="TOTAL",
    color="steelblue",
    width=0.4,
    linewidth=1.5,
    flierprops=dict(marker="o", 
    markerfacecolor="#9A21FD", 
    markeredgecolor = "#09090B",
    markersize=7)
)

plt.title("Boxplot - Felicidad")
plt.xlabel("Total Felicidad")
plt.ylabel("")
plt.show()

#Grafico de dispersión
sns.scatterplot(data=data, x="TOTAL", y="EDAD")

plt.title("Gráfico de Dispersión")
plt.xlabel("Total felicidad")
plt.ylabel("Edad")
plt.show()

#Pasos para hacer correlacion

columna1 = data["EDAD"]
columna2 = data["TOTAL"]

# ---- PEARSON ----
pearson_r, pearson_p = stats.pearsonr(columna1, columna2)
print("=== Correlación de Pearson ===")
print(f"Coeficiente r: {pearson_r:.4f}")
print(f"Valor p:       {pearson_p:.4f}")

# ---- SPEARMAN ----
spearman_r, spearman_p = stats.spearmanr(columna1, columna2)
print("\n=== Correlación de Spearman ===")
print(f"Coeficiente r: {spearman_r:.4f}")
print(f"Valor p:       {spearman_p:.4f}")
print()
#Estadisticos
print("Estadisticos") 

# Separar por grupo
hombre = data[data["SEXO"] == "Hombre"]["TOTAL"].dropna()
mujer  = data[data["SEXO"] == "Mujer"]["TOTAL"].dropna()

def estadisticos(grupo, nombre):
    
    n          = len(grupo)
    media      = grupo.mean()
    error_std  = stats.sem(grupo)                        # Error estándar
    ic         = stats.t.interval(0.95, df=n-1,          # Intervalo de confianza 95%
                                  loc=media, scale=error_std)
    mediana    = grupo.median()
    media_rec  = stats.trim_mean(grupo, 0.05)            # Media recortada al 5%
    varianza   = grupo.var()
    desv_std   = grupo.std()
    minimo     = grupo.min()
    maximo     = grupo.max()
    rango      = maximo - minimo
    rango_iq   = stats.iqr(grupo)                        # Rango intercuartil
    asimetria  = grupo.skew()
    curtosis   = grupo.kurt()

    print(f"\n{'='*45}")
    print(f"  TOTAL DE FELICIDAD - {nombre}")
    print(f"{'='*45}")
    print(f"  Media                    {media:.4f}   Error std: {error_std:.5f}")
    print(f"  IC 95% Límite inferior   {ic[0]:.4f}")
    print(f"  IC 95% Límite superior   {ic[1]:.4f}")
    print(f"  Media recortada al 5%    {media_rec:.4f}")
    print(f"  Mediana                  {mediana:.4f}")
    print(f"  Varianza                 {varianza:.3f}")
    print(f"  Desv. estándar           {desv_std:.5f}")
    print(f"  Mínimo                   {minimo:.2f}")
    print(f"  Máximo                   {maximo:.2f}")
    print(f"  Rango                    {rango:.2f}")
    print(f"  Rango intercuartil       {rango_iq:.2f}")
    print(f"  Asimetría                {asimetria:.3f}   Error std: {error_std:.3f}")
    print(f"  Curtosis                 {curtosis:.3f}")

# Ejecutar para cada grupo
estadisticos(hombre, "Hombre")
estadisticos(mujer,  "Mujer")

# Box plot comparando la felicidad entre hombres y mujeres
sns.boxplot(
    data=data,
    x="SEXO",
    y="TOTAL",
    hue="SEXO",
    palette=["skyblue", "hotpink"],
    legend=False,
    width=0.5,
    linewidth=1.5,
    flierprops=dict(marker="o", color="red", markersize=5)
)

plt.title("Boxplot - Total de Felicidad por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Total")

plt.show()

# Box plot comparando la felicidad entre el tiempo 
sns.boxplot(
    data=data,
    x="TIEMPO",
    y="TOTAL",
    hue="TIEMPO",
    palette=["skyblue", "hotpink"],
    legend=False,
    width=0.5,
    linewidth=1.5,
    flierprops=dict(marker="o", color="red", markersize=5)
)

plt.title("Boxplot - Total de Felicidad por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Total")

plt.show()

#Blox plot de una sola variable
sns.boxplot(
    data=data,
    y="EDAD",
    color="steelblue",
    width=0.5,
    linewidth=1.5,
    flierprops=dict(marker="o", color="red", markersize=5)
)

plt.title("Boxplot - Edad del participante")
plt.xlabel("Edad del participante")
plt.ylabel("")
plt.yticks(np.arange(0, 85, 5))
plt.show()