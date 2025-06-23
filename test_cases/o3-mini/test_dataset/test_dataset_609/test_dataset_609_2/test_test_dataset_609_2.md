We wish to evaluate

  I = ∫₀¹ ⎣cos(π/x)⎦ dx,

where ⎣y⎦ denotes the floor of y. Notice that for any x in (0, 1], we have

  t = π/x ≥ π.

Since cos t oscillates between –1 and 1, its floor (the greatest integer not exceeding cos t) can take on the values –1, 0, or (at isolated points) 1. (Indeed, cos(π/x) = 1 only when π/x = 2πk, i.e. x = 1/(2k) for k ∈ ℕ. Such points have measure zero.)

Observe that for almost every x, the value of cos(π/x) is strictly less than 1. Moreover, because cos t ∈ [–1, 1] its floor is
  ⎣cos t⎦ = 0 if cos t ∈ [0, 1),
  ⎣cos t⎦ = –1 if cos t ∈ [–1, 0).

Thus the integrand is 0 on those x for which cos(π/x) ≥ 0 and –1 otherwise. In other words, we can write

  I = ∫₀¹ ⎣cos(π/x)⎦ dx = [measure of {x ∈ (0,1] where cos(π/x) ≥ 0}]·0 + [measure of its complement]·(–1).

Let S be the set in (0,1] where cos(π/x) ≥ 0. Then

  I = –(1 – m(S)) = m(S) – 1.

Thus the problem reduces to finding the total length (Lebesgue measure) of S.

Step 1. Characterizing the set S

Since we have t = π/x, the condition cos(π/x) ≥ 0 becomes cos t ≥ 0. Recall that

  cos t ≥ 0 ⟺ t ∈ [–π/2 + 2πk, π/2 + 2πk], k ∈ ℤ.

Since t = π/x ≥ π, we must have k ≥ 1. For each integer k ≥ 1, cos t ≥ 0 when
  t ∈ [2πk – π/2, 2πk + π/2].

Changing back to x using t = π/x (a strictly decreasing function) we get, for each k ≥ 1, that
  π/x ∈ [2πk – π/2, 2πk + π/2]
  ⟹ x ∈ [π/(2πk + π/2), π/(2πk – π/2)].

Simplify the endpoints:
  2πk ± (π/2) = π(4k ± 1)/2,
so the interval becomes
  x ∈ [π/(π(4k+1)/2), π/(π(4k–1)/2)] = [2/(4k+1), 2/(4k–1)].

Thus, for every integer k ≥ 1, the set S contains the interval
  Iₖ = [2/(4k+1), 2/(4k–1)].

It is easy to check that these intervals are disjoint and (for every k) they lie in (0,1] (for k = 1, I₁ = [2/5, 2/3] ⊂ (0,1], and for k ≥ 2, the endpoints are even smaller). Hence the total measure of S is the sum of the lengths of these intervals:

  m(S) = Σₖ₌₁∞ (length of Iₖ).

The length of Iₖ is

  ℓₖ = 2/(4k–1) – 2/(4k+1).

Thus

  m(S) = 2 Σₖ₌₁∞ (1/(4k–1) – 1/(4k+1)).

Step 2. Summing the Series

At first glance the series may appear complicated, but a change of index can help relate it to a known series. Write the sum as

  S₀ = Σₖ₌₁∞ (1/(4k–1) – 1/(4k+1)).

Let j = k – 1. Then
  S₀ = Σⱼ₌₀∞ (1/(4(j+1)–1) – 1/(4(j+1)+1))
     = Σⱼ₌₀∞ (1/(4j+3) – 1/(4j+5)).

Now recall the well-known alternating series for arctan 1:

  arctan 1 = 1 – 1/3 + 1/5 – 1/7 + … = π/4.

This can be written as

  Σₙ₌₀∞ ((–1)ⁿ/(2n+1)) = π/4.

Grouping terms with indices 0 and 1 mod 2, one obtains

  Σₖ₌₀∞ (1/(4k+1) – 1/(4k+3)) = π/4.

Call this sum T. Then notice that

  [1/(1) – 1/(3)] + [1/(5) – 1/(7)] + [1/(9) – 1/(11)] + … = π/4.

If we remove the very first term 1/1 from T, we have

  T – 1 = –1/(3) + 1/(5) – 1/(7)+ … = – Σₖ₌₀∞ (1/(4k+3) – 1/(4k+5)).

Thus,
  Σₖ₌₀∞ (1/(4k+3) – 1/(4k+5)) = 1 – T = 1 – (π/4).

But this last sum is exactly our series S₀ after the index change. Therefore,

  S₀ = 1 – (π/4).

Now recall that

  m(S) = 2S₀ = 2(1 – π/4) = 2 – (π/2).

Step 3. Writing the Integral

Recall the integral found earlier:
  I = m(S) – 1.
Thus,

  I = [2 – (π/2)] – 1 = 1 – (π/2).

Step 4. Numerical Approximation

We have
  I = 1 – (π/2).
Since π/2 ≈ 1.5707963268, it follows that

  I ≈ 1 – 1.5707963268 = –0.5707963268.

So the exact answer is 1 – (π/2) and the numerical approximation is –0.5707963268 (to 10 decimal places).

{"answer": "1-\\frac{\\pi}{2}", "numerical_answer": "-0.5707963268"}