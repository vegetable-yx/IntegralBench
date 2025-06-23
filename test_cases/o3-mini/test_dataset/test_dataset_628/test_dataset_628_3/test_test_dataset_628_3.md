We wish to evaluate

  I = ∫₀^(1/2) ln(√(1 – x) – √x) dx.

A very useful manipulation is to write the expression inside the logarithm in an alternative form. Note that

  √(1 – x) – √x = ( (√(1 – x) – √x)(√(1 – x) + √x) )⁄(√(1 – x) + √x)
                = (1 – x – x)/(√(1 – x) + √x)
                = (1 – 2x)/(√(1 – x) + √x).

Thus, we may write
  ln(√(1 – x) – √x) = ln(1 – 2x) – ln(√(1 – x) + √x).

That is, the integral splits as

  I = ∫₀^(1/2) ln(1 – 2x) dx – ∫₀^(1/2) ln(√(1 – x) + √x) dx.
    = I₁ – I₂.

Step 1. Evaluate I₁:

Let u = 1 – 2x so that du = –2 dx. When x = 0, u = 1; when x = 1/2, u = 0. Then

  I₁ = ∫₀^(1/2) ln(1 – 2x) dx = ∫₁⁰ ln u (–du/2) = (1/2) ∫₀¹ ln u du.
We know that
  ∫₀¹ ln u du = –1.
Thus,
  I₁ = –1/2.

Step 2. Evaluate I₂:

We have
  I₂ = ∫₀^(1/2) ln(√(1 – x) + √x) dx.
Make the substitution x = sin²θ. Then
  √x = sinθ,  √(1 – x) = cosθ,
and
  √(1 – x) + √x = cosθ + sinθ.
Also, dx = 2 sinθ cosθ dθ = sin2θ dθ.

The limits change as follows: when x = 0, sin²θ = 0 so θ = 0; when x = 1/2, sin²θ = 1/2 so θ = π/4. Hence,
  I₂ = ∫₀^(π/4) ln(cosθ + sinθ) sin2θ dθ.

Now, use the identity
  cosθ + sinθ = √2 cos(θ – π/4),
so that
  ln(cosθ + sinθ) = ln(√2) + ln(cos(θ – π/4)) = (1/2) ln2 + ln(cos(θ – π/4)).

Thus,
  I₂ = (1/2 ln2) ∫₀^(π/4) sin2θ dθ + ∫₀^(π/4) sin2θ ln(cos(θ – π/4)) dθ.
We compute the first integral:
  ∫₀^(π/4) sin2θ dθ = [ –cos2θ/2 ]₀^(π/4) = (–cos(π/2) + cos0)/2 = (0 + 1)/2 = 1/2.
So the first term gives
  (1/2 ln2)·(1/2) = ln2/4.

For the second term, make the substitution
  u = θ – π/4  ⟹  dθ = du.
When θ = 0, u = –π/4; when θ = π/4, u = 0.
Also, note that
  sin2θ = sin[2(u + π/4)] = sin(2u + π/2) = cos2u,
using the identity sin(A + π/2) = cosA.
Thus, the second term becomes
  ∫₋(π/4)^(0) cos2u ln(cos u) du.
Since cosine is an even function, we may change the limits by setting v = –u:
  Let v = –u, then du = –dv, and when u = –π/4, v = π/4, and when u = 0, v = 0.
It follows that
  ∫₋(π/4)^(0) cos2u ln(cos u) du = ∫_(π/4)^(0) cos2(–v) ln(cos (–v)) (–dv)
                = ∫₀^(π/4) cos2v ln(cos v) dv.
Thus, we denote
  J = ∫₀^(π/4) cos2u ln(cos u) du.
So now,
  I₂ = ln2/4 + J.

We now evaluate J by integration by parts. Let
  w = ln(cos u)  ⟹  dw = –tan u du,
and
  dv = cos2u du  ⟹  v = ∫ cos2u du = sin2u/2.
Then,
  J = [w v]₀^(π/4) – ∫₀^(π/4) v dw
    = [ (sin2u/2) ln(cos u) ]₀^(π/4) – ∫₀^(π/4) (sin2u/2)(–tan u) du.
At u = π/4, note that sin(2·π/4) = sin(π/2) = 1 and cos(π/4) = √2/2 giving ln(√2/2) = –(1/2) ln2. At u = 0, sin0 = 0. Therefore, the boundary term is
  (1/2)(–(1/2) ln2) – 0 = –(ln2)/4.
The remaining integral is
  + (1/2) ∫₀^(π/4) sin2u tan u du.
But note:
  tan u = sin u/cos u  and  sin2u = 2 sin u cos u,
so their product is
  sin2u tan u = 2 sin u cos u · (sin u/cos u) = 2 sin²u.
Thus, the integral becomes
  (1/2) ∫₀^(π/4) 2 sin²u du = ∫₀^(π/4) sin²u du.
We recall that
  ∫ sin²u du = u/2 – sin2u/4.
Thus, over [0, π/4] we have
  ∫₀^(π/4) sin²u du = (π/4)/2 – (sin(π/2))/4 = π/8 – 1/4.
So we obtain
  J = –(ln2)/4 + (π/8 – 1/4).
Therefore,
  I₂ = ln2/4 + J = ln2/4 + (π/8 – 1/4 – ln2/4) = π/8 – 1/4.

Step 3. Put the pieces together:

We earlier had
  I = I₁ – I₂ = (–1/2) – (π/8 – 1/4) = –1/2 – π/8 + 1/4.
Combine the constants:
  –1/2 + 1/4 = –1/4,
so that
  I = –1/4 – π/8 = –(2/8 + π/8) = –(π + 2)/8.

Step 4. Numerical Approximation

We now approximate the value. With π ≈ 3.1415926536, we have
  π + 2 ≈ 3.1415926536 + 2 = 5.1415926536,
so
  I ≈ –5.1415926536/8 ≈ –0.6426990817.

Thus, the exact answer is
  I = –(π + 2)/8,
and the numerical approximation is –0.6426990817.

{"answer": "$-\\frac{\\pi+2}{8}$", "numerical_answer": "-0.6426990817"}