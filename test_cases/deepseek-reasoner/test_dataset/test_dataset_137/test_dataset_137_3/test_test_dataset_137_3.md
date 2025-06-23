<think>
Okay, let's tackle this integral step by step. The integral given is ∫₀⁴ x^(-1/2) (4 - x)^(-1/2) [1 - 0.25x(4 - x)]^(1/2) dx. Hmm, that looks a bit complicated, but maybe there's a substitution that can simplify it.

First, let me rewrite the integrand to see if I can recognize a pattern. The terms x^(-1/2) and (4 - x)^(-1/2) remind me of the Beta function or maybe an integral related to the Beta distribution. The Beta function typically has the form ∫₀¹ t^{a-1}(1 - t)^{b-1} dt, which is related to the Gamma function. But here, the limits are from 0 to 4, so maybe a substitution can adjust the interval.

Let me try substituting x = 4t. Then, when x=0, t=0, and when x=4, t=1. The differential dx would be 4dt. Let's substitute:

x = 4t ⇒ dx = 4dt

So the integral becomes:

∫₀¹ (4t)^(-1/2) (4 - 4t)^(-1/2) [1 - 0.25*(4t)(4 - 4t)]^(1/2) * 4 dt

Simplify each part:

(4t)^(-1/2) = (4)^(-1/2) * t^(-1/2) = (1/2) t^(-1/2)

(4 - 4t)^(-1/2) = [4(1 - t)]^(-1/2) = (4)^(-1/2) (1 - t)^(-1/2) = (1/2) (1 - t)^(-1/2)

Multiply those two: (1/2)(1/2) t^(-1/2)(1 - t)^(-1/2) = (1/4) t^(-1/2)(1 - t)^(-1/2)

Now the term inside the square root:

1 - 0.25*(4t)(4 - 4t) = 1 - 0.25*(16t - 16t²) = 1 - 4t + 4t²

Wait, 0.25*4t*(4 - 4t) = 0.25*4t(1 - t)*4? Wait, let me compute that again.

Wait, 0.25*(4t)*(4 - 4t) = 0.25*4t*4(1 - t) = 0.25*16t(1 - t) = 4t(1 - t). So:

1 - 4t(1 - t) = 1 - 4t + 4t². Hmm, that's (2t - 1)^2, right? Let's check:

(2t - 1)^2 = 4t² -4t +1. Yes, exactly. So the square root becomes sqrt[(2t -1)^2] = |2t -1|. But since t is between 0 and 1, 2t -1 ranges from -1 to 1. So the absolute value would split the integral into two parts: from t=0 to t=0.5, where 2t -1 is negative, and t=0.5 to t=1, where it's positive. But maybe there's symmetry here.

But wait, the original integral is from x=0 to x=4, which translates to t=0 to t=1. So the integrand becomes:

(1/4) t^(-1/2)(1 - t)^(-1/2) * |2t -1| * 4 dt

Wait, the 4 from dx is multiplied here. Let's recheck:

Original substitution gives us:

Integral becomes:

(1/4) t^(-1/2)(1 - t)^(-1/2) * sqrt(1 - 4t(1 - t)) * 4 dt

Which simplifies to:

(1/4)*4 * t^(-1/2)(1 - t)^(-1/2) * |2t -1| dt = t^(-1/2)(1 - t)^(-1/2) * |2t -1| dt

So the integral is ∫₀¹ t^(-1/2)(1 - t)^(-1/2) |2t -1| dt

Hmm, that's interesting. The integrand is t^(-1/2)(1 - t)^(-1/2) |2t -1|. Let's split the integral at t=0.5.

So, ∫₀¹ becomes ∫₀^0.5 + ∫0.5¹. For t from 0 to 0.5, |2t -1| = 1 - 2t. For t from 0.5 to 1, |2t -1| = 2t -1.

So the integral becomes:

∫₀^0.5 t^(-1/2)(1 - t)^(-1/2)(1 - 2t) dt + ∫0.5^1 t^(-1/2)(1 - t)^(-1/2)(2t -1) dt

But maybe there's a substitution that can combine these. Let's consider the second integral. Let u = 1 - t in the second integral. When t = 0.5, u = 0.5; when t=1, u=0. Then the second integral becomes:

∫0.5^1 t^(-1/2)(1 - t)^(-1/2)(2t -1) dt = ∫0^0.5 (1 - u)^(-1/2) u^(-1/2) (2(1 - u) -1) (-du)

But the (-du) reverses the limits, so:

= ∫0^0.5 u^(-1/2)(1 - u)^(-1/2) (2 - 2u -1) du = ∫0^0.5 u^(-1/2)(1 - u)^(-1/2) (1 - 2u) du

