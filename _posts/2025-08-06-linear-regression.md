---
layout: post
title: "Linear Regression"
description: "Understand linear regression from intuition to gradient descent and build a scratch Python implementation tailored for machine learning newcomers."
date: 2025-08-06
last_modified_at: 2025-10-17
categories: ML
thumbnail: /assets/images/posts/2025/linear-regression/thumbnail.webp
image: /assets/images/posts/2025/linear-regression/thumbnail.webp
inspired_by: Kazimir Malevich
---

## 📌 Introduction
Linear regression is the process of finding a line in a graph that best fits the data. It is a type of `supervised learning`, meaning it uses labeled data (datasets that already include the correct answers). It's one of the first things that people learn when starting their machine learning journey.

## 🧠 The Big Idea
{% include responsive-image.html
    src="/assets/images/posts/2025/linear-regression/linear_regression.webp"
    alt="Scatterplot of sample data with blue best-fit line representing linear regression"
%}

Just as I mentioned above, you only have to think of linear regression as fitting the best line to the data! You probably know that the equation of a line is:<br>
$y = wx + b$<br>
In this equation, $w$ is the slope (how steep the line is), and $b$ is the intercept (where the line crosses the y-axis). So to fit the line, you would have to change the $w$ and $b$ values.

## 📊 What does It Actually Do?
By fitting a line which is close to all data, we would be able to predict the $y$ values of any input $x$. Let's use house prices as an example 🏠 (it's one of the most common examples).
{% include responsive-image.html
    src="/assets/images/posts/2025/linear-regression/house_price_prediction.webp"
    alt="Scatterplot of house size versus price with regression line for predicting home values"
%}

In this graph, the white dots represent the data (e.g., a 180 m² house costing 500k), and by linear regression, we can find the blue line that best fits the data. Since we have this line, we can now predict house prices by finding the corresponding values of the line. For example, let's say that we want to predict the price of a 200 m² house. Because the equation of the line is:<br>
$\hat{y} = 2300x + 100,000$<br>

> ℹ️ Note:
>
> The symbol $\hat{y}$ (y-hat) is commonly used to denote predicted values in statistics and machine learning. This helps distinguish predicted values ($\hat{y}$) from actual outcomes ($y$) in the training data.

The predicted price of this house would be:<br>
$\hat{y} = 2300 \times 200 + 100,000 = 560,000$<br>
And voila! We've just used linear regression to predict house prices 😄

## 🔍 How Does It Learn?
You now might be curious about how we actually find the best fitting line. And that's exactly what I'm going to tell you.<br>
Finding the best fitting line is the same as finding the lowest `cost`. And the cost is measured by a `cost function`, which measures the performance (cost) of a model. There are many cost functions used for many cases, but I will use `Mean Squared Error (MSE)` (which is the default for most regression problems) to explain how linear regression learns.<br>
This is the formula for Mean Squared Error:<br>
$J(\vec{w}, b) = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2$<br>
The cost increases if the difference between the predictions ($\hat{y}$) and the actual values ($y$) are larger, and the cost decreases if the predictions ($\hat{y}$) are close to the actual values ($y$).<br>
{% include responsive-image.html
    src="/assets/images/posts/2025/linear-regression/gradient_descent_example.webp"
    alt="Contour plot illustrating gradient descent steps toward the minimum cost"
%}

We now know that we can use the cost function to evaluate the performance of the model. Now it's time for me to tell you about `gradient descent`, which is a method that allows us to minimize the cost (and eventually allow us to find the best parameters - such as the slope and the intercept of our line).<br>
Suppose you're on a hill, and say you have to go down the hill as quickly (efficiently) as possible because you really have to use the bathroom.  However, there's a problem: it's super cloudy, and you can only see things that are close to you. You'll probably take the steepest step, right? Because you'll want to go down quickly. You will repeat the process until you reach the lowest part of the hill. What you’ve just done is similar to what gradient descent does: it takes the steepest step to minimize the cost.<br>
This is the gradient descent formula for linear regression:<br>
repeat {<br>
$w = w - \alpha \dfrac{\partial J}{\partial w}$<br>
$b = b - \alpha \dfrac{\partial J}{\partial b}$<br>
}<br>
Here, $\dfrac{\partial J}{\partial w}$ and $\dfrac{\partial J}{\partial b}$ are the `gradients`. The gradients allow us to take the steepest step. $\alpha$ (alpha) is called the `learning rate`. You could think of this as the 'size' of the steps. If the learning rate is too small, linear regression learns slower, as the steps are small. However, if the learning rate is too big, it could diverge and never be able to minimize the cost. The image below visualizes what happens when the learning rate is too small or big:
{% include responsive-image.html
    src="/assets/images/posts/2025/linear-regression/learning_rate_comparison.webp"
    alt="Line chart comparing convergence for small, optimal, and large learning rates"
%}

## 🛠️ Building It From Scratch
Now that you know how linear regression learns, let's build it from scratch!<br>
We'll start by generating some sample data:
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
```text
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
Let's see what we got for the values of $w$ (slope) and $b$ (intercept):
```python
print(f"Learned parameters: w = {w:.2f}, b = {b:.2f}")
```
Output:
```text
Learned parameters: w = 2.97, b = 4.22
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
{% include responsive-image.html
    src="/assets/images/posts/2025/linear-regression/linear_regression_from_scratch_plot.webp"
    alt="Scatterplot with learned regression line from the scratch-built model"
%}

🎉 We've just built a working linear regression model without using any machine learning libraries! (just math and python)🎉

## 📚 Linear vs. Other Models
Linear regression is simply fitting a line to the data. So it works best when the data is linear. However, what if the data isn't linear? In that case, other models (such as polynomial regression) work better. The image below shows when linear regression works well and doesn't work well:
{% include responsive-image.html
    src="/assets/images/posts/2025/linear-regression/linear_vs_polynomial.webp"
    alt="Side-by-side comparison of linear and polynomial regression fits on curved datasets"
%}

If you want to explore what comes next, the [scikit-learn linear models guide](https://scikit-learn.org/stable/modules/linear_model.html){:target="_blank" rel="noopener noreferrer"} is a fantastic deep dive into production-ready tooling.

## ✅ Summary
In this blog post, we've looked at how linear regression works, when we use it, and the core concepts behind it. It's a great starting point in machine learning as gradient descent and cost functions are actually very important in many machine learning models.<br>
In the next blog post, we'll explore logistic regression, which is another important model in machine learning. See you then! And if you're ready right now, check out [Logistic Regression]({{ site.baseurl }}/2025/08/18/logistic-regression.html) to see how these ideas extend to classification tasks.
