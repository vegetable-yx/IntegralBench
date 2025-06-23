To compute the definite integral \(\int_1^\infty \frac{\log x}{x^2} \, dx\), we proceed as follows:

1. **Integration by Parts**:
   - Let \(u = \log x\) and \(dv = \frac{1}{x^2} \, dx\).
   - Then \(du = \frac{1}{x} \, dx\) and \(v = -\frac{1}{x}\).

2. **Apply Integration by Parts Formula**:
   \[
   \int \frac{\log x}{x^2} \, dx = \left. -\frac{\log x}{x} \right|_1^\infty + \int_1^\infty \frac{1}{x^2} \, dx
   \]

3. **Evaluate the Boundary Term**:
   - As \(x \to \infty\), \(\frac{\log x}{x} \to 0\) because \(\log x\) grows slower than \(x\).
   - At \(x = 1\), \(\frac{\log 1}{1} = 0\).
   - Thus, the boundary term is \(0 - 0 = 0\).

4. **Evaluate the Remaining Integral**:
   \[
   \int_1^\infty \frac{1}{x^2} \, dx = \left. -\frac{1}{x} \right|_1^\infty = 0 - (-1) = 1
   \]

5. **Combine Results**:
   The integral simplifies to \(0 + 1 = 1\).

6. **Numerical Approximation**:
   The exact value is \(1\), so the numerical approximation to 10 decimal places is \(1.0000000000\).

### Final Answer
{"answer": "1", "numerical_answer": "1.0000000000"}