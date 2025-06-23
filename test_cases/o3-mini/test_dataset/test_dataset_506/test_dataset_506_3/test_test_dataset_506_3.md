We wish to evaluate

  I = ∫₁²⁰¹¹ (√x)/(√(2012 – x) + √x) dx.

Step 1. Notice the symmetry of the integrand. Perform the substitution
  u = 2012 – x  ⇒  du = –dx.
When x = 1, then u = 2011; and when x = 2011, then u = 1.
Thus, the integral becomes
  I = ∫ₓ₌₁⁽²⁰¹¹⁾ (√x)/(√(2012 – x) + √x) dx
    = ∫ᵤ₌₂₀₁₁¹ (√(2012 – u))/(√u + √(2012 – u)) (–du)
    = ∫₁²⁰₁₁ (√(2012 – u))/(√u + √(2012 – u)) du.
Let’s denote this new form as J, so that
  J = ∫₁²₀₁₁ (√(2012 – x))/(√x + √(2012 – x)) dx.

Step 2. Now add the original and the substituted forms:
  I + J = ∫₁²₀₁₁ [√x + √(2012 – x)]/(√(2012 – x) + √x) dx
      = ∫₁²₀₁₁ 1 dx
      = (2011 – 1) = 2010.
Since the substitution shows that I = J, we have
  2I = 2010  ⇒  I = 1005.

Step 3. The exact answer is 1005. For a numerical approximation (to 10 decimal places), we write it as 1005.0000000000.

Thus, the final result is:

{"answer": "$1005$", "numerical_answer": "1005.0000000000"}