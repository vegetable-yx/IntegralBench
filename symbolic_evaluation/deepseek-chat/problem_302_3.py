import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the arcsine of 1/4
arcsin_val = mp.asin(1/4)

# Square the result to get (arcsin(1/4))^2
result = arcsin_val ** 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))