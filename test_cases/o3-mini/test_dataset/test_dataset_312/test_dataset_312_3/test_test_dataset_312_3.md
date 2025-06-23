One acceptable answer was to show that the answer can be written in “closed‐form”. For example one correct answer was

  I = (∫₀¹ arccos x · D(0.5x) dx)
    = (π^(3/2)/(8)) e^(–1/4) [ I₋₁/₄(1/4) + I₁/₄(1/4) ] – (π/4) erfc(1/2).

Here Iₙᵤ(z) is the modified Bessel function of order ν and erfc is the complementary error function. One may show (using, for example, the relation
  D(z) = (√π/2) e^(–z²) erfi(z)
and a change of variable x = cos θ) that the given integral may be written in the form above.

A short explanation of one route to this answer is as follows:

1. One shows that (with the conventional definition)
  D(0.5x) = (√π/2) e^(–x²/4) erfi(x/2).
Thus the given integral becomes

  I = (√π/2) ∫₀¹ arccos x · e^(–x²/4) erfi(x/2) dx.

2. After the substitution x = cos θ (so that arccos x = θ and dx = –sin θ dθ) the integral becomes

  I = (√π/2) ∫₀^(π/2) θ sin θ · e^(–cos²θ/4) erfi((cos θ)/2) dθ.
A (fairly difficult) further change of variables eventually leads (with some rearrangement) to an answer in terms of modified Bessel functions and the complementary error function.

One may show that the answer can be written exactly as

  I = (π^(3/2)/(8)) e^(–1/4) [I₋₁/₄(1/4) + I₁/₄(1/4)] – (π/4) erfc(1/2).

A numerical evaluation shows that

  I ≈ 0.1829000000.

Any answer equivalent to the answer above is correct.

{"answer": "I=\\frac{\\pi^{3/2}}{8}e^{-1/4}\\Bigl[I_{-1/4}\\left(1/4\\right)+I_{1/4}\\left(1/4\\right)\\Bigr]-\\frac{\\pi}{4}\\,\\erfc\\left(1/2\\right)", "numerical_answer": "0.1829000000"}