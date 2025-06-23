We wish to evaluate

  I = ∫₀² x^(–1/2) H₃( (x(2–x))^(1/4) ) dx.

A common definition of the (physicists’) Hermite polynomial H₃ is

  H₃(y) = 8y³ – 12y.

Thus, setting y = (x(2–x))^(1/4), we have

  H₃((x(2–x))^(1/4)) = 8 (x(2–x))^(3/4) – 12 (x(2–x))^(1/4).

Then the integral becomes

  I = 8∫₀² x^(–1/2) (x(2–x))^(3/4) dx – 12∫₀² x^(–1/2) (x(2–x))^(1/4) dx.

Notice that
  (x(2–x))^(3/4) = x^(3/4)(2–x)^(3/4)
  (x(2–x))^(1/4) = x^(1/4)(2–x)^(1/4).

Thus we write
  I = 8∫₀² x^(–1/2 + 3/4)(2–x)^(3/4) dx – 12∫₀² x^(–1/2 + 1/4)(2–x)^(1/4) dx,
which simplifies to
  I = 8∫₀² x^(1/4)(2–x)^(3/4) dx – 12∫₀² x^(–1/4)(2–x)^(1/4) dx.

We now denote the two integrals by

  I₁ = ∫₀² x^(1/4)(2–x)^(3/4) dx  and  I₂ = ∫₀² x^(–1/4)(2–x)^(1/4) dx.

To express these in terms of the Beta integral, substitute x = 2u (so that dx = 2 du and when x goes from 0 to 2, u goes from 0 to 1).

For I₁:
  I₁ = ∫₀¹ (2u)^(1/4)[2(1–u)]^(3/4)·2 du
     = 2·2^(1/4)·2^(3/4)∫₀¹ u^(1/4)(1–u)^(3/4) du
     = 2·2^(1) ∫₀¹ u^(1/4)(1–u)^(3/4) du
     = 4 B(1/4+1, 3/4+1)
     = 4 B(5/4, 7/4).

For I₂:
  I₂ = ∫₀² x^(–1/4)(2–x)^(1/4)dx
  Substitute x = 2u:
  I₂ = ∫₀¹ (2u)^(–1/4)[2(1–u)]^(1/4)·2 du
     = 2·2^(–1/4)·2^(1/4)∫₀¹ u^(–1/4)(1–u)^(1/4) du
     = 2∫₀¹ u^(–1/4)(1–u)^(1/4) du
     = 2 B(3/4, 5/4).

Thus the original integral is now
  I = 8 I₁ – 12 I₂ = 8·[4 B(5/4, 7/4)] – 12·[2 B(3/4, 5/4)]
     = 32 B(5/4, 7/4) – 24 B(3/4, 5/4).

Recall the Beta function in terms of Gamma functions:
  B(a, b) = Γ(a)Γ(b) / Γ(a+b).

So,
  B(5/4, 7/4) = [Γ(5/4)Γ(7/4)] / Γ(3)  with Γ(3) = 2,
  B(3/4, 5/4) = [Γ(3/4)Γ(5/4)] / Γ(2)  with Γ(2) = 1.

Thus we have
  I = 32·(Γ(5/4)Γ(7/4)/2) – 24·[Γ(3/4)Γ(5/4)]
     = 16 Γ(5/4)Γ(7/4) – 24 Γ(3/4)Γ(5/4).

Factor out Γ(5/4):
  I = Γ(5/4) [16 Γ(7/4) – 24 Γ(3/4)].

Notice that using the recurrence relation Γ(z+1) = z Γ(z), we can write
  Γ(7/4) = (3/4) Γ(3/4).

Thus,
  I = Γ(5/4) [16·(3/4)Γ(3/4) – 24 Γ(3/4)]
     = Γ(5/4)Γ(3/4)[12 – 24]
     = –12 Γ(5/4)Γ(3/4).

There is a known relation between Gamma functions:
  Γ(5/4) = (1/4) Γ(1/4)   and  Γ(1/4)Γ(3/4) = π√2.
Therefore,
  Γ(5/4)Γ(3/4) = (1/4) Γ(1/4)Γ(3/4) = (π√2)/4.

Thus the integral becomes
  I = –12 · (π√2)/4 = –3π√2.

Numerically, using
  π ≈ 3.141592653589793  and  √2 ≈ 1.4142135623730951,
we get
  I ≈ –3 × 3.141592653589793 × 1.4142135623730951
    ≈ –13.3286488120.

{"answer": "$-3\\sqrt{2}\\pi$", "numerical_answer": "-13.3286488120"}