import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate components of the expression step by step
sqrt5 = mp.sqrt(5)  # Compute square root of 5
phi = (1 + sqrt5) / 2  # Calculate golden ratio (1+√5)/2
log_phi = mp.log(phi)  # Natural logarithm of golden ratio
pi_over_2 = mp.pi / 2  # Compute π/2

# Combine components for final result
result = pi_over_2 * log_phi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))