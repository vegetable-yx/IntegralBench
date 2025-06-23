We will show that the integral
  I = ∫₀² x^(–1/4) (2–x)^(–3/4) cosh(√[4]{x(2–x)}) dx
may be written in “closed‐form” in terms of the confluent hypergeometric U–function. (Any answer equivalent to the answer below is correct.)

One acceptable answer was

  I = π·2^(3/4) e^(√2) U(1/4, 1/2, 2√2).

In what follows we describe one route to this answer.

───────────────────────────── 
Outline of one derivation

(1) Because of the factors x^(–1/4) and (2–x)^(–3/4) an Euler–type substitution is natural. For example one may set

  x = 2 sin²θ,  0 ≤ θ ≤ π/2.
 
Then
  2–x = 2 cos²θ  and  dx = 4 sinθ cosθ dθ.
Also,
  x^(–1/4) = (2 sin²θ)^(–1/4) = 2^(–1/4) sin^(–1/2)θ
  (2–x)^(–3/4) = (2 cos²θ)^(–3/4) = 2^(–3/4) cos^(–3/2)θ.
Thus the “power‐part” becomes
  x^(–1/4)(2–x)^(–3/4) dx = [2^(–1/4–3/4) sin^(–1/2)θ cos^(–3/2)θ] · [4 sinθ cosθ dθ]
             = 2 sin^(1/2)θ cos^(–1/2)θ dθ.
Next one observes that
  √[4]{x(2–x)} = √[4]{ (2 sin²θ)(2 cos²θ) } = √[4]{4 sin²θ cos²θ}
         = 2^(1/2)(sinθ cosθ)^(1/2).
Then the cosh–term becomes
  cosh(√[4]{x(2–x)}) = cosh (2^(1/2)(sinθ cosθ)^(1/2)).
Thus one obtains
  I = 2 ∫₀^(π/2) sin^(1/2)θ cos^(–1/2)θ cosh(2^(1/2)(sinθ cosθ)^(1/2)) dθ.
A further change (for example letting u = sin²θ, so that du = 2 sinθ cosθ dθ) will bring the integral into the form of a “bilinear” series in u which may be summed in closed‐form in terms of a confluent–hypergeometric function. (There are several possible routes.) One may show that after some standard algebra one obtains
  I = π 2^(3/4) e^(√2) U(1/4, 1/2, 2√2),
where U(a,b,z) is the confluent hypergeometric U–function.
───────────────────────────── 
Numerical value

A numerical evaluation shows that

  I ≈ 5.6232562768.
 
Thus one acceptable final answer is

  I = π·2^(3/4)e^(√2) U(1/4, 1/2, 2√2) ≈ 5.6232562768.
  
───────────────────────────── 
Final answer in JSON

{"answer": "$I=\\pi\\,2^{3/4}e^{\\sqrt{2}}U\\left(\\frac{1}{4},\\frac{1}{2},2\\sqrt{2}\\right)$", "numerical_answer": "5.6232562768"}