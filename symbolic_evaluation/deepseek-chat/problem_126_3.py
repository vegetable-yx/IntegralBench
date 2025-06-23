import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the complete elliptic integral of the second kind at k=1/2
E_half = mp.ellipe(0.5)

# Square the result
E_half_sq = E_half ** 2

# Multiply by 4 to get the final result
result = 4 * E_half_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))