To solve the definite integral \(\int\limits_{0}^{1}\arccos x \cdot \mathbf{D}\left(0.5x\right)dx\), where \(\mathbf{D}(x)\) is the Dirac delta function, we follow these steps:

### Step 1: Understand the Dirac Delta Function
The Dirac delta function \(\mathbf{D}(x)\) has the property that:
\[
\int_{-\infty}^{\infty} f(x) \mathbf{D}(x - a) \, dx = f(a)
\]
if \(a\) is within the integration limits, and 0 otherwise. 

In this problem, \(\mathbf{D}(0.5x)\) can be rewritten using the scaling property of the Dirac delta function:
\[
\mathbf{D}(0.5x) = 2 \mathbf{D}(x)
\]
because \(\mathbf{D}(kx) = \frac{1}{|k|}\mathbf{D}(x)\) for \(k \neq 0\).

### Step 2: Rewrite the Integral
Substituting the scaling property into the integral:
\[
\int_{0}^{1} \arccos x \cdot \mathbf{D}(0.5x) \, dx = \int_{0}^{1} \arccos x \cdot 2 \mathbf{D}(x) \, dx = 2 \int_{0}^{1} \arccos x \cdot \mathbf{D}(x) \, dx
\]

### Step 3: Evaluate the Integral
The Dirac delta function \(\mathbf{D}(x)\) is non-zero only at \(x = 0\). However, the integration limits are from \(0\) to \(1\), and \(x = 0\) is included. Thus:
\[
\int_{0}^{1} \arccos x \cdot \mathbf{D}(x) \, dx = \arccos(0) = \frac{\pi}{2}
\]

Therefore:
\[
2 \int_{0}^{1} \arccos x \cdot \mathbf{D}(x) \, dx = 2 \cdot \frac{\pi}{2} = \pi
\]

### Step 4: Numerical Approximation
The exact answer is \(\pi\), and its numerical approximation to 10 decimal places is:
\[
\pi \approx 3.1415926536
\]

### Final Answer
```json
{"answer": "\\pi", "numerical_answer": "3.1415926536"}
```