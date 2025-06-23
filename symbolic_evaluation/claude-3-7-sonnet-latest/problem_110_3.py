import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the complete elliptic integral of the second kind at k=0.5
E_val = mp.ellipe(0.5)

# Multiply by 8 as per the expression
result = 8 * E_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))