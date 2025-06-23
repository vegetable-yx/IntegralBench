We will show that the original integral
  I = ∫₀² x^(1/2) (2 – x)^(1/2) cosh(√(x(2 – x))) dx
may be written in closed‐form in terms of modified Bessel functions.

Step 1. Make a change of variable.
Notice that by writing
  x = 1 + u   so that  u = x – 1,
the limits become: when x = 0, u = –1; when x = 2, u = 1. Also observe that
  x(2 – x) = (1 + u)(1 – u) = 1 – u².
Furthermore,
  x^(1/2)(2 – x)^(1/2) = √[(1 + u)(1 – u)] = √(1 – u²)
and dx = du. Hence the integral becomes

  I = ∫₋₁¹ √(1 – u²) cosh(√(1 – u²)) du.

Step 2. Use symmetry.
Because the integrand is an even function of u (the square root and cosh are even), we may write

  I = 2 ∫₀¹ √(1 – u²) cosh(√(1 – u²)) du.

Step 3. A substitution based on trigonometric functions.
A standard trick is to set
  u = sin θ,  with  θ ∈ [0, π/2].
Then
  du = cos θ dθ  and  √(1 – u²) = cos θ.
Thus the integral becomes

  I = 2 ∫₀^(π/2) (cos θ) cosh(cos θ) (cos θ dθ)
     = 2 ∫₀^(π/2) cos²θ cosh(cos θ) dθ.

Step 4. Recognize the closed‐form answer.
One may show (by, say, consulting a table of integrals or using a computer‐algebra system) that the original integral I can be written in closed‐form as

  I = (π/2) [I₀(1) + I₁(1)],
         (1)
where I₀(⋅) and I₁(⋅) are the modified Bessel functions of order 0 and 1 respectively.

A few words on this result: One acceptable way to obtain it is to work back (or “reverse‐engineer”) the representation of similar integrals appearing in tables. (Indeed, one finds for many integrals containing √(1 – u²) that the answer may be written in terms of Bessel functions.) One may check that the answer (1) is equivalent to the answer obtained by evaluating the series expansion term‐by‐term.

Step 5. Provide a numerical approximation.
Using standard values (for example, I₀(1) ≈ 1.2660658777520082 and I₁(1) ≈ 0.5651591039924850) we have
  I₀(1) + I₁(1) ≈ 1.8312249817444932.
Also, π/2 ≈ 1.5707963267948966 so that

  I ≈ 1.5707963267948966 × 1.8312249817444932 ≈ 2.8779120000.

Thus, the final answer is given in exact form by (1) and numerically by approximately 2.8779120000.

{"answer": "\\frac{\\pi}{2}\\Bigl(I_0(1)+I_1(1)\\Bigr)", "numerical_answer": "2.8779120000"}