To solve the definite integral \(\int\limits_{0}^{1}\arccos x\:\mathbf{D}\left(0.5x\right)dx\), where \(\mathbf{D}(x)\) is the Dirac delta function, we follow these steps:

### Step 1: Understand the Dirac Delta Function
The Dirac delta function \(\mathbf{D}(x - a)\) has the property that:
\[
\int_{-\infty}^{\infty} f(x) \mathbf{D}(x - a) \, dx = f(a)
\]
if \(a\) is within the integration limits, and 0 otherwise.

In this problem, \(\mathbf{D}(0.5x)\) can be rewritten as \(2\mathbf{D}(x)\), since:
\[
\mathbf{D}(0.5x) = 2\mathbf{D}(x)
\]
This is due to the scaling property of the Dirac delta function.

### Step 2: Rewrite the Integral
Substitute \(\mathbf{D}(0.5x) = 2\mathbf{D}(x)\) into the integral:
\[
\int_{0}^{1} \arccos x \cdot 2\mathbf{D}(x) \, dx = 2 \int_{0}^{1} \arccos x \cdot \mathbf{D}(x) \, dx
\]

### Step 3: Evaluate the Integral
The Dirac delta function \(\mathbf{D}(x)\) is non-zero only at \(x = 0\). However, \(x = 0\) is at the lower limit of integration. The integral of \(f(x)\mathbf{D}(x)\) over \([0, 1]\) is \(f(0)\) if the lower limit is included (which it is, since the integral is from 0 to 1).

Thus:
\[
2 \int_{0}^{1} \arccos x \cdot \mathbf{D}(x) \, dx = 2 \arccos 0 = 2 \cdot \frac{\pi}{2} = \pi
\]

### Step 4: Numerical Approximation
The exact answer is \(\pi\). A numerical approximation to 10 decimal places is:
\[
\pi \approx 3.1415926536
\]

### Final Answer
```json
{"answer": "\\pi", "numerical_answer": "3.1415926536"}
```