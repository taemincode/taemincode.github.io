---
layout: post
title: "Logistic Regression"
date: 2025-08-18
categories: ML
---

## 📌 Introduction
Previously, we've learned that [linear regression](/ml/2025/08/06/linear-regression.html) was fitting the best line through data. Logistic regression fits an S-shaped curve (sigmoid function) to the data. Logistic regression is also a type of `supervised learning` (has labeled data), and while linear regression is a regression model which predicts continuous values for its output, logistic regression is a classification model (although it's called logistic 'regression'), which can only have two possible outputs: 0 and 1. This model is used to find out yes or no questions. Such as spam detection (is this a spam or not?), medical diagnosis (does this person have a disease or not?), and fraud detection (is this a fraudulent transaction or not?).

## 🧠 The Big Idea
![Logistic regression example](/assets/images/posts/2025/logistic-regression/logistic_regression.png)
Instead of predicting continuous values like linear regression, logistic regression predicts probabilities. As I mentioned above, you predict the probabilities through the S-shaped curve, also called the sigmoid function or the logistic function. The equation for the sigmoid function is:<br>
$\sigma(z) = \frac{1}{1 + e^{-z}}$<br>
where<br>
$z = wx + b$<br>
From the graph above, we could notice that as the input value $x$ increases, the predicted probability increases as well. Through the sigmoid function, we could separate data.

## 🧩 How It Works
Logistic regression works as follows:
1. Take input features: in this example, let's create an algorithm that predicts if a student will pass their test based on study hours. 
2. Compute the weighted sum: $z = w x + b$ (similar to linear regression).
3.	Apply the sigmoid function: $\hat{y} = \sigma(z) = \dfrac{1}{1 + e^{-z}}$ (this will give us a probability between 0 and 1)
4. Make a prediction:
- If $\hat{y} \geq 0.5$, predict Class 1 (e.g., the student passes).
- If $\hat{y} < 0.5$, predict Class 0 (e.g., the student fails).

> ℹ️ Note:
> In $\hat{y} \geq 0.5$ and $\hat{y} < 0.5$, the value $0.5$ is called the `decision boundary`. The decision boundary is usually 0.5, but it could be a different value based on the problem. For example, if we are creating a disease detection algorithm, and this algorithm will be used to flag 'potential' diseases, we could lower the decision boundary to let's say 0.3.

## 🔍 How Does It Learn?
We've learned that we need cost functions in order to use gradient descent to find the best fitting graph in the data (this is explained in the [previous blog](/ml/2025/08/06/linear-regression.html)). However, if we use the same cost function as linear regression (MSE) for logistic regression, we get a cost function as below:
![MSE in linear vs logistic regression](/assets/images/posts/2025/logistic-regression/mse.png)
As you could see, while the cost function plot for linear regression is a smooth convex, the cost function plot for logistic regression is a wiggly non-convex. This makes it hard to reach the global minimum since there are many local minima where gradient descent can get stuck. Instead, we use a different cost function: Binary Cross-Entropy (also called Log Loss)! This is the formula of binary cross-entropy:<br><br>
$$
J(w, b) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log\big(\hat{y}^{(i)}\big) + \big(1 - y^{(i)}\big) \log\big(1 - \hat{y}^{(i)}\big) \Big]
$$
<br><br>
It looks very complicated, right? Let's dive in to the specific details so that you will eventually understand what's happening in this formula.<br>
First, you have to understand the difference between a `cost` and a `loss`. The main difference is that loss is for only one example and cost is for all the examples (the sum of all the loss). The formula for binary cross entropy derives from this formula for calculating a single loss:<br><br>
$$
L\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right),\, y^{(i)}\right) =
\begin{cases}
    -\log\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right) & \text{if } y^{(i)} = 1 \\\\
    -\log\left(1 - f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right) & \text{if } y^{(i)} = 0
\end{cases}
$$<br><br>
This is the plot for $-\log\left(f\right)$ and $-\log\left(1 - f\right)$:
![Log plot](/assets/images/posts/2025/logistic-regression/log_plot.png)
As you can see, in $-\log\left(f\right)$, as the value of $f$ get's closer to 0, the loss increases. That's why we use this function if $y^{(i)} = 1$ (because we want to have high loss when our prediction is far from the actual ground truth). Similarly, we use $-\log\left(1 - f\right)$ if $y^{(i)} = 0$ because we want to have low loss when the prediction is close to 0 and have high loss when it's close to 1. The formula for calculating a single loss can be writen in a more compact form like this:<br><br>
$$
L\big(f_{\vec w, b}(\vec x^{(i)}), y^{(i)}\big) = - \Big[ y^{(i)} \log \hat y^{(i)} + (1 - y^{(i)}) \log \big(1 - \hat y^{(i)}\big) \Big]
$$<br><br>
> ℹ️ Note:
> When $y^{(i)} = 1$, $\big(1-y^{(i)}\big) \log\big(1 - f_{\vec{w},b}(\vec{x}^{(i)})\big)$ cancels out, leaving us with $- y^{(i)} \log\big(f_{\vec{w},b}(\vec{x}^{(i)})\big)$; and similarly when $y^{(i)} = 0$.

