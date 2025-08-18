---
layout: post
title: "Logistic Regression"
date: 2025-08-16
categories: ML
---

### 📌 Introduction
Previously, we've learned that [linear regression](/ml/2025/08/06/linear-regression.html) was fitting the best line through data. Logistic regression is fitting the best S-shaped curve. Logistic regression is also a type of `supervised learning` (has labeled data), and while linear regression is a regression model which predicts continuous values for its output, logistic regression is a classification model (although it's called logistic 'regression'), which can only have two possible outputs: 0 and 1. This model is used to find out yes or no questions. Such as spam detection (is this a spam or not?), medical diagnosis (does this person have a disease or not?), and fraud detection (is this a fraudulent transaction or not?).

### 🧠 The Big Idea
![Logistic regression example](/assets/images/posts/2025/logistic-regression/logistic_regression.png)
Instead of predicting direct values like clean your regression, logistic regression, predicts probabilities. As I mentioned above, you predict the probabilities through the S shaped curve, also called the sigmoid function or the logistic function. The equation for the sigmoid function is:<br>
$\sigma(z) = \frac{1}{1 + e^{-z}}$<br>
where<br>
$z = wx + b$<br>
From the graph above, we could notice that as the input value $x$ increases the probability $x$ increases as well. Through the sigmoid function, we could separate data.

### 🧩 How It Works
Logistic regression works as follows:
1. Take input features: let's say that we have features such as study hours, and we want to know if a student will pass their test based on it.
2. Compute the weighted sum: $z = w x + b$ (similar to linear regression).
3.	Apply the sigmoid function: $\hat{y} = \sigma(z) = \dfrac{1}{1 + e^{-z}}$ (this will give us a probability between 0 and 1)
4. Make a prediction:
- If $\hat{y} \geq 0.5$, predict Class 1 (e.g., the student passes).
- If $\hat{y} < 0.5$, predict Class 0 (e.g., the student fails).

> ℹ️ Note:
> In $\hat{y} \geq 0.5$ and $\hat{y} < 0.5$, the value $0.5$ is called the `decision boundary`. The decision boundary is usually 0.5, but it could be a different value based on the problem. For example, if we are creating a disease detection algorithm, and this algorithm will be used to flag 'potential' diseases, we could lower the decision boundary to let's say 0.3.

### 🔍 How Does It Learn?
We've learned that we need cost functions in order to use gradient descent to find the best fitting graph in the data (this is explained in the [previous blog](/ml/2025/08/06/linear-regression.html)). However, if we use the same cost function as linear regression (MSE) for logistic regression, we get a cost function as below:
![MSE in linear vs logistic regression](/assets/images/posts/2025/logistic-regression/mse.png)
As you could see, while the cost function plot for linear regression is a smooth convex, the cost function plot for logistic regression is a wiggly non-convex. This makes it hard to reach the global minimum as there would be lots of local minima that gradient descent can be stuck in. So, let me introduce a cost function for logistic regression: Binary Cross-Entropy (also called Log Loss)! This is the formula of binary cross-entropy:<br><br>
$$
J(w, b) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log\big(\hat{y}^{(i)}\big) + \big(1 - y^{(i)}\big) \log\big(1 - \hat{y}^{(i)}\big) \Big]
$$
<br><br>
It looks very complicated, right? Let's dive in to the specific details so that you will eventually understand what's happening in this formula.<br>
First, you have to understand the difference between a `cost` and a `loss`. The main difference is that loss is for only one example and cost is for all the examples (the sum of all the loss). The formula for binary cross entropy derives from this formula for calculating a single loss:<br>
$$
L\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right),\, y^{(i)}\right) =
\begin{cases}
    -\log\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right) & \text{if } y^{(i)} = 1 \\\\
    -\log\left(1 - f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right) & \text{if } y^{(i)} = 0
\end{cases}
$$<br><br>
This is the plot for $-\log\left(f\right)$ and $-\log\left(1 - f\right)$:
![Log plot](/assets/images/posts/2025/logistic-regression/log_plot.png)
As you can see, in $-\log\left(f\right)$, as the value of $f$ get's closer to 0, the loss increases. That's why we use this function if $y^{(i)} = 1$ (becuase we want to have high loss when our prediction is far from the actual ground truth). Similarly, we use $-\log\left(1 - f\right)$ if $y^{(i)} = 0$ because we want to have low loss when the prediction is close to 0 and have high loss when it's close to 1. The formula for calculating a single loss can be writen in a more compact form like this:<br><br>
$$
L\left(f_{\vec{w},b}\!\left(\vec{x}^{(i)}\right),\, y^{(i)}\right)
= - \Big[ y^{(i)} \log\!\big(f_{\vec{w},b}(\vec{x}^{(i)})\big) + \big(1-y^{(i)}\big) \log\!\big(1 - f_{\vec{w},b}(\vec{x}^{(i)})\big) \Big]
$$<br><br>
> ℹ️ Note:
> When $y^{(i)} = 1$, $\big(1-y^{(i)}\big) \log\big(1 - f_{\vec{w},b}(\vec{x}^{(i)})\big)$ cancels out, leaving us with $- y^{(i)} \log\big(f_{\vec{w},b}(\vec{x}^{(i)})\big)$. Vice versa.

Finally, if we add all the loss to find out the loss, we get this formula (same as the one above):<br><br>
$$
J(w, b) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log\big(\hat{y}^{(i)}\big) + \big(1 - y^{(i)}\big) \log\big(1 - \hat{y}^{(i)}\big) \Big]
$$<br><br>
Since we have the cost function, we can now use gradient decsent to minimize the cost (I'm thinking about writting a blog post about explaining the details of gradient descent - like backpropagation - in the future) and find the best fitting S-shaped curve.