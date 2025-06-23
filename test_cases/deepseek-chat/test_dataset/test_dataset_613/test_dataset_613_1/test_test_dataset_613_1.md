To compute the definite integral \(\int_{-1}^{0} 5\left(x^{6} + x\right)^{4} \, dx\), we follow these steps:

### Step 1: Expand the Integrand
First, expand \(\left(x^{6} + x\right)^{4}\) using the binomial theorem:
\[
\left(x^{6} + x\right)^{4} = \sum_{k=0}^{4} \binom{4}{k} x^{6k} x^{4-k} = \sum_{k=0}^{4} \binom{4}{k} x^{6k + 4 - k} = \sum_{k=0}^{4} \binom{4}{k} x^{5k + 4}
\]
Expanding the terms:
\[
\left(x^{6} + x\right)^{4} = \binom{4}{0}x^{4} + \binom{4}{1}x^{9} + \binom{4}{2}x^{14} + \binom{4}{3}x^{19} + \binom{4}{4}x^{24}
\]
\[
= x^{4} + 4x^{9} + 6x^{14} + 4x^{19} + x^{24}
\]

### Step 2: Multiply by 5 and Integrate Term by Term
Multiply the expanded form by 5:
\[
5\left(x^{6} + x\right)^{4} = 5x^{4} + 20x^{9} + 30x^{14} + 20x^{19} + 5x^{24}
\]
Now, integrate term by term from \(-1\) to \(0\):
\[
\int_{-1}^{0} \left(5x^{4} + 20x^{9} + 30x^{14} + 20x^{19} + 5x^{24}\right) dx
\]
\[
= \left[ \frac{5x^{5}}{5} + \frac{20x^{10}}{10} + \frac{30x^{15}}{15} + \frac{20x^{20}}{20} + \frac{5x^{25}}{25} \right]_{-1}^{0}
\]
\[
= \left[ x^{5} + 2x^{10} + 2x^{15} + x^{20} + \frac{x^{25}}{5} \right]_{-1}^{0}
\]

### Step 3: Evaluate the Antiderivative at the Bounds
Evaluate at \(x = 0\):
\[
0^{5} + 2 \cdot 0^{10} + 2 \cdot 0^{15} + 0^{20} + \frac{0^{25}}{5} = 0
\]
Evaluate at \(x = -1\):
\[
(-1)^{5} + 2(-1)^{10} + 2(-1)^{15} + (-1)^{20} + \frac{(-1)^{25}}{5} = -1 + 2(1) + 2(-1) + 1 + \frac{-1}{5}
\]
\[
= -1 + 2 - 2 + 1 - \frac{1}{5} = 0 - \frac{1}{5} = -\frac{1}{5}
\]
Subtract the lower bound evaluation from the upper bound evaluation:
\[
0 - \left(-\frac{1}{5}\right) = \frac{1}{5}
\]

### Step 4: Numerical Approximation
The exact value is \(\frac{1}{5}\), which numerically is:
\[
0.2000000000
\]

### Final Answer
```json
{"answer": "\\frac{1}{5}", "numerical_answer": "0.2000000000"}
```