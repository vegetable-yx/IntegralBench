To compute the definite integral \(\int\limits_0^1 x \arcsin x \arccos x \, dx\), we follow these steps:

### Step 1: Simplify the Integrand
First, observe that \(\arccos x = \frac{\pi}{2} - \arcsin x\). Thus, the integrand can be rewritten as:
\[
x \arcsin x \arccos x = x \arcsin x \left(\frac{\pi}{2} - \arcsin x\right) = \frac{\pi}{2} x \arcsin x - x (\arcsin x)^2.
\]
So, the integral becomes:
\[
\int_0^1 x \arcsin x \arccos x \, dx = \frac{\pi}{2} \int_0^1 x \arcsin x \, dx - \int_0^1 x (\arcsin x)^2 \, dx.
\]

### Step 2: Compute \(\int x \arcsin x \, dx\)
Let \(I_1 = \int x \arcsin x \, dx\). Using integration by parts with \(u = \arcsin x\) and \(dv = x \, dx\):
\[
I_1 = \frac{x^2}{2} \arcsin x - \int \frac{x^2}{2} \cdot \frac{1}{\sqrt{1 - x^2}} \, dx.
\]
The remaining integral is:
\[
\int \frac{x^2}{\sqrt{1 - x^2}} \, dx = \int \frac{1 - (1 - x^2)}{\sqrt{1 - x^2}} \, dx = \int \frac{1}{\sqrt{1 - x^2}} \, dx - \int \sqrt{1 - x^2} \, dx.
\]
These are standard integrals:
\[
\int \frac{1}{\sqrt{1 - x^2}} \, dx = \arcsin x, \quad \int \sqrt{1 - x^2} \, dx = \frac{x}{2} \sqrt{1 - x^2} + \frac{1}{2} \arcsin x.
\]
Thus:
\[
\int \frac{x^2}{\sqrt{1 - x^2}} \, dx = \arcsin x - \left(\frac{x}{2} \sqrt{1 - x^2} + \frac{1}{2} \arcsin x\right) = \frac{1}{2} \arcsin x - \frac{x}{2} \sqrt{1 - x^2}.
\]
Therefore:
\[
I_1 = \frac{x^2}{2} \arcsin x - \frac{1}{2} \left(\frac{1}{2} \arcsin x - \frac{x}{2} \sqrt{1 - x^2}\right) = \frac{x^2}{2} \arcsin x - \frac{1}{4} \arcsin x + \frac{x}{4} \sqrt{1 - x^2}.
\]
Evaluating from 0 to 1:
\[
I_1 \Big|_0^1 = \left(\frac{1}{2} \cdot \frac{\pi}{2} - \frac{1}{4} \cdot \frac{\pi}{2} + \frac{1}{4} \cdot 0\right) - 0 = \frac{\pi}{8}.
\]

### Step 3: Compute \(\int x (\arcsin x)^2 \, dx\)
Let \(I_2 = \int x (\arcsin x)^2 \, dx\). Using integration by parts with \(u = (\arcsin x)^2\) and \(dv = x \, dx\):
\[
I_2 = \frac{x^2}{2} (\arcsin x)^2 - \int \frac{x^2}{2} \cdot 2 \arcsin x \cdot \frac{1}{\sqrt{1 - x^2}} \, dx = \frac{x^2}{2} (\arcsin x)^2 - \int \frac{x^2 \arcsin x}{\sqrt{1 - x^2}} \, dx.
\]
The remaining integral is similar to the one in \(I_1\):
\[
\int \frac{x^2 \arcsin x}{\sqrt{1 - x^2}} \, dx = \int \arcsin x \cdot \left(\frac{1}{\sqrt{1 - x^2}} - \sqrt{1 - x^2}\right) dx.
\]
This can be split into:
\[
\int \frac{\arcsin x}{\sqrt{1 - x^2}} \, dx - \int \arcsin x \cdot \sqrt{1 - x^2} \, dx.
\]
The first integral is straightforward:
\[
\int \frac{\arcsin x}{\sqrt{1 - x^2}} \, dx = \frac{1}{2} (\arcsin x)^2.
\]
The second integral requires integration by parts:
\[
\int \arcsin x \cdot \sqrt{1 - x^2} \, dx = \arcsin x \cdot \left(\frac{x}{2} \sqrt{1 - x^2} + \frac{1}{2} \arcsin x\right) - \int \frac{1}{\sqrt{1 - x^2}} \cdot \left(\frac{x}{2} \sqrt{1 - x^2} + \frac{1}{2} \arcsin x\right) dx.
\]
Simplifying:
\[
= \frac{x}{2} \sqrt{1 - x^2} \arcsin x + \frac{1}{2} (\arcsin x)^2 - \frac{1}{2} \int x \, dx - \frac{1}{2} \int \frac{\arcsin x}{\sqrt{1 - x^2}} \, dx.
\]
\[
= \frac{x}{2} \sqrt{1 - x^2} \arcsin x + \frac{1}{2} (\arcsin x)^2 - \frac{x^2}{4} - \frac{1}{4} (\arcsin x)^2.
\]
Thus:
\[
\int \frac{x^2 \arcsin x}{\sqrt{1 - x^2}} \, dx = \frac{1}{2} (\arcsin x)^2 - \left(\frac{x}{2} \sqrt{1 - x^2} \arcsin x + \frac{1}{4} (\arcsin x)^2 - \frac{x^2}{4}\right) = \frac{1}{4} (\arcsin x)^2 - \frac{x}{2} \sqrt{1 - x^2} \arcsin x + \frac{x^2}{4}.
\]
Therefore:
\[
I_2 = \frac{x^2}{2} (\arcsin x)^2 - \left(\frac{1}{4} (\arcsin x)^2 - \frac{x}{2} \sqrt{1 - x^2} \arcsin x + \frac{x^2}{4}\right).
\]
Evaluating from 0 to 1:
\[
I_2 \Big|_0^1 = \left(\frac{1}{2} \cdot \frac{\pi^2}{4} - \frac{1}{4} \cdot \frac{\pi^2}{4} + 0 - \frac{1}{4}\right) - 0 = \frac{\pi^2}{16} - \frac{1}{4}.
\]

### Step 4: Combine the Results
Now, the original integral is:
\[
\frac{\pi}{2} I_1 - I_2 = \frac{\pi}{2} \cdot \frac{\pi}{8} - \left(\frac{\pi^2}{16} - \frac{1}{4}\right) = \frac{\pi^2}{16} - \frac{\pi^2}{16} + \frac{1}{4} = \frac{1}{4}.
\]

### Numerical Approximation
The exact answer is \(\frac{1}{4}\), which numerically is \(0.25\).

### Final Answer
```json
{"answer": "\\frac{1}{4}", "numerical_answer": "0.2500000000"}
```