Which is the same as the first integral. Therefore, both integrals are equal. So the total integral is 2 times the first integral. Wait, no. Wait, the first integral is from 0 to 0.5, and the second after substitution becomes the same as the first. So the total integral is 2 times the first integral. Wait, original integral is first integral (0 to 0.5) plus second integral (0.5 to 1). But after substitution, the second integral becomes the same as the first. So total integral is 2 * ∫₀^0.5 t^(-1/2)(1 - t)^(-1/2)(1 - 2t) dt

Wait, no. Let me check again. The first integral is from 0 to 0.5: I1 = ∫₀^0.5 t^{-1/2}(1 - t)^{-1/2}(1 - 2t) dt

The second integral after substitution becomes ∫0^0.5 u^{-1/2}(1 - u)^{-1/2}(1 - 2u) du, which is the same as I1. Therefore, the total integral is I1 + I1 = 2I1. So the original integral is 2I1.

But wait, that can't be right. Wait, the substitution for the second integral: when t = 0.5, u = 0.5, and when t=1, u=0. So the integral becomes from u=0.5 to u=0, which after flipping the limits and changing the sign, becomes from u=0 to u=0.5. So the second integral is equal to ∫0^0.5 u^{-1/2}(1 - u)^{-1/2}(1 - 2u) du, which is I1. Therefore, the total integral is I1 + I1 = 2I1. So the original integral is 2I1.

Therefore, the integral becomes 2 * ∫₀^0.5 t^{-1/2}(1 - t)^{-1/2}(1 - 2t) dt

Hmm, but how do we compute this integral? Let's see. The integrand is t^{-1/2}(1 - t)^{-1/2}(1 - 2t). Let me write this as (1 - 2t) / [sqrt(t(1 - t))]

Alternatively, perhaps we can use substitution. Let me consider another substitution. Let’s set t = sin²θ. Then dt = 2 sinθ cosθ dθ. But maybe that complicates things. Alternatively, note that t(1 - t) is symmetric, and the term (1 - 2t) is antisymmetric around t=0.5. Wait, but we are integrating from 0 to 0.5, so (1 - 2t) is positive here? Wait, when t is from 0 to 0.5, 2t is from 0 to 1, so 1 - 2t is from 1 to 0. So it's positive in this interval.

Alternatively, maybe we can use substitution u = sqrt(t/(1 - t)) or something like that. Let me think. Let’s try substitution u = 2t. Wait, when t is from 0 to 0.5, u is from 0 to 1. Let’s try u = 2t. Then t = u/2, dt = du/2. Then the integral becomes:

2 * ∫₀¹ [ (u/2)^{-1/2} (1 - u/2)^{-1/2} (1 - u) ) ] * (du/2)

Wait, let's compute each term:

t^{-1/2} = (u/2)^{-1/2} = (2/u)^{1/2} = sqrt(2)/sqrt(u)

(1 - t)^{-1/2} = (1 - u/2)^{-1/2} = [ (2 - u)/2 ]^{-1/2} = sqrt(2)/sqrt(2 - u)

(1 - 2t) = 1 - u

dt = du/2

So putting it all together:

2 * ∫₀¹ [ sqrt(2)/sqrt(u) * sqrt(2)/sqrt(2 - u) * (1 - u) ) ] * (du/2)

Simplify constants:

2 * [ sqrt(2) * sqrt(2) / 2 ] ∫₀¹ [1 / sqrt(u(2 - u)) ] * (1 - u) du

sqrt(2)*sqrt(2) = 2, so 2 * (2 / 2) = 2 * 1 = 2. Wait:

Wait, 2 * [ (sqrt(2) * sqrt(2)) / (sqrt(u) * sqrt(2 - u)) ) * (1 - u) * du/2 ]

Wait, the constants: sqrt(2)/sqrt(u) * sqrt(2)/sqrt(2 - u) = 2 / sqrt(u(2 - u))

Then multiplied by (1 - u) and dt is du/2. So the integral becomes:

2 * ∫₀¹ [2 / sqrt(u(2 - u))] * (1 - u) * (du/2) = 2 * [ (2 * du/2) / sqrt(u(2 - u)) * (1 - u) ]

The 2 and 1/2 cancel, so:

2 * ∫₀¹ (1 - u) / sqrt(u(2 - u)) du = 2 ∫₀¹ (1 - u) / sqrt(u(2 - u)) du

Hmm, not sure if this helps. Maybe another substitution. Let’s set v = u - 1, but that might not help. Alternatively, complete the square in the denominator. The denominator sqrt(u(2 - u)) = sqrt(2u - u²) = sqrt(1 - (u -1)^2). Let me check:

