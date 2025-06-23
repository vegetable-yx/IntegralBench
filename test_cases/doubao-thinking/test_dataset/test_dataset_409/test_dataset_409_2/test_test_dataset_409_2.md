

To solve the definite integral \(\int_0^1 \arctan(x^2 - x + 1) \, dx\), we proceed as follows:

### Step 1: Key Identity for \(\arctan(x^2 - x + 1)\)
First, we use the property of the arctangent function: \(\arctan(z) + \arctan\left(\frac{1}{z}\right) = \frac{\pi}{2}\) for \(z > 0\). For \(z = x^2 - x + 1\), which is always positive (since its discriminant is negative), we have:
\[
\arctan(x^2 - x + 1) = \frac{\pi}{2} - \arctan\left(\frac{1}{x^2 - x + 1}\right).
\]

Next, we simplify \(\arctan\left(\frac{1}{x^2 - x + 1}\right)\). Notice that \(x^2 - x + 1 = 1 - x + x^2 = 1 - x(1 - x)\). Using the identity \(\arctan(a) + \arctan(b) = \arctan\left(\frac{a + b}{1 - ab}\right)\) for \(ab < 1\), we set \(a = x\) and \(b = 1 - x\). Since \(x(1 - x) \leq \frac{1}{4} < 1\), the identity holds:
\[
\arctan(x) + \arctan(1 - x) = \arctan\left(\frac{x + (1 - x)}{1 - x(1 - x)}\right) = \arctan\left(\frac{1}{x^2 - x + 1}\right).
\]

Thus, we rewrite the integrand:
\[
\arctan(x^2 - x + 1) = \frac{\pi}{2} - \arctan(x) - \arctan(1 - x).
\]

### Step 2: Integrate the Rewritten Expression
The integral becomes:
\[
\int_0^1 \arctan(x^2 - x + 1) \, dx = \int_0^1 \left( \frac{\pi}{2} - \arctan(x) - \arctan(1 - x) \right) dx.
\]

We split this into three integrals:
\[
\int_0^1 \frac{\pi}{2} \, dx - \int_0^1 \arctan(x) \, dx - \int_0^1 \arctan(1 - x) \, dx.
\]

### Step 3: Evaluate Each Integral
1. The first integral is straightforward:
\[
\int_0^1 \frac{\pi}{2} \, dx = \frac{\pi}{2} \cdot (1 - 0) = \frac{\pi}{2}.
\]

2. For the second integral \(\int_0^1 \arctan(x) \, dx\), use integration by parts with \(u = \arctan(x)\) and \(dv = dx\). Then \(du = \frac{1}{1 + x^2} dx\) and \(v = x\):
\[
\int_0^1 \arctan(x) \, dx = \left[ x \arctan(x) \right]_0^1 - \int_0^1 \frac{x}{1 + x^2} \, dx.
\]
Evaluating the boundary term: \(\left[ x \arctan(x) \right]_0^1 = 1 \cdot \frac{\pi}{4} - 0 = \frac{\pi}{4}\). For the remaining integral, let \(w = 1 + x^2\), so \(dw = 2x \, dx\):
\[
\int_0^1 \frac{x}{1 + x^2} \, dx = \frac{1}{2} \int_1^2 \frac{1}{w} \, dw = \frac{1}{2} \ln(2).
\]
Thus:
\[
\int_0^1 \arctan(x) \, dx = \frac{\pi}{4} - \frac{1}{2} \ln(2).
\]

3. The third integral \(\int_0^1 \arctan(1 - x) \, dx\) is equivalent to the second integral via substitution \(t = 1 - x\), so:
\[
\int_0^1 \arctan(1 - x) \, dx = \int_0^1 \arctan(t) \, dt = \frac{\pi}{4} - \frac{1}{2} \ln(2).
\]

### Step 4: Combine Results
Substituting back, the original integral becomes:
\[
\frac{\pi}{2} - \left( \frac{\pi}{4} - \frac{1}{2} \ln(2) \right) - \left( \frac{\pi}{4} - \frac{1}{2} \ln(2) \right) = \frac{\pi}{2} - \frac{\pi}{2} + \ln(2) = \ln(2).
\]

### Numerical Approximation
The numerical value of \(\ln(2)\) is approximately \(0.69314718056\), rounded to 10 decimal places.

{"answer": "\(\ln 2\)", "numerical_answer": "0.6931471806"}