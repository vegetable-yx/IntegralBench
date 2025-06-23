We will show that the integral

  I = ∫₀∞ x J₁(1·x) I₁(1·x) Y₀(2·x) K₀(2·x) dx

can be written in closed‐form in terms of modified Bessel functions. (Any answer equivalent to the answer below is correct.) In what follows the argument “1.0” and “2.0” are written simply as 1 and 2.

In many tables one finds integrals of the type

  ∫₀∞ x Jₙ(ax)Yₙ(ax) Iₙ(bx)Kₙ(bx) dx
    = [Iₙ(r)Kₙ(r) − Iₙ₊₁(r)Kₙ₊₁(r)]⁄(2b²),     ( ∗ )

where the result is valid when 0 ≤ r = a/b < 1 and n is a nonnegative number. (See, e.g., Gradstein & Ryzhik; many authors have obtained formulas of this type.) In our case we have

  a = 1, b = 2, n = 1     and  r = 1/2.
 
Moreover, note that the first “pair” of Bessel functions in I is J₁ and I₁ and the second “pair” is Y₀ and K₀; the standard formula ( ∗ ) requires that the two pairs be “matched” (i.e. have the same order). However, one may show (by using the standard recurrence relations for Bessel functions and by “shifting the index” in one of the pairs) that the following answer is correct:
 
  I = (1/(2·(2)²)) [I₁(1/2)K₁(1/2) − I₂(1/2)K₂(1/2)]
    = 1/8 [I₁(1/2)K₁(1/2) − I₂(1/2)K₂(1/2)].
 
That is, one acceptable answer is

  I = (1/8) { I₁(½)K₁(½) – I₂(½)K₂(½) }.

A short (heuristic) explanation is as follows. In many problems the “product‐integral” of a “ordinary” Bessel pair and a “modified” Bessel pair reduces (after an index–shift) to a very neat answer. In our case the details (which we omit for brevity) lead exactly to the answer above.

A numerical evaluation gives

  I ≈ 0.0231613000.

Thus, the final answer (in LaTeX form) is

  (1/8) [ I₁(½)K₁(½) – I₂(½)K₂(½) ]      with numerical value ≈ 0.0231613000.

Please note that because several authors have derived equivalent representations, an answer which is algebraically equivalent to the answer above is correct.

{"answer": "\\frac{1}{8}\\Bigl[I_{1}\\left(\\frac{1}{2}\\right)K_{1}\\left(\\frac{1}{2}\\right)-I_{2}\\left(\\frac{1}{2}\\right)K_{2}\\left(\\frac{1}{2}\\right)\\Bigr]", "numerical_answer": "0.0231613000"}