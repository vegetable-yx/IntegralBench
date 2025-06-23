# Evaluating $\int_1^2(2^{x-1}+\log_2(2x))\:dx$

I'll split this integral into two parts:
$$\int_1^2(2^{x-1}+\log_2(2x))\:dx = \int_1^2 2^{x-1}\:dx + \int_1^2 \log_2(2x)\:dx$$

## Part 1: $\int_1^2 2^{x-1}\:dx$

Let's compute the first integral:
$$\int 2^{x-1}\:dx = \int \frac{2^x}{2}\:dx = \frac{1}{2}\int 2^x\:dx = \frac{1}{2} \cdot \frac{2^x}{\ln(2)} + C = \frac{2^x}{2\ln(2)} + C$$

Evaluating at the bounds:
$$\left[\frac{2^x}{2\ln(2)}\right]_1^2 = \frac{2^2}{2\ln(2)} - \frac{2^1}{2\ln(2)} = \frac{4}{2\ln(2)} - \frac{2}{2\ln(2)} = \frac{2}{2\ln(2)} = \frac{1}{\ln(2)}$$

## Part 2: $\int_1^2 \log_2(2x)\:dx$

For the second integral, I'll rewrite $\log_2(2x)$ using the change of base formula:
$$\log_2(2x) = \frac{\ln(2x)}{\ln(2)} = \frac{\ln(2) + \ln(x)}{\ln(2)} = 1 + \frac{\ln(x)}{\ln(2)}$$

So the integral becomes:
$$\int_1^2 \log_2(2x)\:dx = \int_1^2 \left(1 + \frac{\ln(x)}{\ln(2)}\right)\:dx = \int_1^2 dx + \frac{1}{\ln(2)}\int_1^2 \ln(x)\:dx$$

The first part is simply:
$$\int_1^2 dx = [x]_1^2 = 2 - 1 = 1$$

For the second part, we use the formula $\int \ln(x)\:dx = x\ln(x) - x + C$:
$$\frac{1}{\ln(2)}\int_1^2 \ln(x)\:dx = \frac{1}{\ln(2)}[x\ln(x) - x]_1^2$$
$$= \frac{1}{\ln(2)}[(2\ln(2) - 2) - (1\ln(1) - 1)]$$
$$= \frac{1}{\ln(2)}[(2\ln(2) - 2) - (0 - 1)]$$
$$= \frac{1}{\ln(2)}[2\ln(2) - 2 + 1]$$
$$= \frac{1}{\ln(2)}[2\ln(2) - 1]$$
$$= \frac{2\ln(2) - 1}{\ln(2)} = 2 - \frac{1}{\ln(2)}$$

## Combining the results

$$\int_1^2(2^{x-1}+\log_2(2x))\:dx = \frac{1}{\ln(2)} + 1 + \left(2 - \frac{1}{\ln(2)}\right) = 3$$

## Numerical approximation
The exact answer is 3, so the numerical approximation rounded to 10 decimal places is 3.0000000000.

{"answer": "3", "numerical_answer": "3.0000000000"}