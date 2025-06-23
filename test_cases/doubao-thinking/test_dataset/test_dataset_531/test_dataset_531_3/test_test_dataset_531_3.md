

To calculate the definite integral \(\int_{-3/2}^{-1/2}(x^5 + 5x^4 + 10x^3 + 8x^2 + x)\,dx\), we follow these steps:

### Step 1: Find the antiderivative
The integrand is a polynomial, so we integrate term-by-term using the power rule \(\int x^n \,dx = \frac{x^{n+1}}{n+1}\) for \(n \neq -1\):

\[
\begin{aligned}
\int (x^5 + 5x^4 + 10x^3 + 8x^2 + x)\,dx &= \int x^5 \,dx + 5\int x^4 \,dx + 10\int x^3 \,dx + 8\int x^2 \,dx + \int x \,dx \\
&= \frac{x^6}{6} + 5 \cdot \frac{x^5}{5} + 10 \cdot \frac{x^4}{4} + 8 \cdot \frac{x^3}{3} + \frac{x^2}{2} \\
&= \frac{x^6}{6} + x^5 + \frac{5}{2}x^4 + \frac{8}{3}x^3 + \frac{x^2}{2}.
\end{aligned}
\]

Let \(F(x) = \frac{x^6}{6} + x^5 + \frac{5}{2}x^4 + \frac{8}{3}x^3 + \frac{x^2}{2}\) denote the antiderivative.

### Step 2: Evaluate \(F(x)\) at the bounds
We compute \(F(-1/2) - F(-3/2)\).

#### Evaluation at \(x = -1/2\):
\[
\begin{aligned}
F\left(-\frac{1}{2}\right) &= \frac{\left(-\frac{1}{2}\right)^6}{6} + \left(-\frac{1}{2}\right)^5 + \frac{5}{2}\left(-\frac{1}{2}\right)^4 + \frac{8}{3}\left(-\frac{1}{2}\right)^3 + \frac{\left(-\frac{1}{2}\right)^2}{2} \\
&= \frac{1}{384} - \frac{1}{32} + \frac{5}{32} - \frac{1}{3} + \frac{1}{8} \\
&= \frac{1 - 12 + 60 - 128 + 48}{384} \\
&= -\frac{31}{384}.
\end{aligned}
\]

#### Evaluation at \(x = -3/2\):
\[
\begin{aligned}
F\left(-\frac{3}{2}\right) &= \frac{\left(-\frac{3}{2}\right)^6}{6} + \left(-\frac{3}{2}\right)^5 + \frac{5}{2}\left(-\frac{3}{2}\right)^4 + \frac{8}{3}\left(-\frac{3}{2}\right)^3 + \frac{\left(-\frac{3}{2}\right)^2}{2} \\
&= \frac{729}{384} - \frac{243}{32} + \frac{405}{32} - 9 + \frac{9}{8} \\
&= \frac{243 - 972 + 1620 - 1152 + 144}{128} \\
&= -\frac{117}{128}.
\end{aligned}
\]

### Step 3: Compute the definite integral
\[
\begin{aligned}
\int_{-3/2}^{-1/2}(x^5 + 5x^4 + 10x^3 + 8x^2 + x)\,dx &= F\left(-\frac{1}{2}\right) - F\left(-\frac{3}{2}\right) \\
&= -\frac{31}{384} - \left(-\frac{117}{128}\right) \\
&= -\frac{31}{384} + \frac{351}{384} \\
&= \frac{320}{384} \\
&= \frac{5}{6}.
\end{aligned}
\]

### Step 4: Numerical approximation
The exact value is \(\frac{5}{6}\), which approximates to \(0.8333333333\) (rounded to 10 decimal places).

{"answer": "\(\frac{5}{6}\)", "numerical_answer": "0.8333333333"}