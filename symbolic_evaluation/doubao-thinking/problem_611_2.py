import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute numerator: 2 + sqrt(3)
numerator = 2 + sqrt3

# Construct the argument for logarithm: (2 + sqrt(3)) / sqrt(3)
arg = numerator / sqrt3

# Compute natural logarithm of the argument
result = mp.log(arg)

# Print result rounded to 10 decimal places
print(mp.nstr(result, n=10))