We start with the integral

  I = ∫₀² H₃(√[x(2 – x)]) dx.

The Hermite polynomial of degree 3 is given by

  H₃(z) = 8z³ − 12z.

Thus the integral becomes

  I = ∫₀² [8 (√(x(2 – x)))³ – 12 √(x(2 – x))] dx
    = 8∫₀² (x(2 – x))^(3/2) dx − 12∫₀² (x(2 – x))^(1/2) dx.

Define

  I₁ = ∫₀² (x(2 – x))^(3/2) dx  and  I₂ = ∫₀² (x(2 – x))^(1/2) dx.

A useful substitution in both integrals is
  x = 1 + cosθ,
so that
  dx = – sinθ dθ
and the limits change as follows:
  when x = 0: 1 + cosθ = 0 ⇒ cosθ = –1 ⇒ θ = π,
  when x = 2: 1 + cosθ = 2 ⇒ cosθ = 1 ⇒ θ = 0.

Notice that
  x(2 – x) = (1 + cosθ)(1 – cosθ) = 1 – cos²θ = sin²θ.

Because sinθ is nonnegative for θ in [0, π], we have
  √(sin²θ) = sinθ.

Now, for I₂:

  I₂ = ∫₀² (x(2 – x))^(1/2) dx
    = ∫_{θ=π}^{0} sinθ (– sinθ dθ)
    = ∫_{θ=π}^{0} (– sin²θ dθ)
    = ∫₀^π sin²θ dθ.

A standard result is

  ∫₀^π sin²θ dθ = π/2.

Thus, I₂ = π/2.

Next, for I₁:

  I₁ = ∫₀² (x(2 – x))^(3/2) dx
    = ∫_{θ=π}^{0} (sin²θ)^(3/2)(– sinθ dθ)
    = ∫_{θ=π}^{0} sin³θ (– sinθ dθ)
    = ∫_{θ=π}^{0} (– sin⁴θ dθ)
    = ∫₀^π sin⁴θ dθ.

Using the power-reduction formula, we know that

  sin⁴θ = 3/8 − 1/2 cos2θ + 1/8 cos4θ.
Integrating over [0, π] the cosine terms vanish, so

  I₁ = ∫₀^π sin⁴θ dθ = (3/8)π.

Now return to the original integral:

  I = 8 I₁ − 12 I₂
    = 8 (3π/8) − 12 (π/2)
    = 3π − 6π
    = −3π.

Thus the exact answer is −3π.

The numerical approximation is
  −3π ≈ −9.4247779608  (rounded to 10 decimal places).

{"answer": "-3\\pi", "numerical_answer": "-9.4247779608"}