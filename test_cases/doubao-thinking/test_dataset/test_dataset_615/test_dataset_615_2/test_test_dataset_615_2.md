

To solve the definite integral \(\int_{0}^{7}\left(\sqrt[3]{\sqrt{x^{2}+1}+x}-\sqrt[3]{\sqrt{x^{2}+1}-x}\right)\,\mathrm{d}x\), we proceed as follows:

### Step 1: Simplify the integrand
Let \( A = \sqrt[3]{\sqrt{x^2 + 1} + x} \) and \( B = \sqrt[3]{\sqrt{x^2 + 1} - x} \). The integrand is \( A - B \).

First, observe that:
\[
A^3 = \sqrt{x^2 + 1} + x \quad \text{and} \quad B^3 = \sqrt{x^2 + 1} - x.
\]
Multiplying \( A \) and \( B \):
\[
AB = \sqrt[3]{\left(\sqrt{x^2 + 1} + x\right)\left(\sqrt{x^2 + 1} - x\right)} = \sqrt[3]{\left(x^2 + 1\right) - x^2} = \sqrt[3]{1} = 1.
\]
Thus, \( B = \frac{1}{A} \), so the integrand becomes \( A - \frac{1}{A} \).

### Step 2: Substitution
Let \( t = A - B = A - \frac{1}{A} \). We aim to express \( x \) in terms of \( t \). From \( t = A - \frac{1}{A} \), we cube both sides:
\[
t^3 = A^3 - 3A \cdot \frac{1}{A}\left(A - \frac{1}{A}\right) - \frac{1}{A^3} = (A^3 - \frac{1}{A^3}) - 3t.
\]
From \( A^3 = \sqrt{x^2 + 1} + x \) and \( B^3 = \sqrt{x^2 + 1} - x \), we have \( A^3 - B^3 = 2x \). Since \( B^3 = \frac{1}{A^3} \), this gives \( A^3 - \frac{1}{A^3} = 2x \). Substituting into the equation for \( t^3 \):
\[
t^3 = 2x - 3t \implies x = \frac{t^3 + 3t}{2}.
\]

### Step 3: Change of variables
Compute \( \mathrm{d}x \) in terms of \( t \):
\[
\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{3t^2 + 3}{2} = \frac{3(t^2 + 1)}{2} \implies \mathrm{d}x = \frac{3(t^2 + 1)}{2}\,\mathrm{d}t.
\]

### Step 4: Adjust limits of integration
- When \( x = 0 \): \( A = \sqrt[3]{\sqrt{0 + 1} + 0} = 1 \), \( B = \sqrt[3]{\sqrt{0 + 1} - 0} = 1 \), so \( t = A - B = 0 \).
- When \( x = 7 \): Solve \( 7 = \frac{t^3 + 3t}{2} \implies t^3 + 3t - 14 = 0 \). Testing \( t = 2 \): \( 8 + 6 - 14 = 0 \), so \( t = 2 \).

### Step 5: Evaluate the integral
The integral transforms to:
\[
\int_{0}^{7} (A - B)\,\mathrm{d}x = \int_{0}^{2} t \cdot \frac{3(t^2 + 1)}{2}\,\mathrm{d}t = \frac{3}{2} \int_{0}^{2} (t^3 + t)\,\mathrm{d}t.
\]
Compute the antiderivative:
\[
\int (t^3 + t)\,\mathrm{d}t = \frac{t^4}{4} + \frac{t^2}{2}.
\]
Evaluate from \( 0 \) to \( 2 \):
\[
\left[\frac{2^4}{4} + \frac{2^2}{2}\right] - \left[\frac{0^4}{4} + \frac{0^2}{2}\right] = \left[4 + 2\right] - 0 = 6.
\]
Thus, the integral becomes:
\[
\frac{3}{2} \cdot 6 = 9.
\]

### Numerical Approximation
The exact value is \( 9 \), so the numerical approximation to 10 decimal places is \( 9.0000000000 \).

{"answer": "9", "numerical_answer": "9.0000000000"}