We begin with the integral

  I = ∫₋₁¹ x² · √[3](x³ + 1) dx.

Step 1. Substitution

Let u = x³ + 1. Then, differentiate:
  du/dx = 3x², or x² dx = du/3.

When x = –1, u = (–1)³ + 1 = 0.
When x = 1, u = 1³ + 1 = 2.

Thus, the integral becomes:
  I = ∫₍u=0₎^(2) u^(1/3) · (1/3) du = (1/3) ∫₀² u^(1/3) du.

Step 2. Evaluate the Integral

Compute ∫ u^(1/3) du:
  ∫ u^(1/3) du = (3/4) u^(4/3) + C.

Substitute back:
  I = (1/3) · (3/4) [u^(4/3)] evaluated from 0 to 2
    = (1/4) [2^(4/3) – 0^(4/3)]
    = (1/4) · 2^(4/3).

Thus, the analytic answer is
  I = 2^(4/3)/4.

Step 3. Numerical Approximation

Now, calculate:
  2^(4/3) = exp((4/3) ln 2) ≈ exp(0.924196) ≈ 2.5198420998.
Then,
  I ≈ 2.5198420998 / 4 ≈ 0.6299605249.

Step 4. Final Answer in JSON Format

{"answer": "$\\frac{2^{\\frac{4}{3}}}{4}$", "numerical_answer": "0.6299605249"}