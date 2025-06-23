import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Base value
base = 2

# Exponent: -2/3
exponent = mp.mpf(-2) / mp.mpf(3)

# Calculate 2^(-2/3)
result = base ** exponent

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))