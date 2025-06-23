To solve the definite integral \(\int_0^2 x^{1/2}(2-x)^{1/2}\cosh\left(\sqrt{x(2-x)}\right)dx\), we proceed as follows:

1. **Analytical Calculation**:
   - We use the substitution \(x = 1 + \sin\theta\), transforming the integral into:
     \[
     2 \int_0^{\pi/2} \cos^2\theta \cosh(\cos\theta) \, d\theta
     \]
   - This integral is split into two parts using trigonometric identities and series expansions, leading to the involvement of modified Bessel functions of the first kind \(I_0\) and \(I_1\).
   - The result simplifies to:
     \[
     \pi \left( I_0(1) - I_1(1) \right)
     \]

2. **Numerical Approximation**:
   - Using known values of the modified Bessel functions:
     \[
     I_0(1) \approx 1.2660658777520083 \quad \text{and} \quad I_1(1) \approx 0.565159103992485
     \]
   - The numerical value is computed as:
     \[
     \pi \left( 1.2660658777520083 - 0.565159103992485 \right) \approx 2.2019635725
     \]

### Final Answer
{"answer": "\\pi \\left( I_0(1) - I_1(1) \\right)", "numerical_answer": "2.2019635725"}