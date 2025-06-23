We wish to evaluate

  I = ∫₀² x^(–1/2) · (2 – x)^(–1/2) · [1 – 0.5·x(2 – x)] dx.

Step 1. Use the substitution x = 2 sin²θ.
• When x = 0, sin²θ = 0 so θ = 0.
• When x = 2, sin²θ = 1 so θ = π/2.
Also, dx/dθ = 4 sinθ cosθ so dx = 4 sinθ cosθ dθ.

Step 2. Rewrite the integrand in terms of θ.
• Note that
  x^(–1/2) = (2 sin²θ)^(–1/2) = 1/(√2 sinθ),
  (2 – x)^(–1/2) = [2 – 2 sin²θ]^(–1/2) = (2 cos²θ)^(–1/2) = 1/(√2 cosθ).
Thus, their product is
  [1/(√2 sinθ)]·[1/(√2 cosθ)] = 1/(2 sinθ cosθ).

• Next, observe that
  x(2 – x) = (2 sin²θ)(2 – 2 sin²θ) = 4 sin²θ cos²θ,
so
  0.5 · x(2 – x) = 2 sin²θ cos²θ,
and then
  [1 – 0.5·x(2 – x)] = 1 – 2 sin²θ cos²θ.

Step 3. Substitute into the integral.
The new integral becomes:
  I = ∫₀^(π/2) { [1/(2 sinθ cosθ)] · [1 – 2 sin²θ cos²θ] · [4 sinθ cosθ dθ] }.
Cancellation of sinθ cosθ yields:
  I = 2 ∫₀^(π/2) [1 – 2 sin²θ cos²θ] dθ.

Step 4. Simplify the remaining integrand.
Note that sin²θ cos²θ = ¼ sin²(2θ) (since sin(2θ) = 2 sinθ cosθ).
Thus,
  1 – 2 sin²θ cos²θ = 1 – 2·(1/4) sin²(2θ) = 1 – ½ sin²(2θ).

Therefore,
  I = 2 ∫₀^(π/2) [1 – ½ sin²(2θ)] dθ
    = 2 {∫₀^(π/2) dθ – (1/2) ∫₀^(π/2) sin²(2θ) dθ}.

Step 5. Evaluate the sub-integrals.
The first integral is straightforward:
  ∫₀^(π/2) dθ = π/2.
For the second, use the substitution u = 2θ so that du = 2 dθ and dθ = du/2. When θ = 0, u = 0; when θ = π/2, u = π. Thus,
  ∫₀^(π/2) sin²(2θ) dθ = (1/2) ∫₀^π sin²u du.
It is known that ∫₀^π sin²u du = π/2.
So,
  ∫₀^(π/2) sin²(2θ) dθ = (1/2)(π/2) = π/4.

Step 6. Combine the results.
  I = 2 { (π/2) – (1/2)(π/4) } = 2 { (π/2) – (π/8) } = 2 { (4π – π)/8 } = 2·(3π/8) = (3π)/4.

Step 7. Numerical approximation.
  (3π)/4 ≈ (3×3.1415926536)/4 ≈ 2.3561944902.

Thus, the final answers are:

Exact answer: (3π)/4,
Numerical approximation: 2.3561944902.

{"answer": "$\\frac{3\\pi}{4}$", "numerical_answer": "2.3561944902"}