# Evaluating $\int_1^\infty\frac{\log x}{x^2}dx$

## Step 1: Let's set up an integration by parts approach.
For the integral $\int_1^\infty\frac{\log x}{x^2}dx$, I'll use integration by parts with:
* $u = \log x$
* $dv = \frac{1}{x^2}dx$

This gives:
* $du = \frac{1}{x}dx$
* $v = -\frac{1}{x}$

## Step 2: Apply the integration by parts formula
$\int u\,dv = uv - \int v\,du$

$\int_1^\infty\frac{\log x}{x^2}dx = \left[\log x \cdot \left(-\frac{1}{x}\right)\right]_1^\infty - \int_1^\infty \left(-\frac{1}{x}\right) \cdot \frac{1}{x}dx$

$= \left[-\frac{\log x}{x}\right]_1^\infty + \int_1^\infty \frac{1}{x^2}dx$

## Step 3: Evaluate each part

For the first part, we need to compute:
$\left[-\frac{\log x}{x}\right]_1^\infty = \lim_{t\to\infty}\left(-\frac{\log t}{t}\right) - \left(-\frac{\log 1}{1}\right)$

Since $\log 1 = 0$, the second term is $0$.

For the limit, we can use L'Hôpital's rule:
$\lim_{t\to\infty}\frac{\log t}{t} = \lim_{t\to\infty}\frac{1/t}{1} = \lim_{t\to\infty}\frac{1}{t} = 0$

So the first part evaluates to $0$.

For the second part:
$\int_1^\infty \frac{1}{x^2}dx = \left[-\frac{1}{x}\right]_1^\infty = \lim_{t\to\infty}\left(-\frac{1}{t}\right) - \left(-\frac{1}{1}\right) = 0 - (-1) = 1$

## Step 4: Combine the results
$\int_1^\infty\frac{\log x}{x^2}dx = 0 + 1 = 1$

## Numerical approximation
The exact value is 1, so the numerical approximation rounded to 10 decimal places is 1.0000000000.

{"answer": "1", "numerical_answer": "1.0000000000"}