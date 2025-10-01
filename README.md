
# ft_linear_regression

Linear Regression is a fundamental machine learning technique used to predict continuous values based on input data. The model learns from a dataset by finding the line that best fits the relationship between inputs and outputs, minimizing the difference between predicted and actual values. Once trained, it can make predictions on new, unseen data, making it useful for tasks like price estimation, trend analysis, or forecasting.

## How it works

The project follows these steps to predict car prices using linear regression:

#### 1. Data Collection

We load the dataset containing car mileage (km) and price (price).

#### 2. Normalization

Both input and output values are normalized to the range [0,1] to improve training stability:

![MSE](https://latex.codecogs.com/svg.image?\large&space;{\color{White}x_{norm}=\frac{x-x_{min}}{x_{max}-x_{min}}})

![MSE](https://latex.codecogs.com/svg.image?\large&space;&space;{\color{White}y_{norm}=\frac{y-y_{min}}{y_{max}-y_{min}}})
#### 3. Mean Squared Error (MSE) Calculation

The cost function measures the average squared difference between predicted and actual values:

![MSE](https://latex.codecogs.com/svg.image?\large&space;\&space;{\color{White}J(\theta_{0},\theta_{1})=\frac{1}{n}\sum_{i=1}^{n}\left(\widehat{y_{i}}-y_{i}\right)^{2}})

#### 4. Gradient Computation

Compute the gradients of the cost function with respect to the model parameters:

**For the slope :**

![MSE](https://latex.codecogs.com/svg.image?\large&space;{\color{White}\frac{\delta&space;J}{\delta\theta_{1}}=-\frac{2}{n}\sum_{i=1}^{n}x_{i}\cdot\left(y_{i}-\left(\theta_{1x_{i}}&plus;\theta_{0}\right)\right)})

**For the intercept :**

![MSE](https://latex.codecogs.com/svg.image?\large&space;{\color{White}\frac{\delta&space;J}{\delta\theta_{0}}=-\frac{2}{n}\sum_{i=1}^{n}\left(y_{i}-\left(\theta_{1x_{i}}&plus;\theta_{0}\right)\right)})

#### 5. Update Parameters and MSE

The model parameters are updated using gradient descent:

![MSE](https://latex.codecogs.com/svg.image?\large&space;{\color{White}\theta_{1}=\theta_{1}-\alpha\frac{\delta&space;J}{\delta\theta_{1}},\theta_{0}=\theta_{0}-\alpha\frac{\delta&space;J}{\delta\theta_{0}}})

The MSE is recalculated at each iteration until convergence.

#### 6. Denormalization

The predicted values are transformed back to the original scale:

![MSE](https://latex.codecogs.com/svg.image?\large&space;{\color{White}\hat{x}=\hat{x}_{norm}\cdot\left(x_{max}-x_{min}\right)&plus;x_{min}})

![MSE](https://latex.codecogs.com/svg.image?\large&space;{\color{White}\hat{y}=\hat{y}_{norm}\cdot\left(y_{max}-y_{min}\right)&plus;y_{min}})


## Installation

Install ft_linear_regression with gcl

```bash
  git clone https://github.com/ocussy/ft_linear_regression.git ft_linear_regression
  cd ft_linear_regression
  python3 train.py
```
    
## Usage/Examples

```bash
python3 predict.py
Entrez le kilométrage de la voiture : 4000
Prix estimé pour 4000.0 km : 8413.68 €
```


## Documentation

[Wikipedia - Linear Regression](https://fr.wikipedia.org/wiki/R%C3%A9gression_lin%C3%A9aire)

[Youtube - DESCENTE DE GRADIENT](https://www.youtube.com/watch?v=rcl_YRyoLIY)

[GeeksForGeeks - Gradient Descent in Linear Regression](https://www.geeksforgeeks.org/machine-learning/gradient-descent-in-linear-regression/)

[GeeksForGeeks - Mean Squared Error](https://www.geeksforgeeks.org/maths/mean-squared-error/)


