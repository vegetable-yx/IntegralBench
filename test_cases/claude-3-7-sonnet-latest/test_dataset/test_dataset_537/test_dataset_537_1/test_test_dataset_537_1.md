# Evaluating $\int_1^2(2^{x-1}+\log_2(2x))\:dx$

I'll break this down into two parts:
$I = \int_1^2 2^{x-1} dx + \int_1^2 \log_2(2x) dx$

## Part 1: $\int_1^2 2^{x-1} dx$

Let's compute this first integral:
$\int 2^{x-1} dx = \int \frac{2^x}{2} dx = \frac{1}{2} \int 2^x dx$

The integral of $2^x$ is $\frac{2^x}{\ln(2)}$, so:
$\int 2^{x-1} dx = \frac{1}{2} \cdot \frac{2^x}{\ln(2)} = \frac{2^x}{2\ln(2)}$

Evaluating at the bounds:
$\left[\frac{2^x}{2\ln(2)}\right]_1^2 = \frac{2^2}{2\ln(2)} - \frac{2^1}{2\ln(2)} = \frac{4}{2\ln(2)} - \frac{2}{2\ln(2)} = \frac{2}{\ln(2)}$

## Part 2: $\int_1^2 \log_2(2x) dx$

I'll use the change of base formula: $\log_2(2x) = \frac{\ln(2x)}{\ln(2)}$

So: $\int_1^2 \log_2(2x) dx = \frac{1}{\ln(2)} \int_1^2 \ln(2x) dx$

For $\int \ln(2x) dx$, I'll use integration by parts:
Let $u = \ln(2x)$ and $dv = dx$
Then $du = \frac{1}{x} dx$ and $v = x$

$\int \ln(2x) dx = x\ln(2x) - \int x \cdot \frac{1}{x} dx = x\ln(2x) - \int dx = x\ln(2x) - x + C$

Therefore:
$\int \ln(2x) dx = x\ln(2x) - x + C$

Evaluating at the bounds:
$\left[x\ln(2x) - x\right]_1^2 = [2\ln(4) - 2] - [\ln(2) - 1] = 2\ln(4) - 2 - \ln(2) + 1$

Simplifying: $2\ln(4) - 2 - \ln(2) + 1 = 2\ln(2^2) - 2 - \ln(2) + 1 = 4\ln(2) - 2 - \ln(2) + 1 = 3\ln(2) - 1$

So: $\int_1^2 \log_2(2x) dx = \frac{1}{\ln(2)} \cdot (3\ln(2) - 1) = 3 - \frac{1}{\ln(2)}$

## Combining both parts:

$I = \frac{2}{\ln(2)} + 3 - \frac{1}{\ln(2)} = 3 + \frac{1}{\ln(2)}$

## Numerical approximation:

$\ln(2) \approx 0.6931471806$

$3 + \frac{1}{\ln(2)} \approx 3 + 1.4426950409 \approx 4.4426950409$

{"answer": "3 + \\frac{1}{\\ln(2)}", "numerical_answer": "4.4426950409"}