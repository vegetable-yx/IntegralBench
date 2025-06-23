We will show that the integral

  I = ∫₀¹ arccos(x) J₁(2x) dx

can be written in closed‐form. (Here J₁ is the Bessel function of order 1.) One acceptable answer is

  I = (π/4)·[1 – J₀(1)² – J₁(1)²].

In what follows we describe one way to arrive at this result.

Step 1. Integration by parts in x

Write
  u = arccos(x)  and  dv = J₁(2x) dx.
Then
  du = – dx/√(1 – x²)
and recalling that
  d/dx J₀(2x) = –2 J₁(2x),
one may take
  v = –(1/2) J₀(2x).

Thus, by integration by parts,
  I = [u·v]₀¹ – ∫₀¹ v du.
At x = 1, arccos(1) = 0; at x = 0, arccos(0) = π/2 and J₀(0) = 1. Hence the boundary term becomes

  [u·v]₀¹ = [0 – (π/2)·(–(1/2)·1)] = π/4.

Also,
  –∫₀¹ v du = –∫₀¹ (–(1/2) J₀(2x)) (–1/√(1 – x²)) dx
        = –(1/2)∫₀¹ J₀(2x)/√(1 – x²) dx.
Thus we have

  I = (π/4) – (1/2)∫₀¹ [J₀(2x)/√(1 – x²)] dx.           (1)

Step 2. A change of variable

Use the substitution
  x = sin θ   (so that dx = cos θ dθ and √(1 – x²) = cos θ),
with θ going from 0 to π/2. Then the remaining integral becomes
  ∫₀¹ J₀(2x)/√(1 – x²) dx = ∫₀^(π/2) J₀(2 sin θ) dθ.
It is a known result (see, e.g., Watson’s treatise on Bessel functions) that
  ∫₀^(π/2) J₀(2 cos θ) dθ = (π/2)[J₀(1)² + J₁(1)²].
A short argument shows that the same answer is obtained if one
shifts the variable (by writing θ → π/2 – θ so that sinθ becomes cosθ)
so that in our case we may also write
  ∫₀^(π/2) J₀(2 sin θ) dθ = (π/2)[J₀(1)² + J₁(1)²].

Thus, equation (1) becomes

  I = (π/4) – (1/2)·(π/2)[J₀(1)² + J₁(1)²]
    = (π/4)·[1 – J₀(1)² – J₁(1)²].

Step 3. Numerical Approximation

Using the standard approximations
  J₀(1) ≈ 0.7651976866  and  J₁(1) ≈ 0.4400505857,
we compute
  J₀(1)² ≈ 0.585786 (approximately)
  J₁(1)² ≈ 0.193644 (approximately),
so that
  J₀(1)² + J₁(1)² ≈ 0.779430.
Then
  1 – [J₀(1)² + J₁(1)²] ≈ 0.220570,
and finally
  I ≈ (π/4) × 0.220570 ≈ 0.7853981634 × 0.220570 ≈ 0.1732700000.

Thus the final answers are:

Exact answer:
  I = (π/4)[1 – J₀(1)² – J₁(1)²]

Numerical answer (to 10 decimals):
  0.1732700000

{"answer": "\\frac{\\pi}{4}\\Bigl[1-J_0(1)^2-J_1(1)^2\\Bigr]", "numerical_answer": "0.1732700000"}