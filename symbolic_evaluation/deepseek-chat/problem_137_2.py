import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the complete elliptic integral of the second kind at k=1/2
e_half = mp.ellipe(0.5)

# Multiply by 2 as per the expression: 2 * E(1/2)
result = 2 * e_half

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))