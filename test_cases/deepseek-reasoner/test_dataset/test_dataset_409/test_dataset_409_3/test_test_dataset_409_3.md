<think>
Okay, so I need to compute the definite integral of arctan(x² - x + 1) from 0 to 1. Hmm, arctangent integrals can be tricky. Let me start by recalling some integration techniques. Maybe integration by parts? Since the integrand is arctan of a quadratic function, that might be a way to go.

Let me set u = arctan(x² - x + 1) and dv = dx. Then du would be the derivative of arctan(x² - x + 1) times dx, and v would be x. The integration by parts formula is ∫u dv = uv - ∫v du. Let's compute du first.

The derivative of arctan(u) is 1/(1 + u²) times the derivative of u. So here, u = x² - x + 1, so du/dx = 2x - 1. Therefore, du = (2x - 1)/(1 + (x² - x + 1)²) dx. Hmm, that looks complicated. So the integral becomes x * arctan(x² - x + 1) evaluated from 0 to 1 minus the integral from 0 to 1 of x*(2x - 1)/(1 + (x² - x + 1)²) dx.

Let me compute the boundary term first. At x=1: 1 * arctan(1² -1 +1) = arctan(1) = π/4. At x=0: 0 * arctan(0 -0 +1) = 0. So the boundary term is π/4 - 0 = π/4. So now the integral is π/4 minus the integral of x*(2x -1)/(1 + (x² -x +1)^2) dx from 0 to1. Let me denote this remaining integral as I.

So I need to compute I = ∫₀¹ [x*(2x -1)] / [1 + (x² -x +1)^2] dx. Let me simplify the denominator first. Let's compute (x² -x +1)^2. Expanding that: (x² -x +1)^2 = x^4 - 2x³ + 3x² - 2x +1. So the denominator becomes 1 + x^4 - 2x³ + 3x² - 2x +1 = x^4 -2x³ +3x² -2x +2. Hmm, that's a quartic polynomial. Not sure if it factors.

Alternatively, maybe there's a substitution that can simplify this. Let me look at the numerator: x*(2x -1) = 2x² -x. Let me see if the numerator is related to the derivative of the denominator. Let's compute the derivative of the denominator: d/dx [x^4 -2x³ +3x² -2x +2] = 4x³ -6x² +6x -2. Hmm, not the same as the numerator. But maybe there's a linear combination or something.

Alternatively, perhaps the denominator can be rewritten in terms of (x² -x +1). Let me note that x² -x +1 is a quadratic. Let me set t = x² -x +1. Then dt/dx = 2x -1. Wait, the numerator is 2x² -x. Let me see if I can express 2x² -x in terms of t and dt/dx.

Let me note that 2x² -x = x*(2x -1). Since dt/dx = 2x -1, then 2x -1 = dt/dx, so 2x² -x = x*(dt/dx). Hmm, but integrating x*(dt/dx) dx. Maybe integration by parts again? Wait, but if t = x² -x +1, then x = (t -1 +x)/x? Not sure. Alternatively, maybe express x in terms of t and dt/dx.

Alternatively, let's try substitution. Let me set t = x² -x +1. Then dt = (2x -1) dx. But the numerator is x*(2x -1) dx, which is x dt. So I = ∫ [x dt] / (1 + t²). But x is expressed in terms of t. Hmm, this might not be straightforward. Let's see. If t = x² -x +1, then solving for x in terms of t is a quadratic equation: x² -x + (1 - t) = 0. The solutions would be x = [1 ± sqrt(1 -4(1 - t))]/2 = [1 ± sqrt(4t -3)]/2. That seems complicated. Maybe not helpful.

Alternatively, perhaps split the numerator. Let me write 2x² -x as a combination of the derivative of the denominator and something else. Let me see:

Denominator D = x^4 -2x³ +3x² -2x +2. Its derivative D' = 4x³ -6x² +6x -2. The numerator is 2x² -x. Hmm, not directly related. Maybe try to express 2x² -x as a linear combination of D' and lower degree terms. Let me see:

Suppose 2x² -x = A*D' + Bx + C. Let's compute A*D' + Bx + C. Let me pick A as a constant. Let's see:

If A = something, but this might not be straightforward. Alternatively, maybe partial fractions? But the denominator is a quartic, which might not factor nicely. Let me check if the denominator factors. Let me try to factor D = x^4 -2x³ +3x² -2x +2.

Trying rational roots. Possible rational roots are ±1, ±2. Let's test x=1: 1 -2 +3 -2 +2 = 2 ≠0. x=-1: 1 +2 +3 +2 +2=10≠0. So no rational roots. Maybe it factors into quadratics. Suppose D = (x² + ax + b)(x² + cx + d). Then expanding:

x^4 + (a + c)x³ + (b + d + ac)x² + (ad + bc)x + bd. Comparing coefficients:

x^4 -2x³ +3x² -2x +2. So:

a + c = -2

b + d + ac = 3

ad + bc = -2

bd = 2

We need to solve this system. Let's try possible integer factors for bd=2. So possible (b,d) = (1,2), (2,1), (-1,-2), (-2,-1). Let's try b=1, d=2. Then:

From a + c = -2.

From ad + bc = a*2 + c*1 = -2. So 2a + c = -2. But since a + c = -2, subtract: (2a + c) - (a + c) = a = 0. Then a=0, so c=-2. Then check b + d + ac =1 +2 +0=3. Which matches. So yes, D factors as (x² +0x +1)(x² -2x +2) = (x² +1)(x² -2x +2). Great! So denominator factors into (x² +1)(x² -2x +2). That's a big step.

