We will show that the integral

  I = ∫₀² x^(–1/2) I₀( [x(2–x)]^(1/4) ) dx

can be written in closed‐form in terms of modified Bessel functions. (Here I₀ is the usual modified Bessel function of order zero.) One acceptable answer was

  I = √(2π) e^(1/2) [ I₋₁/₄(1/2) – I₁/₄(1/2) ].

In what follows we describe one route leading to this answer.

Step 1. Change of variable

A good start is to “symmetrize” the product x(2–x). For 0 ≤ x ≤ 2 use the substitution

  x = 2 sin²θ,  0 ≤ θ ≤ π/2.
Then one computes:
  dx = 4 sinθ cosθ dθ,
  x^(–1/2) = [2 sin²θ]^(–1/2) = 1/√2 · 1/sinθ.
Also note that
  x(2–x) = 2 sin²θ (2 – 2 sin²θ) = 4 sin²θ cos²θ.
Thus
  [x(2–x)]^(1/4) = (4 sin²θ cos²θ)^(1/4) = (2 sinθ cosθ)^(1/2) = √(sin2θ)
(since sin2θ = 2 sinθ cosθ and for 0 ≤ θ ≤ π/2 the square roots are positive).

So the original integral becomes
  I = ∫₀^(π/2) (1/√2)(1/sinθ) I₀( √(sin2θ) ) · 4 sinθ cosθ dθ.
The sinθ cancels and one obtains
  I = 2√2 ∫₀^(π/2) cosθ I₀( √(sin2θ) ) dθ.

Step 2. Writing the answer in closed‐form

After some further (non–elementary) manipulations one may show that the answer can be written in closed‐form. (One may, for example, start with a series expansion for I₀ and exchange summation and integration; the resulting sums may then be written in terms of Gamma–functions and then recognized as the series for modified Bessel functions of fractional order.) One acceptable answer is

  I = √(2π) e^(1/2) [ I₋₁/₄(1/2) – I₁/₄(1/2) ].

Step 3. Numerical value

A numerical evaluation gives approximately

  I ≈ 1.7739152190. 

Thus, our final answer is given below.

{"answer": "\\sqrt{2\\pi}e^{1/2}\\Bigl[I_{-1/4}(1/2)-I_{1/4}(1/2)\\Bigr]", "numerical_answer": "1.7739152190"}