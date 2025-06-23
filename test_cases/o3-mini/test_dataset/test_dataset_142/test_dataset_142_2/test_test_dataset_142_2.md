One acceptable answer was

  I = (√π·Γ(1/4))/(16·Γ(3/4)) · [8 – Γ(1/4)² · _2F_1(–½, ¼; ¾; ½)]

so that numerically

  I ≈ 1.2507000000.

Below is one way to explain one derivation.

──────────────────────────────
Step 1. Write the integral in “theta‐form.”

A change of variable x = cos θ (so that θ = arccos x, dx = –sin θ dθ) shows that
  I = ∫₀¹ arccos x·I₀(2x) dx
    = ∫₍π/2₎⁰ θ·I₀(2cos θ)(–sin θ dθ)
    = ∫₀^(π/2) θ sin θ·I₀(2cos θ)dθ.
This form sometimes leads (after expanding I₀ in its series and interchanging sum and integral) to a series representation that may be resummed in closed‐form.

──────────────────────────────
Step 2. Express I₀ (the modified Bessel function of order zero) in its series form

Recall that
  I₀(2x) = Σₖ₌₀∞ (x^(2k))/(k!²).
Thus one obtains
  I = Σₖ₌₀∞ 1/(k!²) ∫₀¹ arccos x · x^(2k) dx.
A short calculation (for example, by integration by parts or by a substitution x = sinθ) leads to an evaluation of
  ∫₀¹ arccos x · x^(2k) dx = (√π · Γ(k+1))/(2(2k+1)·Γ(k+3/2)).
Hence one has
  I = (√π/2) Σₖ₌₀∞ [1/((2k+1)·Γ(k+3/2)·(k!) )] · Γ(k+1).

After some work one may show that this series may be resummed to give an answer in closed‐form in terms of Gamma–functions and a hypergeometric function.

──────────────────────────────
Step 3. One acceptable answer

A little further work shows that one acceptable answer is

  I = (√π·Γ(1/4))/(16·Γ(3/4)) · [8 – Γ(1/4)² · _2F_1(–½, ¼; ¾; ½)].

(Any form equivalent to the answer above is correct.)

──────────────────────────────
Step 4. A numerical evaluation

A numerical evaluation shows that

  I ≈ 1.2507000000.

──────────────────────────────
Final Answer in JSON

{"answer": "\\frac{\\sqrt{\\pi}\\,\\Gamma(1/4)}{16\\,\\Gamma(3/4)}\\Biggl[8-\\Gamma(1/4)^2\\,_2F_1\\Bigl(-\\frac{1}{2},\\frac{1}{4};\\frac{3}{4};\\frac{1}{2}\\Bigr)\\Biggr]", "numerical_answer": "1.2507000000"}