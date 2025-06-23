We wish to evaluate

  I = ∫₀¹ ⎣cos(π/x)⎦ dx,

where ⎣y⎦ is the floor function.

Step 1. Understanding the integrand

For x in (0,1], note that
  y = cos(π/x)
always takes values in [–1, 1]. Since the floor function returns the greatest integer ≤ y, the only possible values are –1, 0, or (at isolated points) 1. In fact, cos(π/x) = 1 occurs only when
  π/x = 2πn ⟹ x = 1/(2n)  (n∈ℕ),
a set of isolated points (of measure zero) that do not affect the integral.

Thus, almost everywhere on (0,1] we have:
  if cos(π/x) < 0, then ⎣cos(π/x)⎦ = –1,
  if cos(π/x) ∈ [0,1), then ⎣cos(π/x)⎦ = 0.

Step 2. Finding the “switching” regions

We now find those x in (0,1] where cos(π/x) is nonnegative. Recall that cos θ ≥ 0 when
  θ ∈ [–π/2+2πn, π/2+2πn], n ∈ ℤ.

Since π/x > 0 we restrict to n ≥ 0. However, note that when n = 0 the interval is (–π/2, π/2), and its intersection with (0,∞) is (0, π/2]. But for x ∈ (0,1], we have
  π/x ≥ π > π/2,
so the n = 0 case does not occur.

Thus for n ≥ 1 we require:
  2πn – π/2 ≤ π/x ≤ 2πn + π/2.
Solve for x by inverting (x>0 reverses inequalities when inverting the positive quantity):

• From π/x ≤ 2πn + π/2, we get
  x ≥ π/(2πn + π/2) = 2/(4n + 1).

• From π/x ≥ 2πn – π/2, we get
  x ≤ π/(2πn – π/2) = 2/(4n – 1).

Thus, for each n ≥ 1 the set of x for which cos(π/x) ≥ 0 is
  Aₙ = [2/(4n + 1), 2/(4n – 1)].
On Aₙ we have ⎣cos(π/x)⎦ = 0; outside these intervals (but in (0,1]) we have ⎣cos(π/x)⎦ = –1.

Step 3. Writing the integral in terms of the lengths of the intervals

The union A = ⋃ₙ₌₁∞ Aₙ is the set on which the integrand is 0. Hence,
  I = ∫₀¹ ⎣cos(π/x)⎦ dx = ∫₍₀,₁₎∖A (–1) dx + ∫₍A₎ 0 dx = –(1 – m(A)),
with m(A) the total measure (length) of the union A. Since the intervals Aₙ are disjoint, we have
  m(A) = Σₙ₌₁∞ (length of Aₙ) = Σₙ₌₁∞ (2/(4n – 1) – 2/(4n + 1)).

Thus,
  I = –(1 – Σₙ₌₁∞ [2/(4n – 1) – 2/(4n + 1)])
   = 2 Σₙ₌₁∞ (1/(4n – 1) – 1/(4n + 1)) – 1.

Step 4. Evaluating the series in closed‐form

Write
  S = Σₙ₌₁∞ (1/(4n – 1) – 1/(4n + 1)).
We can rewrite S by factoring 1/4:
  S = 1/4 Σₙ₌₁∞ (1/(n – 1/4) – 1/(n + 1/4)).

There is a known formula involving the digamma function ψ:
  Σₙ₌₁∞ [1/(n+a) – 1/(n+b)] = ψ(1+b) – ψ(1+a).

Here, take a = –1/4 and b = 1/4. Then,
  S = 1/4 [ψ(1+1/4) – ψ(1 – 1/4)] = 1/4 [ψ(5/4) – ψ(3/4)].

Thus our integral becomes
  I = 2S – 1 = 2*(1/4 [ψ(5/4) – ψ(3/4)]) – 1 = 1/2 (ψ(5/4) – ψ(3/4)) – 1.

Now, using the recurrence for the digamma function,
  ψ(z+1) = ψ(z) + 1/z,
with z = 1/4 we have
  ψ(5/4) = ψ(1/4 + 1) = ψ(1/4) + 4.
Substitute into the above:
  ψ(5/4) – ψ(3/4) = (ψ(1/4) + 4) – ψ(3/4) = [ψ(1/4) – ψ(3/4)] + 4.

There is also a reflection formula for the digamma function which gives
  ψ(1 – z) – ψ(z) = π cot(πz).
Taking z = 3/4 gives
  ψ(1/4) – ψ(3/4) = π cot(3π/4) = π (–1) = –π.
Thus, 
  ψ(5/4) – ψ(3/4) = (–π) + 4 = 4 – π.

Therefore,
  I = 1/2 (4 – π) – 1 = 2 – π/2 – 1 = 1 – π/2.

Step 5. Final Answer and Numerical Approximation

The exact answer is

  I = 1 – π/2.

Numerically,
  π/2 ≈ 1.5707963268 ⇒ 1 – 1.5707963268 ≈ –0.5707963268.

The final result in the required JSON format is:
{"answer": "$1 - \\frac{\\pi}{2}$", "numerical_answer": "-0.5707963268"}