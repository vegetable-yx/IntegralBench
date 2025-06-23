We wish to show that

  I = ∫₀¹ x³·arccos(x)·(arcsin(x))² dx

may be written in closed‐form. One useful idea is to use the identity

  arccos x = π⁄2 – arcsin x.

Thus

  I = ∫₀¹ x³·[π⁄2 – arcsin x]·(arcsin x)² dx
    = (π⁄2)∫₀¹ x³·(arcsin x)² dx – ∫₀¹ x³·(arcsin x)³ dx.

Call

  I₁ = ∫₀¹ x³·(arcsin x)² dx  and  I₂ = ∫₀¹ x³·(arcsin x)³ dx,

so that

  I = (π⁄2) I₁ – I₂.

A convenient change of variable is

  u = arcsin x  ⇒  x = sin u  and  dx = cos u du.
When x goes from 0 to 1, u goes from 0 to π⁄2. In these terms we have:
  x³ = sin³ u  and the integrals become
  I₁ = ∫₀^(π⁄2) sin³ u · u² · cos u du  and  I₂ = ∫₀^(π⁄2) sin³ u · u³ · cos u du.

A key observation is that
  d/du [sin⁴ u] = 4 sin³u cos u.
Thus one may write
  sin³u cos u du = (1⁄4) d(sin⁴ u),
so that in general (with n a positive integer)
  Iₙ ≡ ∫₀^(π⁄2) uⁿ sin³ u cos u du = (1⁄4)∫₀^(π⁄2) uⁿ d(sin⁴ u).
An integration by parts (with uⁿ as the “algebraic factor”) then gives
  Iₙ = (1⁄4)[uⁿ sin⁴u]₀^(π⁄2) – (n⁄4)∫₀^(π⁄2) u^(n–1) sin⁴u du.
Since sin⁴(π⁄2) = 1, we obtain
  Iₙ = (π⁄2)ⁿ⁄4 – (n⁄4) Jₙ₋₁      (1)
with
  Jₙ₋₁ = ∫₀^(π⁄2) u^(n–1) sin⁴u du.

In our case we need n = 2 (for I₁) and n = 3 (for I₂):

• For n = 2:
  I₁ = (π⁄2)²⁄4 – (2⁄4) J₁ = π²⁄16 – (1⁄2) J₁.
  To compute J₁ = ∫₀^(π⁄2) u·sin⁴u du note that
   sin⁴u = (3⁄8) – (1⁄2) cos 2u + (1⁄8) cos 4u.
  Then
   J₁ = (3⁄8)∫₀^(π⁄2) u du – (1⁄2)∫₀^(π⁄2) u cos2u du + (1⁄8)∫₀^(π⁄2) u cos4u du.
  A short calculation gives
   ∫₀^(π⁄2) u du = π²⁄8,
   ∫₀^(π⁄2) u cos2u du = –1⁄2,
   ∫₀^(π⁄2) u cos4u du = 0.
  So
   J₁ = (3π²)/(64) + 1⁄4.
Thus,
  I₁ = π²⁄16 – (1⁄2)[(3π²)/(64) + 1⁄4]
     = π²⁄16 – (3π²)/(128) – 1⁄8
     = (8π² – 3π²)/(128) – 1⁄8
     = (5π²)/(128) – 1⁄8.

• For n = 3:
  I₂ = (π⁄2)³⁄4 – (3⁄4) J₂,
with
  J₂ = ∫₀^(π⁄2) u² sin⁴u du = (3⁄8) Iₐ – (1⁄2) I_b + (1⁄8) I_c,
where
  Iₐ = ∫₀^(π⁄2) u² du = π³⁄24,
  I_b = ∫₀^(π⁄2) u² cos2u du,  and  I_c = ∫₀^(π⁄2) u² cos4u du.
A (lengthy but standard) evaluation yields
  I_b = –π⁄4  and  I_c = π⁄16.
Then one obtains
  J₂ = (3π³)/(192) + π⁄8 + π⁄128.
A little algebra shows that
  J₂ = (6π³ + 51π)/384.
Thus,
  I₂ = (π³/8)/4 – (3⁄4)[(6π³ + 51π)/384]
     = (π³/32) – (18π³ + 153π)/1536
     = (30π³ – 153π)/1536.

Returning to the original integrals, we have
  I = (π⁄2) I₁ – I₂
    = (π⁄2)[(5π²)/(128) – 1⁄8] – (30π³ – 153π)/1536.
Writing everything with common denominator 1536 (since 1536 = 12×128) we note that
  (π⁄2)·(5π²/128) = 5π³/256 = 30π³/1536  and  (π⁄2)·(1⁄8) = π/16 = 96π/1536.
Thus,
  I = [30π³/1536 – 96π/1536] – [30π³/1536 – 153π/1536]
    = [30π³ – 96π – 30π³ + 153π]⁄1536
    = (57π)/1536
    = (19π)/512.

A numerical approximation is:
  (19π)/512 ≈ (19 × 3.141592653589793)⁄512 ≈ 59.690260⁄512 ≈ 0.1165605469.

Thus, the final answer is

Exact: 19π/512  and  Numerical: 0.1165605469

{"answer": "\\frac{19\\pi}{512}", "numerical_answer": "0.1165605469"}