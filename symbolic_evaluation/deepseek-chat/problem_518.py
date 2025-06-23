import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is the integer 4036
# Convert to mpmath floating point number
result = mp.mpf(4036)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))