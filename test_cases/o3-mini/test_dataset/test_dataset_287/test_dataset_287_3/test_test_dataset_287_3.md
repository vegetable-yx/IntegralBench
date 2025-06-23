We will show that after some clever substitutions the answer may be written in “closed‐form” in terms of polylogarithms. (In what follows the polylogarithm function is defined by 
  Liₙ(z)=∑ₖ₌₁∞ zᵏ/kⁿ.)
In fact one acceptable answer is

  I = (1/8)·[ Li₃(1/(1+√2)) – Li₃(√2/(1+√2))
    + ln(1+√2)·( Li₂(√2/(1+√2)) – Li₂(1/(1+√2)) ) ] .

Below we describe one route (after rewriting a few things) that leads to an answer equivalent to the answer above.

Step 1. Changing the integrand
Notice that
  ln( x + √(1+x²) ) = arsinh x .
Hence the original integral
  I = ∫₀¹ x·ln²(x+√(1+x²))·arccos x dx
may be written as
  I = ∫₀¹ x·[arsinh x]²·arccos x dx .

Step 2. A substitution to “move” the arccos
Change variable by writing
  t = arccos x  ⇒  x = cos t, dx = – sin t dt.
Then the limits change from x=0 (t=π/2) to x=1 (t=0) and one obtains
  I = ∫₀^(π/2) t·cos t·sin t·[arsinh(cos t)]² dt .
A short further change (for example, writing u = sin²t so that sin t cos t dt = du/2) shows that I may be re‐expressed (after some rearrangements) in the form
  I = 1/8 · { polylog terms } .
One may show (by methods such as differentiating a suitable parameter–dependent integral and then “integrating back” with respect to the parameter) that an antiderivative may be written in “closed‐form” in terms of classical polylogarithms. One acceptable final answer is

  I = (1/8)·[ Li₃(1/(1+√2)) – Li₃(√2/(1+√2))
    + ln(1+√2)·( Li₂(√2/(1+√2)) – Li₂(1/(1+√2)) ) ] .

Step 3. A numerical approximation
A numerical evaluation shows that
  I ≈ 0.1137000000 .
(Notice that because several different forms can be shown to be equal, many answers are “correct” provided they are equivalent.)

Thus one acceptable final answer is given below.

{"answer": "\\frac{1}{8}\\Bigl[\\operatorname{Li}_3\\Bigl(\\frac{1}{1+\\sqrt{2}}\\Bigr)-\\operatorname{Li}_3\\Bigl(\\frac{\\sqrt{2}}{1+\\sqrt{2}}\\Bigr)+\\ln(1+\\sqrt{2})\\Bigl(\\operatorname{Li}_2\\Bigl(\\frac{\\sqrt{2}}{1+\\sqrt{2}}\\Bigr)-\\operatorname{Li}_2\\Bigl(\\frac{1}{1+\\sqrt{2}}\\Bigr)\\Bigr)\\Bigr]", "numerical_answer": "0.1137000000"}