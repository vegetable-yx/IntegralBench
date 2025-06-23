To solve the definite integral \(\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor\), we need to understand the behavior of the floor function \(\lfloor x \rfloor\). The floor function \(\lfloor x \rfloor\) is a step function that jumps at integer values of \(x\). Therefore, the integral can be interpreted as a sum of the integrand evaluated at these jumps.

### Step-by-Step Solution

1. **Identify the jumps of \(\lfloor x \rfloor\)**:
   - The floor function \(\lfloor x \rfloor\) jumps at \(x = 1\) and \(x = 2\) within the interval \([0, 3]\).

2. **Evaluate the integrand at these jumps**:
   - At \(x = 1\), the integrand is \(1^2 + 1 = 2\).
   - At \(x = 2\), the integrand is \(2^2 + 1 = 5\).

3. **Sum the contributions from each jump**:
   - The integral \(\int_0^3 (x^2 + 1) \, d\lfloor x \rfloor\) can be written as:
     \[
     \int_0^3 (x^2 + 1) \, d\lfloor x \rfloor = \sum_{k=1}^2 (k^2 + 1)
     \]
   - This simplifies to:
     \[
     (1^2 + 1) + (2^2 + 1) = 2 + 5 = 7
     \]

### Numerical Approximation

The exact answer is already a simple integer, so the numerical approximation is the same as the exact answer.

### Final Answer in JSON Format

```json
{"answer": "7", "numerical_answer": "7.0000000000"}
```