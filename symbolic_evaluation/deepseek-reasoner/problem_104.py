import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate complete elliptic integrals
k = mp.mpf(1)/4  # Modulus parameter for the integrals
E_value = mp.ellipe(k)  # Compute complete elliptic integral of the second kind
K_value = mp.ellipk(k)  # Compute complete elliptic integral of the first kind

# Calculate terms from the analytical expression
term1 = 4 * E_value
term2 = (15/4) * K_value

# Combine terms for final result
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))