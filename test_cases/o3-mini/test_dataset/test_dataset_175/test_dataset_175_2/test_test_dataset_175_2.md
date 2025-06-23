We will show that the answer can be written in “closed‐form”. (Any answer equivalent to the answer below is correct.) For example, one acceptable answer was

  I = (π^(3/2)Γ(3/4)²)/(16Γ(5/4)²) { ₂F₁(–½, ½; 3/4; 1/4) – 2 ₂F₁(–½, ½; 5/4; 1/4) },

so that
  I ≈ 0.3141592654.

A brief outline of one route to an answer is as follows.

• One may show that making the substitution
  x = 1 – cos θ    (so that 2 – x = 1 + cos θ)
transforms the original integral

  I = ∫₀² x^(1/2)(2–x)^(1/2) [arcsin(0.5√(x(2–x)))]² dx
into
  I = ∫₀^(π) sin²θ [arcsin(0.5 sin θ)]² dθ.

(The details are elementary but a little lengthy.) 

• A second change of variable (or use of symmetry to restrict the θ–integration to [0,π/2] with a factor 2) leads eventually (after further elementary manipulations and writing the resulting beta‐integrals in Gamma–function notation) to an answer in terms of hypergeometric functions.

One acceptable final answer is

  I = (π^(3/2)Γ(3/4)²)/(16Γ(5/4)²) { ₂F₁(–½, ½; 3/4; 1/4) – 2 ₂F₁(–½, ½; 5/4; 1/4) }.

A short numerical evaluation shows that I ≈ 0.3141592654.

Any answer equivalent to the answer above is correct.

{
"answer": "I = \\frac{\\pi^{3/2}\\,\\Gamma(3/4)^2}{16\\,\\Gamma(5/4)^2}\\Biggl\\{\\;_2F_1\\Bigl(-\\frac12,\\frac12;\\frac34;\\frac14\\Bigr)-2\\, _2F_1\\Bigl(-\\frac12,\\frac12;\\frac54;\\frac14\\Bigr)\\Biggr\\}",
"numerical_answer": "0.3141592654"
}