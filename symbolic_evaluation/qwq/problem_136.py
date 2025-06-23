import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the modulus parameter k = sqrt(2)/2
k = mp.sqrt(2) / 2

# Compute the complete elliptic integral of the second kind E(k)
E_value = mp.ellipe(k)

# Multiply by 2 to get the final result
result = 2 * E_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))