We wish to evaluate

  I = ∫₋₁¹ 1/(3ˣ + 1) dx.

Step 1. Notice that if we let u = –x, then the differential du = –dx and the limits swap. Performing the substitution gives

  I = ∫₋₁¹ 1/(3^(–x) + 1) dx = ∫₋₁¹ 1/(3^(–x) + 1) dx.

Since 3^(–x) = 1/3ˣ, we have
  1/(3^(–x) + 1) = 1/((1/3ˣ) + 1) = 3ˣ/(3ˣ + 1).

So we obtain a second expression for the integral:

  I = ∫₋₁¹ 3ˣ/(3ˣ + 1) dx.

Step 2. Add the two expressions for I:
  I + I = ∫₋₁¹ [1/(3ˣ + 1) + 3ˣ/(3ˣ + 1)] dx
     = ∫₋₁¹ [1 + 3ˣ]/(3ˣ + 1) dx
     = ∫₋₁¹ 1 dx
     = 2.

Thus, 2I = 2, which implies I = 1.

Step 3. The exact result is 1, and numerically this is 1.0000000000 (to 10 decimal places).

{"answer": "1", "numerical_answer": "1.0000000000"}