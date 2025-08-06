---
layout: post
title: "Linear Regression"
date: 2025-08-05
categories: ML
---

### 📌 Introduction
Linear regression is the process of finding a line in a graph that best fits the data. Due to it's basicness (I don't know if this is even a word - it is), linear regression is one of the first things that people learn when starting their machine learning journey.

### 📈 The Big Idea
![Linear regression example](/assets/images/posts/2025/linear-regression/linear_regression.png)<br>
Just as I mentioned above, you only have to think of linear regression as fitting the best line to the data! You probably know that the equation of a line is:<br>
$y = wx + b$<br>
So to fit the line, you would have to change the $w$ and $b$ values.

### 📊 What does It Actually Do?
By fitting a line which is close to all data, we would be able to predict the $y$ values of any input $x$. Let's use house prices as an example 🏠 (it's one of the most common example).
![House price prediction](/assets/images/posts/2025/linear-regression/house_price_prediction.png)
The yellow dot represent the data. For example, we could know that the price of a 180 m² house is 500k. And by linear regression, we could fit the blue line. Since we have this line, we could now predict house prices by finding the corresponding values of the line. Let's say that we want to predict the price of a 200 m² house. Because the equation of the line is:<br>
$\hat{y} = 2300x + 100,000$<br>

> ℹ️ Note:
> The symbol $\hat{y}$ (y-hat) is commonly used to denote predicted values in statistics and machine learning This distinguishes it from the actual values $y$ in our training data.

The predicted price of this house would be:<br>
$\hat{y} = 2300 \times 200 + 100,000 = 560,000$<br>
And voila! We've just used linear regression to predict house prices 😄

### 🔍 How Does It Learn?
You now might be curious about how we actually fit the best line. And that's what I'm going to tell you.<br>
Finding the best fit of a line is the same as finding the lowest `cost`. And the cost is measured by a `cost function`, which measures the performance (cost) of a model. There are many different cost functions used for many different cases, but I will use `Mean Sqaured Error (MSE)` (which is default for most regression problems) to exaplain how linear regression learns.<br>
This is the formula for Mean Sqaured Error:<br>
$J(\vec{w}^{\}, b) = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2$<br>
The cost increases if the difference between the predictions ($\hat{y}$) and the actual values ($y$) are larger, and the cost decreases if the the predictions ($\hat{y}$) are close to the actual values ($y$).<br>
![Gradient descent exampe](/assets/images/posts/2025/linear-regression/gradient_descent_example.png)
We now know that we could use the cost function to evaluate the performance of the model. Now it's time for me to tell you about `gradient descent`, which is a method allows us to minimize the cost (and eventually allow us to find the best parameters - such as the slope and the intercept of our line).<br>
Suppose you're on a hill ⛰️, and say you have to go down the hill as quickly (efficiently) as possible because you really have to use the bathroom 🚽.  However, there's a problem: it's super cloudy ☁️, and you can only see things that are close to you. You'll probably take the steepest step, right? Because you'll want to go down quickly. You will repeat the process until you reach the lowest part of the hill. What you've just did is what gradient descent does minimize the cost (to go to the lowest part of the cost surface)!<br>
This is the gradient descent formula for linear regression:<br>
repeat {<br>
$w = w - \alpha \dfrac{\partial J}{\partial w}$<br>
$b = b - \alpha \dfrac{\partial J}{\partial b}$<br>
}<br>
Here, $\dfrac{\partial J}{\partial w}$ and $\dfrac{\partial J}{\partial b}$ are the `gradients`. The gradients allow us to take the steepest step. $\alpha$ (alpha) is called the `learning rate`. You could think of this as the 'size' of the steps. If the learning rate is too small, linear regression learns slower, as the steps are small. However, if the learning rate is too big, it could diverge and never be able to minimize the cost. The image below visualizes what happens when the learning rate is too small or big:
![Learning rate comparison](/assets/images/posts/2025/linear-regression/learning_rate_comparison.png)

### 🛠️ Building It From Scratch
Now that you know how linear regression learns, let's know build it from scratch!<br>
Let's start building by generating some sample data:
```python
import numpy as np

# Fake dataset: y = 4 + 3x + noise
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
```
Our goal is to find the best value for $w$ and $b$. At first, we can just set them to zero:
```python
w = 0.0
b = 0.0
```
Now, let's define the cost function. We'll use Mean Squared Error (MSE):
```python
def compute_loss(X, y, w, b):
    y_pred = w * X + b
    return np.mean((y - y_pred) ** 2)
```
We'll now use gradient descent to minimize the cost:
```python
learning_rate = 0.05
epochs = 1000 # number of iterations
n = len(X)

for epoch in range(epochs):
    y_pred = w * X + b
    error = y_pred - y

    dw = (2/n) * np.sum(error * X)
    db = (2/n) * np.sum(error)

    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 100 == 0:
        loss = compute_loss(X, y, w, b)
        print(f"Epoch {epoch}: Loss = {loss:.4f}")
```
Output:
```bash
Epoch 0: Loss = 34.0180
Epoch 100: Loss = 1.0010
Epoch 200: Loss = 0.9928
Epoch 300: Loss = 0.9925
Epoch 400: Loss = 0.9924
Epoch 500: Loss = 0.9924
Epoch 600: Loss = 0.9924
Epoch 700: Loss = 0.9924
Epoch 800: Loss = 0.9924
Epoch 900: Loss = 0.9924
```
Finally, let's see how well our line fits the data:
```python
import matplotlib.pyplot as plt

plt.scatter(X, y, label='Data')
plt.plot(X, w * X + b, color='red', label='Best Fit Line')
plt.legend()
plt.title("Linear Regression from Scratch")
plt.show()
```
Output:<br>
![Gradient descent plot](/assets/images/posts/2025/linear-regression/gradient_descent_plot.png)<br>
🎉 We've just build a working linear regression model without using any machine learning libraries! (just math and python)🎉

### 📚 Linear vs. Other Models
Linear regression is simply fitting a line into the data. So it works best when the data is linear. However, what if the data isn't linear? In that case, other models (such as polynomial regression) works better. The image below shows when linear regression work well and doesn't work well:
![Linear vs polynomial](/assets/images/posts/2025/linear-regression/linear_vs_polynomial.png)<br>