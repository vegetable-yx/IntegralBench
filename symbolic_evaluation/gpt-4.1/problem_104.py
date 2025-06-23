import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute K(1/4) - complete elliptic integral of the first kind
k_val = mp.ellipk(0.25)

# Compute E(1/4) - complete elliptic integral of the second kind
e_val = mp.ellipe(0.25)

# Calculate the first term: (31/128) * K(1/4)
term1 = (31 / 128) * k_val

# Calculate the second term: (1/128) * E(1/4)
term2 = (1 / 128) * e_val

# Sum the terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))