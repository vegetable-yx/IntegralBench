We will show that

  I = ∫₀^(π/2) [cos²x (1 + cos x)]⁄[1 + cos x + sin x]² dx = (1 – ln2)/2

and that numerically I ≈ 0.1534264097.

The idea is to “engineer” a derivative in the integrand. One may check that if we define

  f(x) = sin x⁄[1 + cos x + sin x],

then a short calculation gives

  f ′(x) = [cos x (1 + cos x)]⁄[1 + cos x + sin x]².

Thus our integrand is
  cos²x (1 + cos x)/[1 + cos x + sin x]² = cos x · f ′(x).

Now, write

  I = ∫₀^(π/2) cos x · f ′(x) dx.

An integration by parts (with u = f(x) so that du = f ′(x)dx, and dv = cos x dx so that v = sin x) gives

  I = [sin x · f(x)]₀^(π/2) – ∫₀^(π/2) sin x · f(x) dx.

Since
  f(x) = sin x⁄[1 + cos x + sin x],
we have
  ∫₀^(π/2) sin x · f(x) dx = ∫₀^(π/2) sin²x⁄[1 + cos x + sin x] dx.

Thus,
  I = [sin x · sin x⁄(1 + cos x + sin x)]₀^(π/2) – J,
where
  J = ∫₀^(π/2) sin²x⁄[1 + cos x + sin x] dx.

At the endpoints one finds: At x = π/2, sin(π/2)=1 and cos(π/2)=0 so that f(π/2)=1⁄(1+0+1)=1/2; at x = 0, the term vanishes. Hence the boundary term is ½ and

  I = ½ – J.            (1)

Now a symmetry trick will allow us to evaluate J. Notice that if we also define
  B = ∫₀^(π/2) cos²x⁄[1 + cos x + sin x] dx,
then by the substitution x → (π/2 – x) (which interchanges sin and cos) we deduce that J = B. Adding these we have

  J + B = ∫₀^(π/2) [sin²x + cos²x]⁄[1 + cos x + sin x] dx = ∫₀^(π/2) 1⁄[1 + cos x + sin x] dx.

Because J = B the sum equals 2J, that is,

  2J = ∫₀^(π/2) 1⁄[1 + cos x + sin x] dx.

Thus

  J = (1⁄2) ∫₀^(π/2) 1⁄[1 + cos x + sin x] dx.  (2)

It remains now to evaluate

  K = ∫₀^(π/2) 1⁄[1 + cos x + sin x] dx.

A useful trick is to shift the variable; set

  u = x – (π/4),  so that dx = du.
Then one easily verifies that
  cos x + sin x = √2 cos u,
and hence
  1 + cos x + sin x = 1 + √2 cos u.
The new limits become u = –π/4 to π/4 and so

  K = ∫₋(π/4)^(π/4) 1/(1 + √2 cos u) du.

Since the integrand is even we can write

  K = 2∫₀^(π/4) 1/(1 + √2 cos u) du.

Next we use the Weierstrass substitution t = tan(u/2). One may show that after some algebra this integral reduces to

  L = ∫₀^(tan(π/8)) [2 dt/((1+√2) + (1–√2)t²)].

A brief calculation shows that (1+√2)(√2–1) = 1. Hence one obtains

  L = 2 artanh[(√2–1)t] evaluated from 0 to t = tan(π/8).

But one well-known trigonometric fact is that tan(π/8) = √2 – 1. Thus

  L = 2 artanh[(√2 – 1)²].

Writing out artanh
  artanh(z) = (1/2) ln((1+z)/(1–z)),
and noting that

  (√2–1)² = 3 – 2√2,
one finds after some algebra that

  L = ln(√2) = (1⁄2) ln2.

Thus it follows that

  K = 2L = ln2.

Returning to (2), we have

  J = ½ · K = (ln 2)/2.

Finally, (1) gives

  I = ½ – (ln2)/2 = (1 – ln2)/2.

A numerical evaluation gives ln2 ≈ 0.6931471806 so that

  I ≈ (1 – 0.6931471806)/2 ≈ 0.1534264097.

The final answer is therefore:

{"answer": "$(1-\\ln2)/2$", "numerical_answer": "0.1534264097"}