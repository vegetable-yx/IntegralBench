<think>
Okay, so I need to calculate the definite integral of |x³ - x| from -4 to 4. Hmm, integrating an absolute value function means I have to figure out where the expression inside the absolute value is positive or negative, right? Because the function x³ - x changes its sign at certain points, and the absolute value will affect the integral depending on those intervals.

First, let me find the points where x³ - x equals zero. That's where the function inside the absolute value changes sign. So, solving x³ - x = 0. Factoring that, x(x² - 1) = 0, which gives x = 0, x = 1, and x = -1. So the critical points are at x = -1, 0, and 1. These points divide the interval from -4 to 4 into subintervals where the expression inside the absolute value is either positive or negative.

Now, the original integral is from -4 to 4. So the intervals to consider are: [-4, -1], [-1, 0], [0, 1], and [1, 4]. I need to determine the sign of x³ - x in each of these intervals.

Let me test each interval:

1. For x in [-4, -1]: Let's pick x = -2. Then x³ - x = (-8) - (-2) = -8 + 2 = -6, which is negative. So the absolute value will make it positive, so |x³ - x| = -(x³ - x) = -x³ + x.

2. For x in [-1, 0]: Let's take x = -0.5. Then x³ - x = (-0.125) - (-0.5) = 0.375, which is positive. So |x³ - x| = x³ - x here.

Wait, that's positive? Wait, x is negative here. Let me check again. x = -0.5, so x³ is (-0.5)^3 = -0.125, and -x is 0.5. So -0.125 + 0.5 = 0.375. Yes, positive. So in [-1, 0], the expression is positive, so |x³ - x| = x³ - x.

3. For x in [0, 1]: Let's take x = 0.5. Then x³ - x = 0.125 - 0.5 = -0.375, which is negative. So |x³ - x| = -(x³ - x) = -x³ + x.

4. For x in [1, 4]: Let's take x = 2. Then x³ - x = 8 - 2 = 6, which is positive. So |x³ - x| = x³ - x here.

So summarizing:

- From -4 to -1: |x³ - x| = -x³ + x
- From -1 to 0: |x³ - x| = x³ - x
- From 0 to 1: |x³ - x| = -x³ + x
- From 1 to 4: |x³ - x| = x³ - x

Therefore, the integral can be split into four parts:

Integral from -4 to -1 of (-x³ + x) dx +
Integral from -1 to 0 of (x³ - x) dx +
Integral from 0 to 1 of (-x³ + x) dx +
Integral from 1 to 4 of (x³ - x) dx

Now, let's compute each integral separately.

First integral: ∫ from -4 to -1 of (-x³ + x) dx

The antiderivative of -x³ is - (x^4)/4, and the antiderivative of x is (x²)/2. So:

[- (x^4)/4 + (x²)/2] evaluated from -4 to -1.

Compute at upper limit (-1):

- ((-1)^4)/4 + ((-1)^2)/2 = - (1/4) + (1/2) = (-1/4 + 2/4) = 1/4

Compute at lower limit (-4):

- ((-4)^4)/4 + ((-4)^2)/2 = - (256/4) + (16/2) = -64 + 8 = -56

So the first integral is 1/4 - (-56) = 1/4 + 56 = 56.25

Second integral: ∫ from -1 to 0 of (x³ - x) dx

Antiderivative of x³ is (x^4)/4, and antiderivative of -x is - (x²)/2. So:

[(x^4)/4 - (x²)/2] evaluated from -1 to 0.

At upper limit (0):

0 - 0 = 0

At lower limit (-1):

[(-1)^4 /4 - (-1)^2 /2] = (1/4 - 1/2) = -1/4

So the second integral is 0 - (-1/4) = 1/4

Third integral: ∫ from 0 to 1 of (-x³ + x) dx

Antiderivative is same as first integral: - (x^4)/4 + (x²)/2

Evaluate from 0 to 1.

At upper limit (1):

- (1/4) + (1/2) = (-1/4 + 2/4) = 1/4

At lower limit (0):

0 + 0 = 0

So third integral is 1/4 - 0 = 1/4

Fourth integral: ∫ from 1 to 4 of (x³ - x) dx

Antiderivative is same as second integral: (x^4)/4 - (x²)/2

Evaluate from 1 to 4.

At upper limit (4):

(256/4) - (16/2) = 64 - 8 = 56

At lower limit (1):

(1/4) - (1/2) = -1/4

So the fourth integral is 56 - (-1/4) = 56 + 1/4 = 56.25

Now, sum all four integrals:

56.25 + 0.25 + 0.25 + 56.25 = 56.25 + 56.25 = 112.5, and 0.25 + 0.25 = 0.5. So total is 112.5 + 0.5 = 113.

Wait, that seems too clean. Let me check the calculations again.

First integral: 56.25

Second: 0.25

Third: 0.25

Fourth: 56.25

Adding them up: 56.25 + 0.25 = 56.5; 56.5 + 0.25 = 56.75; 56.75 + 56.25 = 113. So total integral is 113.

