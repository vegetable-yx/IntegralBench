import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant integer 5040
# Assign directly to result
result = 5040

# Print the result to exactly 10 decimal places using mp.nstr
print(mp.nstr(result, n=10))