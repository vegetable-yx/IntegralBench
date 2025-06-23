We wish to evaluate

  I = ∫₀¹ ⎣cos(π/x)⎦ dx,

where ⎣·⎦ denotes the floor function.

Step 1. Analyze the Values of cos(π/x) and Its Floor

Since
  cos(π/x) ∈ [–1, 1],
the possible integer values of ⎣cos(π/x)⎦ are –1, 0, or 1. (The value 1 occurs only when cos(π/x) exactly equals 1 at isolated points; such points have zero measure, so they do not contribute to the integral.) Thus almost everywhere on (0, 1] the integrand is either 0 or –1. In particular, when
  cos(π/x) < 0  ⟹  ⎣cos(π/x)⎦ = –1,
and when
  0 ≤ cos(π/x) < 1  ⟹  ⎣cos(π/x)⎦ = 0.

Step 2. Find the Intervals on Which cos(π/x) Is Negative

The cosine function is negative when its argument lies in an interval
  (π/2 + 2πk, 3π/2 + 2πk)  for k = 0, 1, 2, ….
Set
  t = π/x.
Then cos(π/x) < 0 if and only if
  t ∈ (π/2 + 2πk, 3π/2 + 2πk).
Converting back to x, we have
  π/x ∈ (π/2 + 2πk, 3π/2 + 2πk)
⟹  x ∈ (π/(3π/2 + 2πk), π/(π/2 + 2πk)).
Simplify each endpoint:
  Lower endpoint, aₖ = π/(3π/2 + 2πk) = (π)/( (3π + 4πk)/2 ) = 2/(3 + 4k),
  Upper endpoint, bₖ = π/(π/2 + 2πk) = (π)/( (π + 4πk)/2 ) = 2/(1 + 4k).

Thus for each k the open interval is
  Iₖ = (2/(3+4k), 2/(1+4k)).
Observe that for k = 0 we obtain I₀ = (2/3, 2). However, since our integration is over x ∈ [0, 1], for k = 0 we only take the intersection I₀ ∩ [0, 1] = (2/3, 1].

For k ≥ 1 the entire interval Iₖ lies in (0, 1].

Step 3. Compute the Contribution of the “–1” Regions

On any interval where cos(π/x) < 0, we have ⎣cos(π/x)⎦ = –1. Hence the contribution from such an interval is minus its length. Therefore the total contribution is

  I = – [ (length of I₀ ∩ [0,1]) + Σₖ₌₁∞ (length of Iₖ) ].

Now, compute the lengths:

• For k = 0:
  Length = min{1, 2/(1+0)} – 2/3 = 1 – 2/3 = 1/3.

• For k ≥ 1:
  Length(Iₖ) = 2/(1+4k) – 2/(3+4k).

Thus,
  I = – [ 1/3 + Σₖ₌₁∞ (2/(1+4k) – 2/(3+4k)) ].

Step 4. Sum the Series Using a Known Result

Notice that the series
  Σₖ₌₀∞ [1/(4k+1) – 1/(4k+3)]
is well known and sums to π/4 (this is one form of the Leibniz series for π). In our case, we have the sum starting at k = 0:
  Σₖ₌₀∞ [1/(4k+1) – 1/(4k+3)] = π/4.
But our series for k ≥ 1 is the full series minus the k = 0 term. When k = 0, 1/(1) – 1/(3) = 1 – 1/3 = 2/3. Therefore,
  Σₖ₌₁∞ [1/(4k+1) – 1/(4k+3)] = (π/4) – 2/3.

Multiply by 2:
  Σₖ₌₁∞ [2/(1+4k) – 2/(3+4k)] = 2[(π/4) – 2/3] = (π/2) – (4/3).

Thus, the total measure of x for which cos(π/x) is negative is
  (1/3) + [ (π/2) – (4/3) ] = (π/2) – 1.

Step 5. Conclude the Value of the Integral

Since on these intervals the integrand is –1, we have
  I = – [ (π/2) – 1 ] = 1 – (π/2).

Step 6. Provide the Numerical Approximation

Using π ≈ 3.141592653589793,
  π/2 ≈ 1.5707963267948966,
so
  1 – (π/2) ≈ 1 – 1.5707963267948966 ≈ –0.5707963267948966.
Rounded to 10 decimal places, this is approximately –0.5707963268.

Thus, the final results are:

Exact answer: 1 - (π/2)

Numerical approximation: -0.5707963268

{"answer": "1-\\frac{\\pi}{2}", "numerical_answer": "-0.5707963268"}