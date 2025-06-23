To compute the definite integral \(\int_0^1 \sqrt[3]{x} \left\lfloor \frac{1}{\sqrt[3]{x}} \right\rfloor \, dx\), we proceed as follows:

1. **Substitution and Interval Division**:
   - Let \( t = \frac{1}{\sqrt[3]{x}} \), which implies \( x = \frac{1}{t^3} \) and \( dx = -\frac{3}{t^4} dt \).
   - The integral transforms to \( 3 \int_{1}^{\infty} \frac{\lfloor t \rfloor}{t^5} \, dt \).

2. **Breaking the Integral into Sums**:
   - For each integer \( n \geq 1 \), the interval \( [n, n+1) \) contributes \( \lfloor t \rfloor = n \).
   - The integral becomes \( 3 \sum_{n=1}^{\infty} \int_{n}^{n+1} \frac{n}{t^5} \, dt \).

3. **Evaluating Each Integral**:
   - Compute \( \int_{n}^{n+1} \frac{n}{t^5} \, dt = n \left[ -\frac{1}{4t^4} \right]_{n}^{n+1} = \frac{n}{4} \left( \frac{1}{n^4} - \frac{1}{(n+1)^4} \right) \).
   - This simplifies to \( \frac{1}{4n^3} - \frac{n}{4(n+1)^4} \).

4. **Summing the Series**:
   - The series \( \sum_{n=1}^{\infty} \left( \frac{1}{n^3} - \frac{n}{(n+1)^4} \right) \) is evaluated by recognizing:
     - \( \sum_{n=1}^{\infty} \frac{1}{n^3} = \zeta(3) \), but this term cancels partially.
     - \( \sum_{n=1}^{\infty} \frac{n}{(n+1)^4} = \sum_{m=2}^{\infty} \frac{m-1}{m^4} = \sum_{m=2}^{\infty} \left( \frac{1}{m^3} - \frac{1}{m^4} \right) \).
   - After simplification, the remaining terms involve the Riemann zeta function at 4: \( \zeta(4) = \frac{\pi^4}{90} \).

5. **Final Calculation**:
   - The integral simplifies to \( \frac{3}{4} \cdot \frac{\pi^4}{90} = \frac{\pi^4}{120} \).

6. **Numerical Approximation**:
   - The numerical value of \( \frac{\pi^4}{120} \) is approximately \( 0.8117424253 \).

### Final Answer
{"answer": "\\dfrac{\\pi^4}{120}", "numerical_answer": "0.8117424253"}