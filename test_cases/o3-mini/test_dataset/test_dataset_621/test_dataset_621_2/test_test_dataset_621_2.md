We wish to evaluate

  I = ∫₀^(π/2) [ln(sin x)]/(cos² x) dx.

A very effective approach is to use integration by parts. We choose

  u = ln(sin x), dv = (1/cos² x) dx = sec² x dx.

Then we have

  du = (d/dx)[ln(sin x)] dx = (cos x/sin x) dx = cot x dx,
  v = ∫ sec² x dx = tan x.

By the integration by parts formula

  ∫ u dv = [u v]₀^(π/2) − ∫₀^(π/2) v du,
we obtain

  I = [ln(sin x) tan x]₀^(π/2) − ∫₀^(π/2) tan x · cot x dx.

Let us examine the boundary term [ln(sin x) tan x]₀^(π/2).

1. As x → π/2:
  sin(π/2) = 1 so ln(sin(π/2)) = 0.
  tan(π/2) diverges; however, the product has an indeterminate form 0·∞.
  To analyze it, set u = π/2 − x for small u > 0.
  Then, near x = π/2:
   sin x = cos u ≈ 1 – u²/2  ⇒ ln(sin x) ≈ −u²/2,
   tan x = cot u ≈ 1/u.
  Thus ln(sin x) tan x ≈ (−u²/2)·(1/u) = −u/2 → 0.
  So the contribution at x = π/2 is 0.

2. As x → 0:
  sin x ≈ x  ⇒ ln(sin x) ≈ ln x,
  tan x ≈ x,
  so ln(sin x) tan x ≈ x ln x → 0.
  Thus the contribution at x = 0 is also 0.

Therefore, the boundary term is 0 and we are left with

  I = − ∫₀^(π/2) tan x · cot x dx.

Now, note that

  tan x · cot x = (sin x/cos x)·(cos x/sin x) = 1.

Thus the integral simplifies to

  I = − ∫₀^(π/2) 1 dx = − [x]₀^(π/2) = − (π/2).

So the exact value is

  I = −π/2.

For a numerical approximation, we have

  −π/2 ≈ −1.5707963268  (rounded to 10 decimal places).

According to the instructions, here is the JSON output:

{"answer": "-\\frac{\\pi}{2}", "numerical_answer": "-1.5707963268"}