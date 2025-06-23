We want to calculate

  I = ∫₀∞ e^(–x²) cos(2x) dx.

Step 1. Recognize that there is a standard formula for integrals of the form

  ∫₀∞ e^(–a x²) cos(bx) dx = ½ √(π/a) exp(–b²/(4a)),  (a > 0).

Here, we have a = 1 and b = 2. Substituting these values gives

  I = ½ √π exp[–(2²)/(4)] = ½ √π exp(–1).

Thus, the exact answer is

  (√π/2) e^(–1).

Step 2. Compute the numerical approximation.
We have:
  √π ≈ 1.7724538509,
  ½ √π ≈ 0.88622692545,
  e^(–1) ≈ 0.36787944117.

Multiplying these:

  0.88622692545 × 0.36787944117 ≈ 0.32602466609.

Rounded to 10 decimal places, the numerical approximation is 0.3260246661.

{"answer": "\\frac{\\sqrt{\\pi}}{2} e^{-1}", "numerical_answer": "0.3260246661"}