import os

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def main():
    """ predict a cost given a mileage given with linear regression"""
    if os.path.exists("thetas.txt"):
        with open("thetas.txt", "r") as f:
            theta0, theta1 = map(float, f.read().split(","))
    else:
        theta0, theta1 = 0, 0

    # takes a mileage to do the calculus
    mileage = float(input("Entrez le kilométrage de la voiture : "))

    # do the math
    price = estimate_price(mileage, theta0, theta1)
    print(f"Prix estimé pour {mileage} km : {price:.2f} €")

if __name__ == "__main__":
    main()
