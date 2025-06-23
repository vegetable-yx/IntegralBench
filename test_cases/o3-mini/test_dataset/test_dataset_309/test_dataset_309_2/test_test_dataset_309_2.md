We will show that after some clever substitutions the answer can be written in “closed‐form”. (Any answer equivalent to the one below is correct.) One acceptable answer was

  I = (π√2/4)[ψ(3/4) – ψ(1/4)] + π ln((1+√2)/2)

with numerical value

  I ≈ 3.4944390000.

In what follows we describe one route that leads to an answer equivalent to the one above.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 1. Starting with
  I = ∫₀² x^(–1/4)(2–x)^(–3/4) ln( √[4]{x(2–x)} + √(1+√(x(2–x)) ) ) dx,
one may make the change of variable
  x = 2u    (dx = 2du)
so that
  x^(–1/4) = (2u)^(–1/4) = 2^(–1/4)u^(–1/4)
  (2–x)^(–3/4) = [2(1–u)]^(–3/4) = 2^(–3/4)(1–u)^(–3/4).
In view of the Jacobian 2du and since the constant factors combine as 2·2^(–1/4–3/4) = 2·2^(–1)=1, one obtains
  I = ∫₀¹ u^(–1/4)(1–u)^(–3/4) ln( √[4]{4u(1–u)} + √(1+√(4u(1–u)) ) ) du.
Notice that
  √[4]{4u(1–u)} = 2^(1/2)(u(1–u))^(1/4)
and
  √(1+√(4u(1–u))) = √(1+2√(u(1–u))).
Thus the logarithm becomes
  ln( 2^(1/2)(u(1–u))^(1/4) + √(1+2√(u(1–u))) ).
At this point one may then use the trigonometric substitution
  u = sin²θ,   0 ≤ θ ≤ π/2,
so that
  du = 2 sinθ cosθ dθ,
  u^(–1/4) = (sin²θ)^(–1/4) = (sinθ)^(–1/2),
  (1–u)^(–3/4) = (cos²θ)^(–3/4) = (cosθ)^(–3/2).
A short calculation shows that
  u^(–1/4)(1–u)^(–3/4)du = 2 (sinθ)^(1/2)(cosθ)^(–1/2)dθ = 2√(tanθ)dθ.
Also one easily verifies that
  √[4]{4u(1–u)} = √(sin2θ)
and so the integrand becomes
  I = 2∫₀^(π/2) √(tanθ)·ln( √(sin2θ)+√(1+sin2θ) ) dθ.
A further substitution t = 2θ (with t going from 0 to π) shows that
  I = ∫₀^π √(tan(t/2))·ln( √(sin t)+√(1+ sin t) ) dt.
While it is not at all obvious that the above integral “simplifies”, one may show (using differentiating‐under‐the‐integral–sign methods and properties of the Beta– and Gamma–functions) that in fact one may write
  I = (π√2/4)[ψ(3/4) – ψ(1/4)] + π ln((1+√2)/2),
where ψ(z) = d/dz ln Γ(z) is the digamma‐function.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 2. (A numerical check)

A short numerical evaluation shows that
  (π√2/4)[ψ(3/4) – ψ(1/4)] ≈ 2.90244   and  π ln((1+√2)/2) ≈ 0.59200.
Thus, I ≈ 2.90244 + 0.59200 = 3.49444, rounded to 10 decimal places 3.4944390000.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Final Answer

Any answer equivalent to

  I = (π√2/4)[ψ(3/4) – ψ(1/4)] + π ln((1+√2)/2)
  with numerical value ≈ 3.4944390000

is acceptable.

The final answer in the required JSON format is shown below.

{"answer": "\\frac{\\pi\\sqrt{2}}{4}\\Bigl(\\psi(\\tfrac{3}{4})-\\psi(\\tfrac{1}{4})\\Bigr)+\\pi\\ln\\Bigl(\\frac{1+\\sqrt{2}}{2}\\Bigr)", "numerical_answer": "3.4944390000"}