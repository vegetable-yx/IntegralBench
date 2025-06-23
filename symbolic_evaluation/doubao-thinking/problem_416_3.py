import mpmath as mp
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Compute e^(π/4)
exp_pi_over4 = mp.exp(pi_over_4)

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply e^(π/4) by sqrt(2)
exp_pi4_times_sqrt2 = exp_pi_over4 * sqrt2

# Subtract 1 from the product
numerator = exp_pi4_times_sqrt2 - 1

# Divide by 2 to get final result
result = numerator / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))