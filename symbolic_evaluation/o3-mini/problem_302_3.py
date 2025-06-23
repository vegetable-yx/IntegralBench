import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate 1 divided by the square root of 17
inner_value = 1 / mp.sqrt(17)

# Compute the arcsine of the inner_value
arcsin_val = mp.asin(inner_value)

# Multiply by π/2
result = (mp.pi / 2) * arcsin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))