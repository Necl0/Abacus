from sklearn.datasets import fetch_openml
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import pandas as pd

# load MNIST dataset
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist["data"], mnist["target"]
y = y.astype(np.uint8)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

param_grid = [
    {'weights': ['uniform', 'distance'], 'n_neighbors': [i for i in range(1, 10)]}
]

# grid search to find best hyperparameters
knn_clf = KNeighborsClassifier()

grid_search = GridSearchCV(knn_clf, param_grid, cv=3, verbose=3)
grid_search.fit(X_train, y_train)

knn_clf = grid_search.best_estimator_

# run model on test set
y_pred = knn_clf.predict(X_test)

# analyze model results
print(confusion_matrix(y_test, y_pred))
print(f"\n\nPrecision Score: {precision_score(y_test, y_pred, average='micro')}")
print(f"\n\nBest Hyperparameters: {grid_search.best_params_}")


# save model in model.pkl
with open('model.pkl', 'wb') as f:
    pickle.dump(knn_clf, f)
