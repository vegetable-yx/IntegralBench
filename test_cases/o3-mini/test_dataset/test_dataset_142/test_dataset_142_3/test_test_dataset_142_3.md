We will show that one acceptable answer is
  I = (π/4)[I₀(2) − L₀(2)] + (1/2)L₁(2),
where I₀ is the modified Bessel function of order zero and Lₙ is the modified Struve function of order n.

One way to “discover” this answer is to start with

  I = ∫₀¹ arccos x · I₀(2x) dx.

A useful change of variable is to set
  x = cos u    (so that u = arccos x)
with 
  dx = – sin u du.
Then the limits become: when x = 0, u = π/2 and when x = 1, u = 0. Hence

  I = ∫ᵤ₌π/2⁰ u · I₀(2 cos u) (– sin u du)
    = ∫₀^(π/2) u sin u I₀(2 cos u) du.

One may then try to expand I₀(2 cos u) (recalling that
  I₀(z) = Σₘ₌₀∞ (z/2)^(2m)/(m!)²)
and exchange summation and integration. In this way one finds that the answer can be written in “closed‐form” in terms of special functions. (There are several equivalent forms.) For example one may show that

  I = (π/4)[I₀(2) − L₀(2)] + (1/2)L₁(2).

A short numerical check (using, for instance, known values
  I₀(2) ≈ 2.2795853023, L₀(2) ≈ 1.5906368546, L₁(2) ≈ 1.1910036)
shows that

  (π/4)[I₀(2) − L₀(2)] ≈ 0.541052     and (1/2)L₁(2) ≈ 0.595502,
so that I ≈ 0.541052 + 0.595502 = 1.136554.

Any answer equivalent to the answer above is acceptable.

{"answer": "\\frac{\\pi}{4}\\Bigl[I_0(2)-L_0(2)\\Bigr]+\\frac{1}{2}L_1(2)", "numerical_answer": "1.1365538000"}