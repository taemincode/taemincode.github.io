---
layout: post
title: "Logistic Regression"
date: 2025-08-16
categories: ML
---

### 📌 Introduction
Previously, we've learned that [linear regression](/ml/2025/08/06/linear-regression.html) was fitting the best line through data. Logistic regression is fitting the best S-shaped curve. Logistic regression is also a type of `supervised learning` (has labeled data), and while linear regression is a regression model which predicts continous values for its output, logistic regression is a classification model (although it's called logistic 'regression'), which can only have two possible outputs: 0 and 1. Logistic regression is used to find out yes or no questions. Such as spam detection (is this a spam or not?), medical diagnosis (does this person have a disease or not?), and fraud detection (is this a fraudulent transactioin or not?).

### 🧠 The Big Idea
![Logistic regression example](/assets/images/posts/2025/logistic-regression/logistic_regression.png)
Instead of predicting direct values like clean your regression, logistic regression, predicts probabilities. As I mentioned above, you predict the probabilities through the S shaped curve, also called the sigmoid function or the logistic function. The equation for the sigmoid function is:<br>
$\sigma(z) = \frac{1}{1 + e^{-z}}$<br>
where<br>
$z = wx + b$<br>
From the graph above, we could notice that as the inputvalue $x$ increases the probability $x$ increases as well. Through the sigmoid function, we could separate data.

### 🧩 How It Works
Logistic regression works as follows:
1. Take input features: let's say that we have features such as study hours and we want to know if a student will pass their test based on it.
2. Compute the weighted sum: $z = w x + b$ (similar to linear regression).
3.	Apply the sigmoid function: $\hat{y} = \sigma(z) = \dfrac{1}{1 + e^{-z}}$ (this will give us a probability between 0 and 1)
4. Make a precition:
- If $\hat{y} \geq 0.5$, predict Class 1 (e.g., the student passes).
- If $\hat{y} < 0.5$, predict Class 0 (e.g., the student fails).

> ℹ️ Note:
> In $\hat{y} \geq 0.5$ and $\hat{y} < 0.5$, the value $0.5$ is called the `decision boundary`. The desicion boundary is usually 0.5, but it could be a different value based on the problem. For exmaple, if we are creating a desease detection algorithm, and this algorithm will be used to flag 'potencial' deseases, we could lower the decision boundary to let's say 0.3.

### 🔍 How Does It Learn?
We've learned we need cost functions and how we use grading descent to minimize the cost (this is explained in the [previous blog](/ml/2025/08/06/linear-regression.html)), however, if we use the same cost function as linear regression (MSE) for logistic regression, we get a cost function as below:
![MSE in linear vs logistic regression](/assets/images/posts/2025/logistic-regression/mse.png)