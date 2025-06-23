To solve the definite integral \(\int_0^{441}\frac{\pi\sin(\pi\sqrt{x})}{\sqrt{x}}dx\), we can proceed with the following steps:

### Step 1: Substitution
Let \( u = \sqrt{x} \). Then, \( x = u^2 \) and \( dx = 2u \, du \). The limits of integration change as follows:
- When \( x = 0 \), \( u = 0 \).
- When \( x = 441 \), \( u = \sqrt{441} = 21 \).

The integral becomes:
\[
\int_{0}^{21} \frac{\pi \sin(\pi u)}{u} \cdot 2u \, du = 2\pi \int_{0}^{21} \sin(\pi u) \, du.
\]

### Step 2: Integrate
The integral of \(\sin(\pi u)\) is:
\[
\int \sin(\pi u) \, du = -\frac{1}{\pi} \cos(\pi u) + C.
\]

Thus, the definite integral evaluates to:
\[
2\pi \left[ -\frac{1}{\pi} \cos(\pi u) \right]_{0}^{21} = 2\pi \left( -\frac{1}{\pi} \cos(21\pi) + \frac{1}{\pi} \cos(0) \right).
\]

### Step 3: Simplify
Since \(\cos(21\pi) = \cos(\pi) = -1\) (because \(21\pi\) is an odd multiple of \(\pi\)) and \(\cos(0) = 1\), we have:
\[
2\pi \left( -\frac{1}{\pi} (-1) + \frac{1}{\pi} (1) \right) = 2\pi \left( \frac{1}{\pi} + \frac{1}{\pi} \right) = 2\pi \left( \frac{2}{\pi} \right) = 4.
\]

### Step 4: Numerical Approximation
The exact value is \(4\), so the numerical approximation is:
\[
4.0000000000
\]

### Final Answer
```json
{"answer": "4", "numerical_answer": "4.0000000000"}
```