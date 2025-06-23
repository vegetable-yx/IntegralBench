import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi constant using mpmath
pi_value = mp.pi

# Compute denominator
denominator = 20

# Calculate final result as -π/20
result = -pi_value / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))