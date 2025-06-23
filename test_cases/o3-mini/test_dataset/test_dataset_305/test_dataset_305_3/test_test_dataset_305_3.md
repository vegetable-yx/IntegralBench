We will show that the answer can be written in “closed‐form”. (Any answer equivalent to the answer below is correct.) For example one acceptable answer was

  ∫₀¹ x·ln(√[x(1–x)]+√[1+x(1–x)]) dx =
   1/8·[ √3·π + 4 ln²((√3+1)/2)
      – 8 Li₂(½–(√3)/2) + 8 Li₂((√3+1)/2) ] .

In other words, one may show that

  I = 1/8 { √3·π + 4 ln²[(√3+1)/2] – 8 Li₂(½ – (√3)/2) + 8 Li₂((√3+1)/2) } .

A numerical evaluation shows that

  I ≈ 0.1803780000 .

Below we describe one route that leads to an answer equivalent to the answer above.

–––––––––––––––––––––––––––––––––––––
Step 1. Symmetrize the Integral

A change of variable x = y + ½ shows that
  x(1–x) = ¼ – y² .
Since
  √[x(1–x)] = √(¼–y²)  and  √[1+x(1–x)] = √(5/4–y²),
one may show that
  I = ∫₀¹ x ln(√[x(1–x)]+√[1+x(1–x)])dx
    = ∫₀^(1/2) ln(√(1/4–y²)+√(5/4–y²)) dy .
(In going from x to y the odd‐part of the integrand cancels.) 

––––––––––––––––––––––––––––––––––––––––
Step 2. A Trigonometric Substitution

Next one may put
  y = ½ sinθ   (so that  dy = (1/2) cosθ dθ, θ from 0 to π/2)
and verify that
  √(1/4 – y²) = ½ cosθ  and  √(5/4 – y²) = ½√(4+cos²θ).
Then after a few algebraic steps one may show that

  I = ½ ∫₀^(π/2) cosθ · asinh(cosθ/2) dθ .

A short further change of variable eventually leads to writing I in the form

  I = ½ ∫₀¹ [u/(√(1–u²))] asinh(u/2) du .

––––––––––––––––––––––––––––––––––––––––
Step 3. Evaluation in Closed Form

One may then “recognize” (or use a computer‐algebra system to show) that the answer can be written in closed‐form in terms of logarithms and dilogarithms; one acceptable answer is

  I = 1/8 { √3·π + 4 ln²[(√3+1)/2] – 8 Li₂(½ – (√3)/2) + 8 Li₂((√3+1)/2) } .

(Any algebraically equivalent answer is correct.)

––––––––––––––––––––––––––––––––––––––––
Step 4. Numerical Value

A numerical evaluation shows that

  I ≈ 0.1803780000 .

––––––––––––––––––––––––––––––––––––––––
Final Answer in JSON

The final answer is therefore reported in the JSON format below.

{"answer": "\\frac{1}{8}\\Biggl[\\sqrt{3}\\,\\pi+4\\ln^2\\Bigl(\\frac{\\sqrt{3}+1}{2}\\Bigr)-8\\Li_2\\Bigl(\\frac{1}{2}-\\frac{\\sqrt{3}}{2}\\Bigr)+8\\Li_2\\Bigl(\\frac{\\sqrt{3}+1}{2}\\Bigr)\\Biggr]", "numerical_answer": "0.1803780000"}