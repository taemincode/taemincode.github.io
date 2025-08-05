---
layout: post
title: "Linear Regression"
date: 2025-08-05
categories: ML
---

### 📌 Introduction
Linear regression is the process of finding a line in a graph that best fits the data. Due to it's basicness (I don't know if this is even a word - it is), linear regression is one of the first things that people learn when starting their machine learning journey.

### 📈 The Big Idea
![Linear regression example](/assets/images/posts/2025/linear-regression/linear_regression_example.png)<br>
Just as I mentioned above, you only have to think of linear regression as fitting the best line to the data! You probably know that the equation of a line is:<br>
$y = wx + b$<br>
So to fit the line, you would have to change the $w$ and $b$ values.

### 📊 What does It Actually Do?
By fitting a line which is close to all data, we would be able to predict the $y$ values of any input $x$. Let's use house prices as an example 🏠 (it's one of the most common example).
![House price prediction](/assets/images/posts/2025/linear-regression/house_price_prediction.png)
The yellow dot represent the data. For example, we could know that the price of a 180 m² house is 500k. And by linear regression, we could fit the blue line. Since we have this line, we could now predict house prices by finding the corresponding values of the line. Let's say that we want to predict the price of a 200 m² house. Because the equation of the line is:<br>
$ŷ = 2300x + 100,000$<br>

> ℹ️ Note:
> The symbol $ŷ$ (y-hat) is commonly used to denote predicted values in statistics and machine learning This distinguishes it from the actual values $y$ in our training data.

The predicted price of this house would be:<br>
$ŷ = 2300 \times 200 + 100,000 = 560,000$<br>
And voila! We've just used linear regression to predict house prices 😄