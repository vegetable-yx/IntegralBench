import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate components of the expression
sqrt5 = mp.sqrt(5)  # Compute square root of 5
bracket_term = sqrt5 - 2  # Calculate (√5 - 2)
pi_half = mp.pi / 2  # Precompute π/2

# Combine components for final result
result = pi_half * bracket_term  # Multiply π/2 by (√5 - 2)

print(mp.nstr(result, n=10))  # Print result with 10 decimal places