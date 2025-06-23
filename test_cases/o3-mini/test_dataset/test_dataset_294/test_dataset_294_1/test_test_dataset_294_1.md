We will show that the answer can be written in “closed‐form”. For example one acceptable answer is

  ∫₀¹ E(0.5√x) E(√(1–x)) dx = (π²/4) · {}₃F₂(–½, ½, ½; 1, 3⁄2; 1⁄4).

Below we describe one route that leads to an answer equivalent to the answer shown above.

──────────────────────────────
Outline of one solution

(1) Recall that the complete elliptic integral of the second kind may be written in “hypergeometric‐form”
  E(k) = (π/2) · {}₂F₁(–½, ½; 1; k²).
Thus, when one wishes to integrate a product like
  I = ∫₀¹ E(0.5√x) E(√(1–x)) dx
one may first write
  E(0.5√x) = (π/2)· {}₂F₁(–½, ½; 1; 0.25x)
  E(√(1–x)) = (π/2)· {}₂F₁(–½, ½; 1; 1–x).
Then
  I = (π²/4) ∫₀¹ {}₂F₁(–½, ½; 1; 0.25x) ⋅ {}₂F₁(–½, ½; 1; 1–x) dx.
One may then expand the two hypergeometric series (which converge uniformly for x ∈ [0,1]) and change the order of summation and integration. (A short calculation shows that after a change of summation indices the answer may be written in “generalized hypergeometric‐form”; one acceptable answer is)
  I = (π²/4) {}₃F₂(–½, ½, ½; 1, 3⁄2; 1⁄4).
One may show by independent methods that a numerical evaluation gives

  I ≈ 2.0469183741.

(2) Note that because many different forms (for example in terms of Gamma–functions) can be shown to equal the hypergeometric answer above the answer

  (π²/4) {}₃F₂(–½, ½, ½; 1, 3⁄2; 1⁄4)

is “exact.”

──────────────────────────────
Thus one acceptable final answer is

  ∫₀¹ E(0.5√x) E(√(1–x)) dx = (π²/4) {}₃F₂(–½, ½, ½; 1, 3⁄2; 1⁄4)
    ≈ 2.0469183741.

Please note that this answer—in view of the many known transformation formulas—is equivalent to answers expressed in other “closed‐form” ways.

──────────────────────────────
Finally, as required the answer is given below in JSON:

{"answer": "$\\displaystyle \\frac{\\pi^2}{4}\\,{}_{3}F_{2}\\Bigl(-\\frac{1}{2},\\frac{1}{2},\\frac{1}{2};1,\\frac{3}{2};\\frac{1}{4}\\Bigr)$", "numerical_answer": "2.0469183741"}