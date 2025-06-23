We start with the integral

  I = ∫₋₁⁰ 5(x⁶ + x)⁴ dx.

Notice that
  x⁶ + x = x(x⁵ + 1).

Raising to the fourth power we have
  (x⁶ + x)⁴ = [x(x⁵ + 1)]⁴ = x⁴ (x⁵ + 1)⁴.

Thus the integral becomes

  I = ∫₋₁⁰ 5 x⁴ (x⁵ + 1)⁴ dx.

Now, recognize that the derivative of (x⁵ + 1) is 5x⁴. This suggests the substitution

  u = x⁵ + 1  ⟹ du = 5x⁴ dx.

The differential 5x⁴ dx in the integral is exactly du, so the integral rewrites as

  I = ∫ u⁴ du.

We must also update the limits of integration in terms of u:
  When x = –1: u = (–1)⁵ + 1 = –1 + 1 = 0,
  When x = 0: u = 0⁵ + 1 = 1.

Thus, the integral becomes

  I = ∫₀¹ u⁴ du.

This integral is elementary:

  I = [u⁵/5]₀¹ = (1⁵/5) – (0⁵/5) = 1/5.

Thus, the exact value of the integral is 1/5. The numerical approximation of 1/5 is 0.2, which rounded to 10 decimal places is 0.2000000000.

{"answer": "\\frac{1}{5}", "numerical_answer": "0.2000000000"}