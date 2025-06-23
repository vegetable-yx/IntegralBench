import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate the arcsine of 1/4
arcsin_val = mp.asin(1/4)

# Subtract 1 from the arcsine result
arcsin_minus_one = arcsin_val - 1

# Multiply by pi/2
result = (mp.pi / 2) * arcsin_minus_one

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))