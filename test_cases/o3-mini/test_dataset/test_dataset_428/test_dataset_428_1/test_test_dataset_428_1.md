The floor function, ⌊x⌋, is constant between integers and jumps by 1 at every integer. In a Riemann‐Stieltjes integral of the form

  ∫ₐᵇ f(x) d⌊x⌋

the only contributions come from the discontinuities of ⌊x⌋ in the interval (a, b] (assuming the usual convention that takes the right-hand jumps). In our case, the integration interval is [0, 3] and the points of discontinuity (jump points) in (0, 3] are x = 1, 2, 3.

At each such point t, the integration contributes f(t)·Δ⌊x⌋|ₓ=t, where Δ⌊x⌋|ₓ=t = ⌊t⌋ − ⌊t⁻⌋ = 1.

Thus, the integral becomes:
  ∫₀³ (x² + 1) d⌊x⌋ = (1² + 1) + (2² + 1) + (3² + 1).

Calculating each term:
  For x = 1: 1² + 1 = 1 + 1 = 2.
  For x = 2: 2² + 1 = 4 + 1 = 5.
  For x = 3: 3² + 1 = 9 + 1 = 10.

Adding these, we obtain:
  2 + 5 + 10 = 17.

The exact answer is 17.

For the numerical approximation rounded to 10 decimal places, we have:
  17.0000000000

{"answer": "17", "numerical_answer": "17.0000000000"}