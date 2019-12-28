# Feature Extraction with PCA
from pandas import read_csv
from sklearn.decomposition import PCA


# load data
filename = '../../data/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = read_csv(filename, names=names)

array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)

# summarize components
print('Explained Variance: {}'.format(fit.explained_variance_ratio_))
print(fit.components_)