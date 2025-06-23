import mpmath as mp

# Set decimal places for internal calculation
mp.dps = 15

# Compute the argument for the elliptic integral
k = 1 / mp.sqrt(2)

# Calculate the complete elliptic integral of the second kind
E_val = mp.ellipe(k)

# Multiply by 2 as per the expression
result = 2 * E_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))