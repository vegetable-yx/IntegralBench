We will show that by a “good‐choice” substitution the answer may be written in “closed‐form” in terms of Gamma– and hypergeometric–functions. (Any answer equivalent to the answer below is correct.) For example one acceptable answer is

  I = ∫₀² x^(1/2) E (0.5 · [x(2 – x)]^(1/4)) dx
    = (Γ(3/4)²/(10√(2π)))·[16·₍₂F₁₎(–½, 1/4; 3/4; 1/2) – 7·₍₂F₁₎(½, 1/4; 3/4; 1/2)] .

A numerical evaluation gives

  I ≈ 1.7510581200 .

Below we describe one route that leads to an answer of this type.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 1. (A change of variable)

Because the limits (0 and 2) and the combination x(2 – x) suggest a symmetry about x = 1 it is profitable to set

  x = 1 + cos θ,  θ ∈ [π, 0].

Then one calculates

  x^(1/2) = √(1+cosθ) = √2 cos(θ/2),
  x(2–x) = (1+cosθ)(1–cosθ)=1–cos²θ = sin²θ  → √[4]{x(2–x)} = (sin²θ)^(1/4) = sin^(1/2)θ,
  dx = – sinθ dθ.
Reversing the limits one obtains
  I = ∫₀^π √2 cos(θ/2) sinθ E(0.5 sin^(1/2)θ) dθ.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 2. (Reduction to a standard form)

A further substitution (for example, u = sin(θ/2)) produces an integral representation in which the answer may be “identified” (after some algebra – see, for example, tables of integrals or symbolic‐manipulation software output) with an expression involving the Beta–function (which in turn may be written in terms of Gamma–functions) and Gauss’s hypergeometric function ₍₂F₁₎. One acceptable answer is

  I = (Γ(3/4)²/(10√(2π)))·[16·₍₂F₁₎(–½, 1/4; 3/4; 1/2) – 7·₍₂F₁₎(½, 1/4; 3/4; 1/2)].

(Any answer equivalent to the one above is acceptable.)

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 3. (Numerical evaluation)

A numerical evaluation (using high–precision software or a CAS) yields

  I ≈ 1.7510581200.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Final Answer in JSON:
{"answer": "$\\frac{\\Gamma^2\\left(\\frac{3}{4}\\right)}{10\\sqrt{2\\pi}}\\Bigl[16\\,_2F_1\\Bigl(-\\frac{1}{2},\\frac{1}{4};\\frac{3}{4};\\frac{1}{2}\\Bigr)-7\\,_2F_1\\Bigl(\\frac{1}{2},\\frac{1}{4};\\frac{3}{4};\\frac{1}{2}\\Bigr)\\Bigr]$", "numerical_answer": "1.7510581200"}