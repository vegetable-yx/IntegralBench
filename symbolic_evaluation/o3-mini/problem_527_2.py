import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Assign the exact analytical result (zero)
result = mp.mpf(0)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))