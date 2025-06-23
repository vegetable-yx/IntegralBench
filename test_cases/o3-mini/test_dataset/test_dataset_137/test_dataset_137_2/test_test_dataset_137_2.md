We begin with the integral

  I = ∫₀⁴ x^(–1/2) (4 – x)^(–1/2) [1 – 0.25·x·(4 – x)]^(1/2) dx.

Step 1. Substitute x = 4 sin²θ. Then the limits change as follows:
  When x = 0, sin²θ = 0 ⟹ θ = 0;
  When x = 4, sin²θ = 1 ⟹ θ = π/2.
Also, dx = 8 sinθ cosθ dθ, and note that

  √x = 2 sinθ,
  √(4 – x) = 2 cosθ.
Thus,
  x^(–1/2)(4 – x)^(–1/2) = 1/(√x √(4 – x)) = 1/(2 sinθ · 2 cosθ) = 1/(4 sinθ cosθ).

So, the product dx · [x^(–1/2)(4 – x)^(–1/2)] becomes

  [8 sinθ cosθ dθ] / [4 sinθ cosθ] = 2 dθ.

Step 2. Next, simplify the square root factor. We have:
  x(4 – x) = [4 sin²θ][4 cos²θ] = 16 sin²θ cos²θ.
Thus,
  0.25 · x(4 – x) = 4 sin²θ cos²θ.
Recall that 4 sin²θ cos²θ = sin²2θ (since sin2θ = 2 sinθ cosθ). Hence,

  [1 – 0.25·x·(4 – x)]^(1/2) = [1 – sin²2θ]^(1/2) = |cos2θ|.

Since θ ranges from 0 to π/2, the expression cos2θ is positive for 0 ≤ θ ≤ π/4 and negative for π/4 ≤ θ ≤ π/2. Taking the absolute value, we break the integral into two parts.

Step 3. The transformed integral becomes

  I = 2 ∫₀^(π/2) |cos2θ| dθ.

Split the integral at θ = π/4:
  I = 2 [ ∫₀^(π/4) cos2θ dθ + ∫_(π/4)^(π/2) (–cos2θ) dθ ].

Evaluate each part:
- For the first part, note that ∫ cos2θ dθ = (1/2) sin2θ. Then,
  ∫₀^(π/4) cos2θ dθ = (1/2)[sin(π/2) – sin0] = (1/2)[1 – 0] = 1/2.
- For the second part,
  ∫_(π/4)^(π/2) cos2θ dθ = (1/2)[sin(π) – sin(π/2)] = (1/2)[0 – 1] = –1/2.
Since the integrand in the second interval is –cos2θ, we have:
  ∫_(π/4)^(π/2) (–cos2θ) dθ = –(–1/2) = 1/2.

Thus, the total integral is

  I = 2 [ (1/2) + (1/2) ] = 2·(1) = 2.

Step 4. Finally, the analytical (exact) answer is 2. Its numerical approximation, to 10 decimal places, is 2.0000000000.

{"answer": "$2$", "numerical_answer": "2.0000000000"}