import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(3) once for reuse
sqrt3 = mp.sqrt(3)

# Compute the arguments for the error functions
arg1 = sqrt3 / 2
arg2 = 1 / (2 * sqrt3)

# Evaluate the error function at each argument
erf_term1 = mp.erf(arg1)
erf_term2 = mp.erf(arg2)

# Compute the difference between the two error function terms
difference = erf_term1 - erf_term2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * difference

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))