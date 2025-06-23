import mpmath as mp

# Set internal decimal places of precision to 15
mp.dps = 15

# The analytical expression is the constant integer 4
# Convert to mpmath floating-point number
result = mp.mpf(4)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))