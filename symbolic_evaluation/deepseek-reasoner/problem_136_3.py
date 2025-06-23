import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the argument for the elliptic integral
k = mp.sqrt(2) / 2  # Compute sqrt(2)/2

# Compute the complete elliptic integral of the second kind E(k)
E_value = mp.ellipe(k)

# Multiply by 2 to get the final result
result = 2 * E_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))