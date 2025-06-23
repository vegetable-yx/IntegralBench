import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Compute e^(π/4)
exp_pi_over_4 = mp.exp(pi_over_4)

# Calculate sqrt(2)
sqrt_2 = mp.sqrt(2)

# Multiply e^(π/4) by sqrt(2)
product = exp_pi_over_4 * sqrt_2

# Subtract 1 from the product
numerator = product - 1

# Divide by 2 to get final result
result = numerator / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))