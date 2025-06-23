To compute the definite integral 

\[
\int\limits_{0}^{\infty}\frac{1}{x(x^2 + 4)}\arctan x\:dx,
\]

we will follow these steps:

### Step 1: Simplify the Integrand
First, observe that the integrand can be rewritten as:

\[
\frac{\arctan x}{x(x^2 + 4)}.
\]

### Step 2: Use Integration by Parts
Let us consider integration by parts with:

\[
u = \arctan x \quad \Rightarrow \quad du = \frac{1}{1 + x^2}dx,
\]
\[
dv = \frac{1}{x(x^2 + 4)}dx \quad \Rightarrow \quad v = \int \frac{1}{x(x^2 + 4)}dx.
\]

To find \( v \), perform partial fraction decomposition on \( \frac{1}{x(x^2 + 4)} \):

\[
\frac{1}{x(x^2 + 4)} = \frac{A}{x} + \frac{Bx + C}{x^2 + 4}.
\]

Solving for \( A \), \( B \), and \( C \):

\[
1 = A(x^2 + 4) + (Bx + C)x.
\]

Setting \( x = 0 \):

\[
1 = 4A \quad \Rightarrow \quad A = \frac{1}{4}.
\]

Comparing coefficients:

For \( x^2 \): \( 0 = A + B \quad \Rightarrow \quad B = -\frac{1}{4} \).

For \( x \): \( 0 = C \).

Thus:

\[
\frac{1}{x(x^2 + 4)} = \frac{1}{4x} - \frac{x}{4(x^2 + 4)}.
\]

Integrating to find \( v \):

\[
v = \int \left( \frac{1}{4x} - \frac{x}{4(x^2 + 4)} \right) dx = \frac{1}{4} \ln|x| - \frac{1}{8} \ln(x^2 + 4) + C.
\]

For simplicity, we can ignore the constant \( C \) as it will cancel out in the definite integral.

### Step 3: Apply Integration by Parts
Now, apply integration by parts:

\[
\int u \, dv = uv - \int v \, du.
\]

Thus:

\[
\int_{0}^{\infty} \frac{\arctan x}{x(x^2 + 4)} dx = \left[ \arctan x \left( \frac{1}{4} \ln x - \frac{1}{8} \ln(x^2 + 4) \right) \right]_{0}^{\infty} - \int_{0}^{\infty} \left( \frac{1}{4} \ln x - \frac{1}{8} \ln(x^2 + 4) \right) \frac{1}{1 + x^2} dx.
\]

Evaluate the boundary term:

As \( x \to 0 \):

\[
\arctan x \to 0, \quad \ln x \to -\infty, \quad \ln(x^2 + 4) \to \ln 4.
\]

However, \( \arctan x \cdot \ln x \to 0 \) because \( \arctan x \sim x \) and \( x \ln x \to 0 \).

As \( x \to \infty \):

\[
\arctan x \to \frac{\pi}{2}, \quad \ln x \to \infty, \quad \ln(x^2 + 4) \sim 2 \ln x.
\]

Thus:

\[
\arctan x \left( \frac{1}{4} \ln x - \frac{1}{8} \ln(x^2 + 4) \right) \to \frac{\pi}{2} \left( \frac{1}{4} \ln x - \frac{1}{8} \cdot 2 \ln x \right) = \frac{\pi}{2} \left( \frac{1}{4} \ln x - \frac{1}{4} \ln x \right) = 0.
\]

So the boundary term vanishes, and we are left with:

\[
- \int_{0}^{\infty} \left( \frac{1}{4} \ln x - \frac{1}{8} \ln(x^2 + 4) \right) \frac{1}{1 + x^2} dx.
\]

### Step 4: Simplify the Remaining Integral
The remaining integral is:

\[
- \frac{1}{4} \int_{0}^{\infty} \frac{\ln x}{1 + x^2} dx + \frac{1}{8} \int_{0}^{\infty} \frac{\ln(x^2 + 4)}{1 + x^2} dx.
\]

We know that:

\[
\int_{0}^{\infty} \frac{\ln x}{1 + x^2} dx = 0
\]

(because it is an odd function under \( x \to \frac{1}{x} \)).

For the second integral, let \( x = 2 \tan \theta \):

\[
\int_{0}^{\infty} \frac{\ln(x^2 + 4)}{1 + x^2} dx = \int_{0}^{\pi/2} \frac{\ln(4 \tan^2 \theta + 4)}{1 + 4 \tan^2 \theta} \cdot 2 \sec^2 \theta \, d\theta.
\]

Simplify:

\[
\ln(4 \tan^2 \theta + 4) = \ln(4 \sec^2 \theta) = \ln 4 + 2 \ln \sec \theta.
\]

Thus:

\[
\int_{0}^{\pi/2} \frac{\ln 4 + 2 \ln \sec \theta}{\sec^2 \theta} \cdot 2 \sec^2 \theta \, d\theta = 2 \int_{0}^{\pi/2} (\ln 4 + 2 \ln \sec \theta) d\theta.
\]

Compute:

\[
2 \ln 4 \cdot \frac{\pi}{2} + 4 \int_{0}^{\pi/2} \ln \sec \theta \, d\theta = \pi \ln 4 + 4 \cdot \frac{\pi}{2} \ln 2 = \pi \ln 4 + 2 \pi \ln 2 = 2 \pi \ln 2 + 2 \pi \ln 2 = 4 \pi \ln 2.
\]

Thus:

\[
\frac{1}{8} \cdot 4 \pi \ln 2 = \frac{\pi}{2} \ln 2.
\]

### Step 5: Final Answer
The value of the integral is:

\[
\frac{\pi}{2} \ln 2.
\]

Numerical approximation:

\[
\frac{\pi}{2} \ln 2 \approx 1.0887930452.
\]

### Final JSON Output
```json
{"answer": "\\frac{\\pi}{2} \\ln 2", "numerical_answer": "1.0887930452"}
```