2u - u² = -u² + 2u = -(u² - 2u) = -(u² - 2u +1 -1) = -(u -1)^2 +1 = 1 - (u -1)^2. Yes! So sqrt(2u - u²) = sqrt(1 - (u -1)^2). So the integral becomes:

2 ∫₀¹ (1 - u) / sqrt(1 - (u -1)^2) du

Let’s make substitution w = u -1. Then dw = du, and when u=0, w=-1; u=1, w=0. So the integral becomes:

2 ∫_{-1}^0 (1 - (w +1)) / sqrt(1 - w²) dw = 2 ∫_{-1}^0 (-w) / sqrt(1 - w²) dw

Simplify the numerator: 1 - (w +1) = -w. So:

2 ∫_{-1}^0 (-w)/sqrt(1 - w²) dw = 2 ∫_{-1}^0 (-w)/sqrt(1 - w²) dw

Let’s reverse the limits by substituting w = -v, v from 0 to1:

= 2 ∫₀¹ (-(-v))/sqrt(1 - (-v)^2) dv = 2 ∫₀¹ v / sqrt(1 - v²) dv

That's a standard integral. The integral of v / sqrt(1 - v²) dv is -sqrt(1 - v²) + C. Let me check:

Let’s = sqrt(1 - v²), then ds/dv = (-v)/sqrt(1 - v²). So ∫ v / sqrt(1 - v²) dv = -sqrt(1 - v²) + C.

Therefore, the integral becomes:

2 [ -sqrt(1 - v²) ] from 0 to1 = 2 [ -sqrt(1 -1) + sqrt(1 -0) ] = 2 [ 0 +1 ] = 2*1 =2

Wait, so the integral evaluates to 2? But let me check the steps because that seems too straightforward.

Wait, let's recap:

Original integral after substitution x=4t became 2 times ∫₀^0.5 t^{-1/2}(1 - t)^{-1/2}(1 - 2t) dt. Then through substitutions, we transformed it into 2 * 1 =2. So the original integral is 2. But let me verify with numerical approximation. Let's see, if the integral is 2, then the numerical approximation would be 2.0000000000. But let me check with a different approach.

Alternatively, let's consider the Beta function. The original integral after substitution x=4t is:

∫₀¹ t^{-1/2}(1 - t)^{-1/2} |2t -1| dt. But we split it and found it equals 2. Alternatively, maybe there's a mistake in the substitution steps.

Wait, let's check the substitution steps again. Let me go back to the integral after substitution x=4t:

Integral becomes ∫₀¹ (1/4) t^{-1/2}(1 - t)^{-1/2} sqrt(1 -4t +4t²) *4 dt = ∫₀¹ t^{-1/2}(1 - t)^{-1/2} sqrt{(2t -1)^2} dt = ∫₀¹ t^{-1/2}(1 - t)^{-1/2} |2t -1| dt

Then splitting into two parts:

∫₀^0.5 t^{-1/2}(1 - t)^{-1/2}(1 -2t) dt + ∫0.5^1 t^{-1/2}(1 - t)^{-1/2}(2t -1) dt

Then, as we did before, substituting u=1 -t in the second integral, which becomes ∫0.5^1 ... = ∫0^0.5 ... which is same as the first integral, so total integral is 2 times the first integral. Then through substitution, we found that the integral equals 2. So the original integral is 2. But let me check with a numerical approximation.

Let me compute the original integral numerically. Let's take x from 0 to4, and compute x^{-1/2}(4 -x)^{-1/2}[1 -0.25x(4 -x)]^{1/2} dx. Let's pick some points. For example, at x=1, the integrand is 1^{-1/2} *3^{-1/2} * sqrt(1 -0.25*1*3) =1 * 1/sqrt(3) * sqrt(1 - 0.75) = 1/sqrt(3) * sqrt(0.25) = 1/sqrt(3) *0.5 ≈0.2887. At x=2, integrand is (2)^{-1/2}*(2)^{-1/2} * sqrt(1 -0.25*2*2) = (1/2) * sqrt(1 -1) = (1/2)*0=0. At x=0.5, integrand is (0.5)^{-1/2}*(3.5)^{-1/2} * sqrt(1 -0.25*0.5*3.5). Let's compute:

(0.5)^{-1/2} = sqrt(2) ≈1.4142

(3.5)^{-1/2} ≈1/sqrt(3.5) ≈0.5345

So product: 1.4142 *0.5345 ≈0.756

Inside the sqrt: 1 -0.25*0.5*3.5 =1 -0.25*1.75=1 -0.4375=0.5625. sqrt(0.5625)=0.75. So total integrand at x=0.5: 0.756 *0.75≈0.567.

