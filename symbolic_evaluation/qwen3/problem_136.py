import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate the argument for the elliptic integral
k = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the second kind
E_value = mp.ellipe(k)

# Multiply by 2 to get the final result
result = 2 * E_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))