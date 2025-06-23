import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: π²/16
pi_sq_over_16 = mp.pi**2 / 16

# Compute the expression inside the arctan denominator
inner_sqrt = mp.sqrt(120)  # √120
denom = 11 + inner_sqrt    # 11 + √120

# Calculate the argument for arctan: 1/(11 + √120)
arctan_arg = 1 / denom

# Compute arctan of the argument
arctan_val = mp.atan(arctan_arg)

# Square the arctan result
arctan_sq = arctan_val**2

# Calculate the second term: (1/2) * arctan²
half_arctan_sq = 0.5 * arctan_sq

# Final result: π²/16 - (1/2)*arctan²
result = pi_sq_over_16 - half_arctan_sq

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))