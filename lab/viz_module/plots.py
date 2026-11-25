"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x="rating", bins=20, ax=ax)
    ax.set_title("Distribuição das notas dos vinhos")
    ax.set_xlabel("Nota (rating)")
    ax.set_ylabel("Frequência")
    fig.savefig(out_path, format="png", bbox_inches="tight")
    plt.close(fig)


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    top = df["variety"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=top.values, y=top.index, ax=ax, orient="h")
    ax.set_title("Top 10 variedades por quantidade de vinhos")
    ax.set_xlabel("Quantidade de vinhos")
    ax.set_ylabel("Variedade")
    fig.savefig(out_path, format="png", bbox_inches="tight")
    plt.close(fig)


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    top_varieties = df["variety"].value_counts().head(5).index
    subset = df[df["variety"].isin(top_varieties)]
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=subset, x="variety", y="rating", order=list(top_varieties), ax=ax)
    ax.set_title("Distribuição do rating nas 5 variedades mais frequentes")
    ax.set_xlabel("Variedade")
    ax.set_ylabel("Nota (rating)")
    fig.savefig(out_path, format="png", bbox_inches="tight")
    plt.close(fig)
