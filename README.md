# Détection d'Anomalies par K-Means

Détection d'anomalies non supervisée sur 20 000 transactions bancaires par clustering K-means.

## Méthodologie

- Normalisation des données avec StandardScaler
- Clustering K-means (6 clusters) sur les features financières
- Score d'anomalie : distance au centroïde + Z-score modifié (MAD-based, seuil > 4)
- Visualisation interactive des outliers en 2D via PCA et Plotly

## Résultats

- Jeu de données : 20 000 transactions bancaires
- Variables : montant initial, montant transféré, montant reçu, solde final
- Outliers détectés avec des Z-scores jusqu'à 587

## Stack technique

- Python, scikit-learn, Pandas, Plotly, NumPy

## Installation

```bash
pip install scikit-learn pandas plotly numpy jupyter
jupyter notebook
```
