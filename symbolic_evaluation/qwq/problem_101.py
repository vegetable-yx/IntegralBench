import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the first kind K(1/4)
k_value = mp.mpf(1)/4
K_k = mp.ellipk(k_value)

# Compute the complete elliptic integral of the second kind E(1/4)
E_k = mp.ellipe(k_value)

# Calculate the difference between K and E values
difference = K_k - E_k

# Multiply the difference by 2 to get the final result
result = 2 * difference

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))