To compute the definite integral \(\int_{1/\sqrt{2}}^1 \frac{\arcsin(x)}{x^3} \, dx\), we will follow these steps:

### Step 1: Integration by Parts
Let \( u = \arcsin(x) \) and \( dv = \frac{1}{x^3} dx \). Then:
- \( du = \frac{1}{\sqrt{1 - x^2}} dx \)
- \( v = -\frac{1}{2x^2} \)

Using integration by parts:
\[
\int u \, dv = uv - \int v \, du
\]
\[
\int \frac{\arcsin(x)}{x^3} dx = -\frac{\arcsin(x)}{2x^2} + \int \frac{1}{2x^2 \sqrt{1 - x^2}} dx
\]

### Step 2: Simplify the Remaining Integral
The remaining integral is:
\[
\frac{1}{2} \int \frac{1}{x^2 \sqrt{1 - x^2}} dx
\]
Let \( x = \sin(\theta) \), then \( dx = \cos(\theta) d\theta \), and \( \sqrt{1 - x^2} = \cos(\theta) \). The integral becomes:
\[
\frac{1}{2} \int \frac{1}{\sin^2(\theta) \cos(\theta)} \cdot \cos(\theta) d\theta = \frac{1}{2} \int \csc^2(\theta) d\theta = -\frac{1}{2} \cot(\theta) + C
\]
Substituting back \( \theta = \arcsin(x) \):
\[
-\frac{1}{2} \cot(\arcsin(x)) + C = -\frac{1}{2} \frac{\sqrt{1 - x^2}}{x} + C
\]

### Step 3: Combine Results
The antiderivative is:
\[
-\frac{\arcsin(x)}{2x^2} - \frac{\sqrt{1 - x^2}}{2x} + C
\]

### Step 4: Evaluate the Definite Integral
Evaluate from \( x = \frac{1}{\sqrt{2}} \) to \( x = 1 \):
\[
\left[ -\frac{\arcsin(x)}{2x^2} - \frac{\sqrt{1 - x^2}}{2x} \right]_{1/\sqrt{2}}^1
\]

At \( x = 1 \):
\[
-\frac{\arcsin(1)}{2(1)^2} - \frac{\sqrt{1 - 1}}{2(1)} = -\frac{\pi}{4} - 0 = -\frac{\pi}{4}
\]

At \( x = \frac{1}{\sqrt{2}} \):
\[
-\frac{\arcsin(1/\sqrt{2})}{2(1/\sqrt{2})^2} - \frac{\sqrt{1 - (1/\sqrt{2})^2}}{2(1/\sqrt{2})} = -\frac{\pi/4}{2 \cdot (1/2)} - \frac{\sqrt{1/2}}{\sqrt{2}} = -\frac{\pi}{4} - \frac{1}{2}
\]

Subtract the lower limit from the upper limit:
\[
-\frac{\pi}{4} - \left( -\frac{\pi}{4} - \frac{1}{2} \right) = \frac{1}{2}
\]

### Step 5: Numerical Approximation
The exact answer is \( \frac{1}{2} \), which numerically is \( 0.5 \).

### Final Answer
```json
{"answer": "\\frac{1}{2}", "numerical_answer": "0.5000000000"}
```