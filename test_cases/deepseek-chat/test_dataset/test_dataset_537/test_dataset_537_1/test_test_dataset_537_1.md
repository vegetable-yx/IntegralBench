Let's solve the definite integral step by step:

### Given Integral:
\[ \int_1^2 \left(2^{x-1} + \log_2(2x)\right) \, dx \]

### Step 1: Split the Integral
The integral can be split into two parts:
\[ \int_1^2 2^{x-1} \, dx + \int_1^2 \log_2(2x) \, dx \]

### Step 2: Solve the First Integral \(\int 2^{x-1} \, dx\)
Let \( u = x - 1 \), then \( du = dx \). The integral becomes:
\[ \int 2^u \, du = \frac{2^u}{\ln 2} + C = \frac{2^{x-1}}{\ln 2} + C \]

Evaluate from 1 to 2:
\[ \left. \frac{2^{x-1}}{\ln 2} \right|_1^2 = \frac{2^{1}}{\ln 2} - \frac{2^{0}}{\ln 2} = \frac{2}{\ln 2} - \frac{1}{\ln 2} = \frac{1}{\ln 2} \]

### Step 3: Solve the Second Integral \(\int \log_2(2x) \, dx\)
First, rewrite \(\log_2(2x)\) using logarithm properties:
\[ \log_2(2x) = \log_2 2 + \log_2 x = 1 + \log_2 x \]

Now, the integral becomes:
\[ \int (1 + \log_2 x) \, dx = \int 1 \, dx + \int \log_2 x \, dx \]

The first part is straightforward:
\[ \int 1 \, dx = x + C \]

For the second part, \(\int \log_2 x \, dx\), use integration by parts:
Let \( u = \log_2 x \), \( dv = dx \). Then:
\[ du = \frac{1}{x \ln 2} \, dx, \quad v = x \]

Integration by parts formula:
\[ \int u \, dv = uv - \int v \, du \]

So:
\[ \int \log_2 x \, dx = x \log_2 x - \int x \cdot \frac{1}{x \ln 2} \, dx = x \log_2 x - \frac{x}{\ln 2} + C \]

Combine the results:
\[ \int \log_2(2x) \, dx = x + x \log_2 x - \frac{x}{\ln 2} + C \]

Evaluate from 1 to 2:
At \( x = 2 \):
\[ 2 + 2 \log_2 2 - \frac{2}{\ln 2} = 2 + 2(1) - \frac{2}{\ln 2} = 4 - \frac{2}{\ln 2} \]

At \( x = 1 \):
\[ 1 + 1 \log_2 1 - \frac{1}{\ln 2} = 1 + 0 - \frac{1}{\ln 2} = 1 - \frac{1}{\ln 2} \]

Subtract the lower limit from the upper limit:
\[ \left(4 - \frac{2}{\ln 2}\right) - \left(1 - \frac{1}{\ln 2}\right) = 3 - \frac{1}{\ln 2} \]

### Step 4: Combine the Results
Add the results from Step 2 and Step 3:
\[ \frac{1}{\ln 2} + 3 - \frac{1}{\ln 2} = 3 \]

### Numerical Approximation:
The exact answer is 3, so the numerical approximation is:
\[ 3.0000000000 \]

### Final Answer:
```json
{"answer": "3", "numerical_answer": "3.0000000000"}
```