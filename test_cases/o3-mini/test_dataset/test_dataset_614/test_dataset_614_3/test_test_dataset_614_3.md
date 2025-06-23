We wish to evaluate
  I = ∫₀¹ (x³ + x + 1)/(3x² − 3x + 4) dx.

Step 1. Perform polynomial division (since the degree in the numerator is 3 and in the denominator is 2).

Divide x³ + 0·x² + x + 1 by 3x² − 3x + 4:

• The leading term: x³/(3x²) = x/3.
• Multiply: (x/3)(3x² − 3x + 4) = x³ − x² + (4/3)x.
• Subtract from the numerator:
  [x³ + 0x² + x + 1] − [x³ − x² + (4/3)x] = x² + (x − 4/3 x) + 1 = x² − (1/3)x + 1.

Thus, we express the integrand as:
  (x³ + x + 1)/(3x² − 3x + 4) = x/3 + [x² − (1/3)x + 1]/(3x² − 3x + 4).

So the integral splits as

  I = ∫₀¹ x/3 dx + ∫₀¹ [x² − (1/3)x + 1]/(3x² − 3x + 4) dx.

Computing the first part:
  ∫₀¹ x/3 dx = (1/3)[x²/2]₀¹ = 1/6.

Let J denote the second part:
  J = ∫₀¹ [x² − (1/3)x + 1]/(3x² − 3x + 4) dx.

Step 2. Make a substitution to complete the square in the denominator.
Write the denominator as:
  3x² − 3x + 4 = 3(x² − x) + 4.
Complete the square in x² − x:
  x² − x = (x − 1/2)² − 1/4.
Then
  3x² − 3x + 4 = 3[(x − 1/2)² − 1/4] + 4 = 3(x − 1/2)² − 3/4 + 4 = 3(x − 1/2)² + 13/4.

Next, let u = x − 1/2. Then x = u + 1/2 and dx = du. The limits change as:
  x = 0 ⇒ u = −1/2,
  x = 1 ⇒ u = 1/2.

Now express the numerator in terms of u:
  x² − (1/3)x + 1 becomes
   (u + 1/2)² − (1/3)(u + 1/2) + 1
   = u² + u + 1/4 − (1/3)u − 1/6 + 1
   = u² + (1 − 1/3)u + (1/4 − 1/6 + 1)
   = u² + (2/3)u + ( (3 − 2)/12 + 1 )
   = u² + (2/3)u + (1/12 + 1)
   = u² + (2/3)u + 13/12.

The denominator becomes:
  3(x − 1/2)² + 13/4 = 3u² + 13/4.

Thus, J can be written as
  J = ∫₍₋½₎^(½) [u² + (2/3)u + 13/12] / [3u² + 13/4] du.

Step 3. Clear the fractions by multiplying numerator and denominator by 12:
  Numerator: 12[u² + (2/3)u + 13/12] = 12u² + 8u + 13.
  Denominator: 12[3u² + 13/4] = 36u² + 39.
Notice that 36u² + 39 factors as 3(12u² + 13) because 3(12u² + 13) = 36u² + 39.
So,
  J = ∫₍₋½₎^(½) (12u² + 8u + 13)/(3(12u² + 13)) du = 1/3 ∫₍₋½₎^(½) [12u² + 8u + 13]/(12u² + 13) du.
Write the integrand as:
  [12u² + 8u + 13]/(12u² + 13) = 1 + (8u)/(12u² + 13).

Thus,
  J = 1/3 ∫₍₋½₎^(½) {1 + (8u)/(12u² + 13)} du
    = 1/3 { ∫₍₋½₎^(½) 1 du + ∫₍₋½₎^(½) (8u)/(12u² + 13) du }.

Observe that the second integrand, (8u)/(12u² + 13), is an odd function of u since the numerator is odd and the denominator is even. Over symmetric limits [−½, ½] its integral is zero.

Therefore,
  J = 1/3 { [u]₍₋½₎^(½)} = 1/3 (1/2 − (−1/2)) = 1/3 (1) = 1/3.

Step 4. Combine the parts:
  I = (first part) + J = 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2.

Thus the exact answer is ½.

The numerical approximation is 0.5000000000 (to 10 decimal places).

{"answer": "$\\frac{1}{2}$", "numerical_answer": "0.5000000000"}