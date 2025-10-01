import numpy as np
import pandas as pd
import os

def mae():

    data = pd.read_csv("data.csv")
    df = pd.DataFrame(data)
    km = df['km']
    price = df['price']
    # Calcul de la MAE sur les données normalisées
    if os.path.exists("thetas.txt"):
        with open("thetas.txt", "r") as f:
            theta0, theta1 = map(float, f.read().split(","))
    else:
        theta0, theta1 = 0, 0
    mae = np.mean([abs(valPrice - (theta1 * valKm + theta0)) for valKm, valPrice in zip(km, price)])

    print(f"On average, my model is off by €{mae:.0f} from the predicted price.")


if __name__ == "__main__":
    mae()
