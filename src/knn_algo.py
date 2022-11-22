import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

model = KNeighborsClassifier(n_neighbors=4)
excel = pd.read_excel('crop.xlsx', header=0)


def init_model():

    global excel, model
    crop = preprocessing.LabelEncoder().fit_transform(list(excel["CROP"]))

    nitrogen = list(excel["NITROGEN"])
    phosphorus = list(excel["PHOSPHORUS"])
    potassium = list(excel["POTASSIUM"])
    temperature = list(excel["TEMPERATURE"])
    humidity = list(excel["HUMIDITY"])
    ph = list(excel["PH"])
    rainfall = list(excel["RAINFALL"])

    features = np.array([nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall])

    features = features.transpose()

    model.fit(features, crop)
    print("model initialized")


def verify(values):
    nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall = values
    if nitrogen < 1 or nitrogen > 100:
        raise ValueError('Nitrogen range error')
    if phosphorus < 1 or phosphorus > 100:
        raise ValueError('Phosphorus range error')
    if potassium < 1 or potassium > 100:
        raise ValueError('Potassium range error')
    if temperature < 1 or temperature > 60:
        raise ValueError('Temperature range error')
    if humidity < 1 or humidity > 100:
        raise ValueError('Humidity range error')
    if ph < 1 or ph > 10:
        raise ValueError('Ph range error')
    if rainfall < 0 or rainfall > 1000:
        raise ValueError('Rainfall range error')


def num_to_string(num):
    crop_name = str()
    if num == 0:
        crop_name = 'Apple'
    elif num == 1:
        crop_name = 'Banana'
    elif num == 2:
        crop_name = 'Blackgram'
    elif num == 3:
        crop_name = 'Chickpea'
    elif num == 4:
        crop_name = 'Coconut'
    elif num == 5:
        crop_name = 'Coffee'
    elif num == 6:
        crop_name = 'Cotton'
    elif num == 7:
        crop_name = 'Grapes'
    elif num == 8:
        crop_name = 'Jute'
    elif num == 9:
        crop_name = 'Kidneybeans'
    elif num == 10:
        crop_name = 'Lentil'
    elif num == 11:
        crop_name = 'Maize'
    elif num == 12:
        crop_name = 'Mang0'
    elif num == 13:
        crop_name = 'Mothbeans'
    elif num == 14:
        crop_name = 'Mungbeans'
    elif num == 15:
        crop_name = 'Muskmelon'
    elif num == 16:
        crop_name = 'Orange'
    elif num == 17:
        crop_name = 'Papaya'
    elif num == 18:
        crop_name = 'Pigeonpeas'
    elif num == 19:
        crop_name = 'Pomegranate'
    elif num == 20:
        crop_name = 'Rice'
    elif num == 21:
        crop_name = 'Watermelon'
    return crop_name


def predict_crop(values):
    verify(values)
    nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall = values

    inp = np.array([nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]).reshape(1, -1)
    prediction = num_to_string(model.predict(inp))
    return prediction
