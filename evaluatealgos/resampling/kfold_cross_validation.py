# Evaluate using Cross Validation
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression



# load data
filename = '../../data/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']


dataframe = read_csv(filename, names=names)

array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

num_folds = 10
seed = 7

kfold = KFold(n_splits=num_folds, random_state=seed)

model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold)

print('Accuracy: {:.5}  {:.5}'.format(results.mean()*100.0, results.std()*100.0))




