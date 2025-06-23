import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute ζ(3, 0.75) using Hurwitz zeta function
zeta_term1 = mp.zeta(3, 0.75)

# Compute ζ(3, 1.25) using Hurwitz zeta function
zeta_term2 = mp.zeta(3, 1.25)

# Calculate the difference between the two zeta values
zeta_difference = zeta_term1 - zeta_term2

# Compute final result by subtracting the difference from 64
result = 64 - zeta_difference

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))