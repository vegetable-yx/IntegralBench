import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of a = (sqrt(3) - 1)/2
a = (mp.sqrt(3) - 1) / 2

# Compute arcsin(a) using mpmath's asin function
arcsin_a = mp.asin(a)

# The expression simplifies to 2 * arcsin(a) due to the odd property of arcsin
result = 2 * arcsin_a

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))