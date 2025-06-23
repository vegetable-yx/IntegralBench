We begin by writing out the integral to be evaluated:

  I = ∫ from -1 to 1 (5x³ − 3x)² dx

Step 1. Expand the integrand:
  (5x³ − 3x)² = (5x³)² − 2·(5x³)(3x) + (3x)²
    = 25x⁶ − 30x⁴ + 9x²

Step 2. Rewrite the integral:
  I = ∫ from -1 to 1 (25x⁶ − 30x⁴ + 9x²) dx

Since each term is an even function (i.e., f(−x) = f(x)), we can use symmetry:
  I = 2∫ from 0 to 1 (25x⁶ − 30x⁴ + 9x²) dx

Step 3. Compute the antiderivatives term by term:
  ∫ 25x⁶ dx = 25 * (x⁷/7) = (25/7)x⁷
  ∫ (−30x⁴) dx = −30 * (x⁵/5) = −6x⁵
  ∫ 9x² dx = 9 * (x³/3) = 3x³

Thus,
  ∫ from 0 to 1 (25x⁶ − 30x⁴ + 9x²) dx = [ (25/7)x⁷ − 6x⁵ + 3x³ ] evaluated from 0 to 1.
At x = 1:
  = (25/7) − 6 + 3 = (25/7) − 3
At x = 0:
  = 0

Therefore:
  ∫ from 0 to 1 (25x⁶ − 30x⁴ + 9x²) dx = (25/7) − 3 = (25 − 21)/7 = 4/7

Now, multiply by 2 (using symmetry):
  I = 2 * (4/7) = 8/7

Step 4. Numerical approximation:
  8/7 ≈ 1.1428571429

Thus, the final answers in the requested JSON format are:
{"answer": "$\\frac{8}{7}$", "numerical_answer": "1.1428571429"}