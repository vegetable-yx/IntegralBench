import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the square root of (pi / 2)
sqrt_pi_over_2 = mp.sqrt(mp.pi / 2)

# Compute e raised to the power of 1/8
exp_term = mp.exp(0.125)

# Multiply the two intermediate results
result = sqrt_pi_over_2 * exp_term

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))