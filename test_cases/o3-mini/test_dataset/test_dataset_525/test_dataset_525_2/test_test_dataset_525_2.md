We begin with the integral

  I = ∫₁/√2¹ (arcsin x)/(x³) dx.

Step 1. Substitution
Let u = arcsin x. Then,
  x = sin u  and  dx = cos u du.
Also, when x = 1/√2, u = arcsin(1/√2) = π/4; when x = 1, u = arcsin 1 = π/2.

Rewriting the integral in terms of u:
  I = ∫[u=π/4 to π/2] u/(sin³ u) · cos u du.

Step 2. Integration by Parts
Set
  A = u  ⇒ dA = du,
and let
  dB = (cos u/sin³ u) du.
To find B, perform the substitution:
  Let z = sin u, dz = cos u du.
Then,
  B = ∫ (dz/z³) = -1/(2z²) + C = -1/(2 sin² u).

Now apply integration by parts:
  I = [A·B]₍π/4₎^(π/2) - ∫[π/4 to π/2] B dA
    = [ -u/(2 sin² u) ]₍π/4₎^(π/2) + (1/2) ∫[π/4 to π/2] (du/sin² u).

Step 3. Evaluate the Boundary Term
At u = π/2: sin(π/2) = 1, so the term is −(π/2)/(2·1) = −π/4.
At u = π/4: sin(π/4) = √2/2, so sin²(π/4) = 1/2, giving the term −(π/4)/(2·(1/2)) = −(π/4)/1 = −π/4.
Thus, the boundary contribution is:
  [ −u/(2 sin² u) ]₍π/4₎^(π/2) = (−π/4) − (−π/4) = 0.

Step 4. Evaluate the Remaining Integral
Now we have:
  I = (1/2) ∫[π/4 to π/2] du/sin² u.
Recall that ∫ csc² u du = −cot u + C. Thus,
  I = (1/2)[ −cot u ]₍π/4₎^(π/2)
    = (1/2)[ −cot(π/2) + cot(π/4) ].
Since cot(π/2) = 0 and cot(π/4) = 1, we get:
  I = (1/2)[0 + 1] = 1/2.

Step 5. Numerical Approximation
The exact answer is 1/2, which numerically is 0.5. To 10 decimal places, this is 0.5000000000.

Final Answer in JSON format:
{"answer": "\\frac{1}{2}", "numerical_answer": "0.5000000000"}