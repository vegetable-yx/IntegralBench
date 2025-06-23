We wish to evaluate

  I = ∫₀⁴ x^(–1/2) (4 – x)^(–1/2) [1 – 0.25 x (4 – x)]^(1/2) dx.

Step 1. Use a substitution that “symmetrizes” the two algebraic factors. Let

  x = 4 sin²θ,
  so that dx = 8 sinθ cosθ dθ.
  When x = 0, sin²θ = 0 so θ = 0; and when x = 4, sin²θ = 1 so θ = π/2.

Step 2. Rewrite the factors in terms of θ.
 • x^(–1/2) = (4 sin²θ)^(–1/2) = 1/(2 sinθ).
 • (4 – x)^(–1/2) = [4 – 4 sin²θ]^(–1/2) = [4 cos²θ]^(–1/2) = 1/(2 cosθ).
 • Thus, the product
   x^(–1/2)(4 – x)^(–1/2) = 1/(4 sinθ cosθ).
 • The differential dx = 8 sinθ cosθ dθ.
 • Therefore, the combination dx/(4 sinθ cosθ) simplifies to:
   [8 sinθ cosθ dθ] / [4 sinθ cosθ] = 2 dθ.

Next, handle the remaining square-root factor. Notice that:
  x (4 – x) = 4 sin²θ · 4 cos²θ = 16 sin²θ cos²θ.
Thus,
  1 – 0.25 x (4 – x) = 1 – 0.25 (16 sin²θ cos²θ) = 1 – 4 sin²θ cos²θ.
Now write sin²θ cos²θ in terms of a double-angle. Since
  sin²θ cos²θ = (1/4)sin²2θ,
it follows that
  4 sin²θ cos²θ = sin²2θ.
Therefore, the square-root becomes:
  [1 – 4 sin²θ cos²θ]^(1/2) = [1 – sin²2θ]^(1/2) = |cos2θ|.
For θ ∈ [0, π/2], cos2θ is positive for 0 ≤ θ ≤ π/4 and negative for π/4 < θ ≤ π/2. Thus, we must take the absolute value.

Step 3. Write the integral in terms of θ. Combining all factors,
  I = ∫₀^(π/2) 2 · |cos2θ| dθ.
We now split the interval where cos2θ changes sign:
  I = 2 [∫₀^(π/4) cos2θ dθ + ∫_(π/4)^(π/2) (–cos2θ) dθ].

Step 4. Evaluate the two integrals.
Recall that ∫ cos2θ dθ = (1/2) sin2θ.

For the first part:
  I₁ = ∫₀^(π/4) cos2θ dθ = (1/2)[sin2θ]₀^(π/4) = (1/2)(sin(π/2) – sin0) = 1/2.
For the second part:
  I₂ = ∫_(π/4)^(π/2)(–cos2θ) dθ = –∫_(π/4)^(π/2) cos2θ dθ = –(1/2)[sin2θ]_(π/4)^(π/2).
Now, compute the limits:
  sin2(π/2) = sinπ = 0,
  sin2(π/4) = sin(π/2) = 1.
Thus,
  I₂ = –(1/2)(0 – 1) = 1/2.

So, the entire integral becomes:
  I = 2 [I₁ + I₂] = 2 (1/2 + 1/2) = 2 · 1 = 2.

Step 5. Conclusion.

The exact value of the integral is 2, and its numerical approximation is 2.0000000000 (to ten decimal places).

{"answer": "$2$", "numerical_answer": "2.0000000000"}