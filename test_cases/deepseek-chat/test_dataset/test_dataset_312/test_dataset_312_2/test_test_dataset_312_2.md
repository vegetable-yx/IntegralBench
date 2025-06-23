To solve the definite integral \(\int\limits_{0}^{1}\arccos x\:\mathbf{D}\left(0.5x\right)dx\), we follow these steps:

### Step 1: Understand the Integral
The integral involves the arccosine function \(\arccos x\) and the Dirac delta function \(\mathbf{D}\left(0.5x\right)\). The Dirac delta function \(\mathbf{D}(x - a)\) is zero everywhere except at \(x = a\), where it is infinite, and its integral over any interval containing \(a\) is 1.

Here, \(\mathbf{D}\left(0.5x\right) = 2 \mathbf{D}(x)\), because scaling the argument of the Dirac delta function by a factor \(k\) scales the delta function by \(1/|k|\). Thus:
\[
\mathbf{D}\left(0.5x\right) = 2 \mathbf{D}(x).
\]

### Step 2: Simplify the Integral
Substitute \(\mathbf{D}\left(0.5x\right)\) with \(2 \mathbf{D}(x)\):
\[
\int\limits_{0}^{1}\arccos x \cdot 2 \mathbf{D}(x) \, dx = 2 \int\limits_{0}^{1}\arccos x \cdot \mathbf{D}(x) \, dx.
\]

### Step 3: Evaluate the Integral with the Dirac Delta
The Dirac delta function \(\mathbf{D}(x)\) is zero everywhere except at \(x = 0\). However, the interval of integration is \([0, 1]\), which includes \(x = 0\). The integral evaluates the integrand at \(x = 0\):
\[
2 \int\limits_{0}^{1}\arccos x \cdot \mathbf{D}(x) \, dx = 2 \arccos 0 = 2 \cdot \frac{\pi}{2} = \pi.
\]

### Step 4: Numerical Approximation
The exact answer is \(\pi\), and its numerical approximation to 10 decimal places is:
\[
\pi \approx 3.1415926536.
\]

### Final Answer
```json
{"answer": "\\pi", "numerical_answer": "3.1415926536"}
```