We start by considering the integral

  I = ∫₋₁¹ x² · ∛(x³ + 1) dx.

Step 1. Substitution:
Let u = x³ + 1. Then, differentiate:
  du/dx = 3x² ⟹ x² dx = du/3.

Change the limits of integration:
  When x = –1, u = (–1)³ + 1 = –1 + 1 = 0,
  When x = 1, u = 1³ + 1 = 1 + 1 = 2.

Thus, the integral becomes:
  I = (1/3) ∫₀² u^(1/3) du.

Step 2. Integration:
Evaluate the integral ∫ u^(1/3) du:
  ∫ u^(1/3) du = (3/4) u^(4/3) + C.
So,
  I = (1/3) · (3/4) [u^(4/3)]₀² = (1/4) [2^(4/3) – 0^(4/3)] = (2^(4/3))/4.

Step 3. Simplification:
Notice that 2^(4/3) = 2 · 2^(1/3), so one may also write the answer as:
  I = [2 · 2^(1/3)]/4 = 2^(1/3)/2.

Step 4. Numerical Approximation:
Calculate 2^(1/3) (cube root of 2) approximately:
  2^(1/3) ≈ 1.2599210499,
Thus,
  I ≈ 1.2599210499/2 ≈ 0.6299605249.

Final Answer in JSON format:
{"answer": "\\frac{2^{4/3}}{4}", "numerical_answer": "0.6299605249"}