We start by splitting the integration region into intervals of length 1. For x in the interval [n, n + 1) (with n an integer ≥ 0), we have
 • ⌈x⌉ = n + 1,
 • {x} = x − n.

Thus the integrand becomes
  ({x})^(⌈x⌉)⁄(1 + ⌈x⌉) = (x − n)^(n + 1)⁄(n + 2).

Then the integral is written as a sum:
  I = ∫₀∞ {x}^(⌈x⌉)/(1 + ⌈x⌉) dx 
    = ∑ₙ₌₀∞ ∫ₙⁿ⁺¹ (x − n)^(n + 1)⁄(n + 2) dx.

Let t = x − n, so dt = dx, and t runs from 0 to 1. Then for each n we have
  Iₙ = 1/(n + 2) ∫₀¹ t^(n + 1) dt = 1/(n + 2) ⋅ [1/(n + 2)] = 1/(n + 2)².

Thus, the overall integral becomes
  I = ∑ₙ₌₀∞ 1/(n + 2)² = ∑ₘ₌₂∞ 1/m²,
where in the last sum we set m = n + 2.

The series ∑ₘ₌₁∞ 1/m² is known to be ζ(2) = π²/6. Therefore,
  I = ζ(2) − 1 = π²/6 − 1.

A numerical evaluation gives:
  π²/6 ≈ 1.6449340668482264 ⟹ π²/6 − 1 ≈ 0.6449340668482264.
Rounded to 10 decimal places, this is 0.6449340668.

{"answer": "$\\frac{\\pi^2}{6} - 1$", "numerical_answer": "0.6449340668"}