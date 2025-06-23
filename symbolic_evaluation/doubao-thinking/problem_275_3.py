import mpmath as mp

mp.dps = 15  # Set internal precision for intermediate calculations

# Compute components of the first term
sqrt_pi = mp.sqrt(mp.pi)          # Calculate square root of pi
sqrt3 = mp.sqrt(3)                # Calculate square root of 3
cosh3 = mp.cosh(3)                # Hyperbolic cosine of 3
erf_sqrt3 = mp.erf(sqrt3)         # Error function of sqrt(3)

# Calculate the first main term: (sqrt(pi)*cosh(3)*erf(sqrt(3)))/2
term1 = (sqrt_pi * cosh3 * erf_sqrt3) / 2

# Calculate the second term: sqrt(3)/4
term2 = sqrt3 / 4

# Combine both terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))