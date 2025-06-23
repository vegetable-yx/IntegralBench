<think>
Okay, so I need to compute the definite integral of |x³ - x| from -4 to 4. Hmm, absolute value integrals can be tricky because the function inside can change signs, so I have to find where the expression inside the absolute value is positive or negative. That way, I can split the integral into intervals where I can remove the absolute value appropriately.

First, let me find the points where x³ - x equals zero because those are the points where the sign might change. Let's solve x³ - x = 0. Factoring that, x(x² - 1) = 0, so x = 0, x = 1, or x = -1. So the critical points are at x = -1, 0, and 1. These points divide the interval [-4, 4] into subintervals where the function x³ - x is either positive or negative.

Now, I need to determine the sign of x³ - x in each interval. Let's consider the intervals: [-4, -1], [-1, 0], [0, 1], and [1, 4].

Starting with [-4, -1]: Let's pick a test point, say x = -2. Plugging into x³ - x: (-2)^3 - (-2) = -8 + 2 = -6, which is negative. So in this interval, |x³ - x| = -(x³ - x) = -x³ + x.

Next, [-1, 0]: Let's take x = -0.5. Then (-0.5)^3 - (-0.5) = -(-0.125) + 0.5 = 0.125 + 0.5 = 0.625. Wait, no, wait. Wait, the original expression is x³ - x. So at x = -0.5: (-0.5)^3 - (-0.5) = -0.125 + 0.5 = 0.375, which is positive. So |x³ - x| = x³ - x here.

Wait, but that contradicts my initial thought. Wait, let me check again. For x in [-1, 0], let's compute x³ - x. Let's take x = -0.5: (-0.5)^3 - (-0.5) = -0.125 + 0.5 = 0.375, which is positive. So in [-1, 0], x³ - x is positive, so |x³ - x| = x³ - x.

Then in [0, 1], let's take x = 0.5: (0.5)^3 - 0.5 = 0.125 - 0.5 = -0.375, which is negative. So |x³ - x| = -(x³ - x) = -x³ + x here.

In [1, 4], take x = 2: 2^3 - 2 = 8 - 2 = 6, positive. So |x³ - x| = x³ - x here.

So summarizing:

- From -4 to -1: |x³ - x| = -x³ + x
- From -1 to 0: |x³ - x| = x³ - x
- From 0 to 1: |x³ - x| = -x³ + x
- From 1 to 4: |x³ - x| = x³ - x

Therefore, the integral becomes the sum of the integrals over these four intervals with the corresponding expressions.

So the integral is:

Integral from -4 to -1 of (-x³ + x) dx
+ Integral from -1 to 0 of (x³ - x) dx
+ Integral from 0 to 1 of (-x³ + x) dx
+ Integral from 1 to 4 of (x³ - x) dx

Now, let's compute each integral one by one.

First integral: ∫ from -4 to -1 of (-x³ + x) dx. Wait, no, wait. Wait, the first interval is [-4, -1], where |x³ - x| = -x³ + x. So the integral is ∫_{-4}^{-1} (-x³ + x) dx.

Let's compute that. The antiderivative of -x³ + x is:

∫(-x³ + x) dx = - (x^4)/4 + (x^2)/2 + C

Evaluated from -4 to -1.

So compute at upper limit (-1):

- [ (-1)^4 /4 ] + [ (-1)^2 /2 ] = - (1/4) + (1/2) = (-1/4 + 2/4) = 1/4

At lower limit (-4):

- [ (-4)^4 /4 ] + [ (-4)^2 /2 ] = - (256/4) + (16/2) = -64 + 8 = -56

So the first integral is (1/4) - (-56) = 1/4 + 56 = 56.25

Second integral: ∫ from -1 to 0 of (x³ - x) dx

Antiderivative is (x^4)/4 - (x^2)/2 + C

At upper limit 0:

(0)^4/4 - (0)^2/2 = 0

At lower limit -1:

[ (-1)^4 /4 ] - [ (-1)^2 /2 ] = (1/4) - (1/2) = -1/4

So the second integral is 0 - (-1/4) = 1/4 = 0.25

Third integral: ∫ from 0 to 1 of (-x³ + x) dx

Antiderivative is - (x^4)/4 + (x^2)/2 + C

At upper limit 1:

- (1^4)/4 + (1^2)/2 = -1/4 + 1/2 = 1/4

At lower limit 0:

0 + 0 = 0

So third integral is 1/4 - 0 = 0.25

Fourth integral: ∫ from 1 to 4 of (x³ - x) dx

Antiderivative is (x^4)/4 - (x^2)/2 + C

At upper limit 4:

(4^4)/4 - (4^2)/2 = 256/4 - 16/2 = 64 - 8 = 56

At lower limit 1:

(1^4)/4 - (1^2)/2 = 1/4 - 1/2 = -1/4

So fourth integral is 56 - (-1/4) = 56 + 1/4 = 56.25

Now, summing all four integrals:

56.25 + 0.25 + 0.25 + 56.25 = 56.25 + 56.25 = 112.5, and 0.25 + 0.25 = 0.5, so total 112.5 + 0.5 = 113.

Wait, that's 113? Let me check the calculations again because that seems a bit clean. Let me verify each step.

