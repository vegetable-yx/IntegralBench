We begin with the integral

  I = ∫₀¹ arcsin(x) · arccos(x) dx.

Notice that since
  arcsin(x) + arccos(x) = π/2,
we can write
  arccos(x) = π/2 − arcsin(x).

Then
  I = ∫₀¹ arcsin(x) [π/2 − arcsin(x)] dx = (π/2)∫₀¹ arcsin(x) dx − ∫₀¹ [arcsin(x)]² dx.

A more straightforward method is to express everything in terms of u = arcsin(x). Since x = sin u and dx = cos u du, the limits change as follows:
  when x = 0, u = 0,
  when x = 1, u = π/2.

Noting that arccos(x) = π/2 − u, the integral becomes
  I = ∫₀^(π/2) u (π/2 − u) cos u du
    = (π/2)∫₀^(π/2) u cos u du − ∫₀^(π/2) u² cos u du.

We now compute the two integrals separately.

Step 1. Compute J₁ = ∫₀^(π/2) u cos u du.
• Let v = u and dB = cos u du. Then dv = du and B = sin u.
• By integration by parts:
  J₁ = u sin u − ∫ sin u du = u sin u + cos u + C.
• Evaluating from 0 to π/2:
  J₁ = [(π/2)·sin(π/2) + cos(π/2)] − [0·sin(0) + cos 0]
    = [(π/2)·1 + 0] − [0 + 1] = π/2 − 1.

Step 2. Compute J₂ = ∫₀^(π/2) u² cos u du.
• Again use integration by parts:
  Let A = u², dB = cos u du, then dA = 2u du and B = sin u.
• So,
  J₂ = u² sin u − ∫ 2u sin u du.
• Now, compute K = ∫ u sin u du.
  Let C = u and dF = sin u du, then dC = du and F = −cos u.
  Thus, K = −u cos u + ∫ cos u du = −u cos u + sin u.
• It follows that
  ∫ 2u sin u du = 2K = −2u cos u + 2 sin u.
• Thus,
  J₂ = u² sin u − (−2u cos u + 2 sin u) = u² sin u + 2u cos u − 2 sin u.
• Evaluating from 0 to π/2:
  At u = π/2: 
   u² sin u = (π/2)² · 1 = π²/4,
   2u cos u = 2·(π/2)·0 = 0,
   2 sin u = 2·1 = 2.
  At u = 0:
   All terms are 0.
  Thus, J₂ = (π²/4 − 2) − 0 = π²/4 − 2.

Returning to the original decomposition:
  I = (π/2) J₁ − J₂
    = (π/2)(π/2 − 1) − (π²/4 − 2)
    = (π²/4 − π/2) − (π²/4 − 2)
    = −π/2 + 2
    = 2 − π/2.

Finally, a numerical approximation:
  π/2 ≈ 1.5707963268,
  so I ≈ 2 − 1.5707963268 = 0.4292036732.

{"answer": "2 - \\frac{\\pi}{2}", "numerical_answer": "0.4292036732"}