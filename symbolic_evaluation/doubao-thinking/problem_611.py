import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the argument for the first logarithm: 2 + sqrt(3)
arg1 = 2 + sqrt3

# Compute the first logarithm: ln(2 + sqrt(3))
log1 = mp.log(arg1)

# Compute the second logarithm: ln(sqrt(3))
log2 = mp.log(sqrt3)

# Subtract the logarithms: ln(2 + sqrt(3)) - ln(sqrt(3))
result = log1 - log2

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))