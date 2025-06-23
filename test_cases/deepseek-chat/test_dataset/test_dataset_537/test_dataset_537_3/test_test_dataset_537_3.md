Let's compute the definite integral step by step:

\[
\int_1^2 \left(2^{x-1} + \log_2(2x)\right) \, dx
\]

### Step 1: Split the integral
The integral can be split into two parts:

\[
\int_1^2 2^{x-1} \, dx + \int_1^2 \log_2(2x) \, dx
\]

### Step 2: Compute the first integral \(\int 2^{x-1} \, dx\)
Let \(u = x - 1\), then \(du = dx\). The integral becomes:

\[
\int 2^{x-1} \, dx = \int 2^u \, du = \frac{2^u}{\ln 2} + C = \frac{2^{x-1}}{\ln 2} + C
\]

Evaluate from 1 to 2:

\[
\left. \frac{2^{x-1}}{\ln 2} \right|_1^2 = \frac{2^{1}}{ln 2} - \frac{2^{0}}{ln 2} = \frac{2}{ln 2} - \frac{1}{ln 2} = \frac{1}{ln 2}
\]

### Step 3: Compute the second integral \(\int \log_2(2x) \, dx\)
First, rewrite \(\log_2(2x)\) using logarithm properties:

\[
\log_2(2x) = \log_2 2 + \log_2 x = 1 + \log_2 x
\]

Now, the integral becomes:

\[
\int \log_2(2x) \, dx = \int 1 \, dx + \int \log_2 x \, dx = x + \int \frac{\ln x}{\ln 2} \, dx = x + \frac{1}{\ln 2} \int \ln x \, dx
\]

Compute \(\int \ln x \, dx\) using integration by parts:

Let \(u = \ln x\), \(dv = dx\), then \(du = \frac{1}{x} dx\), \(v = x\):

\[
\int \ln x \, dx = x \ln x - \int x \cdot \frac{1}{x} \, dx = x \ln x - x + C
\]

Thus:

\[
\int \log_2(2x) \, dx = x + \frac{1}{\ln 2} (x \ln x - x) + C
\]

Evaluate from 1 to 2:

At \(x = 2\):

\[
2 + \frac{1}{\ln 2} (2 \ln 2 - 2) = 2 + \frac{2 \ln 2 - 2}{\ln 2} = 2 + 2 - \frac{2}{\ln 2} = 4 - \frac{2}{\ln 2}
\]

At \(x = 1\):

\[
1 + \frac{1}{\ln 2} (1 \ln 1 - 1) = 1 + \frac{-1}{\ln 2} = 1 - \frac{1}{\ln 2}
\]

Subtract the lower limit from the upper limit:

\[
\left(4 - \frac{2}{\ln 2}\right) - \left(1 - \frac{1}{\ln 2}\right) = 3 - \frac{1}{\ln 2}
\]

### Step 4: Combine the results
Add the results from Step 2 and Step 3:

\[
\frac{1}{\ln 2} + 3 - \frac{1}{\ln 2} = 3
\]

### Step 5: Numerical approximation
The exact answer is 3, so the numerical approximation is:

\[
3.0000000000
\]

### Final Answer
```json
{"answer": "3", "numerical_answer": "3.0000000000"}
```