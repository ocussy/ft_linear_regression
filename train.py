import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def cost_function(km , price, t1, t0):
    """ calculate the cost function with 2 arguments : price and km """
    n = len(price)
    mse = 0
    for valKm, valPrice in zip(km, price):
        prediction = t1 * valKm + t0
        mse += (valPrice - prediction) ** 2
    mse = mse / n
    return mse
    
def gradient_slope(km, price, t1, t0):
    """ calculate the derivative to find the slope depending on km """
    n = len(km)
    gradient = -(2/n) * sum(km[i] * (price[i] - (t1 * km[i] + t0)) for i in range(n))
    return gradient

def gradient_intercept(km, price, t1, t0):
    """ calculate the derivative to find the slope depending on price """
    n = len(km)
    gradient = (-2/n) * sum(price[i] - (t1 * km[i] + t0) for i in range(n))
    return gradient

def linear_regression():
    """ calculate the linear regression of a dataset """
    # read of data.csv to get data
    data = pd.read_csv("data.csv")
    df = pd.DataFrame(data)
    km = df['km']
    price = df['price']

    # normalisation
    km_norm = (km - km.min()) / (km.max() - km.min())
    price_norm = (price - price.min()) / (price.max() - price.min())

    # linear regression calcul
    t1, t0 = 0, 0
    max_iterations = 1000
    iteration = 0
    # we are looking for the smallest MSE (mean square error)
    mse = cost_function(km_norm, price_norm, t1, t0)
    while mse >  0.001 and iteration < max_iterations:
        dt1 = gradient_slope(km_norm, price_norm, t1, t0)
        dt0 = gradient_intercept(km_norm, price_norm, t1, t0)
        t1 = t1 - 0.1 * dt1
        t0 = t0 - 0.1 * dt0
        mse = cost_function(km_norm, price_norm, t1, t0)
        iteration += 1

    # denormalization of t0 and t1 and write it in a txt file
    theta1 = t1 * (price.max() - price.min()) / (km.max() - km.min())
    theta0 = price.min() + (t0 * (price.max() - price.min())) - theta1 * km.min()
    with open("thetas.txt", "w") as f:
        f.write(f"{theta0},{theta1}")

    # show the data and the regression line on a graph
    plt.plot(km, price, "o")
    x_line = np.linspace(km.min(), km.max(), 100)
    y_line = theta1 * x_line + theta0
    plt.plot(x_line, y_line, 'r-', linewidth=2, label='Regression line')
    plt.xlabel('Kilometrage')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    linear_regression()