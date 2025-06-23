# Evaluating $\int_1^2(2^{x-1}+\log_2(2x))\:dx$

I'll split this into two parts and evaluate each separately.

## Part 1: $\int_1^2 2^{x-1} \, dx$

Let's compute $\int 2^{x-1} \, dx$:

$\int 2^{x-1} \, dx = \int \frac{2^x}{2} \, dx = \frac{1}{2} \int 2^x \, dx$

Using the formula $\int a^x \, dx = \frac{a^x}{\ln(a)} + C$, we get:

$\frac{1}{2} \int 2^x \, dx = \frac{1}{2} \cdot \frac{2^x}{\ln(2)} + C = \frac{2^x}{2\ln(2)} + C$

Now, we can evaluate the definite integral:

$\int_1^2 2^{x-1} \, dx = \left[ \frac{2^x}{2\ln(2)} \right]_1^2 = \frac{2^2}{2\ln(2)} - \frac{2^1}{2\ln(2)} = \frac{4 - 2}{2\ln(2)} = \frac{2}{2\ln(2)} = \frac{1}{\ln(2)}$

## Part 2: $\int_1^2 \log_2(2x) \, dx$

Let's use the change of base formula to convert to natural logarithm:
$\log_2(2x) = \frac{\ln(2x)}{\ln(2)}$

So:
$\int_1^2 \log_2(2x) \, dx = \frac{1}{\ln(2)} \int_1^2 \ln(2x) \, dx$

Let's evaluate $\int \ln(2x) \, dx$:
Let $u = 2x$, then $du = 2 \, dx$ or $dx = \frac{du}{2}$

$\int \ln(2x) \, dx = \int \ln(u) \cdot \frac{du}{2} = \frac{1}{2} \int \ln(u) \, du$

Using the formula $\int \ln(u) \, du = u\ln(u) - u + C$:

$\frac{1}{2} \int \ln(u) \, du = \frac{1}{2}(u\ln(u) - u) + C = \frac{u\ln(u) - u}{2} + C = \frac{2x\ln(2x) - 2x}{2} + C = x\ln(2x) - x + C$

Now, evaluating the definite integral:

$\int_1^2 \log_2(2x) \, dx = \frac{1}{\ln(2)} [x\ln(2x) - x]_1^2$

$= \frac{1}{\ln(2)} [(2\ln(4) - 2) - (1\ln(2) - 1)]$

$= \frac{1}{\ln(2)} [2\ln(4) - 2 - \ln(2) + 1]$

$= \frac{1}{\ln(2)} [2\ln(2^2) - 2 - \ln(2) + 1]$

$= \frac{1}{\ln(2)} [4\ln(2) - 2 - \ln(2) + 1]$

$= \frac{1}{\ln(2)} [3\ln(2) - 1]$

$= \frac{3\ln(2) - 1}{\ln(2)} = 3 - \frac{1}{\ln(2)}$

## Combining both parts:

$\int_1^2(2^{x-1}+\log_2(2x))\:dx = \frac{1}{\ln(2)} + \left(3 - \frac{1}{\ln(2)}\right) = 3$

## Numerical approximation:
The exact answer is 3, so the numerical approximation rounded to 10 decimal places is 3.0000000000.

{"answer": "3", "numerical_answer": "3.0000000000"}