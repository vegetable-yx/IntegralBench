To solve the definite integral \(\int_{-1}^1 (5x^3 - 3x)^2 \, dx\), we will follow these steps:

1. **Expand the integrand**:
   \[
   (5x^3 - 3x)^2 = (5x^3 - 3x)(5x^3 - 3x) = 25x^6 - 30x^4 + 9x^2
   \]

2. **Set up the integral**:
   \[
   \int_{-1}^1 (25x^6 - 30x^4 + 9x^2) \, dx
   \]

3. **Integrate term by term**:
   \[
   \int_{-1}^1 25x^6 \, dx - \int_{-1}^1 30x^4 \, dx + \int_{-1}^1 9x^2 \, dx
   \]

4. **Compute each integral separately**:
   - For \(\int_{-1}^1 25x^6 \, dx\):
     \[
     25 \int_{-1}^1 x^6 \, dx = 25 \left[ \frac{x^7}{7} \right]_{-1}^1 = 25 \left( \frac{1^7}{7} - \frac{(-1)^7}{7} \right) = 25 \left( \frac{1}{7} + \frac{1}{7} \right) = 25 \cdot \frac{2}{7} = \frac{50}{7}
     \]

   - For \(\int_{-1}^1 30x^4 \, dx\):
     \[
     30 \int_{-1}^1 x^4 \, dx = 30 \left[ \frac{x^5}{5} \right]_{-1}^1 = 30 \left( \frac{1^5}{5} - \frac{(-1)^5}{5} \right) = 30 \left( \frac{1}{5} + \frac{1}{5} \right) = 30 \cdot \frac{2}{5} = 12
     \]

   - For \(\int_{-1}^1 9x^2 \, dx\):
     \[
     9 \int_{-1}^1 x^2 \, dx = 9 \left[ \frac{x^3}{3} \right]_{-1}^1 = 9 \left( \frac{1^3}{3} - \frac{(-1)^3}{3} \right) = 9 \left( \frac{1}{3} + \frac{1}{3} \right) = 9 \cdot \frac{2}{3} = 6
     \]

5. **Combine the results**:
   \[
   \frac{50}{7} - 12 + 6 = \frac{50}{7} - 6 = \frac{50}{7} - \frac{42}{7} = \frac{8}{7}
   \]

6. **Numerical approximation**:
   \[
   \frac{8}{7} \approx 1.1428571429
   \]

The final answer in the required JSON format is:
```json
{"answer": "\\frac{8}{7}", "numerical_answer": "1.1428571429"}
```