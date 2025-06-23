To compute the definite integral \(\int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor \, dx\), we need to consider the intervals where \(\cos\left(\frac{\pi}{x}\right)\) is negative or non-negative. 

1. **Analytical Calculation**:
   - The floor function \(\left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor\) is -1 when \(\cos\left(\frac{\pi}{x}\right)\) is in \([-1, 0)\) and 0 when it is in \([0, 1]\).
   - The intervals where \(\cos\left(\frac{\pi}{x}\right)\) is negative are found by solving \(\frac{\pi}{x} \in \left(\frac{\pi}{2} + 2k\pi, \frac{3\pi}{2} + 2k\pi\right)\) for integers \(k\). This translates to \(x \in \left(\frac{2}{4k+3}, \frac{2}{4k+1}\right)\) for \(k \geq 0\).
   - The total length \(L\) of these intervals within \((0, 1]\) is calculated by summing the lengths of each interval:
     \[
     L = \left(1 - \frac{2}{3}\right) + \sum_{k=1}^{\infty} \left(\frac{2}{4k+1} - \frac{2}{4k+3}\right)
     \]
   - This series simplifies using properties of the digamma function and the reflection formula, resulting in \(L = \frac{\pi}{2} - 1\).
   - The integral is the negative of this length:
     \[
     \int_0^1 \left\lfloor \cos\left(\frac{\pi}{x}\right) \right\rfloor \, dx = -L = 1 - \frac{\pi}{2}
     \]

2. **Numerical Approximation**:
   - The numerical value of \(1 - \frac{\pi}{2}\) is approximately:
     \[
     1 - \frac{\pi}{2} \approx -0.5707963268
     \]

### Final Answer
{"answer": "1 - \\frac{\\pi}{2}", "numerical_answer": "-0.5707963268"}