First integral: from -4 to -1, we had 56.25. Second integral 0.25, third 0.25, fourth 56.25. So 56.25 + 0.25 = 56.5, then 56.5 + 0.25 = 56.75, then 56.75 + 56.25 = 113. Yes, that's correct.

But let me check the antiderivatives again to make sure.

For the first integral, ∫(-x³ + x) dx. The antiderivative is -x^4/4 + x^2/2. Correct. Evaluated at -1: -1/4 + 1/2 = 1/4. At -4: -256/4 + 16/2 = -64 + 8? Wait, (-4)^2 is 16, so 16/2 is 8. So -64 + 8 = -56. Then 1/4 - (-56) = 56.25. Correct.

Second integral: ∫(x³ - x) dx from -1 to 0. Antiderivative x^4/4 - x^2/2. At 0: 0. At -1: (1/4 - 1/2) = -1/4. So 0 - (-1/4) = 1/4. Correct.

Third integral: ∫(-x³ + x) dx from 0 to1. Antiderivative -x^4/4 + x^2/2. At 1: -1/4 + 1/2 = 1/4. At 0: 0. So 1/4. Correct.

Fourth integral: ∫(x³ -x) dx from1 to4. Antiderivative x^4/4 -x^2/2. At 4: 256/4 - 16/2 = 64 -8=56. At1:1/4 -1/2= -1/4. So 56 - (-1/4)=56.25. Correct.

So total integral is 56.25 +0.25 +0.25 +56.25=113. So the exact value is 113. But wait, 113 is an integer. Let me check if that's a mistake. Because the integral of absolute value functions can sometimes result in such clean numbers, but let me confirm.

Alternatively, maybe there's symmetry here. Let's see. The function |x³ -x|. Let's check if it's even or odd. Since x³ -x is an odd function: f(-x) = (-x)^3 - (-x) = -x³ +x = - (x³ -x) = -f(x). So the absolute value of an odd function is even, because |f(-x)| = | -f(x)| = |f(x)|. Therefore, the integrand |x³ -x| is even. Therefore, the integral from -4 to4 is twice the integral from 0 to4. But wait, in our calculation, we split into intervals from -4 to -1, -1 to0, etc. But if the function is even, then integrating from 0 to4 and doubling would be easier. Let me check that approach.

If the integrand is even, then ∫_{-a}^a f(x) dx = 2 ∫_{0}^a f(x) dx. So here, a=4. So the integral from -4 to4 is 2 times the integral from 0 to4 of |x³ -x| dx. But wait, but in the interval from 0 to1, |x³ -x| is -(x³ -x), and from1 to4, it's x³ -x. So integrating from0 to4 would be ∫0^1 (-x³ +x) dx + ∫1^4 (x³ -x) dx. Then multiply by 2. Let's see if that gives the same result.

Compute ∫0^1 (-x³ +x) dx: as before, that's 1/4. ∫1^4 (x³ -x) dx: 56.25 - (-1/4) =56.25 +0.25=56.5? Wait, no. Wait, the integral from1 to4 is 56.25 as computed earlier. So total from0 to4 is 1/4 +56.25=56.5. Then multiply by2: 113. So same result. So that's correct. So the exact answer is 113. So the exact value is 113. But wait, 113 is an integer. So the exact answer is 113. But let me check again.

Wait, maybe I made a mistake in the first approach. Let me check the sum again. 56.25 (from -4 to -1) +0.25 (from -1 to0) +0.25 (from0 to1) +56.25 (from1 to4) =56.25+56.25=112.5, and 0.25+0.25=0.5, so 112.5+0.5=113. Yes. So exact answer is 113. So the exact answer is 113, which is an integer, so the exact value is 113. Then the numerical approximation is 113.0000000000. But let me check with another approach.

Alternatively, maybe there's a mistake in the calculation. Let me check the first interval again. From -4 to -1, the integral of (-x³ +x) dx. The antiderivative is -x^4/4 +x^2/2. At x=-1: - (1)/4 + (1)/2 = (-0.25 +0.5)=0.25. At x=-4: - (256)/4 + (16)/2= -64 +8= -56. So the difference is 0.25 - (-56)=56.25. Correct. Then the second integral from -1 to0: (x³ -x) dx. Antiderivative x^4/4 -x^2/2. At0:0. At-1: (1/4 -1/2)= -0.25. So 0 - (-0.25)=0.25. Third integral from0 to1: (-x³ +x) dx. Antiderivative -x^4/4 +x^2/2. At1: -0.25 +0.5=0.25. At0:0. So 0.25. Fourth integral from1 to4: (x³ -x) dx. Antiderivative x^4/4 -x^2/2. At4: 256/4 -16/2=64-8=56. At1:0.25 -0.5= -0.25. So 56 - (-0.25)=56.25. So sum all:56.25+0.25+0.25+56.25=113. So yes, exact answer is 113. So the exact answer is 113, and numerical approximation is 113.0000000000.

But let me check with a numerical estimation. For example, maybe compute the integral numerically. Let's see, the integral from -4 to4 of |x³ -x| dx. Let's split into the intervals as before. But since we already did the analytical calculation and got 113, which is an integer, and the steps check out, I think that's correct. So the exact answer is 113, and the numerical approximation is 113.0000000000.
</think>

{"answer": "113", "numerical_answer": "113.0000000000"}