We wish to evaluate

  I = ∫₀² x^(1/2) (2 – x)^(–1/2) · arcsin(0.5·√[x(2 − x)]) dx.

A good idea is to introduce a substitution that “symmetrizes” the factors. In fact, letting

  x = 2 sin²θ      (so that 0 ≤ θ ≤ π/2)
  ⇒ 2 – x = 2 cos²θ,
  √x = √2 sinθ   and √(2 – x) = √2 cosθ.
Also note that
  √[x(2 – x)] = √(2 sin²θ · 2 cos²θ) = 2 sinθ cosθ = sin(2θ)
and the differential is
  dx = 4 sinθ cosθ dθ.

Now rewrite the factors in the integrand. Observe that

  x^(1/2)(2 – x)^(–1/2) = (√2 sinθ)/(√(2 cos²θ)) = tanθ.
Moreover, the factor inside the arcsine becomes
  0.5·√[x(2 – x)] = 0.5 sin(2θ) = sinθ cosθ.
Thus the integrand transforms into

  I = ∫₀^(π/2) [tanθ · arcsin(sinθ cosθ)] · [4 sinθ cosθ dθ]
     = ∫₀^(π/2) 4 sinθ cosθ · tanθ · arcsin(sinθ cosθ) dθ.
But since tanθ = sinθ/cosθ the product simplifies as
  tanθ · 4 sinθ cosθ = 4 sin²θ.
Thus
  I = 4∫₀^(π/2) sin²θ · arcsin(sinθ cosθ) dθ.
Noting that sinθ cosθ = (1/2) sin(2θ), we can rewrite
  arcsin(sinθ cosθ) = arcsin((1/2) sin 2θ).

It is now convenient to change the variable by setting

  u = 2θ,   so that θ = u/2   and dθ = du/2,
and the limits become u = 0 to u = π. Also,
  sin²θ = sin²(u/2) = (1 – cos u)/2.
Thus the integral becomes

  I = 4 ∫₀^(π/2) sin²θ · arcsin((1/2) sin 2θ) dθ
    = 4 ∫₀^(π) sin²(u/2) · arcsin((1/2) sin u) · (du/2)
    = 2 ∫₀^(π) sin²(u/2) · arcsin((1/2) sin u) du
    = 2 ∫₀^(π) [ (1 – cos u)/2 ] · arcsin((1/2) sin u) du
    = ∫₀^(π) [1 – cos u] · arcsin((1/2) sin u) du.
That is, we may write I as the difference of two integrals:
  I = ∫₀^(π) arcsin((1/2) sin u) du – ∫₀^(π) cos u · arcsin((1/2) sin u) du.
Notice now that the second term is very conveniently handled by the substitution
  t = sin u  (with dt = cos u du);
when u runs from 0 to π, t goes from 0 to 0. (Even though the limits are the same, one may show by symmetry that this term vanishes.) Hence,
  I = ∫₀^(π) arcsin((1/2) sin u) du.
Thus the problem is reduced to evaluating
  J = ∫₀^(π) arcsin((1/2) sin u) du.

A useful technique is to introduce a parameter. For 0 ≤ a ≤ 1 define
  F(a) = ∫₀^(π) arcsin(a sin u) du.
Then, differentiating with respect to a (and interchanging differentiation and integration when justified),
  F′(a) = ∫₀^(π) [sin u/√(1 – a² sin² u)] du.
Because the integrand is symmetric about u = π/2 one may write
  F′(a) = 2 ∫₀^(π/2) [sin u/√(1 – a² sin² u)] du.
A change of variable (for example, t = cos u) shows that this integral can be evaluated in closed‐form. One finds
  F′(a) = (2/a) sinh⁻¹( a/√(1 – a²) )
      = (2/a) ln((1 + a)/√(1 – a²)).
One may then integrate with respect to a and check that F(0) = 0; the result is
  F(a) = Li₂(a) – Li₂(–a),
where Li₂ denotes the dilogarithm function. (One may verify by differentiating that the derivative of Li₂(a) – Li₂(–a) is the expression above.) In our case a = 1/2 so that
  J = F(1/2) = Li₂(1/2) – Li₂(–1/2).

Thus we have shown that
  I = Li₂(1/2) – Li₂(–1/2).

Numerically one may check that
  Li₂(1/2) ≈ 0.5822405264650125   and  Li₂(–1/2) ≈ –0.4484142069236460,
so that
  I ≈ 0.5822405264650125 – (–0.4484142069236460) ≈ 1.0306547333886585.
Rounded to 10 decimal places the numerical value is 1.0306547334.

The final answer is therefore given in exact form by
  I = Li₂(1/2) – Li₂(–1/2)
with numerical value approximately 1.0306547334.

{"answer": "$\\operatorname{Li}_2\\left(\\frac{1}{2}\\right)-\\operatorname{Li}_2\\left(-\\frac{1}{2}\\right)$", "numerical_answer": "1.0306547334"}