# Evaluating $\int_1^{\infty}\frac{\log x}{x^2}dx$

## Step 1: Set up the integral

I'll solve the definite integral $\int_1^{\infty}\frac{\log x}{x^2}dx$ by using integration by parts.

## Step 2: Apply integration by parts

Integration by parts formula: $\int u(x)v'(x)dx = u(x)v(x) - \int v(x)u'(x)dx$

Let's set:
- $u(x) = \log x$
- $v'(x) = \frac{1}{x^2}$

Then:
- $u'(x) = \frac{1}{x}$
- $v(x) = -\frac{1}{x}$

Applying the formula:
$\int \frac{\log x}{x^2}dx = \log x \cdot (-\frac{1}{x}) - \int (-\frac{1}{x}) \cdot \frac{1}{x}dx$
$= -\frac{\log x}{x} - \int (-\frac{1}{x^2})dx$
$= -\frac{\log x}{x} + \int \frac{1}{x^2}dx$
$= -\frac{\log x}{x} - \frac{1}{x} + C$

## Step 3: Evaluate the definite integral

Now, I'll find the value of the definite integral:

$\int_1^{\infty}\frac{\log x}{x^2}dx = \left[-\frac{\log x}{x} - \frac{1}{x}\right]_1^{\infty}$

Evaluating at the limits:

For $x = 1$:
$-\frac{\log 1}{1} - \frac{1}{1} = 0 - 1 = -1$

For $x = \infty$:
$\lim_{x \to \infty} \left(-\frac{\log x}{x} - \frac{1}{x}\right)$

To evaluate this limit, I'll use L'Hôpital's rule for $\frac{\log x}{x}$:
$\lim_{x \to \infty} \frac{\log x}{x} = \lim_{x \to \infty} \frac{\frac{1}{x}}{1} = \lim_{x \to \infty} \frac{1}{x} = 0$

Therefore:
$\lim_{x \to \infty} \left(-\frac{\log x}{x} - \frac{1}{x}\right) = -0 - 0 = 0$

Now I can compute the definite integral:
$\int_1^{\infty}\frac{\log x}{x^2}dx = 0 - (-1) = 1$

## Step 4: Numerical approximation

The exact answer is 1, so the numerical approximation to 10 decimal places is 1.0000000000.

{"answer": "1", "numerical_answer": "1.0000000000"}