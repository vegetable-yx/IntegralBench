We begin by writing the given integral as a sum over the intervals [n, n + 1) for n = 0, 1, 2, … Since on each such interval the functions simplify nicely, we have

  ∫₀∞ ( {x}^(⌈x⌉) / [1 + ⌈x⌉] ) dx = Σₙ₌₀∞ Iₙ

where, for each integer n,

  Iₙ = ∫ₙⁿ⁺¹ ( {x}^(⌈x⌉) / [1 + ⌈x⌉] ) dx.

Recall that if x ∈ [n, n + 1) then the fractional part is {x} = x − n and (for n ≥ 1; note that for n = 0 almost every x in [0, 1) has ⌈x⌉ = 1) the ceiling is ⌈x⌉ = n + 1.

Thus for n ≥ 0 we have

  Iₙ = ∫ₙⁿ⁺¹ ((x − n)^(n+1) / [1 + (n+1)]) dx = 1/(n+2) ∫ₙⁿ⁺¹ (x − n)^(n+1) dx.

Make the substitution u = x − n so that when x = n, u = 0 and when x = n + 1, u = 1. Then

  Iₙ = 1/(n+2) ∫₀¹ u^(n+1) du.

Since ∫₀¹ u^(n+1) du = 1/(n+2), it follows that

  Iₙ = 1/(n+2)².

Thus the overall integral is

  ∫₀∞ ( {x}^(⌈x⌉) / (1 + ⌈x⌉) ) dx = Σₙ₌₀∞ 1/(n+2)².

Change the index by letting m = n + 2 so that when n runs from 0 to ∞, m runs from 2 to ∞. Then

  Σₙ₌₀∞ 1/(n+2)² = Σₘ₌₂∞ 1/m².

Since the Riemann zeta function ζ(2) = Σₘ₌₁∞ 1/m² = π²/6, we have

  Σₘ₌₂∞ 1/m² = ζ(2) − 1.

That is, the integral is exactly

  (π²/6) − 1.

For the numerical approximation, note that π²/6 ≈ 1.64493406685, so

  (π²/6) − 1 ≈ 0.64493406685.

Rounded to 10 decimal places, the value is 0.6449340669.

{"answer": "\\frac{\\pi^2}{6} - 1", "numerical_answer": "0.6449340669"}