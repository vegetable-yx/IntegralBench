import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the negative of the mathematical constant pi
result = -mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))