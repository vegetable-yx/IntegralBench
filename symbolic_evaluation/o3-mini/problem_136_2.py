import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the second kind E(k) at k=1/2
elliptic_value = mp.ellipe(0.5)

# Multiply by 2 as per the analytical expression
result = 2 * elliptic_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))