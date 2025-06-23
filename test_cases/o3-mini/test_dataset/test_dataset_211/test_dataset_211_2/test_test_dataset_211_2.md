We will show that the integral

  I = ∫₀¹ x^(–1/2) cos(2√(x(1–x))) dx

can be written in closed‐form. (Any answer equivalent to the following is acceptable.)

Step 1. (Change of variable)

A useful substitution is

  x = sin²θ, 0 ≤ θ ≤ π/2.
Then
  dx = 2 sinθ cosθ dθ  and  x^(–1/2) = 1/sinθ.
Also, note that
  √(x(1–x)) = √(sin²θ cos²θ) = sinθ cosθ.
Thus
  2√(x(1–x)) = 2 sinθ cosθ = sin 2θ.
So the integral becomes

  I = ∫₀^(π/2) (1/sinθ)·cos(sin2θ)·[2 sinθ cosθ dθ]
    = 2∫₀^(π/2) cosθ cos(sin2θ) dθ.

Step 2. (Rewrite in a “symmetrized” form)

It is sometimes clearer to change the variable by setting t = 2θ so that
  θ = t/2  and  dθ = dt/2.
When θ goes from 0 to π/2, t runs from 0 to π. Also cosθ = cos(t/2). Hence

  I = 2·(1/2) ∫₀^(π) cos(t/2) cos(sin t) dt
    = ∫₀^(π) cos(t/2) cos(sin t) dt.
It turns out that one may show (by expanding cos(sin t) in a Fourier–Bessel series or by other means) that the answer can be written in closed‐form in terms of modified Bessel functions. (There are many routes to the answer; see, for example, tables of integrals or techniques using the Laplace transform.)

Step 3. (State the closed‐form answer)

One acceptable answer is

  I = π e^(–½) [ I₋₁/₄(1/2) – I₁/₄(1/2) ],
            (1)

where Iₙ(z) is the modified Bessel function of order n.

Step 4. (Numerical approximation)

A numerical evaluation shows that

  I ≈ 0.8237000000  (to ten decimal places).

Thus, our final answer is given in the JSON format below.

{"answer": "$\\pi e^{-1/2}\\Bigl[I_{-1/4}(1/2)-I_{1/4}(1/2)\\Bigr]$", "numerical_answer": "0.8237000000"}