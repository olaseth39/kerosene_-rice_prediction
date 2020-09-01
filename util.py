import json
import pickle
import numpy as np

# create variables
months = ""
data_columns = ""
model = ""


def get_estimated_price(month, year):
    try:
        month_index = data_columns.index(month.lower())

    except:
        month_index = -1

    x = np.zeros(len(data_columns))
    x[0] = year

    if month_index == 0:
        x[month_index] = 1

    return round(model.predict([x])[0], 2)


def get_month_names():
    return months      # this is just to store the months name being gotten from the json to be called from a function


def get_load_saved_artifacts():
    print("Loading saved artifacts...start")
    global data_columns
    global months
    global model

    with open("./artifacts/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        months = data_columns[1:]      # start from the month name

    with open("./artifacts/kerosene_price_prediction.pickle", "rb") as f:
        model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == "__main__":
    get_load_saved_artifacts()
    print(get_month_names())
    print(get_estimated_price('aug', 2020))
    print(get_estimated_price('july', 2021))
    print(get_estimated_price('sept', 2019))

