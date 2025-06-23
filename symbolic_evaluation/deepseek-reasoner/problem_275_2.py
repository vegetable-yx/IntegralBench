import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each component of the expression
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
exp_term = mp.exp(9/4)    # Exponential term e^(9/4)

# Compute modified Bessel functions I0 and I1 at 9/4
bessel_I0 = mp.besseli(0, 9/4)
bessel_I1 = mp.besseli(1, 9/4)
bessel_sum = bessel_I0 + bessel_I1  # Sum of Bessel functions

# Combine all components
numerator = 3 * sqrt_pi * exp_term * bessel_sum
denominator = 2 * mp.sqrt(3)  # 2 times square root of 3
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))