import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate arcsin(0.25) using mp.asin
arcsin_val = mp.asin(0.25)

# Multiply by pi and divide by 32
result = (mp.pi / 32) * arcsin_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))