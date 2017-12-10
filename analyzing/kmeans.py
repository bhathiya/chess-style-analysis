import numpy as np
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn import metrics
from time import time

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

kmeans = KMeans(init='k-means++', n_clusters=5, n_init=50)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(42 * '-')
    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Cluster label')

def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)

    print(82 * '-')
    print('init\t\ttime\tinertia\thomo\tcompl\tv-meas\tARI\tAMI\tsilhouette')
    print(82 * '-')
    print('%-9s\t%.2fs\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=len(data[:,0]))))
    print(82 * '-')
    print()


bench_k_means(kmeans, 'K Means', data)

# Compute confusion matrix
dat = pd.DataFrame({'Labels': labels.values, 'Clusters': kmeans.labels_})
ct = pd.crosstab(dat['Labels'], dat['Clusters'])
print(ct)

np.set_printoptions(precision=2)
print()

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(ct.as_matrix(), classes=uniqLabels,
                      title='Confusion matrix, without normalization')
print()

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(ct.as_matrix(), classes=uniqLabels, normalize=True,
                      title='Normalized confusion matrix')

data = PCA(n_components=2).fit_transform(data)

plt.figure()
for i in range(len(uniqLabels)):
    indx = labels == uniqLabels[i]
    plt.scatter(data[:, 0][indx], data[:, 1][indx], s=15, color=scalarMap.to_rgba(i), label=uniqLabels[i])

x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
plt.title('PCA-reduced data')
plt.legend(loc='upper right')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()

