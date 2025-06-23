We wish to evaluate

  I = ∫₀² x^(–1/2) H₃(√[4]{x(2 – x)}) dx,
             (1)

where H₃ denotes the Hermite polynomial of order 3. In the physicists’ convention the Hermite polynomials are given by

  H₃(z) = 8z³ – 12z.

Thus,
  H₃(√[4]{x(2 – x)}) = 8 (√[4]{x(2 – x)})³ – 12 (√[4]{x(2 – x)})
            = 8 [x(2 – x)]^(3/4) – 12 [x(2 – x)]^(1/4).

Inserting this into (1) we write I as the difference of two integrals:
  I = 8I₁ – 12I₂,
where
  I₁ = ∫₀² x^(–1/2) [x(2 – x)]^(3/4) dx,
  I₂ = ∫₀² x^(–1/2) [x(2 – x)]^(1/4) dx.

Notice that
  I₁ = ∫₀² x^(–1/2 + 3/4) (2 – x)^(3/4) dx = ∫₀² x^(1/4) (2 – x)^(3/4) dx,
  I₂ = ∫₀² x^(–1/2 + 1/4) (2 – x)^(1/4) dx = ∫₀² x^(–1/4) (2 – x)^(1/4) dx.

It is convenient to make the substitution

  x = 2u, dx = 2 du,
with u running from 0 to 1. Note that
  2 – x = 2 – 2u = 2(1 – u).

Then for I₁ we have:
  I₁ = ∫₀¹ (2u)^(1/4) [2(1 – u)]^(3/4) · 2 du
     = 2^(1/4)2^(3/4)·2 ∫₀¹ u^(1/4)(1 – u)^(3/4) du
     = 2^(1/4+3/4+1) ∫₀¹ u^(1/4)(1 – u)^(3/4) du
     = 2² ∫₀¹ u^(1/4)(1 – u)^(3/4) du
     = 4 B(5/4, 7/4),
since the Beta function is given by
  B(a, b) = ∫₀¹ u^(a–1)(1 – u)^(b–1) du,
and here a = 5/4 (because 1/4 = a – 1) and b = 7/4.

Similarly, for I₂ we get:
  I₂ = ∫₀² x^(–1/4) (2 – x)^(1/4) dx
     = ∫₀¹ (2u)^(–1/4) [2(1 – u)]^(1/4) · 2 du
     = 2^(–1/4+1/4+1) ∫₀¹ u^(–1/4)(1 – u)^(1/4) du
     = 2 ∫₀¹ u^(–1/4)(1 – u)^(1/4) du
     = 2 B(3/4, 5/4),
where now a = 3/4 (since –1/4 = a – 1) and b = 5/4.

Thus, our original integral becomes
  I = 8I₁ – 12I₂ = 8·[4 B(5/4, 7/4)] – 12·[2 B(3/4,5/4)]
     = 32 B(5/4, 7/4) – 24 B(3/4, 5/4).

Writing the Beta functions in terms of Gamma functions,
  B(5/4, 7/4) = Γ(5/4)Γ(7/4) / Γ(3)   (with Γ(3) = 2! = 2),
  B(3/4, 5/4) = Γ(3/4)Γ(5/4) / Γ(2)   (with Γ(2) = 1),
so that
  I = 32 [Γ(5/4)Γ(7/4)/2] – 24 [Γ(3/4)Γ(5/4)]
     = 16 Γ(5/4) Γ(7/4) – 24 Γ(3/4) Γ(5/4)
     = Γ(5/4) [16 Γ(7/4) – 24 Γ(3/4)].

Recall the recurrence relation for the Gamma function:
  Γ(7/4) = (3/4) Γ(3/4).
Thus,
  16 Γ(7/4) – 24 Γ(3/4) = 16 (3/4) Γ(3/4) – 24 Γ(3/4)
             = [12 – 24] Γ(3/4)
             = –12 Γ(3/4).

Therefore, the integral simplifies to
  I = –12 Γ(5/4) Γ(3/4).

A further nice simplification comes from the relation
  Γ(5/4) = (1/4) Γ(1/4),
so that
  Γ(5/4)Γ(3/4) = (1/4) Γ(1/4)Γ(3/4).
A well‐known identity is
  Γ(1/4)Γ(3/4) = π√2.
Thus,
  Γ(5/4)Γ(3/4) = (1/4) π√2,
and hence,
  I = –12 · (π√2/4) = –3π√2.

Finally, the numerical approximation is computed as follows:
  √2 ≈ 1.4142135624 and π ≈ 3.1415926536,
so that
  I ≈ –3 × 1.4142135624 × 3.1415926536 ≈ –13.3286488140.

Therefore, the exact answer is 
  –3√2 π 
and numerically it is approximately –13.3286488140.

{"answer": "$-3\\sqrt{2}\\pi$", "numerical_answer": "-13.3286488140"}