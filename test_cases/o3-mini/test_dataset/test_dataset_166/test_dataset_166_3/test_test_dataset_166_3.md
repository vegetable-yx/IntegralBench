We need to compute

  I = ∫₀^(π/2) (sin^(2n)x) / (sin^(2n)x + cos^(2n)x) dx.

Step 1. Notice the symmetry. Make the substitution u = π/2 - x. Then, du = -dx and when x = 0, u = π/2; when x = π/2, u = 0. Changing the limits and using symmetry, we have:

  I = ∫₀^(π/2) [sin^(2n)x] / [sin^(2n)x + cos^(2n)x] dx.

Under the substitution,
  sin x becomes cos u, and cos x becomes sin u.
Thus, the integral becomes

  I = ∫₀^(π/2) [cos^(2n)u] / [cos^(2n)u + sin^(2n)u] du.

Step 2. Denote the original integral by I and the transformed one by I'. Hence, we have

  I = ∫₀^(π/2) [sin^(2n)x] / [sin^(2n)x + cos^(2n)x] dx,
  I' = ∫₀^(π/2) [cos^(2n)x] / [sin^(2n)x + cos^(2n)x] dx.

Adding I and I' gives

  I + I' = ∫₀^(π/2) [sin^(2n)x + cos^(2n)x] / [sin^(2n)x + cos^(2n)x] dx = ∫₀^(π/2) 1 dx = π/2.

Since the transformation shows that I = I', we have

  2I = π/2  ⟹  I = π/4.

Step 3. The numerical approximation of π/4 is

  π/4 ≈ 0.7853981634 (rounded to 10 decimal places).

Final Answer in JSON format:
{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}