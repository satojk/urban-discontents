import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from scipy.stats import zscore

N = 9
NUM_ATTRIBUTES = ["Population 2010", "Sq km", "income per cap", "avg prop val (residential)", "avg rent val (1 bed apt)"]

df = pd.read_csv("wide.csv", header=0, index_col=0)

# Label cities using normalized k-Means Clustering algorithm
df["Cluster"] = KMeans(n_clusters=N, random_state=0).fit(
                df[NUM_ATTRIBUTES].apply(zscore)).labels_

print(df)

print("\nShowing cities and clusters by region:")
for region in sorted(pd.unique(df["region"]), key=lambda x: x[-1]):
    print("\n\n\n\nRegion: " + region + "\n")
    print(df["Cluster"].loc[df["region"]==region].value_counts)

print("\nShowing cities and regions by cluster:")
for cluster in sorted(pd.unique(df["Cluster"])):
    print("\n\n\n\nCluster: " + str(cluster) + "\n")
    print(df["region"].loc[df["Cluster"]==cluster].value_counts)
