import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the arctangent of 4
arctan4 = mp.atan(4)

# Square the arctangent of 4
arctan4_sq = arctan4**2

# Calculate the arctangent of 1/4
arctan_quarter = mp.atan(1/4)

# Square the arctangent of 1/4
arctan_quarter_sq = arctan_quarter**2

# Compute the expression: (1/2)*(arctan4)^2 - (1/2)*(arctan(1/4))^2
result = 0.5 * arctan4_sq - 0.5 * arctan_quarter_sq

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))