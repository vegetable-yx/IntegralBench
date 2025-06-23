To compute the definite integral \(\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor\), we follow these steps:

### Step 1: Understand the Integral
The integral involves the floor function \(\lfloor x \rfloor\), which is piecewise constant with jumps at integer values. The differential \(d\lfloor x \rfloor\) is zero everywhere except at the integers \(x = 1, 2, 3\), where it has a Dirac delta-like behavior. 

### Step 2: Evaluate the Integral
The integral can be expressed as a sum over the jumps of \(\lfloor x \rfloor\):
\[
\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor = \sum_{k=1}^3 \left( (k^2 + 1) \cdot (\lfloor k^+ \rfloor - \lfloor k^- \rfloor) \right)
\]
At each integer \(k\), \(\lfloor x \rfloor\) jumps by 1, so \(\lfloor k^+ \rfloor - \lfloor k^- \rfloor = 1\). Thus:
\[
\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor = (1^2 + 1) + (2^2 + 1) + (3^2 + 1) = 2 + 5 + 10 = 17
\]

### Step 3: Numerical Approximation
The exact value is 17, so the numerical approximation is:
\[
17.0000000000
\]

### Final Answer
```json
{"answer": "17", "numerical_answer": "17.0000000000"}
```