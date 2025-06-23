To solve the definite integral \(\int\limits_{0}^{\infty}\frac{x^{3}}{e^x-1}\left[8\cosh\left(0.5x\right)-\cosh\left(0.25x\right)\right]dx\), we will follow the steps outlined.

### Step 1: Analytical Computation

First, let's rewrite the integrand in a more convenient form. Recall that \(\cosh(ax) = \frac{e^{ax} + e^{-ax}}{2}\). Thus, we have:
\[
8\cosh(0.5x) = 8 \cdot \frac{e^{0.5x} + e^{-0.5x}}{2} = 4(e^{0.5x} + e^{-0.5x})
\]
\[
\cosh(0.25x) = \frac{e^{0.25x} + e^{-0.25x}}{2}
\]

So the integrand becomes:
\[
\frac{x^3}{e^x - 1} \left[ 4(e^{0.5x} + e^{-0.5x}) - \frac{e^{0.25x} + e^{-0.25x}}{2} \right]
\]

Simplify the expression inside the brackets:
\[
4(e^{0.5x} + e^{-0.5x}) - \frac{e^{0.25x} + e^{-0.25x}}{2} = 4e^{0.5x} + 4e^{-0.5x} - \frac{e^{0.25x}}{2} - \frac{e^{-0.25x}}{2}
\]

Thus, the integral becomes:
\[
\int_0^\infty \frac{x^3}{e^x - 1} \left( 4e^{0.5x} + 4e^{-0.5x} - \frac{e^{0.25x}}{2} - \frac{e^{-0.25x}}{2} \right) dx
\]

We can split this into four separate integrals:
\[
4 \int_0^\infty \frac{x^3 e^{0.5x}}{e^x - 1} dx + 4 \int_0^\infty \frac{x^3 e^{-0.5x}}{e^x - 1} dx - \frac{1}{2} \int_0^\infty \frac{x^3 e^{0.25x}}{e^x - 1} dx - \frac{1}{2} \int_0^\infty \frac{x^3 e^{-0.25x}}{e^x - 1} dx
\]

Each of these integrals can be evaluated using the known result for integrals of the form \(\int_0^\infty \frac{x^3 e^{-ax}}{e^x - 1} dx\), which is related to the Riemann zeta function and the Gamma function. Specifically:
\[
\int_0^\infty \frac{x^3 e^{-ax}}{e^x - 1} dx = \Gamma(4) \zeta(4) \cdot \frac{1}{a^4}
\]

Using \(\Gamma(4) = 6\) and \(\zeta(4) = \frac{\pi^4}{90}\), we get:
\[
\int_0^\infty \frac{x^3 e^{-ax}}{e^x - 1} dx = 6 \cdot \frac{\pi^4}{90} \cdot \frac{1}{a^4} = \frac{\pi^4}{15a^4}
\]

Applying this to each term:
\[
4 \cdot \frac{\pi^4}{15 (0.5)^4} + 4 \cdot \frac{\pi^4}{15 (0.5)^4} - \frac{1}{2} \cdot \frac{\pi^4}{15 (0.25)^4} - \frac{1}{2} \cdot \frac{\pi^4}{15 (0.25)^4}
\]

Simplify the powers:
\[
4 \cdot \frac{\pi^4}{15 \cdot 0.0625} + 4 \cdot \frac{\pi^4}{15 \cdot 0.0625} - \frac{1}{2} \cdot \frac{\pi^4}{15 \cdot 0.00390625} - \frac{1}{2} \cdot \frac{\pi^4}{15 \cdot 0.00390625}
\]

\[
4 \cdot \frac{\pi^4}{0.9375} + 4 \cdot \frac{\pi^4}{0.9375} - \frac{1}{2} \cdot \frac{\pi^4}{0.05859375} - \frac{1}{2} \cdot \frac{\pi^4}{0.05859375}
\]

\[
4 \cdot 10.6667 \pi^4 + 4 \cdot 10.6667 \pi^4 - \frac{1}{2} \cdot 17.0833 \pi^4 - \frac{1}{2} \cdot 17.0833 \pi^4
\]

\[
42.6668 \pi^4 - 17.0833 \pi^4 = 25.5835 \pi^4
\]

### Step 2: Numerical Approximation

Using \(\pi \approx 3.141592653589793\), we get:
\[
\pi^4 \approx 97.40909103400244
\]

Thus:
\[
25.5835 \cdot 97.40909103400244 \approx 2492.535275
\]

### Step 3: Final Answer in JSON Format

\[
\boxed{
\begin{aligned}
&\text{"answer": "25.5835 \pi^4",} \\
&\text{"numerical_answer": "2492.535275"}
\end{aligned}
}
\]