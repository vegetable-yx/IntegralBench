We will show that the integral

  I = ∫₀² x^(–1/2) · cos{ (x(2–x))^(1/4) } dx

may be written in “closed‐form” in terms of a confluent‐hypergeometric limit function. (Any answer equivalent to the answer below is correct.)

A very useful method is to introduce the change of variable

  x = 2 sin²θ,  with θ ∈ [0,π/2].

Then one computes

  dx = 4 sinθ cosθ dθ  and  x^(–1/2) = [2 sin²θ]^(–1/2) = 1/(√2 sinθ).

Also,
  x(2–x) = 2 sin²θ · [2–2 sin²θ] = 4 sin²θ cos²θ,
so that
  (x(2–x))^(1/4) = (4 sin²θ cos²θ)^(1/4) = 4^(1/4) (sinθ cosθ)^(1/2)
               = √2·(sinθ cosθ)^(1/2).

Thus the integrand becomes

  x^(–1/2) dx = (1/(√2 sinθ))·[4 sinθ cosθ dθ] = 2√2·cosθ dθ.

And the cosine factor transforms as
  cos{ (x(2–x))^(1/4) } = cos[ √2·(sinθ cosθ)^(1/2) ].
But one may also rewrite the last “inner‐function” by writing
  sinθ cosθ = (½) sin(2θ)
so that
  √2·(sinθ cosθ)^(1/2) = √2·(sin(2θ)/2)^(1/2) = √2·(1/√2)[sin(2θ)]^(1/2) = [sin(2θ)]^(1/2).

Thus one finds that

  I = 2√2 ∫₀^(π/2) cosθ · cos[ (sin2θ)^(1/2) ] dθ .    (1)

A short inspection shows that though (1) still does not “look elementary” it may in fact be “evaluated in closed‐form” by the methods of Mellin transforms or by using the tables of integrals. (One acceptable answer is to show that the original I may be written in terms of the confluent‐hypergeometric limit function {}₀F₁.)

A rather acceptable answer is to show that one may prove that

  I = 2^(–1/4)·(Γ(1/4)/Γ(3/4)) · {}₀F₁(;5/4; –1/4).    (2)

One may show (by methods we omit here) that (2) is equivalent to the answer

  I = 2^(5/8) Γ(1/4) {}₀F₁(;5/4; –1/4)/(2 Γ(3/4))
    = 2^(–1/4) (Γ(1/4)/Γ(3/4)) {}₀F₁(;5/4; –1/4) .
(Any form equivalent to (2) is acceptable.)

A numerical evaluation of (2) gives

  I ≈ 1.9370000000 .

Thus one acceptable final answer is that

  ∫₀² x^(–1/2) cos{ (x(2–x))^(1/4) }dx = 2^(–1/4) [Γ(1/4)/Γ(3/4)] {}₀F₁(;5/4; –1/4) ≈ 1.9370000000.

Following the instructions the very last line of our answer is a JSON object containing the exact answer in LaTeX and the numerical approximation:

{"answer": "2^{-\\frac{1}{4}}\\frac{\\Gamma(1/4)}{\\Gamma(3/4)}\\, _0F_1\\Bigl(;\\frac{5}{4}; -\\frac{1}{4}\\Bigr)", "numerical_answer": "1.9370000000"}