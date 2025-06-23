import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

k = mp.mpf(1)/4  # Define the modulus parameter

# Calculate complete elliptic integrals of first and second kind
E_value = mp.ellipe(k)  # E(1/4)
K_value = mp.ellipk(k)  # K(1/4)

# Compute the terms of the expression
term_4E = 4 * E_value
term_15_4K = (15/4) * K_value

# Combine terms to get final result
result = term_4E - term_15_4K

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))