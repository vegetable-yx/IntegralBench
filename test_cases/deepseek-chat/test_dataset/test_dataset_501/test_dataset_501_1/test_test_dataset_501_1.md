To compute the definite integral \(\int_0^1 \sin^2(\log x) \, dx\), we follow these steps:

### Step 1: Substitution
Let \( u = \log x \). Then, \( x = e^u \), and \( dx = e^u \, du \). When \( x = 0 \), \( u = -\infty \), and when \( x = 1 \), \( u = 0 \). The integral becomes:
\[
\int_{-\infty}^0 \sin^2(u) \cdot e^u \, du.
\]

### Step 2: Simplify the Integrand
Using the identity \(\sin^2(u) = \frac{1 - \cos(2u)}{2}\), the integrand becomes:
\[
\frac{1 - \cos(2u)}{2} \cdot e^u = \frac{e^u}{2} - \frac{e^u \cos(2u)}{2}.
\]
Thus, the integral splits into two parts:
\[
\frac{1}{2} \int_{-\infty}^0 e^u \, du - \frac{1}{2} \int_{-\infty}^0 e^u \cos(2u) \, du.
\]

### Step 3: Evaluate the First Integral
The first integral is straightforward:
\[
\frac{1}{2} \int_{-\infty}^0 e^u \, du = \frac{1}{2} \left[ e^u \right]_{-\infty}^0 = \frac{1}{2} (1 - 0) = \frac{1}{2}.
\]

### Step 4: Evaluate the Second Integral
The second integral requires integration by parts or recognizing it as a standard form. The integral of \( e^u \cos(2u) \) can be found using the formula:
\[
\int e^{au} \cos(bu) \, du = \frac{e^{au}}{a^2 + b^2} (a \cos(bu) + b \sin(bu)) + C.
\]
Here, \( a = 1 \) and \( b = 2 \), so:
\[
\int e^u \cos(2u) \, du = \frac{e^u}{5} (\cos(2u) + 2 \sin(2u)) + C.
\]
Evaluating from \( -\infty \) to \( 0 \):
\[
\left. \frac{e^u}{5} (\cos(2u) + 2 \sin(2u)) \right|_{-\infty}^0 = \frac{1}{5} (1 + 0) - 0 = \frac{1}{5}.
\]
Thus:
\[
-\frac{1}{2} \int_{-\infty}^0 e^u \cos(2u) \, du = -\frac{1}{2} \cdot \frac{1}{5} = -\frac{1}{10}.
\]

### Step 5: Combine Results
Adding the two parts together:
\[
\frac{1}{2} - \frac{1}{10} = \frac{5}{10} - \frac{1}{10} = \frac{4}{10} = \frac{2}{5}.
\]

### Step 6: Numerical Approximation
The numerical value of \( \frac{2}{5} \) is \( 0.4 \).

### Final Answer
\[
\boxed{
{"answer": "\frac{2}{5}", "numerical_answer": "0.4000000000"}
}
\]