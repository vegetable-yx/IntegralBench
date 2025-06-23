import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate e^(π/4)
exp_pi4 = mp.exp(pi_over_4)

# Calculate √2
sqrt2 = mp.sqrt(2)

# Calculate √2 * e^(π/4)
sqrt2_times_exp = sqrt2 * exp_pi4

# Calculate numerator: √2 * e^(π/4) - 1
numerator = sqrt2_times_exp - 1

# Final result calculation
result = numerator / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))