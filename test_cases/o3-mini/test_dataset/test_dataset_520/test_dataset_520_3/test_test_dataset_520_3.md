We wish to compute
  I = ∫₀^(2π) tan(cos x) dx.

Step 1. Notice that the cosine function is shifted symmetric about π. In fact, if we set
  u = x – π,
then
  cos x = cos(u + π) = –cos u.
Thus,
  tan(cos x) = tan(–cos u) = –tan(cos u).

Step 2. Change the limits of integration accordingly. When x = 0, then u = –π; when x = 2π, then u = π. So the integral becomes
  I = ∫₋π^(π) tan(cos(u + π)) du = ∫₋π^(π) [–tan(cos u)] du = –∫₋π^(π) tan(cos u) du.

Step 3. Notice that the rewritten integrals are the same (u is simply a dummy variable):
  I = –∫₋π^(π) tan(cos u) du.
But we also have
  I = ∫₋π^(π) tan(cos u) du
(by simply reinterpreting the original integral over a full period). Therefore,
  I = –I,
which implies that
  I = 0.

Step 4. Numerical approximation:
  0 (to 10 decimal places, 0.0000000000).

Thus, the exact answer is 0 and the numerical approximation is 0.0000000000.

{"answer": "0", "numerical_answer": "0.0000000000"}