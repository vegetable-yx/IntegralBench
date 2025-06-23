import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for the first erf function: sqrt(3)/2
arg1 = mp.sqrt(3) / 2

# Calculate the argument for the second erf function: 1/(2*sqrt(3))
arg2 = 1 / (2 * mp.sqrt(3))

# Compute erf values for both arguments
erf_val1 = mp.erf(arg1)
erf_val2 = mp.erf(arg2)

# Calculate the difference between erf values
erf_diff = erf_val1 - erf_val2

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * erf_diff

# Print result with 10 decimal places
print(mp.nstr(result, n=10))