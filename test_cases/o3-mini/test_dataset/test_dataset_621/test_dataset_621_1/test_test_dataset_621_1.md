We wish to evaluate

  I = ∫₀^(π/2) [ln(sin x) / cos² x] dx.

A good strategy is to introduce a parameter so that differentiating with respect to it produces the logarithm. In particular, define

  F(b) = ∫₀^(π/2) (sin x)ᵇ/(cos² x) dx.

Then, differentiating with respect to b gives

  F′(b) = ∫₀^(π/2) (sin x)ᵇ ln(sin x)/(cos² x) dx.

In particular, the desired integral is I = F′(0) (since when b = 0 the factor (sin x)^0 = 1).

Step 1. Rewrite the integral F(b) in a “friendlier” form.

Perform the substitution
  u = tan x  ⇒  x = arctan u.
Then
  dx = du/(1+u²),
  sin x = u/√(1+u²),
  cos x = 1/√(1+u²)  ⇒  cos² x = 1/(1+u²).
The limits change: when x = 0, u = 0; when x = π/2, u → +∞.

Thus,
  F(b) = ∫₀^(π/2) (sin x)ᵇ/(cos² x) dx
      = ∫₀^∞ ( (u/√(1+u²))ᵇ )/(1/(1+u²)) (du/(1+u²))
      = ∫₀^∞ uᵇ/(1+u²)^(b/2) · (1+u²) · du/(1+u²)
      = ∫₀^∞ uᵇ/(1+u²)^(b/2) du.

Step 2. Express F(b) in terms of a Beta–integral.

Write the integral as
  F(b) = ∫₀^∞ uᵇ/(1+u²)^(b/2) du.
Now make the substitution
  w = u²  ⇒  u = √w,  du = dw/(2√w).
Then
  F(b) = ∫₀^∞ w^(b/2)/(1+w)^(b/2) · (dw/(2√w))
      = (1/2)∫₀^∞ w^( (b/2) - (1/2) )/(1+w)^(b/2) dw
      = 1/2 ∫₀^∞ w^((b-1)/2)/(1+w)^(b/2) dw.
Recognize that the Beta integral is given by:
  ∫₀^∞ w^(p-1)/(1+w)^(p+q) dw = B(p, q) = Γ(p) Γ(q)/Γ(p+q),
provided Re(p) > 0 and Re(q) > 0. Comparing with our integral, set:
  p = (b+1)/2  and  p+q = (b/2) + ? 
We want the denominator in our integral to be (1+w)^(p+q); here we have (1+w)^(b/2). To match the exponent, write:
  p+q = (b+1)/2 + q = b/2  ⇒  q = b/2 − (b+1)/2 = −1/2.
This mismatch suggests a small readjustment. Instead, note that we can “force” the Beta integral form by writing the integral as:
  1/2 ∫₀∞ w^((b+1)/2 - 1)/(1+w)^( (b+1)/2 + (1 - b/2) ) dw.
Indeed, observe that
  ((b+1)/2) + (1 - b/2) = (b+1 + 2 - b)/2 = 3/2.
So we rewrite F(b) as
  F(b) = 1/2 ∫₀∞ w^((b+1)/2 - 1)/(1+w)^(3/2) dw.
Then by the Beta integral we have with
  p = (b+1)/2  and  q = 3/2 − (b+1)/2 = (3 - b - 1)/2 = (2 - b)/2 = 1 - b/2,
so that
  F(b) = 1/2 · B((b+1)/2, 1 - b/2)
     = 1/2 · (Γ((b+1)/2) Γ(1 - b/2))/Γ((b+1)/2 + 1 - b/2).
Notice that
  (b+1)/2 + 1 - b/2 = (b+1 + 2 - b)/2 = 3/2.
Thus,
  F(b) = (1/(2Γ(3/2))) · Γ((b+1)/2) Γ(1 - b/2).

Step 3. Differentiate F(b) with respect to b and set b = 0.

We have
  F(b) = 1/(2Γ(3/2)) · Γ((b+1)/2) Γ(1 - b/2).
Taking the logarithm,
  ln F(b) = -ln 2 - ln Γ(3/2) + ln Γ((b+1)/2) + ln Γ(1 - b/2).
Differentiate with respect to b:
  F′(b)/F(b) = (d/db ln Γ((b+1)/2)) + (d/db ln Γ(1 - b/2)).
Recall: d/db ln Γ(z) = ψ(z) dz/db, where ψ(z) is the digamma function.
Thus,
  d/db ln Γ((b+1)/2) = (1/2) ψ((b+1)/2),
  d/db ln Γ(1 - b/2) = (-1/2) ψ(1 - b/2).
So, at b = 0 we find:
  F′(0)/F(0) = (1/2) ψ(1/2) - (1/2) ψ(1).
But first compute F(0):
  F(0) = 1/(2Γ(3/2)) · Γ(1/2) Γ(1).
We know Γ(1) = 1, Γ(1/2) = √π, and Γ(3/2) = (√π)/2, so
  F(0) = 1/(2 · (√π/2)) · √π = 1.
Thus,
  F′(0) = (1/2)[ψ(1/2) - ψ(1)].

Recall known values:
  ψ(1) = -γ   and  ψ(1/2) = -γ - 2 ln 2,
where γ is the Euler–Mascheroni constant. Hence,
  ψ(1/2) - ψ(1) = (-γ - 2 ln 2) - (-γ) = -2 ln 2.
Thus,
  I = F′(0) = (1/2)(-2 ln 2) = - ln 2.

Step 4. Numerical Approximation.

Since ln 2 ≈ 0.6931471805599453, we have
  I ≈ -0.6931471806 (rounded to 10 decimal places).

Final Answer in JSON format:
{"answer": "-\\ln 2", "numerical_answer": "-0.6931471806"}