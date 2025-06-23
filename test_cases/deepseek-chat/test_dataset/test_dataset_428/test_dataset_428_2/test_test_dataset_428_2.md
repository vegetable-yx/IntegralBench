To compute the definite integral \(\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor\), we follow these steps:

### Step 1: Understand the Integral
The integral involves the floor function \(\lfloor x \rfloor\), which is piecewise constant with jumps at integer values. The differential \(d\lfloor x \rfloor\) is zero everywhere except at the points where \(\lfloor x \rfloor\) jumps, i.e., at \(x = 1, 2, 3\). At these points, the jump size is 1.

### Step 2: Rewrite the Integral as a Sum
The integral can be expressed as a sum over the jumps of \(\lfloor x \rfloor\):
\[
\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor = \sum_{k=1}^3 \left( \lim_{x \to k^-} (x^2 + 1) - \lim_{x \to (k-1)^+} (x^2 + 1) \right)
\]
However, since \(\lfloor x \rfloor\) jumps by 1 at each integer \(k\), the integral simplifies to:
\[
\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor = \sum_{k=1}^3 (k^2 + 1)
\]

### Step 3: Compute the Sum
Calculate the sum over the jumps:
\[
\sum_{k=1}^3 (k^2 + 1) = (1^2 + 1) + (2^2 + 1) + (3^2 + 1) = 2 + 5 + 10 = 17
\]

### Step 4: Numerical Approximation
The exact result is 17, so the numerical approximation is:
\[
17.0000000000
\]

### Final Answer
```json
{"answer": "17", "numerical_answer": "17.0000000000"}
```