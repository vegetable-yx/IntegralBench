import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the argument for the elliptic integral: k = 1/sqrt(2)
k_value = 1 / mp.sqrt(2)

# Evaluate the complete elliptic integral of the second kind: E(k)
E_value = mp.ellipe(k_value)

# Multiply the result by 4 as per the analytical expression
result = 4 * E_value

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))