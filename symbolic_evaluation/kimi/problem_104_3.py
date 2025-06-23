import mpmath as mp
mp.dps = 15

# Define the modulus k = 1/4
k = mp.mpf('0.25')

# Compute complete elliptic integrals of first and second kind
E_value = mp.ellipe(k)
K_value = mp.ellipk(k)

# Combine results using the derived formula: 4E(1/4) - (15/4)K(1/4)
result = 4 * E_value - (15/4) * K_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))