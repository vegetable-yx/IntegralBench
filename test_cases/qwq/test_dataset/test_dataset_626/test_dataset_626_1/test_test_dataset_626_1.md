To compute the definite integral \(\int_0^1 \frac{x-1}{(x+1)\ln x} \, dx\), we proceed as follows:

1. **Analytical Calculation**:
   - Recognize that the integrand \(\frac{x-1}{(x+1)\ln x}\) can be expressed using an integral involving a parameter \(t\).
   - Define \(F(a) = \int_0^1 \frac{x^a - 1}{(x+1)\ln x} \, dx\). Differentiating \(F(a)\) with respect to \(a\) gives:
     \[
     \frac{dF}{da} = \int_0^1 \frac{x^a}{x+1} \, dx
     \]
   - This integral, denoted as \(G(a)\), can be expressed as a series:
     \[
     G(a) = \sum_{n=0}^\infty \frac{(-1)^n}{a + n + 1}
     \]
   - The original integral is \(F(1)\), which requires integrating \(G(a)\) from 0 to 1:
     \[
     F(1) = \int_0^1 G(a) \, da = \sum_{n=0}^\infty (-1)^n \int_0^1 \frac{1}{a + n + 1} \, da
     \]
   - Evaluating the inner integrals and summing the resulting series, we find that the series telescopes to \((\ln 2)^2\).

2. **Numerical Approximation**:
   - The numerical value of \((\ln 2)^2\) is approximately \(0.4804530140\).

### Final Answer
The exact value of the integral is \(\boxed{(\ln 2)^2}\), and the numerical approximation is 0.4804530140.

JSON Output:
{"answer": "{(\ln 2)^2}", "numerical_answer": "0.4804530140"}