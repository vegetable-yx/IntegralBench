To compute the definite integral \(\int_0^\pi \cos(x)\cos(3x)\cos(5x)\,dx\), we proceed as follows:

1. **Apply trigonometric identities to simplify the integrand:**
   - First, use the product-to-sum formula on \(\cos(x)\cos(3x)\):
     \[
     \cos(x)\cos(3x) = \frac{\cos(4x) + \cos(2x)}{2}
     \]
   - Substitute this back into the integral:
     \[
     \int_0^\pi \cos(x)\cos(3x)\cos(5x)\,dx = \frac{1}{2} \int_0^\pi \left[\cos(4x) + \cos(2x)\right]\cos(5x)\,dx
     \]
   - Split the integral into two parts:
     \[
     \frac{1}{2} \left( \int_0^\pi \cos(4x)\cos(5x)\,dx + \int_0^\pi \cos(2x)\cos(5x)\,dx \right)
     \]

2. **Simplify each integral using product-to-sum identities:**
   - For \(\int_0^\pi \cos(4x)\cos(5x)\,dx\):
     \[
     \cos(4x)\cos(5x) = \frac{\cos(9x) + \cos(x)}{2}
     \]
     \[
     \int_0^\pi \cos(4x)\cos(5x)\,dx = \frac{1}{2} \left( \int_0^\pi \cos(9x)\,dx + \int_0^\pi \cos(x)\,dx \right)
     \]
   - For \(\int_0^\pi \cos(2x)\cos(5x)\,dx\):
     \[
     \cos(2x)\cos(5x) = \frac{\cos(7x) + \cos(3x)}{2}
     \]
     \[
     \int_0^\pi \cos(2x)\cos(5x)\,dx = \frac{1}{2} \left( \int_0^\pi \cos(7x)\,dx + \int_0^\pi \cos(3x)\,dx \right)
     \]

3. **Evaluate each integral:**
   - Each integral of the form \(\int_0^\pi \cos(nx)\,dx\) for integer \(n\) evaluates to zero because \(\sin(n\pi) = 0\):
     \[
     \int_0^\pi \cos(nx)\,dx = \left[ \frac{\sin(nx)}{n} \right]_0^\pi = 0
     \]
   - Therefore, all four integrals \(\int_0^\pi \cos(9x)\,dx\), \(\int_0^\pi \cos(x)\,dx\), \(\int_0^\pi \cos(7x)\,dx\), and \(\int_0^\pi \cos(3x)\,dx\) are zero.

4. **Combine the results:**
   - Substituting back, all terms become zero:
     \[
     \frac{1}{4} \left( 0 + 0 + 0 + 0 \right) = 0
     \]

5. **Numerical approximation:**
   - The numerical value is \(0.0000000000\) when rounded to 10 decimal places.

### Final Answer
{"answer": "0", "numerical_answer": "0.0000000000"}