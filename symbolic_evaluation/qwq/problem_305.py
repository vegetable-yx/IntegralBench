import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the argument for the elliptic integrals
k_val = 1 / mp.sqrt(5)

# Calculate complete elliptic integrals of first and second kind
K = mp.ellipk(k_val)
E = mp.ellipe(k_val)

# Compute the difference between K and E
difference = K - E

# Calculate the constant multiplier sqrt(5)/2
sqrt5_over_2 = mp.sqrt(5) / 2

# Compute the final result
result = sqrt5_over_2 * difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))