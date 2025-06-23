import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/4
pi_over_4 = mp.pi / 4

# Compute e^(π/4)
exp_pi4 = mp.exp(pi_over_4)

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply e^(π/4) by sqrt(2)
numerator_part = exp_pi4 * sqrt2

# Subtract 1 to complete the numerator
numerator = numerator_part - 1

# Divide by 2 to get final result
result = numerator / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))