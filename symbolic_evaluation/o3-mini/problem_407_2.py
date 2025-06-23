import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the first erf: sqrt(3)/2
arg1 = mp.sqrt(3) / 2

# Compute the argument for the second erf: 1/(2*sqrt(3))
arg2 = 1 / (2 * mp.sqrt(3))

# Evaluate erf at the first argument
erf_val1 = mp.erf(arg1)

# Evaluate erf at the second argument
erf_val2 = mp.erf(arg2)

# Calculate the difference between the erf values
erf_diff = erf_val1 - erf_val2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * erf_diff

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))