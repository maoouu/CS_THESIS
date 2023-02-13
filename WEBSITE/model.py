# model.py
import pandas as pd
import pickle

from config import DATASET_FILE
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier


class KNeighborsClassifierModel:
    def __init__(self, n_neighbors=5, weights='distance', scaler=None) -> None:
        self.n_neighbors = n_neighbors
        self.weights = weights
        self.scaler = scaler
        self.model = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights)


    def fit(self, X, y):
        if self.scaler:
            X = self.scaler.fit_transform(X)
        self.model.fit(X, y)
    

    def save(self, file_path):
        pickle.dump(self.model, open(file_path, 'wb'))


if __name__ == '__main__':
    dataset = pd.read_csv(DATASET_FILE).iloc[:, 2:]
    y = dataset['label'] # target variable
    X = dataset.loc[:, dataset.columns != 'label'] # feature variable
    scaler = MinMaxScaler()
    model = KNeighborsClassifierModel(scaler=scaler)
    model.fit(X, y)
    model.save('model.pkl')