To compute the definite integral \(\int_{-1}^{0} 5\left(x^{6} + x\right)^{4} \, dx\), we follow these steps:

### Step 1: Expand the Integrand
First, expand \(\left(x^{6} + x\right)^{4}\) using the binomial theorem:
\[
\left(x^{6} + x\right)^{4} = \sum_{k=0}^{4} \binom{4}{k} x^{6k} x^{4 - k} = \sum_{k=0}^{4} \binom{4}{k} x^{6k + 4 - k} = \sum_{k=0}^{4} \binom{4}{k} x^{5k + 4}
\]
Expanding each term:
\[
\left(x^{6} + x\right)^{4} = x^{24} + 4x^{19} + 6x^{14} + 4x^{9} + x^{4}
\]
Now, multiply by 5:
\[
5\left(x^{6} + x\right)^{4} = 5x^{24} + 20x^{19} + 30x^{14} + 20x^{9} + 5x^{4}
\]

### Step 2: Integrate Term by Term
Integrate each term from \(-1\) to \(0\):
\[
\int_{-1}^{0} \left(5x^{24} + 20x^{19} + 30x^{14} + 20x^{9} + 5x^{4}\right) dx
\]
Compute each integral separately:
\[
\int x^{n} \, dx = \frac{x^{n+1}}{n+1} + C
\]
Applying this to each term:
\[
\int_{-1}^{0} 5x^{24} \, dx = 5 \left[ \frac{x^{25}}{25} \right]_{-1}^{0} = 5 \left(0 - \frac{(-1)^{25}}{25}\right) = 5 \left(0 + \frac{1}{25}\right) = \frac{5}{25} = \frac{1}{5}
\]
\[
\int_{-1}^{0} 20x^{19} \, dx = 20 \left[ \frac{x^{20}}{20} \right]_{-1}^{0} = 20 \left(0 - \frac{(-1)^{20}}{20}\right) = 20 \left(0 - \frac{1}{20}\right) = -1
\]
\[
\int_{-1}^{0} 30x^{14} \, dx = 30 \left[ \frac{x^{15}}{15} \right]_{-1}^{0} = 30 \left(0 - \frac{(-1)^{15}}{15}\right) = 30 \left(0 + \frac{1}{15}\right) = 2
\]
\[
\int_{-1}^{0} 20x^{9} \, dx = 20 \left[ \frac{x^{10}}{10} \right]_{-1}^{0} = 20 \left(0 - \frac{(-1)^{10}}{10}\right) = 20 \left(0 - \frac{1}{10}\right) = -2
\]
\[
\int_{-1}^{0} 5x^{4} \, dx = 5 \left[ \frac{x^{5}}{5} \right]_{-1}^{0} = 5 \left(0 - \frac{(-1)^{5}}{5}\right) = 5 \left(0 + \frac{1}{5}\right) = 1
\]

### Step 3: Sum the Results
Add all the integrated terms:
\[
\frac{1}{5} - 1 + 2 - 2 + 1 = \frac{1}{5}
\]

### Step 4: Numerical Approximation
The exact answer is \(\frac{1}{5}\), which numerically is:
\[
0.2
\]

### Final Answer
```json
{"answer": "\\frac{1}{5}", "numerical_answer": "0.2000000000"}
```