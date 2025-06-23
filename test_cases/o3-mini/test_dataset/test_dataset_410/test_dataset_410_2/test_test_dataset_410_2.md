We wish to compute

  I = ∫₀∞ e^(–x²) cos(2x) dx.

Step 1. Recall the standard formula:
  ∫₀∞ e^(–αx²) cos(βx) dx = (1/2) √(π/α) exp(–β²/(4α)),  for α > 0.

Step 2. In our case, α = 1 and β = 2 so that:
  I = (1/2) √π exp(–(2²)/(4))
   = (√π/2) exp(–4/4)
   = (√π/2) e^(–1).

Step 3. Numerical evaluation:
  √π ≈ 1.772453850905516 and hence √π/2 ≈ 0.886226925452758.
  Multiplying by e^(–1) (where e^(–1) ≈ 0.367879441171442) gives:
  I ≈ 0.886226925452758 × 0.367879441171442 ≈ 0.3260246661.

{"answer": "\\frac{\\sqrt{\\pi}}{2}e^{-1}", "numerical_answer": "0.3260246661"}