import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute the amplitude phi = arcsin(1/4)
phi = mp.asin(1/4)

# Evaluate the incomplete elliptic integral of the second kind E(phi, m) with m=4
result = mp.ellipe(phi, 4)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))