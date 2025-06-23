To compute the definite integral \(\int_{1/\sqrt{2}}^1 \frac{\arcsin(x)}{x^3} \, dx\), we will proceed with integration by parts.

### Step 1: Integration by Parts
Recall the integration by parts formula:
\[
\int u \, dv = uv - \int v \, du
\]
Let:
\[
u = \arcsin(x) \quad \Rightarrow \quad du = \frac{1}{\sqrt{1 - x^2}} \, dx
\]
\[
dv = \frac{1}{x^3} \, dx \quad \Rightarrow \quad v = -\frac{1}{2x^2}
\]

Applying integration by parts:
\[
\int \frac{\arcsin(x)}{x^3} \, dx = -\frac{\arcsin(x)}{2x^2} + \int \frac{1}{2x^2 \sqrt{1 - x^2}} \, dx
\]

### Step 2: Simplify the Remaining Integral
The remaining integral is:
\[
\int \frac{1}{2x^2 \sqrt{1 - x^2}} \, dx
\]
Let \(x = \sin \theta\), then \(dx = \cos \theta \, d\theta\), and \(\sqrt{1 - x^2} = \cos \theta\). The integral becomes:
\[
\int \frac{1}{2 \sin^2 \theta \cos \theta} \cdot \cos \theta \, d\theta = \frac{1}{2} \int \csc^2 \theta \, d\theta = -\frac{1}{2} \cot \theta + C
\]
Substituting back \(x = \sin \theta\):
\[
-\frac{1}{2} \cot \theta = -\frac{1}{2} \cdot \frac{\sqrt{1 - x^2}}{x}
\]

### Step 3: Combine Results
The indefinite integral is:
\[
-\frac{\arcsin(x)}{2x^2} - \frac{\sqrt{1 - x^2}}{2x} + C
\]

### Step 4: Evaluate the Definite Integral
Evaluate from \(x = \frac{1}{\sqrt{2}}\) to \(x = 1\):
\[
\left[ -\frac{\arcsin(x)}{2x^2} - \frac{\sqrt{1 - x^2}}{2x} \right]_{1/\sqrt{2}}^1
\]

At \(x = 1\):
\[
-\frac{\arcsin(1)}{2 \cdot 1^2} - \frac{\sqrt{1 - 1}}{2 \cdot 1} = -\frac{\pi}{4} - 0 = -\frac{\pi}{4}
\]

At \(x = \frac{1}{\sqrt{2}}\):
\[
-\frac{\arcsin\left(\frac{1}{\sqrt{2}}\right)}{2 \left(\frac{1}{\sqrt{2}}\right)^2} - \frac{\sqrt{1 - \left(\frac{1}{\sqrt{2}}\right)^2}}{2 \cdot \frac{1}{\sqrt{2}}} = -\frac{\pi/4}{2 \cdot \frac{1}{2}} - \frac{\sqrt{1/2}}{\sqrt{2}} = -\frac{\pi}{4} - \frac{1}{2}
\]

Subtract the lower limit from the upper limit:
\[
-\frac{\pi}{4} - \left(-\frac{\pi}{4} - \frac{1}{2}\right) = \frac{1}{2}
\]

### Step 5: Numerical Approximation
The exact answer is \(\frac{1}{2}\). The numerical approximation is:
\[
0.5000000000
\]

### Final Answer
```json
{"answer": "\\frac{1}{2}", "numerical_answer": "0.5000000000"}
```