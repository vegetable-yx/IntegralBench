Let's compute the definite integral step by step.

### Step 1: Compute the Antiderivative
We integrate the integrand \( f(x) = x^5 + 5x^4 + 10x^3 + 8x^2 + x \) term by term:

\[
\int (x^5 + 5x^4 + 10x^3 + 8x^2 + x) \, dx = \frac{x^6}{6} + x^5 + \frac{10x^4}{4} + \frac{8x^3}{3} + \frac{x^2}{2} + C
\]

Simplifying the coefficients:

\[
F(x) = \frac{x^6}{6} + x^5 + \frac{5x^4}{2} + \frac{8x^3}{3} + \frac{x^2}{2}
\]

### Step 2: Evaluate the Antiderivative at the Bounds
Compute \( F(-1/2) - F(-3/2) \):

#### Evaluate \( F(-1/2) \):
\[
F\left(-\frac{1}{2}\right) = \frac{\left(-\frac{1}{2}\right)^6}{6} + \left(-\frac{1}{2}\right)^5 + \frac{5\left(-\frac{1}{2}\right)^4}{2} + \frac{8\left(-\frac{1}{2}\right)^3}{3} + \frac{\left(-\frac{1}{2}\right)^2}{2}
\]

Calculate each term:
\[
\frac{\left(-\frac{1}{2}\right)^6}{6} = \frac{1}{64 \times 6} = \frac{1}{384}
\]
\[
\left(-\frac{1}{2}\right)^5 = -\frac{1}{32}
\]
\[
\frac{5\left(-\frac{1}{2}\right)^4}{2} = \frac{5 \times \frac{1}{16}}{2} = \frac{5}{32}
\]
\[
\frac{8\left(-\frac{1}{2}\right)^3}{3} = \frac{8 \times -\frac{1}{8}}{3} = -\frac{1}{3}
\]
\[
\frac{\left(-\frac{1}{2}\right)^2}{2} = \frac{\frac{1}{4}}{2} = \frac{1}{8}
\]

Combine the terms:
\[
F\left(-\frac{1}{2}\right) = \frac{1}{384} - \frac{1}{32} + \frac{5}{32} - \frac{1}{3} + \frac{1}{8}
\]

Convert to a common denominator (384):
\[
\frac{1}{384} - \frac{12}{384} + \frac{60}{384} - \frac{128}{384} + \frac{48}{384} = \frac{1 - 12 + 60 - 128 + 48}{384} = \frac{-31}{384}
\]

#### Evaluate \( F(-3/2) \):
\[
F\left(-\frac{3}{2}\right) = \frac{\left(-\frac{3}{2}\right)^6}{6} + \left(-\frac{3}{2}\right)^5 + \frac{5\left(-\frac{3}{2}\right)^4}{2} + \frac{8\left(-\frac{3}{2}\right)^3}{3} + \frac{\left(-\frac{3}{2}\right)^2}{2}
\]

Calculate each term:
\[
\frac{\left(-\frac{3}{2}\right)^6}{6} = \frac{729}{64 \times 6} = \frac{729}{384}
\]
\[
\left(-\frac{3}{2}\right)^5 = -\frac{243}{32}
\]
\[
\frac{5\left(-\frac{3}{2}\right)^4}{2} = \frac{5 \times \frac{81}{16}}{2} = \frac{405}{32}
\]
\[
\frac{8\left(-\frac{3}{2}\right)^3}{3} = \frac{8 \times -\frac{27}{8}}{3} = -9
\]
\[
\frac{\left(-\frac{3}{2}\right)^2}{2} = \frac{\frac{9}{4}}{2} = \frac{9}{8}
\]

Combine the terms:
\[
F\left(-\frac{3}{2}\right) = \frac{729}{384} - \frac{243}{32} + \frac{405}{32} - 9 + \frac{9}{8}
\]

Convert to a common denominator (384):
\[
\frac{729}{384} - \frac{2916}{384} + \frac{4860}{384} - \frac{3456}{384} + \frac{432}{384} = \frac{729 - 2916 + 4860 - 3456 + 432}{384} = \frac{-351}{384}
\]

#### Compute the Definite Integral:
\[
\int_{-3/2}^{-1/2} f(x) \, dx = F\left(-\frac{1}{2}\right) - F\left(-\frac{3}{2}\right) = \frac{-31}{384} - \left(\frac{-351}{384}\right) = \frac{320}{384} = \frac{5}{6}
\]

### Step 3: Numerical Approximation
The exact value is \( \frac{5}{6} \), which numerically approximates to:

\[
\frac{5}{6} \approx 0.8333333333
\]

### Final Answer
```json
{"answer": "\\frac{5}{6}", "numerical_answer": "0.8333333333"}
```