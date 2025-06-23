# Evaluating $\int_{-3/2}^{-1/2}(x^5+5x^4+10x^3+8x^2+x)\:dx$

I'll find the antiderivative first, then evaluate at the bounds.

## Step 1: Find the antiderivative
For the function $f(x) = x^5+5x^4+10x^3+8x^2+x$, the antiderivative is:

$F(x) = \int (x^5+5x^4+10x^3+8x^2+x)\:dx$

$F(x) = \frac{x^6}{6} + \frac{5x^5}{5} + \frac{10x^4}{4} + \frac{8x^3}{3} + \frac{x^2}{2} + C$

$F(x) = \frac{x^6}{6} + x^5 + \frac{10x^4}{4} + \frac{8x^3}{3} + \frac{x^2}{2} + C$

$F(x) = \frac{x^6}{6} + x^5 + \frac{5x^4}{2} + \frac{8x^3}{3} + \frac{x^2}{2} + C$

## Step 2: Evaluate at the bounds
Now I'll calculate $F(-1/2) - F(-3/2)$:

### Evaluating $F(-1/2)$:
$F(-1/2) = \frac{(-1/2)^6}{6} + (-1/2)^5 + \frac{5(-1/2)^4}{2} + \frac{8(-1/2)^3}{3} + \frac{(-1/2)^2}{2}$

$= \frac{1/64}{6} - \frac{1}{32} + \frac{5 \cdot 1/16}{2} - \frac{8 \cdot 1/8}{3} + \frac{1/4}{2}$

$= \frac{1}{384} - \frac{1}{32} + \frac{5}{32} - \frac{8}{24} + \frac{1}{8}$

$= \frac{1}{384} - \frac{1}{32} + \frac{5}{32} - \frac{1}{3} + \frac{1}{8}$

$= \frac{1}{384} - \frac{12}{384} + \frac{60}{384} - \frac{128}{384} + \frac{48}{384}$

$= \frac{1 - 12 + 60 - 128 + 48}{384}$

$= \frac{-31}{384}$

### Evaluating $F(-3/2)$:
$F(-3/2) = \frac{(-3/2)^6}{6} + (-3/2)^5 + \frac{5(-3/2)^4}{2} + \frac{8(-3/2)^3}{3} + \frac{(-3/2)^2}{2}$

$= \frac{729/64}{6} - \frac{243}{32} + \frac{5 \cdot 81/16}{2} - \frac{8 \cdot 27/8}{3} + \frac{9/4}{2}$

$= \frac{729}{384} - \frac{243}{32} + \frac{5 \cdot 81}{32} - \frac{8 \cdot 27}{24} + \frac{9}{8}$

$= \frac{729}{384} - \frac{243}{32} + \frac{405}{32} - \frac{9}{3} + \frac{9}{8}$

$= \frac{729}{384} - \frac{2916}{384} + \frac{4860}{384} - \frac{1152}{384} + \frac{432}{384}$

$= \frac{729 - 2916 + 4860 - 1152 + 432}{384}$

$= \frac{1953}{384}$

## Step 3: Calculate the definite integral
$\int_{-3/2}^{-1/2}(x^5+5x^4+10x^3+8x^2+x)\:dx = F(-1/2) - F(-3/2)$

$= \frac{-31}{384} - \frac{1953}{384}$

$= \frac{-31 - 1953}{384}$

$= \frac{-1984}{384}$

$= -\frac{1984}{384}$

We can simplify this fraction by dividing both numerator and denominator by their greatest common divisor:
$\gcd(1984, 384) = 128$

$= -\frac{1984/128}{384/128} = -\frac{15.5}{3} = -\frac{31}{6}$

## Step 4: Numerical approximation
The decimal approximation of $-\frac{31}{6}$ is $-5.1666666667$, rounded to 10 decimal places.

{"answer": "-\\frac{31}{6}", "numerical_answer": "-5.1666666667"}