So now, the integral I is ∫₀¹ (2x² -x)/[(x² +1)(x² -2x +2)] dx. Now, we can use partial fractions. Let me set up the integrand as (2x² -x)/[(x² +1)(x² -2x +2)] = (Ax + B)/(x² +1) + (Cx + D)/(x² -2x +2). Let's find A, B, C, D.

Multiply both sides by (x² +1)(x² -2x +2):

2x² -x = (Ax + B)(x² -2x +2) + (Cx + D)(x² +1)

Expand the right-hand side:

(Ax + B)(x² -2x +2) = Ax³ -2Ax² +2Ax + Bx² -2Bx +2B

(Cx + D)(x² +1) = Cx³ + Cx + Dx² + D

Combine like terms:

x³ terms: A + C

x² terms: (-2A + B + D)

x terms: (2A -2B + C)

constant terms: 2B + D

Set equal to left-hand side 2x² -x, which is 0x³ +2x² -1x +0. So equate coefficients:

x³: A + C = 0

x²: -2A + B + D = 2

x: 2A -2B + C = -1

constant: 2B + D = 0

Now solve the system of equations.

From x³: C = -A

From constant: D = -2B

Substitute C = -A and D = -2B into the other equations.

x² equation: -2A + B + (-2B) = 2 → -2A - B = 2

x equation: 2A -2B + (-A) = -1 → A -2B = -1

So we have:

-2A - B = 2

A - 2B = -1

Let me solve these two equations. Let's write them:

1) -2A - B = 2

2) A - 2B = -1

Multiply equation 2 by 2: 2A -4B = -2

Add to equation 1: (-2A - B) + (2A -4B) = 2 + (-2) → -5B = 0 → B = 0

Then from equation 2: A - 0 = -1 → A = -1

Then C = -A = 1

From D = -2B = 0

So the partial fractions decomposition is:

( (-1)x + 0 )/(x² +1) + (1x + 0)/(x² -2x +2) = (-x)/(x² +1) + x/(x² -2x +2)

Therefore, integral I becomes:

∫₀¹ [ -x/(x² +1) + x/(x² -2x +2) ] dx

Let's split this into two integrals:

I = -∫₀¹ x/(x² +1) dx + ∫₀¹ x/(x² -2x +2) dx

Compute each integral separately.

First integral: ∫ x/(x² +1) dx. Let me substitute u = x² +1, du = 2x dx. Then (1/2) du = x dx. So integral becomes (1/2) ∫ du/u = (1/2) ln|u| + C = (1/2) ln(x² +1) + C. Evaluated from 0 to1: (1/2)(ln(2) - ln(1)) = (1/2) ln2.

So first term is - (1/2) ln2.

Second integral: ∫₀¹ x/(x² -2x +2) dx. Let me complete the square in the denominator: x² -2x +2 = (x -1)^2 +1. So the integral becomes ∫ x / [(x -1)^2 +1] dx. Let me substitute t = x -1, so x = t +1, dx = dt. When x=0, t=-1; x=1, t=0. So integral becomes ∫_{-1}^0 (t +1)/(t² +1) dt. Split into two terms: ∫_{-1}^0 t/(t² +1) dt + ∫_{-1}^0 1/(t² +1) dt.

First part: ∫ t/(t² +1) dt. Let u = t² +1, du = 2t dt. So (1/2) du/u. Integral is (1/2) ln|u| + C. Evaluated from t=-1 to 0: (1/2)(ln(1) - ln(2)) = - (1/2) ln2.

Second part: ∫_{-1}^0 1/(t² +1) dt = arctan(t) from -1 to0 = arctan(0) - arctan(-1) = 0 - (-π/4) = π/4.

So the second integral becomes (-1/2 ln2) + π/4.

Putting it all together, the integral I is:

- (1/2 ln2) + [ (-1/2 ln2) + π/4 ] = - (1/2 +1/2) ln2 + π/4 = -ln2 + π/4.

Therefore, the original integral was π/4 - I = π/4 - (-ln2 + π/4) = π/4 + ln2 - π/4 = ln2.

Wait, that's interesting. So the integral from 0 to1 of arctan(x² -x +1) dx equals ln2. Let me verify this because that seems surprisingly simple. Let me check the steps again.

Original integral: ∫₀¹ arctan(x² -x +1) dx. Integration by parts gives π/4 - I. Then I was computed as -ln2 + π/4. So π/4 - (-ln2 + π/4) = ln2. Yes, that's correct. So the exact answer is ln2. For the numerical approximation, ln2 is approximately 0.6931471806. Rounded to 10 decimal places, that's 0.6931471806.

But let me confirm with a numerical check. Let me compute the integral numerically. For example, using a calculator or approximate integration. Let me take x=0: arctan(0 -0 +1)=arctan(1)=π/4≈0.7854. At x=1: arctan(1 -1 +1)=arctan(1)=π/4. The function is arctan of a quadratic. The integral from 0 to1 of this function is ln2≈0.6931. That seems plausible. Let me check with a simple approximation. The average of the function at endpoints and midpoint: maybe trapezoidal rule. Let's compute at x=0.5: arctan(0.25 -0.5 +1)=arctan(0.75)≈0.6435. The trapezoidal estimate with n=2: (0.7854 + 0.6435)/2 *1 ≈ (1.4289)/2 ≈0.71445. Simpson's rule would be (0.7854 +4*0.6435 +0.7854)/6 ≈ (0.7854 +2.574 +0.7854)/6 ≈4.1448/6≈0.6908, which is close to ln2≈0.6931. So that seems to confirm the analytical result is correct.
</think>

{"answer": "\\ln 2", "numerical_answer": "0.6931471806"}