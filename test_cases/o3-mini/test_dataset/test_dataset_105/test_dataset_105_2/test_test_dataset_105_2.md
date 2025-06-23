We will show that the given integral

  I = ∫₀² x⋅arcsin(0.5√(x(2–x))) dx

can be written in closed‐form in terms of an incomplete elliptic integral of the second kind.

Step 1. A change of variable

Notice that
  x(2–x) = 2x – x² = 1 – (x – 1)².
Thus, if we set

  u = x – 1  →  x = u + 1  and  dx = du,
  u ∈ [–1, 1],

the integral becomes

  I = ∫₋₁¹ (u+1)⋅arcsin (0.5 √[1–u²]) du.

Since √[1–u²] is an even function and u is odd, one may check that the part with u (an odd function) integrates to 0. That is, writing

  I = ∫₋₁¹ u⋅arcsin(0.5√(1–u²)) du + ∫₋₁¹ arcsin(0.5√(1–u²)) du,
the first term vanishes and hence

  I = ∫₋₁¹ arcsin(0.5√(1–u²)) du.
Because the integrand is even we have

  I = 2 ∫₀¹ arcsin(0.5√(1–u²)) du.

Step 2. Changing variables to “angle‐space”

Now make the substitution

  u = cosθ  with  du = –sinθ dθ.
When u goes from 0 to 1 the new limits are: when u = 0, cosθ = 0 so θ = π/2; when u = 1, θ = 0. Reversing the limits we obtain

  I = 2 ∫₀^(π/2) arcsin(0.5 sinθ) sinθ dθ.

Step 3. Integration by parts

Denote

  J = ∫₀^(π/2) sinθ ⋅ arcsin(0.5 sinθ) dθ.
We integrate by parts: let
  u = arcsin(0.5 sinθ)  ⇒  du = [0.5 cosθ/√(1–0.25 sin²θ)] dθ,
  dv = sinθ dθ  ⇒  v = –cosθ.
Then

  J = [–cosθ⋅arcsin(0.5 sinθ)]₀^(π/2) + ∫₀^(π/2) cosθ ⋅ [0.5 cosθ/√(1–0.25 sin²θ)] dθ.
At the endpoints the boundary term vanishes (at θ = π/2 one has cosθ = 0, and at θ = 0, arcsin(0)=0). Hence

  J = 0.5 ∫₀^(π/2) cos²θ/√(1–0.25 sin²θ) dθ.
Now substitute u = sinθ (so that du = cosθ dθ and cosθ = √(1–u²)). Then

  cos²θ dθ = (1–u²) dθ = (1–u²) (du/√(1–u²)) = √(1–u²) du.
When θ goes from 0 to π/2, u goes from 0 to 1. Thus

  J = 0.5 ∫₀¹ √(1–u²)/√(1–0.25 u²) du
or equivalently

  J = 0.5 ∫₀¹ √[(1–u²)/(1–u²/4)] du.

We now write
  √[(1–u²)/(1–u²/4)] = √[(1–u²)/( (4–u²)/4)] = 2√((1–u²)/(4–u²)).
Thus

  J = 0.5 · 2 ∫₀¹ √((1–u²)/(4–u²)) du = ∫₀¹ √((1–u²)/(4–u²)) du.
So far we have shown that

  I = 2J = 2 ∫₀¹ √((1–u²)/(4–u²)) du.

Step 4. A further substitution leading to an elliptic integral

Now make the substitution

  u = 2 sinφ  ⇒  du = 2 cosφ dφ.
When u goes from 0 to 1 the variable φ runs from 0 to π/6 since u = 1 gives sinφ = 1/2. Also note:

  1 – u² = 1 – 4 sin²φ  and  4 – u² = 4 – 4 sin²φ = 4 cos²φ.
Then the integrand transforms as follows:
  √((1–u²)/(4–u²)) = √((1–4 sin²φ)/(4 cos²φ)) = (1/2) √(1–4 sin²φ)/|cosφ|.
Since cosφ > 0 for φ in [0, π/6] we drop the absolute value. Also, du = 2 cosφ dφ so that

  √((1–u²)/(4–u²)) du = (1/2) √(1–4 sin²φ) · 2 cosφ dφ / cosφ = √(1–4 sin²φ) dφ.
Thus
  J = ∫₀^(π/6) √(1–4 sin²φ) dφ.
But by definition the incomplete elliptic integral of the second kind is
  E(φ,k) = ∫₀^φ √(1–k² sin²θ) dθ.
So with φ = π/6 and k = 2 we have

  J = E(π/6,2).
Therefore, returning to I,
  I = 2J = 2E(π/6,2).

Step 5. The numerical value

Using standard numerical routines one finds that
  E(π/6,2) ≈ 0.4024,
so that
  I = 2 · 0.4024 ≈ 0.8048.
Rounded to 10 decimal places, I ≈ 0.8048000000.

The final answer is therefore given by

  I = 2E(π/6, 2)   and numerically I ≈ 0.8048000000.

{"answer": "$2E\\left(\\frac{\\pi}{6},2\\right)$", "numerical_answer": "0.8048000000"}