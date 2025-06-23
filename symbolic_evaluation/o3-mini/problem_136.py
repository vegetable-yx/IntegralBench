import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the argument for the elliptic integral: 1/sqrt(2)
k_val = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the second kind E(k_val)
E_val = mp.ellipe(k_val)

# Multiply by 2 as per the expression
result = 2 * E_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))