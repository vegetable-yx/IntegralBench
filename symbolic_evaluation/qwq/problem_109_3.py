import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the argument for the elliptic integral
k = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the second kind E(k)
E_value = mp.ellipe(k)

# Multiply by pi to get the final result
result = mp.pi * E_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))