But integrating from 0 to4, the integrand is symmetric around x=2? Wait, when x approaches 0, the integrand behaves like x^{-1/2} *4^{-1/2} * sqrt(1 -0) = x^{-1/2}*(1/2)*1, so integrand ~ (1/2) x^{-1/2}, which is integrable. Similarly near x=4, behaves like (4 -x)^{-1/2}*(1/2)*sqrt(1 -0.25*4*(0))= (4 -x)^{-1/2}*(1/2)*1, which is also integrable. So the integral is finite. If the analytical result is 2, then the numerical approximation should be 2.0000000000. But let me check with substitution.

Alternatively, perhaps there's a better substitution. Let me think again. The original integral is ∫₀⁴ x^{-1/2}(4 -x)^{-1/2} sqrt{1 -0.25x(4 -x)} dx.

Let me make substitution y = x/4, so x=4y, dx=4dy. Then the integral becomes:

∫₀¹ (4y)^{-1/2}(4 -4y)^{-1/2} sqrt{1 -0.25*(4y)(4 -4y)} *4 dy

Simplify:

(4y)^{-1/2} = (4)^{-1/2} y^{-1/2} = (1/2) y^{-1/2}

(4 -4y)^{-1/2} = (4(1 - y))^{-1/2} = (1/2) (1 - y)^{-1/2}

Multiply those: (1/2)(1/2) y^{-1/2}(1 - y)^{-1/2} = (1/4) y^{-1/2}(1 - y)^{-1/2}

Inside the sqrt: 1 -0.25*(4y)(4 -4y) =1 -0.25*16y(1 - y) =1 -4y(1 - y) =1 -4y +4y² = (2y -1)^2

So sqrt{(2y -1)^2} = |2y -1|

Then the integral becomes:

(1/4) * |2y -1| *4 dy = ∫₀¹ y^{-1/2}(1 - y)^{-1/2} |2y -1| dy

Which is the same as before. So the integral is ∫₀¹ y^{-1/2}(1 - y)^{-1/2} |2y -1| dy. As before, split into two intervals. Then through substitution, we found that the integral equals 2. So the original integral is 2. Therefore, the exact answer is 2. The numerical approximation is 2.0000000000.

But let me verify with another approach. Let's consider the Beta function. The integral ∫₀¹ t^{c-1}(1 - t)^{d-1} dt = B(c, d) = Γ(c)Γ(d)/Γ(c + d). But in our case, the integrand is t^{-1/2}(1 - t)^{-1/2} |2t -1|. Hmm, but the presence of |2t -1| complicates things. However, we can express |2t -1| as a combination of terms that can be expressed via Beta functions.

Alternatively, note that the integral ∫₀¹ t^{-1/2}(1 - t)^{-1/2} |2t -1| dt can be expressed as ∫₀¹ |2t -1| / sqrt(t(1 - t)) dt. Let me consider substitution u = 2t -1. Then t = (u +1)/2, dt = du/2. When t=0, u=-1; t=1, u=1. So the integral becomes:

∫_{-1}^1 |u| / sqrt( [(u +1)/2] [1 - (u +1)/2 ]) * (du/2)

Simplify the denominator:

[(u +1)/2] [1 - (u +1)/2 ] = [(u +1)/2] [ (1 - u)/2 ] = (1 - u²)/4

So sqrt of that is sqrt(1 - u²)/2. Therefore, the integral becomes:

∫_{-1}^1 |u| / (sqrt(1 - u²)/2) * (du/2) = ∫_{-1}^1 |u| * 2 / sqrt(1 - u²) * (du/2) = ∫_{-1}^1 |u| / sqrt(1 - u²) du

Since the integrand is even function (|u| is even, sqrt(1 - u²) is even), so integral from -1 to1 is 2 times integral from 0 to1:

2 ∫₀¹ u / sqrt(1 - u²) du

Let’s compute this integral. Let substitution v =1 - u², dv = -2u du ⇒ -dv/2 = u du. Then:

∫ u / sqrt(1 - u²) du = ∫ (1/ sqrt(v)) (-dv/2) = -1/2 ∫ v^{-1/2} dv = -1/2 * 2 v^{1/2} + C = -sqrt(v) + C = -sqrt(1 - u²) + C

Evaluated from 0 to1:

[ -sqrt(1 -1) + sqrt(1 -0) ] = 0 +1 =1

So the integral becomes 2 *1 =2. Therefore, the original integral is indeed 2. So the exact answer is 2, and the numerical approximation is 2.0000000000.
</think>

{"answer": "2", "numerical_answer": "2.0000000000"}