 #Load the library with the iris dataset
from sklearn.datasets import load_iris

# Load scikit's random forest classifier library
from sklearn.ensemble import RandomForestClassifier

# Load pandas
import pandas as pd

# Load numpy
import numpy as np

# Set random seed
np.random.seed(0)

# Create an object called iris with the iris data
iris = load_iris()

# Create a dataframe with the four feature variables
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# View the top 5 rows
#print(df.head(5))

# Add a new column with the species names, this is what we are going to try to predict
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# View the top 5 rows
#print(df.head(5))



# Create a new column that for each row, generates a random number between 0 and 1, and
# if that value is less than or equal to .75, then sets the value of that cell as True
# and false otherwise. This is a quick and dirty way of randomly assigning some rows to
# be used as the training data and some as the test data.
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

# View the top 5 rows
print(df.head(2))



# Create two new dataframes, one with the training rows, one with the test rows
train, test = df[df['is_train']==True], df[df['is_train']==False]
# Show the number of observations for the test and training dataframes
print('Number of observations in the training data:', len(train))
print('Number of observations in the test data:',len(test))


# Create a list of the feature column's names
features = df.columns[:4]

# View features
print(features)


# train['species'] contains the actual species names. Before we can use it,
# we need to convert each species name into a digit. So, in this case there
# are three species, which have been coded as 0, 1, or 2.
y = pd.factorize(train['species'])[0]


#print(y)

# Create a random forest Classifier. By convention, clf means 'Classifier'
clf = RandomForestClassifier(n_jobs=2, random_state=0)


# Train the Classifier to take the training features and learn how they relate
# to the training y (the species)
clf.fit(train[features], y)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=10, n_jobs=2, oob_score=False, random_state=0,
            verbose=0, warm_start=False)


# Apply the Classifier we trained to the test data (which, remember, it has never seen before)
print(clf.predict(test[features]))
# View the predicted probabilities of the first 10 observations
print(clf.predict_proba(test[features])[0:10])

# Create actual english names for the plants for each predicted plant class
preds = iris.target_names[clf.predict(test[features])]
# View the PREDICTED species for the first five observations
#print(preds[0:5])

# View the ACTUAL species for the first five observations
test['species'].head()
# Create confusion matrix
ct=pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species'])
print(ct)
'''

# View a list of the features and their importance scores
list(zip(train[features], clf.feature_importances_))
'''