Finally, if we add all the individual losses to find out the cost, we get this formula (same as the one above):<br><br>
$$
J(w, b) = -\frac{1}{m} \sum_{i=1}^{m} \Big[ y^{(i)} \log\big(\hat{y}^{(i)}\big) + \big(1 - y^{(i)}\big) \log\big(1 - \hat{y}^{(i)}\big) \Big]
$$ <br><br>
Since we have the cost function, we can now use gradient descent to minimize the cost (I'm thinking about writing a blog post about explaining the details of gradient descent - like backpropagation - in the future) and find the best fitting S-shaped curve.

## 🛠️ Building It From Scratch
Let's build a logistic regression model for a simple binary task where it predicts if a student passes (1) or fails (0) a test based on hours spent studying.<br>
We'll create data so that studying more hours will increase the probability of passing:
```python
import numpy as np

# Reproducibility
np.random.seed(0)

# Toy data: hours studied between 0 and 10
n = 200
X = np.random.uniform(0, 10, size=(n, 1))

# True (hidden) relationship used to generate labels
# pass_prob = sigmoid(w_true * hours + b_true)
w_true = 0.8
b_true = -4.0

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

pass_prob = sigmoid(w_true * X + b_true)

# Sample pass/fail labels from the probability
y = (np.random.rand(n, 1) < pass_prob).astype(np.float64)
```
Now, let's define the model, the cost function, and computing the gradients:
```python
def predict_proba(X, w, b):
    return 1 / (1 + np.exp(-(w * X + b)))

def compute_loss(X, y, w, b, eps=1e-12):
    p = predict_proba(X, w, b)
    # Binary cross-entropy
    return -np.mean(y * np.log(p + eps) + (1 - y) * np.log(1 - p + eps))

def compute_gradients(X, y, w, b):
    n = len(X)
    p = predict_proba(X, w, b)
    error = p - y
    dw = (1 / n) * np.sum(error * X)
    db = (1 / n) * np.sum(error)
    return dw, db
```
Let's now train the model with gradient descent:
```python
# Initialize parameters
w = 0.0
b = 0.0

learning_rate = 0.1
epochs = 2000

for epoch in range(epochs):
    dw, db = compute_gradients(X, y, w, b)
    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 200 == 0:
        loss = compute_loss(X, y, w, b)
        print(f"Epoch {epoch}: Loss = {loss:.4f}")

# Learned parameters
print(f"Learned parameters: w = {w:.2f}, b = {b:.2f}")

# Accuracy at 0.5 threshold
probs = predict_proba(X, w, b)
y_pred = (probs >= 0.5).astype(np.float64)
acc = (y_pred == y).mean()
print(f"Training accuracy: {acc*100:.1f}%")
```
Output:
```text
Epoch 0: Loss = 0.6160
Epoch 200: Loss = 0.4145
Epoch 400: Loss = 0.3759
Epoch 600: Loss = 0.3630
Epoch 800: Loss = 0.3574
Epoch 1000: Loss = 0.3547
Epoch 1200: Loss = 0.3533
Epoch 1400: Loss = 0.3525
Epoch 1600: Loss = 0.3520
Epoch 1800: Loss = 0.3518
Learned parameters: w = 0.88, b = -4.30
Training accuracy: 85.5%
```
Now let's plot the learned sigmoid curve:
```python
import matplotlib.pyplot as plt

# Sort for a smooth curve
idx = np.argsort(X[:, 0])
X_sorted = X[idx]
probs_sorted = predict_proba(X_sorted, w, b)

# Jitter y for visualization
jitter = (np.random.rand(len(y), 1) - 0.5) * 0.05

plt.scatter(X, y + jitter, label="Data (pass=1, fail=0)", alpha=0.6)
plt.plot(X_sorted, probs_sorted, label="Learned probability (sigmoid)")
plt.xlabel("Hours studied")
plt.ylabel("P(pass | hours)")
plt.title("Logistic Regression from Scratch")
plt.legend()
plt.show()
```
Output:<br>
![Gradient descent plot](/assets/images/posts/2025/logistic-regression/logistic_regression_from_scratch_plot.png)<br>
There you go! We've just built logistic regression from scratch!

## 📚 Logistic vs. Other Models
I hope that now you can confidently explain the difference: logistic regression predicts probabilities (classification), while linear regression predicts continuous values (regression). However, like linear regression, logistic regression is the simplest form of classification models, so it could struggle with non-linear boundaries (e.g., data that is not linearly separable).
![Logistic regression vs other](/assets/images/posts/2025/logistic-regression/logistic_vs_other.png)

## ✅ Summary
In this blog post, we've learned that logistic regression predicts probabilities and classifies based on a threshold. We've also learned that logistic regression uses the sigmoid function, binary cross-entropy, and gradient descent to learn. By learning this model, I believe that you now have a solid foundation for classification problems! See you in the next blog post 😊
