We start with the integral

  I = ∫₀^(π/2) [cos²x (1 + cos x)] / [1 + cos x + sin x]² dx.

A very effective way is to use the tangent half‐angle substitution. Let

  t = tan(x/2).

Then the following formulas hold:
  sin x = 2t/(1+t²),
  cos x = (1-t²)/(1+t²),
  dx = 2 dt/(1+t²).

Step 1. Express the terms in the integrand in terms of t.

• cos² x (1+cos x):

  cos x = (1-t²)/(1+t²) ⇒ cos² x = ((1-t²)/(1+t²))².
  Also, 1 + cos x = 1 + (1-t²)/(1+t²) = [(1+t²)+(1-t²)]/(1+t²) = [2/(1+t²)].
  Thus,
   cos²x (1+cos x) = ((1-t²)²/(1+t²)²)·(2/(1+t²)) = 2(1-t²)²/(1+t²)³.

• Denominator: 1+cos x+sin x:

  1 + cos x + sin x = 1 + (1-t²)/(1+t²) + (2t/(1+t²))
            = [(1+t²) + (1-t²) + 2t] / (1+t²)
            = [2 + 2t] / (1+t²) = 2(1+t)/(1+t²).
  Thus,
   [1+cos x+sin x]² = [2(1+t)/(1+t²)]² = 4(1+t)²/(1+t²)².

Step 2. Substitute everything into the integral.

The differential dx is
  dx = 2 dt/(1+t²).

So the integrand becomes:
  I = ∫ [2(1-t²)²/(1+t²)³] ÷ [4(1+t)²/(1+t²)²] * [2 dt/(1+t²)].

Simplify step by step:
1. Write the division as multiplication by the reciprocal:
  = ∫ [2(1-t²)²/(1+t²)³] * [(1+t²)²/(4(1+t)²)] * [2/(1+t²)] dt.
2. Combine the constants:
  2 * 2 = 4 in the numerator and 4 in the denominator cancel.
3. Combine the powers of (1+t²):
  We have (1+t²)³ in the denominator multiplied by 1/(1+t²) from dx and (1+t²)² in the numerator:
  (1+t²)²/( (1+t²)³*(1+t²)) = (1+t²)²/(1+t²)⁴ = 1/(1+t²)²; however, note that:
  2/(1+t²) from dx multiplies our denominator to give overall factor:
  [2/(1+t²)] * [1/(1+t²)³] * (1+t²)² = 2/(1+t²)².
  It is easier to see cancellation directly:
  The factors (1+t²)² in the numerator cancel with two of the three factors in (1+t²)³, and then the extra factor 1/(1+t²) cancels the remaining one:
  Overall, these (1+t²) factors cancel completely.
4. So the integrand simply becomes:
  I = ∫ (1-t²)²/(1+t)² dt.

Step 3. Notice a perfect cancellation.

Write (1-t²)² as ((1-t)(1+t))² = (1-t)² (1+t)². Then,
  (1-t)²(1+t)²/(1+t)² = (1-t)².

Thus, the integral reduces to:
  I = ∫₀¹ (1-t)² dt.
Here the new limits are obtained from:
  x = 0 ⇒ t = tan(0) = 0,
  x = π/2 ⇒ t = tan(π/4) = 1.

Step 4. Compute the simplified integral.

Expand (1-t)²:
  (1-t)² = 1 - 2t + t².
Integrate term by term:
  ∫₀¹ (1 - 2t + t²) dt = [t - t² + t³/3] from 0 to 1 = (1 - 1 + 1/3) - 0 = 1/3.

Thus, the exact value of the integral is 1/3.

Step 5. Provide a numerical approximation.

1/3 ≈ 0.3333333333 (rounded to 10 decimal places).

The final answer in the required JSON format is:
{"answer": "\\frac{1}{3}", "numerical_answer": "0.3333333333"}