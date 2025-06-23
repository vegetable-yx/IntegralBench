# Evaluating $\int_{-3/2}^{-1/2}(x^5+5x^4+10x^3+8x^2+x)\:dx$

## Step 1: Find the antiderivative

I need to find the antiderivative of $f(x) = x^5+5x^4+10x^3+8x^2+x$

For each term, I'll use the power rule: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$

$\int x^5 dx = \frac{x^6}{6}$

$\int 5x^4 dx = 5 \cdot \frac{x^5}{5} = x^5$

$\int 10x^3 dx = 10 \cdot \frac{x^4}{4} = \frac{10x^4}{4} = \frac{5x^4}{2}$

$\int 8x^2 dx = 8 \cdot \frac{x^3}{3} = \frac{8x^3}{3}$

$\int x dx = \frac{x^2}{2}$

So the antiderivative is:
$F(x) = \frac{x^6}{6} + x^5 + \frac{5x^4}{2} + \frac{8x^3}{3} + \frac{x^2}{2} + C$

## Step 2: Evaluate the definite integral

Using the Fundamental Theorem of Calculus:
$\int_{-3/2}^{-1/2}(x^5+5x^4+10x^3+8x^2+x)\:dx = F(-1/2) - F(-3/2)$

First, let's calculate $F(-1/2)$:

$F(-1/2) = \frac{(-1/2)^6}{6} + (-1/2)^5 + \frac{5(-1/2)^4}{2} + \frac{8(-1/2)^3}{3} + \frac{(-1/2)^2}{2}$

$= \frac{1/64}{6} - \frac{1}{32} + \frac{5 \cdot 1/16}{2} - \frac{8 \cdot 1/8}{3} + \frac{1/4}{2}$

$= \frac{1}{384} - \frac{1}{32} + \frac{5}{32} - \frac{1}{3} + \frac{1}{8}$

Now, let's calculate $F(-3/2)$:

$F(-3/2) = \frac{(-3/2)^6}{6} + (-3/2)^5 + \frac{5(-3/2)^4}{2} + \frac{8(-3/2)^3}{3} + \frac{(-3/2)^2}{2}$

$= \frac{729/64}{6} - \frac{243}{32} + \frac{5 \cdot 81/16}{2} - \frac{8 \cdot 27/8}{3} + \frac{9/4}{2}$

$= \frac{729}{384} - \frac{243}{32} + \frac{5 \cdot 81}{32} - \frac{27}{3} + \frac{9}{8}$

## Step 3: Find the difference $F(-1/2) - F(-3/2)$

Let me convert all terms to a common denominator and simplify:

$F(-1/2) = \frac{1}{384} - \frac{12}{384} + \frac{60}{384} - \frac{128}{384} + \frac{48}{384} = \frac{-31}{384}$

$F(-3/2) = \frac{729}{384} - \frac{2916}{384} + \frac{5 \cdot 972}{384} - \frac{3456}{384} + \frac{432}{384}$
$= \frac{729 - 2916 + 4860 - 3456 + 432}{384} = \frac{-351}{384}$

Therefore:
$F(-1/2) - F(-3/2) = \frac{-31}{384} - \frac{-351}{384} = \frac{-31+351}{384} = \frac{320}{384} = \frac{5}{6}$

## Step 4: Numerical approximation

$\frac{5}{6} \approx 0.8333333333$

{"answer": "\\frac{5}{6}", "numerical_answer": "0.8333333333"}