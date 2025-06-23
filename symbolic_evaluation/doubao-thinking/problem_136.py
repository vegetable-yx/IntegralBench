import mpmath as mp
mp.dps = 15

# Calculate the argument for the elliptic integral
k = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the second kind
E_value = mp.ellipe(k)

# Multiply by 2 as per the analytical expression
result = 2 * E_value

print(mp.nstr(result, n=10))