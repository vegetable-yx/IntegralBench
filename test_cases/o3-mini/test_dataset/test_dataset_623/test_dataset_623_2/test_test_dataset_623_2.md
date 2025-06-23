We wish to evaluate

  I = ∫₀ᴨ sec x · ln(1 + (cos x)/3) dx.

A very neat trick is to introduce a parameter by writing a family of integrals

  I(a) = ∫₀ᴨ sec x · ln(1 + a cos x) dx    (–)

so that our integral is I(1/3). (Notice that when a = 0 we get I(0) = 0 because ln 1 = 0.) Differentiating (–) with respect to a we may hope to obtain an expression that is easier to integrate.

Step 1. Differentiate I(a) with respect to a.

By differentiating under the integral sign we have

  I′(a) = d/da ∫₀ᴨ sec x · ln(1 + a cos x) dx = ∫₀ᴨ sec x · (cos x/(1 + a cos x)) dx.

But sec x = 1/cos x, so

  sec x · cos x/(1 + a cos x) = 1/(1 + a cos x).

Thus

  I′(a) = ∫₀ᴨ 1/(1 + a cos x) dx.

Step 2. Evaluate the x–integral.

A standard result (which holds for |a| < 1) is

  ∫₀ᴨ  dx/(1 + a cos x) = π/√(1 – a²).

So we have

  I′(a) = π/√(1 – a²).

Step 3. Integrate with respect to a.

We now recover I(a) by integrating I′(a):

  I(a) = ∫₀ᵃ I′(t) dt = ∫₀ᵃ [π/√(1 – t²)] dt = π ∫₀ᵃ dt/√(1 – t²).

But

  ∫₀ᵃ dt/√(1 – t²) = arcsin a.

Thus

  I(a) = π · arcsin a    (and the constant of integration vanishes since I(0) = 0).

Step 4. Our final answer.

Returning to our original problem we set a = 1/3 so that

  I = I(1/3) = π · arcsin(1/3).

Step 5. Numerical approximation.

Calculating arcsin(1/3) (in radians) we find

  arcsin(1/3) ≈ 0.3398369094541219,

so

  I ≈ π × 0.3398369094541219 ≈ 1.068329057359.

Rounded to 10 decimal places, this is approximately 1.0683290574.

Thus, the final answers are:

Exact Answer: π·arcsin(1/3)

Numerical Answer: 1.0683290574

{"answer": "$\\pi\\arcsin(1/3)$", "numerical_answer": "1.0683290574"}