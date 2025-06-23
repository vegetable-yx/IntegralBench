We start with the integral

  I = ∫ from x = 1 to 2011 of (√x / (√x + √(2012 - x))) dx.

Step 1. Notice the symmetry. Define
  f(x) = √x / (√x + √(2012 - x)).
Then, examining f(2012 - x), we have
  f(2012 - x) = √(2012 - x) / (√(2012 - x) + √x),
which implies
  f(x) + f(2012 - x) = (√x + √(2012 - x)) / (√x + √(2012 - x)) = 1.

Step 2. Now, consider the integral of 1 over the same interval:
  ∫ from 1 to 2011 of 1 dx = 2011 − 1 = 2010.
Since
  I = ∫ from 1 to 2011 f(x) dx,
and by substituting u = 2012 − x we find that
  ∫ from 1 to 2011 f(2012 - x) dx = I,
it follows that
  I + I = 2010 ⟹ 2I = 2010 ⟹ I = 1005.

Step 3. The exact value of the integral is 1005. The numerical approximation rounded to 10 decimal places is 1005.0000000000.

{"answer": "$1005$", "numerical_answer": "1005.0000000000"}