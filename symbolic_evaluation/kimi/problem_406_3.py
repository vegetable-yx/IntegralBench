import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the common value of sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute the first argument: (sqrt(3) - 1)/2
arg1 = (sqrt3 - 1) / 2

# Compute the second argument: (1 - sqrt(3))/2
arg2 = (1 - sqrt3) / 2

# Compute the arcsine of the first argument
term1 = mp.asin(arg1)

# Compute the arcsine of the second argument
term2 = mp.asin(arg2)

# Subtract the two terms: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))