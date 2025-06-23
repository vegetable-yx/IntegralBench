import mpmath as mp
mp.dps = 15

# Compute the argument for the elliptic integral
k = 1 / mp.sqrt(2)

# Calculate the complete elliptic integral of the second kind E(k)
E_value = mp.ellipe(k)

# Multiply by 2 according to the given expression
result = 2 * E_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))