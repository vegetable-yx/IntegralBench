import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate ζ(3, 0.75) using Hurwitz zeta function
zeta_term1 = mp.zeta(3, 0.75)

# Calculate ζ(3, 1.25) using Hurwitz zeta function
zeta_term2 = mp.zeta(3, 1.25)

# Compute the difference between the two zeta values
zeta_difference = zeta_term1 - zeta_term2

# Calculate final result by subtracting the difference from 64
result = 64 - zeta_difference

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))