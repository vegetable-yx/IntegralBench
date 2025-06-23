To solve the definite integral 

\[
\int_{0}^{1} x^{-1/2} \cos\left(2\sqrt{x(1-x)}\right) dx,
\]

we proceed with the following steps:

### Step 1: Substitution
Let’s make the substitution \( u = \sqrt{x} \), which implies \( x = u^2 \) and \( dx = 2u \, du \). The limits change as follows:
- When \( x = 0 \), \( u = 0 \).
- When \( x = 1 \), \( u = 1 \).

The integral becomes:

\[
\int_{0}^{1} u^{-1} \cos\left(2\sqrt{u^2(1 - u^2)}\right) \cdot 2u \, du = 2 \int_{0}^{1} \cos\left(2u\sqrt{1 - u^2}\right) du.
\]

### Step 2: Simplify the Argument of the Cosine
Notice that \( 2u\sqrt{1 - u^2} \) is the double-angle identity for sine. Specifically, 

\[
2u\sqrt{1 - u^2} = \sin(2\theta) \quad \text{if} \quad u = \sin(\theta).
\]

Thus, we make another substitution: \( u = \sin(\theta) \), \( du = \cos(\theta) d\theta \). The limits become:
- When \( u = 0 \), \( \theta = 0 \).
- When \( u = 1 \), \( \theta = \frac{\pi}{2} \).

The integral transforms to:

\[
2 \int_{0}^{\pi/2} \cos\left(\sin(2\theta)\right) \cos(\theta) d\theta.
\]

### Step 3: Use Trigonometric Identities
We can express \( \cos(\sin(2\theta)) \cos(\theta) \) using a Bessel function identity or recognize that this integral is related to the Bessel function of the first kind \( J_0 \). Specifically, 

\[
\int_{0}^{\pi/2} \cos(a \sin(2\theta)) \cos(\theta) d\theta = \frac{\pi}{4} J_0(a).
\]

Here, \( a = 1 \), so the integral evaluates to:

\[
2 \cdot \frac{\pi}{4} J_0(1) = \frac{\pi}{2} J_0(1).
\]

### Step 4: Exact and Numerical Value
The Bessel function \( J_0(1) \) has an exact value in terms of its series representation, but it is commonly approximated numerically. The numerical value of \( J_0(1) \) is approximately 0.7651976866.

Thus, the integral evaluates to:

\[
\frac{\pi}{2} \cdot J_0(1) \approx \frac{\pi}{2} \cdot 0.7651976866 \approx 1.2019697153.
\]

### Final Answer
The exact answer is \( \frac{\pi}{2} J_0(1) \), and the numerical approximation is 1.2019697153.

```json
{"answer": "\\frac{\\pi}{2} J_0(1)", "numerical_answer": "1.2019697153"}
```