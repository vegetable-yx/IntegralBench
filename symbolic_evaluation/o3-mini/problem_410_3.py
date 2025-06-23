import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Divide the result by 2
half_sqrt_pi = sqrt_pi / 2

# Compute the exponential of -1
exp_minus_one = mp.exp(-1)

# Multiply the two components to get the final result
result = half_sqrt_pi * exp_minus_one

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))