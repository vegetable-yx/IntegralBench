We wish to evaluate

  I = ∫ from x=1/√2 to x=1 (arcsin(x))/(x³) dx.

Step 1. Change of variable

Let
  u = arcsin(x)  ⇒  x = sin(u).
Then
  dx = cos(u) du.
The limits change as follows:
  When x = 1/√2, then u = arcsin(1/√2) = π/4.
  When x = 1, then u = arcsin(1) = π/2.
Substitute into the integral:
  I = ∫ from u=π/4 to u=π/2 [u/(sin³(u))] · cos(u) du = ∫ from π/4 to π/2 [u cos(u)/sin³(u)] du.

Step 2. Integration by parts

Choose:
  f(u) = u  →  f′(u) = 1,
and
  g′(u) = cos(u)/sin³(u).
We now need to find a function g(u) satisfying g′(u) = cos(u)/sin³(u). Notice that
  d/du [–1/(2 sin²(u))] = (1/(2))·(2 cos(u))/(sin³(u)) = cos(u)/sin³(u).
Thus, we set:
  g(u) = – 1/(2 sin²(u)).

Now, by integration by parts,
  ∫ f(u) g′(u) du = f(u)g(u) – ∫ g(u) f′(u) du.
Hence,
  I = [ u · (–1/(2 sin²(u)))] from u=π/4 to u=π/2 – ∫ from π/4 to π/2 (–1/(2 sin²(u))) du.
That is,
  I = –[ u/(2 sin²(u))] | from π/4 to π/2 + 1/2 ∫ from π/4 to π/2 du/sin²(u).

Step 3. Evaluate the boundary term

Compute the boundary term:
  At u = π/2: sin(π/2) = 1, so sin²(π/2) = 1. Thus, term = – (π/2)/(2·1) = –π/4.
  At u = π/4: sin(π/4) = 1/√2, so sin²(π/4) = 1/2. Thus, term = – (π/4)/(2·(1/2)) = – (π/4)/1 = –π/4.
Then the difference is:
  [–π/4] – [–π/4] = 0.

Step 4. Evaluate the remaining integral

Now, we have
  I = 0 + (1/2) ∫ from π/4 to π/2 du/sin²(u).
Recall that
  ∫ du/sin²(u) = –cot(u).
Thus,
  I = 1/2 · [ –cot(u)] evaluated from u = π/4 to u = π/2.
That is,
  I = 1/2 · ( [–cot(π/2)] – [–cot(π/4)] ) = 1/2 · ( –cot(π/2) + cot(π/4) ).
We find:
  cot(π/2) = cos(π/2)/sin(π/2) = 0/1 = 0,
  cot(π/4) = 1.
Therefore,
  I = 1/2 · (0 + 1) = 1/2.

Step 5. Numerical approximation

The exact evaluated result is 1/2, which numerically is 0.5. Rounding to 10 decimal places gives 0.5000000000.

Final Answer in JSON format:
{"answer": "\\frac{1}{2}", "numerical_answer": "0.5000000000"}