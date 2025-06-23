import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the argument for the elliptic integral: k = 1/sqrt(2)
k = 1 / mp.sqrt(2)

# Calculate the complete elliptic integral of the second kind: E(k)
result = mp.ellipe(k)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))