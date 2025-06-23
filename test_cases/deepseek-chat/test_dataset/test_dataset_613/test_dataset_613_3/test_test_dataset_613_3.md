To compute the definite integral \(\int_{-1}^{0} 5\left(x^{6} + x\right)^{4} \, dx\), we follow these steps:

### Step 1: Expand the Integrand
First, expand \(\left(x^{6} + x\right)^{4}\) using the binomial theorem:
\[
\left(x^{6} + x\right)^{4} = \sum_{k=0}^{4} \binom{4}{k} x^{6k} x^{4-k} = \sum_{k=0}^{4} \binom{4}{k} x^{6k + 4 - k} = \sum_{k=0}^{4} \binom{4}{k} x^{5k + 4}
\]
Expanding the sum:
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
Compute the antiderivative:
\[
\int 5x^{24} \, dx = \frac{5}{25}x^{25} = \frac{1}{5}x^{25}
\]
\[
\int 20x^{19} \, dx = \frac{20}{20}x^{20} = x^{20}
\]
\[
\int 30x^{14} \, dx = \frac{30}{15}x^{15} = 2x^{15}
\]
\[
\int 20x^{9} \, dx = \frac{20}{10}x^{10} = 2x^{10}
\]
\[
\int 5x^{4} \, dx = \frac{5}{5}x^{5} = x^{5}
\]
Now, evaluate from \(-1\) to \(0\):
\[
\left[\frac{1}{5}x^{25} + x^{20} + 2x^{15} + 2x^{10} + x^{5}\right]_{-1}^{0}
\]
At \(x = 0\):
\[
\frac{1}{5}(0)^{25} + (0)^{20} + 2(0)^{15} + 2(0)^{10} + (0)^{5} = 0
\]
At \(x = -1\):
\[
\frac{1}{5}(-1)^{25} + (-1)^{20} + 2(-1)^{15} + 2(-1)^{10} + (-1)^{5} = \frac{1}{5}(-1) + 1 + 2(-1) + 2(1) + (-1) = -\frac{1}{5} + 1 - 2 + 2 - 1 = -\frac{1}{5}
\]
Subtract the lower limit from the upper limit:
\[
0 - \left(-\frac{1}{5}\right) = \frac{1}{5}
\]

### Step 3: Numerical Approximation
The exact value is \(\frac{1}{5}\), which numerically is:
\[
0.2
\]

### Final Answer
```json
{"answer": "\\frac{1}{5}", "numerical_answer": "0.2000000000"}
```