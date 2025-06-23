import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the complete elliptic integral of the second kind E(0.25)
E_val = mp.ellipe(0.25)

# Compute the complete elliptic integral of the first kind K(0.25)
K_val = mp.ellipk(0.25)

# Calculate 16 times E(0.25)
term1 = 16 * E_val

# Calculate 15 times K(0.25)
term2 = 15 * K_val

# Subtract the two terms: 16E(0.25) - 15K(0.25)
diff = term1 - term2

# Divide the result by 8 to get the final value
result = diff / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))