But let me verify each step again because 113 seems a whole number, which might be correct, but let's check.

First integral: from -4 to -1 of (-x³ + x) dx.

Antiderivative: -x^4/4 + x²/2.

At x = -1: -(-1)^4/4 + (-1)^2/2 = -1/4 + 1/2 = 1/4.

At x = -4: -(-4)^4/4 + (-4)^2/2 = -256/4 + 16/2 = -64 + 8 = -56.

So 1/4 - (-56) = 56.25. Correct.

Second integral: from -1 to 0 of (x³ - x) dx.

Antiderivative: x^4/4 - x²/2.

At 0: 0 - 0 = 0.

At -1: (1)/4 - (1)/2 = -1/4.

0 - (-1/4) = 1/4. So 0.25. Correct.

Third integral: from 0 to 1 of (-x³ + x) dx.

Antiderivative: -x^4/4 + x²/2.

At 1: -1/4 + 1/2 = 1/4.

At 0: 0. So 1/4. Correct.

Fourth integral: from 1 to 4 of (x³ - x) dx.

Antiderivative: x^4/4 - x²/2.

At 4: 256/4 - 16/2 = 64 - 8 = 56.

At 1: 1/4 - 1/2 = -1/4.

56 - (-1/4) = 56.25. Correct.

So adding all parts: 56.25 + 0.25 + 0.25 + 56.25 = 56.25 + 56.25 = 112.5, plus 0.5 gives 113. So the exact value is 113.

Wait, but 56.25 is 225/4, right? 56.25 * 4 = 225. So 225/4 + 1/4 + 1/4 + 225/4 = (225 + 1 + 1 + 225)/4 = 452/4 = 113. Yes, 452 divided by 4 is 113. So exact answer is 113.

But let me check if the integration steps are correct. For example, in the first integral, when we integrate from -4 to -1, the function is -x³ + x. The antiderivative is correct. The evaluation at -1 and -4 also seems correct.

Similarly, the other integrals. So the exact answer is 113. The numerical approximation would be 113.0000000000, but maybe I should check if there's a mistake here. Wait, but the problem says to compute the integral analytically and then provide a numerical approximation. But if the exact answer is an integer, then the numerical approximation is the same. But let me confirm once again.

Wait, perhaps I made a mistake in splitting the intervals. Let me check the sign of x³ - x in each interval again.

For x in [-4, -1], take x = -2: (-8) - (-2) = -6, which is negative. So |x³ -x| = -x³ + x. Correct.

For x in [-1, 0], take x = -0.5: (-0.125) - (-0.5) = 0.375, positive. So |x³ -x| = x³ -x. Correct.

For x in [0,1], take x=0.5: 0.125 - 0.5 = -0.375, negative. So |x³ -x| = -x³ +x. Correct.

For x in [1,4], take x=2: 8 - 2 = 6, positive. So |x³ -x| = x³ -x. Correct.

So the splitting is correct. Then the sum of the integrals gives 113. So the exact answer is 113, and the numerical approximation is 113.0000000000.

But wait, maybe I should check with another approach. For example, since the function |x³ -x| is even? Let's see. Let's check if the function is even. An even function satisfies f(-x) = f(x). Let's compute f(-x) = |(-x)^3 - (-x)| = | -x³ + x | = |x - x³| = |x³ - x|, which is the same as f(x). So yes, the function is even. Therefore, the integral from -4 to 4 is twice the integral from 0 to 4. Wait, but 4 is symmetric around 0, so maybe we can exploit that.

But in this case, since the function is even, ∫_{-4}^4 |x³ -x| dx = 2 * ∫_{0}^4 |x³ -x| dx. But wait, but the critical points are at 0 and 1, so from 0 to 1, the function is negative, and from 1 to 4, positive. So ∫_{0}^4 |x³ -x| dx = ∫_{0}^1 (-x³ +x) dx + ∫_{1}^4 (x³ -x) dx. Then multiply by 2. Wait, but in the original calculation, the integral from -4 to 4 is split into four parts. But since the function is even, maybe we can compute from 0 to 4 and double it. Let's check.

Original integral: 113. If we compute 2*(integral from 0 to4 of |x³ -x| dx). Let's compute that.

From 0 to1: integral of (-x³ +x) dx = [ -x^4/4 + x²/2 ] from 0 to1 = (-1/4 + 1/2) - 0 = 1/4.

From1 to4: integral of (x³ -x) dx = [x^4/4 -x²/2] from1 to4 = (256/4 - 16/2) - (1/4 -1/2) = (64 -8) - (-1/4) = 56 + 1/4 = 56.25.

So total from0 to4 is 1/4 +56.25 = 56.5. Multiply by 2 gives 113. So same result. So that's correct.

Therefore, the exact answer is 113, and the numerical approximation is 113.0000000000. So the problem is solved.
</think>

{"answer": "113", "numerical_answer": "113.0000000000"}