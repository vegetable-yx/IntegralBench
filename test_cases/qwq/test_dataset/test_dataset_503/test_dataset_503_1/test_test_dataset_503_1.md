To compute the definite integral \(\int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx\), we proceed as follows:

1. **Apply Product-to-Sum Identities**:
   - First, use the identity \(\cos(A)\cos(B) = \frac{1}{2}[\cos(A+B) + \cos(A-B)]\) on \(\cos(x)\cos(3x)\):
     \[
     \cos(x)\cos(3x) = \frac{1}{2}[\cos(4x) + \cos(2x)]
     \]
   - Substitute this back into the integral:
     \[
     \int_0^\pi \cos(x)\cos(3x)\cos(5x) \, dx = \frac{1}{2} \int_0^\pi [\cos(4x) + \cos(2x)]\cos(5x) \, dx
     \]
   - Split the integral into two parts:
     \[
     \frac{1}{2} \left( \int_0^\pi \cos(4x)\cos(5x) \, dx + \int_0^\pi \cos(2x)\cos(5x) \, dx \right)
     \]

2. **Apply Product-to-Sum Identities Again**:
   - For \(\cos(4x)\cos(5x)\):
     \[
     \cos(4x)\cos(5x) = \frac{1}{2}[\cos(9x) + \cos(x)]
     \]
   - For \(\cos(2x)\cos(5x)\):
     \[
     \cos(2x)\cos(5x) = \frac{1}{2}[\cos(7x) + \cos(3x)]
     \]
   - Substitute these back into the integrals:
     \[
     \frac{1}{2} \left( \frac{1}{2} \int_0^\pi [\cos(9x) + \cos(x)] \, dx + \frac{1}{2} \int_0^\pi [\cos(7x) + \cos(3x)] \, dx \right)
     \]

3. **Evaluate Each Integral**:
   - Each integral of the form \(\int_0^\pi \cos(kx) \, dx\) evaluates to zero because \(\sin(k\pi) = 0\) for integer \(k\):
     \[
     \int_0^\pi \cos(9x) \, dx = 0, \quad \int_0^\pi \cos(x) \, dx = 0, \quad \int_0^\pi \cos(7x) \, dx = 0, \quad \int_0^\pi \cos(3x) \, dx = 0
     \]
   - Combining these results:
     \[
     \frac{1}{4} \left( 0 + 0 + 0 + 0 \right) = 0
     \]

4. **Numerical Approximation**:
   - The numerical approximation of the integral is \(0.0000000000\).

### Final Answer
{"answer": "0", "numerical_answer": "0.0000000000"}