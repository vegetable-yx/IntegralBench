To compute the definite integral \(\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor \, dx\), we follow these steps:

1. **Substitution and Transformation**:
   - Substitute \( t = \frac{1}{x} \), which transforms the integral into \(\int_1^\infty \left\lfloor \cos(\pi t) \right\rfloor \frac{1}{t^2} \, dt\).

2. **Behavior Analysis**:
   - The function \(\cos(\pi t)\) oscillates between -1 and 1. The floor function \(\left\lfloor \cos(\pi t) \right\rfloor\) takes values -1 or 0 depending on the interval.
   - For intervals where \(\cos(\pi t) \geq 0\), the floor is 0; where \(\cos(\pi t) < 0\), the floor is -1.

3. **Interval Decomposition**:
   - Split the integral into intervals where \(\cos(\pi t)\) is negative or positive. Each interval \([n, n+1]\) for integer \(n\) is split into two halves.
   - For even \(n\), \(\cos(\pi t)\) is negative in \([n+0.5, n+1]\).
   - For odd \(n\), \(\cos(\pi t)\) is negative in \([n, n+0.5]\).

4. **Summing Contributions**:
   - Compute the integral contributions from each interval and sum them up using series and properties of the digamma function \(\psi\).
   - The key steps involve recognizing the telescoping nature of the series and using the reflection formula for the digamma function: \(\psi(1 - z) - \psi(z) = \pi \cot(\pi z)\).

5. **Final Result**:
   - After simplification, the integral evaluates to \(\frac{\pi}{2} - \frac{5}{3}\).

6. **Numerical Approximation**:
   - The numerical value rounded to 10 decimal places is approximately \(-0.0958703399\).

### Final Answer
{"answer": "\\frac{\\pi}{2} - \\frac{5}{3}", "numerical_answer": "-0.0958703399"}