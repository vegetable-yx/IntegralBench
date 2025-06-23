import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is a constant integer 17
# Convert to mpmath floating-point number
result = mp.mpf(17)

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))