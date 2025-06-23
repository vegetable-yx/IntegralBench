
To solve the definite integral \(\int_{0}^{7}\left(\sqrt[3]{\sqrt{x^{2}+1}+x}-\sqrt[3]{\sqrt{x^{2}+1}-x}\right)\,\mathrm{d}x\), we proceed as follows:


### Step 1: Simplify the Integrand
Let \( u = \sqrt[3]{\sqrt{x^2 + 1} + x} - \sqrt[3]{\sqrt{x^2 + 1} - x} \). We analyze the relationship between \( u \) and \( x \).

First, denote \( a = \sqrt[3]{\sqrt{x^2 + 1} + x} \) and \( b = \sqrt[3]{\sqrt{x^2 + 1} - x} \). Then \( u = a - b \). Note that:
\[
a^3 = \sqrt{x^2 + 1} + x, \quad b^3 = \sqrt{x^2 + 1} - x
\]
Multiplying \( a^3 \) and \( b^3 \):
\[
a^3 b^3 = (\sqrt{x^2 + 1} + x)(\sqrt{x^2 + 1} - x) = (x^2 + 1) - x^2 = 1 \implies ab = 1
\]
Thus, \( b = 1/a \), so \( u = a - 1/a \).


### Step 2: Relate \( u \) and \( x \)
We derive a relationship between \( u \) and \( x \). Cubing \( u \):
\[
u^3 = \left(a - \frac{1}{a}\right)^3 = a^3 - \frac{1}{a^3} - 3\left(a - \frac{1}{a}\right)
\]
Substituting \( a^3 = \sqrt{x^2 + 1} + x \) and \( 1/a^3 = \sqrt{x^2 + 1} - x \):
\[
u^3 = \left(\sqrt{x^2 + 1} + x\right) - \left(\sqrt{x^2 + 1} - x\right) - 3u = 2x - 3u
\]
Rearranging gives:
\[
u^3 + 3u = 2x \implies x = \frac{u^3 + 3u}{2}
\]


### Step 3: Change Variables
We perform a substitution \( u \to x \). Compute \( dx \):
\[
dx = \frac{d}{du}\left(\frac{u^3 + 3u}{2}\right) du = \frac{3u^2 + 3}{2} du = \frac{3(u^2 + 1)}{2} du
\]

### Step 4: Adjust Limits of Integration
- When \( x = 0 \), \( u^3 + 3u = 0 \implies u = 0 \).
- When \( x = 7 \), \( u^3 + 3u = 14 \). Testing \( u = 2 \): \( 2^3 + 3(2) = 8 + 6 = 14 \), so \( u = 2 \).


### Step 5: Evaluate the Integral
The integral becomes:
\[
\int_{0}^{7} u \, dx = \int_{0}^{2} u \cdot \frac{3(u^2 + 1)}{2} du = \frac{3}{2} \int_{0}^{2} (u^3 + u) du
\]
Integrate term-by-term:
\[
\int_{0}^{2} (u^3 + u) du = \left[\frac{u^4}{4} + \frac{u^2}{2}\right]_{0}^{2} = \left(\frac{16}{4} + \frac{4}{2}\right) - 0 = 4 + 2 = 6
\]
Thus:
\[
\frac{3}{2} \cdot 6 = 9
\]


### Exact Answer and Numerical Approximation
The exact value of the integral is \( 9 \). The numerical approximation is \( 9.0000000000 \).


{"answer": "9", "numerical_answer": "9.0000000000"}