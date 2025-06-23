We start with the integral

  I = ∫₀¹ sin(cos⁻¹(x)) dx.

Let u = cos⁻¹(x), so that x = cos u. When x = 0, u = cos⁻¹(0) = π/2 and when x = 1, u = cos⁻¹(1) = 0.
Differentiate x = cos u to get dx = –sin u du.

Thus, the integral becomes

  I = ∫₍u=π/2₎^(u=0) sin(u) (–sin u du)
    = –∫₍π/2₎^(0) sin² u du
    = ∫₀^(π/2) sin² u du    (reversing the limits).

Using the half-angle identity sin² u = (1 – cos 2u)/2, we have

  I = ∫₀^(π/2) (1 – cos 2u)/2 du
    = 1/2 ∫₀^(π/2) du – 1/2 ∫₀^(π/2) cos 2u du.

Evaluating the first integral:

  ∫₀^(π/2) du = π/2.

For the second integral, perform a substitution:
Let v = 2u so that dv = 2 du or du = dv/2, and when u = 0, v = 0; when u = π/2, v = π. Then,
  ∫₀^(π/2) cos 2u du = ∫₀^(π) cos v (dv/2) = (1/2) ∫₀^(π) cos v dv.
But ∫₀^(π) cos v dv = sin v │₀^(π) = sin π – sin 0 = 0 – 0 = 0.

Thus, we obtain

  I = 1/2 (π/2) – 1/2 · 0 = π/4.

The numerical approximation is

  π/4 ≈ 0.7853981634.

{"answer": "\\frac{\\pi}{4}", "numerical_answer": "0.7853981634"}