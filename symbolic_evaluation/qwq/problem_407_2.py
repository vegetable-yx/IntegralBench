import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate sqrt(3) once for reuse
sqrt3 = mp.sqrt(3)

# Compute the arguments for the error functions
term1_arg = sqrt3 / 2
term2_arg = 1 / (2 * sqrt3)

# Evaluate the error function at each argument
erf1 = mp.erf(term1_arg)
erf2 = mp.erf(term2_arg)

# Calculate the difference between the two error function values
difference = erf1 - erf2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * difference

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))