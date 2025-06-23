import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the exact expression: -π/2
# Using mp.pi for the mathematical constant π
result = -mp.pi / 2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))