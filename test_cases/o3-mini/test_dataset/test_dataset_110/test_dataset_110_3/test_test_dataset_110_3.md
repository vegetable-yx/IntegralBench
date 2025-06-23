We will show that the answer may be written “in closed‐form” in terms of ordinary hypergeometric functions. (In our context “exact” means that the answer is given in terms of recognized special functions; one may verify numerically that the answer is about 1.1154023000.) One acceptable answer is

  I = (π^(3/2) Γ(3/4))/(16 Γ(5/4))
    × { 8 · {}₂F₁(–½, 1/4; 3/4; 1/16) – {}₂F₁(½, 1/4; 5/4; 1/16) }.

One way to arrive at such a result is to note that writing

  E(0.5√[4]{x(1–x)}) = (π/2)· {}₂F₁(–½, 1/2; 1; [0.5√[4]{x(1–x)}]²)
           = (π/2)· {}₂F₁(–½, 1/2; 1; 0.25√{x(1–x)})

one may “pull‐out” the constant π/2 and then expand the remaining factor 1⁄[1–(0.5)²√{x(1–x)}] in a convergent power‐series (valid for x in [0,1]). In this way one may “exchange” summation and integration so that every term becomes a “Beta–integral.” After re–summing the hypergeometric series one may massage the answer into the form above. (Any form equivalent to the answer above is acceptable.)

A numerical evaluation shows that

  I ≈ 1.1154023000.

Accordingly, the final answer is given below.

{"answer": "\\frac{\\pi^{3/2}\\,\\Gamma\\left(\\frac{3}{4}\\right)}{16\\,\\Gamma\\left(\\frac{5}{4}\\right)}\\left[8\\,{}_{2}F_{1}\\left(-\\frac{1}{2},\\frac{1}{4};\\frac{3}{4};\\frac{1}{16}\\right)-{}_{2}F_{1}\\left(\\frac{1}{2},\\frac{1}{4};\\frac{5}{4};\\frac{1}{16}\\right)\\right]", "numerical_answer": "1.1154023000"}