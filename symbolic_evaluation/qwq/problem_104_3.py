import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate complete elliptic integrals of first and second kind
K_val = mp.ellipk(mp.mpf(1)/4)  # K(1/4)
E_val = mp.ellipe(mp.mpf(1)/4)  # E(1/4)

# Compute each term of the expression
term1 = 8 * E_val
term2 = (mp.mpf(15)/2) * K_val

# Combine terms to get final result
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))