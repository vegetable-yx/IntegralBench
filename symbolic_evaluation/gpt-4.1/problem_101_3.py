import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the parameter k = 1/4
k = mp.mpf(1) / mp.mpf(4)

# Compute complete elliptic integrals
# K(k) - first kind
K_val = mp.ellipk(k)
# E(k) - second kind
E_val = mp.ellipe(k)

# Compute the terms: 16*E(k) and 15*K(k)
term1 = 16 * E_val
term2 = 15 * K_val

# Combine the terms: 16E(k) - 15K(k)
combined = term1 - term2

# Multiply by 1/8 (i.e., divide by 8)
result = combined / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))