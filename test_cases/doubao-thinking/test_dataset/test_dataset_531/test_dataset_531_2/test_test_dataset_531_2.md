

To calculate the definite integral \(\int_{-3/2}^{-1/2}(x^5 + 5x^4 + 10x^3 + 8x^2 + x)\,dx\), we follow these steps:

### Step 1: Find the antiderivative of the integrand
The integrand is a polynomial, so we integrate term-by-term using the power rule \(\int x^n \,dx = \frac{x^{n+1}}{n+1}\) for \(n \neq -1\):

\[
\begin{aligned}
\int (x^5 + 5x^4 + 10x^3 + 8x^2 + x)\,dx &= \int x^5 \,dx + 5\int x^4 \,dx + 10\int x^3 \,dx + 8\int x^2 \,dx + \int x \,dx \\
&= \frac{x^6}{6} + 5 \cdot \frac{x^5}{5} + 10 \cdot \frac{x^4}{4} + 8 \cdot \frac{x^3}{3} + \frac{x^2}{2} \\
&= \frac{x^6}{6} + x^5 + \frac{5x^4}{2} + \frac{8x^3}{3} + \frac{x^2}{2}.
\end{aligned}
\]

Let \(F(x)\) denote this antiderivative:
\[
F(x) = \frac{x^6}{6} + x^5 + \frac{5x^4}{2} + \frac{8x^3}{3} + \frac{x^2}{2}.
\]

### Step 2: Evaluate \(F(x)\) at the bounds \(-1/2\) and \(-3/2\)
We compute \(F(-1/2) - F(-3/2)\).

#### Evaluation at \(x = -1/2\):
\[
\begin{aligned}
F\left(-\frac{1}{2}\right) &= \frac{\left(-\frac{1}{2}\right)^6}{6} + \left(-\frac{1}{2}\right)^5 + \frac{5\left(-\frac{1}{2}\right)^4}{2} + \frac{8\left(-\frac{1}{2}\right)^3}{3} + \frac{\left(-\frac{1}{2}\right)^2}{2} \\
&= \frac{1}{6 \cdot 64} - \frac{1}{32} + \frac{5 \cdot 1}{2 \cdot 16} + \frac{8 \cdot (-1)}{3 \cdot 8} + \frac{1}{4 \cdot 2} \\
&= \frac{1}{384} - \frac{1}{32} + \frac{5}{32} - \frac{1}{3} + \frac{1}{8}.
\end{aligned}
\]
Converting to a common denominator (384):
\[
\frac{1}{384} - \frac{12}{384} + \frac{60}{384} - \frac{128}{384} + \frac{48}{384} = \frac{1 - 12 + 60 - 128 + 48}{384} = \frac{-31}{384}.
\]

#### Evaluation at \(x = -3/2\):
\[
\begin{aligned}
F\left(-\frac{3}{2}\right) &= \frac{\left(-\frac{3}{2}\right)^6}{6} + \left(-\frac{3}{2}\right)^5 + \frac{5\left(-\frac{3}{2}\right)^4}{2} + \frac{8\left(-\frac{3}{2}\right)^3}{3} + \frac{\left(-\frac{3}{2}\right)^2}{2} \\
&= \frac{729}{6 \cdot 64} - \frac{243}{32} + \frac{5 \cdot 81}{2 \cdot 16} + \frac{8 \cdot (-27)}{3 \cdot 8} + \frac{9}{4 \cdot 2} \\
&= \frac{243}{128} - \frac{243}{32} + \frac{405}{32} - 9 + \frac{9}{8}.
\end{aligned}
\]
Converting to a common denominator (128):
\[
\frac{243}{128} - \frac{972}{128} + \frac{1620}{128} - \frac{1152}{128} + \frac{144}{128} = \frac{243 - 972 + 1620 - 1152 + 144}{128} = \frac{-117}{128}.
\]

### Step 3: Compute the definite integral
The integral is \(F(-1/2) - F(-3/2)\):
\[
\left(-\frac{31}{384}\right) - \left(-\frac{117}{128}\right) = -\frac{31}{384} + \frac{351}{384} = \frac{320}{384} = \frac{5}{6}.
\]

### Step 4: Numerical approximation
The exact value is \(\frac{5}{6}\), which approximates to \(0.8333333333\) when rounded to 10 decimal places.

{"answer": "\(\frac{5}{6}\)", "numerical_answer": "0.8333333333"}