import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Divide sqrt(pi) by 2
half_sqrt_pi = sqrt_pi / 2

# Calculate e^{-1}
exp_minus_one = mp.exp(-1)

# Multiply the two parts to get the final result
result = half_sqrt_pi * exp_minus_one

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))