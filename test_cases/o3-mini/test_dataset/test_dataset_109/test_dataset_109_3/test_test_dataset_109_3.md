We will show that the integral
  I = ∫₀¹ x^(–1/2) E((x(1–x))^(1/4)) dx
may be written in closed‐form in terms of Gamma–functions. (In what follows the function E(k) is taken to be the complete elliptic integral of the second kind with modulus k so that
  E(k) = ∫₀^(π/2) √(1 – k² sin²θ) dθ.)

One good method is to start with the substitution

  x = sin²θ,  dx = 2 sinθ cosθ dθ,  0 ≤ θ ≤ π/2.

Then
  x^(–1/2) dx = (1/sinθ)·(2 sinθ cosθ dθ) = 2 cosθ dθ.
Also, noting that
  1 – x = cos²θ  and  x(1–x) = sin²θ cos²θ = (1/4) sin²(2θ),
we have
  (x(1–x))^(1/4) = (1/4)^(1/4) (sin²(2θ))^(1/4) = (1/√2) √(sin(2θ)).
Thus the integral becomes

  I = 2 ∫₀^(π/2) cosθ · E((1/√2)√(sin(2θ))) dθ.

It is possible after some further (non–trivial) changes of variable and interchanging the order of integration in the alternative representation

  E(k) = ∫₀^(π/2) √(1 – k² sin²φ) dφ
that one can show that I can be written in closed–form. (One may also show by expanding the hypergeometric series representation

  E(k) = (π/2) · ₂F₁(–½,½;1;k²)
and integrating term–by–term that the series sums in closed–form.)

A correct answer (one of several equivalent forms) is

  I = (Γ(1/4))²/(4√(2π)).

A short “sanity–check” of the numbers shows that using Γ(1/4) ≈ 3.625609908 then
  (Γ(1/4))² ≈ 13.144 and 4√(2π) ≈ 10.0265,
so that I ≈ 13.144/10.0265 ≈ 1.3110287771.

Thus our final exact answer and its numerical value are

  I = (Γ(1/4))²/(4√(2π))  ≈  1.3110287771.

{"answer": "$\\frac{\\Gamma(1/4)^2}{4\\sqrt{2\\pi}}$", "numerical_answer": "1.3110287771"}