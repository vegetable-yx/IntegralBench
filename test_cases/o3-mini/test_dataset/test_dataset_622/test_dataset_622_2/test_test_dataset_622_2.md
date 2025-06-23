We wish to evaluate

  I = ∫₀^(π/2) [cos²x (1 + cos x)]⁄[ (1 + cos x + sin x)² ] dx.

It turns out that a smart change of variable makes the answer obvious. One successful method is to use the Weierstrass (t‑substitution) transformation. In outline, one shows that letting

  u = tan(x/2)

transforms the trigonometric functions as follows:
  sin x = (2u)/(1 + u²),
  cos x = (1 – u²)/(1 + u²),
  dx = 2 du/(1 + u²).

Step 1. Express the integrand in terms of u.

We have:
  cos²x = ((1 – u²)/(1 + u²))² and 1 + cos x = 1 + (1 – u²)/(1 + u²)
           = ( (1 + u²) + (1 – u²))/(1 + u²) = 2/(1 + u²).

Thus, the numerator becomes

  cos²x (1+ cos x) = ((1 – u²)²/(1+u²)²) · (2/(1+u²))
               = 2 (1 – u²)²/(1+u²)³.

Next, the denominator:
  1 + cos x + sin x = 1 + (1 – u²)/(1 + u²) + (2u)/(1 + u²)
       = [ (1+u²) + (1 – u²) + 2u ]/(1+u²)
       = [2 + 2u]/(1+u²) = 2(1+u)/(1+u²).

Thus, (1+cos x+ sin x)² = 4(1+u)²/(1+u²)².

Also, dx = 2 du/(1+u²).

Collecting everything we have:

  I = ∫ (from x=0 to π/2) {2(1 – u²)²/(1+u²)³} ÷ {4(1+u)²/(1+u²)²} · [2 du/(1+u²)].

It is a good idea to combine the factors step‐by‐step. Write the quotient first:

  [2(1 – u²)²/(1+u²)³] ÷ [4(1+u)²/(1+u²)²] = [2(1–u²)²/(1+u²)³] · [(1+u²)²/(4(1+u)²)]
            = (2(1–u²)²)/(4(1+u)²(1+u²))
            = (1 – u²)²/(2(1+u)² (1+u²)).

Now include the dx factor:
  dx = 2 du/(1+u²) so multiplying gives
  (1 – u²)²/(2(1+u)² (1+u²)) · [2/(1+u²)] = (1 – u²)²/[(1+u)² (1+u²)²].

Thus, in u–terms the integral becomes

  I = ∫ (u from ? to ?) (1 – u²)²/[(1+u)² (1+u²)²] du.

Next, we must adjust the limits. When x = 0, u = tan(0/2) = 0; when x=π/2, u = tan(π/4) = 1.

Step 2. Simplify the integrand.

Notice that
  (1 – u²)² = [ (1 – u)(1+ u)]² = (1–u)² (1+u)².
Thus the (1+u)² cancels with the same factor in the denominator, and we get

  I = ∫₀¹ (1 – u)²/(1+u²)² du.

Step 3. Split the integrand into simpler parts.

Write (1 – u)² = 1 – 2u + u² so that

  I = ∫₀¹ [1/(1+u²)² – 2u/(1+u²)² + u²/(1+u²)²] du.
Define the three integrals as follows:
  I₁ = ∫₀¹ 1/(1+u²)² du,
  I₂ = ∫₀¹ u/(1+u²)² du,
  I₃ = ∫₀¹ u²/(1+u²)² du.
Then

  I = I₁ – 2I₂ + I₃.

Step 3a. Compute I₂.

Make the substitution w = 1+u², so that dw = 2u du. Then
  I₂ = ∫ u/(1+u²)² du = (1/2)∫ dw/w² = –1/(2w) + C.
Evaluating from u=0 to u=1:
  I₂ = [ –1/(2(1+1²)) ] – [ –1/(2(1+0²)) ] = (–1/4) + (1/2) = 1/4.

Step 3b. Compute I₁.

A standard integral is
  ∫ du/(1+u²)² = (u/(2(1+u²))) + (1/2) arctan u + C.
Hence,
  I₁ = [(1/(2(1+1²)) + ½ arctan 1) – (0 + ½ arctan 0)]
    = [1/4 + ½·(π/4)] = 1/4 + π/8.

Step 3c. Compute I₃.

Notice that
  u²/(1+u²)² = [ (1+u²) – 1 ]/(1+u²)² = 1/(1+u²) – 1/(1+u²)².
Thus,
  I₃ = ∫₀¹ [1/(1+u²) – 1/(1+u²)²] du = ∫₀¹ 1/(1+u²) du – I₁.
But ∫₀¹ 1/(1+u²) du = arctan u|₀¹ = π/4.
Thus,
  I₃ = π/4 – (1/4 + π/8) = (π/4 – π/8) – 1/4 = (π/8) – 1/4.

Step 4. Combine the pieces.

Now,
  I = I₁ – 2I₂ + I₃ = (1/4 + π/8) – 2(1/4) + [(π/8) – 1/4].
Combine like terms:
  Coefficients without π: 1/4 – 1/2 – 1/4 = –1/2.
  Coefficients with π: π/8 + π/8 = π/4.
Thus,
  I = (π/4) – 1/2.

Step 5. Numerical approximation.

Since π/4 ≈ 0.7853981634, we have
  I ≈ 0.7853981634 – 0.5 = 0.2853981634.

Thus, the exact answer is (π/4) – 1/2 and its 10‐digit rounded decimal value is 0.2853981634.

{"answer": "\\frac{\\pi}{4} - \\frac{1}{2}", "numerical_answer": "0.2853981634"}