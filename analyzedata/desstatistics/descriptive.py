# View first 20 rows
from pandas import read_csv
from pandas import set_option

filename = '../../data/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = read_csv(filename, names=names)

# Take a look at the data
peek = data.head(20)
print(peek)

# Data dimensions
shape = data.shape
print(shape)

# Data type of each attribute
types = data.dtypes
print(types)

# Descriptive statistics
set_option('display.width', 100)
set_option('precision', 3)
description = data.describe()
print(description)

# Class Distribution
class_counts = data.groupby('class').size()
print(class_counts)

# Correlation between attributes
correlations = data.corr(method='pearson')
print(correlations)

# Skew
skew = data.skew()
print(skew)

