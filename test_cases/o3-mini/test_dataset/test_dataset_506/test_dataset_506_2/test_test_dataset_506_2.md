We wish to evaluate

  I = ∫₁^(2011) [√x/(√(2012–x) + √x)] dx.

Step 1. Notice that if we make the substitution
  u = 2012 – x  ⟹  du = –dx,
then when x = 1 the new variable u = 2011 and when x = 2011, u = 1. Changing the variable,

  I = ∫ₓ₌₁^(2011) [√x/(√(2012–x)+√x)] dx
     = ∫ᵤ₌₂₀₁₁^(1) [√(2012–u)/(√u+√(2012–u))] (–du)
     = ∫₁^(2011) [√(2012–u)/(√u+√(2012–u))] du.

Let’s denote the new form by I' (with the dummy variable u, which we revert to x for simplicity):

  I' = ∫₁^(2011) [√(2012–x)/(√x+√(2012–x))] dx.

Step 2. Now add the original integral I and this transformed integral I'. We have

  I + I' = ∫₁^(2011) { [√x/(√(2012–x)+√x)] + [√(2012–x)/(√x+√(2012–x))] } dx.

Since the denominators are the same,
  I + I' = ∫₁^(2011) [(√x + √(2012–x))/(√x+√(2012–x))] dx
     = ∫₁^(2011) 1 dx.

Evaluating the right-hand side gives
  I + I' = (2011 – 1) = 2010.

But note that I and I' are the same integral (by the symmetry built into the substitution), so we have

  2I = 2010  ⟹  I = 2010/2 = 1005.

Step 3. Thus, the exact answer is 1005. In numerical form, the value is 1005.0000000000 (rounded to 10 decimal places).

Final Answer in JSON format:
{"answer": "1005", "numerical_answer": "1005.0000000000"}