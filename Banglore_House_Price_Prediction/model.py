import pickle
import json
import numpy as np


# Load the model and columns

with open('banglore_home_prices_model.pickle', 'rb') as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]  # Assuming first 3 columns are not locations

def predict_price(location, sqft, bath, bhk):
    loc_index = data_columns.index(location.lower())

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

def get_location_names():
    return locations
