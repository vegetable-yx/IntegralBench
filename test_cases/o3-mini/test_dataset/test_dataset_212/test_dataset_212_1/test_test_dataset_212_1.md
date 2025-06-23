We begin with the integral

  I = ∫₀² x^(1/2) (2 – x)^(1/2) cos(√(x(2 – x))) dx.

Step 1. Change of Variable

Notice that
  x^(1/2)(2 – x)^(1/2) = √[x(2 – x)].
Thus the integrand becomes
  √(x(2 – x)) cos(√(x(2 – x))).
Now, let
  u = x – 1.
Then x = u + 1 and when x = 0, u = –1, and when x = 2, u = 1. Also observe that
  x(2 – x) = (u + 1)(2 – (u + 1)) = (u + 1)(1 – u) = 1 – u².
Thus the integral now reads
  I = ∫₋₁¹ √(1 – u²) cos(√(1 – u²)) du.

Step 2. Symmetry and a New Substitution

Since √(1 – u²) and cos(√(1 – u²)) are even functions, the integrand is even. Hence:
  I = 2 ∫₀¹ √(1 – u²) cos(√(1 – u²)) du.
A more convenient change is to set
  u = cosθ.
Then, note that
  du = –sinθ dθ  and  √(1 – u²) = sinθ.
When u goes from 0 to 1, the corresponding θ-values are:
  for u = 1: θ = 0,  for u = 0: θ = π/2.
Because u originally went from 0 to 1 (and we already doubled the integral), however it turns out to be even more natural to reparameterize the entire u–integral by writing it from –1 to 1. In fact, doing the substitution u = cosθ for the entire u–integral (u from –1 to 1) gives:
  when u = –1, cosθ = –1 so θ = π,
  when u = 1, cosθ = 1 so θ = 0.
Then
  I = ∫₍θ=π₎⁰ sinθ cos(sinθ) (–sinθ dθ) = ∫₀π sin²θ cos(sinθ) dθ.

Step 3. Expressing the Integral in Terms of Bessel Functions

Write sin²θ = (1 – cos2θ)/2, so that
  I = ½ [∫₀π cos(sinθ)dθ – ∫₀π cos(sinθ) cos2θ dθ].

There is a standard result (which one may verify using the Fourier–Bessel expansion) stating that for any real number z,
  ∫₀π cos(z sinθ)dθ = π J₀(z)
and, for even integers n,
  ∫₀π cos(z sinθ) cos(nθ)dθ = π Jₙ(z).
In our case z = 1 and n = 2. Hence,
  ∫₀π cos(sinθ)dθ = π J₀(1)
  ∫₀π cos(sinθ) cos2θ dθ = π J₂(1).

Thus the integral becomes
  I = ½ [π J₀(1) – π J₂(1)] = (π/2)[J₀(1) – J₂(1)].

Step 4. Numerical Approximation

Using standard numerical values for the Bessel functions:
  J₀(1) ≈ 0.7651976866  and  J₂(1) ≈ 0.1149088680,
we have
  I ≈ (π/2) (0.7651976866 – 0.1149088680)
     = (π/2) (0.6502888186)
     ≈ 1.5707963268 × 0.6502888186
     ≈ 1.0210176120.

Thus, our final answer is

  I = (π/2)[J₀(1) – J₂(1)]      and  I ≈ 1.0210176120.

{"answer": "\\frac{\\pi}{2}\\left[J_0(1)-J_2(1)\\right]", "numerical_answer": "1.0210176120"}