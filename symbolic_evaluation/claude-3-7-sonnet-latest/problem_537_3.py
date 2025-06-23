import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the constant integer 3
# Convert to mpmath floating-point number
result = mp.mpf(3)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))