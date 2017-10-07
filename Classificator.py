# Required Python Machine learning Packages
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
# For preprocessing the data
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
# To split the dataset into train and test datasets
from sklearn.cross_validation import train_test_split
# To model the Gaussian Navie Bayes classifier
from sklearn.naive_bayes import GaussianNB
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score


def learn(features, target):
    features_train, features_test, target_train, target_test = train_test_split(features,
                                                                            target, test_size=0.33, random_state=10)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(50,), random_state=1)
    clf.fit(features, target)
    joblib.dump(clf, '50hidden', compress=9)
    train_score = clf.score(features_train, target_train)
    print('train score ', train_score)
    test_score = clf.score(features_test, target_test)
    print('test score ', test_score)