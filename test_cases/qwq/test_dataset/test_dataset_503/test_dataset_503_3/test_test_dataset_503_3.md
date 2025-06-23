To compute the definite integral \(\int_0^\pi \cos(x)\cos(3x)\cos(5x)\,dx\), we follow these steps:

1. **Simplify the integrand using trigonometric identities**:
   - First, apply the product-to-sum formula to \(\cos(x)\cos(3x)\):
     \[
     \cos(x)\cos(3x) = \frac{\cos(4x) + \cos(2x)}{2}
     \]
   - Multiply the result by \(\cos(5x)\):
     \[
     \frac{\cos(4x) + \cos(2x)}{2} \cdot \cos(5x)
     \]
   - Apply the product-to-sum formula to each term:
     \[
     \cos(4x)\cos(5x) = \frac{\cos(9x) + \cos(x)}{2}
     \]
     \[
     \cos(2x)\cos(5x) = \frac{\cos(7x) + \cos(3x)}{2}
     \]
   - Combine these results:
     \[
     \cos(x)\cos(3x)\cos(5x) = \frac{\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)}{4}
     \]

2. **Integrate term by term**:
   - The integral becomes:
     \[
     \frac{1}{4} \int_0^\pi \left[\cos(9x) + \cos(x) + \cos(7x) + \cos(3x)\right] dx
     \]
   - Each term \(\cos(kx)\) integrated over \([0, \pi]\) evaluates to zero because \(\sin(k\pi) = 0\) for any integer \(k\):
     \[
     \int_0^\pi \cos(kx) \, dx = \left[\frac{\sin(kx)}{k}\right]_0^\pi = 0
     \]
   - Summing these results, the entire integral is zero.

3. **Numerical approximation**:
   - The exact result is \(0\), so the numerical approximation to 10 decimal places is \(0.0000000000\).

### Final Answer
{"answer": "0", "numerical_answer": "0.0000000000"}