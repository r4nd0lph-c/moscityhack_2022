import sys
import pickle
import pandas as pd
import numpy as np
import gc
from catboost import CatBoostClassifier


def main():
    df = pd.read_csv('new_data.csv')
    model = CatBoostClassifier()
    model.load_model('model.json')
    return model.predict(data=df)


if __name__ == "__main__":
    main()
