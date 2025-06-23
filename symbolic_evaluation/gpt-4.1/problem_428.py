import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the analytical result as a constant value
result = mp.mpf(17)

# Print the result formatted to 10 decimal places
# Using strip_zeros=False ensures exactly 10 digits after the decimal are shown
print(mp.nstr(result, 10, strip_zeros=False))