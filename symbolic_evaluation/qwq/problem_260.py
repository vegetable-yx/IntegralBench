import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/2 * ln(2)
pi_over_2 = mp.pi / 2
term1 = pi_over_2 * mp.log(2)

# Compute the sine integral of 1 (Si(1))
term2 = mp.si(1)

# Calculate (π/2 - 1)
term3 = (mp.pi / 2) - 1

# Combine all components for final result
result = term1 + term2 - term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))