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
Finding the best fit of a line is the same as finding the lowest `cost`. And the cost is measured by a `cost function`, which measures the performance (cost) of a model. There are many different cost functions used for many different cases, but I will use the `mean sqaured error (MSE)` (which is default for most regression problems) to exaplain how linear regression learns.<br>
This is the formula for the mean sqaured error:<br>
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