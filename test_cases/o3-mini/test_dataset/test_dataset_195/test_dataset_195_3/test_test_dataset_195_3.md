We start with the integral

  I = ∫₀¹ arcsin(x) · arccos(x) dx.

Step 1. Use the identity
  arcsin(x) + arccos(x) = π/2  (for all x in [0, 1])
to rewrite the product:
  arccos(x) = π/2 − arcsin(x).

Thus, the integrand becomes:
  arcsin(x) · (π/2 − arcsin(x)) = (π/2) · arcsin(x) − [arcsin(x)]².

So the integral splits into two parts:
  I = (π/2) ∫₀¹ arcsin(x) dx − ∫₀¹ [arcsin(x)]² dx.

Step 2. Compute I₁ = ∫₀¹ arcsin(x) dx.

Make the substitution:
  u = arcsin(x) ⇒ x = sin u and dx = cos u du.
When x = 0, u = 0, and when x = 1, u = π/2.
This changes the integral to:
  I₁ = ∫₀^(π/2) u cos u du.

Integrate by parts:
  Let a = u ⇒ da = du,
  and db = cos u du ⇒ b = sin u.
Then,
  ∫ u cos u du = u sin u − ∫ sin u du = u sin u + cos u + C.
Evaluate from 0 to π/2:
  At u = π/2: (π/2)·1 + cos(π/2) = (π/2) + 0 = π/2.
  At u = 0: 0·0 + cos(0) = 1.
Thus,
  I₁ = (π/2 − 1).

Step 3. Compute I₂ = ∫₀¹ [arcsin(x)]² dx.

Again, use the substitution:
  u = arcsin(x) ⇒ dx = cos u du,
with limits from u = 0 to u = π/2. Then:
  I₂ = ∫₀^(π/2) u² cos u du.
Integrate by parts:
  Let A = u² ⇒ dA = 2u du,
  and dB = cos u du ⇒ B = sin u.
Then,
  ∫ u² cos u du = u² sin u − ∫ 2u sin u du.
Now, compute ∫ 2u sin u du:
  Let P = u ⇒ dP = du,
  and dQ = sin u du ⇒ Q = −cos u.
Thus,
  ∫ u sin u du = −u cos u + ∫ cos u du = −u cos u + sin u.
So,
  ∫ 2u sin u du = 2(−u cos u + sin u) = −2u cos u + 2 sin u.
Therefore,
  ∫ u² cos u du = u² sin u + 2u cos u − 2 sin u + C.
Now evaluate from 0 to π/2:
  At u = π/2:
   sin(π/2) = 1, cos(π/2) = 0,
   gives: (π/2)² · 1 + 2(π/2)·0 − 2·1 = (π²/4) − 2.
  At u = 0:
   sin 0 = 0, cos 0 = 1,
   gives: 0 + 0 − 0 = 0.
Thus,
  I₂ = (π²/4) − 2.

Step 4. Combine the results:
  I = (π/2)·I₁ − I₂
    = (π/2)(π/2 − 1) − [(π²/4) − 2]
    = (π²/4 − π/2) − π²/4 + 2
    = 2 − (π/2).

We can write this as:
  I = (4 − π)/2.

Step 5. Numerical Approximation

Using π ≈ 3.1415926536,
  I ≈ (4 − 3.1415926536)/2 ≈ 0.8584073464/2 ≈ 0.4292036732.

Thus, the exact answer is (4 − π)/2 and the numerical approximation is 0.4292036732.

{"answer": "\\frac{4-\\pi}{2}", "numerical_answer": "0.4292036732"}