import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt5 = mp.sqrt(5)       # Compute square root of 5
bracket_term = sqrt5 - 2 # Calculate (sqrt(5) - 2)
pi_half = mp.pi / 2      # Precompute π/2

# Combine components for final result
result = pi_half * bracket_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))