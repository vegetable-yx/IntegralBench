import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the constant sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute the first argument for erf: sqrt(3)/2
arg1 = sqrt3 / 2

# Compute the second argument for erf: 1/(2*sqrt(3))
arg2 = 1 / (2 * sqrt3)

# Calculate erf values for both arguments
erf1 = mp.erf(arg1)
erf2 = mp.erf(arg2)

# Compute the difference between erf values
erf_diff = erf1 - erf2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * erf_diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))