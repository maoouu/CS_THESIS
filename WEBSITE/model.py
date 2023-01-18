# model.py
import pandas as pd
import pickle

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

dataset = pd.read_csv('data/features_3_sec.csv')
dataset = dataset.iloc[:, 2:]
y = dataset['label'] # target variables
X = dataset.loc[:, dataset.columns != 'label'] # feature variables

# Preprocessing
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Model
k_neighbors_model = KNeighborsClassifier(n_neighbors=3, weights='distance')
k_neighbors_model.fit(X_scaled, y)

# Save Model to disk
pickle.dump(k_neighbors_model, open('model.pkl', 'wb'))