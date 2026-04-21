# K-Means Anomaly Detection

Unsupervised anomaly detection on banking transaction data using K-means clustering.

## Overview

Processes 20,000 synthetic banking transactions with four features: initial amount, transfer amount, amount received, and final amount. Transactions are grouped into 6 clusters using K-means. Anomalies are scored using centroid distance combined with a modified Z-score (MAD-based, threshold > 4), and visualized in 2D via PCA using Plotly. Detected outliers reach Z-scores up to 587.

## Tech Stack

- Python
- scikit-learn (KMeans, StandardScaler, PCA)
- pandas, numpy
- Plotly
- Jupyter Notebook

## Setup

```bash
pip install -r requirements.txt
jupyter notebook kmeans_anomaly_detection.ipynb
```

## Results

- Dataset: 20,000 transactions
- Clusters: 6
- Anomaly threshold: modified Z-score > 4
- Maximum Z-score observed: ~587

See `reports/anomaly_detection_report.pdf` for the full analysis.
