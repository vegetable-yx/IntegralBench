import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant integer 2
# Convert it to an mpmath floating-point number
result = mp.mpf(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))