"""
===========================================================
A demo of K-Means clustering on the handwritten digits data
===========================================================

In this example we compare the various initialization strategies for
K-means in terms of runtime and quality of the results.

As the ground truth is known here, we also apply different cluster
quality metrics to judge the goodness of fit of the cluster labels to the
ground truth.

Cluster quality metrics evaluated (see :ref:`clustering_evaluation` for
definitions and discussions of the metrics):

=========== ========================================================
Shorthand    full name
=========== ========================================================
homo         homogeneity score
compl        completeness score
v-meas       V measure
ARI          adjusted Rand index
AMI          adjusted mutual information
silhouette   silhouette coefficient
=========== ========================================================

"""
print(__doc__)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

from sklearn.decomposition import PCA

#input_file="/apps/chess/players/output/chess_all_modified.csv"
input_file="/apps/chess/players/output/chess_all_modified_names.csv"

np.random.seed(42)

raw_df = pd.read_csv(input_file)
df = raw_df._get_numeric_data()
data = df.as_matrix()

labels = raw_df['Player']
uniqLabels = list(set(labels))

# Set the color map to match the number of species
z = range(1,len(uniqLabels))
prism = plt.get_cmap('prism')
cNorm  = colors.Normalize(vmin=0, vmax=len(uniqLabels))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=prism)

reduced_data = PCA(n_components=2).fit_transform(data)

# Plot each species
for i in range(len(uniqLabels)):
    indx = labels == uniqLabels[i]
    print(reduced_data[:, 0][indx], reduced_data[:, 1][indx])
    plt.scatter(reduced_data[:, 0][indx], reduced_data[:, 1][indx], s=15, color=scalarMap.to_rgba(i), label=uniqLabels[i])

x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
plt.title('PCA-reduced data')
plt.legend(loc='upper right')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()

