<think>
Okay, so I need to compute the definite integral from 1 to 2011 of sqrt(x) divided by (sqrt(2012 - x) + sqrt(x)) dx. Hmm, that looks a bit tricky at first glance. Let me think about how to approach this.

I remember that sometimes when you have an integrand with symmetric terms in the denominator, like sqrt(a - x) and sqrt(x), a substitution might help. Maybe substituting x with something that swaps the terms in the denominator? Let me try substituting x with 2012 - t. Let's see if that works.

Let t = 2012 - x. Then, when x = 1, t = 2012 - 1 = 2011, and when x = 2011, t = 2012 - 2011 = 1. So the limits of integration will switch places. Also, dx = -dt, so the integral becomes the integral from t=2011 to t=1 of sqrt(2012 - t) / (sqrt(t) + sqrt(2012 - t)) * (-dt). Flipping the limits to go from 1 to 2011, the negative sign cancels out, so we have the integral from 1 to 2011 of sqrt(2012 - t) / (sqrt(t) + sqrt(2012 - t)) dt.

But the original integral is sqrt(x)/(sqrt(2012 - x) + sqrt(x)) dx. So if I call the original integral I, then after substitution, the new integral is the same as I but with sqrt(2012 - x) in the numerator. Let me write that:

Original integral: I = ∫₁²⁰¹¹ [sqrt(x)/(sqrt(2012 - x) + sqrt(x))] dx

After substitution: I = ∫₁²⁰¹¹ [sqrt(2012 - x)/(sqrt(x) + sqrt(2012 - x))] dx

Wait, but that's the same as the original integrand but with numerator and denominator terms swapped. Wait, no, the denominator is the same. So if I add the original integral and the substituted integral, I get:

I + I = ∫₁²⁰¹¹ [sqrt(x) + sqrt(2012 - x)] / [sqrt(2012 - x) + sqrt(x)] dx

Which simplifies to ∫₁²⁰¹¹ 1 dx, because the numerator and denominator are the same. So 2I = ∫₁²⁰¹¹ 1 dx = 2011 - 1 = 2010. Therefore, I = 2010 / 2 = 1005. So the integral is 1005. That seems too straightforward. Let me check if I did that correctly.

Wait, so the substitution step: when I set t = 2012 - x, then x = 2012 - t. So sqrt(x) becomes sqrt(2012 - t), and sqrt(2012 - x) becomes sqrt(t). Then the denominator becomes sqrt(t) + sqrt(2012 - t). So the integrand after substitution is sqrt(2012 - t)/(sqrt(t) + sqrt(2012 - t)) dt. So when I add the original integral and the substituted integral, the sum is ∫ [sqrt(x) + sqrt(2012 - x)] / [sqrt(2012 - x) + sqrt(x)] dx from 1 to 2011, which is indeed ∫1 dx from 1 to 2011. So 2I = 2010, so I = 1005. That seems correct. So the exact answer is 1005.

But wait, let me verify with a simpler case. Suppose the integral is from a to b of sqrt(x)/(sqrt(a + b - x) + sqrt(x)) dx. Then using the same substitution x = a + b - t, the integral becomes ∫ from b to a of sqrt(a + b - t)/(sqrt(t) + sqrt(a + b - t)) (-dt) = ∫ from a to b of sqrt(a + b - t)/(sqrt(t) + sqrt(a + b - t)) dt. Then adding the original and substituted integrals gives ∫ from a to b of [sqrt(x) + sqrt(a + b - x)] / [sqrt(a + b - x) + sqrt(x)] dx = ∫ from a to b of 1 dx = b - a. Therefore, 2I = b - a, so I = (b - a)/2. So in our case, a = 1, b = 2011, so the integral is (2011 - 1)/2 = 2010/2 = 1005. So yes, the general case gives that result. Therefore, the exact answer is 1005.

For the numerical approximation, since 1005 is an integer, the numerical approximation is exactly 1005.0000000000. But let me check if that's correct. Wait, the integral is exactly 1005, so the numerical approximation is 1005.0000000000. But maybe I should confirm with a specific example. Let's take a smaller interval, say from 1 to 3. Then the integral would be (3 -1)/2 = 1. Let's compute it manually. The integrand is sqrt(x)/(sqrt(4 - x) + sqrt(x)) from 1 to 3. Let's compute at x=1: sqrt(1)/(sqrt(3) + sqrt(1)) = 1/(sqrt(3)+1). At x=2: sqrt(2)/(sqrt(2) + sqrt(2)) = sqrt(2)/(2 sqrt(2)) = 1/2. At x=3: sqrt(3)/(sqrt(1) + sqrt(3)) = sqrt(3)/(1 + sqrt(3)). The integral from 1 to 3 of this function. If we compute it numerically, say using substitution, but according to the formula, it should be (3 -1)/2 = 1. Let me compute it approximately. Let's approximate the integral from 1 to 3 of sqrt(x)/(sqrt(4 -x) + sqrt(x)) dx. Let's use midpoint with a few intervals. Take x=1.5: sqrt(1.5)/(sqrt(2.5) + sqrt(1.5)) ≈ 1.2247/(1.5811 + 1.2247) ≈ 1.2247/2.8058 ≈ 0.4364. x=2.5: sqrt(2.5)/(sqrt(1.5) + sqrt(2.5)) ≈ 1.5811/(1.2247 + 1.5811) ≈ 1.5811/2.8058 ≈ 0.5636. The average of these two midpoints is (0.4364 + 0.5636)/2 = 1.0, multiplied by the interval width (3 -1) = 2, gives 1.0 * 2 = 2.0. Wait, that's not matching. Wait, no, midpoint method with two intervals would be (1.5 to 2.5 as midpoints?), no, actually, if we split the interval [1,3] into two intervals, each of width 1, then midpoints are at 1.5 and 2.5. The function values there are approximately 0.4364 and 0.5636. Then the integral approximation is (0.4364 + 0.5636) * 1 = 1.0. Which matches the exact result. So that's correct. So the method works here. Therefore, the original integral is indeed 1005. So the numerical approximation is exactly 1005.0000000000. So the answer is 1005.
</think>

{"answer": "1005", "numerical_answer": "1005.0000000000"}