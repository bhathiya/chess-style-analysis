import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

from sklearn.decomposition import PCA

input_file="/apps/chess/players/output/chess_all_modified_names.csv"

raw_df = pd.read_csv(input_file)
df = raw_df._get_numeric_data()
data = df.as_matrix()

labels = raw_df['Player']
uniqLabels = list(set(labels))

z = range(1,len(uniqLabels))
prism = plt.get_cmap('prism')
cNorm  = colors.Normalize(vmin=0, vmax=len(uniqLabels))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=prism)

reduced_data = PCA(n_components=2).fit_transform(data)

for i in range(len(uniqLabels)):
    indx = labels == uniqLabels[i]
    plt.scatter(reduced_data[:, 0][indx], reduced_data[:, 1][indx], s=15, color=scalarMap.to_rgba(i), label=uniqLabels[i])

x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
plt.title('PCA-reduced data')
plt.legend(loc='upper right')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()

