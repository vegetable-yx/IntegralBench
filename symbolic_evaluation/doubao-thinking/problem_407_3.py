import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute square root of 3
sqrt3 = mp.sqrt(3)

# Calculate arguments for error functions
arg1 = sqrt3 / 2
arg2 = sqrt3 / 6

# Compute error function values
erf1 = mp.erf(arg1)
erf2 = mp.erf(arg2)

# Calculate the difference between error functions
erf_diff = erf1 - erf2

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * erf_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))