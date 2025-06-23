import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate arcsin(1/4)
phi = mp.asin(mp.mpf(1)/4)

# Calculate the incomplete elliptic integral of the second kind E(φ | 16)
elliptic_value = mp.ellipe(phi, 16)

# Multiply by 1/2 to get final result
result = mp.mpf(1)/2 * elliptic_value

# Print result with 10 decimal places
print(mp.nstr(result, n=10))