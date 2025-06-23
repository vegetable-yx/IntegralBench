To evaluate

  I = ∫ from –1 to 1 [sin(√x) / (sinh(√x) + sin(√x))] dx,

we need to interpret the square root for negative x. For x ≥ 0 the square root is the usual nonnegative real number, whereas for x < 0 we use the principal branch. In particular, for t > 0 one has

  √(–t) = i√t.

Thus, if x = –t (with t ∈ [0, 1]), then

  sin(√(–t)) = sin(i√t) = i sinh(√t)
  sinh(√(–t)) = sinh(i√t) = i sin(√t).

It is convenient to break the integral into two parts:

  I = ∫ from –1 to 0 f(x) dx + ∫ from 0 to 1 f(x) dx
     where f(x) = sin(√x)/(sinh(√x) + sin(√x)).

Change variable in the first part using t = –x (so that when x goes from –1 to 0, t goes from 1 to 0). We then have dx = –dt and

  I₁ = ∫ from x = –1 to 0 f(x) dx
     = ∫ from t = 1 to 0 f(–t)(–dt)
     = ∫ from 0 to 1 f(–t) dt.

Now substitute using the formulas for negative arguments:

  f(–t) = sin(√(–t))/(sinh(√(–t)) + sin(√(–t)))
     = [i sinh(√t)] / [i sin(√t) + i sinh(√t)]
     = sinh(√t) / [sin(√t) + sinh(√t)].

The second part of the integral is

  I₂ = ∫ from 0 to 1 sin(√x)/(sinh(√x) + sin(√x)) dx.

Thus, the total integral becomes

  I = I₁ + I₂
     = ∫ from 0 to 1 { sinh(√t)/(sin(√t) + sinh(√t)) + sin(√t)/(sin(√t) + sinh(√t)) } dt
     = ∫ from 0 to 1 { [sinh(√t) + sin(√t)]/(sin(√t) + sinh(√t)) } dt
     = ∫ from 0 to 1 1 dt
     = 1.

Thus, the analytical (exact) answer is 1.

A numerical approximation to 10 decimal places is 1.0000000000.

{"answer": "1", "numerical_answer": "1.0000000000"}